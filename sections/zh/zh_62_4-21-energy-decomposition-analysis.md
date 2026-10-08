# 能量分解分析

> Multiwfn manual, p.913–930.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.913 -->


在.xyz轨迹文件中记录元素名而非原子名，否则Multiwfn可能错误猜测元素，使amIGM分析出错。注意Multiwfn载入输入文件后会显示体系化学式，从中你可很容易检查每种元素是否都被正确判断。

提示(Tip)：用amIGM研究配体-蛋白相互作用时制备轨迹文件的常用做法

首先，对溶剂化盒中的整个复合物做NPT模拟使其充分平衡，然后在配体固定的同时做至少1 ns的NVT模拟，至少保存500帧。再用VMD提取含配体及所有紧密接触残基的簇，并将此部分的轨迹保存为.xyz文件。你可用选择“resname MOL or protein same resid as within 3.5 of resname MOL”提取该簇，其中MOL为配体的残基名。接着，在amIGM分析中，你应定义两个片段，第一个为配体，另一个包含所有其它原子。在我的博客文章http://sobereva.com/591中给出了为aNCI分析生成配体-蛋白相互作用.xyz轨迹文件的完整例子，其也完全适用于amIGM分析。

## 4.21 能量分解分析

除本节所给例子外，Multiwfn还能做所谓简单能量分解，见4.100.8节例子。

### 4.21.1 基于力场(forcefield)的能量分解分析(EDA-FF)例子

本节我将说明如何基于经典力场对特定片段做能量分解分析，该方法称作EDA-FF。请先仔细阅读3.24.1节以获得关于EDA-FF基本思想与实现的知识。若你已仔细读过下例，你应能很容易地将此法用于各种体系。

更深入的讨论见我的博客文章“使用Multiwfn做基于力场的能量分解分析”（中文，http://sobereva.com/442）。

若你的工作中用了EDA-FF分析，请引用此文：Mat. Sci. Eng. B, 273, 115425 (2021) DOI: 10.1016/j.mseb.2021.115425，其中我简述了EDA-FF并用它研究了环[18]碳与石墨烯的相互作用

### 4.21.1.1 例1：水二聚体

作为首例，我们基于AMBER力场对非常简单的体系——水二聚体做EDA-FF，其最稳定几何如下所示

<!-- p.914 -->


相关文件 相关文件已提供于“examples\EDA\EDA_FF\waterdimer”文件夹，如下所示：

- dimer.mol：水二聚体的.mol文件，含其在B3LYP-D3(BJ)/6-311G**水平优化的几何，该水平对优化分子簇非常可靠。注意此文件中原子顺序为O1 H2 H3 O4 H5 H6

- water.fchk：水单体在B3LYP-D3(BJ)/6-311G**水平优化任务产生的.fchk文件

- mollist.txt：对应水二聚体的分子列表文件
- water.txt：水单体的分子类型文件 可见，mollist.txt内容很简单

```text
water.txt 2
```

对应水二聚体有两个水分子这一事实，它们由当前文件夹中的water.txt描述。

water.txt内容为

```text
OW  -0.737121
HW  0.368560
HW  0.368560
```

表明水中氧和氢的原子类型分别为OW和HW。第二列为用Merz-Kollman (MK)方法求得的原子电荷。

分子类型文件细节 此处我描述water.txt是如何构建的。原子类型可按原子的实际化学环境及力场原始论文中原子类型的定义手动指定，但若分子中原子很多则此过程很麻烦。因此，此处我展示如何用流行的GaussView自动指定原子类型。将water.fchk载入GaussView，点击粗体A字母图标进入“原子列表编辑器(atom list editor)”，再点击粗体橙色M字母图标以显示原子类型，然后双击“AMBER Type”列标题，此时窗口状态应为

然后点击“文件(File)”-“导出数据(Export Data)”，将文件保存为water.txt。接着，通过Ultraedit等高级

![](../imgs/p914_451.png)

![](../imgs/p914_452.png)

<!-- p.915 -->


文本编辑器的列模式，删除除“AMBER Type”列之外的所有列，再删除文件首行。此时，water.txt中只呈现所有原子的原子类型。之后，基于water.fchk用主功能7的子功能13（或12）计算MK（或CHELPG）电荷（可参阅4.7.1节例子），再将屏幕输出的电荷（或从导出的.chg文件）复制为water.txt的第二列。至此，water.txt的准备完毕。

进行分析 现在，我们开始做EDA-FF分析。将water.txt复制到当前文件夹，然后启动Multiwfn并输入

dimer.mol // 含二聚体结构信息的文件（你也可用含几何信息的其它格式作输入文件，如二聚体优化任务产生的.fch文件）

21 // 能量分解分析(Energy decomposition analysis) 1 // 基于力场的能量分解分析(Energy decomposition analysis based on forcefield) 3 // 载入原子类型与原子电荷(Load atom types and atomic charges) mollist.txt // 分子列表文件的实际路径。此时，程序从water.txt读取原子类型与电荷并赋给当前体系中的两个水分子

2 // 定义片段(Define fragments) 2 // 将定义两个片段(Two fragments will be defined) 1-3 // 片段1的原子序号(The atomic indices of the fragment 1) 4-6 // 片段2的原子序号(The atomic indices of the fragment 2) 若你想检查当前体系所有原子的原子类型与电荷是否已正确设置，可选选项4，输出为

```text
*** Fragment   1:
 Atom:    1(O )    Charge:   -0.737121    Type: OW
 Atom:    2(H )    Charge:    0.368560    Type: HW
 Atom:    3(H )    Charge:    0.368560    Type: HW
 *** Fragment   2:
 Atom:    4(O )    Charge:   -0.737121    Type: OW
 Atom:    5(H )    Charge:    0.368560    Type: HW
 Atom:    6(H )    Charge:    0.368560    Type: HW
```

可见原子类型与电荷都已正确指定。

现选选项1开始EDA-FF分析，结果立即显示于屏幕：

```text
Contribution of each atom in defined fragments to overall interfragment interac
tion energies:
 Atom    1(O )   Elec:   12.53  Rep:    3.85  Disp:   -2.21  Total:   14.17
 Atom    2(H )   Elec:   -6.24  Rep:    0.00  Disp:    0.00  Total:   -6.24
 Atom    3(H )   Elec:  -16.87  Rep:    0.00  Disp:    0.00  Total:  -16.87
 Atom    4(O )   Elec:  -23.52  Rep:    3.85  Disp:   -2.21  Total:  -21.88
 Atom    5(H )   Elec:    6.47  Rep:    0.00  Disp:    0.00  Total:    6.47
 Atom    6(H )   Elec:    6.47  Rep:    0.00  Disp:    0.00  Total:    6.47

 Interaction energy components between all fragments:
```

<!-- p.916 -->


```text
                         Electrostatic   Repulsive   Dispersion     Total
 Frag   1 -- Frag   2:       -21.15         7.71        -4.43       -17.87
```

输出单位均为kJ/mol。上述信息表明两水分子间总相互作用能为-17.87 kJ/mol，接近高精度CCSD(T)/CBS水平的结果-20.58 kJ/mol（见S66弱相互作用测试集原始论文，J. Chem. Theory Comput., 7, 2427 (2011)）。尽管给定结果有些误差，至少足以作定性讨论。上述数据还表明静电相互作用（-21.15 kJ/mol）对两水间结合能有决定性贡献，显然一般氢键的主要本质由静电相互作用主导。色散相互作用也有贡献，但量级相对较小。交换排斥效应（7.71 kJ/mol）在一定程度上抵消了静电与色散的吸引作用。

在S66测试集原文中，用非常理想的DFT-SAPT方法给出的水二聚体色散相互作用能与静电相互作用能之比为0.29，与EDA-FF给出的值（4.43/21.15=0.21）定性一致。因此，以非常简单的水二聚体为例可见，只要力场与原子电荷选择得当，EDA-FF结果一般是可靠的。对有些体系，力场算得的总相互作用能与可靠量子化学方法求得的不太接近，但即便如此，一般EDA-FF提供的各物理成分间比例仍有意义。依我之见，

用适当力场求得的ΔEele与ΔEtot之比乘以量子化学方法得到的总相互作用能（ΔEtot），以近似估计静电相互作用能（ΔEele），不失为一个好主意。

上述输出还给出每个原子对所有已定义片段间总相互作用的贡献，使你能很容易识别哪些原子对片段间相互作用有关键影响。所有原子贡献之和等于总相互作用能（若体系只有两个原子A和B，且各自定义为一个片段，则原子A的贡献为A-B相互作用能之半）。由上数据可见每个原子的影响都不可忽略。毕竟体系中原子间距离不远。对吸引作用最重要的贡献是O4原子的静电相互作用（-23.52 kJ/mol），此结果易于理解，因O4为氢键受体原子。与O4直接作用形成氢键的H3也因显著的静电效应而对结合有很大贡献（-16.87 kJ/mol）。数据表明只有氧原子有非零排斥与色散项，这是因为HW原子类型的vdW势参数为零，故HW原子仅表现为点电荷以呈现静电效应。

原子间相互作用 若你选一次选项-3将其状态从默认“否(No)”切换为“是(Yes)”，则在经选项1做EDA-FF分析时，程序还将每对原子的距离（Å）、相互作用能（kJ/mol）及其成分输出到当前文件夹的interatm.txt中。当前例子的文件内容为

```text
******* Between fragment   1 and fragment   2:
  Atom_i  Atom_j  Dist(Ang) Electrostatic   Repulsive    Dispersion     Total
      1      4:     2.873       262.78         7.71        -4.43       266.05
```

<!-- p.917 -->


```text
      1      5:     3.176      -118.86         0.00         0.00      -118.86
      1      6:     3.176      -118.86         0.00         0.00      -118.86
      2      4:     3.346      -112.79         0.00         0.00      -112.79
      2      5:     3.762        50.16         0.00         0.00        50.16
      2      6:     3.762        50.16         0.00         0.00        50.16
      3      4:     1.916      -197.02         0.00         0.00      -197.02
      3      5:     2.312        81.64         0.00         0.00        81.64
      3      6:     2.312        81.64         0.00         0.00        81.64
```

由上数据可见，每对原子间相互作用能都很大，主要来自静电相互作用。例如，因两氧原子O1与O4电荷大且同号，静电互斥能高达262.78 kJ/mol。片段间结合能看似比上述值小数量级，这是因为计算片段间相互作用能时，原子对的静电相互作用正负大部抵消。

### 4.21.1.2 例2：环晕苯-胞嘧啶-鸟嘌呤三聚体

在J. Chem. Theory Comput., 9, 3364 (2013)给出的L7弱相互作用测试集中，一个体系C3GC是由环晕苯（下文简称C3）、鸟嘌呤(G)与胞嘧啶(C)组成的三聚体。几何已由作者在TPSS-D/TZVP水平优化，如下

所示。GC碱基对已形成三重氢键，且它经由π-π堆积物理吸附于C3之上。

本节我们将基于AMBER力场对此体系做EDA-FF分析。相关文件提供于“examples\EDA\EDA-FF\C3GC”目录。

准备工作 注意Multiwfn仅当任一分子类型中的原子序号连续时才能做EDA-FF。否则，无法经分子列表文件和分子类型文件为体系中每个原子设置原子电荷与类型。L7测试集补充材料给的结构文件为C3GC.xyz。此文件不能直接使用，因为每个单体中的原子序号不连续。判断原子序号是否连续的最简单方法之一如下：首先将C3GC.xyz载入Multiwfn，用主功能100的子功能2将其转为C3GC.pdb（做此转换是因为GaussView不支持.xyz

![](../imgs/p917_453.png)

<!-- p.918 -->


格式），再将此pdb文件载入GaussView，在任一分子的任意原子（如C5原子）上右击，选“按原子C5选择片段(Select Fragments of Atom C5)”（此选项自GaussView 6起可用）。此时该分子中所有原子被选中呈黄色，再点击“工具(Tools)”-“原子选择(Atom Selection)”。如下截图所示，文本框显示的序号为5-9、13-17、19、25-29，显然原子序号不连续，应予修正。

使每个分子中原子序号连续的最简方法是进入GaussView的“原子列表编辑器(Atom list editor)”，再选“编辑(Edit)”-“重排(Reorder)”-“按成键重排除首原子外的所有原子(All Atoms (Except the First) by Bonding)”，之后原子序号按连通性重排，你将看到每个单体中的原子序号已变为连续，如下所示。现将此结构保存为C3GC.pdb以替换旧文件。

然后我们将三聚体中每个单体复制到各自的GaussView窗口，保存为各自的.gjf文件，将关键词改为“B3LYP/6-311G**”并用Gaussian运行，再基于所得.fch文件用Multiwfn计算MK电荷。同时，我们利用GaussView确定每个单体的原子类型。最后，将原子类型与电荷合并为每个单体的单个文件，于是得到C.txt、G.txt和C3.txt，它们已提供于“examples\EDA\EDA-FF\C3GC”目录。

最后，创建分子列表文件mollist.txt（其它名字亦可），内容为C.txt、G.txt和C3.txt的实际路径以及相应分子数，注意

![](../imgs/p918_454.png)

![](../imgs/p918_455.png)

<!-- p.919 -->


文件路径的顺序必须与G3GC.pdb所给几何中的分子顺序严格一致。显然，mollist.txt内容应为（设所有分子类型文件置于C:\下）

```text
C:\C.txt 1
C:\G.txt 1
C:\C3.txt 1
```

开始分析 所有准备工作已完成，现在开始EDA-FF分析。启动Multiwfn并输入

C3GC.pdb 21 // 能量分解分析(Energy decomposition analysis) 1 // EDA-FF 3 // 载入原子类型与电荷(Load atom types and charges) mollist.txt // 输入mollist.txt实际路径(Input actual path of mollist.txt) 2 // 定义片段(Define fragments) 3 // 将定义三个片段(Three fragments will be defined) 1-13 // 片段1中的原子序号，即胞嘧啶(C)(Atom indices in fragment 1, namely cytosine (C)) 14-29 // 片段2中的原子序号，即鸟嘌呤(G)(Atom indices in fragment 2, namely guanine (G)) 30-101 // 片段3中的原子序号，即C3(Atom indices in fragment 3, namely C3) 选选项1进行EDA-FF计算，结果如下（忽略原子贡献部分）

```text
                         Electrostatic   Repulsion   Dispersion     Total
 Frag   1 -- Frag   2:      -120.98        60.26       -45.54      -106.27
 Frag   1 -- Frag   3:         1.88        44.86       -94.69       -47.95
 Frag   2 -- Frag   3:         0.71        62.08      -132.62       -69.84
```

数据显示G-C结合很强，高达-106.27 kJ/mol，主因是静电成分很大（-120.98 kJ/mol），这是G与C之间形成三对氢键的结果。C3与G间（-47.95 kJ/mol）以及C3与C间（-69.84 kJ/mol）的总相互作用能也不小，主要归因于

其间显著的π-π堆积。因π-π堆积本质纯为色散效应，可见C3-C与C3-G的色散相互作用很强（分别为-94.69和-132.62 kJ/mol），远高于G-C之间（-45.54 kJ/mol）。因C3本质为有限石墨烯片，其与G、C的相互作用区域显然非极性（即原子电荷很小），故C3-C与C3-G相互作用中的静电成分可忽略（仅0.71和1.88 kJ/mol）。

我还用二聚体模型在B3LYP-D3(BJ)/6-311+G**水平计算了G-C、C3-G与C3-C间结合能，该水平对评估弱相互作用非常稳健，结果为

```text
G-C (Frag 1 - Frag 2)：-143.97 kJ/mol
C3-C (Frag 1 - Frag 3)：-56.69 kJ/mol
C3-G (Frag 2 - Frag 3)：-76.27 kJ/mol
```

对C3-C与C3-G，可见AMBER力场算得的结果与量子化学方法求得的很接近，但对G-C定量差异颇显著。此现象表明力场用于强度很大的弱相互作用时定量精度有限。但在此情形，若只关注

<!-- p.920 -->


各物理成分间比例，EDA-FF结果仍有用，不会造成明显误导性结论。

按对相互作用能的贡献给原子着色 利用.pqr文件格式，原子性质可很容易地在VMD可视化程序中按不同颜色给原子着色来可视化，此策略在4.A.10节详细介绍。显然，若将原子对片段间相互作用能的贡献存入.pqr文件，则每个原子的重要性与作用将能生动展示于图中。类似思想也用于IGM分析，如4.20.10节所示。

现我们在EDA-FF界面选“-4 是否输出原子贡献到.pqr文件(Toggle if outputting atom contributions to .pqr files)”选项将其状态切换为“是(Yes)”，再选选项1进行EDA-FF分析。计算后，当前目录出现atmint_tot.pqr、atmint_ele.pqr、atmint_rep.pqr、atmint_disp.pqr和atmint_vdW.pqr（其中一些已提供于“examples\EDA\EDA-FF\C3GC\pqr”）。这些.pqr文件中原子电荷列的数据分别对应每个原子对片段间总/静电/排斥/色散/vdW相互作用能的贡献，数值与屏幕打印的完全相同。例如，atmint_disp.pqr中片段1的C1原子在原子电荷列的值对应C1原子与片段2、3所有原子间色散相互作用能之半。

我们将atmint_tot.pqr载入VMD程序，进入“图形(Graphics)”-“显示方式(Representation)”，按“电荷(Charge)”属性给原子着色，将色标下限与上限从默认值分别改为-50和50。将G、C部分的绘制方法设为CPK模式（在“选定原子(Selected Atoms)”框用fragment 0 1选它们），C3部分以甘草式(Licorice)显示（用fragment 2选它）。我们还将色标方法设为BWR（蓝-白-红）。最后，图将如下所示（若你不熟悉VMD而不知如何在VMD实现这些设置，请参阅4.A.10节）：

因当前所用色标为蓝-白-红(Blue-White-Red)，图中原子颜色越蓝，对三聚体间总结合能的原子贡献越负（即吸引效应越显著）；而原子越红，其排斥效应越强

![](../imgs/p920_456.png)

<!-- p.921 -->



作用。颜色较白的原子对三聚体结合只起微不足道的作用。从该图中可以看出，每个氢键受体原子以及与其直接作用的氢原子颜色明显偏蓝，因此它们对 G-C 结合的稳定性贡献很大。所有氢键给体原子的颜色为红色，表明它们的存在不利于结合，这是因为氢键给体与受体原子的原子电荷数值大且符号相同，因此它们之间存在显著的静电互斥。从上图中还可以看出，C3 的所有原子以及 G 和 C 中远离氢键区域的原子都只有很浅的颜色或纯白色，这一现象并不意味着它们对三聚体结合的贡献几乎消失，而是表明它们的贡献相对较弱，因此在当前的颜色标尺设置下难以显示出来。

假设我们想生动地展示 C3 与 GC 碱基对之间的色散相互作用，则在 EDA-FF 界面中输入以下命令

2 // 重新定义片段(Redefine fragments) 2 // 将定义两个片段(Two fragments will be defined) 1-29 // 片段 1，即 GC 碱基对 30-101 // 片段 2，即 C3 部分 1 // 开始 EDA-FF 计算 然后屏幕上将显示以下信息，该数据等于 C3-C 与 C3-G 相互作用能之和


```text
                         Electrostatic   Repulsion   Dispersion     Total
 Frag   1 -- Frag   2:         2.59       106.94      -227.31      -117.79
```

同时，当前文件夹中会生成四个新的 .pqr 文件（它们已提供在 "examples\EDA\EDA-FF\C3GC\pqr2" 文件夹中）。将其中 atmint_disp.pqr 载入 VMD，按照上述方法根据原子着色，但使用 -10 到 10 的颜色标尺，然后选择 显示(Display) - 正交投影(Orthographic) 以改变视角，你将看到

在上图中，原子颜色越蓝，其对 C3 与 GC 之间色散相互作用的贡献越大。从图中可以看出，GC 部分的每个重原子对色散相互作用的贡献几乎相等，这主要是因为它们到 C3 平面的垂直距离几乎相同，且这些原子所携带的电子数没有很大


![](../imgs/p921_457.png)

<!-- p.922 -->



差异。GC 碱基对中的氢原子对 C3-GC 色散相互作用的贡献非常小，这是因为氢原子只有很少的电子。在 C3 部分，与 GC 碱基对直接接触的碳原子颜色为浅蓝色，表明它们对色散相互作用有显著贡献。远离 GC 碱基对的 C3 原子颜色为白色，反映了它们对色散相互作用的影响可以忽略（回想色散吸引随距离急剧衰减这一事实，它具有 1/r6 渐近行为）。

注：上图中 GC 碱基对中的重原子非常蓝，而处于等价位置的 C3 原子却没有那么蓝，原因是：由于 C3 中原子很多，GC 碱基对中的每个重原子可以与大范围的 C3 原子形成色散相互作用，因此各项之和很大。由于 GC 碱基对中的原子数目较少，C3 的每个原子只能与 GC 碱基对中相对较少的原子相互作用，因此各项之和不大。如果你想让 C3 部分的原子颜色更突出，可以将 C3 部分对应的表示(Representation)的颜色标尺范围设为比我们之前使用的 -10~10 更小的值；例如，改为 -6 到 6 将得到满意的图形。

关于确定单个氢键的结合能 一些读者可能想到，如果能独立确定 G-C 之间三个氢键各自的结合能就好了。实现这一目标没有唯一的方法，因为这相当于把体系划分成几个部分，必然会引入人为误差。实现这一目的的一个看似简单的方法是直接把一个氢键的给体和受体部分定义为两个片段。例如，让我们考察 N10-H13...O14 氢键，我们输入

2 // 重新定义片段(Redefine fragments) 2 // 将定义两个片段(Two fragments will be defined) 10,13 // N10-H13...O14 给体部分的原子序号 14 // N10-H13...O14 受体部分的原子序号 1 // 执行 EDA-FF 分析 结果为


```text
                         Electrostatic   Repulsion   Dispersion     Total
 Frag   1 -- Frag   2:        71.27        21.78        -9.40        83.65
```

显然结果不合理，因为预测的总结合能为正值！根本原因在于静电相互作用是一种长程效应（1/r 渐近行为），因此不能简单地忽略其它原子的贡献。我还尝试了其它方法来评估 N10-H13...O14 氢键的结合能，尽管其中一些方法给出了看似可接受的结果（例如，把 N10、H12、H13 和 O14 对总 G-C 结合能的原子贡献加和），但遗憾的是三种氢键的相对强弱无法得到忠实解释。在我看来，基于 EDA-FF 无法推导该体系中单个氢键的相互作用能，原因是三个氢键靠得太近，因而耦合非常强，极化效应明显，同时这些氢键中还涉及共振协助效应，这些因素使得三个氢键的总相互作用能很难被合理分解。然而，如果存在几个氢键且位点彼此相距较远，那么通过估计相应局域区域内原子之间的相互作用能，分别评估每个氢键的强度应该是可行的。

据我所知，确定单个氢键结合能的最佳方法是使用分子中的原子(AIM)分析，见第 4.2.1 节的介绍和示例。

其它方面 值得注意的是，除了 SAPT 之外，评估色散相互作用能的一个可能可行的方法是使用零阻尼参数的 DFT-D3 色散校正，该参数是针对完全不能描述色散相互作用的交换相关泛函拟合的。该策略已在第 4.100.8 节的能量分解分析示例中使用。使用零阻尼 BLYP 泛函参数的片段间相互作用能的 DFT-D3 色散校正如下所示


<!-- p.923 -->



交换相关泛函。如下所示


```text
C -- G: -26.65 kJ/mol
C -- C3: -87.78 kJ/mol
G -- C3: -115.10 kJ/mol
```

可以看出，这三个值与用 AMBER 力场评估的相应色散相互作用能（分别为 -45.54、-94.69、-132.62）接近，表明用 AMBER 力场或 DFT-D3 来估计色散相互作用能都是合理的方法。

使用 UFF 进行 EDA-FF 分析通常不理想。如果我们对当前体系这样做，结果为


```text
                         Electrostatic   Repulsion   Dispersion     Total
 Frag   1 -- Frag   2:      -120.98       848.28       -80.36       646.94
 Frag   1 -- Frag   3:         1.88        52.65      -107.41       -52.87
 Frag   2 -- Frag   3:         0.71        68.89      -143.58       -73.99
```

可以看出，UFF 预测的 C3-C 和 C3-G 相互作用正常，结果数值与 AMBER 计算的结果接近，但 G-C 的相互作用能为很大的正值，显然这完全不合理。从数据中很容易发现原因是交换排斥分量被严重高估。这不是个别现象，而是 UFF 的普遍现象，这就是为什么我一般不推荐基于 UFF 进行 EDA-FF（尽管在 EDA-FF 之前先用 UFF 优化几何可以缓解这一问题）。

如第 3.24.1 节所述，对于非常大的体系，使用非常廉价的 EEM 电荷（以 B3LYP/6-31G* 水平下的 CHELPG 电荷拟合的参数）代替严格推导的 ESP 拟合电荷来进行 EDA-FF 分析可能是一个可行的选择；然而，我的测试表明这种处理会对当前体系的静电相互作用造成显著误差。基于 EEM 电荷评估的 G 与 C 之间的静电相互作用能仅为 -74.26 kJ/mol，远低于基于 MK 电荷评估的值（-120.98 kJ/mol）。因此，只要可能，强烈推荐在 EDA-FF 分析中使用 ESP 拟合电荷（MK 或 CHELPG），这对获得足够准确的静电相互作用能至关重要。


### 4.21.2 Shubin Liu 能量分解分析在乙烷旋转

### 势垒中的应用

Shubin Liu 能量分解（EDA-SBL）的思想和用法已在第 3.24.2 节中介绍。本节我们用 EDA-SBL 方法研究乙烷优化后的重叠式与交错式构象之间能量差异的来源。相关输入和输出文件已在 "examples\EDA\EDA_SBL" 文件夹中给出。

首先，我们用 Gaussian 在 B3LYP/def-TZVP 水平下优化交错式构象（D3 点群）和重叠式


<!-- p.924 -->



构象（D3h 点群）的乙烷，后者实际上是一个过渡态。然后利用这些几何结构创建两个 Gaussian 输入文件，分别命名为 ethane_staggered.gjf 和 ethane_eclipsed.gjf。这两个文件对应于 B3LYP/def2-TZVP 水平的单点任务。如第 3.24.2 节所述，路径行包含 ExtraLinks=L608 关键词，且输入文件末尾有 -5 行，表示当前使用的泛函为 B3LYP。

用 Gaussian 运行这两个 .gjf 文件，分别得到 ethane_staggered.out 和 ethane_eclipsed.out，然后用 formchk 将得到的 .chk 文件转换为 .fch 文件。

我们首先评估交错式乙烷的 EDA-SBL 方法定义的能量项。启动 Multiwfn 并输入

examples\EDA\EDA_SBL\ethane_staggered.fch 21 // 能量分解分析(Energy decomposition analysis) 2 // Shubin Liu 能量分解(Shubin Liu's energy decomposition) examples\EDA\EDA_SBL\ethane_staggered.out 现在 Multiwfn 从 Gaussian 输出文件中载入相关信息，然后评估 EDA-SBL 方法定义的空间位阻(steric)项。最后，打印 EDA-SBL 能量分量：


```text
 E_steric:              64.213411 Hartree
 E_electrostatic:     -146.114859 Hartree
 E_quantum:              2.037465 Hartree

 E_total:              -79.863983 Hartree
```

E_total 与 Gaussian 输出文件中的单点能完全一致。

我们对重叠式乙烷重复上述分析，然后将数据汇总到下表中

Etotal Esteric Eelectrostatic Equantum

重叠式(Eclipsed) (a.u.) -79.85972 64.21925 -146.10780 2.02883 交错式(Staggered) (a.u.) -79.86398 64.21341 -146.11486 2.03747 差值(Diff.) (kJ/mol) 11.2 15.3 18.5 -22.7

可以看出，重叠式构象的能量比重叠式高 11.2 kJ/mol，这对应于乙烷 C-C 单键旋转的势垒。数据表明

空间位阻效应应该是势垒的主要贡献者之一，因为 ΔEsteric 明显为正。此外，相当大的 ΔEelectrostatic=18.5 kJ/mol 表明静电相互作用是决定势垒高度的主导因素。相比之下，反映纯粹由量子效应引起的能量变化的 Equantum 的变化显著抵消了空间位阻项和经典静电项，从而在降低势垒方面起重要作用。

如屏幕上所见，EDA-SBL 模块还打印了构成 Esteric、Eelectrostatic 和 Equantum 的其它中间量，例如 Pauli 动能，因此你可以利用它们尝试从更多角度分析两种构象之间的能量差异。

在 J. Phys. Chem. A, 117, 962 (2013) 中给出了用 EDA-SBL 方法对一系列小有机分子旋转势垒的深入分析，建议感兴趣的用户阅读。


<!-- p.925 -->




### 4.21.3 sobEDA 和 sobEDAw 能量分解

### 分析示例

sobEDA.sh 脚本用于基于 Gaussian 和 Multiwfn 方便地进行 sobEDA 和 sobEDAw 能量分解分析。非常详细的介绍和丰富的应用示例见 http://sobereva.com/soft/sobEDA_tutorial.zip，请仔细查看。


### 4.21.4 原子对色散能贡献分析示例

注：本节的中文版是我的博文“使用 Multiwfn 图形化展示原子对色散能的贡献和色散密度”（http://sobereva.com/705），其中包含更多示例和讨论。

本节给出原子对色散能贡献以及色散能分析的一些示例。请先仔细阅读第 3.24.4 节以获得基础知识，并了解如何在 `settings.ini` 中设置“dftd3path”。

### 4.21.4.1 考察螺旋烯中原子对色散能的贡献

和色散密度

在本例中，我们考察哪些原子对 6-螺旋烯的色散能有突出贡献。启动 Multiwfn 并输入

examples\helicene.xyz // 6-螺旋烯的结构文件 21 // 能量分解分析(Energy decomposition analysis) 4 // 原子对色散能贡献分析(Analysis of atomic contribution to dispersion energy) 1 // 计算当前体系原子对色散能的贡献(Calculate atomic contributions to dispersion energy for current system) 立即，你将在屏幕上看到以下信息，其中包含当前体系的总色散，即带有为 B3LYP 拟合参数的 DFT-D3(BJ) 色散校正能。同时，清楚地给出了每个原子对色散能的贡献。


```text
Total dispersion energy:     -74.468 kcal/mol

 Atomic contribution to dispersion energy
     1(C )    -2.681 kcal/mol
     2(C )    -2.072 kcal/mol
     3(C )    -2.068 kcal/mol
     4(C )    -2.650 kcal/mol
     5(C )    -3.432 kcal/mol
[...ignored]
    40(H )    -0.569 kcal/mol
    41(H )    -0.511 kcal/mol
    42(H )    -0.614 kcal/mol
```

接下来，你可以输入 y 以在当前文件夹中导出 atomdisp.pqr。将其载入 VMD 程序，在 图形(Graphics) - 表示(Representation) 界面中，将 绘制方式(Drawing Method) 设为 CPK，将 着色方式(Coloring Method) 设为


<!-- p.926 -->



“电荷(Charge)”，然后在 轨迹(Trajectory) 面板中，将颜色标尺的下限和上限分别设为 -5.0 和 5.0。你将看到如下图所示。由于 VMD 默认使用的颜色标尺为红-白-蓝，此图中颜色越红，原子对色散能的贡献越负，其与其它原子的色散相互作用越强。

从上图可以看出，碳原子对色散能的贡献远大于氢原子，且越靠近螺旋烯中心的碳原子贡献越大。原因很容易理解，因为越靠近分子中心的碳原子越能与其它原子有丰富的色散相互作用。

接下来，我们计算色散密度。选择选项“2 计算当前体系的色散密度(Calculate dispersion density for current system)”，然后选择“中等质量格点(Medium-quality grid)”，你会发现 dispdens.cub 已导出到当前文件夹，它是色散密度的 cube 文件（单位为 kcal/mol/Bohr3）。将其载入 VMD，以等值面图绘制，等值设为 -0.15，材质设为透明，并将分子结构图的表示方式设为 licorice，你将得到如下图所示。图中S等值面的分布清楚地表明，螺旋烯内部区域对比其它区域对色散能有相对更显著的贡献。

值得注意的是，你可以使用本功能中的选项 6 来计算任意定义的两个片段之间的色散相互作用能。例如，要计算螺旋烯两端的两个六元碳环之间的色散相互作用能，选择该选项后，你应输入 17-22 然后输入 11-12,23-26，你将看到


```text
Dispersion interaction energy between the fragments:      -2.809 kcal/mol
```


![](../imgs/p926_458.png)

![](../imgs/p926_459.png)

<!-- p.927 -->



### 4.21.4.2 actos 两种构象之间色散能的

差异

Actos 是一种柔性药物分子，其卷曲构象和伸展构象的 xyz 文件已在“examples”文件夹中分别作为 Actos_curly.xyz 和 Actos_linear.xyz 提供。本节我们考察卷曲构象相对于伸展构象原子对色散能贡献的变化。启动 Multiwfn 并输入

examples\Actos_curly.xyz 21 // 能量分解分析(Energy decomposition analysis) 4 // 原子对色散能贡献分析(Analysis of atomic contribution to dispersion energy) 3 // 计算当前体系与另一体系之间原子对色散能贡献的差值(Calculate difference of atomic contributions to dispersion energy between current and another systems)

[直接按 ENTER 键] //当前体系（Actos_curly.xyz）中的所有原子都是感兴趣的 examples\Actos_linear.xyz [直接按 ENTER 键] //Actos_curly.xyz 中的所有原子都是感兴趣的 从屏幕输出中，你可以发现 Actos_linear.xyz 和 Actos_curly.xyz 的总色散能分别为 -57.553 kcal/mol 和 -69.757 kcal/mol。显然卷曲构象的色散相互作用更显著。同时，还打印了每个原子对两种结构色散能贡献的差值。

然后输入 y，将在当前目录中生成 diffatomdisp.pqr，其中“charge”属性记录了 Actos_curly.xyz 每个原子贡献的色散能减去 Actos_linear.xyz 每个原子贡献的色散能，该文件中的原子坐标与 Actos_curly.xyz 相同。使用 VMD 基于该文件根据“charge”属性对分子结构着色绘制，并将颜色标尺范围设为 -1.0 到 1.0 kcal/mol，你将得到下面左侧的图（颜色标尺条是从 图形(Graphics) - 颜色(Color) - 颜色标尺(Color Scale) 面板截取后用 Powerpoint 手工制作的），下面右侧图中的原子按元素名称着色以作比较（黄色/青色/红色/蓝色/白色分别为硫/碳/氧/氮/氢）。

左上图中越红的原子对应于在从伸展构象变为卷曲构象过程中对色散能变化贡献更大的原子。可以看出，色散相互作用的增强主要发生在构象卷曲后能与其它原子变得更近的原子上。主要分布在边角处的白色原子的色散效应没有明显变化。


![](../imgs/p927_460.png)

<!-- p.928 -->



Multiwfn 还可以生成色散密度的差值格点数据。在当前功能中输入以下命令

4 // 计算当前体系与另一体系之间的色散密度差值(Calculate dispersion density difference between current and another system) [直接按 ENTER 键] //当前体系（Actos_curly.xyz）中的所有原子都是感兴趣的 examples\Actos_linear.xyz // 另一体系 [直接按 ENTER 键] //Actos_curly.xyz 中的所有原子都是感兴趣的 3 // 高质量格点(High-quality grid) 现在当前文件夹中生成了 dispdensdiff.cub。使用 VMD 通过第 4.A.14 节所述的便捷 VMD 脚本将其绘制为等值面图，等值设为 ±0.025，你将看到如下图所示，蓝色表示等值面对应负值。可以看出，等值面很好地突出了因结构卷曲导致色散能显著增强的区域。

### 4.21.4.3 甲苯在沸石上的吸附

本节说明对周期性体系的分析。“examples”文件夹中的 zeolite.cif 和 zeolite-mol.cif 分别是沸石以及吸附了甲苯的沸石的结构文件。后者由 CP2K 程序在 PBE-D3(BJ)/DZVP-MOLOPT-SR-GTH 水平下优化，前者的坐标直接从后者中提取。这两个 .cif 文件可用作原子对色散能贡献分析和计算色散密度的输入文件。由于 .cif 文件向 Multiwfn 提供了晶胞信息，计算将自动考虑周期性进行。

首先，我们对 zeolite-mol.cif 进行分析，并用与第 4.21.4.1 节所述完全相同的方法根据原子对色散能的贡献着色，将颜色标尺设为 -8.0 到 8.0 kcal/mol，你将得到如下图所示。只有吸附的甲苯的原子（对应文件中的原子 217-231）显示为大球。从图中可以看出，硅原子对色散能的贡献最大，远大于氧和碳原子，甲苯中的氢原子贡献最小。


![](../imgs/p928_461.png)

<!-- p.929 -->



上图没有直接显示沸石中哪些原子与甲苯有最强的色散相互作用。为了清楚地研究这一点，我们需要求出 zeolite-mol.cif 体系中沸石原子（原子 1-216）对其色散能的贡献与 zeolite.cif 体系中原子对其色散能的贡献之差。下面将进行此操作。

启动 Multiwfn 并输入 examples\zeolite-mol.cif 21 // 能量分解分析(Energy decomposition analysis) 4 // 原子对色散能贡献分析(Analysis of atomic contribution to dispersion energy) 3 // 计算当前体系与另一体系之间原子对色散能贡献的差值(Calculate difference of atomic contributions to dispersion energy between current and another systems)

1-216 // 感兴趣的原子是当前体系（zeolite-mol.cif）中沸石部分的原子（前 216 个原子）

examples\zeolite.cif // 另一体系 [直接按 ENTER 键] //感兴趣的原子是 zeolite.cif 中的全部 216 个原子，它们也对应于 zeolite-mol.cif 中的原子 1-216

y // 在当前文件夹中导出 diffatomdisp.pqr 将 diffatomdisp.pqr 载入 VMD，按“charge”属性对原子着色，将颜色标尺设为 -0.8 到 0.8，你将看到


![](../imgs/p929_462.png)

<!-- p.930 -->



上图中吸附的甲苯完全为白色，因为它不在我们先前定义的 zeolite-mol.cif 的感兴趣原子范围内，因此其数据完全为零。图中粉色或红色的原子表明，靠近甲苯的沸石原子贡献的色散能因吸附而发生了很大变化。由于 zeolite-mol.cif 中沸石部分的结构与 zeolite.cif 相同，因此，上图中原子的颜色完全反映了沸石原子与甲苯之间的色散相互作用。从图中可以看出，色散相互作用随距离衰减非常快（已知为 1/r6 衰减行为）。基本上，只有最靠近甲苯的一层沸石原子才与其有显著的色散相互作用。

上图可以变为如下图所示，它更清楚地显示了与甲苯有突出相互作用的沸石原子。具体而言，在 VMD 的 图形(Graphics) - 表示(Representation) 界面中应创建三个表示(Rep)

- 表示 1(Rep 1)：显示甲苯，用名称(Name)着色，以 Licorice 风格和 BrushedMetal 材质显示

- 表示 2(Rep 2)：使用选择 serial 1 to 216 显示整个沸石，将绘制方式设为 Licorice（键半径(Bond Radius) = 0.1），将着色方式设为“电荷(Charge)”，材质设为透明(Transparent)

- 表示 3(Rep 3)：显示“charge”属性比 -0.2 更负的沸石原子（使用选择 charge<-0.2），使用 CPK 绘制方式和“电荷(Charge)”着色方式。


![](../imgs/p930_463.png)
