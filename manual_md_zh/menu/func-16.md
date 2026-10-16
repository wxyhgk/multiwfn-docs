# 主功能16：电荷分解分析与轨道相互作用图

功能概述：电荷分解分析（CDA）用于揭示复合物中各片段之间如何转移电荷以达到电荷平衡，其思想基于片段轨道（FO，即片段孤立状态下的分子轨道）。Multiwfn 采用的是广义 CDA 形式，既适用于闭壳层也适用于开壳层、post-HF（自然轨道）情形。进入模块后先载入复合物文件，再设置片段数目并依次载入各片段文件，即可打印 d（给予）/b（回授）/r（排斥极化）项与 ECDA 净转移电子数，还可查看复合物轨道的片段轨道组成、分解轨道对贡献、绘制轨道相互作用图。

## 打印 CDA/ECDA 结果（选项0/1）

说明：输出两片段之间的 d、b、d−b 与 r 项，以及 ECDA 的净转移电子数。选项1仅在轨道为自然轨道时可用，显示全部复合物轨道（含高于 LUNO+4 的轨道）。

菜单路径：主功能16（电荷分解分析）→ 选项0 / 选项1（选项-3 设打印阈值，选项-2 把输出切换到 CDA.txt）

输入要求：复合物文件 + 各片段文件（.mwfn/.fch/.molden/.gms 或 Gaussian 输出；复合物与片段的方法基组须相同、坐标完全一致、原子顺序可拼接，避免使用弥散函数；Gaussian 计算须加 nosymm，混合基组加 5d）。

操作步骤（原始格式，闭壳层 CO→BH₃ 例）：

```text
examples\CDA\COBH3\COBH3.fch  // Gaussian .fch file of the complex
16  // Enter CDA module
2  // We define two fragments
examples\CDA\COBH3\CO.fch  // Gaussian .fch file of fragment 1
examples\CDA\COBH3\BH3.fch  // Gaussian .fch file of fragment 2
```

屏幕立刻输出 CDA 结果：

```text
   Orb.      Occ.          d           b        d - b          r
      1    2.000000   -0.000004   -0.000000   -0.000004   -0.000001
      2    2.000000    0.001119   -0.000023    0.001141    0.000326
      3    2.000000   -0.000002   -0.000471    0.000469    0.000313
      4    2.000000   -0.013250   -0.000704   -0.012546   -0.005676
      5    2.000000    0.041648   -0.003309    0.044957    0.232262
      6    2.000000    0.037385   -0.020136    0.057521    0.212422
      7    2.000000   -0.000543    0.000647   -0.001190    0.022166
      8    2.000000   -0.000543    0.000647   -0.001190    0.022166
      9    2.000000    0.171353    0.026952    0.144401   -0.741381
     10    2.000000   -0.000569    0.043713   -0.044281   -0.038916
     11    2.000000   -0.000569    0.043713   -0.044282   -0.038916
     12    0.000000    0.000000    0.000000    0.000000    0.000000
     13    0.000000    0.000000    0.000000    0.000000    0.000000
     14    0.000000    0.000000    0.000000    0.000000    0.000000
     15    0.000000    0.000000    0.000000    0.000000    0.000000
 ......
-------------------------------------------------------------------
Sum:      22.000000    0.236023    0.091027    0.144996   -0.335233
```

"Orb." 指复合物轨道序号，"occ." 为占据数；d(i) 为经该轨道从片段1施舍到片段2的电子量，b(i) 为反施舍量；r(i) 为两片段占据 FO 之间的交叠布居，正值表示电子累积到交叠区（成键特征），负值表示耗散（排斥效应）。之后输出 ECDA 结果：

```text
     ========== Extended Charge decomposition analysis (ECDA) ==========
  Contribution to all occupied complex orbital:
Occupied, virtual orbitals of fragment  1:     680.4194%         8.0593%
Occupied, virtual orbitals of fragment  2:     390.3988%        21.1226%
  Contribution to all virtual complex orbital:
Occupied, virtual orbitals of fragment  1:      19.5806%      2291.9407%
Occupied, virtual orbitals of fragment  2:       9.6012%      1678.8774%
PL( 1) + CT( 1-> 2) =    0.3916      PL( 1) + CT( 2-> 1) =    0.1612
PL( 2) + CT( 1-> 2) =    0.4225      PL( 2) + CT( 2-> 1) =    0.1920
The net electrons obtained by frag. 2 = CT( 1-> 2) - CT( 2-> 1) =    0.2304
```

通常只需关注最后一行：从片段1向片段2净转移的电子数。

产出：各复合物轨道的 d/b/d−b/r 表与总和；ECDA 四项与净转移电子数。

来源：[3.19](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md)、[4.16.1](sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md#4161-闭壳层相互作用情形cobh₃)

## 查看复合物轨道的片段轨道组成（选项2）

说明：输出指定复合物轨道中各片段轨道的 Mulliken（或 SCPA）组成，定位关键片段轨道贡献。默认只显示贡献 ≥1% 的片段轨道（阈值可用 settings.ini 中的 "compthresCDA" 修改）。输入 x 输出复合物轨道 x 的组成；输入如 1,6 输出片段1轨道6在所有复合物轨道中的组成。

菜单路径：主功能16 → 选项2

输入要求：同上（CDA 已载入复合物＋片段波函数）。

操作步骤（原始格式，接上例）：在菜单中选选项 2 并输入 `9`，配合物轨道 9 的组成如下所示：

```text
Occupation number of orbital     9 of the complex:  2.00000000
Orbital     7 of fragment  1, Occ: 2.00000    Contribution:   25.8560%
Orbital    13 of fragment  1, Occ: 0.00000    Contribution:    1.0798%
Orbital     2 of fragment  2, Occ: 2.00000    Contribution:   57.2921%
Orbital     5 of fragment  2, Occ: 0.00000    Contribution:   14.5640%
```

由此可推断 CO→BH₃ 电子转移本质上是 CO 的 FO 7（占据）与 BH₃ 的 FO 5（虚）之间的混合。

产出：指定复合物轨道的片段轨道组成表。

来源：[3.19.3](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md#3193-使用方法)、[4.16.1](sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md#4161-闭壳层相互作用情形cobh₃)

## 导出片段轨道系数/重叠矩阵（选项3/4）

说明：选项3导出复合物轨道在片段轨道基下的系数矩阵，选项4导出片段轨道之间的重叠矩阵。

菜单路径：主功能16 → 选项3 / 选项4

输入要求：同上。

操作步骤（原始格式）：

- **3 以片段轨道基导出复合物轨道的系数矩阵**：所有复合物轨道中所有片段轨道对应的系数矩阵将输出到当前文件夹下的 *coFO.txt*。
- **4 导出片段轨道之间的重叠矩阵**：所有片段轨道之间的重叠矩阵将输出到当前文件夹下的 *ovlpint.txt*。

产出：当前文件夹下的 *coFO.txt*（选项3）、*ovlpint.txt*（选项4）。

来源：[3.19.3](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md#3193-使用方法)

## 分解复合物轨道的 CDA 贡献（选项6）

说明：把指定复合物轨道的 d、b、r 项分解为片段轨道对的贡献，需输入复合物轨道指标并设置打印阈值。

菜单路径：主功能16 → 选项6

输入要求：同上。

操作步骤（原始格式，以复合物轨道 9 为例）：输入 `0` 回到上一级菜单，选选项 6 并输入 `9`，再输入阈值如 `0.005`，则对 d、b、r 任一项贡献大于 0.005 的 FO 对都打印出来：

```text
FragA Orb(Occ.)  FragB Orb(Occ.)      d           b        d - b          r
   4( 2.0000)       2( 2.0000)    0.000000    0.000000    0.000000   -0.009969
   7( 2.0000)       1( 2.0000)    0.000000    0.000000    0.000000   -0.005759
   7( 2.0000)       2( 2.0000)    0.000000    0.000000    0.000000   -0.723845
   7( 2.0000)       5( 0.0000)    0.176503    0.000000    0.176503    0.000000
   7( 2.0000)       8( 0.0000)    0.006221    0.000000    0.006221    0.000000
   7( 2.0000)      11( 0.0000)    0.005846    0.000000    0.005846    0.000000
   7( 2.0000)      12( 0.0000)   -0.023941    0.000000   -0.023941    0.000000
  13( 0.0000)       2( 2.0000)    0.000000    0.021958   -0.021958    0.000000
```

从输出清楚看到，CO 的 FO 7 与 BH₃ 的 FO 5 之间的混合贡献了配合物轨道 9 的绝大部分 d 项。

产出：指定复合物轨道的片段轨道对贡献表。

来源：[3.19.3](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md#3193-使用方法)、[4.16.1](sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md#4161-闭壳层相互作用情形cobh₃)

## 绘制轨道相互作用图（选项5）

说明：按能量为每条复合物轨道和片段轨道画线，若某片段轨道在某复合物轨道中的组成大于判据（默认 10%），则用红线连接。post-HF（自然轨道，能量未定义）时不可用。可用选项 "4 Set the rule for connecting and drawing orbital bars" 设置连接和绘制规则，选项 "12 Set orbital energy shifting value" 平移某侧轨道能量。

菜单路径：主功能16 → 选项5（子菜单：选项3 设能量范围，选项1 绘图，选项5 切换自旋，选项4 设连接规则，选项12 设能量平移）

输入要求：同上（post-HF 无轨道能量时不可用）。

操作步骤（原始格式，接 COBH₃ 例）：输入 `0` 回到上一级菜单，再选 5 进入绘制轨道相互作用图的菜单。选选项 3 并输入 -30,10，把图的能量下限和上限分别设为 -30eV 和 10eV。再选选项 1 以默认设置绘图，屏幕弹出图形。占据和虚轨道分别用实线和虚线短棒表示，轨道序号用蓝色文字标注；同一短棒出现多个标注即能量简并；组成大于 10% 的 FO–复合物轨道对用红线连接，组成标注在线中央。

产出：屏幕弹出的轨道相互作用图（占据实线/虚设虚线，能量为纵坐标，红线标出主要混合）。

来源：[3.19.3](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md#3193-使用方法)、[4.16.1](sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md#4161-闭壳层相互作用情形cobh₃)

## 开壳层（共价结合）体系 CDA 分析（CH₃–NH₂）

说明：两片段以共价键结合时，必须翻转其中一片段的电子自旋，使 α/β 电子数与复合物守恒。此时 d−b 不如 ECDA 可靠，但 d/b 的轨道分解仍有用。

菜单路径：主功能16 → 选项2（定义两片段）→ 翻转其中一片段自旋

输入要求：配合物 .fch＋两开壳层片段 .fch。

操作步骤（原始格式）：

```text
examples\CDA\CH3NH2\CH3NH2.fch  // Gaussian output file of the complex
16  // Enter CDA module
2  // We define two fragments
examples\CDA\CH3NH2\CH3.fch  // Gaussian output file of fragment 1
examples\CDA\CH3NH2\NH2.fch  // Gaussian output file of fragment 2
n  // Do not flip electron spin of fragment 1
y  // Flip electron spin of fragment 2, then NH_2 will have 4 alpha and 5 beta electrons.
```

屏幕分别对 alpha 和 beta 电子计算并打印 CDA 和 ECDA 结果。总电子的结果即二者之和：

```text
d=  0.044335  b=  0.145181  d - b = -0.100847  r= -0.172318
CT( 1-> 2) - CT( 2-> 1) for all electrons:    0.1252
```

d−b 为负与化学直觉（电子从 CH₃ 流向电负性更大的 NH₂）矛盾，而 ECDA 的 0.1252 符合预期，说明对开壳层相互作用 d−b 不如 ECDA 可靠。

产出：分自旋的 CDA/ECDA 结果与总和；β 自旋轨道相互作用图（选项5 → 选项5 切到 Beta → 选项3 设 -30,10 → 选项1 绘图）。

来源：[4.16.2](sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md#4162-开壳层相互作用情形ch₃nh₂)

## 多片段 CDA 分析（顺铂）与 RO 波函数 CDA（乙烷）

说明：可定义任意多个片段；多于两个片段时 ECDA 不可用，需用选项0指定片段对分别输出。限制性开壳层（RO）波函数须先转为非限制（UKS）形式再做常规两片段 CDA。

菜单路径：主功能16 → 选项3（定义三片段）→ 选项0 选片段对；RO 转 UKS：主功能6 → 选项37 → 主功能100 → 选项2 → 7 导出 .fch → 主功能16 → 选项2

输入要求：配合物与各片段的 .fch（原子顺序须与配合物一致；RO 情形先转换）。

操作步骤（原始格式，顺铂例）：

```text
examples\CDA\Pt(NH3)2Cl2\Pt(NH3)2Cl2.fch  // Complex
16  // CDA module
3  // Define three fragments
examples\CDA\Pt(NH3)2Cl2\Pt.fch  // Fragment 1
examples\CDA\Pt(NH3)2Cl2\Cl2.fch  // Fragment 2
examples\CDA\Pt(NH3)2Cl2(NH3)2.fch  // Fragment 3
```

然后选选项 0 并输入 `1,2`，输出片段对 1-2 的 CDA 分析结果；同样得 1-3 和 2-3 结果：

|         | 1-2     | 1-3     | 2-3     |
|---------|---------|---------|---------|
| *d*     | 0.0017  | 0.0077  | 0.0538  |
| *b*     | 0.5156  | 0.0368  | 0.0071  |
| *d*-*b* | -0.5139 | -0.0291 | 0.0467  |
| *r*     | 0.0581  | -0.0579 | -0.1415 |

操作步骤（原始格式，乙烷 RO 转 UKS 例，以 CH3_1.fch 为例）：

```text
examples\CDA\CH3CH3\CH3_1.fch
6  // Modify wavefunction
37  // Split spatial orbitals (RO orbitals in the current context) as alpha and beta spin orbitals
-1  // Return
100  // Other functions (Part 1)
2  // Export current wavefunction to a file
7  // Export to .fch file
CH3_1_UKS.fch  // Name of new file
```

同样把 CH3_2.fch 转为 CH3_2_UKS.fch 后做 CDA：

```text
examples\CDA\CH3CH3\ethane.fch
16  // CDA
2  // Two fragments
examples\CDA\CH3CH3\CH3_1_UKS.fch
examples\CDA\CH3CH3\CH3_2_UKS.fch
n  // Do not flip spin of fragment 1
y  // Flip spin of fragment 2
```

产出：各片段对的 d/b/d−b/r 表；UKS 转换后的新 .fch 文件与分自旋 CDA 结果；α 自旋轨道相互作用图（选项5 → 3 设 -25,10 → 1 绘图）。

来源：[4.16.3](sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md#4163-多于两个片段的情形ptnh₃₂cl₂)、[4.16.4](sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md#4164-基于限制性开壳层波函数的-cda-分析乙烷)
