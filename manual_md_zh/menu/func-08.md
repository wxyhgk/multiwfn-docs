# 主功能8：轨道成分分析

功能概述：主功能 8 用于定量给出每条轨道中各基函数、壳层、原子或用户定义片段的百分比组成，是指认轨道定域位置、成键/反键贡献和电荷转移方向的核心工具。支持 Mulliken（选项 1）、Stout-Politzer（选项 2）、SCPA（选项 3）、NAO（选项 7）、Hirshfeld（选项 8）/Hirshfeld-I（选项 10）、Becke（选项 9）以及 LOBA/mLOBA 氧化态评估（选项 100）。基于基组展开的方法（1/2/3）禁止使用带弥散函数的基组；带弥散函数时应使用 NAO 或 Hirshfeld/Becke 方法。每次打印原子成分时还会给出轨道离域指数 ODI，ODI 越小轨道越离域。

## 子功能 1/2/3：特定轨道的基函数/壳层/原子成分（Mulliken、Stout-Politzer、SCPA）

说明：Mulliken、SCPA 和 Stout-Politzer 方法把轨道分解为基函数、壳层和原子成分。$\Theta_{i,a}\times 100\%$ 即基函数 $a$ 在轨道 $i$ 中的成分；同一壳层内基函数成分求和得到壳层成分；归属同一原子的壳层成分求和得到原子成分。球谐基函数标号与 Gaussian 完全相同（如 `D+1=XZ`、`D-2=XY` 等）。

菜单路径：主功能 `8` → `1`（Mulliken）/ `2`（Stout-Politzer）/ `3`（SCPA）→ 输入轨道序号。

输入要求：含基函数信息的 `.mwfn`/`.fch`/`.molden`/`.gms` 文件；若输入文件带 NBO 则被分析的是 NBO。禁弥散函数。

操作步骤：

```text
examples\CH3CONH2.fch  // You have to use .mwfn/.fch/.molden/.gms file as input for this type of analysis
8  // Orbital composition analysis
1  // Use Mulliken partition
6  // The orbital index is 6 (Note that as shown in the prompt on the screen, you can also input orbital label here, for example h-3 corresponds to HOMO-3, l+1 corresponds to LUMO+1, etc.)
```

也可输入 `-1` 打印全部轨道的基本信息以定位感兴趣的轨道。默认只打印成分大于 0.5% 的项，该阈值由 `settings.ini` 中的 `compthres` 调整。

产出：逐基函数 `Local`/`Cross term`/`Total` 组成、壳层组成、`s/p/d/f/g/h` 分类组成、原子组成百分比，以及末尾的 `Orbital delocalization index`（如乙酰胺 MO6：N7 占 65.5%，C5 约 11.8%，O6 约 11.6%，ODI=46.15）。

来源：[3.10.1](sec-3-10-orbital-composition-analysis.md#3101-用-mullikenstout-politzer-和-scpa-方法输出特定轨道中的基函数壳层和原子成分-1-2-3) · 实例 [4.8.1](sec-4-8-molecular-orbital-composition-analysis.md#481-用mulliken方法分析乙酰胺) · 方法比较 *Acta Chim. Sinica*, **69**, 2393 (2011) (<http://sioc-journal.cn/Jwk_hxxb/CN/abstract/abstract340458.shtml>)

## 子功能 -1/-2、4/5/6：定义片段并输出片段成分与片段间交叉项

说明：用 Mulliken、Stout-Politzer、SCPA 做片段成分分析前必须先定义片段。片段内容可选基函数、壳层、原子或其混合，最终记录的只是相应基函数序号。若只关心一个片段的成分，只需定义片段 1；若还关心两片段间交叉项，必须同时定义片段 1 和片段 2。Mulliken（子功能 4）与 Stout-Politzer（子功能 5）还会输出 `c^2` 项、内交叉项、外交叉项：片段总成分 = c² 项 + 内交叉项 + 外交叉项；片段 1–2 交叉项为 $\sum_{a\in\mathrm{frag1}}\sum_{b\in\mathrm{frag2}} 2C_{a,i}C_{b,i}S_{a,b}\times 100\%$，其与占据数乘积即该轨道贡献的片段间 Mayer 键级。

菜单路径：主功能 `8` → `-1` 定义片段 1 → `-2` 定义片段 2 → `4`（Mulliken 片段组成）/ `5`（Stout-Politzer）/ `6`（SCPA）。

输入要求：同上（含基函数信息的波函数文件）。

操作步骤：

```text
examples\CH3CONH2.fch
8  // Orbital composition analysis
-1  // Define fragment 1
a 1-4  // Add all basis functions in atom 1, 2, 3, 4 (methyl group) into fragment1
q  // Save fragment and return to upper menu
-2  // Define fragment 2
a 5-9  // Add all basis functions in atom 5, 6, 7, 8, 9 (formamide moiety) into fragment 2
q
4  // Print composition of fragment 1 and the cross term between fragment 1 and 2 in all orbitals by Mulliken analysis. If you only defined fragment 1, then only composition of fragment 1 will be printed
```

片段定义界面的典型流程：`all` 列出全部基函数信息，按原子/壳层找到目标（如原子 3 的 P 壳层序号 3、6、7），输入 `s 3,6,7` 加入片段，用 `all` 检查（已纳入的行最左侧出现星号），`clean` 清空旧片段，`q` 保存返回。每次进入片段定义界面时片段状态与上次离开时相同，重定义前先 `clean`。

产出：所有轨道的片段成分表；定义了片段 1+2 时还有 `Frag.1 part`/`Frag.2 part`/`Total` 交叉项表（例：MO7 交叉项 15.9% 为强成键贡献，MO14/16 为负大值即反键）。

来源：[3.10.2](sec-3-10-orbital-composition-analysis.md#3102-定义片段-1-和-2--1--2) · [3.10.3](sec-3-10-orbital-composition-analysis.md#3103-用-mullikenstout-politzer-和-scpa-方法输出片段-1-的成分和片段间成分-4-5-6)

## 子功能 7：NAO 轨道成分分析

说明：基于自然原子轨道（NAO）计算轨道成分。NBO 分析第一步把原始基函数转为 NAO（芯型/价型/Rydberg 型；芯+价统称最小集，与真实原子轨道一一对应）。NAO 是正交归一集，某 NAO 对特定 MO 的贡献即其展开系数平方乘以 100%。基组稳定性好，特别适合占据轨道；虚轨道常含大 Rydberg 成分，不宜用此法（Rydberg 占比大时，如 >10%，重归一化也失去意义）。

菜单路径：主功能 `8` → `7` → `0` 看单轨道成分 / `1` 看片段对一批轨道的贡献 / `2` 选输出模式 / `3` 切换自旋 / `-1` 定义片段。

输入要求：含 NAO 基 MO 系数矩阵的 NBO 输出文件（默认 NBO 不输出此矩阵，需在 `$NBO ... $END` 间加 `NAOMO` 关键词；Gaussian 内嵌 NBO 模块 L607 亦可）。任务须为单点任务。Gaussian 输入示例：

```text
# HF/6-31g* pop=nboread

Title Card Required

0 1
 O                  0.00000000    0.00000000    0.11472000
 H                  0.00000000    0.75403100   -0.45888100
 H                  0.00000000   -0.75403100   -0.45888100

$NBO NAOMO $END
[blank line]
[blank line]
```

操作步骤：

```text
examples/H2O_NAOMO.out  // Note that DO NOT use .fch as input file in current case
8  // Enter orbital composition analysis module
7  // Enter NAO analysis function
0  // Show orbital composition of specific MO
4  // Analyze MO 4
```

输出模式（选项 2）：`(0)` 显示所有项、`(1)` 显示非 Rydberg 项、`(2)` 显示贡献大于特定标准的项、`(3)` 显示贡献大于特定标准的非 Rydberg 项（默认）。片段贡献：先 `-1` 定义片段（`all` 列 NAO 详情，`a 2,3` 把原子 2、3 的 NAO 加入，`q` 保存），再 `1` 并输入轨道范围（如 `1-8`），得到 Core/Valence/Rydberg/Total 四列百分比。

产出：NAO 组成表、凝聚到壳层/原子的组成、芯/价/Rydberg 组成汇总、ODI（例：水 MO4：O 2pz 占 84.09%，O 共 92.9%，两 H 各 3.5%）。

来源：[3.10.4](sec-3-10-orbital-composition-analysis.md#3104-用自然原子轨道方法做轨道成分分析-7) · 实例 [4.8.2](sec-4-8-molecular-orbital-composition-analysis.md#482-用自然原子轨道方法分析水)

## 子功能 8/10：Hirshfeld / Hirshfeld-I 轨道成分

说明：用 Hirshfeld（或 Hirshfeld-I）权重函数做实空间积分划分：原子 $A$ 在轨道 $i$ 中的成分为 $\int\varphi_i^2(\mathbf{r})w_A(\mathbf{r})\mathrm{d}\mathbf{r}\times 100\%$，片段成分为其原子之和。基组稳定性好，兼容弥散函数；只能给出原子/片段组成，给不出原子轨道组成。Hirshfeld 已足够好，Hirshfeld-I 开销大而改进有限，一般不用。

菜单路径：主功能 `8` → `8`（Hirshfeld）/ `10`（Hirshfeld-I）→ 选原子密度来源 → 输入轨道序号。

输入要求：原子坐标 + GTF（如 `.fch`/`.wfn`/`.wfx`）。

操作步骤：

```text
examples\CH3CONH2.fch  // You can also use such as .wfn and .wfx file as input. But .wfn and .wfx files do not contain virtual orbital information!
8  // Orbital composition analysis
8  // Use Hirshfeld partition
```

选 `1` 使用内建原子密度（推荐；用原子 `.wfn` 文件的方式见 3.7.3 节）。数据初始化后输入轨道序号（如 `6`）。常用附加选项：`-2` 看某原子在一段轨道中的成分与布居（先输原子序号再输轨道范围，如 `7` + `14-19`）；`-9` 定义片段后再输轨道序号即附带片段贡献；`-3` 算所定义片段对一段轨道的贡献；`-4` 计算每个原子在每个轨道中的成分并全部导出到 `orbcomp.txt`。

```text
-2  // Print atom contribution to a range of orbitals
7  // Atom index
14-19  // Orbital range
```

```text
-9  // Define fragment
7-9  // The atoms in the amino group
h  // This stands for HOMO. You can also directly input its index (16)
```

产出：数值积分后自动归一化的各原子百分比（例：乙酰胺 MO6：C5 14.92%、O6 12.09%、N7 56.34%，与 Mulliken 结果相近）；`-2` 模式输出每轨道 `Composition`/`Population` 及总布居（占据轨道范围加和即 Hirshfeld 原子布居，可得原子电荷）。

来源：[3.10.5](sec-3-10-orbital-composition-analysis.md#3105-用-hirshfeld-或-hirshfeld-i-方法计算原子和片段贡献-810) · 实例 [4.8.3](sec-4-8-molecular-orbital-composition-analysis.md#483-用hirshfeld和becke方法分析乙酰胺)

## 子功能 9：Becke 轨道成分

说明：与 Hirshfeld 版用法完全相同，唯一区别是用 Becke 划分代替 Hirshfeld 划分，多数情况下两者结果定性一致。突出优点是不需要原子波函数文件（Becke 原子空间基于原子半径构建）。同样只能给出原子/片段组成。

菜单路径：主功能 `8` → `9` → 输入轨道序号。

输入要求：原子坐标 + GTF。

操作步骤：

```text
examples\CH3CONH2.fch
8  // Orbital composition analysis
9  // Use Becke partition
6  // The 6th orbital
```

产出：归一化原子百分比（例：乙酰胺 MO6：C5 14.90%、O6 12.07%、N7 60.74%，与 Hirshfeld 版非常接近）。

来源：[3.10.6](sec-3-10-orbital-composition-analysis.md#3106-用-becke-方法计算原子和片段贡献-9) · 划分细节 [3.18.0](sec-3-18-fuzzy-atomic-space-analysis.md#3180-基本概念)

## 子功能 100：LOBA / mLOBA 氧化态评估

说明：定域轨道键分析（LOBA，*Phys. Chem. Chem. Phys.*, **11**, 11297 (2009)）基于定域轨道（LMO）：若核电荷为 $Z$ 的原子在 $N$ 个占据 LMO 中的成分大于给定阈值（如 50%，双占据计两次），则氧化态为 $Z-N$；片段氧化态类推。mLOBA 把每个 LMO 的电子指派给贡献最大的原子，消除阈值任意性并保证氧化态之和严格等于体系净电荷（强烈推荐用 mLOBA）。注意对称体系中 mLOBA 可能给出不平衡结果（如乙烷 C–C 键 LMO 的两个电子被指派给任一碳），此时应把等价原子定义为一个片段求片段氧化态再平均。Multiwfn 对 LOBA/mLOBA 采用 Hirshfeld 成分法，比原文 Mulliken 法稳健得多。

菜单路径：先做轨道定域化得到 LMO → 主功能 `8` → `100` → 输入阈值（如 `50`）得 LOBA，或输入 `m` 得 mLOBA；`-1` 可定义片段并输出片段氧化态。

输入要求：记录 LMO（或 NBO）的 `.mwfn`/`.fch`/`.molden` 文件；或 Gaussian `pop=saveNBO`/`pop=saveNLMO` 任务所得 `.fch`（基于 NBO/NLMO 做分析）。

操作步骤（以 Fe(CN)₆³⁻ 为例，先定域占据轨道）：

```text
Fe(CN)6_3-.fch
19  // Orbital localization
1  // Only localize occupied orbitals, this is enough for LOBA/mLOBA analysis
```

```text
8  // Orbital composition analysis
100  // LOBA/mLOBA analysis
50  // Percentage threshold for performing LOBA
```

片段氧化态示例（二茂铁 C₅H₅ 片段）：

```text
-1  // Define fragment
1-5,7-11  // Index of the atoms constituting the C_5H_5 fragment
50  // Percentage threshold for performing LOBA
```

产出：各原子氧化态、氧化态之和（应等于体系净电荷）、片段氧化态（例：Fe(CN)₆³⁻ 中 Fe 为 +3，C 为 +2，N 为 −3；二茂铁 Fe 为 +2，C₅H₅ 片段为 −1）。

来源：[3.10.100](sec-3-10-orbital-composition-analysis.md#310100-用-loba-和-mloba-方法评估氧化态-100) · 实例 [4.8.4](sec-4-8-molecular-orbital-composition-analysis.md#484-用lobamloba方法计算氧化态)

## 附：轨道离域指数 ODI

说明：打印原子成分时附带的 ODI 定义为 $\mathrm{ODI}_{i}=0.01\times\sum_{A}(\Theta_{A,i})^{2}$，ODI 越低轨道越离域。任意实空间函数的离域另用主功能 300 系的 SDI 研究。

菜单路径：主功能 `8` → `1`/`8`（任选组成方法）→ 分析指定轨道（如 `D-pi-A.fchk` 的 MO52）。

输入要求：`.fch`/`.fchk` 等。

操作步骤：

```text
examples\excit\D-pi-A.fchk
8  // Orbital composition analysis
1  // Mulliken method
52  // Analyze MO 52
```

```text
0  // Return
8  // Hirshfeld method
1  // Use built-in atomic density
52  // Analyze MO52
```

产出：`Orbital delocalization index` 数值（例：MO52 的 Mulliken ODI=44.28，Hirshfeld ODI=38.93），结合等值面比较各轨道离域程度。

来源：实例 [4.8.5](sec-4-8-molecular-orbital-composition-analysis.md#485-通过轨道离域指数odi定量轨道的空间离域程度)
