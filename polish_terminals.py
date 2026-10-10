#!/usr/bin/env python3
"""终端交互记录结构化: `cmd // 说明`长串 -> !!! terminal admonition.

用法: python3 polish_terminals.py [--write]
  默认dry-run只统计; --write才落盘. 可重复跑(已生成块自动跳过, 收敛).
"""
import glob
import os
import re
import sys

BASE = '/Users/wxyhgk/Documents/Quamtum_Chemistry_md/Multiwfn'
SEC = [os.path.join(BASE, 'sections', 'en'), os.path.join(BASE, 'sections', 'zh')]

SPLIT_PAT = re.compile(r'(?<!:) // ')
CMD_PAT = re.compile(r'^-?[\d,.\s\-+*a-zA-Z\\/_()]+$')
GUIDE_PAT = re.compile(r'Boot up|input|输入|启动|below commands|如下|命令', re.I)
FILE_PAT = re.compile(r'examples\\|\.(fch|out|wfn|mwfn|wfx)\b')
TAIL_CMD = re.compile(r'\s(-?[\d,.\-]{1,12})$')


def looks_cmd(s):
    s = s.strip()
    if not s:
        return False
    if FILE_PAT.search(s):
        return True
    if len(s) > 40:
        return False
    if not CMD_PAT.match(s):
        return False
    if re.match(r'^[A-Za-z][a-z]+(\s+[A-Za-z][a-z]+){2,}$', s):
        return False
    return True


def parse_line(line):
    """返回 (pre, [(cmd, desc)], tail) 或 None."""
    parts = SPLIT_PAT.split(line)
    if len(parts) < 4:
        return None
    start = -1
    for i, p in enumerate(parts):
        if looks_cmd(p):
            start = i
            break
    if start < 0:
        return None
    if start == 0 and len(parts[0]) > 40:
        pre, start = parts[0].strip(), 1
    else:
        pre = ' // '.join(parts[:start]).strip() if start > 0 else ''
    if pre and not GUIDE_PAT.search(pre) and not FILE_PAT.search(pre):
        return None
    rest = parts[start:]
    pairs = []
    lead = None
    m0 = re.search(r'\s(-?[\d,.\-]{1,12})$', pre)
    if m0 and (GUIDE_PAT.search(pre) or FILE_PAT.search(pre)):
        lead = m0.group(1)
        pre = pre[:m0.start()].strip()
    if ' // ' in pre:
        a, b = pre.rsplit(' // ', 1)
        m1 = re.search(r'\s(-?[\d,.\-]{1,12})$', a)
        if m1 and not looks_cmd(b):
            pairs.append((m1.group(1), b.strip()))
            pre = a[:m1.start()].strip()
    i = 0
    carry = lead
    while True:
        if carry is not None:
            cmd, carry = carry, None
        else:
            if i >= len(rest):
                break
            cmd = rest[i].strip()
            i += 1
        if not looks_cmd(cmd):
            break
        if i >= len(rest):
            break
        desc = rest[i].strip()
        i += 1
        if len(desc) < 2:
            break
        m = TAIL_CMD.search(desc)
        if m and len(desc) - len(m.group(1)) >= 10:
            carry = m.group(1)
            desc = desc[:m.start()].strip()
        pairs.append((cmd, desc))
    if len(pairs) < 2:
        return None
    tail = ' // '.join(rest[i:]).strip() if i < len(rest) else ''
    return pre, pairs, tail


def render(pre, pairs, tail, title='Multiwfn 交互'):
    out = []
    if pre:
        out.append(pre + '\n')
    out.append(f'!!! terminal "{title}"')
    out.append('')
    for cmd, desc in pairs:
        out.append(f'    - **{cmd}** — {desc}')
    if tail:
        out.append('\n' + tail)
    return '\n'.join(out)


def process(text, title):
    lines = text.split('\n')
    out = []
    n = 0
    in_fence = False
    in_admon = False
    for ln in lines:
        if ln.strip().startswith('```'):
            in_fence = not in_fence
            in_admon = False
            out.append(ln)
            continue
        if not in_fence and re.match(r'!!! \w+', ln.strip()):
            in_admon = True
            out.append(ln)
            continue
        if in_admon:
            if ln.startswith('    ') or not ln.strip():
                out.append(ln)
                continue
            in_admon = False
        if in_fence or ln.lstrip().startswith(('>', '<!--', '#', '|', '![')):
            out.append(ln)
            continue
        r = parse_line(ln)
        if r:
            pre, pairs, tail = r
            out.append(render(pre, pairs, tail, title))
            n += 1
        else:
            out.append(ln)
    return '\n'.join(out), n


def main():
    write = '--write' in sys.argv
    tf = ff = 0
    for sec in SEC:
        title = 'Multiwfn 交互' if sec.endswith('zh') else 'Multiwfn session'
        for f in sorted(glob.glob(os.path.join(sec, '*.md'))):
            t = open(f, encoding='utf-8').read()
            new, n = process(t, title)
            if n:
                ff += 1
                tf += n
                if write:
                    open(f, 'w', encoding='utf-8').write(new)
    print(f'blocks: {tf} in {ff} files, mode={"WRITE" if write else "DRY"}')


if __name__ == '__main__':
    main()
