#!/usr/bin/env python3
"""Wave2b: 断裂标题合并. 规则: ##/### 行若不以节编号开头, 则为上行的延续, 合并.
节编号头: 数字编号(4.20.1/3.21/5.1/6.6/4.A...), Prologue/Note/Tip/Skills/Appendix/Contents.
只在围栏外操作; 合并后ZH尾若残留纯英文尾巴则记入报告.
"""
import re, glob

FILES = ["multiwfn_full.md"] + sorted(glob.glob("chapters/*.md"))
HEAD = re.compile(r"^#{2,3}\s+(\d+\.\S*|[456]\s|Prologue|Note|Tip|Skill|Appendix|Contents|前言|概述|安装|使用|功能|教程|附录|技巧|程序|输出| contents)", re.I)
TAILS_EN_LEFT = []  # ZH合并后仍有英文尾的, 备查

log = []
for path in FILES:
    lines = open(path, encoding="utf-8").read().split("\n")
    in_code = False
    flags = []
    for l in lines:
        if l.strip().startswith("```"):
            in_code = not in_code
        flags.append(in_code)
    out = []
    n = 0
    for i, l in enumerate(lines):
        m = re.match(r"^(#{2,3})\s+(.*\S)\s*$", l)
        if m and not flags[i] and not HEAD.match(l):
            # 找上一个非空非注释行
            j = len(out) - 1
            while j >= 0 and (not out[j].strip() or out[j].strip().startswith("<!--")
                              or out[j].strip().startswith("```") or out[j].strip().startswith("|")):
                j -= 1
            if j >= 0 and re.match(r"^#{1,3}\s", out[j]):
                tail = m.group(2)
                out[j] = out[j].rstrip() + " " + tail
                n += 1
                if re.search(r"[A-Za-z]{4,}$", tail) and "zh_" in path:
                    TAILS_EN_LEFT.append(f"{path} L{i+1}: ...{out[j][-90:]}")
                continue
        out.append(l)
    if n:
        open(path, "w", encoding="utf-8").write("\n".join(out))
    log.append(f"{path}: 合并{n}处")

print("\n".join(log))
print("\n--- ZH英文尾待译 ---")
print("\n".join(TAILS_EN_LEFT[:30]) if TAILS_EN_LEFT else "无")
