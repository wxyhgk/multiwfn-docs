# 电子离域与芳香性分析示例

> Multiwfn manual, p.990–1005.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.990 -->


请注意，主功能24的子功能1解析出的γ张量对应的是输入取向（与之相反，解析出的α和β对应的是标准取向），因此，载入到VMD中的分子结构文件也必须对应输入取向，否则单位球表示图可能会产生误导。为了得到对应输入取向的.pdb文件，我们将`settings.ini`中的“iloadGaugeom”改为1，然后重新启动Multiwfn并输入

!!! terminal "Multiwfn 交互"

    - **examples\polar\C18\gamma.out** — 将从该文件载入输入取向下的几何结构
    - **100** — 其他功能（第一部分）(Other function (Part 1))
    - **2** — 生成新文件(Generate new file)
    - **1** — 将当前几何结构导出为.pdb文件(Export current geometry as .pdb file) C18.pdb 将C18.pdb载入VMD并以CPK风格显示，你将看到下图

该图的特点与α图相似。从着色的小箭头可以看出，平行于环面同时施加的三个电场的组合效应可以在相同方向上诱导出相对较强的偶极矩变化，而在垂直于环面的方向上这种现象则弱得多。

从矢量表示，即从沿X、Y和Z轴的三个双向大箭头的长度

可以更好地识别γ在三个方向上的相对大小。由于青色箭头相当短，Z方向的γ相对可以忽略。

## 4.25 电子离域与芳香性分析示例

一些芳香性分析示例如下，而Multiwfn中的大多数电子离域与芳香性分析在其它节中有说明，概述见第4.A.3节。

### 4.25.3 研究苯的等化学屏蔽表面（ICSS）和磁屏蔽分布

等化学屏蔽表面（ICSS）表示磁屏蔽值的等值面，它

![](../imgs/p990_505.png)

<!-- p.991 -->


给出了关于芳香性的直观图像。如果你熟悉NICS，你也可以简单地把ICSS看作符号反转后的NICS等值面。更多信息请参见第3.28.3节。在本例中我们将研究苯。由于这是一个平面体系，我们将绘制ICSSZZ而不是ICSS，也就是说只考虑垂直于分子平面的磁屏蔽张量分量。ICSSZZ一定比ICSS具有更明确的物理意义，就像NICSZZ是比NICS更好的芳香性指标一样（如Org. Lett., 8, 863 (2006)所证明）。同时我还将展示如何绘制沿一条直线和在一个平面内的磁屏蔽值。

据我所知，ICSSZZ是我在Multiwfn中实现ICSS期间首次提出的。因此，如果你的工作中涉及ICSSZZ，请引用我包含ICSSZZ分析的研究工作：Carbon, 165, 468 (2020)。

你应首先为当前体系准备一个标准的Gaussian单点任务输入文件，它将作为后续的模板输入文件。该文件已作为examples\ICSS\benzene.gjf提供，其中几何结构已在合理水平下优化过。

启动Multiwfn并输入以下命令 examples\ICSS\benzene.gjf // 注意分子平面在XY平面内 25 // 电子离域与芳香性分析(Electron delocalization and aromaticity analyses) 3 // 生成ICSS或相关量的格点数据(Generate grid data of ICSS or related quantities) 1 // 低质量格点，后续将由Gaussian计算130910个点处的磁屏蔽张量。使用“中等质量格点”可以得到更光滑的图，但计算会昂贵得多。注意默认的外延距离是12 Bohr，这通常已经足够大

n // 不要跳过生成Gaussian输入文件的步骤，因为这是我们第一次进行分析，因此目前手头还没有Gaussian输入/输出文件

现在Multiwfn在当前文件夹中基于模板文件生成了大量NMR任务的Gaussian输入文件。文件命名为NICS0001.gjf、NICS0002.gjf ... NICS0017.gjf。用Gaussian运行这些文件，必须首先运行NICS0001.gjf。输出文件可直接从此处下载：http://sobereva.com/multiwfn/extrafiles/benzene_ICSS.rar。

注：如果这些文件无法被你的Gaussian正常运行，请检查输出文件的尾部，常见原因有两个：

(1) %mem太小导致任务无法完成，你需要在模板.gjf文件中将%mem设为较大值后重试。

(2) `settings.ini`中的“NICSnptlim”太大，你应适当减小它后再试。原因是Gaussian中对Bq原子数目有限制，且某种程度上取决于Gaussian版本和你的计算机。对于G09 D.01和E.01，你应添加“guess=huckel”关键词，否则由于内存分配bug，必须把NICSnptlim减小到很小的值才能使Gaussian正常运行（在这种情况下总计算代价会相当高）。如果使用“guess=huckel”时在Link401报错，则改用“guess=core”。对于G16，不需要guess关键词。

提示：你可以利用脚本“examples\runall.sh”（用于Linux）或“examples\runall.bat”（用于Windows），它调用Gaussian运行当前文件夹中的所有.gjf文件，生成同名但后缀为.out的输出文件。

假设输出文件（NICS0001.out、NICS0002.out...）已放在“C:\benzene”文件夹中，在Multiwfn中你应输入C:\benzene\NICS。我们想先研究ICSSZZ，因此选择“5: ZZ分量”，然后Multiwfn载入所有Gaussian输出文件并将磁屏蔽张量转换为ICSSZZ格点数据。之后你将看到一个新菜单，你可以直接通过选项1可视化格点数据的等值面，通过选项2将其导出为cube文件，或通过选项-1重新选择ICSS的形式。ICSSZZ = 2.0 ppm的等值面如下所示

<!-- p.992 -->


如你所见，绿色等值面（Z分量屏蔽值为正）完全覆盖了苯环上方和下方的区域，表明由于源自全局离域π电子的诱导环电流，Z方向外磁场在这些区域中被大幅屏蔽，该现象意味着苯具有强芳香性。从下面的示意图我们可以更深入地理解ICSSZZ；在垂直于苯并穿过苯的圆柱形区域内，诱导磁场的方向（紫色箭头）恰好与外磁场（B0）相反，这就是为什么该区域Z分量磁屏蔽值很大的原因。

你还可以看到，蓝色等值面（Z分量屏蔽值为负）出现在苯的外侧区域，表现出退屏蔽效应。这主要是因为诱导磁场与B0平行，从而增强了该区域的B0。

如果你适当旋转视角，你会清楚地发现C-H键也被绿色表面完全覆盖。原因是参与C-H成键的σ电子形成显著的局域诱导环电流，因此C-H键周围的外磁场也被强烈屏蔽。

如果你想将当前格点数据导出为.cub文件，以便用VMD等第三方软件可视化，你可以关闭GUI窗口并选择2，将格点数据导出到当前文件夹的ICSSZZ.cub中。

基于已有的Gaussian输出文件直接研究ICSS 假设你已经获得了用于ICSS目的的Gaussian输出文件，并且你想直接研究ICSS，你应在启动Multiwfn后输入以下命令：

!!! terminal "Multiwfn 交互"

    - **examples\ICSS\benzene.gjf 25** — 电子离域与芳香性分析(Electron delocalization and aromaticity analyses)
    - **3** — 生成ICSS或相关量的格点数据(Generate grid data of ICSS or related quantities)
    - **1** — 低质量格点(Low-quality grid) y

![](../imgs/p992_506.png)

![](../imgs/p992_507.png)

<!-- p.993 -->


5 // 研究ICSSZZ(Study ICSSZZ) 如你所见，这次我们采用的格点设置与我们之前用来生成Gaussian输入/输出文件时完全相同，这一点极其重要。如果格点设置不相同，文件载入必定失败。

绘制磁屏蔽值的平面图 注意：如果你只对平面图感兴趣，强烈建议使用主功能25的子功能14来实现该目的，它要方便得多，且计算代价比计算三维ICSS格点数据低得多。关于如何简便绘制NICS-2D平面图，见第4.25.14节。注意NICS和ICSS仅差一个符号。

接下来，我将展示如何绘制一个平面内的磁屏蔽值。由于我们手头已有ICSSZZ格点数据，基于格点数据利用插值技术可以很容易地得到任意直线/平面上各点的磁屏蔽值。

我们首先绘制X=0的YZ平面内的ICSSZZ填充色图。该平面垂直于苯并经过C4-H10和C1-H7。将`settings.ini`中的“iuserfunc”设为-3，然后启动一个新的Multiwfn实例并输入以下命令

ICSSZZ.cub 4 // 绘制平面图(Plot plane map) 100 // 用户自定义函数(User-defined function)，此时对应通过B样条算法对ICSSZZ.cub格点数据插值得到的函数

!!! terminal "Multiwfn 交互"

    - **1** — 填充色图(Color-filled map) [按回车键]
    - **0** — 设置图的扩展距离(Set extension distance of the plot)
    - **8** — 8 Bohr 3

X=0 现在图形弹出，关闭它然后输入 4 // 显示原子标签(Show atom labels) 3 // 蓝色(Blue) 1 // 改变色标上下限(Change lower and upper limit of color scale) -60,60 2 // 显示等值线(Enable showing contour lines) -2 // 设置X、Y和色标轴的标签间隔(Set label interval in X, Y and color scale axes) 3,3,10 19 // 设置颜色过渡(Set color transition) 8 // 蓝-白-红(Blue-White-Red) -1 // 重新绘制(Replot the map) 现在你可以看到下图

<!-- p.994 -->


从图中可以发现，尽管苯中心处Z分量磁屏蔽为正值，但其大小远小于环平面上方和下方区域的值。原因很清楚，即苯只有π芳香性，而其σ电子并未全局离域形成σ芳香性，因此由于缺乏σ环电流的形成，平面内的屏蔽效应相对较弱。

磁屏蔽值的曲线图 注意：如果你只对曲线图感兴趣，强烈建议使用主功能25的子功能13来实现该目的，它要方便得多，且计算代价比计算三维ICSS格点数据低得多。关于如何简便绘制NICS曲线图，见第4.25.13节。

接下来，我们绘制曲线图来研究从环中心出发垂直于环平面直线上的磁屏蔽变化。选择-5返回主菜单并输入

!!! terminal "Multiwfn 交互"

    - **3** — 绘制曲线图(Plot curve map)
    - **100** — 用户自定义函数(User-defined function)
    - **2** — 输入两点坐标定义一条直线(Input coordinate of two points to define a line)
    - **0,0,-8,0,0,8** — 直线从环中心下方和上方8 Bohr处起止 你将立即看到

![](../imgs/p994_508.png)

![](../imgs/p994_509.png)

<!-- p.995 -->


可以看到，Z分量磁屏蔽的最大值出现在环平面上方/下方约1.8 Bohr处。如果你选择“6 寻找局域极小和极大值(Find the positions of local minimum and maximum)”，你将看到

```text
Maximum X (Bohr):    6.122667  Value:    0.28936394E+02
Minimum X (Bohr):    8.000000  Value:    0.13254245E+02
Maximum X (Bohr):    9.882667  Value:    0.28937419E+02
```

即沿该直线ICSSZZ的最大值为28.9 ppm，其位置在环平面上方/下方9.88-8=1.88 Bohr（0.995 Å）处。而在环中心处，ICSSZZ仅为13.2 ppm。

请注意，由于计算ICSSZZ格点数据时使用的外延距离仅为12 Bohr，当我们基于ICSSZZ插值数据绘制曲线或平面图时，图中涉及的空间范围不应太大。例如，我们不能绘制从(0,0,0)到(0,0,20)的曲线图。如果某点超出格点数据插值的有效空间范围，该处的值将为0。

基于ICSSZZ数据计算NICS(0)ZZ和NICS(1)ZZ 值得注意的是，如果你已有ICSSZZ格点数据，你可以直接获得流行的NICS(0)ZZ和NICS(1)ZZ指标，而无需做任何额外计算，因为任意点处的NICS值可通过ICSSzz格点数据的插值直接得到。作为例子，我们计算NICS(1)ZZ。由于上述原因，确保`settings.ini`中的“iuserfunc”已设为-3，然后启动Multiwfn并输入

!!! terminal "Multiwfn 交互"

    - **ICSSZZ.cub 1** — 计算一点处的函数值(Calculate function values at a point)
    - **0,0,1** — 环中心上方1 Å处的点(The point 1 Å above the ring center)
    - **2** — 输入的位置单位为Å(The inputted position is in Å) 从屏幕上你可以发现“用户自定义实空间函数(User-defined real space function)”值为28.9，即NICS(1)ZZ为-28.9 ppm。

结语 ICSS/ICSSZZ确实是讨论芳香性和反芳香性的非常有用的方法，许多实例可在ICSS原始论文（J. Chem. Soc. Perkin Trans. 2, 2001, 1893）以及一些应用论文中找到，如J. Phys. Chem. C, 123, 18593 (2019)以及我关于环[18]碳的研究，Carbon, 165, 468 (2020)。

我强烈建议你多做一些关于绘制和分析ICSS/ICSSZZ的练习，我在“examples\ICSS”文件夹中提供了一些理想的练习体系，包括薁、环丁二烯、环庚三烯、卟啉、丙烷和苝；其中环丁二烯是最简单的一个。下面是环丁二烯ICSS = 0.5等值面以两种风格显示的图；从图中可以清楚地看出该体系表现出强反芳香性特征，4n个π电子在垂直于环并穿过环的圆柱形区域内引起明显的退屏蔽效应，该情形与苯完全相反。

<!-- p.996 -->


我就ICSS写过一篇非常详细的博文，其中涉及“examples\ICSS”文件夹中的所有体系，见我的博客文章“使用Multiwfn研究芳香性：绘制等化学屏蔽表面”（中文，http://sobereva.com/216）。

### 4.25.6 计算菲的HOMA和Bird芳香性指数

HOMA是基于几何均等化最常用的芳香性指数，详见第3.28.6节。这里我们用HOMA研究菲的哪个环具有更强的芳香性。

由于HOMA计算只需要分子坐标，你可以直接使用如.pdb和.xyz作为输入文件。当然，其它包含分子坐标的文件，如.wfn和.fch文件也是可以的。本例中的几何结构是在B3LYP/6-31G*水平下优化的。

启动Multiwfn并输入以下命令 examples/phenanthrene.pdb 25 // 电子离域与芳香性分析(Electron delocalization and aromaticity analyses) 6 // 计算HOMA和Bird芳香性指数(Calculate HOMA and Bird aromaticity index) 0 // 开始计算(Start the calculation) 你将看到打印出默认参数，它们取自J. Chem. Inf. Comput. Sci., 33, 70 (1993)，你也可以在计算前通过选项1自行修改这些参数。

现在我们输入我们感兴趣的环中的原子序号，我们先计算中心环的HOMA，因此输入3,4,8,9,10,7，输入顺序必须与原子连接顺序一致。你将立即得到如下所示的结果

```text
        Atom pair         Contribution  Bond length(Angstrom)
   3(C )  --    4(C ):      -0.065698        1.427111
```

![](../imgs/p996_510.png)

![](../imgs/p996_511.png)

<!-- p.997 -->


```text
   4(C )  --    8(C ):      -0.210455        1.458000
   8(C )  --    9(C ):      -0.065698        1.427111
   9(C )  --   10(C ):      -0.096016        1.435282
  10(C )  --    7(C ):      -0.033673        1.360000
   7(C )  --    3(C ):      -0.096016        1.435282
HOMA value is    0.432442
```

显然，C4-C8与理想键长1.388偏离最显著，对HOMA给出大的负贡献，换句话说，显著破坏了芳香性。HOMA值计算为1加上环中所有键的贡献之和。

然后输入8,15,14,13,11,9计算边缘环的HOMA，结果为0.855126。由于该值比中心环的值更接近1，HOMA表明两个边缘环具有更强的芳香性。

Bird指数是另一个用于衡量芳香性程度的量，简述见第3.28.6节。现在选择选项2计算两个环的Bird指数，你会发现边缘环的值比中心环更接近100。同样，Bird指数也表明两个边缘环具有更强的芳香性。

### 4.25.13 绘制一维NICS曲线、计算积分（INICS）和FiPC-NICS的示例

注：本节的中文版是我的博客文章“使用Multiwfn绘制一维NICS曲线并通过其积分衡量芳香性”（http://sobereva.com/681），其中还包含更多讨论和例子。

在本节中我将说明如何绘制NICS曲线并计算其积分（INICS指标）以及FiPC-NICS指标来研究芳香性。请先阅读第3.28.13节以获得一些基础知识。

### 4.25.13.1 例1：无限烯（infinitene）的NICSZZ曲线

在PBE0/6-31G*水平下优化的无限烯分子是examples\NICS_scan\infinitene.pdb，如下所示（给出两个视角）。在本例中我们将对高亮显示的环进行NICSZZ扫描。扫描方向为从该环的几何中心出发，沿垂直于拟合环平面指向体系外侧的方向。

启动Multiwfn并输入以下命令 examples\NICS_scan\infinitene.pdb //你也可以使用任何其它包含结构信息的文件格式，下同

![](../imgs/p997_512.png)

<!-- p.998 -->


25 //电子离域与芳香性分析(Electron delocalization and aromaticity analyses) 13 //NICS一维扫描曲线图、积分NICS（INICS）和FiPC-NICS(NICS-1D scan curve map, integral NICS (INICS) and FiPC-NICS) 2 //扫描线的两个端点在特定原子拟合平面的中心上方和下方，且直线垂直穿过其中心(The two end points of scanning line are above and below the center of a plane fitted for specific atoms, and the line perpendicularly passes through their center)

35-37,68-69,71 //使用这些原子（上图中高亮显示）定义拟合平面(Using these atoms to define a fitting plane) [直接按回车键] //中心选为所选原子的几何中心(The center is chosen as geometric center of the selected atoms)（在这一步你也可以输入其它类型的中心坐标，如通过Multiwfn拓扑分析模块得到的环临界点）

10 //扫描线的一个端点在拟合平面上方距中心10 Å处(An end point of the scanning line is above 10 Å of the fitting plane from the center) 0 //另一个端点在拟合平面下方距中心0 Å处(Another end point is below 0 Å of the fitting plane from the center)，即扫描将从环中心开始

[直接按回车键] //使用推荐的扫描点数（本例中为100个点），对应步长约为0.1 Å(Using recommended number of scanning points)

1 //生成用于NICS一维扫描的Gaussian输入文件(Generate Gaussian input file for NICS-1D scanning) examples\NICS_scan\template_NMR.gjf //Gaussian的NMR任务模板输入文件(Template input file of NMR task of Gaussian)，用于生成NICS一维扫描的Gaussian输入文件。该文件中的[geometry]行将被扫描点的坐标替换，其它部分保持不变

现在当前文件夹中已生成NICS_1D.gjf。你可以将其载入GaussView以可视化扫描点，见下图。紫色球为Bq原子，在NMR任务中将计算其磁屏蔽张量。可以看到所有Bq原子均匀地分布在预期的扫描线上。

为降低代价，手动将NICS_1D.gjf中的基组改为6-31G*。然后用Gaussian运行它。相应的输入和输出文件已作为“examples\NICS_1D”文件夹中的infinitene_NICS_1D.gjf和infinitene_NICS_1D.out提供。

接下来，在Multiwfn窗口中输入 2 //载入NICS一维扫描的Gaussian输出文件(Load Gaussian output file of NICS-1D scanning) examples\NICS_scan\infinitene_NICS_1D.out //Gaussian输出文件(Gaussian output file) 然后出现一个新界面，选项都是自明的。一个值得注意的选项是-1，从中你可以选择要研究的NICS分量。默认使用垂直于拟合平面的分量，它在表征芳香性方面最有意义。我们将它称为

![](../imgs/p998_513.png)

<!-- p.999 -->


NICSZZ，假设Z为拟合平面法线方向。

现在选择选项1绘制NICS曲线（当前对应NICSZZ），你将看到如下图（在选择该选项前选择一次选项-3可将图水平翻转）

可以看到该环是芳香性的，因为NICSZZ明显为负，尤其在距环中心1 Å处。

从屏幕上你还可以找到曲线的积分：

```text
Integral of NICS component:    -96.19 ppm*Angstrom
```

此外，你可以选择选项5获得曲线的极值：

```text
Minimum X (Angstrom):    1.111111  Value:   -0.29469963E+02
Totally found    1 minima,    0 maxima
```

### 4.25.13.2 例2：苯的NICSsigma,ZZ和NICSpi,ZZ曲线

在本例中，我们将绘制苯的分别由σ和π电子贡献的NICSZZ曲线，即NICSσ,ZZ和NICSπ,ZZ。要绘制NICSπ,ZZ，在启动Multiwfn后输入以下命令。

examples\NICS_scan\benzene.pdb //在B3LYP/6-31G*水平下优化的苯，分子位于Z=0的XY平面上(Benzene optimized at B3LYP/6-31G* level, the molecule is lying at XY plane of Z=0)

25 //电子离域与芳香性分析(Electron delocalization and aromaticity analyses) 13 //NICS一维扫描曲线图、积分NICS（INICS）和FiPC-NICS(NICS-1D scan curve map, integral NICS (INICS) and FiPC-NICS) 2 //扫描线的两个端点在特定原子拟合平面的中心上方和下方，且直线垂直穿过其中心(The two end points of scanning line are above and below the center of a plane fitted for specific atoms, and the line perpendicularly passes through their center)

1-6 //使用该体系中所有碳原子定义拟合平面(Using all carbon atoms in this system to define a fitting plane) [直接按回车键] //中心选为所选原子的几何中心(The center is chosen as geometric center of the selected atoms) 10 //扫描线的一个端点在拟合平面上方距中心10 Å处(An end point of the scanning line is above 10 Å of the fitting plane from the center) 10 //另一个端点在拟合平面下方距中心10 Å处(Another end point is below 10 Å of the fitting plane from the center) [直接按回车键] //使用推荐的扫描点数（本例中为200个点）(Using recommended number of scanning points)

1 //生成用于NICS一维扫描的Gaussian输入文件(Generate Gaussian input file for NICS-1D scanning)

![](../imgs/p999_514.png)

<!-- p.1000 -->


examples\NICS_scan\template_NMR_benzene-pi.gjf //Gaussian模板文件(Gaussian template file) 这次使用的模板文件内容如下，它要求Gaussian只计算由MO 17,20,21（当前水平下苯的π-MO）贡献的磁屏蔽信息。关键词nmr=csgt iop(10/93=2)必须存在。AICD.txt是由该IOp生成的文件，在此情形下完全无用，运行后可直接删除。

```text
#p b3lyp/6-31+G* nmr=csgt iop(10/93=2)

template file

  0  1
[geometry]

AICD.txt

17,20,21
```

用Gaussian运行在当前文件夹中生成的NICS_1D.gjf。输出文件已作为examples\NICS_scan\benzene-pi_NICS_1D.out提供。

接下来，在Multiwfn窗口中输入 2 //载入NICS一维扫描的Gaussian输出文件(Load Gaussian output file of NICS-1D scanning) examples\NICS_scan\benzene-pi_NICS_1D.out //Gaussian输出文件(Gaussian output file)

1 //绘制NICS曲线图(Plot NICS curve map)，在当前情形下对应NICSπ,ZZ 现在你可以看到下图。X=0对应环中心位置。

你可以用几乎完全相同的方式绘制NICSσ,ZZ，唯一区别是在模板文件中应指定σ MO的序号。相应的模板文件是examples\NICS_scan\template_NMR_benzene-sigma.gjf。

在“examples\NICS_scan\”文件夹中，C5H5-.pdb和C7H7+.pdb分别是优化过的C5H5−和C7H7+离子。你可以用与上面所示相同的方式得到它们的NICSσ,ZZ和

![](../imgs/p1000_515.png)

<!-- p.1001 -->


NICSπ,ZZ曲线，相关文件也已在该文件夹中提供。注意在界面中，你可以选择选项“3 沿直线导出NICS曲线数据(Export NICS curve data along the line)”将曲线数据导出为纯文本文件。然后，在将不同情形的曲线数据导入如Origin后，你可以将它们绘制在一起，如下所示。

可以看到σ电子对环中心附近的NICSZZ有相当大的影响。根据NICSπ,ZZ曲线，所有三个体系都显示出相当的π芳香性。然而，它们的差异可从其积分定量确定。苯、C5H5−和C7H7+的NICSπ,ZZ积分分别为-142.45、-134.85和-145.02 ppm·Å，表明π芳香性强弱顺序为C7H7+ ≥ 苯 > C5H5−。

### 4.25.13.3 例3：计算苯的FiPC-NICS指数

注：关于FiPC-NICS的更多讨论见我的博客文章“使用Multiwfn计算FiPC-NICS芳香性指数”（http://sobereva.com/724，中文）。

在主功能25的子功能13的后处理菜单中，可以直接计算FiPC-NICS芳香性指数，下面以苯为例说明。如果你不熟悉它，请查看第3.28.13节。

启动Multiwfn并输入 examples\NICS_scan\benzene.pdb //在B3LYP/6-31G*水平下优化的苯，分子位于Z=0的XY平面上(Benzene optimized at B3LYP/6-31G* level, the molecule is lying at XY plane of Z=0)

25 //电子离域与芳香性分析(Electron delocalization and aromaticity analyses) 13 //NICS一维扫描曲线图、积分NICS（INICS）和FiPC-NICS(NICS-1D scan curve map, integral NICS (INICS) and FiPC-NICS) 2 //扫描线的两个端点在特定原子拟合平面的中心上方和下方，且直线垂直穿过其中心(The two end points of scanning line are above and below the center of a plane fitted for specific atoms, and the line perpendicularly passes through their center)

1-6 //使用该体系中所有碳原子定义拟合平面(Using all carbon atoms in this system to define a fitting plane) [直接按回车键] //中心选为所选原子的几何中心(The center is chosen as geometric center of the selected atoms) 0 //扫描线的一个端点距中心0 Å(An end point of the scanning line is 0 Å from the center) 10 //另一个端点距中心10 Å(Another end point is 10 Å from the center) 200 //NICS扫描使用200个点(200 points used in NICS scan)

![](../imgs/p1001_516.png)

<!-- p.1002 -->


1 // 生成用于NICS一维扫描的Gaussian输入文件(Generate Gaussian input file for NICS-1D scanning) examples\NICS_scan\template_NMR.gjf //对应B3LYP/6-31+G*水平NMR计算的Gaussian模板文件(Gaussian template file corresponding NMR calculation at B3LYP/6-31+G* level)

现在当前文件夹中已生成NICS_1D.gjf，将其重命名为benzene_NICS_1D_0to10.gjf并用Gaussian运行它。输出文件已提供。接下来，我们输入

2 // 载入NICS一维扫描的Gaussian输出文件(Load Gaussian output file of NICS-1D scanning) examples\NICS_scan\benzene_NICS_1D_0to10.out //Gaussian输出文件(Gaussian output file) 6 //计算FiPC-NICS(Calculate FiPC-NICS) 你将立即看到结果：

```text
FiPC-NICS is   -9.332247 ppm, at   1.179 Angstrom
```

结果表明，在苯环中心上方1.179 Å处，NICS的面内分量（NICSin）消失，而面外分量（NICSout）为-9.33 ppm。该结果与FiPC-NICS原始论文中的相应数据（在1.18 Å处为-9.59 ppm）非常接近，该论文中几何优化和NMR计算使用PBE0/6-311++G**。

Multiwfn还在当前文件夹中导出了FiPC-NICS.txt，各列含义在屏幕上清楚显示。该文件包含所有扫描点的信息。你可以取最后两列，即NICSin和NICSout，分别作为X轴和Y轴绘制散点+连线图。所得图如下所示，与FiPC-NICS原始论文的图1非常一致。

### 4.25.14 绘制二维NICS平面图的示例

注：本节的中文版是我的博客文章“使用Multiwfn简便绘制二维NICS平面图考察芳香性”（http://sobereva.com/682），其中还包含更多讨论和例子。

在本节中我将说明如何绘制NICS平面图。请先阅读第3.28.14节以获得一些基础知识。注意下面例子中的NICSZZ指垂直于所关注平面的NICS分量，Z并不总对应Z轴。

### 4.25.14.1 绘制晕苯上方1 Å处的NICSZZ平面图

在本例中我们绘制晕苯上方1 Å处的填充色NICSZZ平面图，晕苯

![](../imgs/p1002_517.png)

<!-- p.1003 -->


在B3LYP/6-31G*水平下优化的结构是examples\NICS_scan\coronene.pdb。分子恰好为平面并位于Z=0的XY平面上。

启动Multiwfn并输入以下命令 examples\NICS_scan\coronene.pdb 25 //电子离域与芳香性分析(Electron delocalization and aromaticity analyses) 14 //NICS二维扫描平面图(NICS-2D scan plane map) 1 //填充色图(Color-filled map) [直接按回车键] //使用默认格点数（100*100）(Using default number of grid points) 0 //设置外延距离(Set extension distance) 1 // 1 Bohr 1 //XY平面(XY plane) 1a //Z = 1Å 1 //用于NICS二维扫描的Gaussian输入文件(Gaussian input file for NICS-2D scanning) examples\NICS_scan\template_NMR.gjf //Gaussian的NMR任务模板输入文件(Template input file of NMR task of Gaussian)，用于生成NICS二维扫描的Gaussian输入文件。该文件中的[geometry]行将被扫描点的坐标替换，其它部分保持不变

当前文件夹中已生成NICS_2D.gjf，你可根据实际情况适当修改它。用Gaussian运行它，输出文件是examples\NICS_scan\coronene_NICS_2D.out。

接下来，在Multiwfn窗口中输入 2 //载入NICS二维扫描的Gaussian输出文件(Load Gaussian output file of NICS-2D scanning) examples\NICS_scan\coronene_NICS_2D.out 5 //取ZZ笛卡尔分量(Taking ZZ Cartesian component)。由于分子恰好在XY平面内，所得NICS将对应通常意义的NICSZZ（即垂直于环平面的分量）

从屏幕上你可以找到该平面内NICSZZ的最小值和最大值：

```text
The minimum of data:  -43.3034000000000
The maximum of data:   11.3487000000000
```

关闭屏幕上显示的图，然后输入以下命令微调绘图设置

4 //显示原子标签(Enable showing atom labels) 1 //红色(Red) 8 //显示化学键(Enable showing bonds) 14 //棕色(Brown) 17 //设置显示原子标签的距离阈值(Set distance threshold for showing atom labels) 5 //5 Bohr y //以浅色字体显示超出阈值的原子的标签(Show labels of the atoms that beyond the threshold by light font) 1 //设置色标上下限(Set lower&upper limit of color scale) -45,45 -8 //将图的长度单位改为Angstrom(Change length unit of the graph to Angstrom) -2 //设置X、Y和色标轴的标签间隔(Set label intervals in X, Y, and color scale axes) 2,2,10 2 //显示等值线(Enable showing contour lines) 3 //改变等值线设置(Change contour line setting) 8 //按等差数列生成等值线值(Generate contour value by arithmetic progression) -50,5,21 //起始值、步长和总数(Starting value, step, and total number)

<!-- p.1004 -->


y //删除已有的等值线(Removing existing contour lines)。然后等值线值将为-50,-45,-40...40,45,50 1 //保存设置并返回(Save setting and return) -1 //重新绘制(Replot) 现在你得到下图。从中可以清楚地看出外圈环比内圈环具有更强的芳香性，因为前者上方1 Å处的NICSZZ明显比后者更负。

### 4.25.14.2 绘制N(phenyl)3中一个苯环上方1 Å处的NICSZZ平面图

在本例中，我们将绘制下面所示N(phenyl)3中高亮环上方1 Å处的NICSZZ平面图。由于该环相对笛卡尔轴是倾斜的，我们将用一种特殊方式定义绘图平面。

启动Multiwfn并输入以下命令 examples\NICS_scan\N(phenyl)3.pdb //在B3LYP/6-31G*水平下优化的结构(Structure optimized at B3LYP/6-31G* level) 25 //电子离域与芳香性分析(Electron delocalization and aromaticity analyses) 14 //NICS二维扫描平面图(NICS-2D scan plane map)

![](../imgs/p1004_518.png)

![](../imgs/p1004_519.png)

<!-- p.1005 -->


1 //填充色图(Color-filled map) [直接按回车键] //使用默认格点数（100*100）(Using default number of grid points) 8 //绘图平面在特定原子组成平面的上方或下方(The plotting plane is above or below the plane consisting of specific atoms) 23,24,26,30,28,25 //感兴趣环中的原子(Atoms in the ring of interest) 注意屏幕上显示了所选原子拟合平面的法向单位矢量，请记录它，稍后会用到：

```text
The unit normal vector is    0.33076524    0.57300118    0.74984265
```

1 //绘图平面平行于拟合平面且在其上方1 Å处(The plotting plane is parallel to the fitting plane and at 1 Å above it)。负值表示在其下方

6 //绘图平面（正方形区域）边长设为6 Å(Length of the plotting plane (a square region) is set to 6 Å) 现在你可以在屏幕上找到以下信息：

```text
draw triangle {   2.495   2.581  -1.739} {  -1.211  -0.235   2.047} {   6.776  -1.451  -0.547}
draw triangle {  -1.211  -0.235   2.047} {   6.776  -1.451  -0.547} {   3.070  -4.266   3.239}
draw material Transparent
```

如果你将N(phenyl)3.pdb载入VMD，然后在VMD控制台窗口中运行上述三条命令，再适当调整图形表示，你将看到下图，它说明了绘图平面对应的区域。可以看到绘图平面已被正确定义。

接下来，输入以下命令 1 //生成用于NICS二维扫描的Gaussian输入文件(Generate Gaussian input file for NICS-2D scanning) examples\NICS_scan\template_NMR.gjf //用于NMR任务的Gaussian模板文件(Template file of Gaussian for NMR task) 现在当前文件夹中已生成NICS_2D.gjf，手动编辑它将基组改为6-31G*，然后用Gaussian运行它。输出文件已作为examples\NICS_scan\N(phenyl)3_NICS_2D.out提供。

然后在Multiwfn窗口中输入 2 //载入NICS二维扫描的Gaussian输出文件(Load Gaussian output file of NICS-2D scanning) examples\NICS_scan\N(phenyl)3_NICS_2D.out 0 //取特定方向的NICS分量(Take the NICS component along specific direction) 0.33076524 0.57300118 0.74984265 //前面Multiwfn显示的法向单位矢量(The unit normal vector shown by Multiwfn earlier) 现在NICSZZ平面图已显示在屏幕上。关闭它并适当调整绘图设置（参见第4.4节中的丰富例子），最终你可以得到如下所示的图，它相当漂亮。注意颜色过渡已设为黄-橙-黑(Yellow-Orange-Black)，

![](../imgs/p1005_520.png)
