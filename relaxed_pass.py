#!/usr/bin/env python3
"""宽松二扫: 残留垃圾文本行, threshold 3 + 至少2个希腊/符号token才换.
只用显示公式候选. 结果记入 relaxed_report.json 供审计."""
import json, re, os
from merge_formulas import (CHUNKS, extract_math, garbage, fix, tokens_of_latex,
                            tokens_of_raw, GREEK)

BASE = "/Users/wxyhgk/Documents/Quamtum_Chemistry_md/Multiwfn"
ocr_pages = {}
for start, name in CHUNKS:
    p = os.path.join(BASE, f"ocr_out/{name}.json")
    if not os.path.exists(p):
        continue
    d = json.load(open(p, encoding="utf-8"))
    for i, pg in enumerate(d["pages"]):
        ocr_pages[start + i] = pg["markdownText"]

path = os.path.join(BASE, "multiwfn_full.md")
lines = open(path, encoding="utf-8").read().split("\n")

def page_of(idx):
    for j in range(idx, -1, -1):
        m = re.match(r"<!-- p\.(\d+) -->", lines[j])
        if m:
            return int(m.group(1))
    return None

ENW = re.compile(r"[A-Za-z]{3,}")
report = {"replaced": [], "kept": []}
in_code = False
for i, ln in enumerate(lines):
    s = ln.strip()
    if s.startswith("```"):
        in_code = not in_code
        continue
    if in_code or not s:
        continue
    if s.startswith(("<!--", "|", "!", "#", ">", "$$", "-", "$")):
        continue
    if "formula-ocr" in ln:
        continue
    n_pua = len(re.findall(r"[\ue000-\uf8ff]", ln))
    salad = ("=−−" in ln or "=−" in ln or "()(" in ln)
    if not (n_pua >= 2 or (salad and n_pua >= 1)):
        continue
    if len(ENW.findall(ln)) >= 10 and n_pua <= 6 and "=−−" not in ln and "()(" not in ln:
        continue
    pno = page_of(i)
    page_md = ocr_pages.get(pno)
    if page_md is None:
        report["kept"].append({"line": i + 1, "page": pno, "why": "no-ocr"})
        continue
    cands = []
    for latex, disp in extract_math(page_md):
        if not disp or garbage(latex):
            continue
        if re.search(r"\\_|\.vmd|\.txt|\.png|\.cub|\.mwfn|PNAS|esu", latex):
            continue
        cands.append({"latex": fix(latex), "toks": tokens_of_latex(latex)})
    rt = tokens_of_raw(ln)
    import unicodedata as _ud
    rt_acr = set(re.findall(r"[A-Z]{2,}", _ud.normalize("NFKD", ln)))
    best, best_sc, best_gr, best_acr = None, 0, 0, 0
    for cd in cands:
        inter = rt & cd["toks"]
        gr = sum(1 for t in inter if t in GREEK)
        sc = sum(2 if t in GREEK else 1 for t in inter)
        cd_acr = set(re.findall(r"[A-Z]{2,}", re.sub(r"\\[a-zA-Z]+", " ", cd["latex"])))
        acr = len(rt_acr & cd_acr)
        if sc > best_sc:
            best, best_sc, best_gr = cd, sc, gr
            best_acr = acr
    if best is not None and ((best_sc >= 3 and best_gr >= 2) or (best_sc >= 5 and best_acr >= 1)):
        m = re.match(r"^(\d+\s+[A-Z].{2,80}?:)\s*(.+)$", s)
        if m and len(m.group(2)) > 10:
            lines[i] = f"{m.group(1)} $${best['latex']}$$"
        else:
            lines[i] = f"$${best['latex']}$$"
        report["replaced"].append({"line": i + 1, "page": pno, "score": best_sc, "acr": best_acr,
                                   "latex": best["latex"][:100]})
    else:
        report["kept"].append({"line": i + 1, "page": pno, "why": f"score={best_sc},gr={best_gr}",
                               "text": ln[:80]})

open(path, "w", encoding="utf-8").write("\n".join(lines))
json.dump(report, open(os.path.join(BASE, "relaxed_report.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("relaxed replaced:", len(report["replaced"]), "kept:", len(report["kept"]))
for k in report["kept"]:
    print(" KEPT L%d p%s %s %s" % (k["line"], k["page"], k["why"], k.get("text", "")[:60]))
