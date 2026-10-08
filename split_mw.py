#!/usr/bin/env python3
"""Split multiwfn_full.md into chapters by page markers (抄 GaussView6/split_md.py)."""
import re, os

SRC = "multiwfn_full.md"
OUT_DIR = "chapters"
os.makedirs(OUT_DIR, exist_ok=True)

CHAPTERS = [
    ("01_前言总览.md", "前言与总览", 1, 30, "封面、必读、Linux/Mac说明、第1章 Overview"),
    ("02_基本信息.md", "基本信息", 31, 76, "第2章：安装、使用、输入文件、实空间函数、用户自定义函数、图形格式、周期体系"),
    ("03_功能3.2-3.13.md", "功能 3.2–3.13", 77, 182, "结构显示、点/线/面性质输出、波函数检查、布居分析、轨道成分、键级、DOS、光谱"),
    ("04_功能3.14-3.22.md", "功能 3.14–3.22", 183, 309, "拓扑分析、分子表面定量、格点数据、AdNDP、模糊原子空间、电荷分解、盆分析、激发分析、轨道定域"),
    ("05_功能3.23-3.300.md", "功能 3.23–3.300", 310, 457, "弱作用可视化、能量分解、CDFT、ETS-NOCV、超极化率、离域与芳香性、其它功能"),
    ("06_教程4.0-4.8.md", "教程 4.0–4.8", 458, 616, "序言、输入文件、轨道显示、点性质、拓扑实例、直线/平面作图、格点数据、波函数修改、布居电荷、轨道成分"),
    ("07_教程4.9-4.12.md", "教程 4.9–4.12", 617, 730, "键级、DOS图、各类光谱、分子表面定量分析"),
    ("08_教程4.13-4.19.md", "教程 4.13–4.19", 731, 872, "格点数据处理、AdNDP、模糊原子空间、电荷分解、盆分析、激发分析、轨道定域"),
    ("09_教程4.20-4.24.md", "教程 4.20–4.24", 873, 989, "弱作用可视化、能量分解、CDFT、ETS-NOCV、(超)极化率"),
    ("10_教程4.25-附录.md", "教程 4.25–附录", 990, 1161, "离域与芳香性、其它功能、专题与高级教程、使用技巧、附录"),
]

with open(SRC, encoding="utf-8") as f:
    text = f.read()

parts = re.split(r"<!-- p\.(\d+) -->", text)
header = parts[0]
pages = {}
for i in range(1, len(parts), 2):
    pno = int(parts[i])
    content = parts[i+1] if i+1 < len(parts) else ""
    pages[pno] = content

def fix_imgs(s):
    return s.replace("](mw_imgs/", "](../mw_imgs/")

for fname, title, pstart, pend, desc in CHAPTERS:
    chunks = []
    for p in range(pstart, pend + 1):
        if p in pages:
            chunks.append(f"<!-- p.{p} -->\n" + pages[p])
    missing = [p for p in range(pstart, pend + 1) if p not in pages]
    body = "".join(chunks).strip()
    body = fix_imgs(body)
    out = (f"# Multiwfn：{title}（p.{pstart}–{pend}）\n\n> {desc}\n\n"
           f"> 原文件：`../multiwfn_full.md`（全量单文件存档）｜图片目录：`../mw_imgs/`\n\n---\n\n" + body + "\n")
    with open(os.path.join(OUT_DIR, fname), "w", encoding="utf-8") as f:
        f.write(out)
    print(f"{fname}: p{pstart}-{pend} 缺页{missing if missing else '无'} {len(out)//1024}KB")

idx = ["# Multiwfn 官方手册 · 分章索引\n",
       "\n> PDF 共 1161 页，已转为 Markdown（含 OCR 回填的 LaTeX 行间公式）。单文件全量存档见 `../multiwfn_full.md`（2.8MB）；"
       "本目录为按主题拆分的 10 章，便于检索、翻译与维护。图片统一存放在 `../mw_imgs/`。\n",
       "\n## 章节\n"]
for fname, title, pstart, pend, desc in CHAPTERS:
    idx.append(f"- [{title}（p.{pstart}–{pend}）](./{fname})：{desc}\n")
idx.append("\n## 说明\n- 每章内保留 `<!-- p.N -->` 页标记，可回溯 PDF 原页。\n"
           "- 行间公式为 LaTeX（PaddleOCR 回填，原图在 `../mw_imgs/formula_*` 备查）；终端输出为 ```text 代码块。\n"
           "- 标题层级：`#`=章（22pt）、`##`=节（16pt）、`###`=小节（13pt）。\n")
with open(os.path.join(OUT_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.writelines(idx)
print("README done")
