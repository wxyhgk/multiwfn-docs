# 主功能15：模糊原子空间分析

功能概述：主功能15 在模糊原子空间（连续划分，权重归一；支持 Hirshfeld/Hirshfeld*/Hirshfeld-I/MBIS/Becke，选项 -1 切换，默认 Becke 修正 CSD 半径）中做数值积分与分析。Becke 积分方案成本低精度高，积分点数由 settings.ini 的 radpot/sphpot 调节。涵盖实空间函数原子积分、交叠空间积分、多极矩与 $\langle r^2\rangle$、AOM/FOM、LI/DI（模糊键级）、PDI、FLU/FLU-π、CLRK、PLR、多中心 DI、信息论芳香性指数、原子有效体积/极化率/C6。AOM 误差（SUM 偏离单位阵）应 <0.001，否则关 iautointgrid 并加大 radpot/sphpot。

## 子功能：模糊原子空间积分（选项 1，配合 -1、-5、-10、-11）

说明：对实空间函数做原子加权积分 $I_A=\int w_A f\,d\mathbf r$（如电子布居）；-5 限原子，-10/-11 设参考点（拓扑临界点，源函数常用键临界点）。

菜单路径：主功能15 → -1（选 Hirshfeld/Becke/HI/MBIS 划分）→ 1（选实空间函数后积分）→ -5（限原子）→ -10/-11（设参考点）

输入要求：波函数文件（.fch/.wfn/.molden/.mwfn 等）。

操作步骤：进入主功能15，选项 -1 选 3（内置球平均原子密度的 Hirshfeld）等切换划分，选项 1 选择实空间函数即开始积分；输出含 % of sum 与 % of sum abs。

产出：各原子积分值（如电子布居）。

来源：[3.18.0 基本概念](../sec-3-18-fuzzy-atomic-space-analysis.md)、[3.18.1 原子空间积分](../sec-3-18-fuzzy-atomic-space-analysis.md)

## 子功能：交叠空间积分（选项 8）

说明：计算原子对交叠区积分 $I_{AB}=\int w_A w_B f\,d\mathbf r$（如原子对共有电子数），正负部分开输出，并给对角元/非对角元/全部元之和。

菜单路径：主功能15 → 8 → 选择实空间函数

输入要求：波函数文件（仅 Becke 划分）。

操作步骤：进入主功能15，直接选 8，按提示选实空间函数即可。

产出：$I_{AB}$ 矩阵（正部/负部分开）与三类求和。

来源：[3.18.2 交叠空间积分](../sec-3-18-fuzzy-atomic-space-analysis.md)

## 子功能：原子与分子多极矩及 <r²>（选项 2，配合 -5、-1）

说明：输出单极/偶极/四极/八极矩（Cartesian＋球谐）与原子电子空间范围 $\langle r_A^2\rangle$，末尾给分子总量；用 -5 限原子时末尾“分子”量即片段量，可算片段偶极矩；选 2 输出 multipole.txt＋atom_moment.txt，后者可被 VMD 脚本画箭头/椭球。

菜单路径：主功能15 → -1（划分选择，如 3 为内置 Hirshfeld）→ 2（多极矩）→ 1（屏幕输出）/2（写文件）→ -5（指定原子算片段）→ 2 → 1

输入要求：波函数文件。

操作步骤（原始格式，苯酚二聚体两单体片段偶极矩）：

```text
examples\phenoldimer.wfn  // Wavefunction file of optimized phenol dimer
15  // Fuzzy atomic space analysis
-1  // Select method for defining atomic space
3  // Hirshfeld based on built-in spherically averaged atomic densities
2  // Calculate atomic and molecular multipole moments
1  // Output result on screen
```

```text
-5  // Define the atoms to be calculated
1-13  // Atom indices of the first phenol
2  // Calculate atomic and molecular multipole moments
1  // Output result on screen
```

```text
-5  // Define the atoms to be calculated
14-26  // Atom indices of the second phenol
2  // Calculate atomic and molecular multipole moments
1  // Output result on screen
```

VMD 画偶极箭头（原始格式，先主功能100 → 2 导出 phenoldimer.xyz，再 VMD 中）：

```tcl
draw color green
drawarrow all 1.227306 -0.128087 0.650833 2
draw color red
drawarrow "serial 1 to 13" 0.570356 -0.356257 0.284025 2
draw color yellow
drawarrow "serial 14 to 26" 0.656950 0.228171 0.366808 2
```

原子偶极/四极可视化（原始格式）：主功能15 → 2 → 2（输出 multipole.txt＋atom_moment.txt）；VMD 中 source atomdip.tcl/atomquad.tcl 后运行 atomdip/atomquad；AIM 划分改用主功能 17 子功能 8。

产出：片段偶极/四极/八极矩与净电荷（片段净电荷非零时偶极矩略依赖原点）；VMD 箭头（负电中心指正电中心）与椭球（短轴对应电子伸展方向，如 Br σ-hole）。

来源：[3.18.3 多极矩](../sec-3-18-fuzzy-atomic-space-analysis.md)、[4.15.3 片段偶极矩](../sec-4-15-fuzzy-atomic-space-analysis.md)、[4.15.5 偶极/四极可视化](../sec-4-15-fuzzy-atomic-space-analysis.md)

## 子功能：AOM/FOM（选项 3、33）

说明：选项 3 算各原子空间轨道交叠矩阵，写 AOM.txt；选项 33 算一个或两片段的 FOM（片段内原子 AOM 之和），写 FOM.txt；SUM 偏离单位阵的 Error 为精度指标。

菜单路径：主功能15 → 3（AOM）→ 33（FOM，定义片段原子）

输入要求：波函数文件。

操作步骤：进入主功能15，选 3 即算全部 AOM（最高虚轨道不计；ispecial=3 则计全部轨道）；选 33 按提示定义一或两个片段。精度不足时：增大 radpot/sphpot、radcut=0、选项 -6 换分子积分格点、去弥散函数。

产出：AOM.txt、FOM.txt 与 Error 值。

来源：[3.18.4 AOM 与 FOM](../sec-3-18-fuzzy-atomic-space-analysis.md)

## 子功能：LI/DI 模糊键级（选项 4、44）

说明：先算 AOM 再得 LI/DI，DI 即模糊键级（闭壳层 DI≈1 为一对共享电子，极性键偏小）；开壳层分自旋输出；平面分子可分 σ/π（先经主功能6 → 26 把另一成分占据置零，或主功能100 → 22）。

菜单路径：主功能15 → 4（LI/DI）→ 44；DI-σ/DI-π 需先改占据数

输入要求：波函数文件（AOM 误差大时关 iautointgrid 并加大 radpot/sphpot）。

操作步骤（原始格式，苯 C–C/C–H 键级）：

```text
examples\benzene.wfn  // Generated under B3LYP/6-311G*
15  // Fuzzy atomic space analysis
4  // Calculate localization index (LI) and DI. Multiwfn first makes use of DFT numerical quadrature scheme to calculate atomic overlap matrix (AOM) in each fuzzy atomic space, and then convert AOM to DI and LI.
n  // Do not output LI and DI to plain text file
```

操作步骤（原始格式，DI-π 分解，苯对位 π 离域大于间位）：

```text
6  //Modify wavefunction
26  //Modify occupation number
0  // Select all orbitals
0  // Make occupation number of all orbitals to zero
17,20,21  // MO 17,20,21 correspond to π orbitals.
2  // Set their occupation numbers to 2 (closed-shell orbitals)
q  // Return to upper level of menu
-1  //Return to main menu
```

```text
15  // Fuzzy atomic space analysis
4  // Calculate LI and DI, now only π orbitals are occupied, the result is DI-π
```

产出：DI 矩阵（苯 C–C 1.467、C–H 0.877）；DI-π（C1–C6/C1–C5/C1–C4 为 0.438/0.055/0.093）；对角元为行非对角元之和（原子价）。

来源：[3.18.5 LI 与 DI](../sec-3-18-fuzzy-atomic-space-analysis.md)、[4.15.1 苯的离域指数](../sec-4-15-fuzzy-atomic-space-analysis.md)

## 子功能：PDI、FLU/FLU-π（选项 5、6、7）

说明：PDI 为六元环三对位 DI 均值（越大越芳香，仅闭壳层，平面可分 σ/π）；FLU 基于 DI 偏离参考（默认 C–C/C–N/B–N δref 为 1.468/1.566/1.260，选项 -4 可改），适用任意元环，越小越芳香；FLU-π 用 DI-π 与平均值，不依赖参考但仅严格适用于平面分子。

菜单路径：主功能15 → 5（PDI：按连接顺序输环原子）→ 6（FLU：输环原子）→ 7（FLU-π：先输 π 轨道号，再输环原子）

输入要求：波函数文件（Becke 默认划分；大体系 AOM 耗时；AOM 只算一次，后续 FLU 复用）。

操作步骤（原始格式，菲中间环 vs 边缘环 PDI）：

```text
examples\phenanthrene.wfn  // Optimized at B3LYP/6-31G* level
15  // Fuzzy atomic space analysis
5  // Calculate PDI
4,8,9,10,7,3  // Middle ring atoms in connection order, PDI = 0.047439
8,9,11,13,14,15  // Edge ring atoms, PDI = 0.0817
```

```text
q  // Back to upper level menu
6  // Calculate FLU
4,8,9,10,7,3  // FLU = 0.025289
8,9,11,13,14,15  // FLU = 0.007499
```

```text
q  // Back to upper level menu
7  // Calculate FLU-π
36,40,43,44,45,46,47  // π orbital indices
4,8,9,10,7,3  // FLU-π = 0.149238
8,9,11,13,14,15  // FLU-π = 0.034904
```

产出：PDI/FLU/FLU-π 值与每键贡献；边缘环三者一致显示更芳香。

来源：[3.18.6 PDI](../sec-3-18-fuzzy-atomic-space-analysis.md)、[3.18.7 FLU](../sec-3-18-fuzzy-atomic-space-analysis.md)、[4.15.2 菲的芳香性](../sec-4-15-fuzzy-atomic-space-analysis.md)

## 子功能：CLRK、PLR（选项 9、10）

说明：选项 9 输出原子间线性响应核矩阵（近似式，需虚轨道，仅 HF/DFT 闭壳层）；选项 10 以 CLRK 代 DI 算 PDI 型 PLR（仅闭壳层，平面可分 σ/π）。

菜单路径：主功能15 → 9（CLRK 矩阵）→ 10（PLR：按连接顺序输环原子）

输入要求：.mwfn/.fch/.molden/.gms（需虚轨道，.wfn 不行）。

操作步骤（原始格式，菲 PLR）：

```text
examples\phenanthrene.fch  // Obtained at the same level as phenanthrene.wfn
15  // Fuzzy space analysis
10  // Calculate PLR
4,8,9,10,7,3  // PLR = 0.248030
8,9,11,13,14,15  // PLR = 0.489560
```

产出：CLRK 矩阵；PLR（边缘环显著大于中间环）。

来源：[3.18.8 CLRK](../sec-3-18-fuzzy-atomic-space-analysis.md)、[3.18.9 PLR](../sec-3-18-fuzzy-atomic-space-analysis.md)、[4.15.2](../sec-4-15-fuzzy-atomic-space-analysis.md)

## 子功能：多中心 DI、信息论芳香性指数（选项 11、12）

说明：选项 11 算 n 中心 DI（归一化 δ¹/ⁿ 可跨元数比较；仅单行列式闭壳层，最多 10 中心，6 中心以上可能很耗时）；选项 12 算环原子信息论量（Shannon 熵/Fisher 信息/GBP 熵三选一）平均值。

菜单路径：主功能15 → 11（多中心 DI：输原子数与序号）→ 12（信息论指数：选 Shannon/Fisher/GBP → 输环原子）

输入要求：波函数文件（单行列式闭壳层）。

操作步骤：进入主功能15，选 11 按提示输入中心数与原子序号；选 12 先选三种定义之一，再输环原子序号，得平均值即芳香性指数（原文用 Hirshfeld 划分，模块默认 Becke）。

产出：多中心 DI 值；信息论芳香性指数。

来源：[3.18.10 多中心 DI](../sec-3-18-fuzzy-atomic-space-analysis.md)、[3.18.11 信息论指数](../sec-3-18-fuzzy-atomic-space-analysis.md)

## 子功能：原子有效体积/极化率/C6（选项 13，配合 -1、-5）

说明：TS 方法由 $V^{\mathrm{eff}}/V^{\mathrm{free}}$ 标度自由原子极化率得 $\alpha^{\mathrm{eff}}$ 与 $C_{6,AA}$，再得原子对与分子间 $C_6$；输出各原子 $V^{\mathrm{eff}}/V^{\mathrm{free}}$/比值、$\alpha^{\mathrm{eff}}$/占比/$C_{6,AA}$ 与同分子 $C_6$；划分敏感时看 Contribution 占比。

菜单路径：主功能15 → -1（选权重，如 5 为 MBIS，需先选项 1 建空间）→ 13 → 依次输入各元素孤立原子波函数路径（与分子同水平）→ -5 可限原子

输入要求：体系波函数＋各元素原子波函数文件（同水平；SiH4 用 B3LYP/6-311+G(2df,p)＋MBIS 最好）。

操作步骤（原始格式，环氧乙烷）：

```text
examples\oxirane.fchk
15  // Fuzzy analysis
13  // Calculate atomic effective volume, free volume, polarizability and C_6 coefficient
H.wfn  // Path of wavefunction file of hydrogen atom in isolated state
C.wfn  // Path of wavefunction file of carbon atom in isolated state
O.wfn  // Path of wavefunction file of oxygen atom in isolated state
```

操作步骤（原始格式，SiH4 的 C6）：

```text
examples\SiH4_C6\SiH4.fch
15  // Fuzzy analysis
-1  // Select the method for partitioning atomic spaces
5  // MBIS
1  // Start calculation. Then MBIS atomic spaces will be constructed
13  // Calculate atomic effective volume, free volume, polarizability and C_6 coefficient
examples\SiH4_C6\H.wfn  // Wavefunction file of H atom in isolated state
examples\SiH4_C6\Si.wfn  // Wavefunction file of Si atom in isolated state
```

产出：$V^{\mathrm{eff}}/V^{\mathrm{free}}$、TS 法原子极化率及占比、原子 $C_6$ 与同分子 $C_6$（如 SiH4 同分子 $C_6$ = 347.07 a.u.）。

来源：[3.18.12 体积极化率 C6](../sec-3-18-fuzzy-atomic-space-analysis.md)、[4.15.4 环氧乙烷与 SiH4](../sec-4-15-fuzzy-atomic-space-analysis.md)

## 实例条目

- 苯 C–C/C–H 模糊键级与 DI-σ/DI-π 分解：主功能15 → 4；分解先主功能6 → 26 置零后只留 π 轨道。来源：[4.15.1](../sec-4-15-fuzzy-atomic-space-analysis.md)
- 菲 PDI/FLU/FLU-π/PLR：主功能15 → 5/6/7/10；边缘环一致更芳香。来源：[4.15.2](../sec-4-15-fuzzy-atomic-space-analysis.md)
- 苯酚二聚体两单体片段偶极矩：主功能15 → -1 → 3 → 2 → 1 → -5 → 2 → 1；VMD drawarrow.tcl 画矢量对比。来源：[4.15.3](../sec-4-15-fuzzy-atomic-space-analysis.md)
- 环氧乙烷原子体积极化率 / SiH4 的 C6：主功能15 → 13（SiH4 先 -1 → 5 → 1 建 MBIS 空间）。来源：[4.15.4](../sec-4-15-fuzzy-atomic-space-analysis.md)
- H2O2 原子偶极箭头 / C6H5Br 原子四极椭球：主功能15 → 2 → 2（atom_moment.txt＋atomdip.tcl/atomquad.tcl）。来源：[4.15.5](../sec-4-15-fuzzy-atomic-space-analysis.md)
