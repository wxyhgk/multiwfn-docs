# **3.10 轨道成分分析 (8)**

注意，这里的"轨道"一词不限于分子轨道，例如，若输入文件带有自然键轨道 (NBO)，则被分析的是 NBO。有一篇很好的论文比较了各种轨道成分分析方法，见 *Acta Chim. Sinica*, **69**, 2393 (2011)（中文，<http://sioc-journal.cn/Jwk_hxxb/CN/abstract/abstract340458.shtml>）。

无论你选择哪种轨道成分分析方法，若要求 Multiwfn 打印某轨道中各原子的成分，在输出中你会发现一个值"轨道离域指数" (ODI)。该值越低，轨道离域越强。当你要定量比较各轨道空间离域程度时，会发现该指数很有用。该 ODI 在[4.8.5节](sec-4-8-molecular-orbital-composition-analysis.md#485-通过轨道离域指数odi定量轨道的空间离域程度)有详细描述和示例。

## **3.10.1 用 Mulliken、Stout-Politzer 和 SCPA 方法输出特定轨道中的基函数、壳层和原子成分 (1, 2, 3)**

Mulliken、SCPA 和 Stout-Politzer 方法支持将轨道分解为基函数、壳层和原子成分。实际上，我已在[3.9.5节](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#395-ros--schuit-定义的修正-mulliken-原子布居-scpa-7)、[3.9.6节](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#396-stout--politzer-定义的修正-mulliken-原子布居-8)和[3.9.7节](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#397-bickelhaupt-定义的修正-mulliken-原子布居-9)介绍过相关理论，$\Theta_{i,a}$×100% 就是基函数 *a* 在轨道 *i* 中的成分，若将一个壳层内所有基函数的成分加起来就得到壳层成分，若将归属于同一原子的所有壳层的成分加起来就得到原子成分。

这些方法依赖于基组展开，在当前 Multiwfn 版本中你必须用 .mwfn、.fch、.molden 或 .gms 作为输入文件。

当你从主菜单进入"轨道成分分析"子菜单后，选择要用哪种方法做分解，然后输入轨道序号，结果会立即打印在屏幕上，你也可以输入 *-1* 打印所有轨道的基本信息以找到你感兴趣的那个。默认只打印成分大于 0.5% 的项，该阈值可通过 *settings.ini* 中的 "compthres" 调整。

若 .mwfn/.fch/.molden 文件中存储的基函数是球谐函数型，打印的基函数标号形如 D+1、F-3 而非 XX、XYY。Multiwfn 用的球谐基函数标号与 Gaussian 程序完全相同，转换关系为：

$\mathrm{D\ 0}=-0.5\cdot XX-0.5\cdot YY+ZZ$ 注：对应于 d $z^{2}$

$\mathrm{D+1}=XZ$

$\mathrm{D-1}=YZ$

$\mathrm{D+2}=\sqrt{3}/2\cdot (XX-YY)$ 注：对应于 d( $x^{2}$ - $y^{2}$ )

$\mathrm{D-2}=XY$

$\mathrm{F\ 0}=-3/2/\sqrt{5}\cdot (XXZ+YYZ)+ZZZ$

$\mathrm{F+1}=-\sqrt{3/8}\cdot XXX-\sqrt{3/40}\cdot XYY+\sqrt{6/5}\cdot XZZ$

$\mathrm{F-1}=-\sqrt{3/40}\cdot XXY-\sqrt{3/8}\cdot YYY+\sqrt{6/5}\cdot YZZ$

$\mathrm{F+2}=\sqrt{3}/2\cdot (XXZ-YYZ)$

$\mathrm{F-2}=XYZ$

$\mathrm{F+3}=\sqrt{5/8}\cdot XXX-3/\sqrt{8}\cdot XYY$

$\mathrm{F-3}=3/\sqrt{8}\cdot XXY-\sqrt{5/8}\cdot YYY$

$\mathrm{G\ 0}=ZZZZ+3/8\cdot (XXXX+YYYY)-3\cdot \sqrt{3/35}\cdot (XXZZ+YYZZ-1/4\cdot XXYY)$

$\mathrm{G+1}=2\cdot \sqrt{5/14}\cdot XZZZ-3/2\cdot \sqrt{5/14}\cdot XXXZ-3/2/\sqrt{14}\cdot XYYZ$

$\mathrm{G-1}=2\cdot \sqrt{5/14}\cdot YZZZ-3/2\cdot \sqrt{5/14}\cdot YYYZ-3/2/\sqrt{14}\cdot XXYZ$

$\mathrm{G+2}=3\cdot \sqrt{3/28}\cdot (XXZZ-YYZZ)-\sqrt{5}/4\cdot (XXXX-YYYY)$

$\mathrm{G-2}=3/\sqrt{7}\cdot XYZZ-\sqrt{5/28}\cdot (XXXY+XYYY)$

$\mathrm{G+3}=\sqrt{5/8}\cdot XXXZ-3/\sqrt{8}\cdot XYYZ$

$\mathrm{G-3}=-\sqrt{5/8}\cdot YYYZ+3/\sqrt{8}\cdot XXYZ$

$\mathrm{G+4}=\sqrt{35}/8\cdot (XXXX+YYYY)-3/4\cdot \sqrt{3}\cdot XXYY$

$\mathrm{G-4}=\sqrt{5}/2\cdot (XXXY-XYYY)$

$\mathrm{H\ 0}=ZZZZZ-5/\sqrt{21}\cdot (XXZZZ+YYZZZ)+5/8\cdot (XXXXZ+YYYYZ)+\sqrt{15/7}/4\cdot XXYYZ$

$\mathrm{H+1}=\sqrt{5/3}\cdot XZZZZ-3\cdot \sqrt{5/28}\cdot XXXZZ-3/\sqrt{28}\cdot XYYZZ+\sqrt{15}/8\cdot XXXXX+\sqrt{5/3}/8\cdot XYYYY+\sqrt{5/7}/4\cdot XXXYY$

$\mathrm{H-1}=\sqrt{5/3}\cdot YZZZZ-3\cdot \sqrt{5/28}\cdot YYYZZ-3/\sqrt{28}\cdot XXYZZ+\sqrt{15}/8\cdot YYYYY+\sqrt{5/3}/8\cdot XXXXY+\sqrt{5/7}/4\cdot XXYYY$

$\mathrm{H+2}=\sqrt{5}/2\cdot (XXZZZ-YYZZZ)-\sqrt{35/3}/4\cdot (XXXXZ-YYYYZ)$

$\mathrm{H-2}=\sqrt{5/3}\cdot XYZZZ-\sqrt{5/12}\cdot (XXXYZ+XYYYZ)$

$\mathrm{H+3}=\sqrt{5/6}\cdot XXXZZ-\sqrt{3/2}\cdot XYYZZ-\sqrt{35/2}/8\cdot (XXXXX-XYYYY)+\sqrt{5/6}/4\cdot XXXYY$

$\mathrm{H-3}=-\sqrt{5/6}\cdot YYYZZ+\sqrt{3/2}\cdot XXYZZ-\sqrt{35/2}/8\cdot (XXXXY-YYYYY)-\sqrt{5/6}/4\cdot XXYYY$

$\mathrm{H+4}=\sqrt{35}/8\cdot (XXXXZ+YYYYZ)-3/4\cdot \sqrt{3}\cdot XXYYZ$

$\mathrm{H-4}=\sqrt{5}/2\cdot (XXXYZ-XYYYZ)$

$\mathrm{H+5}=3/8\cdot \sqrt{7/2}\cdot XXXXX+5/8\cdot \sqrt{7/2}\cdot XYYYY-5/4\cdot \sqrt{3/2}\cdot XXXYY$

$\mathrm{H-5}=3/8\cdot \sqrt{7/2}\cdot YYYYY+5/8\cdot \sqrt{7/2}\cdot XXXXY-5/4\cdot \sqrt{3/2}\cdot XXYYY$

例子见[4.8.1节](sec-4-8-molecular-orbital-composition-analysis.md#481-用mulliken方法分析乙酰胺)。

> **所需信息**
>
> 基函数

## **3.10.2 定义片段 1 和 2 (-1, -2)**

在用 Mulliken、Stout-Politzer 和 SCPA 方法做片段成分分析之前，必须先定义片段。若你感兴趣的只是一个片段的成分而非两个片段之间的成分（交叉项成分），只需定义片段 1。片段的内容可选为基函数、壳层、原子或其混合，无论选什么，最终记录的只是相应基函数的序号。

定义片段界面中所有支持的命令都是自明的，我不再赘述，只举一个例子，即把片段定义为原子 3 的所有 P 壳层：首先输入命令 *all*，列出所有基函数的信息，找出归属于中心 3 且包含 X、Y、Z 型基函数（即 PX、PY、PZ）的壳层。假设这类壳层的序号为 3、6、7，则输入 *s 3,6,7* 将其加入片段。若要验证操作，再输入 *all* 并检查相应行最左侧是否出现星号，被标记的基函数即已被纳入片段。最后输入字母 *q* 保存当前片段并返回上一级……

默认片段没有任何内容。每次进入片段定义界面时，片段状态与上次离开界面时相同。因此，若你之前已定义过片段而想彻底重定义，别忘了先用 "clean" 命令清空片段。

## **3.10.3 用 Mulliken、Stout-Politzer 和 SCPA 方法输出片段 1 的成分和片段间成分 (4, 5, 6)**

定义片段 1 后，基于 Mulliken、Stout-Politzer 和 SCPA 方法的片段成分分析即可用。片段成分是片段内所有基函数成分之和，在该功能中所有轨道的片段成分会同时打印在屏幕上。若你选的分析方法是 Mulliken（子功能 4）或 Stout-Politzer（子功能 5），以下分量项会与总成分一起输出：

**c^2 项：** 片段 1 内基函数系数的平方和，即 $\sum_{a\in\mathrm{frag1}} C_{a,i}^2\times 100\%$ 。

**内交叉项 (Int.cross)：** 片段 1 内的内部交叉项之和，即 $\sum_{a\in\mathrm{frag1}}\sum_{b\in\mathrm{frag2}} C_{a,i}C_{b,i}S_{a,b}\times 100\%$ 。

**外交叉项 (Ext.cross)：** 片段 1 与所有其它原子之间总交叉项中归属于片段 1 的部分，即 $\sum_{a\in\mathrm{frag1}}\sum_{b\notin\mathrm{frag1}} w_{a,b}2C_{a,i}C_{b,i}S_{a,b}\times 100\%$ 。

显然，片段 1 的总成分等于 c^2 项 + 内交叉项 + 外交叉项。

若还定义了片段 2（你*必须*已定义过片段 1），在子功能 5 (Mulliken) 或子功能 5 (Stout-Politzer) 中还会输出每个轨道中片段 1 与片段 2 之间的交叉项，即 $\sum_{a\in\mathrm{frag1}}\sum_{b\in\mathrm{frag2}} 2C_{a,i}C_{b,i}S_{a,b}\times 100\%$。"Frag1 部分"和 "Frag2 部分"对应交叉项中分别归属于片段 1 和片段 2 的分量，对 Mulliken 分析两者当然因"均分"而完全相等。

## **3.10.4 用自然原子轨道方法做轨道成分分析 (7)**

该功能用于基于自然原子轨道 (NAO) 计算轨道成分。该思想在我发表于 *Acta Chim. Sinica*, **69**, 2393 (2011) <http://sioc-journal.cn/Jwk_hxxb/CN/abstract/abstract340458.shtml> 的论文中提出。

### **理论**

著名的自然键轨道 (NBO) 分析的第一步是基于密度矩阵将原始基函数转换为 NAO。所得 NAO 可分为三类：

- 芯型 NAO，描述内层电子密度，其占据数几乎等于整数

- 价型 NAO，描述价层电子密度，一般具有高占据数

- Rydberg 型 NAO，主要体现电子的极化和离域特征，其占据数很低

芯和价 NAO 统称为最小集，它们有很强的物理意义并与"实际"原子轨道一一对应，是我们最应关注的。占据 MO 几乎完全由最小集 NAO 贡献。Rydberg NAO 没有明确的物理解释，在占据 MO 中其贡献可忽略，但它们对虚轨道常有很大贡献。

由于 NAO 是正交归一集，若有 NAO 基下的 MO 系数矩阵，只需将相应展开系数平方再乘以 100% 即得某 NAO 对特定 MO 的贡献。某原子的成分可算作该中心最小集 NAO 成分之和。

这种基于 NAO 的轨道成分计算方法有很好的基组稳定性，如 Hirshfeld 方法，特别适合分析占据轨道的成分。但对虚轨道，由于 Rydberg NAO 的贡献常很大，该方法不再很好用。

### **输入文件**

NAO 基下的 MO 系数矩阵不能由 Multiwfn 自身产生，你需要提供含该矩阵的 NBO 程序输出文件作为 Multiwfn 输入文件。默认 NBO 程序不输出该矩阵，需在 NBO 输入文件的 \$NBO ... \$END 字段间手动添加 *NAOMO* 关键词。这里的 NBO 程序可以是独立 NBO 程序（又称 GENNBO），也可以是量子化学软件内嵌的 NBO 模块，如 Gaussian 的 L607。

### **选项**

载入合适的输入文件并进入本功能后，你会在界面中发现以下选项：

**-1 定义片段**：该选项用于定义片段，片段贡献分析（选项 1）需要它。所有命令都是自明的。

**0 显示某轨道的成分**：打印 NAO、壳层和原子对特定 MO 的贡献。同时分别报告芯、价和 Rydberg 型 NAO 的贡献。

**1 显示片段对一批轨道的贡献**：打印由选项 -1 定义的片段对特定轨道的贡献。

**2 选择输出模式**：该选项控制选项 0 打印哪些项，有四种模式：

- (0) 显示所有项

- (1) 显示非 Rydberg 项

- (2) 显示贡献大于特定标准的项

- (3) 显示贡献大于特定标准的非 Rydberg 项（默认）

**3 切换自旋类型**：若当前体系是开壳层可见该选项。可选择要分析的 MO 的自旋。

例子见[4.8.2节](sec-4-8-molecular-orbital-composition-analysis.md#482-用自然原子轨道方法分析水)。

> **所需信息**
>
> NAO 基下的 MO 系数

## **3.10.5 用 Hirshfeld 或 Hirshfeld-I 方法计算原子和片段贡献 (8,10)**

Hirshfeld 和 Hirshfeld-I 权重函数（分别见[3.9.1节](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#391-hirshfeld-原子电荷-1)和[3.9.13节](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3913-hirshfeld-i-原子电荷-15)）也可用于将轨道分解为原子和片段成分，原子 *A* 在轨道 *i* 中的成分为 $\int\varphi_i^2(\mathbf{r})w_A(\mathbf{r})\mathrm{d}\mathbf{r}\times 100\%$ 。片段的成分就是属于该片段的原子的成分之和。这些方法有很好的基组稳定性，总是比 Mulliken 和 MMPA 更可靠合理。实际上，Hirshfeld 划分已经足够好，更复杂且计算量大的 Hirshfeld-I 划分并无必要。

若选择用 Hirshfeld 划分，程序会提示选择生成构建 Hirshfeld 权重函数的原子密度的方式，强烈建议用内建原子密度而非原子 .wfn 文件，因为前者方便得多。若选择用 Hirshfeld-I 划分，会先做常规 HI 迭代以得到收敛的原子权重函数（若对操作困惑，请参考[4.7.4节](sec-4-7-population-analysis-and-atomic-charge-calculation.md#474-hirshfeld-i原子电荷计算示例)计算 HI 电荷的例子和[3.9.13节](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3913-hirshfeld-i-原子电荷-15)介绍的 Hirshfeld-I 实现细节）。

计算轨道成分前会自动进行数据初始化。完成后可输入感兴趣的轨道序号。因数值积分总会引入一些误差，所有原子成分之和不严格等于 100%，极少数情况下偏差可能较显著，故 Multiwfn 会自动归一化并在 "After normalization" 标题下打印结果。

若想同时查看某原子在特定范围轨道中的成分，选择选项 -2，再输入原子序号和轨道序号范围。

若想研究片段对轨道的贡献，先用 -9 定义片段，再输入轨道序号时片段的贡献会与所有原子的贡献一起输出。也可选择 -3 计算所定义片段对一段轨道的贡献。

若选选项 -4，程序会计算每个原子在每个轨道中的成分并全部导出到当前文件夹的 *orbcomp.txt*。

例子见[4.8.3节](sec-4-8-molecular-orbital-composition-analysis.md#483-用hirshfeld和becke方法分析乙酰胺)。

> **所需信息**
>
> 原子坐标和 GTF

## **3.10.6 用 Becke 方法计算原子和片段贡献 (9)**

该功能与[3.10.5节](#3105-用-hirshfeld-或-hirshfeld-i-方法计算原子和片段贡献-810)介绍的功能很相似，唯一区别是用 Becke 划分代替 Hirshfeld 划分。多数情况下两者结果定性一致。用 Becke 划分代替 Hirshfeld 划分有个突出优点，即不需要原子波函数文件，因为 Becke 原子空间可简单地基于原子半径构建。关于 Becke 划分的更多细节见[3.18.0节](sec-3-18-fuzzy-atomic-space-analysis.md#3180-基本概念)。例子见[4.8.3节](sec-4-8-molecular-orbital-composition-analysis.md#483-用hirshfeld和becke方法分析乙酰胺)。

> **所需信息**
>
> 原子坐标和 GTF

## **3.10.7 用 AIM 方法计算原子和片段贡献 (11)**

Multiwfn 也能基于分子空间的 atoms-in-molecules (AIM) 划分计算轨道成分。该划分方法中每个原子 basin 对应一个原子的空间，关于 basin 和 AIM 划分的概念细节见[第 3.20 节](sec-3-20-basin-analysis.md)。要在 AIM 划分下计算轨道成分，应使用 basin 分析模块（主功能 17）的子功能 11，例子见[4.8.6节](sec-4-8-molecular-orbital-composition-analysis.md#486-计算aim盆及其他类型盆贡献的轨道组成)。

通常，我不推荐用这种方式计算轨道成分，因为耗时远高于其它方式而结果并不更好。

> **所需信息**
>
> 原子坐标和 GTF

## **3.10.100 用 LOBA 和 mLOBA 方法评估氧化态 (100)**

该功能实现了发表于 *Phys. Chem. Chem. Phys.*, **11**, 11297 (2009) 的定域轨道键分析 (LOBA) 方法，以及我提出的 modified LOBA (mLOBA)（待发表）。

### **理论**

LOBA 是基于定域 MO (LMO) 的轨道成分评估原子氧化态的方法。思想很简单：若某原子核电荷为 *Z*，它在 *N* 个占据 LMO 中的成分大于给定阈值（例如 50%。此时这些 LMO 中的电子可近似视为完全归属于该原子。若某 LMO 双占据，应计两次），则该原子的氧化态为 *Z*−*N*。

LOBA 的思想也可推广以定义片段的氧化态，即若某片段内核电荷之和为 *Z*，片段对 *N* 个 LMO 的贡献大于某阈值，则片段氧化态为 *Z*−*N*。

mLOBA 采用不同的方式确定 LMO 电子的归属。该方法中，每个 LMO 的电子指派给对它贡献最大的原子。这不仅消除了阈值选择的任意性，还保证氧化态之和严格等于当前体系的净电荷。此外，mLOBA 中片段的氧化态就是其所有组成原子氧化态之和。强烈建议用 mLOBA 代替 LOBA！

mLOBA 唯一的缺点是当存在（局域）几何对称性时结果可能不平衡。例如乙烷中有一个对应 C-C 键的 LMO，两个碳原子对它贡献相等。在 mLOBA 中，LOBA 的两个电子可能被指派给其中任一个碳，最终一个碳氧化态为 -4 而另一个为 -2。规避该问题的最好办法是将两个碳定义为一个片段并求片段氧化态，结果为 -6，每个碳的氧化态应视为 -6/2 = -3，这完全合理。

LOBA/mLOBA 方法的结果在某种程度上依赖于轨道成分分析方法的选择。Multiwfn 对 LOBA/mLOBA 分析采用 Hirshfeld 方法，它比 LOBA 原论文用的 Mulliken 方法稳健得多。因此，尽管一些论文报道了 LOBA 的失效例子，其中多数在 Multiwfn 中并不失效！

### **用法**

要用该功能，应提供记录 LMO（或 NBO）的 .mwfn、.fch 或 .molden 文件。例如，可用 Multiwfn 做轨道定域化以产生含 LMO 的波函数文件。若你是 Gaussian 用户，可用 *pop=saveNBO* 或 *pop=saveNLMO* 任务所得 .fch 文件作为输入文件，基于 NBO 或 NLMO 做 LOBA 分析。当内存中有 LMO 后，进入主功能 8 的子功能 100，再输入一个阈值（例如 50）即得 LOBA 方法的氧化态；或者输入 *m* 即得 mLOBA 方法的氧化态。也可在 LOBA/mLOBA 界面输入 -1 定义片段，片段氧化态会与原子氧化态一起打印。

例子见[4.8.4节](sec-4-8-molecular-orbital-composition-analysis.md#484-用lobamloba方法计算氧化态)。
