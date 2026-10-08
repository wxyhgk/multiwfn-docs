#!/usr/bin/env python3
"""Wave1: 机械类修复 (审计报告 P0-P2). 全部 fence-aware, 只动围栏外.
- P0: zh_04 L1572 补行尾 $$
- 行尾空格删除
- F0B1->±, F0A3->≤ (Symbol)
- Stout- Politzer, positons, R*are
- L119 路径去反引号; 裸 settings.ini(非路径)加反引号
- single-断词合并; Section After 加句号
"""
import re, glob

FILES = ["multiwfn_full.md"] + sorted(glob.glob("chapters/*.md"))
log = []

def process(path, fn):
    lines = open(path, encoding="utf-8").read().split("\n")
    in_code = False
    changed = 0
    for i, l in enumerate(lines):
        if l.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        o = l
        l = l.rstrip(" \t")  # 行尾空格
        l = l.replace("\uf0b1", "±").replace("\uf0a3", "≤")
        l = l.replace("Stout- Politzer", "Stout-Politzer")
        l = l.replace("positons", "positions")
        l = l.replace("R*are defined", "R* are defined")
        l = l.replace("/sob/tmp/`settings.ini`", "/sob/tmp/settings.ini")
        l = re.sub(r"(?<![`\/\\])settings\.ini(?![\w`])", "`settings.ini`", l)
        l = l.replace("last Section After re-entering", "last Section. After re-entering")
        if l != o:
            lines[i] = l
            changed += 1
    # single-断词合并 (跨行)
    out = []
    i = 0
    while i < len(lines):
        if (lines[i].endswith("single-") and i + 1 < len(lines)
                and lines[i+1].startswith("determinant")):
            out.append(lines[i][:-1] + lines[i+1])
            log.append(f"{path}: single-合并 L{i+1}")
            i += 2
            changed += 1
        else:
            out.append(lines[i])
            i += 1
    if changed:
        open(path, "w", encoding="utf-8").write("\n".join(out))
    return changed

total = 0
for f in FILES:
    n = process(f, None)
    if n:
        print(f"{f}: {n}行")
        total += n

# P0
p = "chapters/zh_04_功能3.14-3.22.md"
L = open(p, encoding="utf-8").read().split("\n")
assert L[1571].rstrip().endswith("\\end{aligned}"), L[1571][-40:]
L[1571] = L[1571].rstrip() + "$$"
open(p, "w", encoding="utf-8").write("\n".join(L))
print("P0 zh_04 L1572 补$$ ok")
print("TOTAL", total)
