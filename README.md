# Multiwfn 中文手册（社区译本）

Multiwfn 官方手册的中文翻译（90 篇）+ 术语表 + 菜单索引 + 应用导览 + 避坑 FAQ + 静态浏览站。

> 原文 © Tian Lu / Beijing Kein Research Center for Natural Sciences（http://sobereva.com/multiwfn）。
> 本仓库为未获官方授权的社区翻译整理，仅供学习交流；引用请同时引用原手册与 Multiwfn 原始论文。

## 目录结构

- `manual_md_zh/` —— 中文译文 Markdown（含 `assets/` 图片、`menu/` 29 个分功能详表）
  - `GLOSSARY.md` 术语表（1436 条） · `MENU_INDEX.md` 菜单索引（485 条）
  - `APPLIED_INDEX.md` 应用导览 · `EXP_GUIDE.md` 实验-计算对照
  - `FAQ.md` 避坑表 · `PARAMS.md` 参数关键词表
- `sitegen/` —— 静态站生成器（Node marked 预渲染 + MathJax + 离线搜索）
- `docs/` —— 构建产物（供 GitHub Pages 直接发布，`/docs` 目录模式）

## 构建与预览

```bash
cd sitegen && npm i && node gen.mjs   # 输出到 ../docs
cd ../docs && python3 -m http.server 8123
```

## 翻译约定

- 只译自然语言正文；公式 `$…$/$$…$$`、代码块、命令、路径、URL、菜单编号逐字符保留
- 术语首次出现用“中文 (English)”；内部链接锚点与译文标题自洽
