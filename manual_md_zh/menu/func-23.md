# 主功能23：ETS-NOCV 分析

功能概述：主功能 23 实现扩展过渡态–化学价自然轨道（ETS-NOCV）分析：对密度差矩阵 $\Delta\mathbf{P}^{\mathrm{orb}} = \mathbf{P}[\Psi_{AB}]-\mathbf{P}[\Psi_{AB}^0]$ 对角化得 NOCV 轨道/能量/对密度，把轨道相互作用能分解到各 NOCV 对。支持任意片段数；仅 HF/KS-DFT、限制性闭壳层或非限制性开壳层（禁 ROHF、多组态、双杂化）。NOCV 能量用实际 Fock/KS 矩阵近似（非严格过渡态矩阵），弱相互作用下接近严格值。输入文件禁 .wfn/.wfx（无基函数信息）。

## 通用流程：载入片段并求 NOCV

说明：片段几何须与复合物一致（从复合物优化几何抽取坐标做单点，Gaussian 加 nosymm 防重取向；水平与复合物完全相同；勿用弥散函数、勿用隐式溶剂；3-zeta 如 def2-TZVP 足够）；片段原子在复合物中须连续、顺序与载入顺序一致；开壳层时按提示翻转自旋使 α/β 电子数之和与复合物一致。

菜单路径：主功能 23 → 输入片段数 → 依次载入各片段波函数文件。

输入要求：复合物波函数文件 + 各片段波函数文件（.fch/.mwfn/.molden 等含基函数文件；Fock 矩阵文件另按附录 7 提供，或由选项 −2 生成）。

操作步骤（闭壳层 CO–BH₃，两片段）：

```text
examples\ETS-NOCV\COBH3\COBH3.fch  // Complex wavefunction file
23  // ETS-NOCV analysis
2  // Two fragments
examples\ETS-NOCV\COBH3\CO.fch  // Wavefunction file of fragment 1. Note that loading order of the fragment wavefunction files must be in line with occurrence order of fragments in the complex
examples\ETS-NOCV\COBH3\BH3.fch  // Wavefunction file of fragment 2
```

即得 NOCV 轨道波函数、本征值与自动配对：

```text
       --------------- Pair and NOCV orbital information --------------
There are totally   26 NOCV pairs and    51 NOCV orbitals
NOCV orbitals whose eigenvalues are smaller than 1.0E-03 are not shown
Note: Energies of NOCV orbitals have not been evaluated, so they are all zero

 Pair  Energy | Orbital  Eigenvalue    Energy  | Orbital  Eigenvalue    Energy
    1    0.00       1      0.56514       0.00       51     -0.56514       0.00
    2    0.00       2      0.40205       0.00       50     -0.40205       0.00
    3    0.00       3      0.40204       0.00       49     -0.40204       0.00
    4    0.00       4      0.13007       0.00       48     -0.13007       0.00
    5    0.00       5      0.03704       0.00       47     -0.03704       0.00
    6    0.00       6      0.03703       0.00       46     -0.03703       0.00
    7    0.00       7      0.03419       0.00       45     -0.03419       0.00
    8    0.00       8      0.00834       0.00       44     -0.00834       0.00
    9    0.00       9      0.00273       0.00       43     -0.00273       0.00
Sum of NOCV eigenvalues:   0.00000
```

操作步骤（开壳层乙烷 2×CH₃，注意自旋翻转）：

```text
examples\ETS-NOCV\ethane\ethane.fch  // Wavefunction file of the whole system
23  // ETS-NOCV analysis
2  // Two fragments
examples\ETS-NOCV\ethane\CH3_1.fch  // Wavefunction file of the first ⋅CH_3 radical
examples\ETS-NOCV\ethane\CH3_2.fch  // Wavefunction file of the second ⋅CH_3 radical
n  // Do not flip spin of the first ⋅CH_3 radical
y  // Flip spin of the second ⋅CH_3 radical
```

操作步骤（乙烯 2×CH₂，三重态自旋相反 + 直接求能量）：

```text
examples\ETS-NOCV\ethene\ethene.fch  // Wavefunction file of the ethene
23  // ETS-NOCV analysis
2  // Two fragments
examples\ETS-NOCV\ethene\CH2_1.fch  // Wavefunction file of the first CH_2 fragment
examples\ETS-NOCV\ethene\CH2_2.fch  // Wavefunction file of the second CH_2 fragment
n  // Do not flip spin of the first CH_2 fragment
y  // Flip spin of the second CH_2 fragment
-2  // Generate Fock/KS matrix and evaluate NOCV orbital energies
```

操作步骤（三片段，乙炔三聚过渡态）：

```text
examples\ETS-NOCV\C2H2_trimerization_TS\TS.fch
23  // ETS-NOCV analysis
3  // Three fragments
examples\ETS-NOCV\C2H2_trimerization_TS\1.fch  // Fragment 1
examples\ETS-NOCV\C2H2_trimerization_TS\2.fch  // Fragment 2
examples\ETS-NOCV\C2H2_trimerization_TS\3.fch  // Fragment 3
-2  // Generate Fock/KS matrix and evaluate NOCV orbital energies
```

操作步骤（过渡金属 (CO)₅Cr=CH₂，CH₂ 取单重态参考态）：

```text
examples\ETS-NOCV(CO)5CrCH2(CO)5CrCH2.fch
23  // ETS-NOCV analysis
2  // Two fragments
examples\ETS-NOCV(CO)5CrCH2(CO)5Cr.fch  // Fragment 1
examples\ETS-NOCV(CO)5CrCH2\CH2.fch  // Fragment 2
-2  // Generate Fock/KS matrix and evaluate NOCV orbital energies
```

操作步骤（弱相互作用 A–T 碱基对，ORCA .molden）：

```text
AT.molden  // Wavefunction file of A-T base pair
23  // ETS-NOCV analysis
2  // Two fragments
A.molden  // Wavefunction file of adenine (A) fragment
T.molden  // Wavefunction file of thymine (T) fragment
-2  // Generate Fock/KS matrix and re-evaluate NOCV orbital energies
```

产出：NOCV 轨道、本征值、自动配对信息（本征值和为零）。

来源链接：[3.26.2](sec-3-26-ets-nocv-analysis.md)、[3.26.3](sec-3-26-ets-nocv-analysis.md)、[4.23.1](sec-4-23-examples-of-ets-nocv-analysis.md)。

## 后处理：NOCV 能量（选项 −1 / −2）

说明：−1 载入量子化学程序输出的复合物实际 Fock/KS 矩阵（细节见附录 7）；−2 由复合物波函数轨道能量与系数经 F=SC EC⁻¹ 生成。之后显示带能量的 NOCV 信息，各对能量之和≈ΔE_orb（近似值）。

菜单路径：后处理菜单 → −1 / −2。

输入要求：Fock/KS 矩阵文件（−1），或直接用复合物波函数（−2，无弥散函数时才可直接生成）。

操作步骤：后处理菜单选 `-2 Generate Fock/KS matrix and evaluate NOCV orbital energies`，CO–BH₃ 得：

```text
Pair  Energy | Orbital  Eigenvalue    Energy  | Orbital  Eigenvalue    Energy
    1  -77.88       1      0.56514    -120.88       51     -0.56514      16.93
    2  -15.83       2      0.40205    -139.60       50     -0.40205    -100.22
    3  -15.84       3      0.40204    -139.62       49     -0.40204    -100.23
    4   -5.53       4      0.13007     -44.60       48     -0.13007      -2.06
    5   -0.41       5      0.03704     -18.25       47     -0.03704      -7.19
    6   -0.41       6      0.03703     -18.19       46     -0.03703      -7.13
    7   -0.65       7      0.03419      21.33       45     -0.03419      40.48
    8   -0.06       8      0.00834    -308.53       44     -0.00834    -301.42
    9   -0.02       9      0.00273   -1661.86       43     -0.00273   -1655.69
Sum of NOCV eigenvalues:   0.00000
Sum of pair energies:    -116.63 kcal/mol
```

对 1 能量 −77.88 kcal/mol = −120.88×0.5651 + 16.93×(−0.5651)；乙烷开壳层 α/β 各 −98.93、总 −197.86 kcal/mol；乙烯 α/β 各 −169.05、总 −338.09 kcal/mol。

产出：各 NOCV 轨道/对能量与总和。

来源链接：[3.26.3](sec-3-26-ets-nocv-analysis.md)、[4.23.1](sec-4-23-examples-of-ets-nocv-analysis.md)。

## 后处理：NOCV 轨道与对密度等值面（选项 1 / 2）

说明：选项 1 看 NOCV 轨道等值面（GUI 右下列表选轨道或输序号，功能同主功能 0）；选项 2 看 NOCV 对密度 ${v}_{i}[\varphi_i^2-\varphi_{-i}^2]$，可输串（如 2,4-6,9 求和；1-50 即 Δρ^orb；开壳层 α/β 对序号不同，可混合求和）。

菜单路径：后处理菜单 → 1（轨道）/ 2（对密度）。

输入要求：已算 NOCV（选项 2 可视化前若未设格点，用 −5 设置；选项 −5 可随时更改）。

操作步骤（CO–BH₃ 对 1，Medium 格点，等值面 0.005 a.u. 蓝减绿增，CO→BH₃ 给体 0.565 e，能量 −77.9）：选项 2 → 2 → 输 1。对 2（等值面 0.002 a.u.，BH₃ σ(B–H)→CO π* 反馈 −15.8）；其余对 4–26 输 4-26（等值面 0.001 a.u.，能量和 −7.09，极化为主）。

操作步骤（乙烷 α 对 1 + β 对 22，等值面 0.01 a.u.，两者之和为 C–C 成键电子集中）：

```text
2  // Show isosurface of NOCV pair density
2  // Medium-quality grid
1  // Check NOCV pair 1, which is the dominant pair of alpha spin
```

后输 22 看 β 主导对，输 1,22 看两者之和。

产出：NOCV 轨道/对密度等值面图。

来源链接：[4.23.1](sec-4-23-examples-of-ets-nocv-analysis.md)、[4.23.2](sec-4-23-examples-of-ets-nocv-analysis.md)。

## 后处理：Pauli / 轨道 / 总形变密度（选项 3–5）

说明：$\Delta\rho^{\mathrm{Pauli}} = \rho^0-(\rho_A+\rho_B)$（Pauli 排斥致片段间电子减少）、$\Delta\rho^{\mathrm{orb}} = \rho-\rho^0$（= 全部 NOCV 对密度之和，成键区电子累积）、$\Delta\rho = \Delta\rho^{\mathrm{orb}}+\Delta\rho^{\mathrm{Pauli}}$（亦可用主功能 5 自定义操作算）。

菜单路径：后处理菜单 → 3（Pauli）/ 4（轨道）/ 5（总）。

输入要求：已算 NOCV。

操作步骤：分别选 3 / 4 / 5 显示等值面（CO–BH₃ 例：Pauli 图片段间电子减少、轨道图成键区累积、总图净增加）。

产出：三种形变密度等值面图。

来源链接：[3.26.1](sec-3-26-ets-nocv-analysis.md)、[4.23.1](sec-4-23-examples-of-ets-nocv-analysis.md)。

## 后处理：cube 导出（选项 6–10）

说明：把 NOCV 轨道、NOCV 对、Δρ^Pauli、Δρ^orb、Δρ 格点导出为 .cub 供第三方软件渲染。

菜单路径：后处理菜单 → 6–10 中相应项。

输入要求：已算 NOCV（格点设置同选项 1/2，经 −5 定义）。

操作步骤：选 6–10 中对应项导出 .cub。

产出：.cub 文件。

来源链接：[3.26.3](sec-3-26-ets-nocv-analysis.md)。

## 后处理：前分子 / 冻结 / 实际轨道（选项 11–13）

说明：11 看前分子态轨道（片段 MO 并集）；12 看冻结态轨道（占据片段 MO 经 Löwdin 正交化，空轨道与前分子态相同；小等值面下可见正交化引入的额外节面）；13 看复合物实际轨道。

菜单路径：后处理菜单 → 11 / 12 / 13。

输入要求：已算 NOCV。

操作步骤：选 11 / 12 / 13，屏幕列占据轨道信息如：

```text
Orb:     1 Ene(au/eV):     0.000000       0.0000 Occ: 2.000000 Type:A+B
Orb:     2 Ene(au/eV):     0.000000       0.0000 Occ: 2.000000 Type:A+B
Orb:     3 Ene(au/eV):     0.000000       0.0000 Occ: 2.000000 Type:A+B
Orb:     4 Ene(au/eV):     0.000000       0.0000 Occ: 2.000000 Type:A+B
Orb:     5 Ene(au/eV):     0.000000       0.0000 Occ: 2.000000 Type:A+B
Orb:     6 Ene(au/eV):     0.000000       0.0000 Occ: 2.000000 Type:A+B
Orb:     7 Ene(au/eV):     0.000000       0.0000 Occ: 2.000000 Type:A+B
Orb:    31 Ene(au/eV):     0.000000       0.0000 Occ: 2.000000 Type:A+B
Orb:    32 Ene(au/eV):     0.000000       0.0000 Occ: 2.000000 Type:A+B
Orb:    33 Ene(au/eV):     0.000000       0.0000 Occ: 2.000000 Type:A+B
Orb:    34 Ene(au/eV):     0.000000       0.0000 Occ: 2.000000 Type:A+B
```

CO 的 HOMO（MO 7）冻结态在 BH₃ 区多一节面（等值面 0.02）。

产出：三态轨道等值面图。

来源链接：[4.23.1](sec-4-23-examples-of-ets-nocv-analysis.md)。

## 后处理：SCPA 组成（选项 14）

说明：NOCV 轨道组成用 SCPA 法（禁弥散函数；确需弥散函数时回主菜单用主功能 8 的 Hirshfeld/Becke 法），对组成按 ${v}_{i}\Theta_{i}+{v}_{j}\Theta_{j}$（${v}_{j}=-{v}_{i}$）；正值=得电子、负值=失电子（如 A 得 0.3412 e、B 失 0.2053 e）；对组成之和恒为零。

菜单路径：后处理菜单 → 14 → 输入 NOCV 对序号。

输入要求：已算 NOCV；不用弥散函数。

操作步骤：选 14，输 1（研究 NOCV 对 1），输出基函数/壳层/角动量/原子贡献表（略，见 [4.23.1](sec-4-23-examples-of-ets-nocv-analysis.md)）；如硼 2p_z 对 NOCV 对 1 贡献 18.27%+1.77%=20.04%（正部主导），碳 2s 贡献 −1.72%−19.17%=−20.89%（负部主导）。

产出：NOCV 对/轨道组成表。

来源链接：[3.26.3](sec-3-26-ets-nocv-analysis.md)、[4.23.1](sec-4-23-examples-of-ets-nocv-analysis.md)。

## 后处理：显示与格点控制（选项 0 / −3 / −5 / −6）

说明：0 重打印 NOCV 信息；−3 设本征值打印阈值（默认 0.001）；−5 设各类密度格点；−6 手工重定义简并体系 NOCV 对–轨道对应关系（可多次使用）。

菜单路径：后处理菜单 → 0 / −3 / −5 / −6。

输入要求：已算 NOCV。

操作步骤（A–T 碱基对，328 对太多，提高阈值到 0.02 再打印）：

```text
-3  // Set printing threshold of NOCV eigenvalues
0.02
0  // Print NOCV information again
```

得：

```text
       --------------- Pair and NOCV orbital information --------------
There are totally  328 NOCV pairs and   655 NOCV orbitals
NOCV orbitals with absolute eigenvalues smaller than 2.0E-02 are not shown
Note: All energies are given in kcal/mol

 Pair  Energy | Orbital  Eigenvalue    Energy  | Orbital  Eigenvalue    Energy
    1  -11.20       1      0.20598     -15.91      655     -0.20598      38.45
    2   -4.05       2      0.11820     -18.61      654     -0.11820      15.66
    3   -0.79       3      0.07198     -91.72      653     -0.07198     -80.71
    4   -0.79       4      0.07066     -77.74      652     -0.07066     -66.59
    5   -0.59       5      0.04312     -29.08      651     -0.04312     -15.45
    6   -0.34       6      0.03551     -40.19      650     -0.03551     -30.49
    7   -0.27       7      0.02859     -24.18      649     -0.02859     -14.72
    8   -0.15       8      0.02619     -56.34      648     -0.02619     -50.77
    9   -0.15       9      0.02032     -16.97      647     -0.02032      -9.45
Sum of NOCV eigenvalues:  -0.00000
Sum of pair energies:     -18.33 kcal/mol
```

对 1/2（−11.20/−4.05 kcal/mol）分别对应 N20–H26⋯N1 与 O23⋯H14–N10 氢键（等值面 0.002 a.u.，弱相互作用取值远小于化学键）。

产出：筛选后的 NOCV 信息表。

来源链接：[4.23.4](sec-4-23-examples-of-ets-nocv-analysis.md)。
