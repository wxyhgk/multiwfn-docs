# Multiwfn 在线手册（离线整理版）

> 来源：http://sobereva.com/multiwfn/manual/ ，由网页自动抓取并转换为 Markdown。
> 公式：行内 `$...$`，行间 `$$...$$`（由 MathJax 源码还原）。

## 目录

- [主页 (Home)](README.md)
- [1. 概述 (Overview)](sec-1-overview.md)
- [2. 通用信息 (General information)](2-general-information.md)
  - [2.1 安装 (Install)](sec-2-1-install.md)
  - [2.2 使用 Multiwfn (Using Multiwfn)](sec-2-2-using-multiwfn.md)
  - [2.3 Multiwfn 的文件 (Files of Multiwfn)](sec-2-3-files-of-multiwfn.md)
  - [2.4 并行实现 (Parallel implementation)](sec-2-4-parallel-implementation.md)
  - [2.5 输入文件与波函数类型 (Input files and wavefunction types)](sec-2-5-input-files-and-wavefunction-types.md)
  - [2.6 实空间函数 (Real space functions)](sec-2-6-real-space-functions.md)
  - [2.7 用户自定义实空间函数 (User-defined real space function)](sec-2-7-user-defined-real-space-function.md)
  - [2.8 图形格式与图像尺寸 (Graphic formats and image size)](sec-2-8-graphic-formats-and-image-size.md)
  - [2.9 周期性体系的分析 (Analysis of periodic systems)](sec-2-9-analysis-of-periodic-systems.md)
- [3. 功能 (Functions)](3-functions.md)
  - [3.2 显示分子结构并查看轨道/等值面 (0) (Showing molecular structure and viewing orbitals / isosurfaces (0))](sec-3-2-showing-molecular-structure.md)
  - [3.3 输出某一点处的所有性质 (1) (Outputting all properties at a point (1))](sec-3-3-outputting-all-properties-at-a-point.md)
  - [3.4 在一条线上输出并绘制指定性质 (3) (Outputting and plotting specific property in a line (3))](sec-3-4-outputting-and-plotting-specific-property-in-a-line.md)
  - [3.5 在一个平面上输出并绘制指定性质 (4) (Outputting and plotting specific property in a plane (4))](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md)
  - [3.6 在空间范围内输出并绘制指定性质 (5) (Outputting and plotting specific property within a spatial region (5))](sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md)
  - [3.7 自定义操作、前分子与变形性质 (选项 0、-1、-2) (Custom operation, promolecular and deformation properties (options 0, -1, -2))](sec-3-7-custom-operation-promolecular-and-deformation-properties.md)
  - [3.8 检查与修改波函数 (6) (Checking & modifying wavefunction (6))](sec-3-8-checking-and-modifying-wavefunction.md)
  - [3.9 布居分析与原子电荷计算 (7) (Population analysis and calculation of atomic charges (7))](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md)
  - [3.10 轨道组成分析 (8) (Orbital composition analysis (8))](sec-3-10-orbital-composition-analysis.md)
  - [3.11 键级分析 (9) (Bond order analysis (9))](sec-3-11-bond-order-analysis.md)
  - [3.12 绘制态密度 (DOS)、光电子能谱 (PES) 与 COHP (10) (Plotting density-of-states (DOS), photoelectron spectrum (PES), and COHP (10))](sec-3-12-plotting-density-of-states-pes-and-cohp.md)
  - [3.13 绘制红外、拉曼、紫外-可见、ECD、VCD、ROA 与 NMR 光谱 (11) (Plotting IR, Raman, UV-Vis, ECD, VCD, ROA and NMR spectra (11))](sec-3-13-plotting-spectra.md)
  - [3.14 拓扑分析 (2) (Topology analysis (2))](sec-3-14-topology-analysis.md)
  - [3.15 分子表面的定量分析 (12) (Quantitative analysis of molecular surface (12))](sec-3-15-quantitative-analysis-of-molecular-surface.md)
  - [3.16 处理格点数据 (13) (Processing grid data (13))](sec-3-16-processing-grid-data.md)
  - [3.17 自适应自然密度划分 (AdNDP) 分析 (14) (Adaptive natural density partitioning (AdNDP) analysis (14))](sec-3-17-adaptive-natural-density-partitioning-analysis.md)
  - [3.18 模糊原子空间分析 (15) (Fuzzy atomic space analysis (15))](sec-3-18-fuzzy-atomic-space-analysis.md)
  - [3.19 电荷分解分析与绘制轨道相互作用图 (16) (Charge decomposition analysis and plotting orbital interaction diagram (16))](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md)
  - [3.20 盆分析 (17) (Basin analysis (17))](sec-3-20-basin-analysis.md)
  - [3.21 电子激发分析 (18) (Electron excitation analysis (18))](sec-3-21-electron-excitation-analysis.md)
  - [3.22 轨道定域化分析 (19) (Orbital localization analysis (19))](sec-3-22-orbital-localization-analysis.md)
  - [3.23 弱相互作用的可视化研究 (20) (Visual study of weak interaction (20))](sec-3-23-visual-study-of-weak-interaction.md)
  - [3.24 能量分解分析 (21) (Energy decomposition analysis (21))](sec-3-24-energy-decomposition-analysis.md)
  - [3.25 概念密度泛函理论 (CDFT) 分析 (22) (Conceptual density functional theory (CDFT) analysis (22))](sec-3-25-conceptual-density-functional-theory-analysis.md)
  - [3.26 扩展过渡态-化学价自然轨道 (ETS-NOCV) 分析 (Extended Transition State - Natural Orbitals for Chemical Valence (ETS-NOCV) analysis)](sec-3-26-ets-nocv-analysis.md)
  - [3.27 (超)极化率分析 (24) ((Hyper)polarizability analysis (24))](sec-3-27-hyperpolarizability-analysis.md)
  - [3.28 电子离域与芳香性分析 (25) (Electron delocalization and aromaticity analyses (25))](sec-3-28-electron-delocalization-and-aromaticity-analyses.md)
  - [3.100 其它功能，第 1 部分 (100) (Other functions, part 1 (100))](sec-3-100-other-functions-part-1.md)
  - [3.200 其它功能，第 2 部分 (200) (Other functions, part 2 (200))](sec-3-200-other-functions-part-2.md)
  - [3.300 其它功能，第 3 部分 (300) (Other functions, part 3 (300))](sec-3-300-other-functions-part-3.md)
- [4. 教程与实例 (Tutorials and Examples)](4-tutorials-and-examples.md)
  - [序言与输入文件的生成 (Prologue and generation of input files)](sec-4-prologue-and-generation-of-input-files.md)
  - [4.0 查看轨道与结构 (View orbitals and structure)](sec-4-0-view-orbitals-and-structure.md)
  - [4.1 计算某一点处的性质 (Calculate properties at a point)](sec-4-1-calculate-properties-at-a-point.md)
  - [4.2 拓扑分析 (Topology analysis)](sec-4-2-topology-analysis.md)
  - [4.3 在一条线上输出并绘制各种性质 (Output and plot various properties in a line)](sec-4-3-output-and-plot-various-properties-in-a-line.md)
  - [4.4 在一个平面上输出并绘制各种性质 (Output and plot various properties in a plane)](sec-4-4-output-and-plot-various-properties-in-a-plane.md)
  - [4.5 生成格点数据并查看等值面图 (Generate grid data and view isosurface map)](sec-4-5-generate-grid-data-and-view-isosurface-map.md)
  - [4.6 修改并检查波函数 (Modify and check wavefunction)](sec-4-6-modify-and-check-wavefunction.md)
  - [4.7 布居分析与原子电荷计算 (Population analysis and atomic charge calculation)](sec-4-7-population-analysis-and-atomic-charge-calculation.md)
  - [4.8 分子轨道组成分析 (Molecular orbital composition analysis)](sec-4-8-molecular-orbital-composition-analysis.md)
  - [4.9 键级分析 (Bond order analysis)](sec-4-9-bond-order-analysis.md)
  - [4.10 绘制态密度 (DOS) 图 (Plot density-of-states (DOS) maps)](sec-4-10-plot-density-of-states-dos-maps.md)
  - [4.11 绘制各种光谱 (Plot various kinds of spectra)](sec-4-11-plot-various-kinds-of-spectra.md)
  - [4.12 分子表面的定量分析 (Quantitative analysis of molecular surface)](sec-4-12-quantitative-analysis-of-molecular-surface.md)
  - [4.13 处理格点数据 (Process grid data)](sec-4-13-process-grid-data.md)
  - [4.14 自适应自然密度划分 (AdNDP) 分析 (Adaptive natural density partitioning (AdNDP) analysis)](sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)
  - [4.15 模糊原子空间分析 (Fuzzy atomic space analysis)](sec-4-15-fuzzy-atomic-space-analysis.md)
  - [4.16 电荷分解分析与绘制轨道相互作用图 (Charge decomposition analysis and plotting orbital interaction diagram)](sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md)
  - [4.17 盆分析 (Basin analysis)](sec-4-17-basin-analysis.md)
  - [4.18 电子激发分析 (Electron excitation analysis)](sec-4-18-electron-excitation-analysis.md)
  - [4.19 轨道定域化分析 (Orbital localization analysis)](sec-4-19-orbital-localization-analysis.md)
  - [4.20 弱相互作用的可视化研究 (Visual study of weak interactions)](sec-4-20-visual-study-of-weak-interactions.md)
  - [4.21 能量分解分析 (Energy decomposition analysis)](sec-4-21-energy-decomposition-analysis.md)
  - [4.22 概念密度泛函理论 (CDFT) 分析实例 (Examples of conceptual density functional theory (CDFT) analysis)](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md)
  - [4.23 ETS-NOCV 分析实例 (Examples of ETS-NOCV analysis)](sec-4-23-examples-of-ets-nocv-analysis.md)
  - [4.24 (超)极化率分析实例 (Examples of (hyper)polarizability analyses)](sec-4-24-examples-of-hyperpolarizability-analyses.md)
  - [4.25 电子离域与芳香性分析实例 (Examples of electron delocalization and aromaticity analyses)](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md)
  - [4.100 其它功能 (第 1 部分) (Other functions (Part 1))](sec-4-100-other-functions-part-1.md)
  - [4.200 其它功能 (第 2 部分) (Other functions (Part 2))](sec-4-200-other-functions-part-2.md)
  - [4.300 其它功能 (第 3 部分) (Other functions (Part 3))](sec-4-300-other-functions-part-3.md)
  - [4.A 专题与高级教程 (Special topics and advanced tutorials)](sec-4-A-special-topics-and-advanced-tutorials.md)
  - [5.1 使 Multiwfn 支持更多量子化学程序 (Make Multiwfn support more quantum chemistry programs)](sec-5-1-make-multiwfn-support-more-quantum-chemistry-programs.md)
  - [5.2 在静默模式下运行 Multiwfn (Running Multiwfn in silent mode)](sec-5-2-running-multiwfn-in-silent-mode.md)
  - [5.3 在批处理模式下运行 Multiwfn (Running Multiwfn in batch mode)](sec-5-3-running-multiwfn-in-batch-mode.md)
  - [5.4 从命令行窗口复制输出到剪贴板 (Copy outputs from command-line window to clipboard)](sec-5-4-copy-outputs-from-command-line-window-to-clipboard.md)
  - [5.5 使命令行窗口能够记录更多输出 (Make command-line window capable of recording more outputs)](sec-5-5-make-command-line-window-capable-of-recording-more-outputs.md)
  - [5.6 将文件快速载入 Multiwfn (Rapidly load a file into Multiwfn)](sec-5-6-rapidly-load-a-file-into-multiwfn.md)
  - [5.7 利用 Gaussian 软件包中的 cubegen 工具以减少计算时间 (Make use of cubegen utility in Gaussian package to reduce computational time)](sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md)
  - [5.8 获得理想绘图质量的一些技巧 (Some tips on achieving ideal drawing quality)](sec-5-8-some-tips-on-achieving-ideal-drawing-quality.md)
  - [6.1 在 Windows 下为 Gaussian 设置运行环境 (Setting up running environment for Gaussian in Windows)](sec-6-1-setting-up-running-environment-for-gaussian-in-windows.md)
  - [6.2 计算实空间函数的例程 (The routines for evaluating real space functions)](sec-6-2-the-routines-for-evaluating-real-space-functions.md)
  - [6.3 内置原子密度的细节 (Detail of built-in atomic densities)](sec-6-3-detail-of-built-in-atomic-densities.md)
  - [6.4 关于为涉及赝势的波函数补充内层核电子密度的细节 (Details about supplying inner-core electron density for the wavefunctions involving pseudopotential)](sec-6-4-details-about-supplying-inner-core-electron-density.md)
  - [6.5 检查波函数的合理性 (Check sanity of wavefunction)](sec-6-5-check-sanity-of-wavefunction.md)
  - [6.6 特殊功能 (Special functions)](sec-6-6-special-functions.md)
  - [6.7 关于向 Multiwfn 提供 Fock/KS 矩阵 (About providing Fock/KS matrix to Multiwfn)](sec-6-7-about-providing-fock-ks-matrix-to-multiwfn.md)

---

# 主页 (Home)

> **关于本手册 (About this manual)**
>
> 本在线手册对应最新版本的 Multiwfn 程序。PDF 格式的手册可从 Multiwfn 网站的 "Download" 页面获取：<http://sobereva.com/multiwfn>

**[Multiwfn](http://sobereva.com/multiwfn)**

– *多功能波函数分析仪 (A Multifunctional Wavefunction Analyzer)* –

**软件手册 (Software Manual)**

**附带第 4 章中的教程与丰富实例 (with tutorials and abundant examples in [Chapter 4](4-tutorials-and-examples.md))**

**Multiwfn 官方网站：<http://sobereva.com/multiwfn>**

**[Tian Lu](http://sobereva.com/Tian_Lu.html)**

sobereva@sina.com

北京 Kein 自然科学研究中心 (Beijing Kein Research Center for Natural Sciences) (<http://www.keinsci.com>)

------------------------------------------------------------------------

## **所有用户必读 (ALL USERS MUST READ)**

1.  欢迎在 Multiwfn 英文论坛 (<http://sobereva.com/wfnbbs>) 或 Multiwfn 中文论坛 (<http://bbs.keinsci.com/wfn>) 发帖，咨询任何关于使用 Multiwfn 的问题！我总是愿意尽我所能帮助每一位 Multiwfn 用户！！！\`\\(^∇^)/\`

2.  若想非常快速地了解如何用 Multiwfn 完成很常见的任务，请查看 Multiwfn 二进制包中的 "Multiwfn quick start.pdf"。

3.  入门的最佳 (BEST) 方式是通读第 [1](sec-1-overview.md) 章、第 [2](2-general-information.md) 章的 [2.1](sec-2-1-install.md)\~[2.5](sec-2-5-input-files-and-wavefunction-types.md) 节，然后跟着第 [4](4-tutorials-and-examples.md) 章中的教程学习。之后若想进一步学习 Multiwfn 的理论背景与细节，再读第 [2](2-general-information.md) 章的 [2.6](sec-2-6-real-space-functions.md)\~[2.8](sec-2-8-graphic-formats-and-image-size.md) 节和第 [3](3-functions.md) 章。注意第 [4](4-tutorials-and-examples.md) 章中的教程与实例只覆盖最重要、最常用的功能，而不是 Multiwfn 的全部功能。

4.  Multiwfn 的不同功能需要不同类型的输入文件，请认真阅读 [2.5](sec-2-5-input-files-and-wavefunction-types.md) 节中的说明。

5.  通常 Multiwfn 运行在交互模式下，但 Multiwfn 也可以运行在命令行模式下，编写 shell 脚本让 Multiwfn 处理大量输入文件非常方便。细节见 [5.2](sec-5-2-running-multiwfn-in-silent-mode.md) 和 [5.3](sec-5-3-running-multiwfn-in-batch-mode.md) 节。

6.  如果你不知道如何把 Multiwfn 的输出从命令行窗口复制到纯文本文件，请参考 [5.4](sec-5-4-copy-outputs-from-command-line-window-to-clipboard.md) 节。如果你不知道如何增大 Windows 系统命令行窗口的屏幕缓冲区，请参考 [5.5](sec-5-5-make-command-line-window-capable-of-recording-more-outputs.md) 节。

7.  如果在 Multiwfn 调用 Gaussian 时屏幕上出现 "No executable for file l1.exe" 错误，应先设置 Gaussian 环境变量。Windows 版本可参考[附录 1 (Appendix 1)](sec-6-1-setting-up-running-environment-for-gaussian-in-windows.md)。（注：Multiwfn 中的大多数功能都不需要在本地安装 Gaussian）

8.  本手册以及 Multiwfn 提示信息中所说的"当前文件夹 (current folder)"是指你调用 Multiwfn 时所在的路径。如果你是在 Windows 平台下通过点击可执行文件图标启动 Multiwfn 的，"当前文件夹"就是含有 Multiwfn 可执行文件的文件夹。在命令行模式下，如果你调用 Multiwfn 时位于 "D:\study\\" 目录，那么 "D:\study\\" 就是"当前目录 (current directory)"。

9.  请经常访问 Multiwfn 网站并将程序更新到最新版本。Multiwfn 一直处在活跃开发中，有用的新功能被频繁加入，程序错误被持续修复，效率被持续提升。

------------------------------------------------------------------------

## **Linux 与 MacOS 用户必读 (Linux and MacOS USERS MUST READ)**

1.  如果你是 Multiwfn 新手，强烈建议使用 Windows 版本，因为该版本的 Multiwfn 比其它版本更稳定，图形界面的显示效果最好，而且不需要配置系统。

2.  Linux 和 Mac OS 版本的 Multiwfn 的安装方法分别见 [2.1.2](sec-2-1-install.md#212-linux-版) 和 [2.1.3](sec-2-1-install.md#213-macos-版) 节。

3.  在图形界面窗口中显示等值面时透明风格不起作用。但如果你选择把图形保存为图像文件，生成的图形文件中透明等值面可以正常渲染。

4.  不建议使用 Mac OS 版本，某些功能可能无法正常工作。
