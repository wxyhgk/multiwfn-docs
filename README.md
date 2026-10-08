# Multiwfn 文档工程 · 说明（复用 GaussView6 方法上 GitHub）

> 隔壁 `../GaussView6/` 已跑通全流程并上线：https://wxyhgk.github.io/gview6-docs/
> 本文件夹照同一套方法做 Multiwfn，步骤、命令、坑全部照抄即可。

## 0. 成果对照（GaussView6 样板间）

| 产物 | 位置 | 说明 |
|---|---|---|
| 原 PDF（23M，不进仓库） | `GaussView6/gview6官方说明书.pdf` | `.gitignore` 忽略 |
| 全量单文件 md（存档） | `gview6官方说明书.md` | 381KB |
| 中英分章（11+11） | `chapters/*.md`、`chapters/zh_*.md` | 维护以此为准 |
| 图片 373 张 | `imgs/`、`docs/imgs/` | 两份（git 按内容去重只存一份） |
| 站点源码 | `docs/`、`mkdocs.yml`、`docs/stylesheets/extra.css`、`docs/javascripts/lang-switch.js` | |
| 自动发布 | `.github/workflows/docs.yml` | push 即上线 |

## 1. 准备

```bash
cd /Users/wxyhgk/Documents/Quamtum_Chemistry_md/Multiwfn
# 把 PDF 拷进来（可复制文本型直接转；扫描版看第 2 步备注）
cp "/path/to/multiwfn manual.pdf" ./multiwfn.pdf
python3 -c "import fitz; d=fitz.open('multiwfn.pdf'); print(len(d), 'pages'); print(d[0].get_text()[:300])"
```

## 2. PDF → Markdown

- **可复制文本型**（能选中文字）：抄 `../GaussView6/convert_gview6.py`，改 `SRC/OUT_MD/IMG_DIR` 三个变量。核心逻辑：PyMuPDF 按字号认标题（16pt→`#`、13pt→`##`、11pt→`###`，先抽样确认）、小图标过滤（<80px 不要）、表格用 `find_tables` 转 GFM、`<!-- p.N -->` 页标记保留、目录用 `get_toc()` 生成。
- **扫描型**：走 PaddleOCR skill（`paddleocr api --model_type doc_parsing --file_path xxx.pdf --output_md out/paper.md`），见 `~/.pi/agent/skills/paddleocr-doc-parsing/SKILL.md`。

## 3. 拆分章节

抄 `../GaussView6/split_md.py`：按 `<!-- p.N -->` 页标记切成 8–12 章（每章 10–40 页），英文放 `chapters/`，配 `chapters/README.md` 索引。章名用 `01_主题.md` 格式。

## 4. 翻译（多 agent 并行）

单 agent 先翻最短一章验证 prompt，通过后全量并行（11 章约 3 分钟）：

```bash
pi -p --provider opencode-go --model muse-spark-1.3-contributor --no-session \
"将 chapters/XX.md 全文译为简体中文写入 chapters/zh_XX.md。保留Markdown结构、页标记、图片引用、URL/路径/菜单/关键词（菜单用中文（English）形式）；专有名词不译；译完报 wc -c 和页标记数。"
```

- `--provider/--model` 必须显式带，否则鉴权失败。
- 译文命名 `zh_` 前缀；完工校验：每章页标记数、图片数与英文 1:1（`grep -c` 对）。
- 大文件让 agent 分段读、分段追加写。

## 5. 格式审计修复（必做，PDF 转的有系统性毛病）

1. 起 4 个 agent 只审计不改（每人 5–6 个文件），报告落 `/tmp`：重点孤立 `-`（`◦` 转出来断成 `-` + 裸段落，本次 1522 处）、行尾空格、`•`/`\*X` 混用、表格（补表头、压平段落重制表）、标题误判、拼写。
2. 机械类抄 `../GaussView6/fix_p0_format.py` 直接跑（含：孤立 `-` 合并、图注保护、换行粘连合并、去重只记不删）。
3. 表格/标题/拼写类按审计报告逐条修（可再派 agent 修，文件互不重叠）。
4. **铁律**：图注（如 `The Xxx Panel` 单独成行）不是重复，删前先看后一行是不是图；`2=Fixed` 这类重复选项是合法内容。

## 6. MkDocs 站点

```bash
python3 -m pip install mkdocs-material
mkdir -p docs/zh docs/en
cp chapters/zh_*.md docs/zh/ && cp chapters/0*.md chapters/1*.md docs/en/
cp -r imgs docs/imgs
cp chapters/zh_README.md docs/zh/index.md && cp chapters/README.md docs/en/index.md
```

`mkdocs.yml` 关键项（抄 GaussView6 的）：主题 material（`navigation.tabs` + `navigation.tracking`）、`use_directory_urls: false`（否则双击文件看要多点一次）、`extra_css`（minimap 刻度线、图片居中、语言浮钮样式）、`extra_javascript`（`docs/javascripts/lang-switch.js`，中英同章节互跳，要求中英文件名满足 `zh_A ↔ A` 对应）。

```bash
python3 -m mkdocs build && python3 -m mkdocs serve -a 127.0.0.1:8001
# 打开 http://127.0.0.1:8001/<仓库名>/ 验证
```

## 7. 发 GitHub（一键三连后自动上线）

```bash
printf 'site/\n.DS_Store\n__pycache__/\n*.pdf\n' > .gitignore
git init -b main && git add -A && git commit -m "Multiwfn docs init" \
&& gh repo create multiwfn-docs --public --source=. --remote=origin --push
echo '{"source":{"branch":"gh-pages","path":"/"}}' \
| gh api repos/wxyhgk/multiwfn-docs/pages -X POST --input -
```

- `.github/workflows/docs.yml` 抄 GaussView6（push 到 main → `mkdocs gh-deploy` → `gh-pages`）。
- `site_url`/`repo_url` 换成真实地址再 push。
- 验活：`curl https://wxyhgk.github.io/multiwfn-docs/`，Action 约 30 秒。

## 8. 踩过的坑（速查）

1. `marker-pdf` 在本机是坏的（缺 `transformers.onnx`），可复制 PDF 别用它。
2. `mkdocs serve` 的 livereload 会让 `networkidle` 永不等到，headless 测试用 `domcontentloaded`。
3. Material 右栏容器 `height:0`，自定义竖线别锚定它；minimap 用目录 DOM 本体压扁最稳。
4. 右栏目录只收录 h2 及以下——每章只留一个 `#`，其余降级，否则右侧空白。
5. `navigation.tracking` 开了滚屏才跟 URL；fresh load 滚屏不写 hash 是主题设计，不用修。
6. 翻译 agent 写报告爱用相对路径，prompt 里给绝对路径。

## 待办（本文件夹）

- [x] 放入 Multiwfn 官方手册 PDF（`Multiwfn_manual_2026.10.1.pdf`，1161 页）
- [x] 跑第 2 步转 md（`convert_mw.py` → `multiwfn_full.md` 2.8MB；标题 22/16/13pt；代码围栏 560；公式图片 351）
- [x] 行间公式 OCR 回填（23 逻辑分块 → PaddleOCR → 351/351 LaTeX，`merge_formulas.py`）
- [x] 划分章节（10 章 + 书内目录，`split_mw.py`，页标记/图片 1:1）
- [x] 翻译（11 文件，首章 pilot + 余下分段 71 段并行，全量校验页标记/图片 1:1）
- [x] 格式审计修复（4 agent 审计 + wave1/2a/2b/2c/2d/2e/2f + 公式重录；见本轮记录）
- [ ] 建站（§6 MkDocs） → 发布（§7 GitHub）
