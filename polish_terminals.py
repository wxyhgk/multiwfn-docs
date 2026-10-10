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
FILE_PAT = re.compile(r'examples\\|\.(fchk?|out|wfn|mwfn|wfx|mol|pdb|xyz|cub|gjf|molden|txt)\b|(?<![\d.])\.\d+\b|\?[\w\\/.-]+')
TAIL_CMD = re.compile(r'\s(-?[\d,.\-]{1,12}|[ynqYNQdlXD])$')


def looks_cmd(s):
    s = s.strip()
    if not s:
        return False
    if re.search(r'ENTER|回车', s, re.I) and len(s) <= 80:
        return True
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
    tmp = []
    for pg in parts:
        m = re.search(r'\s(-?[\d,.\-]+|[ynqYNQdlXD])$', pg.strip())
        _front = pg.strip()[:m.start()] if m else ''
        _cjk = sum(1 for _c in _front if '\u4e00' <= _c <= '\u9fff')
        if m and (len(_front) >= 10 or _cjk >= 3):
            tmp += [pg[:m.start()].strip(), m.group(1)]
        else:
            tmp.append(pg)
    parts = tmp
    if len(parts) < 3:
        return None
    start = -1
    for i, p in enumerate(parts):
        if looks_cmd(p):
            start = i
            break
    if start < 0:
        return None
    if start == 0 and len(parts[0]) > 40 and not re.search(r'ENTER|回车', parts[0], re.I):
        pre, start = parts[0].strip(), 1
    elif start == 0 and not re.search(r'\d', parts[0]) and not FILE_PAT.search(parts[0]) and not re.search(r'ENTER|回车', parts[0], re.I):
        pre, start = parts[0].strip(), 1
    else:
        pre = ' // '.join(parts[:start]).strip() if start > 0 else ''
    rest = parts[start:]
    if pre and not GUIDE_PAT.search(pre) and not FILE_PAT.search(pre) and not re.search(r'ENTER|回车', pre, re.I):
        first = rest[0].strip() if rest else ''
        if not re.match(r'^-?[\d,.\-]+$', first) and len(first) > 6:
            return None
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
    # rest首段是说明、次段是命令(如"概念DFT分析 1"): 说明并入pre
    if rest and not looks_cmd(rest[0]) and len(rest) > 1 and looks_cmd(rest[1]):
        pre = (pre + ' // ' + rest[0].strip()).strip() if pre else rest[0].strip()
        i = 1
    if not carry and rest and not looks_cmd(rest[0]):
        if len(rest) > 1 and looks_cmd(rest[1]):
            m = re.search(r'(\S+\.(?:fchk?|out|wfn|mwfn|wfx|mol|pdb|xyz|cub|gjf|molden|txt))\s*$', pre)
            if m:
                pairs.append((m.group(1), rest[0].strip()))
                pre = pre[:m.start()].strip()
                i = 1
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
        if not m or len(desc) - len(m.group(1)) < 10:
            m2 = re.search(r'(\[.*ENTER.*\]|\S+\.(?:fchk?|out|wfn|mwfn|wfx|mol|pdb|xyz|cub|gjf|molden|txt))\s*$', desc)
            if m2 and len(desc) - len(m2.group(1)) >= 10:
                m = m2
            else:
                m = None
        if m and len(desc) - len(m.group(1)) >= 10 and (
                len(m.group(1)) > 1 or len(desc) <= 60):
            carry = m.group(1)
            desc = desc[:m.start()].strip()
        pairs.append((cmd, desc))
    if not pairs:
        return None
    if len(pairs) == 1:
        c0, d0 = pairs[0]
        import unicodedata as _ud
        cjk = sum(1 for _c in d0 if '\u4e00' <= _c <= '\u9fff')
        _cmax = 80 if re.search(r'ENTER|回车', c0, re.I) else 12
        if not (len(c0) <= _cmax and (len(d0) >= 15 or cjk >= 6)):
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
