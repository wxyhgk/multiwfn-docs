# 主功能20：弱相互作用可视化

功能概述：主功能 20 是弱相互作用可视化方法的集合，覆盖 NCI（RDG）、前分子 NCI、aNCI、IRI / IRI-π、DORI、范德华势、IGM、IGMH、aIGM、mIGM、amIGM 共 11 个子功能。仅需原子坐标的方法（前分子 NCI、IGM、mIGM、范德华势、aNCI/aIGM/amIGM）适用于大体系与动力学轨迹；需要波函数的方法（常规 NCI、DORI、IRI、IGMH）结果更严格。着色统一用 sign(λ₂)ρ 映射，VMD 脚本（RDGfill.vmd、IRIfill.vmd、DORIfill.vmd、IGM_inter/intra.vmd、aIGM.vmd）在 examples 目录下。

## 子功能 1：NCI（RDG）分析

说明：约化密度梯度 RDG 方法。RDG 定义为

$$
\mathrm{RDG}(\mathbf{r}) = \frac{1}{2(3\pi^2)^{1/3}} \frac{\left| \nabla \rho(\mathbf{r}) \right|}{\rho(\mathbf{r})^{4/3}}
$$

保留 RDG 取值 0~中等且 ρ 较小的区域即得弱相互作用区域；sign(λ₂)ρ 着色区分氢键（蓝）、范德华（绿）、空间位阻（红）。默认电子密度 ≥ 0.05 处 RDG 置 100.0 屏蔽成键区（`settings.ini` 中 `RDG_maxrho`，默认 0.05）。

菜单路径：主功能 20 → 子功能 1。

输入要求：含 GTF 的波函数文件（.wfn/.wfx/.mwfn/.fch/.molden 等）。

操作步骤（绘制颜色填充 RDG 图的最简流程）：

```text
xxx.wfn (or wfx/mwfn/fch/molden... file)  // Load input file
20  // Visual study of weak interaction
1  // NCI analysis
3  // Please properly define the grid points at this step. “High-quality grid” is usually adequate for small and medium sized system
3  // Export func1.cub and func2.cub
```

将两个 .cub 文件与 `examples\RDGfill.vmd` 移到 VMD 文件夹，启动 VMD 后在 console 输入 `source RDGfill.vmd`。默认 RDG 等值面 0.5，颜色范围 −0.035~0.02。

操作步骤（苯酚二聚体全体系实例）：

```text
examples\PhenolDimer.wfn
20  // Visual study of weak interaction
1  // NCI analysis
-10  // Set extension distance in all directions with respect to molecular boundary
0  // Because weak interaction regions only appear in internal region of present system, we do not need to leave a buffer region at system boundary, so we set the extension distance to 0 Bohr
2  // Medium-quality grid (about 512000 points). Because the spatial scope of grid data is evidently larger than last example, we need more grid points than last example, otherwise the RDG isosurfaces will look discrete
```

操作步骤（2-吡哆素 2-氨基吡啶实例）：

```text
examples\2-pyridoxine_2-aminopyridine.wfn
20  // Visual study of weak interaction
1  // NCI analysis
2  // Medium-quality grid
```

后处理：选项 −1 看 RDG–sign(λ₂)ρ 散点图；选项 1 把散点图存文件；选项 2 把散点 `output.txt` 导出（配合 `examples\scripts\RDGscatter.gnu` 用 gnuplot 画彩色散点图，命令 `gnuplot RDGscatter.gnu`）；选项 3 导出 sign(λ₂)ρ 与 RDG 的 cube（func1.cub、func2.cub）；选项 −2 把指定 sign(λ₂)ρ 范围内的 RDG 置大值以屏蔽不需要的等值面，例如：

```text
-2  // Set RDG value where sign(λ_2)ρ in within given data range
-0.035,-0.015  // The lower and upper limit of sign(λ_2)ρ
100  // Set RDG value in these regions to an arbitrarily large value to screen RDG isosurface
```

产出：散点图尖峰（峰顶近似对应 AIM 临界点）、颜色填充 RDG 等值面图；可叠加 AIM 临界点与键径（主功能 2 → 2 → 3 → 8 → −4 → 6 导出 CPs.pdb → −5 → 6 导出 paths.pdb）。

来源链接：[3.23.1](sec-3-23-visual-study-of-weak-interaction.md)、[4.20.1](sec-4-20-visual-study-of-weak-interactions.md)。

## 子功能 2：基于前分子密度的 NCI 分析

说明：以前分子密度（自由原子密度叠加）代替实际密度，免波函数、适用于大体系；其余流程与常规 NCI 完全相同。VMD 脚本为 `examples\RDGfill_pro.vmd`（默认等值/色标与 RDGfill.vmd 略有不同）。ρ > 0.1 处 RDG 置 100.0，阈值由 `settings.ini` 中 `RDGprodens_maxrho` 控制。

菜单路径：主功能 20 → 子功能 2。

输入要求：仅原子坐标（如 .pdb/.xyz）。

操作步骤（DNA 大体系实例，模式 7 定格点盒）：

```text
examples\DNA.pdb
20  // Visual study of weak interaction
2  // NCI analysis based on promolecular density
7  // Use mode 7 for defining grid data
84,565  // Use midpoint of atom 84 and 565 as center of grid data. You can view molecule structure in your favourite visualization tool to find two proper atoms used to define center
120,120,120  // Because the spatial scope of grid data is large, we need relatively large number of grid points, otherwise the grid spacing will be too large, which results in bad quality of RDG isosurfaces
9,9,9  // Set the extension distances in all directions to 9 Bohr
```

也可用模式 10 在 GUI 窗口中交互式设置盒子。格点算完后选项 3 导出 func1.cub/func2.cub，用 `RDGfill_pro.vmd` 绘图。

产出：大体系弱相互作用填色 RDG 图（如 DNA 相邻碱基对 π–π 堆积大扁平等值面、每对碱基两个强氢键）。

来源链接：[3.23.2](sec-3-23-visual-study-of-weak-interaction.md)、[4.20.2](sec-4-20-visual-study-of-weak-interactions.md)。

## 子功能 3：平均 NCI（aNCI）分析

说明：把 NCI 推广到动力学轨迹：对多帧平均密度求平均约化密度梯度 aRDG

$$
\mathrm{aRDG}(\mathbf{r}) = \frac{1}{2(3\pi^2)^{1/3}} \frac{\left| \nabla \overline{\rho}(\mathbf{r}) \right|}{\left[ \overline{\rho}(\mathbf{r}) \right]^{4/3}}
$$

λ₂ 取平均密度 Hessian 的第二本征值；热涨落指数 $\mathrm{TFI}(\mathbf{r}) = std[\rho(\mathbf{r})]/\overline{\rho}(\mathbf{r})$ 表征稳定性。强制使用前分子近似。注：一般不建议用 aNCI，多数情形 amIGM（子功能 −12）是更好的选择。

菜单路径：主功能 20 → 子功能 3。

输入要求：多帧 .xyz 轨迹（感兴趣分子位置固定、远离盒子边界）；至少 500 帧（50 帧太少）。

操作步骤（体相水 MD 实例）：

```text
wat.xyz
20  // Visual study of weak interaction
3  // aNCI analysis
1,1000  // The range of the frames to be analyzed
7
301,301  // Using atom 301 (the oxygen of the frozen water) as the box center of the grid data
80,80,80  // The number of grid points on each side
4.5,4.5,4.5  // Extend 4.5 Bohr in each side
```

计算完成后选项 1 看平均 RDG–平均 sign(λ₂)ρ 散点图；选项 6 导出 avgRDG.cub/avgsl2r.cub；选项 7 导出热涨落指数 thermflu.cub（需重算每帧密度，耗时）。VMD 脚本为 `examples\aNCI` 下的 avgRDG.vmd / avgRDG_TFI.vmd。降噪可用主功能 13 筛除远离选定原子的格点：

```text
avgRDG.cub
13  // Process grid data
13  // Set the value of the grid points far away from specific atoms
1.5  // If the distance between a grid point and any selected atoms is longer than 1.5 times of vdW radius of corresponding atom, then the value of the grid point will be set as given value
100  // An arbitrarily large value (should be larger than the isovalue of the RDG isosurfaces)
2  // Inputting selected atoms by hand
301-303  // The indices of the atoms are 301, 302 and 303
0  // Export the updated grid data to a new cube file
avgRDG.cub  // The name of the new cube file
```

产出：平均 RDG 等值面（等值 0.25）+ TFI 着色图；蓝色稳定（氢键给体）、红色不稳定（vdW 区）。

来源链接：[3.23.3](sec-3-23-visual-study-of-weak-interaction.md)、[4.20.3](sec-4-20-visual-study-of-weak-interactions.md)。

## 子功能 4：IRI 与 IRI-π 分析

说明：相互作用区域指示函数

$$
IRI(\mathbf{r})=\left|\nabla\rho(\mathbf{r})\right|/\left[\rho(\mathbf{r})\right]^{a}
$$

a 取 `settings.ini` 中 `uservar`（0 即推荐值 1.1）；ρ ≤ `IRI_rhocut`（默认 0.00005 a.u.）处 IRI 置大值 5。推荐等值面 1.0，同时揭示化学键与弱相互作用；定义更简单、比 DORI 更便宜、图形效果显著更好。IRI-π：计算 IRI 前把非 π 轨道占据数置零。

菜单路径：主功能 20 → 子功能 4。

输入要求：原子坐标 + GTF。

操作步骤（苯酚二聚体填色 IRI 图）：

```text
examples\PhenolDimer.wfn
20  // Visual study of weak interaction
4  // IRI analysis
3  // High-quality grid
3  // Export cube file
```

把 func1.cub、func2.cub 与 `examples\IRIfill.vmd` 移到 VMD 文件夹，`source IRIfill.vmd` 绘图。选项 9 屏蔽共价区（sign(λ₂)ρ < −0.1 a.u. 处 IRI 置 100）只看非共价区；选项 2 导出散点 output.txt，配合 `examples\scripts\IRIscatter.gnu`（`gnuplot IRIscatter.gnu`）画填色散点图。

操作步骤（GC 碱基对 IRI 平面图，主功能 4 → 24）：

```text
examples\GC.wfn
4  // Plot plane map
24  // IRI
1  // Color-filled map
[Press ENTER button]  // Use default number of grids
0  // Modify extension distance
1  // 1 Bohr
1  // XY plane, which is the plane all atoms are
0  // Z=0
```

产出：sign(λ₂)ρ 着色 IRI 等值面、IRI–sign(λ₂)ρ 散点图、IRI 平面图；IRI 对应第 24 个实空间函数，可做拓扑/盆分析。

来源链接：[3.23.8](sec-3-23-visual-study-of-weak-interaction.md)、[4.20.4](sec-4-20-visual-study-of-weak-interactions.md)。

## 子功能 5：DORI 分析

说明：密度重叠区域指示函数

$$
\mathrm{DORI}(\mathbf{r}) = \frac{\theta(\mathbf{r})}{1 + \theta(\mathbf{r})}
$$

其中 $\theta(\mathbf{r}) = [\nabla(\nabla \rho(\mathbf{r}) / \rho(\mathbf{r}))^2]^2 / [\nabla \rho(\mathbf{r}) / \rho(\mathbf{r})]^6$，取值 [0,1]，单个函数同时显示共价与非共价区。作者明确更推荐 IRI（定义简单、更便宜、图形更好）。

菜单路径：主功能 20 → 子功能 5（实例中亦经子功能 4 进入，流程相同）。

输入要求：原子坐标 + GTF。

操作步骤（苯酚二聚体）：

```text
examples\PhenolDimer.wfn
20  // Visual study of weak interaction
4  // DORI analysis
3  // High-quality grid
3  // Export cube file
```

把 func1.cub、func2.cub 与 `examples\DORIfill.vmd` 移到 VMD 文件夹，`source DORIfill.vmd` 绘图（默认等值 0.95）。

产出：sign(λ₂)ρ 着色 DORI 等值面图。

来源链接：[3.23.4](sec-3-23-visual-study-of-weak-interaction.md)、[4.20.5](sec-4-20-visual-study-of-weak-interactions.md)。

## 子功能 6：范德华势可视化

说明：基于 UFF 参数（探针原子由 `settings.ini` 中 `ivdwprobe` 指定，默认碳；设 0 则运行时输入元素名），计算 $V^{\mathrm{vdW}}$ / $V^{\mathrm{repul}}$ / $V^{\mathrm{disp}}$ 格点并可视化等值面或导出 cube；分别对应自定义函数 92/93/94。

$$
V^{\mathrm{vdW}}(\mathbf{r})=V^{\mathrm{repul}}(\mathbf{r})+V^{\mathrm{disp}}(\mathbf{r})=\sum_{A}\varepsilon_{AB}\left(\frac{R_{AB}^{0}}{\left|\mathbf{R}_{A}-\mathbf{r}\right|}\right)^{12}+\sum_{A}\left[-2\varepsilon_{AB}\left(\frac{R_{AB}^{0}}{\left|\mathbf{R}_{A}-\mathbf{r}\right|}\right)^{6}\right]
$$

菜单路径：主功能 20 → 子功能 6。

输入要求：仅原子坐标。

操作步骤：

```text
examples\helicene.xyz
20  // Visual study of weak interaction
6  // Visualization of van der Waals potential
3  // High-quality grid (the computational cost of vdW potential is extremely low, therefore we use relatively good grid quality here)
```

后处理选项可视化等值面或导出 cube；自定义函数 92/93/94 可在主功能 4 画平面图（色标范围如 −0.8~0.8 kcal/mol）、主功能 17 做盆分析找极小点（选项 −3 看吸引子信息，−4 导出 attractors.pdb/pqr/txt/gjf，用 resid 1 选全局极小点）。

产出：范德华势等值面/平面图、极小点文件。

来源链接：[3.23.7](sec-3-23-visual-study-of-weak-interaction.md)、[4.20.6](sec-4-20-visual-study-of-weak-interactions.md)。

## 子功能 10：IGM 分析

说明：基于前分子密度的独立梯度模型。$\delta g = g^{\mathrm{IGM}} - g$，$\delta g^{\mathrm{inter}}$ / $\delta g^{\mathrm{intra}}$ 分别揭示片段间/片段内相互作用；BCP 处 δg 与强度正相关；原子对指标 δG 与 IBSIW（$IBSIW(i,j) = 100\,\delta G_{i,j}^{\mathrm{pair}}/(d_{i,j})^2$）定量贡献。相对 NCI 的优势：片段间/内可分离、只依赖几何、等值面更光滑、可定量原子/原子对贡献。

菜单路径：主功能 20 → 子功能 10。

输入要求：仅原子坐标（.xyz/.pdb/.mol 或波函数文件）；几何须已优化。

操作步骤（GC 碱基对，定义两片段并绘图）：

```text
examples\GC.pdb
20  // Visual study of weak interactions
10  // IGM analysis
2  // Define two fragments
1-13  // Range of atoms in the first base
14-29  // Range of atoms in the second base (you can also input c here to define the rest of the present system as the second fragment)
```

格点算完后处理：−1 画 δg/δg_inter/δg_intra–sign(λ₂)ρ 散点图；2 导出散点文本；3 导出 cube（sl2r.cub、dg.cub、dg_inter.cub、dg_intra.cub），用 `examples\IGM_inter.vmd` / `IGM_intra.vmd`（`source IGM_inter.vmd`）绘图；4 在 Multiwfn 内看等值面；5/7/8 按 sign(λ₂)ρ 范围置零屏蔽；6 算定量指标（输出 atmdg.txt、IBSIW.txt，可选 atmdg.pdb 按 beta/occupancy 着色找热点原子）。

操作步骤（三聚体多片段，噁唑烷酮三聚体）：

```text
examples\oxazolidinone_trimer.xyz
20  // Visual study of weak interactions
10  // IGM analysis
3   // Define three fragments
1-11  // Fragment 1: Monomer 1
12-22  // Fragment 2: Monomer 2
```

操作步骤（C₆₀–晕苯二聚体）：

```text
20  // Visual study of weak interactions
10  // IGM analysis
2   // Define two fragments
1-60  // C_60 is fragment 1
c  // Other part, namely coronene, is fragment 2
```

产出：δg 等值面/平面图（主功能 4 → 22 / 主功能 5 → 22）、填色 δg_inter/intra 图、atmdg.txt / IBSIW.txt / atmdg.pdb。

来源链接：[3.23.5](sec-3-23-visual-study-of-weak-interaction.md)、[4.20.10](sec-4-20-visual-study-of-weak-interactions.md)。

## 子功能 11：IGMH 分析

说明：基于 Hirshfeld 分区的 IGM（${\rho}_{i}^{\mathrm{Hirsh}}=\rho w_i$），sign(λ₂)ρ 恒用实际密度；等值面更薄、着色更合理、物理意义更严格，对化学键也有效。只要成本可负担，总建议用 IGMH 代替 IGM。δg_inter 亦为第 91 号自定义函数（先经隐藏功能 1000 选项 16 定义两片段）。

菜单路径：主功能 20 → 子功能 11。

输入要求：含 GTF 的波函数文件（.wfn/.fch/.mwfn/.molden 等）。

操作步骤（2-吡哆素 2-氨基吡啶二聚体）：

```text
examples\2-pyridoxine_2-aminopyridine.wfn  // Since IGMH relies on wavefunction information, therefore you should use such as .wfn, .fch, .mwfn, .molden, etc. as input file
20  // Visual study of weak interaction
11  // IGMH analysis
2  // Define two fragments
1-12  // Atom indices in fragment 1
13-25  // Atom indices in fragment 2
```

后处理与 IGM 完全相同；导出 sl2r.cub + dg_inter.cub 后 `source IGM_inter.vmd` 绘图。省时技巧：`settings.ini` 中 `IGMvdwscl` 设 2.0 只算片段间重叠区格点（此时只能画 δg_inter）。

产出：IGMH 填色等值面图、原子/原子对 δg 指标。

来源链接：[3.23.6](sec-3-23-visual-study-of-weak-interaction.md)、[4.20.11](sec-4-20-visual-study-of-weak-interactions.md)。

## 子功能 12：平均 IGM（aIGM）分析

说明：标准 IGM 向动态环境的扩展。图形效果差得多，作者明确建议一律改用 amIGM（子功能 −12）。

菜单路径：主功能 20 → 子功能 12。

输入要求：多帧原子坐标。

操作步骤：用法同 amIGM，见子功能 −12 实例，唯一区别是选子功能 12 而不是 −12。

产出：平均 δg 相关格点（效果不如 amIGM）。

来源链接：[3.23.9](sec-3-23-visual-study-of-weak-interaction.md)。

## 子功能 −10：修正 IGM（mIGM）分析

说明：以前分子密度代替实际密度、其余与 IGMH 完全一样计算；只依赖坐标、成本与 IGM 相当，效果接近 IGMH。无法用 IGMH 时（太贵或无波函数）的最佳替代。

菜单路径：主功能 20 → 子功能 −10。

输入要求：仅原子坐标。

操作步骤（封端苯丙氨酸三聚体）：

```text
examples\phenylalanineresiduestrimer.xyz is optimized trimer of capped phenylalanine, we use mIGM to reveal the interactions within it. Boot up Multiwfn and load this file, then input
20  // Visual study of weak interaction
-10  // mIGM analysis
3  // Define three fragments
1-29  // Atom indices in fragment 1 (the first monomer)
30-40,52,53,56,57,63-65,77-87  // Atom indices in fragment 2 (the second monomer)
c  // All other atoms (the third monomer)
4  // Manually input grid spacing
0.2  // Grid spacing of 0.2 Bohr is sufficient to obtain a smooth enough image
3  // Output cube files to current folder
```

把 dg_inter.cub + sl2r.cub 移到 VMD 文件夹，`source IGM_inter.vmd`，等值改为 0.07。

产出：mIGM 填色等值面图、原子/原子对 δg 指标。

来源链接：[3.23.10](sec-3-23-visual-study-of-weak-interaction.md)、[4.20.12](sec-4-20-visual-study-of-weak-interactions.md)。

## 子功能 −12：平均修正 IGM（amIGM）分析

说明：mIGM 向动态环境的扩展，定义平均片段间函数 $\overline{\delta g}^{\mathrm{inter}}=\langle\delta g^{\mathrm{mIGM,inter}}\rangle$，平均 sign(λ₂)ρ 基于平均前分子密度；标准差与 $TFI^{\mathrm{amIGM}} = std(\delta g^{\mathrm{inter}})/\overline{\delta g}^{\mathrm{inter}}$ 表征稳定性。

菜单路径：主功能 20 → 子功能 −12。

输入要求：多帧 .xyz 轨迹（关键分子冻结固定，至少 500 帧；片段 1 应为固定的关键区域，`amIGMvdwscl`=2 默认加速安全）。

操作步骤（苯酚–体相水实例）：

```text
20  // Visual study of weak interactions
-12  //amIGM analysis
2  //Define two fragments for amIGM. If you define n fragments, then amIGM will reveal all interactions between the n fragments
1-13  //Atomic indices of fragment 1, corresponding to the phenol
c  //The rest of atoms (waters) is defined as fragment 2
1,1000  //Consider 1 to 1000 frames
11  //Because the interactions of phenol-water occur in various regions around phenol, the box containing the grids to be calculated should cover the entire phenol, we choose mode 11 to realize this aim, namely we will select a set of atoms, set extension distance around them and grid spacing
1-13  //The atoms for defining the box
3 A  //Extension distance is set to 3 Å
[Press ENTER button]  //Grid spacing is set to the default 0.2 Bohr, which is adequate of obtaining fine enough amIGM maps
```

后处理选项 3 导出 avgdg_inter.cub / avgsl2r.cub，用 `examples\aIGM.vmd`（`source aIGM.vmd`，等值如 0.003）绘图；选项 8 生成标准差与 TFI_amIGM 格点（stddg_inter.cub、TFI_amIGM.cub，脚本 aIGM_TFI.vmd）。

产出：平均 δg_inter 填色等值面图、稳定性着色图。

来源链接：[3.23.11](sec-3-23-visual-study-of-weak-interaction.md)、[4.20.13](sec-4-20-visual-study-of-weak-interactions.md)。
