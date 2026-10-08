#!/usr/bin/env python3
"""手工精确修复 (幂等: 锚点消失则跳过). 纯字符串操作, 无正则替换."""
import re

P = "multiwfn_full.md"
txt = open(P, encoding="utf-8").read()
log = []

def sub_once(old, new, tag):
    global txt
    if old in txt:
        txt = txt.replace(old, new, 1)
        log.append(f"{tag}: OK")
    else:
        log.append(f"{tag}: SKIP")

def re_sub_once(pat, new, tag):
    global txt
    txt2, n = re.subn(pat, lambda m: new, txt, count=1, flags=re.S)
    txt = txt2
    log.append(f"{tag}: {n}")

# ---- p66 LSDA 表格内公式 (图+乱码行) ----
re_sub_once(r"!\[\]\(mw_imgs/formula_p66_041\.png\)\n\n<!-- formula-raw p\.66:.*?-->",
 "0 LSDA exchange: $$-(3/2)\\left[3/(4\\pi)\\right]^{1/3}[\\rho_{\\alpha}(\\mathbf{r})^{4/3}+\\rho_{\\beta}(\\mathbf{r})^{4/3}]$$. "
 "For closed-shell cases the equivalent form is $$-(3/4)(3/\\pi)^{1/3}\\rho(\\mathbf{r})^{4/3}$$.", "p66-img")
for ln in txt.split("\n"):
    if ln.startswith("0 LSDA exchange:") and "1/34/3" in ln:
        sub_once(ln, "", "p66-garbled-line")
        break
else:
    log.append("p66-garbled-line: SKIP")

# ---- p222 分段函数 ----
re_sub_once(r"!\[\]\(mw_imgs/formula_p222_126\.png\)\n\n<!-- formula-raw p\.222:.*?-->",
 "$$\\left\\{\\begin{aligned}w_{A}(\\mathbf{r})&=1&\\text{if }\\mathbf{r}\\in\\Omega_{A}\\\\ "
 "w_{A}(\\mathbf{r})&=0&\\text{if }\\mathbf{r}\\notin\\Omega_{A}\\end{aligned}\\right.$$", "p222-img")

# ---- p343 ε 工作方程 ----
re_sub_once(r"!\[\]\(mw_imgs/formula_p343_233\.png\)\n\n<!-- formula-raw p\.343:.*?-->",
 "$$\\varepsilon=\\chi\\left(\\frac{\\phi}{\\gamma}\\right)-\\left(\\frac{\\phi}{\\gamma}\\right)^{2}"
 "\\left(\\frac{\\eta}{2}+\\frac{\\phi}{6}\\right)$$", "p343-eps")

# ---- p429 库仑/交换积分 (乱码行+图) ----
for ln in txt.split("\n"):
    if "1212 1212" in ln:
        sub_once(ln, "Coulomb $(ii|jj)$ and exchange integral $(ij|ji)$ between orbitals $i$ and $j$:\n\n"
 "$$ (ii\\mid jj)=\\int\\int\\frac{\\varphi_{i}^{*}(\\mathbf{r}_{1})\\varphi_{i}(\\mathbf{r}_{1})"
 "\\varphi_{j}^{*}(\\mathbf{r}_{2})\\varphi_{j}(\\mathbf{r}_{2})}{r_{12}}\\mathrm{d}\\mathbf{r}_{1}\\mathrm{d}\\mathbf{r}_{2} $$\n\n"
 "$$ (ij\\mid ji)=\\iint\\frac{\\varphi_{i}^{*}(\\mathbf{r}_{1})\\varphi_{j}(\\mathbf{r}_{1})"
 "\\varphi_{j}^{*}(\\mathbf{r}_{2})\\varphi_{i}(\\mathbf{r}_{2})}{r_{12}}\\mathrm{d}\\mathbf{r}_{1}\\mathrm{d}\\mathbf{r}_{2} $$",
 "p429-both")
        break
else:
    log.append("p429-both: SKIP")
re_sub_once(r"\n\n!\[\]\(mw_imgs/formula_p429_319\.png\)\n\n<!-- formula-raw p\.429:.*?-->",
 "\n\n<!-- formula-ocr-manual: formula_p429_319 见上 -->", "p429-img")

# ---- p343 calc/mu/eta/gamma 四行沙拉 ----
lines = txt.split("\n")
for i, ln in enumerate(lines):
    if ln.startswith("()123()"):
        lines[i] = ("$$\\omega_{cubic}=\\frac{\\left(\\mu_{cubic}\\right)^{2}}{2\\eta_{cubic}}"
 "\\left[1+\\frac{\\mu_{cubic}}{3\\left(\\eta_{cubic}\\right)^{2}}\\gamma_{cubic}\\right]$$")
        log.append("p343-calc: OK"); break
else:
    log.append("p343-calc: SKIP")
for i, ln in enumerate(lines):
    if ln.startswith("\uf06d cubic12"):
        lines[i] = "$$\\mu_{cubic}=(1/6)(-2A-5I_{1}+I_{2})$$"
        log.append("p343-mu: OK"); break
else:
    log.append("p343-mu: SKIP")
for i, ln in enumerate(lines):
    if ln.startswith("\uf068 cubic1"):
        lines[i] = "$$\\eta_{cubic}=I_{1}-A$$"
        log.append("p343-eta: OK"); break
else:
    log.append("p343-eta: SKIP")
for i, ln in enumerate(lines):
    if ln.startswith("\uf067 cubic12"):
        lines[i] = "$$\\gamma_{cubic}=2I_{1}-I_{2}-A$$"
        log.append("p343-gamma: OK"); break
else:
    log.append("p343-gamma: SKIP")
# ---- p60 57/58/59 ----
for i, ln in enumerate(lines):
    if ln.startswith("57 ( )g"):
        lines[i] = ("57 $$g_{1}(\\mathbf{r})=\\nabla^{2}\\rho(\\mathbf{r})"
 "\\ln\\frac{\\rho(\\mathbf{r})}{\\rho_{0}(\\mathbf{r})}$$")
        log.append("p60-57: OK"); break
else:
    log.append("p60-57: SKIP")
for i, ln in enumerate(lines):
    if ln.startswith("58 ( )("):
        lines[i] = ("58 $$g_{2}(\\mathbf{r})=\\rho(\\mathbf{r})\\left["
 "\\frac{\\nabla^{2}\\rho(\\mathbf{r})}{\\rho(\\mathbf{r})}-"
 "\\frac{\\nabla^{2}\\rho_{0}(\\mathbf{r})}{\\rho_{0}(\\mathbf{r})}\\right]$$")
        log.append("p60-58: OK"); break
else:
    log.append("p60-58: SKIP")
for i, ln in enumerate(lines):
    if ln.startswith("59 ( )("):
        lines[i] = ("59 $$g_{3}(\\mathbf{r})=\\rho(\\mathbf{r})\\bigg["
 "\\nabla\\ln\\frac{\\rho(\\mathbf{r})}{\\rho_{0}(\\mathbf{r})}\\bigg]^{2}$$")
        log.append("p60-59: OK"); break
else:
    log.append("p60-59: SKIP")
# ---- p343 phi 方程补回 ----
txt = "\n".join(lines)
if "$$\\phi=\\sqrt{\\eta^{2}-2\\gamma\\mu}-\\eta$$" not in txt:
    ls = txt.split("\n")
    for i, ln in enumerate(ls):
        if ln.strip() == "with" and i + 2 < len(ls) and ls[i + 2].startswith("It is important to note"):
            ls.insert(i + 2, "$$\\phi=\\sqrt{\\eta^{2}-2\\gamma\\mu}-\\eta$$\n")
            log.append("p343-phi: OK"); break
    else:
        log.append("p343-phi: SKIP")
    txt = "\n".join(ls)
else:
    log.append("p343-phi: SKIP(已存在)")

open(P, "w", encoding="utf-8").write(txt)
print("\n".join(log))

# ---- 第二批: 8图 + 232/234 + p225分段 + 碎片删除 ----
import re as _re
_txt2 = open(P, encoding="utf-8").read()
_log2 = []
def _img(fname, latex, tag):
    global _txt2
    pat = _re.compile(r"!\[\]\(mw_imgs/" + _re.escape(fname) + r"\)\n\n<!-- formula-raw p\.\d+:.*?-->", _re.S)
    _txt2, n = pat.subn(lambda m: "$$" + latex + "$$", _txt2, count=1)
    _log2.append(f"{tag}: {n}")
_img("formula_p104_045.png", "q_{A}=-p_{A}+Z_{A}", "p104")
_img("formula_p226_132.png", "I_{AB}=\\int_{A}w_{A}(\\mathbf{r})w_{B}(\\mathbf{r})f(\\mathbf{r})\\mathrm{d}\\mathbf{r}", "p226")
_img("formula_p292_193.png", "\\mathbf{D}^{\\mathrm{tran}}=\\sum_{i,a}(w_{i,a}+w_{i,a}^{\\prime})\\langle\\varphi_{i}|-\\mathbf{r}|\\varphi_{a}\\rangle", "p292")
_img("formula_p363_265.png", "\\gamma_{\\perp}=(1/15)\\sum_{i}\\sum_{j}(2\\gamma_{ijij}-\\gamma_{ijji})\\quad i,j=\\{x,y,z\\}", "p363")
_img("formula_p449_331.png", "|\\mathbf{Q}_{3}|=\\sqrt{\\sum_{m=-3}^{3}(Q_{3,m})^{2}}", "p449-331")
_img("formula_p449_332.png", "\\Theta_{xyzz}=\\sum_{A}q_{A}X_{A}Y_{A}Z_{A}Z_{A}-\\int xyzz\\rho(\\mathbf{r})\\mathrm{d}\\mathbf{r}", "p449-332")
_img("formula_p450_334.png", "\\boldsymbol{\\mu}=\\begin{bmatrix}\\mu_{x}\\\\\\mu_{y}\\\\\\mu_{z}\\end{bmatrix}=\\sum_{A}q_{A}\\begin{bmatrix}X_{A}\\\\Y_{A}\\\\Z_{A}\\end{bmatrix}", "p450")
_img("formula_p343_232.png", "\\omega_{cubic}=\\omega\\left(1+\\frac{\\mu}{3\\eta^{2}}\\gamma\\right)", "p343-232")
_img("formula_p343_234.png", "\\begin{aligned}&\\mu=a\\\\&\\chi=-a\\\\&\\eta=2(b-ac)\\\\&\\gamma=-3c(b-ac)\\\\ \\end{aligned}", "p343-234")
_img("formula_p225_X.png", "PLACEHOLDER", "skip-me")
# p225 分段行(文本行)
for _ln in _txt2.split("\n"):
    if "5.0if5.0" in _ln and "ABAB" in _ln:
        _txt2 = _txt2.replace(_ln, "$$\\left\\{\\begin{aligned}a_{AB}&=-0.5&\\text{if }a_{AB}<-0.5\\\\ a_{AB}&=0.5&\\text{if }a_{AB}>0.5\\end{aligned}\\right.$$", 1)
        _log2.append("p225-piecewise: OK")
        break
else:
    _log2.append("p225-piecewise: SKIP")
# p232 碎片行删除
for _ln in _txt2.split("\n"):
    s = _ln.strip()
    if s and set(s) <= set("AFBG∈>() ") and "∈" in s and len(s) < 25:
        _txt2 = _txt2.replace(_ln, "", 1)
        _log2.append(f"p232-frag deleted: {s!r}")
        break
else:
    _log2.append("p232-frag: SKIP")
open(P, "w", encoding="utf-8").write(_txt2)
print("\n".join(_log2))
