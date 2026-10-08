#!/usr/bin/env python3
"""Multiwfn manual -> Markdown 样张转换 (10页代表页).
重点: 代码围栏 / 公式图片兜底 / 标题重映射 / 页眉页脚过滤.
用法: python3 convert_mw_sample.py
输出: sample_mw.md + sample_imgs/
"""
import fitz, re, os

SRC = "Multiwfn_manual_2026.10.1.pdf"
OUT_MD = "sample_mw.md"
IMG_DIR = "sample_imgs"
# 代表页(0-based): 章首页/安装/公式重灾区/代码重灾区/周期体系
PAGES = [21, 30, 31, 40, 50, 53, 69, 600, 601, 800]

os.makedirs(IMG_DIR, exist_ok=True)
doc = fitz.open(SRC)

def clean(t):
    return t.replace("\u00a0", " ")

def block_text(b):
    return clean("".join(s["text"] for l in b["lines"] for s in l["spans"]))

def block_fonts(b):
    return [(round(s["size"], 1), s["font"], s.get("color", 0), s["text"])
            for l in b["lines"] for s in l["spans"]]

def is_mono_block(b):
    spans = [s for l in b["lines"] for s in l["spans"]]
    if not spans:
        return False
    mono = sum(1 for s in spans if "LucidaConsole" in s["font"])
    return mono / len(spans) > 0.6

def is_formula_frag(b, txt):
    """独立显示公式碎片: 短 + 数学字体主导, 或含大号Symbol; 排除正常句子."""
    if len(txt) > 120:
        return False
    spans = [s for l in b["lines"] for s in l["spans"]]
    if not spans:
        return False
    mathn = sum(len(s["text"]) for s in spans if "Symbol" in s["font"] or "Cambria" in s["font"])
    total = sum(len(s["text"]) for s in spans)
    if total == 0:
        return False
    big_sym = any(("Symbol" in s["font"] or "Cambria" in s["font"]) and s["size"] >= 12 for s in spans)
    # 正常英文句子: 含多个常见英文词且以标点结尾 -> 不是公式
    words = re.findall(r"[A-Za-z]{3,}", txt)
    if len(words) >= 6 and mathn / max(total, 1) < 0.25 and not big_sym:
        return False
    if big_sym and len(txt.strip()) < 60:
        return True
    if mathn / total > 0.4 and len(txt.strip()) < 80:
        return True
    return False

md = []
md.append("# Multiwfn 样张（10页）\n\n")
formula_count = 0
code_count = 0
img_count = 0

for pno in PAGES:
    page = doc[pno]
    md.append(f"\n<!-- p.{pno+1} -->\n")
    md.append(f"\n**（原书 p.{pno+1}）**\n")

    d = page.get_text("dict")
    blocks = [b for b in d["blocks"] if b["type"] == 0]
    blocks.sort(key=lambda b: (round(b["bbox"][1]), b["bbox"][0]))

    # 表格预检
    table_bboxes = []
    try:
        for t in page.find_tables():
            try:
                data = t.extract()
            except Exception:
                continue
            if not data or len(data) < 2:
                continue
            nonEmpty = sum(1 for row in data for c in row if str(c).strip())
            if nonEmpty < 4:
                continue
            table_bboxes.append(fitz.Rect(t.bbox))
    except Exception:
        pass

    def in_table(rect):
        cx = (rect.x0 + rect.x1) / 2
        cy = (rect.y0 + rect.y1) / 2
        return any(tb.x0 - 2 <= cx <= tb.x1 + 2 and tb.y0 - 2 <= cy <= tb.y1 + 2
                   for tb in table_bboxes)

    # 先标出公式碎片, 合并成组
    frag_idx = set()
    for i, b in enumerate(blocks):
        if b["bbox"][1] < 68 or b["bbox"][1] > 758:
            continue
        t = block_text(b).strip()
        if t and is_formula_frag(b, t):
            frag_idx.add(i)
    # 按y分组
    groups = []
    for i in sorted(frag_idx):
        if groups and blocks[i]["bbox"][1] - blocks[groups[-1][-1]]["bbox"][3] < 40:
            groups[-1].append(i)
        else:
            groups.append([i])

    formula_here = {}
    for g in groups:
        x0 = min(blocks[i]["bbox"][0] for i in g) - 6
        x1 = max(blocks[i]["bbox"][2] for i in g) + 6
        y0 = min(blocks[i]["bbox"][1] for i in g) - 4
        y1 = max(blocks[i]["bbox"][3] for i in g) + 4
        formula_count += 1
        fname = f"formula_p{pno+1}_{formula_count:02d}.png"
        try:
            pix = page.get_pixmap(dpi=150, clip=fitz.Rect(x0, y0, x1, y1))
            pix.save(os.path.join(IMG_DIR, fname))
            formula_here[g[0]] = (fname, g)
        except Exception as e:
            formula_here[g[0]] = (None, g)
    skip_idx = set()
    for g in groups:
        for i in g[1:]:
            skip_idx.add(i)

    # 普通图片
    page_imgs = []
    for img in page.get_images(full=True):
        xref = img[0]
        try:
            pix = fitz.Pixmap(doc, xref)
        except Exception:
            continue
        if pix.n - pix.alpha > 3:
            try:
                pix = fitz.Pixmap(fitz.csRGB, pix)
            except Exception:
                continue
        if pix.w < 80 or pix.h < 25:
            continue
        img_count += 1
        fname = f"p{pno+1}_{img_count:03d}.png"
        try:
            pix.save(os.path.join(IMG_DIR, fname))
            try:
                bb = page.get_image_bbox(img)
                y = bb[0].y0 if isinstance(bb, list) else bb.y0
            except Exception:
                y = 1e9
            page_imgs.append((y, fname))
        except Exception:
            continue
    page_imgs.sort()

    code_buf = []

    def flush_code():
        if not code_buf:
            return
        globals()['code_count'] += 1
        # 去掉每行尾部空格, 保留前导空格; 头尾空行去掉
        lines = [ln.rstrip() for ln in code_buf]
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        md.append("\n```text\n" + "\n".join(lines) + "\n```\n")
        code_buf.clear()

    for i, b in enumerate(blocks):
        y0 = b["bbox"][1]
        if y0 < 68 or y0 > 758:  # 页眉/页脚
            continue
        if i in skip_idx:
            continue
        rect = fitz.Rect(b["bbox"])
        txt = block_text(b)
        if not txt.strip():
            continue
        # 公式组起点 -> 嵌图片
        if i in formula_here:
            flush_code()
            fname, g = formula_here[i]
            raw = " ⏎ ".join(block_text(blocks[j]).strip() for j in g)[:300]
            if fname:
                md.append(f"\n![](../{IMG_DIR}/{fname})\n")
                md.append(f"\n<!-- formula-raw p.{pno+1}: {clean(raw)} -->\n")
            else:
                md.append(f"\n> [公式渲染失败，原文：{clean(raw)}]\n")
            continue
        # 等宽代码
        if is_mono_block(b):
            # 保留行内换行与前导空格
            for l in b["lines"]:
                segs = sorted(l["spans"], key=lambda s: s["bbox"][0])
                line = "".join(s["text"] for s in segs).replace("\u00a0", " ")
                code_buf.append(line)
            continue
        else:
            flush_code()
        if in_table(rect):
            continue  # 表格后统一输出
        # Usage 红字块
        if txt.strip().startswith("======="):
            body = txt.strip()
            body = re.sub(r"={3,}\s*Usage\s*={3,}", "", body).strip()
            body = re.sub(r"\s+", " ", body)
            body = body.replace("settings.ini", "`settings.ini`")
            md.append(f"\n> **Usage** — {body}\n")
            continue
        # 标题判定: 单行全粗体
        lines = b["lines"]
        if len(lines) == 1:
            segs = [(s, clean(s["text"])) for s in lines[0]["spans"] if s["text"].strip()]
            if segs:
                sizes = {round(s["size"]) for s, _ in segs}
                fonts = {s["font"] for s, _ in segs}
                t = "".join(t for _, t in segs).strip()
                is_bold = all("Bold" in f for f in fonts)
                if len(sizes) == 1 and is_bold and len(t) >= 2:
                    sz = sizes.pop()
                    if sz >= 22 and len(t) < 120:
                        md.append(f"\n# {t}\n")
                        continue
                    if sz >= 16 and len(t) < 150:
                        md.append(f"\n## {t}\n")
                        continue
                    if sz >= 13 and len(t) < 160:
                        md.append(f"\n### {t}\n")
                        continue
        # 段首 12pt Bold run-in 小标题
        first = b["lines"][0]["spans"][0] if b["lines"][0]["spans"] else None
        para = None
        if first and round(first["size"]) == 12 and "Bold" in first["font"]:
            lead = clean(first["text"]).strip()
            rest = txt[len(first["text"]):].strip()
            rest = re.sub(r"\s+", " ", rest)
            rest = rest.replace("settings.ini", "`settings.ini`")
            md.append(f"\n**{lead}** {rest}\n")
            continue
        # 普通段落: join, bullet
        raw_lines = []
        for l in b["lines"]:
            lt = clean("".join(s["text"] for s in l["spans"])).strip()
            if lt:
                raw_lines.append(lt)
        buf = ""
        for s in raw_lines:
            if s.startswith("•"):
                if buf.strip():
                    md.append(re.sub(r"\s+", " ", buf.strip()) + "\n")
                    buf = ""
                md.append("- " + re.sub(r"\s+", " ", s[1:].strip()) + "\n")
                continue
            if buf == "":
                buf = s
            else:
                buf = buf[:-1] + s if buf.endswith("-") and not buf.endswith(" -") else buf + " " + s
        if buf.strip():
            p = re.sub(r"\s+", " ", buf.strip())
            p = p.replace("settings.ini", "`settings.ini`")
            if re.search(r"\.{6,}", p) and len(p) > 100:
                continue
            md.append(p + "\n")
    flush_code()

    # 表格输出(跳过与代码/公式区重叠的)
    try:
        for t in page.find_tables():
            try:
                data = t.extract()
            except Exception:
                continue
            if not data or len(data) < 2:
                continue
            r = fitz.Rect(t.bbox)
            # 与等宽/公式区重叠则跳过(终端输出不是真表格)
            overlap = False
            for b in blocks:
                if is_mono_block(b) and fitz.Rect(b["bbox"]).intersects(r):
                    overlap = True
                    break
            if overlap:
                continue
            nonEmpty = sum(1 for row in data for c in row if str(c).strip())
            if nonEmpty < 4:
                continue
            ncol = max(len(x) for x in data)
            rows = []
            for row in data:
                cells = [clean(str(c or "")).replace("|", "\\|").replace("\n", "<br/>").strip()
                         for c in row] + [""] * (ncol - len(row))
                rows.append("| " + " | ".join(cells) + " |")
            md.append("\n" + rows[0] + "\n| " + " | ".join(["---"] * ncol) + " |\n"
                      + "\n".join(rows[1:]) + "\n")
    except Exception:
        pass
    for _, fname in page_imgs:
        md.append(f"\n![](../{IMG_DIR}/{fname})\n")

with open(OUT_MD, "w", encoding="utf-8") as f:
    f.writelines(md)
print(f"done: {OUT_MD}, formula={formula_count}, codeblocks={code_count}, images={img_count}")
