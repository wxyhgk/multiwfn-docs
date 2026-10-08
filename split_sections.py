#!/usr/bin/env python3
"""按书二级目录重切: sections/en + sections/zh (文件名 NN_slug, zh_前缀对应).
- 边界 = L2去重起点 + 前言3件(p1-2必读/p3-21 Linux/p22-30 Overview)
- 每文件恰一个 #: 页内22pt章标题降##, 文件头 prepend "# 节标题"
- 内容按页标记切片 (中英标记已1:1)
"""
import fitz, re, os, glob, pickle

BASE = "/Users/wxyhgk/Documents/Quamtum_Chemistry_md/Multiwfn"
d = fitz.open(os.path.join(BASE, "Multiwfn_manual_2026.10.1.pdf"))
toc = d.get_toc()

l2 = [(t[1].strip(), t[2]) for t in toc if t[0] == 2]
# 去重同页起点(保留首个标题, 记录合并)
seen, bounds = {}, []
for title, pg in l2:
    if pg not in seen:
        seen[pg] = title
        bounds.append([pg, title, [title]])
    else:
        bounds[-1][2].append(title)
# bounds: [start, first_title, [all_titles]]

front = [(1, "Must read", "必读"), (3, "Linux and Mac OS notes", "Linux 和 Mac 说明"), (22, "1 Overview", "1 总览")]
for pg, en, zh in front:
    bounds.append([pg, en, [en]])
bounds.sort()
N = len(d)
for i, b in enumerate(bounds):
    b.append(bounds[i+1][0] - 1 if i + 1 < len(bounds) else N)  # end
print("文件数:", len(bounds))

def slug(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:48].strip("-")
    return s or "section"

# 页内容字典
def pagedict(files):
    txt = ""
    for f in files:
        txt += open(f, encoding="utf-8").read() + "\n"
    parts = re.split(r"<!-- p\.(\d+) -->", txt)
    pg = {}
    for i in range(1, len(parts), 2):
        pg[int(parts[i])] = parts[i+1]
    return pg

en_pages = pagedict([os.path.join(BASE, "multiwfn_full.md")])
zh_files = sorted(glob.glob(os.path.join(BASE, "chapters/zh_*.md")))
zh_pages = pagedict(zh_files)
print("EN页:", len(en_pages), "ZH页:", len(zh_pages))

# ZH节标题: 按节号从译文里抓
zh_heads = {}
blob = "\n".join(open(f, encoding="utf-8").read() for f in zh_files)
for m in re.finditer(r"^#{1,3}\s+((?:\d+\.)*\d+|4\.A(?:\.\d+)*)\s+(.+)$", blob, re.M):
    zh_heads.setdefault(m.group(1).rstrip("."), m.group(2).strip())

used = set()
meta = []  # (fname, en_title, zh_title, start, end, parent_l1)
l1s = [(t[1].strip(), t[2]) for t in toc if t[0] == 1]
for idx, b in enumerate(bounds, 1):
    start, en_title, titles, end = b
    num = re.match(r"((?:\d+\.)*\d+|4\.A(?:\.\d+)*)", en_title)
    num = num.group(1).rstrip(".") if num else ""
    front_zh = {1: "必读", 3: "Linux 和 Mac 说明", 22: "1 总览"}
    zh_t = front_zh.get(start, zh_heads.get(num, ""))
    base = f"{idx:02d}_" + (slug(en_title) or f"p{start}")
    if base in used:
        base += f"-p{start}"
    used.add(base)
    cands = [t for t, p in l1s if p <= start]
    parent = cands[-1] if cands else "Front matter"
    meta.append({"file": base, "en": en_title, "zh": zh_t or en_title,
                 "zh_missing": not bool(zh_t), "start": start, "end": end,
                 "parent": parent, "num": num})
print("ZH标题缺失:", sum(1 for m in meta if m["zh_missing"]))
pickle.dump(meta, open("/tmp/sec_meta.pkl", "wb"))

for lang, pages in (("en", en_pages), ("zh", zh_pages)):
    outdir = os.path.join(BASE, "sections", lang)
    os.makedirs(outdir, exist_ok=True)
    for m in meta:
        chunks = []
        for p in range(m["start"], m["end"] + 1):
            if p in pages:
                chunks.append(f"<!-- p.{p} -->\n" + pages[p])
        body = "".join(chunks)
        body = body.replace("](../mw_imgs/", "](../imgs/").replace("](mw_imgs/", "](../imgs/")
        title = m["en"] if lang == "en" else m["zh"]
        # 页内22pt章标题降级, 文件头单H1
        body = re.sub(r"(?m)^# (?!Multiwfn：)", r"## ", body)
        body = re.sub(r"(?m)^# Multiwfn：.*$", r"## Multiwfn", body)
        head = f"# {title}\n\n> Multiwfn manual, p.{m['start']}–{m['end']}."
        if lang == "zh":
            head += "英文原文见同名 English 章节。"
        head += " Images: `../imgs/`.\n\n---\n\n"
        fn = ("zh_" if lang == "zh" else "") + m["file"] + ".md"
        open(os.path.join(outdir, fn), "w", encoding="utf-8").write(head + body.strip() + "\n")
print("sections written")
