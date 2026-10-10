# 轨道组成分析(Orbital composition analysis)(8)

> Multiwfn manual, p.134–140.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.134 -->


### 3.9.19 约束 MBIS(Constrained MBIS，cMBIS)、椭球 MBIS(elliptical MBIS，EMBIS)、

### 非对称椭球 MBIS(asymmetric elliptical MBIS，AEMBIS)(21、22、23)

约束 MBIS(constrained MBIS，cMBIS)、椭球 MBIS(elliptical MBIS，EMBIS)、非对称椭球 MBIS(asymmetric elliptical MBIS，AEMBIS)的代码分别对应主功能7(main function 7)中的子功能21、22 和 23(subfunctions 21, 22 and 23)。它们由 Frank Jensen 教授(frj@chem.au.dk)贡献，关于这些功能的任何细节请联系他。

cMBIS 描述于：J. E. S. Mikkelsen, F. Jensen "Minimal Basis Iterative Stockholder Decomposition with Multipole Constraints", J. Chem. Theory Comput., 21, 1179-1193 (2025)

EMBIS 描述于：A. M. H. Nielsen, F. Jensen "Minimal Basis Iterative Stockholder Decomposition with Ellipsoidal Atoms", J. Chem. Theory Comput., 21, 8753-8761 (2025)

AEMBIS 尚未发表，但相当于在 EMBIS 的 sqrt(Rt*alpha*R) 中加入 beta*R 项，并同时优化三个 beta 参数。这可视为在椭球 basin 上加入偶极-like 项，从而使椭球非中心对称。可能的引用为：B. L. Wessel, A. M. H. Nielsen, F. Jensen, (unpublished)。

cMBIS 和 EMBIS 代码具有使用多极约束的能力。带约束的 EMBIS 在原始文献中称为 cEMBIS。AEMBIS 中的约束代码只是 EMBIS 的直接复制，因此产生的是 EMBIS 结果。

除信息损失值外，还计算原子体积和键级矩阵。

在 cMBIS 代码中，有可能分别通过数值和双重数值计算 Vne 和 Vee 原子贡献。Vee 的积分在数值上(非常)耗时。Vee 仅为 Coulomb 相互作用，但它允许使用 MBIS 原子定义进行 IQA 分解为原子-原子能量相互作用，给出至少半定量的相互作用度量

还有一个在这些功能中沿方向绘制密度的选项。进入这些功能时，程序会要求你选择积分格点。1 (fine)和 2 (ultrafine)是获得非球形分解和高阶多极约 10-4 精度所必需的。

所需信息：GTFs、原子坐标

## 3.10 轨道组成分析(Orbital composition analysis)(8)

注意，这里的“轨道(orbital)”一词不限于分子轨道，例如，若输入文件带有自然键轨道(NBO)，则被分析的将是 NBO。有一篇优秀论文比较了各种轨道组成分析方法，见 Acta Chim. Sinica, 69, 2393 (2011)(中文，http://sioc-journal.cn/Jwk_hxxb/CN/abstract/abstract340458.shtml)。

无论你选择哪种轨道组成分析方法，如果你要求 Multiwfn 打印

<!-- p.135 -->


某轨道中各原子的组成，在输出中你可以找到一个值“轨道离域指数(Orbital delocalization index, ODI)”。该值越低，轨道离域越强。当你打算定量比较各轨道空间离域程度时，你会发现该指数非常有用。该 ODI 在第 4.8.5 节中有详细介绍和示例。

### 3.10.1 用 Mulliken、Stout-Politzer 和 SCPA 方法输出特定

### 轨道中的基函数、壳层和原子组成(1、2、3)

Mulliken、SCPA 和 Stout-Politzer 方法支持将轨道分解为基函数、壳层和原子组成。实际上，我已在第 3.9.5、3.9.6 和

### 3.9.7 节中介绍了理论，Θi,a×100% 就是基函数 a 在轨道 i 中的组成，若将一个壳层内所有基函数的组成加和即得到壳层组成，若将归属于同一原子的所有壳层的组成加和即得到原子组成。

这些方法依赖于基组展开，在当前 Multiwfn 版本中你必须使用 .mwfn、.fch、.molden 或 .gms 作为输入文件。

当你从主菜单进入“轨道组成分析(Orbital composition analysis)”子菜单后，选择你想用于分解的方法，然后输入轨道索引，结果将立即打印在屏幕上，你也可以输入 -1 打印所有轨道的基本信息以找到你感兴趣的那个。默认只打印组成大于 0.5% 的项，该阈值可通过 `settings.ini` 中的 “compthres” 调整。

若 .mwfn/.fch/.molden 文件中存储的基函数为球谐函数类型，则打印的基函数标号看起来像 D+1、F-3 而不是 XX、XYY。Multiwfn 中使用的球谐基函数标号与 Gaussian 程序完全相同，转换关系为：

```text
D 0=-0.5*XX-0.5*YY+ZZ  Note: This corresponds to dz2
D+1=XZ
D-1=YZ
D+2=√3/2*(XX-YY)  Note: This corresponds to d(x2-y2)
D-2=XY

F 0=-3/2/√5*(XXZ+YYZ)+ZZZ
```

F+1=-√(3/8)*XXX-√(3/40)*XYY+√(6/5)*XZZ

F-1=-√(3/40)*XXY-√(3/8)*YYY+√(6/5)*YZZ


```text
F+2=√3/2*(XXZ-YYZ)
F-2=XYZ
```

F+3=√(5/8)*XXX-3/√8*XYY

F-3=3/√8*XXY-√(5/8)*YYY


```text
G 0=ZZZZ+3/8*(XXXX+YYYY)-3*√(3/35)*(XXZZ+YYZZ-1/4*XXYY)
```

G+1=2*√(5/14)*XZZZ-3/2*√(5/14)*XXXZ-3/2/√14*XYYZ

G-1=2*√(5/14)*YZZZ-3/2*√(5/14)*YYYZ-3/2/√14*XXYZ

G+2=3*√(3/28)*(XXZZ-YYZZ)-√5/4*(XXXX-YYYY)

G-2=3/√7*XYZZ-√(5/28)*(XXXY+XYYY)

G+3=√(5/8)*XXXZ-3/√8*XYYZ

<!-- p.136 -->


G-3=-√(5/8)*YYYZ+3/√8*XXYZ

G+4=√35/8*(XXXX+YYYY)-3/4*√3*XXYY


```text
G-4=√5/2*(XXXY-XYYY)
```

H 0=ZZZZZ-5/√21*(XXZZZ+YYZZZ)+5/8*(XXXXZ+YYYYZ)+√(15/7)/4*XXYYZ

H+1=√(5/3)*XZZZZ-3*√(5/28)*XXXZZ-3/√28*XYYZZ+√15/8*XXXXX+√(5/3)/8*XYYYY+√


```text
(5/7)/4*XXXYY
```

H-1=√(5/3)*YZZZZ-3*√(5/28)*YYYZZ-3/√28*XXYZZ+√15/8*YYYYY+√(5/3)/8*XXXXY+√


```text
(5/7)/4*XXYYY
```

H+2=√5/2*(XXZZZ-YYZZZ)-√(35/3)/4*(XXXXZ-YYYYZ)

H-2=√(5/3)*XYZZZ-√(5/12)*(XXXYZ+XYYYZ)

H+3=√(5/6)*XXXZZ-√(3/2)*XYYZZ-√(35/2)/8*(XXXXX-XYYYY)+√(5/6)/4*XXXYY

H-3=-√(5/6)*YYYZZ+√(3/2)*XXYZZ-√(35/2)/8*(XXXXY-YYYYY)-√(5/6)/4*XXYYY

H+4=√35/8*(XXXXZ+YYYYZ)-3/4*√3*XXYYZ


```text
H-4=√5/2*(XXXYZ-XYYYZ)
```

H+5=3/8*√(7/2)*XXXXX+5/8*√(7/2)*XYYYY-5/4*√(3/2)*XXXYY

H-5=3/8*√(7/2)*YYYYY+5/8*√(7/2)*XXXXY-5/4*√(3/2)*XXYYY

例子见第 4.8.1 节。所需信息：基函数

### 3.10.2 定义片段 1 和 2(Define fragments 1 and 2)(-1、-2)

在用 Mulliken、Stout-Politzer 和 SCPA 方法进行片段组成分析之前，你必须预先定义片段。如果你感兴趣的只是一个片段的组成而不是两个片段之间的组成(交叉项组成)，你只需定义片段 1。片段的内容可选择为基函数、壳层、原子或它们的混合，无论你选择什么，最终只记录相应基函数的索引。注意，这里我所说的“片段(fragment)”与第 3.1 节中涉及的“片段(fragment)”没有关系，这里定义的片段完全不干扰波函数。

定义片段界面中所有支持的命令都是自解释的，因此我不再赘述，只举一个例子，即将片段定义为原子 3 的所有 P 壳层：首先，输入命令 all，列出所有基函数的信息，找出归属于中心 3 且包含 X、Y 和 Z 型基函数的壳层(即 PX、PY 和 PZ)。假设这类壳层的索引为 3、6 和 7，然后输入 s 3,6,7 将它们加入片段。若要验证你的操作，再次输入 all 并检查相应行最左侧是否出现星号，被标记的基函数即为已包含在片段中的基函数。最后，输入字母 q 保存当前片段并返回上一级菜单，同时会打印片段中基函数的索引。

默认情况下，片段没有任何内容。每次进入片段定义界面时，片段的状态与上次离开该界面时相同。所以，若你早先已定义过片段而你想完全重新定义，不要忘记先用“clean”

<!-- p.137 -->


命令将片段清空。

### 3.10.3 用 Mulliken、Stout-Politzer 和 SCPA 方法输出片段 1 的组成和

### 片段间组成(4、5、6)

在你定义片段 1 之后，基于 Mulliken、Stout-Politzer 和 SCPA 方法的片段组成分析即已可用。片段组成是片段内所有基函数组成之和，在此功能中所有轨道的片段组成同时打印在屏幕上。若你选择的方法是 Mulliken(子功能4(subfunction 4))或 Stout-Politzer(子功能5(subfunction 5))，以下分量项与总组成一起输出：

c^2 项：片段 1 内基函数系数的平方和，即

$$\sum_{a\in frag1} C_{a,i}^2 \times 100\%$$

<!-- formula-ocr: formula_p137_075.png 已替换为LaTeX, 原图保留备查 -->

Int.cross：片段 1 内的内部交叉项之和，即

$$\sum_{a\in frag1} \sum_{b\notin frag1} w_{a,b} 2C_{a,i} C_{b,i} S_{a,b} \times 100\%$$

Ext.cross：片段 1 与所有其他原子之间总交叉项的片段 1 部分，

$$\sum_{a\in frag1} \sum_{b\notin frag1} w_{a,b} 2C_{a,i} C_{b,i} S_{a,b} \times 100\%$$

显然，片段 1 的总组成等于 c^2 项 + Int.cross + Ext.cross。若还定义了片段 2(你必须已经定义过片段 1)，在子功能5(Mulliken)(subfunction 5 (Mulliken))或子功能5(Stout-Politzer)(subfunction 5 (Stout-Politzer))中每个轨道中片段 1 与片段 2 之间的交叉项，即 $\sum_{a\in\mathrm{frag1}}\sum_{b\in\mathrm{frag2}}2C_{a,i}C_{b,i}S_{a,b}\times100\%$ 也将被输出。“Frag1 part”与 C C S

“Frag2 part”分别对应归属于片段 1 和片段 2 的交叉项分量，对 Mulliken 分析而言，由于“等分”，两项当然完全相等。

### 3.10.4 用自然原子轨道方法进行轨道组成分析

### (7)

本功能用于基于自然原子轨道(NAOs)计算轨道组成。该思想在我发表于 Acta Chim. Sinica, 69, 2393 (2011) http://sioc-journal.cn/Jwk_hxxb/CN/abstract/abstract340458.shtml 的论文中提出。

理论 著名的自然键轨道(NBO)分析的第一步是基于密度矩阵将原始基函数转换为 NAOs。所得 NAOs 可分为三类：

- 芯型 NAOs，描述内层芯密度，其占据数几乎等于整数

- 价型 NAOs，描述价层密度，一般具有高占据数

<!-- p.138 -->


- Rydberg 型 NAOs，主要表现电子的极化和离域特征，它们的占据数非常低

芯和价 NAOs 统称为最小集，它们具有很强的物理意义，并与“实际”原子轨道一一对应，因此是我们最应关注的。占据 MO 几乎完全由最小集 NAOs 贡献。Rydberg NAOs 没有明确的物理解释，在占据 MOs 中的贡献可忽略，但它们对虚轨道往往有很大贡献。

由于 NAOs 是正交归一集，若我们在 NAO 基下有 MO 系数矩阵，就可以通过将相应的展开系数平方再乘以 100% 得到某 NAO 对特定 MO 的贡献。某原子的组成可计算为该中心最小集 NAOs 组成之和。

这种基于 NAOs 的轨道组成计算方法如 Hirshfeld 方法一样具有很好的基组稳定性，特别适合分析占据轨道的组成。然而，对虚轨道而言，由于 Rydberg NAOs 的贡献往往很大，该方法不再很好用。

输入文件 MO 在 NAO 基下的系数矩阵不能由 Multiwfn 自身生成，你需要提供包含该矩阵的 NBO 程序输出文件作为 Multiwfn 输入文件。默认情况下，NBO 程序不输出该矩阵，因此你需要在 NBO 输入文件的 \$NBO ... \$END 字段之间手动加入 NAOMO 关键词。这里所说的 NBO 程序可以是独立的 NBO 程序(也称为 GENNBO)，或量子化学软件中内嵌的 NBO 模块，如 Gaussian 中的 L607。

选项 在载入合适的输入文件并进入本功能后，你会在界面中发现以下选项：

-1 定义片段(Define fragment)：此选项用于定义片段，片段贡献分析(选项1(Option 1))需要用到它。所有命令都是自解释的。

0 显示某轨道的组成(Show composition of an orbital)：打印 NAOs、壳层和原子对特定 MO 的贡献。同时，分别报告芯、价和 Rydberg 型 NAOs 的贡献。

1 显示片段对一批轨道的贡献(Show fragment contribution to a batch of orbitals)：打印由选项-1(Option -1)定义的片段对特定轨道的贡献。

2 选择输出模式(Select output mode)：此选项控制选项0(Option 0)打印哪些项，有四种模式：

(0) 显示所有项(Show all terms) (1) 显示非 Rydberg 项(Show non-Rydberg terms) (2) 显示贡献大于特定标准的项(Show the terms whose contributions are larger than specific criterion) (3) 显示贡献大于特定标准的非 Rydberg 项(Show non-Rydberg terms whose contributions are larger than specific criterion)(默认) 3 切换自旋类型(Switch spin type)：若当前体系为开壳层，你会看到此选项。你可以选择要分析的 MOs 的自旋。

例子见第 4.8.2 节。

<!-- p.139 -->


所需信息：NAO 基下的 MO 系数

### 3.10.5 用 Hirshfeld 或

### Hirshfeld-I 方法计算原子和片段贡献(8、10)

Hirshfeld 和 Hirshfeld-I 权重函数(分别见第 3.9.1 和 3.9.13 节)也可用于将轨道分解为原子和片段组成，原子的组成

$$\int \varphi_i^2(\mathbf{r}) w_A(\mathbf{r}) \mathrm{d}\mathbf{r} \times 100\%$$

属于该片段的原子的组成之和。这些方法具有很好的基组稳定性，总是比 Mulliken 和 MMPA 更可靠、更合理。事实上，Hirshfeld 划分已经足够好，更复杂且计算量更大的 Hirshfeld-I 划分并无必要。

若你选择使用 Hirshfeld 划分，程序会提示你选择生成用于构建 Hirshfeld 权重函数的原子密度的方式，我强烈建议使用内建原子密度而不是使用原子 .wfn 文件，因为前者方便得多。若你选择使用 Hirshfeld-I 划分，将首先进行常规 HI 迭代以得到收敛的原子权重函数(若你对操作感到困惑，请查阅第 4.7.4 节计算 HI 电荷的例子以及第 3.9.13 节介绍的 Hirshfeld-I 实现细节)。

在计算轨道组成之前，程序自动进行数据初始化。一旦完成，你可以输入你感兴趣的轨道索引。由于数值积分总会引入一些误差，因此所有原子组成之和并不精确等于 100%，在极少数情况下偏差可能相对显著，因此 Multiwfn 会自动归一化结果并在标题“After normalization”下打印。

若你想同时查看某原子在特定范围轨道中的组成，选择选项-2(Option -2)，然后输入原子索引和轨道索引范围。

若你想研究片段对轨道的贡献，先用 -9 定义片段，然后当你输入轨道索引时，片段的贡献将与所有原子的贡献一起输出。此外，你还可以选择 -3 计算你定义的片段对一系列轨道的贡献。

若选择选项-4(Option -4)，程序将计算每个原子在每个轨道中的组成，然后将它们全部导出到当前文件夹下的 orbcomp.txt。

例子见第 4.8.3 节。所需信息：原子坐标和 GTFs

### 3.10.6 用 Becke 方法计算原子和片段贡献(9)

本功能与第 3.10.5 节介绍的功能非常相似，唯一区别是使用 Becke 划分代替 Hirshfeld 划分。在大多数情况下，它们的结果在定性上一致。使用 Becke 划分代替 Hirshfeld 划分有一个突出优点，即不需要原子波函数文件，因为 Becke 原子

<!-- p.140 -->


空间可简单地基于原子半径构建。关于 Becke 划分的更多细节，见第 3.18.0 节。例子见第 4.8.3 节。

所需信息：原子坐标和 GTFs

### 3.10.7 用 AIM 方法计算原子和片段贡献(11)

Multiwfn 也能基于分子空间的原子-分子(AIM)划分计算轨道组成。在这种划分方法中，每个原子 basin 对应一个原子的空间，关于 basin 和 AIM 划分的概念细节见第 3.20 节。要在 AIM 划分下计算轨道组成，你应使用 basin 分析模块(主功能17(main function 17))的子功能11(subfunction 11)，例子见第 4.8.6 节。

通常，我不建议用这种方式计算轨道组成，因为其成本显著高于其他方式，而结果并不更好。

所需信息：原子坐标和 GTFs

### 3.10.100 用 LOBA 和 mLOBA 方法评估氧化态(Evaluate oxidation state by LOBA and mLOBA method)(100)

本功能是 Phys. Chem. Chem. Phys., 11, 11297 (2009) 中提出的定域轨道成键分析(localized orbital bonding analysis, LOBA)方法以及由我提出的修正 LOBA(mLOBA)(待发表)的实现。

理论 LOBA 是一种基于定域分子轨道(LMOs)的轨道组成评估原子氧化态的方法。其思想非常简单：若某原子的核电荷为 Z，其在 N 个占据 LMOs 中的组成大于给定阈值(例如 50%。在这种情况下这些 LMOs 中的电子可近似视为完全归属于该原子。若某 LMO 为双占据，应计数两次)，则该原子的氧化态将为

Z−N。

LOBA 的思想也可扩展到定义片段的氧化态，即若某片段内的核电荷之和为 Z，且该片段对 N 个 LMOs 的贡献大于

某一阈值，则该片段的氧化态将为 Z−N。

mLOBA 采用不同的方式确定 LMOs 电子归属。在该方法中，每个 LMO 中的电子被指派给对它贡献最大的原子。这不仅消除了阈值选择的任意性，还保证氧化态之和恰好等于当前体系的净电荷。此外，mLOBA 中片段的氧化态简单地为其所有组成原子的氧化态之和。我强烈建议使用 mLOBA 而不是 LOBA！

mLOBA 唯一的缺点是当存在(局域)几何对称性时，结果可能不均衡。例如，在乙烷中有一个对应于 C-C 键的 LMO，两个碳原子对它的贡献相等。在 mLOBA 中，LOBA 中的两个电子可能被指派给两个碳中的任意一个，最终，一个碳的氧化态为 -4 而另一个为 -2。避免此问题的最好方法是将两个碳定义为一个
