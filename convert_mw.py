#!/usr/bin/env python3
"""Multiwfn manual -> Markdown 全量转换.
- 标题: 22pt Bold=>#, 16pt=>##, 13pt=>###
- 代码: LucidaConsole 连续块合并为 ```text 围栏(保留换行/缩进)
- 公式: 按y-band判定显示公式(短+数学字体主导+无英文句子词), 整band渲染成图片;
        行内公式保留 Unicode 不动
- Usage红字 => 引用块; settings.ini => code ticks; • => -
- 页眉(y<68)/页脚(y>758)丢弃; 等宽区排除在表格识别外
用法: python3 convert_mw.py  (输出 multiwfn_full.md + mw_imgs/)
"""
import fitz, re, os, sys, json, unicodedata

SRC = "Multiwfn_manual_2026.10.1.pdf"
OUT_MD = "multiwfn_full.md"
IMG_DIR = "mw_imgs"
FUSE_DIR = "/Users/wxyhgk/Documents/Quamtum_Chemistry_md/doc-fuse/work"
os.makedirs(IMG_DIR, exist_ok=True)
doc = fitz.open(SRC)
SPLIT_START = [(1, "01"), (31, "02"), (77, "03"), (134, "04"), (183, "05"),
    (222, "06"), (257, "07"), (310, "08"), (354, "09"), (409, "10"),
    (458, "11"), (505, "12"), (563, "13"), (617, "14"), (655, "15"),
    (694, "16"), (731, "17"), (804, "18"), (873, "19"), (931, "20a"),
    (961, "20b"), (990, "21"), (1031, "22"), (1084, "23")]
_SYM_MAP = {0x41:'Α',0x42:'Β',0x47:'Γ',0x44:'Δ',0x45:'Ε',0x5A:'Ζ',0x48:'Η',
    0x51:'Θ',0x49:'Ι',0x4B:'Κ',0x4C:'Λ',0x4D:'Μ',0x4E:'Ν',0x58:'Ξ',0x4F:'Ο',
    0x50:'Π',0x52:'Ρ',0x53:'Σ',0x54:'Τ',0x55:'Υ',0x46:'Φ',0x43:'Χ',0x59:'Ψ',
    0x57:'Ω',0x61:'α',0x62:'β',0x67:'γ',0x64:'δ',0x65:'ε',0x7A:'ζ',0x68:'η',
    0x71:'θ',0x69:'ι',0x6B:'κ',0x6C:'λ',0x6D:'μ',0x6E:'ν',0x78:'ξ',0x6F:'ο',
    0x70:'π',0x72:'ρ',0x73:'σ',0x74:'τ',0x75:'υ',0x66:'φ',0x63:'χ',0x79:'ψ',
    0x77:'ω',0xE5:'∑',0xD5:'∏',0xF2:'∫',0xB6:'∂',0xD1:'∇',0xCE:'∈',0xB1:'±',
    0xB4:'×',0xB8:'÷',0xA3:'≤',0xB3:'≥',0xB9:'≠',0xBB:'↔',0xAC:'→',0xAB:'⇒',
    0xA5:'∞',0xD6:'√',0x2D:'−'}

def _fuse_dec(c):
    _o = ord(c)
    if 0xF020 <= _o <= 0xF0FF:
        return _SYM_MAP.get(_o - 0xF000, c)
    return c

def _fuse_norm(s):
    return re.sub(r"\s+", "", unicodedata.normalize("NFKD", "".join(_fuse_dec(c) for c in s)))
FUSE = {}  # 全局页 -> [(seg_norm, seg, latex)]
try:
    _starts = [s for s, _ in SPLIT_START] + [1162]
    for _si, (_st, _tag) in enumerate(SPLIT_START):
        _rp = os.path.join(FUSE_DIR, f"report_{_tag}.json")
        if not os.path.exists(_rp):
            continue
        _d = json.load(open(_rp, encoding="utf-8"))
        for _pg in _d["pages"]:
            _gp = _st + _pg["page"] - 1
            if _gp >= _starts[_si + 1]:
                continue
            _hits = [(_fuse_norm(h["seg"]), h["seg"], h["latex"])
                     for h in _pg["hits"]]
            _hits.sort(key=lambda x: -len(x[0]))
            if _hits:
                FUSE[_gp] = _hits
except Exception as _e:
    print(f"fuse: load failed ({_e}), skip inline fusion", flush=True)
    FUSE = {}

def apply_inline(pno, text):
    """该页替换表应用: 归一化子串定位, 映射回原文替换为$latex$."""
    hits = FUSE.get(pno + 1)
    if not hits or "$" in text:
        return text, 0
    comp_chars = []
    idx = []  # compact索引 -> 原文索引(NFKD展开对齐)
    for _k, _ch in enumerate(text):
        for _c in unicodedata.normalize("NFKD", _fuse_dec(_ch)):
            if not _c.isspace():
                comp_chars.append(_c)
                idx.append(_k)
    compact = "".join(comp_chars)
    out = text
    n = 0
    _off = 0  # 已替换导致的原文偏移(重建方式避免偏移: 从后往前)
    reps = []
    for _sn, _seg, _lx in hits:
        _at = compact.find(_sn)
        if _at < 0:
            continue
        _s0 = idx[_at]
        _s1 = idx[_at + len(_sn) - 1] + 1
        reps.append((_s0, _s1, f"${_lx}$"))
    # 去重叠(保留先出现的长段) + 从后往前替换
    reps.sort()
    _keep = []
    _last = -1
    for _s0, _s1, _r in reps:
        if _s0 < _last:
            continue
        _keep.append((_s0, _s1, _r))
        _last = _s1
    for _s0, _s1, _r in reversed(_keep):
        out = out[:_s0] + _r + out[_s1:]
        n += 1
    return out, n

EN_WORDS = re.compile(r"[A-Za-z]{3,}")

def clean(t):
    return t.replace("\u00a0", " ")

def block_text(b):
    return clean("".join(s["text"] for l in b["lines"] for s in l["spans"]))

def is_mono_block(b):
    spans = [s for l in b["lines"] for s in l["spans"]]
    if not spans:
        return False
    mono = sum(1 for s in spans if "LucidaConsole" in s["font"])
    return mono / len(spans) > 0.6

def band_math_info(band_blocks):
    n_math = n_tot = 0
    big_sym = False
    for b in band_blocks:
        for l in b["lines"]:
            for s in l["spans"]:
                t = s["text"]
                n_tot += len(t)
                if "Symbol" in s["font"] or "Cambria" in s["font"]:
                    n_math += len(t)
                if ("Symbol" in s["font"] or "Cambria" in s["font"]) and s["size"] >= 12:
                    big_sym = True
    return n_math, n_tot, big_sym

md = []
md.append("# Multiwfn 官方手册（PDF 转 Markdown）\n")
md.append(f"> 来源：`{SRC}`，共 {len(doc)} 页，由 PyMuPDF 直接提取（可复制文本）。"
          "等宽终端输出保留为代码块，独立显示公式渲染为图片，行内公式保留原文字符。\n")
md.append("## 目录（来自 PDF 书签）\n")
for level, title, pageno in doc.get_toc():
    indent = "  " * (level - 1)
    md.append(f"{indent}- {title}（p.{pageno}）\n")
md.append("\n---\n")

formula_count = 0
code_count = 0
img_count = 0

for pno in range(len(doc)):
    page = doc[pno]
    d = page.get_text("dict")
    blocks = [b for b in d["blocks"] if b["type"] == 0
              and b["bbox"][1] >= 68 and b["bbox"][1] <= 758]
    tb = block_text({"lines": [l for b in blocks for l in b["lines"]]}) if False else ""
    blocks.sort(key=lambda b: (round(b["bbox"][1]), b["bbox"][0]))
    if not blocks:
        continue

    # ---- 按y-band聚类(垂直重叠即同band) ----
    bands = []  # list of list[block_idx]
    for i, b in enumerate(blocks):
        placed = False
        for band in bands:
            b0 = blocks[band[0]]
            # y区间重叠(容差3pt)则同band
            lo = max(b["bbox"][1], b0["bbox"][1])
            hi = min(b["bbox"][3], b0["bbox"][3])
            # 用band整体y范围判断
            ys0 = min(blocks[j]["bbox"][1] for j in band)
            ys1 = max(blocks[j]["bbox"][3] for j in band)
            if not (b["bbox"][1] > ys1 - 3 or b["bbox"][3] < ys0 + 3):
                band.append(i)
                placed = True
                break
        if not placed:
            bands.append([i])
    bands.sort(key=lambda band: min(blocks[j]["bbox"][1] for j in band))

    is_formula_band = {}
    for bi, band in enumerate(bands):
        txt = " ".join(block_text(blocks[j]).strip() for j in band)
        txt_nospace = txt.replace(" ", "")
        n_math, n_tot, big_sym = band_math_info([blocks[j] for j in band])
        words = EN_WORDS.findall(txt)
        # 显示公式band: 短(<110字符)、含数学字体、大符号或数学占比高、无英文句子词
        if len(txt) <= 110 and n_tot > 0 and (big_sym or n_math / n_tot > 0.35) and len(words) <= 2:
            is_formula_band[bi] = True
        # 独立的短英文标题行(如 "Postscript:"开头?)不算; 带4个以上英文词一定是段落
        if len(words) >= 4:
            is_formula_band[bi] = False

    # 合并连续公式band(y-gap<28)为一组
    fgroups = []
    for bi, band in enumerate(bands):
        if not is_formula_band.get(bi):
            continue
        if fgroups:
            prev = bands[fgroups[-1][-1]]
            yprev1 = max(blocks[j]["bbox"][3] for j in prev)
            ycur0 = min(blocks[j]["bbox"][1] for j in band)
            if ycur0 - yprev1 < 28:
                fgroups[-1].append(bi)
                continue
        fgroups.append([bi])

    formula_bands = set(bi for g in fgroups for bi in g)
    formula_start = {g[0]: g for g in fgroups}

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
            if sum(1 for row in data for c in row if str(c).strip()) < 4:
                continue
            table_bboxes.append(fitz.Rect(t.bbox))
    except Exception:
        pass

    def in_table(rect):
        cx = (rect.x0 + rect.x1) / 2
        cy = (rect.y0 + rect.y1) / 2
        return any(tb.x0 - 2 <= cx <= tb.x1 + 2 and tb.y0 - 2 <= cy <= tb.y1 + 2
                   for tb in table_bboxes)

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

    page_lines = []
    code_buf = []

    def flush_code():
        if not code_buf:
            return
        globals()["code_count"] += 1
        lines = [ln.rstrip() for ln in code_buf]
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        page_lines.append(("code", "\n```text\n" + "\n".join(lines) + "\n```\n"))
        code_buf.clear()

    for bi, band in enumerate(bands):
        if bi in formula_bands and bi not in formula_start:
            continue  # 已合并到组起点
        if bi in formula_start:
            flush_code()
            g = formula_start[bi]
            xs0 = min(blocks[j]["bbox"][0] for bbi in g for j in bands[bbi]) - 6
            xs1 = max(blocks[j]["bbox"][2] for bbi in g for j in bands[bbi]) + 6
            ys0 = min(blocks[j]["bbox"][1] for bbi in g for j in bands[bbi]) - 4
            ys1 = max(blocks[j]["bbox"][3] for bbi in g for j in bands[bbi]) + 4
            globals()["formula_count"] += 1
            fname = f"formula_p{pno+1}_{formula_count:03d}.png"
            try:
                pix = page.get_pixmap(dpi=150, clip=fitz.Rect(xs0, ys0, xs1, ys1))
                pix.save(os.path.join(IMG_DIR, fname))
                raw = " ⏎ ".join(block_text(blocks[j]).strip()
                                  for bbi in g for j in bands[bbi])[:200]
                page_lines.append(("img", f"\n![]({IMG_DIR}/{fname})\n"
                                          f"\n<!-- formula-raw p.{pno+1}: {clean(raw)} -->\n"))
            except Exception:
                pass
            continue
        # band内全是等宽?
        band_blocks = [blocks[j] for j in band]
        if all(is_mono_block(b) for b in band_blocks):
            for b in sorted(band_blocks, key=lambda b: b["bbox"][0]):
                for l in b["lines"]:
                    segs = sorted(l["spans"], key=lambda s: s["bbox"][0])
                    code_buf.append("".join(s["text"] for s in segs).replace("\u00a0", " "))
            continue
        flush_code()
        # 表格区跳过(后统一输出)
        if all(in_table(fitz.Rect(b["bbox"])) for b in band_blocks):
            continue
        txt = " ".join(block_text(b).strip() for b in
                       sorted(band_blocks, key=lambda b: b["bbox"][0]))
        if not txt:
            continue
        if txt.startswith("======="):
            body = re.sub(r"={3,}\s*Usage\s*={3,}", "", txt).strip()
            body = re.sub(r"\s+", " ", body).replace("settings.ini", "`settings.ini`")
            body, _nc = apply_inline(pno, body)
            globals()["inline_count"] = globals().get("inline_count", 0) + _nc
            page_lines.append(("p", f"\n> **Usage** — {body}\n"))
            continue
        if len(band) == 1:
            b = band_blocks[0]
            if len(b["lines"]) == 1:
                segs = [(s, clean(s["text"])) for s in b["lines"][0]["spans"] if s["text"].strip()]
                if segs:
                    sizes = {round(s["size"]) for s, _ in segs}
                    fonts = {s["font"] for s, _ in segs}
                    t = "".join(t for _, t in segs).strip()
                    if len(sizes) == 1 and all("Bold" in f for f in fonts) and 2 <= len(t):
                        sz = sizes.pop()
                        if sz >= 22 and len(t) < 120:
                            page_lines.append(("h", f"\n# {t}\n"))
                            continue
                        if sz >= 16 and len(t) < 150:
                            page_lines.append(("h", f"\n## {t}\n"))
                            continue
                        if sz >= 13 and len(t) < 160:
                            page_lines.append(("h", f"\n### {t}\n"))
                            continue
        # 段首12pt run-in小标题
        f0 = band_blocks[0]["lines"][0]["spans"][0] if band_blocks[0]["lines"][0]["spans"] else None
        if f0 is not None and round(f0["size"]) == 12 and "Bold" in f0["font"]:
            lead = clean(f0["text"]).strip()
            rest = txt[len(f0["text"]):].strip() if txt.startswith(lead) else txt
            rest = re.sub(r"\s+", " ", rest).replace("settings.ini", "`settings.ini`")
            rest, _nc = apply_inline(pno, rest)
            globals()["inline_count"] = globals().get("inline_count", 0) + _nc
            page_lines.append(("p", f"\n**{lead}** {rest}\n"))
            continue
        # 普通段落
        if txt.startswith("•"):
            _t = re.sub(r"\s+", " ", txt[1:].strip())
            _t, _nc = apply_inline(pno, _t)
            globals()["inline_count"] = globals().get("inline_count", 0) + _nc
            page_lines.append(("p", "- " + _t + "\n"))
            continue
        p = re.sub(r"\s+", " ", txt).replace("settings.ini", "`settings.ini`")
        if re.search(r"\.{6,}", p) and len(p) > 100:
            continue
        p, _nc = apply_inline(pno, p)
        globals()["inline_count"] = globals().get("inline_count", 0) + _nc
        page_lines.append(("p", p + "\n"))
    flush_code()

    if not page_lines and not table_bboxes and not page_imgs:
        continue
    md.append(f"\n<!-- p.{pno+1} -->\n")
    for _, t in page_lines:
        md.append(t + "\n")
    try:
        for t in page.find_tables():
            try:
                data = t.extract()
            except Exception:
                continue
            if not data or len(data) < 2:
                continue
            r = fitz.Rect(t.bbox)
            if any(is_mono_block(b) and fitz.Rect(b["bbox"]).intersects(r) for b in blocks):
                continue
            if sum(1 for row in data for c in row if str(c).strip()) < 4:
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
        md.append(f"\n![]({IMG_DIR}/{fname})\n")
    if (pno + 1) % 200 == 0:
        print(f"... {pno+1}/{len(doc)} pages", flush=True)

with open(OUT_MD, "w", encoding="utf-8") as f:
    f.writelines(md)
print(f"done: {OUT_MD}, formula={formula_count}, codeblocks={code_count}, images={img_count}, inline={globals().get('inline_count', 0)}")
