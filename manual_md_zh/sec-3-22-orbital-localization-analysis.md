# **3.22 轨道定域化分析 (19)**

## **轨道定域化理论**

正则分子轨道 (CMOs, canonical molecular orbitals) 常表现出很强的离域特征，因而不能给出关于化学成键的有用信息。定域化 MO 的方法有很多，最常用的是 Foster-Boys (FB) 定域化、Edmiston–Ruedenberg (ER) 定域化和 Pipek–Mezey (PM) 定域化。NBO 程序中支持的 NLMO 方法也是一种轨道定域化算法。这些方法得到的轨道被称为定域化分子轨道 (LMOs, localized molecular orbitals)。LMO 与 CMO 都是正交归一的基组且维数相同，二者可通过幺正变换相互转换。

FB 是最老的轨道定域化方法，提出于 *Rev. Mod. Phys.*, **32**, 300 (1960)。该方法最小化下面的量，从而使所有轨道的空间分布范围尽可能窄

$$
\left\langle \Omega \right\rangle_{\mathrm{Boys}} = \sum_i \int\int \rho_i(\mathbf{r}_1)(\mathbf{r}_1 - \mathbf{r}_2)^2 \rho_i(\mathbf{r}_2)\mathrm{d}\mathbf{r}_1 \mathrm{d}\mathbf{r}_2 \qquad \rho_i = \left| \varphi_i \right|^2
$$

FB 方法非常流行且应用广泛，因此 Multiwfn 支持它。

ER 定域化提出于 *Rev. Mod. Phys.*, **35**, 457 (1963)，也是一种著名的方法，它通过最大化下面的量（轨道自排斥积分）来定域化轨道

$$
\left\langle \Omega \right\rangle_{\mathrm{ER}} = \sum_i \int\int \rho_i(\mathbf{r}_1) \frac{1}{\left| \mathbf{r}_1 - \mathbf{r}_2 \right|} \rho_i(\mathbf{r}_2)\mathrm{d}\mathbf{r}_1 \mathrm{d}\mathbf{r}_2
$$

ER 方法很不受推崇，因为它需要计算双电子积分，非常复杂；而且积分从 AO 基到 MO 基的变换代价很高。尽管少数论文中有人认为 ER 方法物理意义更好，且引入 resolution-of-identity 技术可显著降低计算代价，但我从不认为有任何令人信服的理由用 ER 方法代替 FB，因此 Multiwfn 不支持 ER 方法。

最流行的轨道定域化方法是 PM。PM 定域化的实质是最大化下面的量，从而使所有轨道的分布范围尽可能收缩

$$
P = \sum_i \sum_A \left( p_A^i \right)^2
$$

在 PM 方法的原始论文 *J. Chem. Phys.*, **90**, 4916 (1989) 中，$p$ *$_{A}^{i}$* 对应 MO $i$ 中原子 *A* 的 Mulliken 布居。而在 *J. Chem. Theory Comput.*, **10**, 642 (2014) 中表明，Löwdin、Hirshfeld、Becke、AIM 等其它布居方法也可与 PM 联用并得到合理的结果。目前 Multiwfn 支持基于 Mulliken、Löwdin 和 Becke 布居的 PM 方法。

## **算法细节**

若对轨道定域化方法的实现细节不感兴趣，可放心跳过本部分。

上述量的最大化或最小化可通过 Jacob sweep 算法完成，该算法用于轨道定域化方法的原始论文中，至今仍被广泛使用。该方法的效率低于后来发展的复杂方法，如幺正优化和信赖域方法；但 Jacob sweep 非常简单，对大多数情形效果很好，特别是在只需要定域化占据轨道时，因此 Multiwfn 采用该算法。

基于各种布居方法的 PM 定域化工作方程大体相同，见 *J. Comput. Chem.*, **14**, 736 (1993) 的 Eq. 9，它们仅在 $Q$ 项的定义上不同，Q 需要在每次 Jacob sweep 迭代中对每个轨道对计算。

对于基于 Mulliken 布居的 PM 定域化（PM-Mulliken 方法），原子 *A* 上轨道 $i$ 和 $j$ 对应的 $Q$ 项为

$$
Q_A^{ij} = \frac{1}{2} \sum_{\mu \in A} \sum_{\nu} \left[ C_{\nu i} C_{\mu j} + C_{\mu i} C_{\nu j} \right] S_{\mu \nu}
$$

其中 *µ* 和 *ν* 对应基函数编号，后者遍历所有基函数。

对于 PM-Löwdin 方法，由于基函数已通过 Löwdin 对称正交化，$Q$ 项简化为

$$
Q_A^{ij} = \sum_{\mu \in A} C_{\mu i} C_{\mu j}
$$

PM-Löwdin 看似比 PM-Mulliken便宜得多；但若编程得当，两种方法的代价基本相同，因为 PM-Mulliken 情形的 $Q$ 可改写为

$$
Q_A^{ij} = \frac{1}{2} \sum_{\mu \in A} \left[ C_{\mu j} (\mathbf{SC})_{\mu i} + C_{\mu i} (\mathbf{SC})_{\mu j} \right]
$$

若在 Jacob sweep 之前计算 **SC** 矩阵并存于内存，且在迭代中频繁更新，则对编号 *ν* 的求和可完全忽略。事实上，由于 Löwdin 方法的对称对角化步骤对大体系耗时，对大体系 PM-Mulliken 的总代价一般低于 PM-Löwdin。

在 PM-Becke，即基于 Becke 布居的 PM 定域化（见第 [3.9.8](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#398-含原子偶极矩校正的-becke-原子电荷-10) 节）中，$Q$ 写为

$$
\begin{gathered} Q_A^{ij} = \mathbf{c}_i^{\mathrm{T}} \mathbf{S}^A \mathbf{c}_j \\ \mathbf{S}_{\mu \nu}^A = \int \chi_\mu(\mathbf{r}) w_A(\mathbf{r}) \chi_\mu(\mathbf{r}) \mathrm{d}\mathbf{r} \end{gathered}
$$

其中 $S^{A}$ 是原子 *A* 处基函数间的原子重叠矩阵，$w$ *$_{A}$*(**r**) 是原子 *A* 的 Becke 权重函数，*χ* 是基函数，$c_{i}$ 代表轨道 $i$ 展开系数的列数组。PM-Becke 方法代价很高，尤其对大体系，这不仅因为用数值积分计算所有原子的原子重叠矩阵相当耗时，而且在整个定域化过程中 $Q$ 项被计算无数次，每次都涉及昂贵的矩阵乘法。

关于 FB 方法，由于它涉及偶极矩积分从 AO 基到 MO 基的变换，需要大量算术运算，因此比 PM-Mulliken 和 PM-Löwdin 贵，但代价显著低于 PM-Becke。

## **应该用哪种轨道定域化方法？**

通常推荐使用 PM-Mulliken 和 PM-Löwdin，因为它们的结果一般令人满意且代价很低。但当存在大量弥散函数时，这些方法可能（但不总是）失效，众所周知弥散函数会严重破坏 Löwdin 和 Mulliken 布居的意义。

若需要用 PM 方法，且弥散函数对描述当前体系的电子结构并非必不可少（*例如* 阴离子或被强外电场严重极化的中性分子），则应改用更稳健但贵得多的 PM-Becke 方法。

FB 定域化也兼容弥散函数，且不如 PM-Becke 昂贵。但 FB 方法定域化的轨道不保持 σ-π 分离特征，例如双键会被表示为两个香蕉键轨道，这与常见的化学直觉有些矛盾，若不在意这一点，可使用 FB 方法。

## **轨道定域化模块的用法**

输入文件必须包含基函数信息，因此可用*例如* .mwfn、.fch、.molden 或 .gms 作为输入文件。该功能仅适用于限制性和非限制性 SCF 波函数。

由于 PM-Mulliken 方法稳健且代价很低，它被选为 Multiwfn 默认的轨道定域化方法。若想换用其它方法，使用选项“-6 Set localization method”。

在界面中，可用选项 1 只定域化占据 MO，或用选项 2 同时定域化占据与非占据 MO（两组轨道分别定域化，*即* 不允许占据与非占据轨道之间混合）。对于非限制性波函数，alpha 与 beta 部分分别处理。通过选项 3 可定域化特定的 MO 子集；换言之，只允许特定的 MO 在定域化过程中混合。该功能可实现特殊目的，例如通过选择适当的 MO 得到特定区域内完全或半定域化的 MO。

轨道定域化是迭代过程，因此应设定收敛判据和最大循环数。默认值一般合适，无需修改。迭代过程中会打印收敛状态，对所有定域化方法，均用 $P = \sum_i \sum_A \left( p_A^i \right)^2$ 的变化判断收敛。

定域化收敛后，会计算所有所得 LMO 的轨道组成并打印 LMO 的主要特征。默认采用稳健的 Hirshfeld 方法计算轨道组成（详见第 [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) 节），也可在轨道定域化之前通过选项“-9 Set the method for calculating orbital composition”换用其它方法。

最后，LMO 被导出到当前文件夹下的 *new.fch*，然后 Multiwfn 自动载入它，之后可用多种方式分析定域化轨道；例如用主功能 0 将其绘制为等值面，或用主功能 8 做轨道组成分析。若不想让 Multiwfn 自动载入新生成的 *new.fch*，可选择一次选项 -3 以切换状态。

## **进行轨道定域化分析的提示**

在 Multiwfn 中，PM-Löwdin 和 PM-Mulliken 方法的代价正比于 $N_{\mathrm{orb}}^{2}$ $N_{\mathrm{bas}}$，而 FB 的代价正比于 $N_{\mathrm{orb}}^{2}$ $N_{\mathrm{bas}}^{2}$，其中 $N_{\mathrm{orb}}$ 和 $N_{\mathrm{bas}}$ 分别是待定域化的轨道数和基函数数。显然 FB 贵得多。PM-Becke 方法对中等大小体系加中等质量基组（*例如* 6-31G\* 基组下的 C₆₀）已极其昂贵，因此绝不要考虑对大体系使用它。

收敛难度一般是：非占据轨道比占据轨道难，大体系比小体系难，FB 比 PM 方法难。

无特殊原因时，**只需定域化占据轨道**，因为只有占据轨道携带关于电子结构的有用信息。定域化非占据轨道比定域化占据轨道耗时得多，因为使用扩展基组时非占据轨道数常多得多。一般地，用 PM-Mulliken/Löwdin 方法，对含至多 200 个原子、中等大小基组的体系，占据轨道可轻松定域化。而对 FB，一般只能实现至多含 100 个原子的体系。

若想降低定域化占据轨道的代价，可选择一次“-5 If also localizing core orbitals”将状态从默认的 "Yes" 切换为 "No"。一般地，价轨道与芯轨道之间的混合很弱，因此在定域化价轨道时忽略内层芯轨道是安全的。但在极少数情形，忽略内层芯轨道可能导致收敛困难。

Multiwfn 中的 PM-Mulliken 和 PM-Löwdin 方法没有并行化，因为我发现并行化并不能明显提速，反而有时使收敛更困难。FB 方法是完全并行化的，因此使用多核 CPU 可显著降低计算代价。

2-zeta 加极化函数质量的基组（*例如* 6-31G\* 和 def2-SVP）对轨道定域化分析已完全足够，用更大质量的基组不会带来可察觉的更好结果。

## **专题 1：计算 LMO 能量**

尽管 LMO 不是 Fock 算符的本征函数，其能量可作为 Fock 算符的期望值计算，可通过矩阵方程求解。具体地，LMO 基下的 Fock 矩阵可由下式得到

$$
\mathbf{F}_{\mathrm{LMO}} = \mathbf{C}^{\mathrm{T}} \mathbf{F}_{\mathrm{AO}} \mathbf{C}
$$

其中 $F_{\mathrm{AO}}$ 是原基函数下的 Fock 矩阵，$\mathbf{C}$ (*µ*, $i$ ) 对应 LMO $i$ 中基函数 *µ* 的系数。LMO $i$ 的能量就是对角项 $F_{\mathrm{LMO}}$ ($i$ , $i$ )。

若想以此方式得到 LMO 能量，应在开始轨道定域化之前选择选项“-4 If calculating and print orbital energies”。然后可用两种方式提供 $\mathbf{F}_{\mathrm{AO}}$：(1) 基于 MO 的能量和系数矩阵通过 $\mathbf{F}_{\mathrm{AO}}=\mathbf{S}\mathbf{C}\mathbf{E}\mathbf{C}^{-1}$ 关系生成 (2) 输入含 $\mathbf{F}_{\mathrm{AO}}$ 的文件的路径，然后载入该矩阵，详见本手册[附录 7](sec-6-7-about-providing-fock-ks-matrix-to-multiwfn.md)。

## **专题 2：揭示 LMO 中心**

为便于把握所得 LMO 的基本分布特征，Multiwfn 可计算 LMO 的中心位置并作为 Bq 原子（幽灵原子）加入当前体系，从而可用主功能 0 方便地可视化它们。LMO 中心按下式计算

$$
\mathbf{R}_i = \left\langle \varphi_i \middle| \mathbf{r} \middle| \varphi_i \right\rangle
$$

其中 **r** 是坐标矢量。

要生成 LMO 中心，应选择一次“-8 If calculating center position and dipole moment of LMOs”将其状态切换为“Yes”。然后在生成 LMO、导出 .fch 并重载后，会计算 LMO 的中心位置并作为 Bq 原子加入。LMO 中心的坐标以及 LMO 编号与 Bq 编号的对应关系将输出到当前文件夹下的 *LMOcen.txt*，同时主功能 0 的设置会被设为显示 LMO 中心的最佳状态（如第 [4.19.1](sec-4-19-orbital-localization-analysis.md#4191-用-pipek-mezey-方法定域-13-丁二烯的分子轨道) 节所示）。由于新加入的 Bq 原子没有伴随的基函数，当前波函数不应再做波函数分析，否则 Multiwfn 可能崩溃或结果完全无意义。

注意若存在重键且使用 PM 定域化算法，同一键的 σ-LMO 与 π-LMO 中心对应的 Bq 原子可能重叠。改用 FB 算法可避免这一点，因为 FB 把重键表示为多个香蕉键 LMO，其中心位置明显不同。

## **专题 3：占据 LMO 的偶极矩分析**

一旦“-8 If calculating center position and dipole moment of LMOs”被切换为“Yes”，做完轨道定域化后，会询问是否同时对占据 LMO 做偶极矩分析。若输入 *y*，则得到 *LMOdip.txt*，其中包含所有占据 LMO 的偶极矩分析结果。为使你正确理解输出，下面描述细节。

占据 LMO 的电子对整个体系偶极矩的贡献为

$$
\mathbf{D}_i = \left\langle \varphi_i \middle| -\mathbf{r} \middle| \varphi_i \right\rangle
$$

所有 LMO 的该矢量作为“LMO 对体系偶极矩的贡献”输出在 *LMOdip.txt* 文件中。

但该量不能直接用来度量 LMO 的极性。给定 **r** = (**r**- $\mathbf{r}_\mathrm{c}$ )+ $\mathbf{r}_\mathrm{c}$，其中 $\mathbf{r}_\mathrm{c}$ 是固定点，上式可改写为

$$
\begin{aligned} & \mathbf{D}_i = \left\langle \varphi_i \middle| -(\mathbf{r} - \mathbf{r}_\mathrm{c}^i) \middle| \varphi_i \right\rangle - \left\langle \varphi_i \middle| \mathbf{r}_\mathrm{c}^i \middle| \varphi_i \right\rangle \\ & = -\left\langle \varphi_i \middle| \mathbf{r} - \mathbf{r}_\mathrm{c}^i \middle| \varphi_i \right\rangle - \mathbf{r}_\mathrm{c}^i \left\langle \varphi_i \middle| \varphi_i \right\rangle \\ & = -\left\langle \varphi_i \middle| \mathbf{r} - \mathbf{r}_\mathrm{c}^i \middle| \varphi_i \right\rangle - \mathbf{r}_\mathrm{c}^i \end{aligned}
$$

可定义量 $\mathbf{d}_{i}$，度量轨道相对于 $\mathbf{r}_\mathrm{c}$ 的偶极矩：

$$
\mathbf{d}_i = -\left\langle \varphi_i \middle| \mathbf{r} - \mathbf{r}_\mathrm{c}^i \middle| \varphi_i \right\rangle = \mathbf{D}_i + \mathbf{r}_\mathrm{c}^i
$$

若为轨道恰当选择 $\mathbf{r}_\mathrm{c}$，则 $\mathbf{d}_{i}$ 可能反映 LMO 的极性。

对每个被识别为单中心 LMO，$\mathbf{r}_\mathrm{c}$ 自动设为对该 LMO 贡献最大的原子的位置。因此 $\mathbf{d}_{i}$ 代表 LMO 电子分布质心相对于核位置的偏离。这些 {**d**} 在 *LMOdip.txt* 中打印为“单中心轨道偶极矩 (a.u.)”。

对每个被识别为双中心 LMO，假设贡献最大的两个原子为 $A$ 和 $B$，$\mathbf{r}_\mathrm{c}$ 设为

$$
\mathbf{r}_\mathrm{c} = \mathbf{r}_A \frac{R_B}{R_A + R_B} + \mathbf{r}_B \frac{R_A}{R_A + R_B}
$$

其中 $\mathbf{r}_{A}$ 和 $R$ *$_{A}$* 分别是原子 *A* 的核位置和共价半径，原子 *B* 类似。$\mathbf{r}_\mathrm{c}$ 位于成键区中心，因此 $\mathbf{d}_{i}$ 体现 LMO 电子分布质心相对 $\mathbf{r}_\mathrm{c}$ 的偏离，能够揭示键极性。这些 {**d**} 在 *LMOdip.txt* 中打印为“双中心轨道偶极矩 (a.u.)”。

对闭壳情形，打印的 **d** 数据乘了 2 因子，因为 LMO 是双占据的。对开壳情形，alpha 与 beta LMO 的 **d** 分别打印。

作为副产物，整个体系的偶极矩以及核贡献和电子贡献也打印在 *LMOdip.txt* 开头。重要的是注意，即使已没有离域的 LMO，所有 LMO 的 **d** 之和一般也不等于整个体系的偶极矩。

顺便说：事实上，只有当所有 **d** 中的 $\mathbf{r}_\mathrm{c}$ 矢量之和等于 $-\sum_{A} {Z}_{A}{\mathbf{r}}_{A}$，即恰好抵消体系偶极矩的核贡献时，所有 **d** 之和才等于体系偶极矩。若想满足这一点，应对所有双中心 LMO 采用 ($\mathbf{r}_{A}$ + $\mathbf{r}_{B}$ )/2 作为 $\mathbf{r}_\mathrm{c}$，且所有 LMO 恰好对应当前体系的一个 Lewis 结构。当然，LMO 分析的当前实现不满足这些条件（但 NBO 理论的“DIPOLE”分析满足）。注意若取 ($\mathbf{r}_{A}$ + $\mathbf{r}_{B}$ )/2 为 $\mathbf{r}_\mathrm{c}$ 同时又用双中心 LMO 的 **d** 度量键极性，会得到荒谬的结果，例如会发现 C-H 甚至比 O-H 极性大得多！

轨道定域化分析的例子见第 [4.19](sec-4-19-orbital-localization-analysis.md) 节。LOBA/mLOBA 方法的例子（第 [4.8.4](sec-4-8-molecular-orbital-composition-analysis.md#484-用lobamloba方法计算氧化态) 节）和第 [4.100.22](sec-4-100-other-functions-part-1.md#410022-分析非平面体系-non-planar-system的π电子-π-electron特征环庚三烯-cycloheptatriene) 节也用到了本功能。

> **所需信息**
>
> 原子坐标、基函数
