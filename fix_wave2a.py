#!/usr/bin/env python3
"""Wave2a: 标题层级 demote + 输出行入围栏. fence-aware."""
import re, glob

FILES = ["multiwfn_full.md"] + sorted(glob.glob("chapters/*.md"))
FENCE_PAT = re.compile(r"^#\s{0,4}(\d+\s*[:() ]|Occ\b|Basin\b)")
ROUTE_PAT = re.compile(r"^#\s*(B3LYP|B972|HF/|CAM-|M062X|PBE\d|wB97|M06)")
PROTECT = re.compile(r"^#\s*(Multiwfn|[0-9]+\s+[A-Z][a-z]+|[0-9]+\s+[一-鿿]|!|Linux|[0-9]\s+(Skills|Appendix|技巧|附录))")

def is_code_head(l):
    if PROTECT.match(l):
        return False
    return bool(FENCE_PAT.match(l) or ROUTE_PAT.match(l))

log = []
for path in FILES:
    lines = open(path, encoding="utf-8").read().split("\n")
    dirty = False
    # 1) demote # 5 Skills / # 6 Appendix -> ##, 其下 ## -> ### (直到下一个同级#)
    for i, l in enumerate(lines):
        if re.match(r"^# 5 +Skills|^# 6 +Appendix|^# 5 +技巧|^# 6 +附录", l):
            lines[i] = "#" + l
            dirty = True
            log.append(f"{path} L{i+1} demote: {l[:30]}")
            for j in range(i+1, len(lines)):
                if re.match(r"^# ", lines[j]):
                    break
                if re.match(r"^### ", lines[j]):
                    lines[j] = "#" + lines[j]
                    dirty = True
                elif re.match(r"^## ", lines[j]):
                    lines[j] = "#" + lines[j]
                    dirty = True
    # 2) fence 代码行: 先标出围栏区
    in_f = [False] * len(lines)
    ic = False
    for i, l in enumerate(lines):
        if l.strip().startswith("```"):
            ic = not ic
            in_f[i] = True
        else:
            in_f[i] = ic
    # 连续代码行成组
    out = []
    i = 0
    n_fenced = 0
    while i < len(lines):
        if not in_f[i] and is_code_head(lines[i]):
            j = i
            grp = []
            while j < len(lines) and not in_f[j] and is_code_head(lines[j]):
                grp.append(lines[j])  # 原样保留(含行首#, 围栏内无标题语义)
                j += 1
            # 去掉行首"# "保留内容; 若组前后紧贴围栏则直接并入(简化: 独立围栏)
            out.append("```text")
            out.extend(grp)
            out.append("```")
            n_fenced += 1
            i = j
        else:
            out.append(lines[i])
            i += 1
    if n_fenced or dirty:
        open(path, "w", encoding="utf-8").write("\n".join(out))
        if n_fenced:
            log.append(f"{path}: fenced {n_fenced}组")

print("\n".join(log))
