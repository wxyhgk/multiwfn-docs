# 键序分析(Bond order analysis) (9)

> Multiwfn manual, p.141–154.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.141 -->


fragment 并得到片段氧化态，结果将为 -6，每个碳的氧化态应视为 -6/2 = -3，这是完全合理的。

LOBA/mLOBA 方法的结果在一定程度上取决于轨道成分分析方法的选择。Multiwfn 对 LOBA/mLOBA 分析采用 Hirshfeld 方法，该方法比 LOBA 原始文献中所用的 Mulliken 方法稳健得多。因此，尽管一些文献报道了 LOBA 的某些失效例子，但在 Multiwfn 中这些例子大多并不失效！

用法 要使用该功能，你应提供记录 LMO（或 NBO）的 .mwfn、.fch 或 .molden 文件。例如，你可以用 Multiwfn 进行轨道定域化以生成包含 LMO 的波函数文件。如果你是 Gaussian 用户，你可以用 pop=saveNBO 或 pop=saveNLMO 任务得到的 .fch 文件作为输入文件，基于 NBO 或 NLMO 进行 LOBA 分析。当内存中已有 LMO 时，你可以进入主功能 8(Main function 8)的子功能 100(subfunction 100)，然后若输入一个阈值（例如 50），你将得到 LOBA 方法的氧化态；或者，若输入 m，你将得到 mLOBA 方法的氧化态。你也可以在 LOBA/mLOBA 界面中输入 -1 来定义一个片段，片段氧化态将与原子氧化态一起打印输出。

一个例子见第 4.8.4 节(Section 4.8.4)。

## 3.11 键序分析(Bond order analysis) (9)

在键序分析模块中，你可以直接选择相应选项以用对应方法分析键序。

如果你想得到两个分子片段中原子之间的总键序，你可以用选项 -1 先定义片段 1 和片段 2，然后再进行键序分析。接着若你选择一个计算键序的选项，两个片段之间的总键序 IRS 将通过对原子间键序求和计算如下，并在输出双中心键序的同时一并输出 RSABA R B SII = 

显然，片段间键序计算不适用于多中心键序分析、轨道占据数微扰 Mayer 键序和 Wiberg 键序分解分析。

### 3.11.1 Mayer 键序分析(Mayer bond order analysis) (1)

原子 A 与 B 之间的 Mayer 键序定义为 (Chem. Phys. Lett, 97, 270 (1983))

$$I_{_{AB}}=I_{_{AB}}^{\alpha}+I_{_{AB}}^{\beta}=2\sum_{a\in A}\sum_{b\in B}[(\mathbf{P}^{\alpha}\mathbf{S})_{ba}(\mathbf{P}^{\alpha}\mathbf{S})_{ab}+(\mathbf{P}^{\beta}\mathbf{S})_{ba}(\mathbf{P}^{\beta}\mathbf{S})_{ab}]$$

<!-- formula-ocr: formula_p141_076.png 已替换为LaTeX, 原图保留备查 -->

其中 Pα 和 Pβ 分别为 α 和 β 密度矩阵，S 为重叠矩阵。上式可利用总密度矩阵 P=Pα+Pβ 和自旋密度矩阵 Ps=Pα−Pβ 等价地改写为

$$I_{_{AB}}=\sum_{a\in A}\sum_{b\in B}[(\mathbf{P}\mathbf{S})_{ba}(\mathbf{P}\mathbf{S})_{ab}+(\mathbf{P}^{\mathrm{s}}\mathbf{S})_{ba}(\mathbf{P}^{\mathrm{s}}\mathbf{S})_{ab}]$$

<!-- formula-ocr: formula_p141_077.png 已替换为LaTeX, 原图保留备查 -->

对于限制性闭壳层情形，由于自旋密度矩阵为零，公式可简化为

<!-- p.142 -->


$$I_{_{AB}}=\sum_{a\in A}\sum_{b\in B}(\mathbf{PS})_{ab}(\mathbf{PS})_{ba}$$

<!-- formula-ocr: formula_p142_078.png 已替换为LaTeX, 原图保留备查 -->

一般而言，Mayer 键序的数值与经验键序一致；对单键、双键和三键，其数值分别接近 1.0、2.0 和 3.0。对于非限制或限制性开壳层波函数，α、β 和总 Mayer 键序将分别输出。默认只在屏幕上打印键序超过 0.05 的键，该阈值可通过 `settings.ini` 中的 “bndordthres” 参数调节，你也可以选择导出完整的键序矩阵。

此外，Multiwfn 还输出总价(total valence)和自由价(free valence)，前者定义为

$$F_{A}=V_{A}-\sum_{B\neq A}I_{AB}=\sum_{a\in A}\sum_{b\in A}(\mathbf{P}^{\mathrm{s}}\mathbf{S})_{ab}(\mathbf{P}^{\mathrm{s}}\mathbf{S})_{ba}$$

<!-- formula-ocr: formula_p142_079.png 已替换为LaTeX, 原图保留备查 -->

后者定义为

对于限制性闭壳层波函数，由于 Ps=0，自由价为零，因此原子的总价就是相关键序之和

$$V_{A}=\sum_{B\neq A}I_{AB}$$

<!-- formula-ocr: formula_p142_080.png 已替换为LaTeX, 原图保留备查 -->

总价（亦称原子价，atomic valence）衡量原子的成键能力，而自由价刻画通过共享电子对形成新键的剩余能力。

对于非限制或限制性开壳层体系，除了对 α 和 β 键序求和之外，还有另一种计算总键序的方法，即先把 α 和 β 密度矩阵相加形成总密度矩阵，再用限制性闭壳层公式计算 Mayer 键序，这种处理有时称为“广义 Wiberg 键序(generalized Wiberg bond order)”，这些总键序打印在标题 “Mayer bond order from mixed alpha&beta density matrix” 之后。

与 Mulliken 布居类似，Mayer 键序及下述多中心键序对基组敏感，因此不要使用带有弥散函数的基组，否则键序结果将不可靠。

虽然 Mayer 键序最初是针对单行列式波函数定义的，但对于后 HF 波函数，Multiwfn 基于相应的后 HF 密度矩阵，用与上式完全相同的公式计算 Mayer 键序。这种处理的合理性已在 Chem. Phys. Lett., 544, 83 (2012) 中得到验证。

Mayer 键序的一些应用可见 J. Chem. Soc., Dalton Trans., 2001, 2095。

所需信息：基函数(Basis functions)

### 3.11.2 多中心键序分析(Multi-center bond order analysis) (2, -2, -3)

在主功能 9(Main function 9)中有三个选项 (2, -2, -3) 用于计算多中心键序，它们非常相似，下面依次介绍。最后，还会提到关于原子序号输入顺序的一个值得注意的问题。

<!-- p.143 -->


**选项 2：标准多中心键序(Standard multi-center bond order)** 多中心键指数最初提出于 Struct. Chem., 1, 423 (1990)，我更愿意称之为多中心键序(MCBO)，因为它的形式与 Mayer 键序非常相似。在某种意义上，MCBO 可视为 Mayer 键序向多中心情形的推广。三/四/五/六中心键序分别定义为

$$\begin{aligned}&I_{ABC}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}(\mathbf{PS})_{ab}(\mathbf{PS})_{bc}(\mathbf{PS})_{ca}\\&I_{ABCD}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\sum_{d\in D}(\mathbf{PS})_{ab}(\mathbf{PS})_{bc}(\mathbf{PS})_{cd}(\mathbf{PS})_{da}\\&I_{ABCDE}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\sum_{d\in D}\sum_{e\in E}(\mathbf{PS})_{ab}(\mathbf{PS})_{bc}(\mathbf{PS})_{cd}(\mathbf{PS})_{de}(\mathbf{PS})_{ea}\\&I_{ABCDEF}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\sum_{d\in D}\sum_{e\in E}\sum_{f\in F}(\mathbf{PS})_{ab}(\mathbf{PS})_{bc}(\mathbf{PS})_{cd}(\mathbf{PS})_{de}(\mathbf{PS})_{ef}(\mathbf{PS})_{fa}\\ \end{aligned}$$

<!-- formula-ocr: formula_p143_081.png 已替换为LaTeX, 原图保留备查 -->

$$\begin{aligned}&I_{ABC}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}(\mathbf{PS})_{ab}(\mathbf{PS})_{bc}(\mathbf{PS})_{ca}\\&I_{ABCD}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\sum_{d\in D}(\mathbf{PS})_{ab}(\mathbf{PS})_{bc}(\mathbf{PS})_{cd}(\mathbf{PS})_{da}\\&I_{ABCDE}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\sum_{d\in D}\sum_{e\in E}(\mathbf{PS})_{ab}(\mathbf{PS})_{bc}(\mathbf{PS})_{cd}(\mathbf{PS})_{de}(\mathbf{PS})_{ea}\\&I_{ABCDEF}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\sum_{d\in D}\sum_{e\in E}\sum_{f\in F}(\mathbf{PS})_{ab}(\mathbf{PS})_{bc}(\mathbf{PS})_{cd}(\mathbf{PS})_{de}(\mathbf{PS})_{ef}(\mathbf{PS})_{fa}\\ \end{aligned}$$

$$I_{ABCDEF\ldots K}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\cdots\sum_{k\in K}(\mathbf{PS})_{ab}(\mathbf{PS})_{bc}(\mathbf{PS})_{cd}\cdots(\mathbf{PS})_{ka}$$

<!-- formula-ocr: formula_p143_082.png 已替换为LaTeX, 原图保留备查 -->

类似地，无限中心键序可写为

对于开壳层情形，MCBO 有两种定义，第一种是 α 部分与 β 部分之和：

$$\begin{aligned}I_{ABCDEF\cdots K}&=I_{ABCDEF\cdots K}^{\alpha}+I_{ABCDEF\cdots K}^{\beta}\\&=2^{n-1}\left[\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\cdots\sum_{k\in K}(\mathbf{P}^{\alpha}\mathbf{S})_{ab}(\mathbf{P}^{\alpha}\mathbf{S})_{bc}(\mathbf{P}^{\alpha}\mathbf{S})_{cd}\cdots(\mathbf{P}^{\alpha}\mathbf{S})_{ka}\right]\\&\quad+2^{n-1}\left[\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\cdots\sum_{k\in K}(\mathbf{P}^{\beta}\mathbf{S})_{ab}(\mathbf{P}^{\beta}\mathbf{S})_{bc}(\mathbf{P}^{\beta}\mathbf{S})_{cd}\cdots(\mathbf{P}^{\beta}\mathbf{S})_{ka}\right]\\ \end{aligned}$$

<!-- formula-ocr: formula_p143_083.png 已替换为LaTeX, 原图保留备查 -->

另一种定义是使用混合密度矩阵，这不如上式严格：

$$I_{A B C D E F\ldots K}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\ldots\sum_{k\in K}(\mathbf{P}^{\mathrm{m i x e d}}\mathbf{S})_{a b}(\mathbf{P}^{\mathrm{m i x e d}}\mathbf{S})_{b c}(\mathbf{P}^{\mathrm{m i x e d}}\mathbf{S})_{c d}\ldots(\mathbf{P}^{\mathrm{m i x e d}}\mathbf{S})_{k a}$$

PPP mixed =+ αβ

对于非限制或限制性开壳层波函数，MCBO 分析的输出由四项组成，已在上文说明：(1) 来自 α 密度矩阵的结果 (2) 来自 β 密度矩阵的结果 (3) α 与 β 部分结果之和 (4) 来自混合 α&β 密度矩阵的结果。通常，若你只关心总 MCBO，应使用 (3)。

注意，不同中心数的 MCBO 不能直接比较，因为结果不在同一量级。但在 Phys. Chem. Chem. Phys., 18, 11839 (2016) 中指出，归一化 MCBO 对不同环大小是可比的，可简单计算为 MCBO1/n，其中 n 为中心数。例如，在 B3LYP/6-31G* 水平下，H3+、苯（6 中心）和萘（10 中心）的 MCBO 分别为 0.2963、0.0863 和 0.0080，而归一化结果分别为 0.667、0.665 和 0.617。当 MCBO 为负时，归一化值将计算为 -|MCBO|1/n。通常，若你需要在不同中心数之间比较 MCBO，应采用 Multiwfn 打印的归一化 MCBO，否则建议使用原始 MCBO 值。

Multiwfn 能够自动搜索多中心键。当 Multiwfn

<!-- p.144 -->


要求你输入原子组合时，若你输入 -3，将计算所有三中心键序，只有大于你输入阈值的才会被打印。类似地，分别输入 -4、-5 和 -6 可搜索四、五和六中心键。出于效率考虑，搜索可能不是穷举的。还要注意，对开壳层情形，搜索基于混合 α&β 密度矩阵。

在主功能 9(Main function 9)中还有一个隐藏选项 -3，用于在 Löwdin 正交化基下计算 MCBO。该选项与上述选项 2 的唯一区别在于，该选项在计算 MCBO 之前先对基函数做 Löwdin 正交化。由于该方法相对标准 MCBO 定义没有明显优势，该选项很少使用，因而在界面中不可见。不过，若你有兴趣，可以一试。

选项 -2：在自然原子轨道(NAO)基下的多中心键序(Multi-center bond order in natural atomic orbital (NAO) basis) MCBO 最严重的缺点是高度的基组依赖性。特别地，若存在弥散函数，则 MCBO 结果可能具有误导性或完全没有意义。为解决该问题，我提出了一种替代计算 MCBO 的方法（待发表），其思想已作为选项 -2 实现。

选项 -2 与上文介绍的选项 2 非常相似，唯一区别在于 MCBO 是基于自然原子轨道(NAO)基而非基组原来定义的基函数计算的。由于 NAO 是正交归一集，因而重叠矩阵 S 为单位矩阵，公式可简化为（以闭壳层形式为例）

$$I_{_{ABCDEF\ldots K}}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\cdots\sum_{k\in K}P_{ab}P_{bc}P_{cd}\cdots P_{ka}$$

<!-- formula-ocr: formula_p144_084.png 已替换为LaTeX, 原图保留备查 -->

以这种方式计算的 MCBO 对基组变化具有很好的稳定性。即使存在弥散函数，结果仍然完全可靠。根据我的经验，若没有基函数表现出弥散特征，选项 2 和 -2 给出的结果会非常相似，尽管不完全相同。

要使用选项 -2，应使用 Gaussian 内嵌的 NBO 模块或独立 NBO 程序（即 GENNBO）的输出文件作为输入文件，且必须使用 DMNAO 关键词使 NBO 打印 NAO 基下的密度矩阵。例如，若你是 Gaussian 用户，你可以用下面实例的输出文件作为 Multiwfn 的输入文件（对此分析不要使用 .fch 文件！）。

```text
#p PBE1PBE/6-311G** pop=nboread

opted

0 1
 C                  0.00000000    1.38886900    0.00000000
... [ignored]
 H                 -2.14060700    1.23588000    0.00000000

$NBO DMNAO $END
```

在该功能中，若你只输入两个原子的序号，则结果就是 NAO 基下的 Wiberg 键序，与 NBO 程序用 bndidx 关键词打印的结果完全相同。

<!-- p.145 -->


**原子序号输入顺序对结果的影响(Influence of input order of atomic indices on the result)** 输入原子序号的方向（例如 A,B,C,D 与 D,C,B,A）和排列（例如 A,B,C,D 与 B,D,C,A ……）都会影响所算 MCBO，下面对此详细说明。

- 输入方向(Input direction) 由于原始 MCBO（即用选项 2 计算的 MCBO）的数学形式，MCBO 结果可能依赖于输入方向。例如，输入 A,B,C,D 得到的结果可能与输入 D,C,B,A 不同。原因很清楚：对应于 A,B,C,D 的项为 (PS)ab(PS)bc(PS)cd(PS)da，而若把输入顺序反转，该项将变为 (PS)dc(PS)cb(PS)ba(PS)ad。虽然 P 和 S 都是对称矩阵，但其乘积 PS 不一定对称，因此两项并不等价。以我自己的观点，为得到更合理的结果，若环中原子连接顺序为 A-B-C-D-E-F（A 还与 F 相连），应分别计算 A,B,C,D,E,F 和 F,E,D,C,B,A 再取其平均。若想让 Multiwfn 直接打印平均值，你可将 `settings.ini` 中的 "iMCBOtype" 设为 1，这种情况下你无需手动计算两次，当然，计算代价是通常情形的两倍。

用选项 -2 在 NAO 基下计算 MCBO 以及用选项 -3 在 Löwdin 正交化基下计算 MCBO 的一个优点是结果与输入方向无关，这是因为在这些情形下不显含重叠矩阵 S，且密度矩阵 P 为对称矩阵。

- 序号排列(Index permutation) 在 MCBO 计算中对输入原子序号作排列可显著改变结果。例如，无论用哪种形式的 MCBO，输入 1,2,3,4,5,6 的结果可能与输入 2,4,3,5,6,1 很不相同。若你的目的是研究芳香性并刻画环上的循环电子离域，你应按顺时针或逆时针顺序输入原子序号，或如上所述取其平均。

有人主张需要考虑所有可能的排列以得到确定性结果，见 J. Phys. Org. Chem., 18, 706 (2005)；这意味着对由六个原子组成的区域，需把 (B,C,A,D,E,F)、(C,A,B,D,E,F)、(D,B,C,A,F,E) 等（共 6!=720 种）的键序都考虑在内。该定义在 Phys. Chem. Chem. Phys., 18, 11839 (2016) 中被称为多中心指数(MCI)。其明确定义如下，见 Phys. Chem. Chem. Phys., 18, 11839 (2016) 的 Eq. 9：

$$\mathrm{M C I}=\frac{1}{2n}\sum_{\hat{P}(A,B,C\ldots)}I_{A,B,C\ldots}$$

<!-- formula-ocr: formula_p145_085.png 已替换为LaTeX, 原图保留备查 -->

其中 n 为参与计算的原子数，𝑃̂ 为产生所有可能排列序列的置换算符。MCI 比 MCBO 昂贵得多，且不适合度量芳香性或循环离域。但它在度量类团簇区域中原子间的“整体”电子离域时可能有用。

若想让 Multiwfn 直接打印 MCI，你可将 `settings.ini` 中的 "iMCBOtype" 设为 2，然后像通常一样计算 MCBO（经由选项 2、-2 和 -3 中任一），所打印结果将对应于 MCI。

最后，值得注意的是，MCBO 在某些情形下可能略为负值。若你

<!-- p.146 -->


没有使用弥散函数，或 MCBO 是基于 NAO 计算的，那么你可简单地把非常小的负 MCBO 视为零。对三中心情形，若 MCBO 为明显的负值，则意味着存在三中心四电子(3c-4e)相互作用（例如 CO2）。

所需信息：基函数（选项 2、-3），带 DMNAO 关键词的 NBO 输出文件（选项 -2）

附录：Multiwfn 中极高效的 MCBO 实现(Appendix: The extremely efficient implementation of MCBO in Multiwfn) 按表达式看，MCBO 的计算代价似乎随环中原子数增加而指数增长，使其对大环的计算不可行。得益于我提出的 MCBO 特殊实现，Multiwfn 中 MCBO 的代价仅随环成员数线性增长，即使对由几十个原子组成的环，计算时间也可忽略！算法描述如下。

这里以五中心 MCBO 为例，其原始定义为

$$I_{A B C D E}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\sum_{d\in D}\sum_{e\in E}(P S)_{a b}(P S)_{b c}(P S)_{c d}(P S)_{d e}(P S)_{e a}$$

$$I_{A B C D E}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\sum_{d\in D}\sum_{e\in E}(P S)_{a b}(P S)_{b c}(P S)_{c d}(P S)_{d e}(P S)_{e a}$$

，则 MCBO 可简化为 ,() ()d adeeae EAPSPS ∈= 

$$I_{A B C D E}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\sum_{d\in D}\sum_{e\in E}(P S)_{a b}(P S)_{b c}(P S)_{c d}(P S)_{d e}(P S)_{e a}$$

，则 MCBO 可简化为 ,,()c acdd ad DBPSA ∈= 

$$I_{A B C D E}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}\sum_{d\in D}\sum_{e\in E}(P S)_{a b}(P S)_{b c}(P S)_{c d}(P S)_{d e}(P S)_{e a}$$

，则 MCBO 可最终简化为 ,,()b abcc ac CCPSB ∈= 

很清楚，利用中间矩阵 A、B、C，MCBO 可以相当简单的方式求值，而构造 A、B、C 也很廉价。该 ,()ABCDEabb aa A b BIPSC =  的形式代价

<!-- p.147 -->


重构后的 MCBO 仅随原子数线性增长，因而即使对由 100 多个原子组成的环也能轻松应用。

为证明 Multiwfn 中 MCBO 特殊实现的正确性和重要价值，下面给出在 ωB97XD/def2-TZVP 水平下计算 cyclo[n]carbon 体系 MCBO1/n 的结果与耗时比较。表中，“old” 表示基于 MCBO 原始方程的直接编程，用 Multiwfn 3.6（其中尚无当前算法）进行，“current” 表示上述算法。测试使用 Intel i9-13980HX CPU。可见两种算法给出完全相同的结果，但 “old” 算法对 cyclo[8]carbon 的代价已很高（即使使用像 6-31G* 这样的小基组，MCBO 通常至多用于含十几个原子的环）。相比之下，当前算法仅在 1 秒内即可精确算出 cyclo[48]carbon 的 MCBO！

n Wall time (s) MCBO1/n old current old current

6 <1s <1s 0.639945 0.639945 8 358s <1s 0.578652 0.578652 10 <1s 0.649397 12 <1s 0.611403 14 <1s 0.637272 24 <1s 0.561782 48 <1s 0.549418

### 3.11.3 在 Löwdin 正交化基下的 Wiberg 键序分析(Wiberg bond order analysis in Löwdin orthogonalized basis) (3)

Wiberg 键序定义如下，见 Tetrahedron, 24, 1083 (1968) 的脚注 2ABaba A b BIP = 

Wiberg 键序的原始定义只适用于用正交基函数表示的波函数，如大多数半经验波函数，且只对限制性闭壳层体系定义。实际上，Mayer 键序可视为 Wiberg 键序的推广，对限制性闭壳层体系和正交归一基函数（即 S 矩阵为单位矩阵）情形，两者结果完全相同。

在该功能中，Multiwfn 先用 Löwdin 方法正交化基函数，再进行通常的 Mayer 键序分析。打印阈值同样由 `settings.ini` 中的 “bndordthres” 控制。

如 J. Mol. Struct. (THEOCHEM), 870, 1 (2008) 所示，以这种方式计算的 Wiberg 键序，即 WL，对基组的敏感性远小于 Mayer 键序（而对小基组，两者结果彼此接近）。应注意，与 Mayer 键序相比，WL 倾向于高估极性键的键序。

通常，若无特殊理由，优先使用 Mayer 键序。注意，许多论文用 NBO 程序计算 Wiberg 键序，其结果

<!-- p.148 -->


必与本功能产生的结果有所不同，因为在 NBO 程序中 Wiberg 键序是在自然原子轨道(NAO)基下计算的，NAO 由 OWSO 正交化方法产生。Multiwfn 也可以在 NAO 基下计算 Wiberg 键序，而且，结果还可分解为原子轨道对贡献，详见第 3.11.8 节(Section 3.11.8)。

所需信息：基函数(Basis functions)

### 3.11.4 Mulliken 键序分析(Mulliken bond order analysis) (4)与分解(decomposition) (5)

Mulliken 键序是最早的键序定义，其定义为

$$I_{_{AB}}=\sum_{i}\eta_{i}\sum_{a\in A}\sum_{b\in B}2C_{a,i}C_{b,i}S_{a,b}=2\sum_{a\in A}\sum_{b\in B}P_{a,b}S_{a,b}$$

Mulliken 键序与经验键序的一致性较差，已不推荐用于定量成键强度，对此 Mayer 键序总是表现更好。但 Mulliken 键序是成键（正值）与反键（负值）的良好定性指标。打印结果的阈值由 `settings.ini` 中的 “bndordthres” 参数控制。

Mulliken 键序易于分解为轨道贡献，轨道 i 对键序 AB 的贡献为 ,,,2iABia ib ia ba A b BIC C Sη = 

从该分解，我们可知哪些轨道有利于或不利于特定成键。

所需信息：基函数(Basis functions)

### 3.11.5 轨道占据数微扰 Mayer 键序(Orbital occupancy-perturbed Mayer bond order) (6)

轨道占据数微扰 Mayer 键序最早提出于 J. Chem. Theory Comput., 8, 908 (2012)。简单地说，用该方法可得到特定轨道对 Mayer 键序的贡献有多大。

轨道占据数微扰 Mayer 键序可写为

$$I_{A,B}^{*}=I_{AB}^{*,\alpha}+I_{AB}^{*,\beta}=2\sum_{a\in A}\sum_{b\in B}[(\mathbf{P}_{X}^{\alpha}\mathbf{S})_{ba}(\mathbf{P}_{X}^{\alpha}\mathbf{S})_{ab}+(\mathbf{P}_{X}^{\beta}S)_{ba}(\mathbf{P}_{X}^{\beta}S)_{ab}]$$

该定义与第 3.11.1 节(Section 3.11.1)所示 Mayer 键序的唯一区别在于

𝛽分别。PX 代表将特定轨道占据数设为零时产生的密度矩阵。𝐼𝐴,𝐵 Pα 和 Pβ 已被 𝐏𝑋 𝛼 和 𝐏𝑋 ∗ 取代。𝐼𝐴,𝐵 ∗ 与 Mayer

键序之差可视为该轨道对 Mayer 键序贡献的度量。记住，因为 Mayer 键序不是密度矩阵的线性函数，所有

轨道的 𝐼𝐴,𝐵 ∗ 之和一般不等于 Mayer 键序。

∗对所有占据轨道以及 𝐼𝐴,𝐵 在 Multiwfn 中，你只需输入两个原子的序号，然后 𝐼𝐴,𝐵 ∗ 与 Mayer 键序将被输出。差值越负

<!-- p.149 -->


（正），轨道的存在对成键越有利（有害）。

你也可用另一种方式计算 𝐼𝐴,𝐵 ∗，即用波函数修饰模块

（主功能 6，Main function 6）手动把特定轨道的占据数设为零，再像通常一样计算 Mayer 键序，但若你想对许多

轨道计算 𝐼𝐴,𝐵 ∗，这种方式可能很繁琐。

这类分析在第 4.9.1 节(Section 4.9.1)和第 4.19.3 节(Section 4.19.3)中有示例说明。所需信息：基函数(Basis functions)

### 3.11.6 模糊键序(Fuzzy bond order) (7)

模糊键序(FBO)最早由 Mayer 在 Chem. Phys. Lett., 383, 368 (2004) 中提出：

$$S_{\mu\nu}^{A}=\int w_{A}(\mathbf{r})\chi_{\mu}^{*}(\mathbf{r})\chi_{\nu}(\mathbf{r})\mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p149_086.png 已替换为LaTeX, 原图保留备查 -->

其中 S 为模糊原子空间中基函数间的重叠矩阵。在 Multiwfn 中，用 sharpness 参数 k=3 的 Becke 模糊原子空间结合改良 CSD 半径计算 FBO。（模糊原子空间介绍见第 3.18.0 节，Section 3.18.0）。

通常 FBO 的大小接近 Mayer 键序，尤其对低极性键，但对基组变化稳定得多。根据 J. Phys. Chem. A, 109, 9904 (2005) 中 FBO 与离域指数(DI)的比较，FBO 本质上是在模糊原子空间中计算的 DI。关于 DI 的细节见第 3.18.5 节(Section 3.18.5)。

FBO 计算需要做 Becke DFT 数值积分，因此计算代价大于 Mayer 键序求值。默认使用 40 个径向点和 230 个角向点做数值积分。该设置一般已能给出足够准确的结果。若你想进一步提高结果精度，可手动设置 `settings.ini` 中的 "radpot" 和 "sphpot" 以设定径向和角向点数，并确保 "iautointgrid" 已设为 0。

打印结果的阈值由 `settings.ini` 中的 “bndordthres” 参数控制。所需信息：GTF、原子坐标(Atom coordinates)

### 3.11.7 拉普拉斯键序(Laplacian bond order) (8)

在 J. Phys. Chem. A, 117, 3100 (2013) (http://pubs.acs.org/doi/abs/10.1021/jp4010345) 中，我提出了一种基于模糊重叠空间中电子密度拉普拉斯 ∇2𝜌 的新型共价键序定义，称为拉普拉斯键序(LBO)。原子 A 与 B 之间的 LBO 可简单写为

$$L_{A,B}=-10\times\int\limits_{\nabla^{2}\rho<0}w_{A}(\mathbf{r})w_{B}(\mathbf{r})\nabla^{2}\rho(\mathbf{r})\mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p149_087.png 已替换为LaTeX, 原图保留备查 -->

<!-- p.150 -->


其中 w 为 Becke 提出的平滑变化权重函数，代表模糊原子空间，因此 wAwB 对应于 A 与 B 之间的模糊重叠空间。注意积分仅限于 ∇2𝜌 的负值部分。LBO 的物理基础是，模糊重叠空间中负 ∇2𝜌 积分的量级越大，电子密度在成键区域集中得越强，因此共价成键越强。

在 LBO 原始文献中，通过将其应用于多种分子并与许多现有键序定义比较，论证了 LBO 的合理性和有用性。结果表明 LBO 与键极性、键解离能和键振动频率直接相关。LBO 计算代价低，且对生成电子密度所用的计算水平不敏感。此外，由于 LBO 本质上不依赖于波函数，原则上可用源自 X 射线衍射数据的精确电子密度得到 LBO。

在 Multiwfn 中，用 sharpness 参数 k=3 的 Becke 模糊原子空间结合改良 CSD 半径计算 LBO。（模糊原子空间细节见第 3.18.0 节，Section 3.18.0）。打印结果的阈值由 `settings.ini` 中的 “bndordthres” 参数控制。

注意在当前实现中，LBO 特别适合有机体系，但不适合离子键，因为在这些情形下应使用能更忠实反映实际原子空间的原子空间定义，才能忠实呈现实际原子空间。LBO 也不太适合研究两个很重原子（重于 Ar）之间的键，因为这些键常伴随模糊重叠空间中不显著的电荷集中，即使成键无疑是共价的。

LBO 的一个很好的应用例子是 Carbon, 165, 468 (2020)，其中 LBO 被用来刻画 cyclo[18]carbon 中两种不同 C-C 键之间的成键。

所需信息：GTF、原子坐标(Atom coordinates)

### 3.11.8 将 NAO 基下的 Wiberg 键序分解为原子轨道(Decompose Wiberg bond order in NAO basis as atomic orbital)

### 对贡献(pair contributions) (9)

理论(Theory) 如第 3.11.3 节(Section 3.11.3)所述，Wiberg 键序表示为

$$I_{_{AB}}=\sum_{a\in A}\sum_{b\in B}P_{ab}^{2}$$

<!-- formula-ocr: formula_p150_088.png 已替换为LaTeX, 原图保留备查 -->

数据按原子对计算。由于表达式只是密度矩阵元平方的简单线性组合，把 Wiberg 键序分解为基函数对贡献很直接（该思想待发表）。例如，Pab2 就是基函数 a 与 b 间相互作用的贡献。由于使用扩展基组时基函数与原子轨道缺乏一一对应，为使分解方法富有物理意义，最好在自然原子轨道(NAO)下进行分解。每个非 Rydberg 型 NAO 唯一对应一个原子轨道，因此，用上述分解方法可得到原子轨道尺度的 Wiberg 键序。

此外，还可得到原子轨道壳层 i 与 j 间相互作用的贡献

<!-- p.151 -->


$$I_{ABC}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}P_{ab}P_{bc}P_{ca}$$

顺便说一下，把多中心键序分解为原子轨道贡献也是可能的。例如，三中心键序表示为

$$I_{_{ABC}}=\sum_{a\in A}\sum_{b\in B}\sum_{c\in C}P_{ab}P_{bc}P_{ca}$$

<!-- formula-ocr: formula_p151_089.png 已替换为LaTeX, 原图保留备查 -->

显然，PabPbcPca 可视为 NAO a、b 与 c 间相互作用的贡献。但 NAO 基下多中心键序的分解尚未实现。

用法(Usage) 进入该功能后，只需输入两个原子的序号，来自 NAO 对和 NAO 壳层对的不可忽略贡献将与总 Wiberg 键一起打印。

你也可输入 -1 以输入原子序号定义两个片段，然后给出两个片段间 NAO 壳层对片段间 Wiberg 键序的贡献。

该功能的输入文件与第 3.11.2 节(Section 3.11.2)所述选项 -2 完全相同，即包含密度矩阵信息的 NBO 程序输出文件（即需要 "DMNAO" 关键词）。

该分解分析的示例见第 4.9.4 节(Section 4.9.4)。

### 3.11.9 本征键强度指数(Intrinsic bond strength index (IBSI)) (10)

理论(Theory) 本征键强度指数(IBSI)提出于 J. Phys. Chem. A, 124, 1850 (2020)，用于定量化化学键强度，也可用于比较弱相互作用强度。IBSI 最初在独立梯度模型(IGM)框架下定义，IGM 在第 3.23.5 节(Section 3.23.5)中有非常详细的描述。IBSI 表示为

$$\mathrm{IBSI}=\frac{(1/d^{2})\int\delta g^{\mathrm{pair}}\mathrm{d}\mathbf{r}}{(1/d^{2}_{H_{2}})\int\delta g^{\mathrm{H}_{2}}\mathrm{d}\mathbf{r}}$$

<!-- formula-ocr: formula_p151_090.png 已替换为LaTeX, 原图保留备查 -->

其中 d 为待研究相互作用的两个原子间距离。分子中的积分等价于我定义的两个原子间的原子对 δg 指数，详见第 3.23.6 节(Section 3.23.6)。分母为参考体系的数据，𝑑H2 和

积分分别为平衡结构下 H2 的键长和原子对 δg 指数。在 IBSI 原始文献中，结果表明 IBSI 值与共价键强度呈适度正相关。此外，发现过渡金属配位键的 IBSI 量级明显小于共价键，而弱相互作用的 IBSI 量级更低，IBSI 的这一特征可用于区分相互作用类型。

实现(Implementation) 重要的是注意，在 IBSI 文献中作者用基于梯度划分的 IGM（IGMGBP）计算 IBSI，但 Multiwfn 不支持这种形式的 IGM。目前 Multiwfn 支持原始形式的 IGM，即基于 promolecular 近似的 IGM（IGMpro），也支持基于分子密度 Hirshfeld 划分的 IGM

<!-- p.152 -->


（IGMH），以及 mIGM。不同形式的 IGM 对应于不同的原子密度梯度求值方式，因此 IBSI 表达式中积分的值也相应不同。在 Multiwfn 中，IBSI 可基于 IGMpro、IGMH 和 mIGM 计算，其结果很不相同，我发现基于 IGMpro 的结果明显更接近 IBSI 原始文献。

用法(Usage) 要计算 IBSI，只需进入主功能 9(Main function 9)并选择子功能 10(subfunction 10)，再选选项 0 开始计算。

计算前，Multiwfn 会要求你选择积分格点质量，显然格点越好，代价越高，而结果越准确。根据我的经验，对 IGMpro，“中等质量(medium quality)”已能给出定量准确的结果；而对 IGMH 和 mIGM，若你对精度有要求，至少应使用“高质量(high-quality)”。

你可用选项 2 选择 IBSI 计算中用哪种形式的 IGM。若输入文件含波函数信息，默认用 IGMH，而若输入文件只含几何信息（例如 .pdb、.mol、.xyz……），可用 IGMpro 或 mIGM。注意 IGMH 比 IGMpro 昂贵得多，因为其求原子密度梯度的公式复杂得多。

若你只关心局域区域的相互作用，你可用选项 3 定义待研究区域，只有定义片段中原子间的 IBSI 会被求值并输出，代价也相应低于对整个体系的 IBSI 计算，尤其当体系巨大时。

参考值可用选项 4 设置，它对应于 IBSI 公式的分母。当然，该值对 IGMpro、IGMH 和 mIGM 必不同。默认参考值是对具实验键长（0.74144 Å）的 H2 算得的，在 IGMH 情形用 B3LYP/6-311G** 波函数。通常，参考值无需更改。但对用 IGMH 计算 IBSI，若你想用当前计算水平下的参考值以追求更严格的结果，你可载入 H2 的波函数文件，再进入本功能，把参考值设为 1.0，然后用选项 0 开始计算 IBSI，结果可用作研究实际分子的参考值。

为避免过多输出，默认只打印间距小于 3.5 Å 的原子对数据，因为间距更大时 IBSI 应可忽略。若需调节距离打印阈值，用选项 5。

计算 IBSI 的例子见第 4.9.6 节(Section 4.9.6)。所需信息：原子坐标（对基于 IGMpro 和 mIGM 的 IBSI），GTF 信息（对基于 IGMH 的 IBSI）

### 3.11.10 AV1245 指数（大环近似多中心键序）(AV1245 index (approximate multi-center bond order for large)

### 环(rings))与 AVmin(and AVmin)

理论(Theory) 如第 3.11.2 节(Section 3.11.2)介绍的多中心键序(MCBO)是非常严格且

<!-- p.153 -->


流行的芳香性刻画方式。在 Phys. Chem. Chem. Phys., 18, 11839 (2016) 中，作者提出 AV1245 指数以定量化大环芳香性，它可视为 MCBO 的近似。

AV1245 相对 MCBO 最初的关键优势在于 AV1245 的计算代价仅随原子数线性增长，而 MCBO 的代价对由超过 11~12 个原子组成的环通常高得难以承受。但自 Multiwfn 3.8 起，MCBO 的计算时间也与环成员数成线性正比，因而 MCBO 可轻松用于非常大的环，AV1245 的价值已远不如前。

AV1245 在原始文献中的定义是“沿环取保持 1、2、4、5 位置关系的所有 4c-ESI 值的平均”。这里我澄清其定义。例如，对下面的环，

其 AV1245 计算为

AV1245=[ESI(1,2,4,5)+ESI(2,3,5,6)+ESI(3,4,6,1)+ESI(4,5,1,2)+ESI(5,6,2,3)+ESI(6,1,3,4)] / 6

其中 nc-ESI（n 中心电子共享指数）可经由具所有可能排列的多中心键序（即 I perm，细节见第 3.11.2 节，Section 3.11.2）由下式直接得到

perm2ESI In= (1)! −

其中 n 为原子数。显然，4c-ESI = (4c-Iperm) / 3。

AV1245 的核心思想基于如下事实：在芳香环中，1-2 键与 4-5 键之间的共振很强，如下图所示。该特征可由 ESI(1,2,4,5) 捕捉。

环路径的 AV1245 值越大，意味着离域越强，因而环的芳香性越大。由于 AV1245 量级小，呈现数据时常乘以 1000。

值得注意的是，在 AV1245 原始文献中，MCBO 是用 AIM 划分下的原子重叠矩阵计算的，这种计算方式不仅昂贵而且复杂。在 Multiwfn 中，AV1245 所涉及的 MCBO 用通常方式计算，即基于密度矩阵和重叠矩阵。由于此时 4 中心 I perm 的计算相当廉价，即使对大体系和大环 AV1245 也可快速得到。但由于 MCBO 计算的差异，Multiwfn 产生的 AV1245 结果小于原始文献。此外，用 Multiwfn 直接计算 AV1245 时（换言之，在原始基函数下计算 AV1245），所用基组不应含弥散函数，否则 AV1245 将无意义。

Multiwfn 也支持在自然原子轨道(NAO)基下计算 AV1245，此时即使存在弥散函数也能得到合理结果。若无弥散

<!-- p.154 -->


函数，在原始基函数下算得的结果与在 NAO 基下算得的结果几乎相同。

AVmin 指数提出于 J. Phys. Chem. C, 121, 27118 (2017)，并在 Phys. Chem. Chem. Phys., 20, 2787 (2018) 中进一步讨论。它对应于 AV1245 计算中所涉及的所有 4c-ESI 中绝对值的最小值。与 AV1245 不同，AVmin 定量化整条路径中最低的共轭程度，因此在区分不同离域路径的芳香性时有独特价值，因为按通常直觉，路径的芳香性应由最阻断整条路径离域的局域区域主导。换言之，AVmin 能确定给定路径芳香性的瓶颈。

用法(Usage)

- 在原始基函数下计算 AV1245 与 AVmin(Calculating AV1245 and AVmin in original basis functions) 你应进入主功能 200(Main function 200)的子功能 19(subfunction 19)，再按连接顺序（沿环顺时针或逆时针）输入环中原子的序号。之后，AV1245 连同其组成 4c-ESI 值以及 AVmin 将被输出

Multiwfn 为大环输入原子序号提供了便利。若你先输入 d 再按 ENTER 键，然后你能以任意顺序输入原子序号，因为此时实际顺序将按原子间连接关系自动推测。但当环中任一原子与环中两个以上其他原子相连时，该输入模式不可用。

- 在 NAO 基下计算 AV1245 与 AVmin(Calculating AV1245 and AVmin in NAO basis) 操作过程与“在原始基函数下计算 AV1245 与 AVmin”相同，但你应用独立 NBO 程序或量子化学程序内嵌 NBO 模块的输出文件作为 Multiwfn 的输入文件，同时 NBO 分析中必须用 "DMNAO" 关键词。注意此时上述 "d" 模式的序号输入不可用。

用 AV1245 和 AVmin 研究小环和大环芳香性的例子见第 4.9.11 节(Section 4.9.11)。

所需信息：原子坐标(Atom coordinates)、基函数(Basis functions)

### 3.11.12 AIM 盆间离域指数(Delocalization index (DI) between AIM basins)

离域指数(DI)的概念见第 3.18.5 节(Section 3.18.5)。在原子-分子中(AIM)盆间，即对电子密度划分的盆间计算的 DI，是不同原子间共享电子对数的定量，也可视为键序的度量。但这类 DI 对键极性越高的键倾向于越低。由于该原因，对非极性键，DI 通常与 Mayer 键序和模糊键序非常接近，而对极性键，差异可能相当大。

盆分析模块可计算 DI，如第 3.20 节(Section 3.20)所述。但获得原子间 DI 的最直接方式是直接用专用功能，即主功能 9(Main function 9)的子功能 12(subfunction 12)。你将被要求选择格点质量，质量越好，代价越高，而结果越准确。在该功能中用原子中心均匀积分格点计算 DI。
