# 主功能12：分子表面定量分析

功能概述：主功能12 对分子表面（默认 $\rho=0.001$ a.u. 电子密度等值面，即 vdW 面）上映射函数（ESP、ALIE、$EA_L$、$D(\mathbf r)$、Fukui 函数等）的分布做定量分析，输出表面极值点位置与数值、表面积/体积、平均值、方差、$\Pi$、$\nu$、MPI 等描述符，并支持原子局域表面、极值点周围区域、类盆分割三种局域分析，以及 Hirshfeld/Becke 表面与指纹图分析。计算流程为：生成包围分子的电子密度格点 → Marching Tetrahedra 构面并求体积 → 合并冗余顶点 → 计算各顶点映射函数值 → 由一、二层邻居判定极值点 → 面积加权统计输出。至少需要原子坐标；ESP 等映射函数需要 GTF（LEA 需要虚轨道）。

## 子功能：常规表面定量分析（选项 0/6、1、2、3、4、5）

说明：在主界面选映射函数与等值面定义后启动分析。默认映射函数为 ESP，默认 $\rho=0.001$ a.u. 等值面为 vdW 面；选项 6 跳过映射函数，只求体积与面积。

菜单路径：主功能12 → 选项1（等值面定义，默认 0.001）→ 选项2（映射函数，默认 ESP）→ 选项3（格点间距）→ 选项4（高级选项）→ 选项5（外部加载映射函数）→ 0 启动分析（6 为无映射函数快速版）

输入要求：至少原子坐标；ESP/ALIE 等需 GTF（大体系可用原子电荷版 ESP 加速，或选项 5 从外部文件/cube 载入映射函数值；LEA 需虚轨道，输入用 .mwfn/.fch/.molden/.gms）。

操作步骤（原始格式）：

```text
examples\phenol_631Gxx.wfn  // Phenol wavefunction produced at B3PW91/6-31G** level. For most systems this level can give acceptable result of ESP analysis. For better accuracy, def-TZVP is recommended, while more expensive def2-TZVP basis set is able to give ideal result
12  // Quantitative analysis of molecular surface
0  // Start the analysis under default settings. By default, the mapped function is ESP
```

ALIE 映射函数切换（原始格式）：

```text
examples\phenol_631Gxx.wfn  // Produced at B3PW91/6-31G** level
12  // Quantitative molecular surface analysis
2  // Reselect mapped function
2  // Choose I as mapped function
0  // Start the surface analysis.
```

D(r) 映射函数切换（原始格式）：

```text
examples\ThioformicAcid.wfn  // Thioformic acid optimized at B3LYP/6-311++G(2d,2p)
12  // Quantitative analysis of molecular surface
2  // Select mapped function
6  // Orbital overlap distance function D(r), which maximizes EDR(r;d) with respect to d
2  // Use default value of total number, start and increment of EDR exponents. Please consult Section 4.5.7 for more information.
0  // Start analysis now!
```

无映射函数只求面积体积（原始格式）：

```text
examples\dopamine.wfn  // Generated using B3LYP/6-31G* level. Commonly the quality of density at this level is absolutely adequate
12  // Quantitative analysis of molecular surface
1  // Change the definition of surface
1  // Use electron density isosurface as molecular surface
0.002  // Condensed phase vdW surface
6  // Start analysis without consideration of mapped function
```

产出：表面极小/极大点位置与数值、表面积/体积、正负区面积、$\overline{V}_S^{+/-}$、$\Pi$、$\sigma^2$、$\nu$、$\nu\sigma^2_{\mathrm{tot}}$、MPI、球形度；ALIE 只输出体积、面积、均值与方差。

来源：[3.15.1 理论](../sec-3-15-quantitative-analysis-of-molecular-surface.md)、[3.15.2 数值算法](../sec-3-15-quantitative-analysis-of-molecular-surface.md)、[3.15.3 参数和选项](../sec-3-15-quantitative-analysis-of-molecular-surface.md)、[4.12.1 苯酚 ESP](../sec-4-12-quantitative-analysis-of-molecular-surface.md)、[4.12.2 苯酚 ALIE](../sec-4-12-quantitative-analysis-of-molecular-surface.md)、[4.12.8 硫代甲酸 D(r)](../sec-4-12-quantitative-analysis-of-molecular-surface.md)、[4.12.9 多巴胺表面积](../sec-4-12-quantitative-analysis-of-molecular-surface.md)

## 子功能：局域分子表面分析（后处理 11、12、14、15）

说明：三种局域模式——(1) 按原子分解的局域表面（权重 $w_A=1-|\mathbf r-\mathbf r_A|/R_A$ 最大者归属）；(2) 特定极值点周围、映射函数值高于/低于判据且连通的区域，用于定量 σ-hole/π-hole 面积；(3) 基于类盆分割（顶点沿最大邻居爬坡归属极值点），联用 ESP 可得化学上有用的表面盆。

菜单路径：分析完成后后处理菜单 → 11（每个原子的表面性质，可导出 locsurf.pqr）→ 12（指定片段的表面性质）→ 14（极值点周围区域面积与均值，导出 selsurf.pqr）→ 15（类盆分割，导出 surfbasin.pdb）

输入要求：同常规分析（需已完成一次表面分析）。

操作步骤（原始格式，原子局域表面，丙烯醛例）：

```text
examples\acrolein.wfn  // Optimized and produced at B3LYP/6-31G** level
12  // Quantitative analysis of molecular surface
0  // Start the analysis for ESP
```

```text
11  // Output surface properties of each atom (in post-processing menu)
y  // Export surface facets to locsurf.pqr in current folder
```

σ-hole/π-hole 面积定量化（原始格式，ClPO2 例，先常规 ESP 分析，再后处理）：

```text
14  // Calculate area and function average in a region around a surface extreme
1  // Maxima (minima for negative holes)
<极值点序号>  // Select the surface extreme
0.04  // Criterion value, e.g. 0.04 a.u. for π-hole, 0.03 a.u. for σ-hole
```

产出：各原子/片段局域表面的面积与描述符（locsurf.pqr，残基序号为归属）；极值周围区域的顶点数、面积、平均值与乘积（selsurf.pqr）；每个表面盆的顶点数、面积与平均 ESP（surfbasin.pdb，B 因子为盆编号）。

来源：[3.15.2.2 局域分析](../sec-3-15-quantitative-analysis-of-molecular-surface.md)、[4.12.3 丙烯醛原子局域表面](../sec-4-12-quantitative-analysis-of-molecular-surface.md)、[4.12.10 σ-hole/π-hole 面积](../sec-4-12-quantitative-analysis-of-molecular-surface.md)、[4.12.11 类盆分析](../sec-4-12-quantitative-analysis-of-molecular-surface.md)

## 子功能：表面分析后处理与导出（选项 -3、-2、0～10、13、19）

说明：分析完成后检查、筛选与导出结果：可视化极值点；导出极值点（txt/pdb/pqr）与表面顶点（vtx.pdb/vtx.txt/vtx.pqr）；按映射函数值区间统计面积；求表面与指定点的最近/最远距离（AIM 非键半径与互穿距离）；导出映射函数格点。

菜单路径：后处理菜单 → -3（可视化表面）→ -2（导出 surf.cub）→ 0（查看结构与极值点）→ 1/2（导出 surfanalysis.txt/pdb）→ 3/4（丢弃某值范围极小/极大点）→ 6/7/8（导出 vtx.pdb/vtx.txt/vtx.pqr 与 extrema.pqr）→ 9（指定值区间面积统计）→ 10（表面与点的最近/最远距离）→ 13（映射函数格点 mapfunc.cub）→ 19（按序号删极值点）

输入要求：已完成的表面分析结果。

操作步骤（原始格式，ESP 区间统计，苯酚例）：

```text
9  // Output surface area in specific value range of mapped function
all  // All atoms are taken into the statistics (alternatively, if you input for example 2-4, then only the local surfaces corresponding to atom 2, 3 and 4 will be taken into account, see Section 4.12.3 for illustration of the concept of local molecular surface)
-30,55  // The ESP range you are interested in. Since we have already known that the minimum and the maximum ESP on the surface are -25.85 and 53.81 kcal/mol respectively, here we input a slightly larger range to enclose them
15  // The number of intervals
3  // Both the inputted and outputted units are in kcal/mol
```

非键半径与互穿距离（原始格式）：

```text
10  // Output the closest and farthest distance between the surface and a point
12  // e.g. atom O12, outputs non-bonded radius 1.701 Angstrom
10  // Again
13  // e.g. atom H13, outputs non-bonded radius 1.172 Angstrom
```

重用映射函数数据（原始格式，N-phenylpyrrole 例，第一次分析后）：

```text
7  // Export all surface vertices to vtx.txt in current folder
-1  // Return to upper-level menu
```

```text
examples\N-phenylpyrrole.fch
12  // Quantitative molecular surface analysis
5  // Loading mapped function values from external file during analysis
1  // Loading mapped function at all surface vertices from a plain text file
0  // Start the analysis
vtx.txt  // Load the mapped function values at the surface vertices from this file
```

仅用 cube 文件做表面 ESP 分析（原始格式）：

```text
density.cub  // Load cube file of electron density first
12  // Quantitative molecular surface analysis
1  // Select the way to define surface
11  // Isosurface of the grid data in memory
0.001  // Use ρ = 0.001 a.u. to define the isosurface
2  // Select mapped function
1  // ESP
5  // Set if loading mapped function values from external file
3  // The mapped function will be interpolated from an external cube file
0  // Start calculation
ESP.cub  // The cube file recording ESP
```

产出：surfanalysis.txt/pdb、vtx.pdb（B 因子为映射函数值）/vtx.txt/vtx.pqr 与 extrema.pqr、区间面积统计表、非键半径与互穿距离、surf.cub 与 mapfunc.cub。

来源：[3.15.4 后处理选项](../sec-3-15-quantitative-analysis-of-molecular-surface.md)、[4.12.1 苯酚 ESP（含统计分布、重用技巧、纯 cube 技巧）](../sec-4-12-quantitative-analysis-of-molecular-surface.md)

## 子功能：Hirshfeld/Becke 表面分析与指纹图（选项 1-5/6、2、后处理 20）

说明：Hirshfeld 表面为片段 Hirshfeld 权重 $w_P^{\mathrm{Hirsh}}=0.5$ 等值面，Becke 表面以 Becke 权重代替（只需几何与共价半径，可在密度为零的远区正常构建）；常用映射函数为 $d_{\mathrm{norm}}$、电子密度、$\mathrm{sign}(\lambda_2)\rho$；后处理选项 20 做指纹图（$d_i$ vs $d_e$）与局域接触分析。

菜单路径：主功能12 → 选项1 → 5（Hirshfeld 面）/6（Becke 面）→ 输入片段原子序号 → 选项2（映射函数，默认电子密度/前分子密度）→ 0 启动 → 后处理 20（指纹图与局域接触：选项0 全表面指纹图；选项1/2 定义 inside/outside 原子；选项3 元素对接触面积；选项4/5 导出 finger.pqr/finger_all.pqr 与 di_de.txt）

输入要求：至少原子坐标（无波函数时用前分子密度）；晶体/配合物体系（尿素团簇可由 .cif 经主功能300 → 7 → 25 提取）。

操作步骤（原始格式，Becke 表面，GC 碱基对例）：

```text
examples\GC.wfn  // Generated at M06-2X/6-31+G** level, optimized at PM7 level
12  // Quantitative molecular surface analysis
1  // Change the definition of surface
6  // Use Becke surface. You can also select 5 to use Hirshfeld surface
1-13  // The index range of the atoms you are interested in (cytosine in present case)
0  // Start calculation
```

操作步骤（原始格式，Hirshfeld 表面与指纹图，尿素晶体团簇例）：

```text
urea.cif  //.cif file of urea, please find it from Internet. PS: DO NOT manually extend it to supercell, otherwise computational cost will significantly increase
300  // Main function 300
7  // Geometry operation
25  // Extract a molecular cluster (central molecule + surrounding ones)
1  // The whole molecule containing atom 1 is taken as the central molecule, this molecule and all surrounding ureas close to it will be extracted
[Press ENTER button]  // Use recommended criterion of 1.2 to detect contact
```

```text
examples\Urea_crystal.pdb
12  // Quantitative molecular surface analysis
1  // Change surface type
5  // Use Hirshfeld surface
16,36,58,2,77,55,34,13  // The index of the atoms in the central urea
0  // Start calculation. Note that the default mapped function d_norm is used here
```

```text
20  // Fingerprint plot analysis
0  // Start fingerprint analysis
1  // Save fingerprint plot to an image file
```

局域接触指纹图（原始格式）：

```text
-1  // Return to upper level of menu
1  // Set the inside atoms to consider
[Press ENTER button]  // Do not set constraint for atomic indices
H  // The inside atoms must be hydrogen
2  // Set the outside atoms to consider
76  // The index of the oxygen in one of surrounding urea
```

VMD 画彩色等值面（原始格式）：

```text
examples\Urea_crystal.pdb
12  // Quantitative molecular surface analysis
1  // Change surface definition
5  // Use Hirshfeld surface
16,36,58,2,77,55,34,13  // The index of the atoms in the central urea
0  // Start calculation
-2  // Export the grid data used to define Hirshfeld surface as surf.cub in current folder
13  // Calculate grid data of mapped function and export it to mapfunc.cub in current folder
```

产出：表面极值与统计、指纹图 pdf（含局域接触面积）、元素对接触面积表、finger.pqr/finger_all.pqr、di_de.txt/di_de_all.txt；VMD 可画 Hirshfeld/Becke 着色等值面。

来源：[3.15.5 Hirshfeld 和 Becke 表面](../sec-3-15-quantitative-analysis-of-molecular-surface.md)、[4.12.5 GC 碱基对 Becke 表面](../sec-4-12-quantitative-analysis-of-molecular-surface.md)、[4.12.6 尿素 Hirshfeld 与指纹图](../sec-4-12-quantitative-analysis-of-molecular-surface.md)

## 实例条目

- 苯酚 vdW 表面 ESP 定量分析：主功能12 → 0；输入 .wfn（B3PW91/6-31G** 可用，更准用 def-TZVP/def2-TZVP）；输出极值位置数值、面积/体积、均值/方差/nu/Pi/MPI 等，后处理 0 可视化极值点。来源：[4.12.1](../sec-4-12-quantitative-analysis-of-molecular-surface.md)
- 表面 ESP 区间统计分布直方图：后处理 9 → 原子范围 → ESP 范围 → 区间数 → 单位；输出每段区间面积与占比。来源：[4.12.1](../sec-4-12-quantitative-analysis-of-molecular-surface.md)
- AIM 非键半径与互穿距离：后处理 10 → 原子序号；非键半径之和减键长即互穿距离。来源：[4.12.1](../sec-4-12-quantitative-analysis-of-molecular-surface.md)
- 苯酚 ALIE 表面分析：主功能12 → 2 → 2（ALIE）→ 0；表面 ALIE 最小处为亲电/自由基进攻有利位点。来源：[4.12.2](../sec-4-12-quantitative-analysis-of-molecular-surface.md)
- 丙烯醛原子局域表面解释亲核位点选择性：主功能12 → 0 → 后处理 11；比较各原子局域表面 ESP 平均值，羰基碳最正即硬亲核试剂最有利位点。来源：[4.12.3](../sec-4-12-quantitative-analysis-of-molecular-surface.md)
- 苯酚表面 Fukui 函数 f− 定量分析：主功能12 → 2 → 0（外部加载）→ 1 → 1（电子密度等值面）→ 0.01 → 0；需中性/阳离子/阴离子三套波函数（或 Fukui cube）。来源：[4.12.4](../sec-4-12-quantitative-analysis-of-molecular-surface.md)
- 基于表面 ESP 预测 FOX-7 分子晶体密度：主功能12 → 0；取 M/V 与 νσ² 代入 ρ=0.9183(M/V)＋0.0028(νσ²)＋0.0443（仅适配 B3PW91/6-31G** 与 C/H/N/O 小有机物）。来源：[4.12.7](../sec-4-12-quantitative-analysis-of-molecular-surface.md)
- 硫代甲酸表面 D(r) 定量分析：主功能12 → 2 → 6（D(r)，EDR 指数默认）→ 0；孤对紧缩处为极小、弥散处为极大。来源：[4.12.8](../sec-4-12-quantitative-analysis-of-molecular-surface.md)
- 整体与片段 vdW 表面积（多巴胺氨基占比；无波函数用前分子密度）：主功能12 → 1 → 1（气相 0.001/凝聚相 0.002）→ 6；片段以后处理 12 → 原子序号。来源：[4.12.9](../sec-4-12-quantitative-analysis-of-molecular-surface.md)
- ClPO2 的 σ-hole/π-hole 面积定量化：主功能12 → 0 → 后处理 14 → 选极大/极小与编号 → 判据（如 π 洞 0.04、σ 洞 0.03 a.u.）；判据通常取极大值约 60%。来源：[4.12.10](../sec-4-12-quantitative-analysis-of-molecular-surface.md)
- ClPO2 的 ESP 分子表面类盆分析：主功能12 → 0 → 后处理 15；输出各盆顶点数、面积与平均 ESP，surfbasin.pdb 按 Beta 着色。来源：[4.12.11](../sec-4-12-quantitative-analysis-of-molecular-surface.md)
- 小分子动力学直径估计（CO）：主功能0 确认取向 → 主功能12 → 1 → 1 → 0.0015 → 6；垂直分子轴方向跨度除以 1.025 即直径。来源：[4.12.12](../sec-4-12-quantitative-analysis-of-molecular-surface.md)
- LEA/Eatt 揭示亲电区（CH3Cl）：脚本流程（examples\\scripts\\local_EA 下 .bat＋.vmd）；LEA 取 ρ=0.01、Eatt 取 ρ=0.004 等值面着色，越负 Eatt/越正 LEA 处亲电性越强。来源：[4.12.13](../sec-4-12-quantitative-analysis-of-molecular-surface.md)
