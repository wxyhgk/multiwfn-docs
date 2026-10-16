# 主功能18：电子激发分析

功能概述：电子激发分析基于单参考方法（CIS/TDHF/TDDFT/TDA）的组态系数，全面表征激发态特征。标准输入是两种文件：含基函数与分子轨道信息的文件（参考态轨道波函数，如 .fch/.molden/.gms/.mwfn），加上含激发态组态系数的文件（Gaussian/ORCA/BDF/CP2K 输出或同格式纯文本；Gaussian 须加 IOp(9/40=4)，ORCA 用 TPrint 1E-8）。模块提供约 20 个子功能：空穴–电子分析、跃迁矩阵热图、密度差 CT 分析、Δr、态间偶极矩、NTO、ghost-hunter、IFCT、TDM 导出、跃迁偶极矩分解、跃迁电荷、激发态自然轨道、Λ 指数、主要 MO 跃迁打印、CTS、密度极化、ECD/CPL 不对称因子等。唯一不需组态系数文件的是子功能3（基于密度差格点）。

## 检查修改导出组态系数（子功能-1）

说明：检查、修改并导出激发的组态系数。改完系数后经 -3 导出文本，再用该文本做后续分析，结果对应修改后的系数；-2 按阈值打印关键轨道对。

菜单路径：主功能18（电子激发分析）→ 子功能-1（选项-1 恢复原始系数，-2 打印关键轨道对，-3 导出文本，1/2 修改系数）

输入要求：参考轨道文件（.fch/.molden/.gms/.mwfn）＋组态系数文件（Gaussian/ORCA/BDF/CP2K 输出或同格式文本）。

操作步骤（原始格式）：

- **1 Set coefficient of an orbital pair**：把某轨道对的已载入组态系数换为输入值。
- **2 Set coefficient for specific range of orbital pairs**：批量把已载入组态系数换为输入值，需输入轨道跃迁对应的占据 MO 和虚 MO 编号范围。
- **-1 Retrieve original coefficient of all orbital pairs**：把系数恢复为原来载入的值。
- **-2 Print coefficient (and contribution to excitation) of some orbital pairs**：打印绝对值大于特定值的组态系数及相应贡献，找出关键轨道对。
- **-3 Export current excitation information to a plain text file**：当前选中激发态的基本信息和组态系数导出到纯文本文件，之后可用作各种电子激发分析功能的第二种输入文件。

产出：屏幕上的关键轨道对系数表；导出的组态系数纯文本文件。

来源：[3.21.0](sec-3-21-electron-excitation-analysis.md#3210-检查修改和导出激发的组态系数--1)

## 空穴–电子/跃迁密度/偶极矩密度分析（子功能1）

说明：计算并可视化空穴分布、电子分布、空穴–电子重叠、跃迁密度、跃迁电/磁偶极矩密度、电荷密度差与 Cele/Chole 函数，输出 Sr/Sm 重叠、t/H/D/CT 等定量指标与 MO/原子/片段贡献及热图。空穴/电子全空间积分理想值为 1.0，跃迁密度理想值为 0，偏离太大则 t/H/D/Sm 等不可靠，原因有三：格点质量太差、格点空间范围太窄、忘了用 IOp(9/40=x) 导致只载入极少组态。默认不算跃迁磁偶极矩密度，进入前选选项-1 才算。

菜单路径：主功能18 → 子功能1（功能1 可视化分析，功能2 显示 MO 贡献，功能3 显示原子/片段贡献并绘热图）

输入要求：同上（两种文件）；每次只能分析一个态，换态须退出重进。

操作步骤（原始格式）：进入子功能1 后设置格点数据，对空穴分布、电子分布、空穴和电子的重叠、跃迁密度、跃迁电/磁偶极矩密度、电荷密度差和 $C_{\mathrm{ele}}$ / $C_{\mathrm{hole}}$ 函数计算格点数据。算完后各种量显示在屏幕上；后处理菜单中可把空穴、电子、跃迁密度、$S_{m}$ / $S_{r}$ 等可视化为等值面图或导出为 cube 文件，也可算空穴–电子间 Coulomb 吸引能（很贵）。

MO 对空穴–电子分布贡献的输出例子（输入打印阈值即显示）：

```text
 MO     126, Occ:   2.00000    Hole:  0.29664     Electron:  0.00000
 MO     127, Occ:   2.00000    Hole:  0.19783     Electron:  0.00000
 MO     128, Occ:   2.00000    Hole:  0.38666     Electron:  0.00000
 MO     130, Occ:   0.00000    Hole:  0.00000     Electron:  0.08058
 MO     131, Occ:   0.00000    Hole:  0.00000     Electron:  0.46282
 MO     132, Occ:   0.00000    Hole:  0.00000     Electron:  0.16703
 MO     133, Occ:   0.00000    Hole:  0.00000     Electron:  0.22976
 Sum of hole:  1.00000    Sum of electron:  1.00000
```

原子贡献输出例子（Mulliken 型划分，默认忽略氢，可切换）：

```text
Contribution of each non-hydrogen atom to hole and electron:
    1(C )  Hole:  1.37 %  Electron:  8.96 %  Overlap:  3.50 %  Diff.:   7.59 %
    2(C )  Hole: 11.86 %  Electron:  0.74 %  Overlap:  2.97 %  Diff.: -11.11 %
    3(C )  Hole:  8.96 %  Electron: 11.00 %  Overlap:  9.93 %  Diff.:   2.04 %
...[ignored]
   14(N )  Hole:  0.18 %  Electron: 23.80 %  Overlap:  2.07 %  Diff.:  23.62 %
   15(O )  Hole:  3.07 %  Electron: 17.23 %  Overlap:  7.28 %  Diff.:  14.16 %
   16(O )  Hole:  3.07 %  Electron: 17.23 %  Overlap:  7.28 %  Diff.:  14.16 %
```

"Overlap" 是 "Hole" 与 "Electron" 的几何平均，"Diff." 为 Electron 减 Hole。若需片段贡献，选 "-1 Load fragment definition" 再输入片段数与原子编号，或从纯文本文件载入（每片段一行），例如：

```text
1,3,6-10,12
2,4,5
11
13-15
```

产出：屏幕上的 Sr/Sm/t/H/D/CT 等定量指标、MO/原子/片段贡献表与热图；空穴/电子/跃迁密度等值面图与 cube 文件。

来源：[3.21.1](sec-3-21-electron-excitation-analysis.md#3211-分析并可视化空穴电子分布跃迁密度和跃迁电磁偶极矩密度-1)、[4.18.1](sec-4-18-electron-excitation-analysis.md#4181-用空穴-电子分析完整表征电子激发)

## 原子/片段跃迁矩阵热图（子功能2）

说明：把各种原子跃迁矩阵（ATM，如基于原子的跃迁密度矩阵、原子–原子电荷转移矩阵、原子跃迁偶极矩矩阵）转为片段跃迁矩阵（FTM）并绘制热图。矩阵来源：常规绘制输入 p 热图；基于 Gaussian 输出的 TDM；纯文本 TDM；AAtrdip 原子跃迁偶极矩矩阵（子功能11 产生）；原子–原子电荷转移矩阵（IFCT 功能输入 -1 导出 atmCTmat.txt）。

菜单路径：主功能18 → 子功能2（选项0 屏幕显示，1 存图，3 导出 matrix.txt，4 切换氢，5 改色标，6 改插值，8 切换归一化）

输入要求：参考轨道文件＋TDM/电荷转移等矩阵来源（tdmat.txt、AAtrdip*.txt、atmCTmat.txt 等，例子文件 examples\excit\tdmat.txt）。

操作步骤（原始格式）：

- 选项 0：在屏幕显示 ATM 的热图。默认横纵坐标标签对应非氢原子的编号。
- 选项 1：与选项 0 相同，但把热图保存为当前文件夹下的图形文件。
- 选项 3：把 ATM 导出为当前文件夹下的 *matrix.txt*，方便用 Origin/Sigmaplot 等绘制。
- 选项 4：切换热图中是否包括氢的状态。
- 选项 5：改变色标上下限（默认自动设为 ATM 最大/最小矩阵元）。
- 选项 6：改变格点数据之间的插值步数（默认 10；设 1 则不插值，每方格恰对应一矩阵元）。
- 选项 8：确定是否归一化（"Yes" 则 ATM 所有元之和为 1）。

产出：屏幕/文件热图；matrix.txt。

来源：[3.21.2](sec-3-21-electron-excitation-analysis.md#3212-把各种原子片段跃迁矩阵绘制为热图-2)、[4.18.2](sec-4-18-electron-excitation-analysis.md#4182-跃迁密度矩阵与跃迁偶极矩密度矩阵分析的说明)

## 基于密度差格点分析电荷转移（子功能3）

说明：直接对密度差 Δρ 格点积分得 CT 量（S+− 等），并可视化 C+/C−。这是唯一不需组态系数文件的子功能。

菜单路径：主功能18 → 子功能3

输入要求：密度差格点（主功能5 自定义操作产生，或载入外部 cube 等含密度差格点的文件）。

操作步骤（原始格式）：先用主功能 5 的自定义操作产生 Δρ 格点数据，或启动时载入含密度差格点数据的文件，之后进入主功能 18 的子功能 3，上述所有量立刻显示在屏幕上（"Overlap integral between C+ and C-" 即 $S_{+-}$）。后处理菜单中可视化 $C_{+}$ 和 $C_{-}$，或把两函数格点数据导出为 cube 文件。

产出：屏幕上的 CT 量与 S+−；C+/C− 等值面图与 cube 文件。

来源：[3.21.3](sec-3-21-electron-excitation-analysis.md#3213-基于密度差格点数据分析电荷转移-3)、[4.18.3](sec-4-18-electron-excitation-analysis.md#4183-基于电子密度差分析电子激发中的电荷转移)

## Δr 电荷转移长度指数（子功能4）

说明：输出 Δr，大值指示长程 CT 激发（纯/低 HF 成分泛函可能失效，应用长程校正泛函）。只选一个态时可进一步分解为轨道对贡献。

菜单路径：主功能18 → 子功能4

输入要求：参考轨道文件＋组态系数文件。

操作步骤（原始格式）：进入本功能后按提示选择要算 Δr 的激发态，结果立刻打印。若只选了一个态，Multiwfn 询问是否把 Δr 分解为轨道对贡献；若输入例如 0.01，则打印对 Δr 贡献大于 0.01 的轨道对。

产出：屏幕上的 Δr 值与轨道对分解表。

来源：[3.21.4](sec-3-21-electron-excitation-analysis.md#3214-计算-r-指数衡量电荷转移长度-4)、[4.18.4](sec-4-18-electron-excitation-analysis.md#4184-计算-r-和-λ-指标表征-n-苯基吡咯的各种电子激发)

## 态间跃迁电/磁偶极矩与态偶极矩（子功能5）

说明：计算所有态（基态＋激发态）之间的跃迁电/磁偶极矩，并打印每个态的电偶极矩。选项0选电/磁；选项1输出到屏幕；2 输出到 transdipmom.txt；3 产生 SOS 模块输入 SOS.txt；4 输出各激发态电偶极矩到 dipmom.txt（同时考虑电子＋核贡献）。Normalization 应接近期望值（闭壳 0.5、开壳 1.0），偏离大则须让量子化学程序输出更多组态（Gaussian 用 IOp(9/40=5)，ORCA 用 TPrint 1E-10）。大体系若只需基态–激发态之间，选 -1 切为 "Yes" 跳过激发态之间计算。

菜单路径：主功能18 → 子功能5（选项0 选电/磁，选项1/2 输出跃迁偶极矩，选项3 产生 SOS.txt，选项4 输出态偶极矩，选项-1 只算基态–激发态）

输入要求：参考轨道文件＋组态系数文件。

操作步骤（原始格式）：

- 选项 1：输出所有态（包括基态和激发态）之间的跃迁电偶极矩到屏幕
- 选项 2：与 1 相同，但输出到当前文件夹下的 *transdipmom.txt*。
- 选项 3：产生 Multiwfn 的 SOS 模块的输入文件作当前文件夹下的 *SOS.txt*。
- 选项 4：输出每个激发态的电偶极矩到当前文件夹下的 *dipmom.txt*。

计算分三阶段：阶段 1 算基函数间偶极矩积分；阶段 2 算 MO 间偶极矩积分；阶段 3 算激发态间偶极矩积分（一般最耗时）。settings.ini 中 "maxloadexc" 非零且激发态数超限时，只载入前 maxloadexc 个态。

产出：屏幕/文件中的态间跃迁偶极矩；transdipmom.txt；SOS.txt；dipmom.txt。

来源：[3.21.5](sec-3-21-electron-excitation-analysis.md#3215-计算所有态之间的跃迁电磁偶极矩和每个态的偶极矩-5)、[4.18.5](sec-4-18-electron-excitation-analysis.md#4185-计算-4-硝基苯胺各激发态的偶极矩和所有态之间的跃迁偶极矩)

## 自然跃迁轨道 NTO（子功能6）

说明：对 TDM 做 SVD（对角化 T_occ/T_vir），得空穴/电子 NTO 对，本征值×100 即对激发的百分比贡献。CIS/TDA 本征值必在 0–1；TDDFT 忽略退激发，本征值略大于 1 可视为 1，远大于 1 则 TDDFT 可能不可靠、建议改 TDA。NTO 保留轨道相位，但有时变换后仍无主导轨道对，此时必须用空穴–电子分析。

菜单路径：主功能18 → 子功能6

输入要求：参考轨道文件＋组态系数文件。

操作步骤（原始格式）：进入本功能后输入要研究的电子激发编号，Multiwfn 载入组态系数并产生 NTO，再输出 NTO 对本征值；接下来选择是否把 NTO 导出为 .fch/.molden/.mwfn 文件。若导出，可用 Multiwfn 载入新文件以可视化 NTO、分析轨道组成（注意此时轨道能量字段实际是 NTO 本征值）。对非限制参考态，alpha/beta 分别计算打印，只需关注本征值最大的 NTO 对。

产出：屏幕上的 NTO 对本征值；导出的 NTO .fch/.molden/.mwfn 文件。

来源：[3.21.6](sec-3-21-electron-excitation-analysis.md#3216-产生自然跃迁轨道-ntos-6)、[4.18.6](sec-4-18-electron-excitation-analysis.md#4186-产生并分析尿嘧啶的自然跃迁轨道-nto)

## ghost-hunter 指数（子功能7）

说明：输出 MAC 指数（$M_{\mathrm{AC}}$，即 TDDFT 的 CT 激发能理论下限 ω_low），判别虚假长程 CT（ghost）态：$E_{\mathrm{TDDFT}}<M_{\mathrm{AC}}$ 视为 ghost 的必要而非充分条件（判据常过于严格）。只适用于一维 CT。先照常做空穴–电子分析得格点，$M_{\mathrm{AC}}$ 及其两项自动打印。

菜单路径：主功能18 → 子功能7（先做空穴–电子分析得格点）

输入要求：参考轨道文件＋组态系数文件（先做空穴–电子分析得格点）。

操作步骤（原始格式）：照常做空穴–电子分析，一旦空穴和电子的格点数据算完，Multiwfn 自动打印 $M_{\mathrm{AC}}$ 指数及其两项。若想基于弛豫密度差的 $D_{\mathrm{CT}}$' 算：经空穴–电子模块得 $M_{\mathrm{AC}}$ 第一项，再经子功能 3 得 $D_{\mathrm{CT}}$' 并手动算第二项（−1/$D_{\mathrm{CT}}$'），加总得 $M_{\mathrm{AC}}$。

产出：屏幕上的 $M_{\mathrm{AC}}$ 指数及其两项。

来源：[3.21.7](sec-3-21-electron-excitation-analysis.md#3217-计算-ghost-hunter-指数-7)、[4.18.1](sec-4-18-electron-excitation-analysis.md#4181-用空穴-电子分析完整表征电子激发)

## IFCT 片段间电荷转移（子功能8）

说明：定义片段后输出片段对空穴/电子的贡献、片段间转移矩阵、净转移、布居变化、片段内重排，以及本征/表观 CT%/LE%。Mulliken 型划分快但绝不能用弥散函数；Hirshfeld 稳健且兼容弥散函数但更贵。输入 -1 则不做常规分析而导出原子–原子电荷转移矩阵 atmCTmat.txt（可拿到子功能2绘热图）。

菜单路径：主功能18 → 子功能8

输入要求：参考轨道文件＋组态系数文件。

操作步骤（原始格式）：进入该功能后选择计算片段对空穴和电子分布的方法，选择要研究的激发态，再输入总片段数，之后依次输入每个片段的原子编号。若想从纯文本文件载入片段定义，在设总片段数时输入 `0`，再输入文件路径，文件格式形如（每片段一行）：

```text
1,3,6-10,12
2,4,5
11
13-15
```

若在这步输入 `-1`，导出当前文件夹下 *atmCTmat.txt*（元定义 $Q_{A,B}$ = Θ$_{A,\mathrm{hole}}$Θ$_{B,\mathrm{ele}}$）。片段定义完成后输出例子：

```text
 Variation of population number of fragment  1:  -0.25313
 Variation of population number of fragment  2:  -0.23110
 Variation of population number of fragment  3:   0.48423

 Intrafragment electron redistribution of fragment  1:   0.00334
 Intrafragment electron redistribution of fragment  2:   0.31271
 Intrafragment electron redistribution of fragment  3:   0.02419

 Transferred electrons between fragments:
  1 ->  2:   0.11977       1 <-  2:   0.00874     Net  1 ->  2:   0.11103
  1 ->  3:   0.14299       1 <-  3:   0.00089     Net  1 ->  3:   0.14210
  2 ->  3:   0.36476       2 <-  3:   0.02263     Net  2 ->  3:   0.34213
```

两片段时打印本征和表观 CT(%)/LE(%)，多于两片段只打印本征值。

产出：屏幕上的片段贡献、转移矩阵、CT%/LE%；atmCTmat.txt（输入 -1 时）。

来源：[3.21.8](sec-3-21-electron-excitation-analysis.md#3218-用-ifct-方法计算电子激发中的片段间电荷转移-8)、[4.18.8](sec-4-18-electron-excitation-analysis.md#4188-用-ifct-方法和电荷转移矩阵热图研究电子激发中的片段间电荷转移)

## 导出跃迁密度矩阵 TDM（子功能9）

说明：构建基函数表象 TDM（基态–激发态，或两激发态之间），可选两种对称化方式（方式1 合理通用；Gaussian 惯例用方式2），输出 tdmat.txt，还可输出 TDM.fch（Total SCF Density 字段即 TDM，可供 cubegen 算 TrEsp 跃迁电荷）。

菜单路径：主功能18 → 子功能9

输入要求：参考轨道文件＋组态系数文件。

操作步骤（原始格式）：进入本功能后按提示选择基态–激发态 TDM 或两激发态间 TDM 及激发态编号，再选择对称化方式（方式 1：$(P+P^T)/2$；方式 2：$(P+P^T)/\sqrt{2}$，Gaussian 惯例）。产生的矩阵输出到 *tdmat.txt*，可选输出 *TDM.fch*。

产出：当前文件夹下的 *tdmat.txt*（可直接拿到子功能2绘热图）；*TDM.fch*（可选）。

来源：[3.21.9](sec-3-21-electron-excitation-analysis.md#3219-产生并导出跃迁密度矩阵-9)、[4.18.9](sec-4-18-electron-excitation-analysis.md#4189-产生跃迁密度矩阵并变换为轨道表象)

## 跃迁偶极矩的 MO 对分解（子功能10）

说明：把基态–激发态跃迁电/磁偶极矩分解为各 MO 对贡献，量化各轨道跃迁对振子强度的贡献，解释吸收强弱。可输出 transdip.txt，或按贡献排序输出前若干，或只输出大于阈值的 MO 对。

菜单路径：主功能18 → 子功能10

输入要求：参考轨道文件＋组态系数文件。

操作步骤（原始格式）：在该功能中选择跃迁偶极矩类型，再选择要分解的激发态；可选相应选项把每个 MO 对的贡献输出到 *transdip.txt*，或按贡献排序输出前几个/几十个，或只输出贡献大于给定阈值的 MO 对。

产出：屏幕上的 MO 对贡献排序表；*transdip.txt*（可选）。

来源：[3.21.10](sec-3-21-electron-excitation-analysis.md#32110-把跃迁电磁偶极矩分解为分子轨道对贡献-10)、[4.18.10](sec-4-18-electron-excitation-analysis.md#41810-获得分子轨道对对跃迁偶极矩的贡献)

## 跃迁偶极矩的基函数/原子分解（子功能11）

说明：Mulliken 型划分把跃迁电/磁偶极矩分解为基函数与原子贡献，结果写 trdipcontri.txt，定位关键原子区；可选输出原子跃迁偶极矩矩阵 AAtrdipX/Y/Z.txt 与总量 AAtrdip.txt（可拿到子功能2绘热图）。有弥散函数时分解不可靠，改看跃迁偶极矩密度。

菜单路径：主功能18 → 子功能11

输入要求：参考轨道文件＋组态系数文件。

操作步骤（原始格式）：进入本功能后按提示选择跃迁偶极矩类型与激发态（基态–激发态或两激发态间），结果导出到 *trdipcontri.txt*；再按提示选择是否输出原子跃迁偶极矩矩阵（选 y 则 X/Y/Z 分量分别到 *AAtrdipX.txt*、*AAtrdipY.txt*、*AAtrdipZ.txt*，总量到 *AAtrdip.txt*）。

产出：*trdipcontri.txt*；*AAtrdipX/Y/Z.txt* 与 *AAtrdip.txt*（可选）。

来源：[3.21.11](sec-3-21-electron-excitation-analysis.md#32111-把跃迁电磁偶极矩分解为基函数和原子贡献-11)、[4.18.11](sec-4-18-electron-excitation-analysis.md#41811-把分子片段贡献的跃迁偶极矩画成箭头)

## Mulliken 原子跃迁电荷（子功能12）

说明：输出原子跃迁电荷（总和必为零），用于激子耦合研究。TrEsp 跃迁电荷更好但对大体系贵得多，做法见专题教程。

菜单路径：主功能18 → 子功能12

输入要求：参考轨道文件＋组态系数文件。

操作步骤（原始格式）：

```text
examples\excit\N-phenylpyrrole.fch
18  // Electron excitation analysis
12  // Calculate Mulliken transition charges
N-phenylpyrrole.out
3  // Study the transition from ground state to the third excited state
```

然后在当前文件夹找到 *atmtrchg.chg*（最后一列即跃迁电荷）。

产出：当前文件夹下的 *atmtrchg.chg*。

来源：[3.21.12](sec-3-21-electron-excitation-analysis.md#32112-计算-mulliken-原子跃迁电荷-12)

## 特定激发态自然轨道（子功能13）

说明：为选定激发态构建（未弛豫）密度矩阵、对角化得自然轨道，导出为 NO_XXXX.mwfn 供波函数分析（如两激发态密度差、片段电荷差）。

菜单路径：主功能18 → 子功能13

输入要求：参考轨道文件＋组态系数文件。

操作步骤（原始格式）：载入含基函数信息的文件，进入该功能时再载入含组态系数的文件；按提示输入要产生 NO 的激发态编号。对每个选定态：产生激发态密度矩阵 $\mathbf{P}^{\mathrm{ES}} = \mathbf{P}^{\mathrm{GS}} + \Delta\mathbf{P}^{\mathrm{local}} + \Delta\mathbf{P}^{\mathrm{cross}}$，对角化得 NO（本征矢为 NO，本征值为占据数），导出为 .mwfn（如选态 2 则为 *NO_0002.mwfn*）。对开壳参考态，alpha/beta 分别计算导出。

产出：*NO_XXXX.mwfn* 文件。

来源：[3.21.13](sec-3-21-electron-excitation-analysis.md#32113-产生特定激发态的自然轨道-13)、[4.18.13](sec-4-18-electron-excitation-analysis.md#41813-研究单个激发态的电子结构和两激发态之间的差别)

## Λ 指数表征激发（子功能14）

说明：输出 Λ（0–1；小值指示长程 CT），只选一个态时可分解为轨道对贡献。Λ 计算（Becke 格点算 MO 模重叠）远贵于 Δr；无特殊原因更推荐 D 与 Sr 指数。

菜单路径：主功能18 → 子功能14

输入要求：参考轨道文件＋组态系数文件。

操作步骤（原始格式）：进入本功能后先计算所有占据–虚 MO 模重叠积分矩阵，再按提示选择激发态，结果立刻打印。若只选了一个态，Multiwfn 询问是否把 Λ 分解为轨道对贡献；若输入例如 0.01，则打印贡献大于 0.01 的轨道对。

产出：屏幕上的 Λ 值与轨道对分解表。

来源：[3.21.14](sec-3-21-electron-excitation-analysis.md#32114-计算-λ-指数表征电子激发-14)、[4.18.4](sec-4-18-electron-excitation-analysis.md#4184-计算-r-和-λ-指标表征-n-苯基吡咯的各种电子激发)

## 打印全部态主要 MO 跃迁

说明：一览各态主导轨道对（激发能、振子强度、自旋多重度与贡献百分比），快速定性。与多数功能不同，本功能不需要含基函数信息的文件，直接用量子化学输出文件即可。

菜单路径：主功能18 → 打印主要 MO 跃迁功能（子功能15）

输入要求：Gaussian/ORCA/GAMESS-US/Firefly 的 ZINDO/CIS/TDHF/TDA-DFT/TDDFT 输出文件（不需基函数文件）。

操作步骤（原始格式）：

```text
examples\excit\D-pi-A.out  // Output file of TDDFT task of Gaussian
18  // Electron excitation analysis
15  // The present function
```

立刻看到：

```text
#   1   3.9069 eV    317.35 nm   f=  0.01880   Spin multiplicity= 1:
   H-4 -> L 81.9%, H-4 -> L+2 12.1%
 #   2   4.0624 eV    305.20 nm   f=  0.63550   Spin multiplicity= 1:
   H -> L 86.0%, H-3 -> L 5.3%
 #   3   4.4166 eV    280.72 nm   f=  0.00010   Spin multiplicity= 1:
   H-6 -> L 85.3%, H-6 -> L+2 11.9%
 #   4   4.7912 eV    258.77 nm   f=  0.01350   Spin multiplicity= 1:
   H-2 -> L 54.5%, H -> L+1 27.6%, H-3 -> L+1 6.4%
 #   5   4.8872 eV    253.69 nm   f=  0.00790   Spin multiplicity= 1:
   H -> L+3 57.3%, H-2 -> L 17.0%, H-1 -> L+2 8.8%, H-1 -> L 8.0%
```

默认只打印贡献大于 5% 的 MO 跃迁（阈值为 settings.ini 中 "compthres" 的 10 倍）。

产出：屏幕上的各态主要 MO 跃迁表。

来源：[3.21.15](sec-3-21-electron-excitation-analysis.md#32115-打印所有激发态中的主要-mo-跃迁)

## 电荷转移光谱 CTS

说明：基于 IFCT 输出各态重排/转移量（IFCTdata.txt 全量、IFCTmajor.txt 主要项），产生 CT_multiple 子文件夹（含 total_spectrum.txt 与 ET_/Redis_ 前缀文件），再以 CT_multiple.txt 为输入进主功能11 选 UV-Vis 绘制总光谱＋转移/重排子光谱。

菜单路径：主功能18 → CTS 功能（子功能16）→ 主功能11 绘制

输入要求：参考轨道文件＋组态系数文件。

操作步骤（原始格式）：

- (1) 准备输入文件（与空穴–电子/IFCT 完全相同）。
- (2) 启动 Multiwfn 并载入含基函数信息的文件，进入本功能，输入片段数与每个片段原子编号，再输入组态系数文件路径，最后选计算片段贡献的方法（大体系无弥散函数用 Mulliken，有弥散函数必须用 Hirshfeld）。算完后当前文件夹有 *IFCTdata.txt*（全量）、*IFCTmajor.txt*（贡献>5% 的主要项）与 "CT_multiple" 子文件夹（*CT_multiple.txt* 为光谱模块输入，*total_spectrum.txt* 绘 UV-Vis，`ET_` 前缀绘片段间转移光谱，`Redis_` 前缀绘片段内重排光谱；移动子文件夹须手动改路径）。
- (3) 启动 Multiwfn，把 *CT_multiple.txt* 作输入文件，进主功能 11 选 "UV-Vis"，选选项 0 绘制光谱（转移/重排子光谱连同 UV-Vis 一起显示；美化选项见光谱绘制模块）。

产出：IFCTdata.txt、IFCTmajor.txt、CT_multiple/ 子文件夹；UV-Vis 总光谱＋CTS 子光谱图。

来源：[3.21.16](sec-3-21-electron-excitation-analysis.md#32116-电荷转移光谱-cts-分析)、[4.18.16](sec-4-18-electron-excitation-analysis.md#41816-绘制电荷转移光谱并计算所有激发态的主要特征以-n-苯基吡咯为例)

## 电子密度极化分析

说明：用点电荷外势 δv 基于激发态微扰计算密度极化 ρpol、展开系数 {ck} 与二阶能量 E(2)、被极化电子量 δN。δv 不宜太强（如 ≤0.1 e 点电荷）；激发态越多越保险（50 个是好起点）；格点小体系用 0.1–0.15 Bohr，大体系 0.2–0.25 Bohr（建议做收敛测试）。只支持 CIS/TDDFT 等单激发方法，推荐 ωB97XD/CAM-B3LYP 联合 def-TZVP。

菜单路径：主功能18 → 密度极化功能（子功能17）

输入要求：参考轨道文件＋组态系数文件＋点电荷外势定义。

操作步骤（原始格式）：

- (1) Multiwfn 启动时载入含基函数信息的文件，例如 Gaussian TDDFT 产生的 .fchk 文件
- (2) 进入主功能 18 的子功能 17
- (3) 输入点电荷总数，再输入每个的 X、Y、Z 坐标和电荷值
- (4) 设置格点
- (5) 载入含激发态组态系数的文件，如 Gaussian TDDFT 输出文件

算完后屏幕显示每个激发态的激发能、$c_k$ 和 $E^{(2)}$，再给出总 $E^{(2)}$ 和 δN，以及 ρpol 全空间积分（越接近 0 格点越好）。后处理菜单中 ρpol、δv 与关键激发态跃迁密度可直接绘等值面图或导出 .cub。

产出：屏幕上的各态 ck/E(2)、总 E(2) 与 δN；ρpol/δv/跃迁密度等值面图与 cube 文件。

来源：[3.21.17](sec-3-21-electron-excitation-analysis.md#32117-基于电子激发的电子密度极化分析)、[4.18.17](sec-4-18-electron-excitation-analysis.md#41817-基于电子激发做电子密度极化分析的例子)

## ECD/CPL 不对称因子 g（子功能18）

说明：基于 Gaussian/ORCA 输出的跃迁电/磁偶极矩，输出 |μ|、|m|、夹角 θ、cosθ、旋光强度 R 与 g 因子；ECD 在基态极小结构算并选 "1 This study is for ECD"，CPL 在发射态极小结构算并选 CPL（自动反转磁偶极矩）。后处理选项1产生 VMD 脚本，用 emtran 命令画 μ（红）/m（青）箭头。

菜单路径：主功能18 → 子功能18

输入要求：Gaussian/ORCA 激发输出（含跃迁电/磁偶极矩）；CPL 用发射态优化输出亦可（自动取最后数据）。

操作步骤（原始格式）：进入主功能 18 的子功能 18，Multiwfn 从输出文件载入跃迁电/磁偶极矩，计算打印所有激发态的 $|{\boldsymbol{\mu}}^{\mathrm{tran}}|$、$|{\mathbf{m}}^{\mathrm{tran}}|$、θ、cos(θ)、R、g。再按研究选：

- 对 ECD：选 "1 This study is for ECD"。
- 对 CPL：选 "1 This study is for CPL"（反转载入的跃迁磁偶极矩；只有实际发射态的数据有意义）。

后处理菜单选选项 1 产生 VMD 绘图脚本，在 VMD 中执行后自定义命令 *emtran* 可用；运行如 *emtran 3* 把第 3 激发态的 μtran 与 mtran 分别作红色/青色箭头画出（箭头长度/半径/中心位移参数见脚本顶部注释）。

产出：屏幕上的 |μ|/|m|/θ/R/g 表；VMD 绘图脚本与偶极矢量箭头图。

来源：[3.21.18](sec-3-21-electron-excitation-analysis.md#32118-计算手性体系的-ecdcpl-不对称因子-g)、[4.18.18](sec-4-18-electron-excitation-analysis.md#41818-计算-p-6螺烯-ecdcpl-不对称因子-g-的例子)
