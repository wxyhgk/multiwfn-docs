#!/usr/bin/env python3
"""第二轮: 垃圾文本行回填 OCR LaTeX + PUA希腊字母映射.
1) 手工精确替换 (p343 x7, p60 x3)
2) 自动: PUA>=3 或沙拉标记 的文本行, 按token交叠匹配同页OCR数学, 整行/保留label替换
3) PUA映射 (Symbol字体): 希腊小写全套 + ΔΘ×√·∂ + •, 跳过代码围栏
"""
import json, re, os, unicodedata

BASE = "/Users/wxyhgk/Documents/Quamtum_Chemistry_md/Multiwfn"
from merge_formulas import (CHUNKS, extract_math, garbage, fix, tokens_of_latex,
                            tokens_of_raw, GREEK)

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

# ---------- 2) 自动回填 ----------
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
    if not (n_pua >= 3 or (salad and n_pua >= 1)):
        continue
    if len(ENW.findall(ln)) >= 10 and n_pua <= 6 and not ("=−−" in ln or "()(" in ln):
        continue  # 散文为主, 只做映射
    pno = page_of(i)
    page_md = ocr_pages.get(pno)
    if page_md is None:
        report["kept"].append({"line": i + 1, "page": pno, "why": "no-ocr"})
        continue
    cands = []
    for latex, disp in extract_math(page_md):
        if not disp:
            continue  # 文本行回填只用显示公式, 行内不碰(防 ω_cubic 这类误伤)
        if garbage(latex):
            continue
        # 文件名/单位/纯文本式候选一律不要
        if re.search(r"\\_|\.vmd|\.txt|\.png|\.cub|\.mwfn|PNAS|esu", latex):
            continue
        cands.append({"latex": fix(latex), "toks": tokens_of_latex(latex)})
    rt = tokens_of_raw(ln)
    best, best_sc = None, 0
    for cd in cands:
        sc = sum(2 if t in GREEK else 1 for t in (rt & cd["toks"]))
        if sc > best_sc:
            best, best_sc = cd, sc
    if best is not None and best_sc >= 4:
        m = re.match(r"^(\d+\s+[A-Z].{2,80}?:)\s*(.+)$", s)
        if m and len(m.group(2)) > 10:
            lines[i] = f"{m.group(1)} $${best['latex']}$$"
        else:
            lines[i] = f"$${best['latex']}$$"
        report["replaced"].append({"line": i + 1, "page": pno, "score": best_sc,
                                   "latex": best["latex"][:100]})
    else:
        report["kept"].append({"line": i + 1, "page": pno, "why": f"score={best_sc}",
                               "text": ln[:80]})

print("auto replaced:", len(report["replaced"]), "kept:", len(report["kept"]))

# ---------- 3) PUA 映射 ----------
PUAMAP = {0xF061: "α", 0xF062: "β", 0xF063: "χ", 0xF064: "δ", 0xF065: "ε",
          0xF066: "φ", 0xF067: "γ", 0xF068: "η", 0xF069: "ι", 0xF06A: "φ",
          0xF06B: "κ", 0xF06C: "λ", 0xF06D: "μ", 0xF06E: "ν", 0xF06F: "ο",
          0xF070: "π", 0xF071: "θ", 0xF072: "ρ", 0xF073: "σ", 0xF074: "τ",
          0xF075: "υ", 0xF076: "ϖ", 0xF077: "ω", 0xF078: "ξ", 0xF079: "ψ",
          0xF07A: "ζ"}
PUAMAP.update({0xF09F: "•", 0xF0A8: "•", 0xF044: "Δ", 0xF051: "Θ", 0xF0B4: "×",
               0xF0D6: "√", 0xF0D7: "·", 0xF0B6: "∂"})
# φ变体 F06A 在上面已是 φ; ιF069 ✓; 修正: q->θ? Symbol q=θ ✓(上面q对θ)
n_map = 0
in_code = False
for i, ln in enumerate(lines):
    if ln.strip().startswith("```"):
        in_code = not in_code
        continue
    if in_code:
        continue
    out = []
    for ch in ln:
        o = ord(ch)
        if o in PUAMAP:
            out.append(PUAMAP[o])
            n_map += 1
        else:
            out.append(ch)
    lines[i] = "".join(out)
print("pua mapped chars:", n_map)

open(path, "w", encoding="utf-8").write("\n".join(lines))
json.dump(report, open(os.path.join(BASE, "garbage_merge_report.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
for k in report["kept"][:20]:
    print(" KEPT L%d p%s %s %s" % (k["line"], k["page"], k["why"], k.get("text", "")[:60]))
