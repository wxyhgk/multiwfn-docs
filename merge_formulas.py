#!/usr/bin/env python3
"""把 OCR JSON 里的公式 LaTeX 按内容匹配回填到 multiwfn_full.md 的公式图片位置.
- 只替换显示公式图片, 正文(命令/参数/结构)保持我们自己的文本
- 垃圾屏蔽: □ / \text{英文} / 纯选项列表 / 英文句子词
- 匹配不上则保留原图片; PNG 全部保留备查
用法: python3 merge_formulas.py
"""
import json, re, os, unicodedata

BASE = "/Users/wxyhgk/Documents/Quamtum_Chemistry_md/Multiwfn"
CHUNKS = [(1, "01_front_overview_p1-30"), (31, "02_general_info_p31-76"),
          (77, "03_func_3.2-3.9_p77-133"), (134, "04_func_3.10-3.13_p134-182"),
          (183, "05_func_3.14-3.17_p183-221"), (222, "06_func_3.18-3.20_p222-256"),
          (257, "07_func_3.21-3.22_p257-309"), (310, "08_func_3.23-3.25_p310-353"),
          (354, "09_func_3.26-3.100_p354-408"), (409, "10_func_3.200-3.300_p409-457"),
          (458, "11_tut_prologue-4.2_p458-504"), (505, "12_tut_4.3-4.6_p505-562"),
          (563, "13_tut_4.7-4.8_p563-616"), (617, "14_tut_4.9-4.10_p617-654"),
          (655, "15_tut_4.11_p655-693"), (694, "16_tut_4.12_p694-730"),
          (731, "17_tut_4.13-4.17_p731-803"), (804, "18_tut_4.18-4.19_p804-872"),
          (873, "19_tut_4.20-4.21_p873-930"), (931, "20a_tut_4.22-4.23_p931-960"),
          (961, "20b_tut_4.24_p961-989"),
          (990, "21_tut_4.25-4.100_p990-1030"), (1031, "22_tut_4.200-4.300_p1031-1083"),
          (1084, "23_tut_4A-skills-appendix_p1084-1161")]

CMD2TOK = {"rho": "ρ", "Gamma": "Γ", "alpha": "α", "beta": "β", "eta": "η",
           "varphi": "φ", "phi": "φ", "chi": "χ", "sigma": "σ", "pi": "π",
           "mu": "μ", "tau": "τ", "varepsilon": "ε", "epsilon": "ε",
           "nabla": "∇", "partial": "∂", "sum": "∑", "int": "∫", "infty": "∞",
           "sqrt": "√", "Delta": "Δ", "omega": "ω", "lambda": "λ",
           "theta": "θ", "kappa": "κ", "xi": "ξ", "zeta": "ζ", "Omega": "Ω",
           "Pi": "Π", "Phi": "Φ", "Psi": "Ψ", "psi": "ψ", "gamma": "γ",
           "delta": "δ", "nu": "ν", "approx": "≈", "times": "×", "cdot": "·",
           "leq": "≤", "geq": "≥", "neq": "≠", "to": "→", "in": "∈",
           "bar": "̄", "hat": "^", "frac": "/", "left": "", "right": ""}
GREEK = set("ΓΧραβγηφχεπσΣ∫∇∂∞ηφχμτωεαβΓΠΔΩλθκξζψΨγδνΩ")
PROSE = {"when", "undefined", "only", "consider", "exchange", "correlation",
         "coulomb", "identical", "exactly", "postscript", "paircortype",
         "paircorrtype", "pairfunctype", "pairfuntype"}

def extract_math(page_md):
    """按顺序抽出所有数学片段, 返回 [(latex, is_display)] (去定界符, strip)."""
    spans = []
    tmp = page_md
    for m in re.finditer(r"\$\$(.+?)\$\$", tmp, re.S):
        spans.append((m.group(1).strip(), True, m.start()))
    tmp = re.sub(r"\$\$(.+?)\$\$", " ", tmp, flags=re.S)
    for m in re.finditer(r"\\\[(.+?)\\\]", tmp, re.S):
        spans.append((m.group(1).strip(), True, m.start()))
    tmp = re.sub(r"\\\[(.+?)\\\]", " ", tmp)
    for m in re.finditer(r"\\\((.+?)\\\)", tmp):
        spans.append((m.group(1).strip(), False, m.start()))
    tmp = re.sub(r"\\\((.+?)\\\)", " ", tmp)
    for m in re.finditer(r"\$(.+?)\$", tmp):
        spans.append((m.group(1).strip(), False, m.start()))
    spans.sort(key=lambda x: x[2])
    return [(a, b) for a, b, _ in spans]

def garbage(latex):
    if "□" in latex or "\u25a1" in latex:
        return "box-garbage"
    if "\\text{" in latex or "\\mbox{" in latex:
        return "has-text"
    if any(c in latex for c in "：，。；"):
        pass  # 后面修, 不直接判死
    body = re.sub(r"\\[a-zA-Z]+", " ", latex)
    body = re.sub(r"[{}$_^&\\]", " ", body)
    words = re.findall(r"[A-Za-z]{3,}", body)
    prose = [w for w in words if w.lower() in PROSE]
    if prose:
        return f"prose:{prose[:3]}"
    if len(re.sub(r"\s+", "", latex)) < 8:
        return "too-short"
    return None

def fix(latex):
    latex = re.sub(r"t\s+o\s+t", "tot", latex)
    latex = latex.replace("：", ":").replace("，", ",").replace("；", ";")
    latex = re.sub(r"\s+", " ", latex).strip()
    return latex

def tokens_of_latex(latex):
    toks = set()
    for m in re.findall(r"\\([a-zA-Z]+)", latex):
        if m in CMD2TOK and CMD2TOK[m]:
            toks.add(CMD2TOK[m])
    for ch in latex:
        if ch in GREEK:
            toks.add(ch)
    for ch in re.findall(r"[A-Za-z]", re.sub(r"\\[a-zA-Z]+", "", latex)):
        toks.add(ch.lower())
    return toks

def tokens_of_raw(raw):
    raw = unicodedata.normalize("NFKD", raw)  # 把 𝑚𝐴 这类数学字母转回 ASCII
    toks = set()
    for ch in raw:
        if ch in GREEK:
            toks.add(ch)
    for ch in re.findall(r"[A-Za-z]", raw):
        toks.add(ch.lower())
    return toks


if __name__ == "__main__":
    manifest = json.load(open(os.path.join(BASE, "formulas_manifest.json"), encoding="utf-8"))
    ocr_pages = {}  # pno -> markdownText
    for start, name in CHUNKS:
        p = os.path.join(BASE, f"ocr_out/{name}.json")
        if not os.path.exists(p):
            print(f"缺 {p}, 跳过")
            continue
        d = json.load(open(p, encoding="utf-8"))
        for i, pg in enumerate(d["pages"]):
            ocr_pages[start + i] = pg["markdownText"]

    report = {"replaced": [], "kept": []}
    replacements = {}  # fname -> latex
    for pno_s, imgs in manifest.items():
        pno = int(pno_s)
        page_md = ocr_pages.get(pno)
        if page_md is None:
            for im in imgs:
                report["kept"].append({"page": pno, "img": im["fname"], "why": "no-ocr-page"})
            continue
        cands = []
        for latex, disp in extract_math(page_md):
            g = garbage(latex)
            if g:
                continue
            cands.append({"latex": fix(latex), "display": disp, "used": False,
                          "toks": tokens_of_latex(latex)})
        last_pos = -1
        for im in imgs:
            rt = tokens_of_raw(im["raw"])
            best, best_sc = None, 0
            for ci, cd in enumerate(cands):
                if cd["used"]:
                    continue
                if ci < last_pos:
                    continue  # 保持阅读顺序单调, 防串行
                inter = rt & cd["toks"]
                # 希腊/符号 token 加权
                sc = sum(2 if t in GREEK else 1 for t in inter)
                if sc > best_sc:
                    best, best_sc = cd, sc
                    best_ci = ci
            need = 2 if len(rt) >= 2 else 1
            if best is not None and best_sc >= need:
                best["used"] = True
                last_pos = best_ci
                replacements[im["fname"]] = best["latex"]
                report["replaced"].append({"page": pno, "img": im["fname"],
                                           "latex": best["latex"][:120]})
            else:
                report["kept"].append({"page": pno, "img": im["fname"],
                                       "why": f"no-match(score={best_sc},rawtoks={len(rt)})",
                                       "raw": im["raw"][:80]})

    path = os.path.join(BASE, "multiwfn_full.md")
    txt = open(path, encoding="utf-8").read()
    n = 0
    for fname, latex in replacements.items():
        pat = re.compile(r"!\[\]\(mw_imgs/" + re.escape(fname) + r"\)\n\n<!-- formula-raw p\.\d+:.*?-->",
                         re.S)
        new = f"$${latex}$$\n\n<!-- formula-ocr: {fname} 已替换为LaTeX, 原图保留备查 -->"
        txt2, cnt = pat.subn(lambda m: new, txt, count=1)
        if cnt:
            txt, n = txt2, n + 1
    open(path, "w", encoding="utf-8").write(txt)
    json.dump(report, open(os.path.join(BASE, "formulas_merge_report.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"replaced: {len(report['replaced'])} (md实际替换{n}), kept: {len(report['kept'])}")
    for k in report["kept"][:15]:
        print(" KEPT p%d %s %s" % (k["page"], k["img"], k.get("why", "")))

