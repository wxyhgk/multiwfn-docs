#!/usr/bin/env python3
"""把翻译失败的章节切成~15页小段, 逐段翻译后合并. 用法: python3 seg_translate.py
流程: 1)切段 2)打印待跑命令(分批) 3)校验合并(单独跑 --verify)
"""
import re, os, sys, glob

CH = "/Users/wxyhgk/Documents/Quamtum_Chemistry_md/Multiwfn/chapters"
RANGES = {"03_功能3.2-3.13": (77, 182), "04_功能3.14-3.22": (183, 309),
          "05_功能3.23-3.300": (310, 457), "06_教程4.0-4.8": (458, 616),
          "07_教程4.9-4.12": (617, 730), "08_教程4.13-4.19": (731, 872),
          "09_教程4.20-4.24": (873, 989), "10_教程4.25-附录": (990, 1161)}
SEG = 16  # 每段页数

PROMPT = ("将 {src} 全文译为简体中文, 写入 {dst}。要求: 保留Markdown结构、页标记、图片引用"
          "(../mw_imgs/开头)、URL/路径; 菜单用中文(English)形式; 专有名词(Multiwfn、Gaussian、"
          "settings.ini、文件名、命令、参数名、LaTeX公式、代码块内容)一律不译, LaTeX公式和代码块原样保留; "
          "必须逐页全翻, 不得摘要或跳页。译完只报告页标记数。")

def pages_of(fname):
    txt = open(os.path.join(CH, fname + ".md"), encoding="utf-8").read()
    parts = re.split(r"<!-- p\.(\d+) -->", txt)
    pg = {}
    for i in range(1, len(parts), 2):
        pg[int(parts[i])] = parts[i+1] if i+1 < len(parts) else ""
    return pg

if "--verify" in sys.argv:
    ok = True
    for f, (a, b) in RANGES.items():
        en = pages_of(f)
        zf = os.path.join(CH, f"zh_{f}.md")
        if not os.path.exists(zf):
            print(f"{f}: 缺译文"); ok = False; continue
        zh = open(zf, encoding="utf-8").read()
        zmarks = sorted(set(int(x) for x in re.findall(r"<!-- p\.(\d+) -->", zh)))
        miss = [p for p in en if p not in zmarks]
        ei = len(re.findall(r"mw_imgs/", open(os.path.join(CH, f+'.md'), encoding='utf-8').read()))
        zi = len(re.findall(r"mw_imgs/", zh))
        st = "OK" if not miss and zi >= ei else "FAIL"
        if st == "FAIL": ok = False
        print(f"{f}: 页缺{miss[:6] if miss else '无'} 图en{ei}/zh{zi} -> {st}")
    sys.exit(0 if ok else 1)

segs = []
for f, (a, b) in RANGES.items():
    en = pages_of(f)
    ps = sorted(en)
    for s in range(0, len(ps), SEG):
        chunk = ps[s:s+SEG]
        body = "".join(f"<!-- p.{p} -->\n" + en[p] for p in chunk)
        seg = f"seg_{f}_{chunk[0]}-{chunk[-1]}"
        open(os.path.join(CH, seg + ".md"), "w", encoding="utf-8").write(body)
        segs.append((seg, f, chunk[0], chunk[-1]))
        # 删掉旧的部分译文, 避免混淆
        zf = os.path.join(CH, f"zh_{f}.md")
        if os.path.exists(zf):
            os.remove(zf)
print(f"共{len(segs)}段")
for seg, f, a, b in segs:
    src = os.path.join(CH, seg + ".md")
    dst = os.path.join(CH, seg + ".zh.md")
    print(f'pi -p --provider opencode-go --model muse-spark-1.3-contributor --no-session "{PROMPT.format(src=src, dst=dst)}"')
