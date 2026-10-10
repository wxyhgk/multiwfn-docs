# 分子表面的定量分析

> Multiwfn manual, p.694–730.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.694 -->




```text
alid range:
RGB (0-1):    1.000000  0.953110  0.026876
RGB (0-255):   255   243     7
RGB of complementary color:     0    12   248
RGB of original color (maximum brightness):        255   243     7
RGB of complementary color (maximum brightness):     7    19   255
```

### 4.11.14.2 基于实验紫外-可见

光谱预测诱惑红的颜色

examples\spectra\Allura_red_UV-Vis.txt 是著名染料诱惑红的实验紫外-可见光谱的 X-Y 曲线数据。在本例中我们基于该光谱预测诱惑红的颜色。

启动 Multiwfn 并载入 examples\spectra\Allura_red_UV-Vis.txt，然后输入

!!! terminal "Multiwfn 交互"

    - **11** — 绘制光谱 (Plotting spectrum)
    - **0** — 基于文本文件中记录的紫外-可见光谱预测颜色 (Predicting color based on UV-Vis spectrum recorded in text file) 此时你可以在屏幕上看到如下图

从左下角显示的颜色可以看出，诱惑红的颜色为红色，这正是该物质实际观察到的颜色。该图还表明诱惑红吸收青色光。


## 4.12 分子表面的定量分析


### 4.12.1 苯酚分子表面上的静电势分析

下面我将以苯酚为例介绍分子表面的定量分析。理论基础已在 3.15.1 节记载，此处不再重复。在本节中我们仅分析苯酚 vdW 表面上的静电势（ESP），在下一节中我们将分析苯酚表面上的平均局部电离能。

启动 Multiwfn 并输入以下命令 examples\phenol_631Gxx.wfn // 在 B3PW91/6-31G** 水平下产生的苯酚波函数。对大多数体系，该水平可给出可接受的 ESP 分析结果。为获得更好精度，推荐 def-TZVP，而更昂贵的 def2-TZVP 基组能给出理想结果


![](../imgs/p694_244.png)

<!-- p.695 -->



!!! terminal "Multiwfn 交互"

    - **12** — 分子表面的定量分析 (Quantitative analysis of molecular surface)
    - **0** — 在默认设置下开始分析。默认情况下，被映射的函数为 ESP (Start the analysis under default settings. By default, the mapped function is ESP) 此时计算开始。由于计算 ESP 耗时较长，你需要等待一会儿。在计算过程中会打印一些中间信息，大多数用户无需关注。计算最终完成后屏幕上将打印以下结果：


```text
Global surface minimum: -0.041203 a.u. at   1.455097   3.343708  -0.007902 Ang.
Global surface maximum:  0.085761 a.u. at  -1.936645   3.093464   0.021360 Ang.

Number of surface minima:     3
   #       a.u.         eV      kcal/mol           X/Y/Z coordinate(Angstrom)
     1 -0.03046066   -0.828877  -19.112843       0.150202  -1.011077  -1.882004
     2 -0.03045989   -0.828856  -19.112362       0.192185  -0.985412   1.877656
*    3 -0.04120321   -1.121196  -25.853368       1.455097   3.343708  -0.007902

Number of surface maxima:     5
   #       a.u.         eV      kcal/mol           X/Y/Z coordinate(Angstrom)
     1  0.02275520    0.619200   14.277975      -3.344441  -2.281045   0.047286
*    2  0.08576096    2.333674   53.811572      -1.936645   3.093464   0.021360
     3  0.01935782    0.526753   12.146259       0.066223  -4.286661   0.040555
     4  0.01980285    0.538863   12.425498       3.340574  -2.325727   0.021485
     5  0.01583741    0.430958    9.937340       3.419218   1.225375  -0.019326

      ================= Summary of surface analysis =================
Volume:   835.71041 Bohr^3  ( 123.83953 Angstrom^3)
Overall surface area:         476.05682 Bohr^2  ( 133.30951 Angstrom^2)
Positive surface area:        231.09186 Bohr^2  (  64.71232 Angstrom^2)
Negative surface area:        244.96497 Bohr^2  (  68.59719 Angstrom^2)
Overall average value:   -0.00020233 a.u. (  -0.12695332 kcal/mol)
Positive average value:   0.01877643 a.u. (  11.78145591 kcal/mol)
Negative average value:  -0.01810626 a.u. ( -11.36095315 kcal/mol)
Overall variance (sigma^2_tot):  0.00041488 a.u.^2 ( 163.34165024 (kcal/mol)^2)
Positive variance:        0.00031106 a.u.^2 ( 122.46642148 (kcal/mol)^2)
Negative variance:        0.00010382 a.u.^2 (  40.87522876 (kcal/mol)^2)
Balance of charges (nu):   0.18762182
Product of sigma^2_tot and nu:   0.00007784 a.u.^2 (  30.6464578 (kcal/mol)^2)
Internal charge separation (Pi):   0.01842642 a.u. (  11.56183883 kcal/mol)
Molecular polarity index (MPI):   0.50154872 eV (     11.56600 kcal/mol)
Nonpolar surface area (|ESP| <= 10 kcal/mol):     67.26 Angstrom^2  ( 50.45 %)
Polar surface area (|ESP| > 10 kcal/mol):         66.05 Angstrom^2  ( 49.55 %)
```

上述信息包含与 ESP 相关的各种量，见 3.15.1 节了解其含义和定义。现在在后处理界面中选择选项 0 查看分子结构和表面极值点（红色和蓝色小球分别对应极大值和极小值）：


<!-- p.696 -->



侧视图中：

极小值 3（-25.85 kcal/mol）是表面上的全局最小值，其很大的负值源于氧的孤对电子。极大值 2（53.81 kcal/mol）是源于带正电的 H13 的全局最大值，该点处的 ESP 远大于其他极大值处（其他极大值处的 ESP 为 10 至 15 kcal/mol）。这是由于氧的存在，从 H13 吸引了大量电子。在复合物中，假设仅存在静电相互作用，单体总是以 ESP 互补最大化的方式彼此接触。因此，我们可以预期，在苯酚二聚体中，一个单体中的 H13 和极大值 2，与相邻单体中的 O12 和极小值 3 将位于一条直线上（形成氢键），这正是苯酚二聚体实际几何构型中的情形，见下图。注意在二聚体中，上述极大值 2 和极小值 3 已相互抵消。


![](../imgs/p696_245.png)

![](../imgs/p696_246.png)

<!-- p.697 -->



极小点1和2（均为-19.11 kcal/mol）是该表面上的局域极小点，主要源自环上下方丰富的π电子。众所周知，亲电试剂总是优先进攻周围ESP非常低的原子，因此C1应该是亲电反应的理想反应位点。这一结论与羟基是邻对位定位基的一般常识部分一致。然而，尽管全局极小点最接近O12，O12却不是亲电反应位点；这一矛盾揭示了ESP分析方法固有的局限性。

注1：由于该分子具有Cs对称性，原则上极小点1和2应具有相同的X和Y坐标。然而，在数值计算过程中这无法被严格满足，因为散布在分子表面上的点不具有分子对称性，详见3.15.1节。因此，极小点1和2的X和Y坐标彼此略有偏离。如果您想改进结果，请选择选项3(option 3)“用于生成分子表面的格点数据的间距(Spacing of grid data for generating molecular surface)”，并输入一个比默认值更小的值。更小的格点间距会得到更准确的结果，但会带来更高的计算负担。

注2：由于Multiwfn图形界面的限制，有时很难查询感兴趣的ESP极值点的序号，此时建议改用VMD，见本视频的第6部分 https://youtu.be/QFpDf_GimA0。

注3：也可以在平面图中的特定等值线的等值线(contour line)上绘制ESP极值点，见4.4.12节。

相互穿透距离 在分子中的原子(AIM)理论框架下定义的非键半径，是原子核到ρ=0.001 a.u.等值面之间的最短距离。让我们计算O12和H13的非键半径。在后处理界面(post-processing interface)中选择选项10(option 10)并输入12，可以看到O12的非键半径为1.701 Å。选择10并输入13，H13的非键半径为1.172 Å。在苯酚二聚体中，氢键的H---O距离为1.937 Å，因此所谓的相互穿透距离为1.701+1.172-1.937=0.936 Å。这是一个不可忽略的数值，表明该氢键很强。

分子表面上的ESP统计分布 作为ESP分析的最后一部分，我们考察每个ESP区间内的分子表面积，这有助于定量讨论整个分子表面上的ESP分布。我们在后处理界面(post-processing interface)中选择选项9(option 9)，然后输入：

all // 将所有原子纳入统计（或者，例如若输入2-4，则只计入与原子2、3和4对应的局域表面，局域分子表面的概念见4.12.3节的说明）

-30,55 // 您感兴趣的ESP范围。由于我们已经知道表面上的最小和最大ESP分别为-25.85和53.81 kcal/mol，这里我们输入一个稍大的范围以将其包围


![](../imgs/p697_247.png)

<!-- p.698 -->



!!! terminal "Multiwfn 交互"

    - **15** — 区间数目
    - **3** — 输入和输出单位均为kcal/mol

然后您将看到每个连续ESP区间内的表面积（单位为Å2）及其占整个表面积的百分比。


```text
     Begin        End       Center       Area         %
   -30.0000    -24.3333    -27.1667      1.8192      1.3647
   -24.3333    -18.6667    -21.5000      6.0284      4.5221
   -18.6667    -13.0000    -15.8333     20.9732     15.7327
   -13.0000     -7.3333    -10.1667     19.0390     14.2818
...
    43.6667     49.3333     46.5000      1.2690      0.9519
    49.3333     55.0000     52.1667      1.0457      0.7844
Sum:                                   133.3095    100.0000
```

利用这些数据，您可以用您喜欢的程序绘制直方图。例如，我们选择“center”列作为X轴、“Area”列作为Y轴来绘制下图

28

24

20

Surface area (Å2) 16 12 8

4

-30-20-10010203040500

Electrostatic potential (kcal/mol)

从图中可以看出，有很大一部分分子表面具有较小的ESP值，即从-20到20 kcal/mol。其中，负值部分主要对应六元环上方和下方的表面，显示了丰富的π电子云的效应；正值部分主要源自带正电的C-H氢；近中性部分代表负、正部分之间的边界区域。还有小部分面积具有显著的正、负ESP值，分别对应靠近全局ESP极大点和极小点的区域。

绘制ESP着色的分子表面 借助VMD程序，可以基于Multiwfn的输出绘制非常精美的、带有各种实空间函数表面极值点的颜色填充分子表面图。下面就是这样一幅ESP图，曾展示在笔者关于苯并[a]芘二醇环氧化物的研究中，见Struct. Chem., 25, 1521 (2014)。其中蓝色、白色和红色对应ESP从-30到35


<!-- p.699 -->



kcal/mol的变化，绿色和橙色小球分别对应ESP表面极小点和极大点

如果您想绘制类似的图形，请下载并参照本教程：http://sobereva.com/multiwfn/res/plotESPsurf.pdf。然而，该教程中有很多步骤，如果您想以简单得多的方式绘制效果相近甚至更好的图，见4.A.13节或本视频教程：https://youtu.be/QFpDf_GimA0。该节和视频还说明了如何绘制不同分子的范德华表面穿透图，这对讨论分子间相互作用很有用。

提示：若您的CPU核心数非常有限（少于10核），Gaussian程序包中的cubegen工具计算ESP的速度明显快于Multiwfn。若您的机器上安装了Gaussian且输入文件为.fch/fchk格式，建议将`settings.ini`文件中的“cubegenpath”参数设为cubegen的实际路径，以便Multiwfn在分析过程中自动调用cubegen来计算ESP。详见5.7节。

如果您是ORCA用户，同时又无法使用Gaussian，当CPU核心数非常有限时，可以利用ORCA程序包中的“orca_vpot”工具来尝试降低分子表面ESP分析的开销，详见http://sobereva.com/wfnbbs/viewtopic.php?pid=937。

常见问题：为什么有的表面ESP极小点（极大点）具有正（负）值？一些Multiwfn用户曾问我，为什么他们观察到有的表面ESP极小点（极大点）具有正（负）值。事实上，这种现象非常常见，它绝不是问题或程序错误。在数学上，极小点（极大点）是指其值低于（高于）周围点的点，显然这绝不意味着该点必定具有负（正）值。如果您仍有困惑，请看下面的示意图


![](../imgs/p699_248.png)

<!-- p.700 -->



对于中性体系，通常具有正值（负值）的表面ESP极小点（极大点）在化学上并不重要，您在讨论时可以直接忽略它们。如果您想去掉这些不重要的极小点（极大点），可以在后处理菜单(post-processing menu)中选择选项3(option 3)（选项4(option 4)），然后输入d。然后您会发现这些不需要的极值点已经消失了。

还值得注意的是，对于阳离子（阴离子）体系，通常所有表面极值点都具有正（负）值，因为表面ESP极值点的整体数值总是被体系所带的净电荷强烈主导。

技巧：重复利用上次分析时产生的映射函数数据 这里介绍一个技巧。您可能已经注意到，在范德华表面上计算ESP很耗时，尤其是对使用高质量基组的大体系。如果您已对一个体系做过ESP分析，之后还要再次分析，实际上您可以把ESP数据导出为纯文本文件，以便下次分析同一体系时直接利用导出的数据。对于其它类型的映射函数，该技巧同样适用。

让我们看一个例子。我们先照常在范德华表面上做ESP分析，输入以下命令：

!!! terminal "Multiwfn 交互"

    - **examples\N-phenylpyrrole.fch 12** — 定量分子表面分析(Quantitative molecular surface analysis)
    - **0** — 开始分析(Start the analysis) 计算完成后，选择选项7(option 7)将带ESP值的表面顶点导出为当前文件夹中名为vtx.txt的纯文本文件。之后选择-1返回上一级菜单。

假设我们要再次进行分析。这次我们可以直接使用记录在纯文本文件中的ESP数据。输入以下命令

!!! terminal "Multiwfn 交互"

    - **5** — 在分析过程中从外部文件载入映射函数值(Loading mapped function values from external file during analysis)
    - **1** — 从纯文本文件载入所有表面顶点处的映射函数(Loading mapped function at all surface vertices from a plain text file)
    - **0** — 开始分析(Start the analysis) 在分子表面构建完成后，Multiwfn会提示您输入记录所有表面顶点处映射函数值的纯文本文件的路径，此时您只需输入vtx.txt即可。

由于这次映射函数值即ESP值不是计算得到的，而是直接从vtx.txt载入的，分析结果会立即显示在屏幕上。

技巧：仅基于cube文件在分子表面上做ESP分析 一些量子化学和第一性原理程序，如Quantum ESPRESSO、ADF、


![](../imgs/p700_249.png)

<!-- p.701 -->



Dmol3和FHI-aims，无法产生Multiwfn支持的波函数文件，但在这种情况下，只要您能用这些程序为您的体系生成电子密度和ESP的cube文件，仍然可以在分子表面上做ESP分析。一旦生成了cube文件，启动Multiwfn后输入以下命令即可：

!!! terminal "Multiwfn 交互"

    - **density.cub** — 首先载入电子密度的cube文件(Load cube file of electron density first)
    - **12** — 定量分子表面分析(Quantitative molecular surface analysis)
    - **1** — 选择定义表面的方式(Select the way to define surface)
    - **11** — 内存中格点数据的等值面(Isosurface of the grid data in memory)

!!! terminal "Multiwfn 交互"

    - **0.001** — 用ρ = 0.001 a.u.定义等值面(Use ρ = 0.001 a.u. to define the isosurface)
    - **2** — 选择映射函数(Select mapped function)
    - **1** — ESP 5

映射函数将从外部cube文件插值得到(The mapped function will be interpolated from an external cube file)

!!! terminal "Multiwfn 交互"

    - **0** — 开始计算(Start calculation)
    - **ESP.cub** — 记录ESP的cube文件(The cube file recording ESP)

注意，用于生成density.cub和ESP.cub的格点设置必须完全相同，且格点间距不宜太大（不大于0.25 Bohr），否则分析结果将不准确。


### 4.12.2 苯酚分子表面上的平均局域电离能(ALIE)分析(Average local ionization energy analysis (ALIE) on phenol molecular surface)


下面我们将分析苯酚范德华表面上的平均局域电离能𝐼̅。启动Multiwfn并输入

!!! terminal "Multiwfn 交互"

    - **examples\phenol_631Gxx.wfn** — 在B3PW91/6-31G**水平下产生(Produced at B3PW91/6-31G** level)
    - **12** — 定量分子表面分析(Quantitative molecular surface analysis)
    - **2** — 重新选择映射函数(Reselect mapped function)
    - **2** — 选择𝐼̅作为映射函数(Choose 𝐼̅ as mapped function)
    - **0** — 开始表面分析(Start the surface analysis)。由于𝐼̅的计算比ESP简单得多，计算很快就完成了。与ESP的表面分析不同，此时除极值点信息外，只输出范德华体积、表面积以及范德华表面上𝐼̅的平均值和方差。

选择0以可视化极值点(visualize extrema)。为了使极值点与原子的对应关系更清楚，我们将“原子尺寸比例(Ratio of atomic size)”滑块拖到4.0，这对应范德华表面，并关闭表面极大点的显示，然后我们将看到：


<!-- p.702 -->



侧视图见下图

𝐼̅值低意味着该位置的电子束缚不紧，范德华表面上𝐼̅最低的位点通常被认为是最易受亲电进攻或自由基进攻的位点。所有高极化性的位点，如π电子和孤对电子区域，通常都有相应的表面𝐼̅极小点。在当前例子中，极小点8和9对应O12的孤对电子，从屏幕输出上可发现它们的𝐼̅值均为10.59 eV。极小点4、5、11以及3、7、10对应π电子，它们的𝐼̅值均约为8.9 eV，可视为简并的全局极小点。值得注意的是，共轭环上方和下方的极小点只出现在邻位和对位碳处。这些观察完美地解释了羟基作为邻对位定位基的效应。由于极小点8和9处的𝐼̅明显大于碳环周围极小点处的𝐼̅，氧不应是亲电反应的易反应位点。

绘制平均局域电离能着色的分子表面图 注1：与本部分对应的有视频说明，请观看！https://youtu.be/-1sBa0lKhp8。注2：本部分的中文版是笔者的博客文章“使用Multiwfn和VMD绘制平均局域电离能(ALIE)着色的分子表面图”(http://sobereva.com/514)。

为了更完整地考察分子表面上𝐼̅的分布，最好绘制按𝐼̅着色的分子表面图。这可通过脚本和VMD程序(http://www.ks.uiuc.edu/Research/vmd/)极其容易地实现。下面展示在Windows环境下如何实现，仍以苯酚为例。请依次做以下步骤：


![](../imgs/p702_250.png)

![](../imgs/p702_251.png)

<!-- p.703 -->



- 将"examples\scripts\"中的ALIE.vmd复制到VMD文件夹
- 将"examples\scripts\"文件夹中的ALIE_isoext.bat和ALIE_isoext.txt复制到含有Multiwfn.exe的文件夹

- 编辑ALIE_isoext.bat，将默认输入文件改为examples\phenol_631Gxx.wfn，将VMD文件夹改为您的机器上实际的VMD文件夹

- 双击ALIE_isoext.bat图标执行它。该脚本将调用当前文件夹中的Multiwfn.exe进行一些计算，然后VMD文件夹中会出现avglocion.cub、density.cub和surfanalysis.pdb

- 启动VMD，在控制台窗口中输入source ALIE.vmd，您将立即看到下图（为了获得更好的效果，笔者使用了Tachyon渲染生成图像）

在上图中，显示的表面为ρ = 0.0005 a.u.等值面。不采用常用的ρ = 0.001 a.u.等值面作为表面的定义的原因是，若采用它，则表面上的𝐼̅分布几乎难以区分。青色小球对应𝐼̅的表面极小点。颜色过渡为蓝-白-红，因此蓝色突出显示具有相对低𝐼̅值的区域，那里是有利于亲电进攻的位点。

默认情况下，𝐼̅的颜色标尺为0.32~0.36 a.u.，若您发现颜色标尺对当前体系不合适，可以在VMD控制台窗口中输入例如mol scaleminmax 0 1 0.31 0.38将下限和上限分别改为0.31和0.38。


### 4.12.3 丙烯醛的原子局域分子表面分析(Atomic local molecular surface analysis for acrolein)

众所周知，丙烯醛（见下图）倾向于在羰基

碳和β碳处发生亲核进攻；特别是，前者是硬亲核试剂的主要位点。所谓硬，意味着亲核试剂的电子云难以极化；这种情况下反应位点的选择性通常由ESP主导。


![](../imgs/p703_252.png)

![](../imgs/p703_253.png)

<!-- p.704 -->



在本例中，我们将尝试通过分析其范德华表面上的ESP来解释丙烯醛的位点选择性。注意，平均局域电离能只对研究亲电进攻有用，而对分析亲核进攻完全无用。

!!! terminal "Multiwfn 交互"

    - **启动Multiwfn并输入：examples\acrolein.wfn** — 在B3LYP/6-31G**水平下优化并产生(Optimized and produced at B3LYP/6-31G** level)
    - **12** — 分子表面的定量分析(Quantitative analysis of molecular surface)
    - **0** — 对ESP开始分析(Start the analysis for ESP) 计算完成后，选择0以可视化表面极值点(visualize surface extrema)：

如您所见，在α碳的边界处有一个ESP表面极小点，且它非常靠近β碳。这一观察间接揭示了α碳的核电荷被电子云屏蔽得更重，因而作为亲核进攻位点的可能性较小。然而，对整个丙烯醛表面的ESP定量分析并未对反应位点的偏好给出直接而明确的解释，因为在羰基

和β碳上没有发现表面极大点，因此我们无法直接考察羰基碳和β碳的特征。

在Multiwfn中，定量分析不仅可应用于整个分子表面，也适用于局域分子表面以揭示原子或片段的特征，见3.15.2.2节的介绍。这里我们在后处理界面(post-processing interface)中选择选项“11 输出每个原子的表面性质(11 Output surface properties of each atom)”来计算并输出每个原子对应的局域表面的性质。部分结果如下所示


```text
Note: Average and variance below are in kcal/mol and (kcal/mol)^2 respectively
 Atom#    All/Positive/Negative average       All/Positive/Negative variance
     1   -24.35251        NaN  -24.35251           NaN        NaN   72.72766
     2     4.65672    5.74594   -1.45401       9.79575    9.01495    0.78080
     3     1.30965    2.36405   -0.88391       2.70896    2.45972    0.24925
     4     8.37174   10.35813   -6.00120      36.74187   17.22299   19.51888
     5     7.07040    8.67973   -6.35468      49.99108   25.33899   24.65209
     6     2.21578    3.02322   -0.73880       5.15593    4.95305    0.20288
     7    15.34251   15.34251        NaN           NaN   22.85377        NaN
     8    14.68486   14.68486        NaN           NaN   25.92230        NaN
```

如您所见，羰基碳（原子2）、α碳和β碳的局域表面上ESP的平均值分别为4.657、1.310和2.216 kcal/mol。这一结果清楚地解释了位点选择性；羰基碳是最有利的位点，因为其局域


![](../imgs/p704_254.png)

<!-- p.705 -->



表面上的平均ESP最正，因此亲核试剂（特别硬亲核试剂）倾向于

被吸引到该位点。相比之下，α碳的局域表面上ESP的平均值比另外两个碳小，因此α碳吸引亲核试剂的能力较弱。

注意，输出的部分数据为NaN（非数字，Not a Number），这些不是程序错误，而是可以理解的。例如，原子1的正ESP部分的平均值为NaN，这是因为氧具有很大的电负性，因此在原子1的局域表面上ESP完全为负，所以正ESP的平均值无法计算。

如果您对什么是“原子的局域表面(local surface of atoms)”感到困惑，或想将其可视化，在选择选项11(option 11)后您可以选择“y”以将表面面片输出为当前文件夹中的locsurf.pqr文件。该文件中的每个原子对应一个表面面片，残基序号对应其归属。利用该文件您可以可视化整个分子是如何划分的，方法是：启动VMD程序并将pqr文件拖入VMD主窗口，在“图形(Graphics)”-“显示方式(Representation)”中将“绘制方式(Drawing method)”设为“点(Points)”，将点尺寸设为4，并将“着色方式(Coloring Method)”设为“残基序号(ResID)”。在VMD主窗口中，选择“显示(Display)”-“正交投影(Orthographic)”并取消选择“显示(Display)”-“深度提示(Depth Cueing)”。然后将丙烯醛的分子结构文件载入VMD并渲染为CPK模式，您将看到下图

在图中，每个点代表一个表面面片；不同颜色代表不同的局域表面区域，每一个对应一个原子。

请注意，`settings.ini`中的“imolsurparmode”参数直接影响局域表面分析的结果，当前我们使用的是imolsurparmode=1。


### 4.12.4 苯酚分子表面上Fukui函数的定量分析(Quantitative analysis of Fukui function on molecular surface of phenol)

笔者已通过可视化其等值面（4.5.4节）和通过布居分析将其凝聚为原子值（4.7.3节）举例说明了如何研究Fukui函数。在本节中，笔者将

说明如何在分子表面上对Fukui函数f −做定量分析，包括三个方面：(1)获得f −的极小点和极大点的位置和数值 (2)研究各原子对应的局域分子表面上f −的平均值 (3)绘制带有表面极值点的f −颜色映射分子表面。笔者仍以苯酚为例：


![](../imgs/p705_255.png)

<!-- p.706 -->



注：若您无法顺利复现下面第1和第2部分所述的步骤，请看视频说明：http://sobereva.com/multiwfn/extrafiles/Molecular_surface_Fukui.mp4。

第1部分：获得f −的极小点和极大点的位置和数值 启动Multiwfn（称为Multiwfn A）并输入以下命令 examples\phenol.wfn

!!! terminal "Multiwfn 交互"

    - **12** — 定量分子表面分析(Quantitative molecular surface analysis)
    - **2** — 选择分子表面上的映射实空间函数(Select the mapped real space function on the molecular surface)
    - **0** — 函数值将从外部文件载入(The function value will be loaded from an external file)
    - **1** — 设置定义表面的方式(Set the way to define the surface)
    - **1** — 用电子密度等值面作为分子表面(Use electron density isosurface as molecular surface)

0.01 // 由于在默认等值面ρ = 0.001上的Fukui函数的量级常常太小，将等值面值增大到0.01 a.u.使接下来的分析更有意义

0 // 开始表面分析(Start the surface analysis) Multiwfn将生成电子密度的格点数据，然后生成表面顶点。在这些顶点的坐标被自动输出到当前文件夹中的surfptpos.txt后，Multiwfn A暂停。不要终止Multiwfn A，我们现在启动另一个Multiwfn（称为Multiwfn B），然后在Multiwfn B中输入以下命令

!!! terminal "Multiwfn 交互"

    - **examples\phenol.wfn 5** — 我们用此模块在surfptpos.txt中记录的点上生成Fukui函数(We use this module to generate Fukui function on the points recorded in surfptpos.txt)
    - **0** — 设置自定义操作(Set custom operation) 1 -,examples\phenol_N-1.wfn

namely Fukui function f − will be calculated)

!!! terminal "Multiwfn 交互"

    - **1** — 电子密度(Electron density)
    - **100** — 从外部文件载入待计算点的坐标(Load the coordinate of the points to be calculated from an external file) surfptpos.txt t.txt

接下来，我们终止Multiwfn B，回到Multiwfn A，然后输入t.txt // 从此文件载入表面顶点处的Fukui函数值(Load the Fukui function values at the surface vertices from this file)

现在您可以在屏幕上找到分子表面（在此为ρ = 0.01 a.u.）上f −的极小点和极大点信息：


```text
The number of surface minima:    16
   #             Value           X/Y/Z coordinate(Angstrom)
     1          0.0005211     -2.128861  -0.802735  -0.931871
     2          0.0005205     -2.076117  -0.773086   0.974712
     3          0.0005075     -1.359761  -2.550410  -0.046948
[ignored...]
```


![](../imgs/p706_256.png)

<!-- p.707 -->




```text
 The number of surface maxima:    12
   #             Value           X/Y/Z coordinate(Angstrom)
     1          0.0015297     -2.922801   1.103604   0.049305
     2          0.0015567     -2.878717  -2.081768  -0.010490
     3          0.0015093     -1.538685   2.959157  -0.031439
*    4          0.0024437     -0.034784  -1.889426  -1.367278
     5          0.0024425     -0.047988  -1.899397   1.366144
[ignored...]
```

您也可以选择选项0(option 0)来可视化表面极值点的分布(visualize distribution of the surface extrema)：

第2部分：研究局域分子表面上f −的平均值 在后处理菜单(post-process menu)中，我们选择选项11(option 11)以输出分布在每个原子对应的局域范德华表面上的Fukui

函数f −的定量统计数据，然后您可以在屏幕上找到以下信息


```text
Atom#   All/Positive/Negative average
    1  1.88921E-03  1.88921E-03          NaN
    2  8.30558E-04  8.30558E-04          NaN
    3  1.20307E-03  1.20307E-03          NaN
    4  1.28067E-03  1.28067E-03          NaN
    5  1.06720E-03  1.06720E-03          NaN
    6  9.43611E-04  9.43611E-04          NaN
[ignored...]
```

NaN意味着局域分子表面上没有f −的负值。从结果中可以清楚地看出，与邻位（C3和C5）和对位（C1）碳对应的局域分子表面上Fukui函数的平均值大于间位碳（C2和C6），这一观察正确地反映了羟基是邻对位定位基的事实。

第3部分：绘制带有表面极值点的f −颜色映射分子表面 在主功能12(main function 12)的后处理菜单(post-process menu)中，选择选项“2 将表面极值点导出为当前文件夹中的surfanalysis.pdb(2 Export surface extrema as surfanalysis.pdb in current folder)”，然后您会得到surfanalysis.pdb。

接下来，为了通过VMD（可在http://www.ks.uiuc.edu/Research/vmd/免费下载）得到f −颜色映射的分子表面，我们需要准备两个分别含有电子密度和f −的cube文件。为此，我们重新启动Multiwfn并输入


![](../imgs/p707_257.png)

<!-- p.708 -->



!!! terminal "Multiwfn 交互"

    - **examples\phenol.wfn 5** — 计算格点数据(Calculate grid data)
    - **0** — 设置自定义操作(Set custom operation) 1 -,examples\phenol_N-1.wfn
    - **1** — 电子密度(Electron density)
    - **3** — 高质量格点(High-quality grid)
    - **2** — 导出格点数据(Export grid data) 现在将刚导出的density.cub重命名为mapped.cub。然后输入0

计算格点数据(Calculate grid data)

!!! terminal "Multiwfn 交互"

    - **1** — 电子密度(Electron density)
    - **3** — 高质量格点(High-quality grid)
    - **2** — 导出格点数据(Export grid data)

现在您在当前文件夹中有了density.cub。将density.cub、mapped.cub、surfanalysis.pdb移动到VMD文件夹。并将“examples\scripts\”文件夹中的VMD绘图脚本molsurfmap.vmd复制到VMD文件夹。之后，启动VMD并在VMD控制台窗口中运行source molsurfmap.vmd执行该脚本，然后您将看到

下图，其中青色和红色小球分别对应ρ = 0.01 a.u.等值面上的极大点和极小点。当前的着色方式为红-白-蓝，对应映射函数从0.0到0.002的变化。

您可以自行编辑molsurfmap.vmd以改变各种默认绘图设置，包括颜色标尺范围、等值面值等。它们也可以在VMD的“图形(Graphics)”-“显示方式(Representation)”界面中更改。


### 4.12.5 鸟嘌呤-胞嘧啶碱基对的Becke表面分析(Becke surface analysis on guanine-cytosine base pair)

Hirshfeld和Becke表面分析的概念已在3.15.5节介绍，请先阅读它们。在本节中笔者将举例说明如何对鸟嘌呤-胞嘧啶(GC)碱基对做Becke表面分析以展示两个单体之间的弱相互作用。注意


![](../imgs/p708_258.png)

<!-- p.709 -->



Hirshfeld表面分析更为常用，见下一节。

!!! terminal "Multiwfn 交互"

    - **启动Multiwfn并输入 examples\GC.wfn** — 在M06-2X/6-31+G**水平下产生，在PM7水平下优化(Generated at M06-2X/6-31+G** level, optimized at PM7 level)
    - **12** — 定量分子表面分析(Quantitative molecular surface analysis)
    - **1** — 改变表面的定义(Change the definition of surface)
    - **6** — 使用Becke表面(Use Becke surface)。您也可以选择5以使用Hirshfeld表面(You can also select 5 to use Hirshfeld surface)
    - **1-13** — 您感兴趣的原子的序号范围（当前为胞嘧啶）(The index range of the atoms you are interested in (cytosine in present case))
    - **0** — 开始计算(Start calculation) Multiwfn找到了许多表面极小点，在这种情况下它们没有意义，同时找到了三个表面极大点


```text
The number of surface maxima:     3
   #             Value           X/Y/Z coordinate(Angstrom)
     1          0.0213498     -1.005651   2.428125   0.009227
     2          0.0251293      0.533238   0.687258   0.007815
*    3          0.0261531      1.861601  -1.067696  -0.009615
```

您可以选择0来将它们可视化(visualize them)，见下图（未显示极小点）

由于这些极大点处电子密度的顺序为3≥2>1，可以预期氢键强度的顺序为O24···H13 ≥ H25···N6 > H29···O8。这一结论与AIM键临界点分析（4.2.1节）完全一致。

如果您想可视化Becke表面，只需选择选项-3(option -3)。如果您想绘制按映射函数值着色的Becke表面，需要利用VMD，有两种方式：(1)将Becke表面绘制为许多点（表面顶点），如下所示 (2)将Becke表面按等值面绘制，将在下一节说明

选择选项8(option 8)将所有表面顶点导出为当前文件夹中的vtx.pqr(export all surface vertices to vtx.pqr in current folder)。该文件中的每个原子对应一个表面顶点，其“电荷(Charge)”属性对应映射函数（当前为电子密度）的值。

将examples\GC.pdb（含有与GC.wfn相同几何结构的pdb文件）拖入VMD程序的主窗口。选择“图形(Graphics)”-“显示方式(Representation)”，将绘制方式改为“棒(Licorice)”并将键半径减小到0.2。然后将vtx.pqr拖入VMD主窗口，选择“图形(Graphics)”-“显示方式(Representation)”，将绘制方式改为“点(Points)”，将着色方式设为“电荷(Charge)”，适当放大点尺寸，在VMD控制台窗口中运行命令color scale method BWR（该命令将着色方式改为蓝-白-红）。现在您应看到


![](../imgs/p709_259.png)

<!-- p.710 -->



上图中Becke表面用点表示，三个红色区域对应高电子密度区，它们源于氢键的存在。本例表明Becke表面分析有助于揭示分子间相互作用明显的区域。

本分析也可通过Hirshfeld表面分析实现，见下一节，当原子数较多时计算开销更低。


### 4.12.6 尿素晶体的Hirshfeld表面分析和指纹图分析(Hirshfeld surface analysis and fingerprint plot analysis on urea crystal)


在本节中我们对尿素晶体做Hirshfeld表面分析，以理解晶体中的分子间相互作用。

注：“用Multiwfn做Hirshfeld表面分析以直观展示分子晶体和配合物中的相互作用”(http://sobereva.com/701，中文)是一篇极其详细的博客文章，全面介绍了Multiwfn中的Hirshfeld/Becke分析并给出了非常丰富的例子，强烈建议阅读！如果您已读过，则无需阅读本节。

分析用结构的准备 您可以直接用尿素晶体的.cif文件作为输入文件，需要足够大的超胞来构建（可通过主功能300(main function 300)的子功能7(subfunction 7)中的选项19(option 19)完成），以便我们关注的分子能完全浸没在环境分子中。您也可以基于分子团簇做分析（这是更好的方式），团簇包含一个中心分子和一批围绕它的分子，Multiwfn直接提供了基于晶体结构构建团簇的功能。您只需启动Multiwfn并输入

urea.cif //尿素的.cif文件，请从互联网上寻找(.cif file of urea, please find it from Internet)。附言：不要手动将其扩展为超胞，否则计算开销会显著增加(PS: DO NOT manually extend it to supercell, otherwise computational cost will significantly increase)

!!! terminal "Multiwfn 交互"

    - **300** — 主功能300(Main function 300)
    - **7** — 几何操作(Geometry operation)
    - **25** — 提取分子团簇（中心分子+周围分子）(Extract a molecular cluster (central molecule + surrounding ones))
    - **1** — 将含原子1的整个分子作为中心分子，该分子及与其靠近的所有周围尿素都将被提取出来(The whole molecule containing atom 1 is taken as the central molecule, this molecule and all surrounding ureas close to it will be extracted)

!!! terminal "Multiwfn 交互"

    - **[按回车键]** — 使用推荐的1.2接触判据([Press ENTER button]


![](../imgs/p710_260.png)

<!-- p.711 -->



现在团簇已被提取出来，中心尿素的原子序号显示在屏幕上，请记下它，稍后会用到。然后您可以用选项0(option 0)可视化团簇结构(visualize the cluster structure)，若发现合理，就可以用相应选项将其导出为结构文件。

尿素团簇的Hirshfeld表面分析 在本例中我们使用下图所示的尿素团簇模型，可按上述方式构建。相应的几何文件examples\Urea_crystal.pdb含有11个尿素，中心分子将在我们的Hirshfeld表面分析中被定义为片段。

启动Multiwfn并输入 examples\Urea_crystal.pdb

!!! terminal "Multiwfn 交互"

    - **12** — 定量分子表面分析(Quantitative molecular surface analysis)
    - **1** — 改变表面类型(Change surface type)
    - **5** — 使用Hirshfeld表面(Use Hirshfeld surface) 16,36,58,2,77,55,34,13

开始计算(Start calculation)。注意这里使用默认的映射函数dnorm(After the calculation is finished, you can select option 8 to export the surface vertices with the mapped electron density to vtx.pqr, and then plot them in VMD via the way described in the last section.) 计算完成后，您可以选择选项8(option 8)将带映射电子密度的表面顶点导出为vtx.pqr，然后按上一节所述方式在VMD中绘制它们。

接下来，我们绘制指纹图。输入以下命令

!!! terminal "Multiwfn 交互"

    - **20** — 指纹图分析(Fingerprint plot analysis)
    - **0** — 开始指纹分析(Start fingerprint analysis)
    - **1** — 将指纹图保存为图像文件(Save fingerprint plot to an image file)

您会发现在当前文件夹中已生成一个.pdf文件，打开后您将看到下图


![](../imgs/p711_261.png)

<!-- p.712 -->



在此图中，X和Y轴分别对应di和de。Hirshfeld表面上的每个顶点对应图中的一个点。可以看到在图的左下方有两个尖峰，这一观察表明尿素既作为氢键受体（下方的尖峰，di > de），又作为氢键给体（左侧的尖峰，di < de）。黄色、绿色和紫色分别表示相应区域的点密度为高、中和低。

局域接触表面的指纹图 在Multiwfn中，指纹图不仅可为整体Hirshfeld表面绘制，也可为局域接触表面绘制（详见3.15.5节）。让我们考察中心尿素中的四个氢与周围尿素中所有原子之间的局域接触表面的指纹图。

关闭显示指纹图的窗口后，选择选项-1(option -1)返回上一级菜单(return to upper level of menu)。现在，我们需要定义“内侧原子(inside atoms)”和“外侧原子(outside atoms)”，只有两组之间的接触表面上的顶点才会在指纹图分析中被计入。我们选择选项1(option 1)来定义“内侧原子(inside atoms)”。系统会依次要求您输入两个条件，它们的交集将定义该集合。我们先直接按回车键使用默认原子范围，即中心尿素中的所有原子，然后输入H以只选中其中的所有氢。从屏幕上可以看到，中心尿素中的四个氢现已被定义为“内侧原子(inside atoms)”。由于默认的“外侧原子(outside atoms)”就是周围尿素中的所有原子，我们无需修改它。

现在，选择选项0(option 0)再次开始指纹图分析(start the fingerprint plot analysis)。您可以在屏幕上找到以下信息：


```text
The area of the local contact surface is    65.639 Angstrom^2
The area of the total contact surface is    94.511 Angstrom^2
The local surface occupies   69.45% of the total surface
```

该信息表明我们定义的局域接触表面的面积为65.6 Å2。显然，通过恰当利用该功能，您可以获得中心分子与周围分子之间任何特定接触对应的面积。

之后，选择选项1(option 1)将相应的指纹图保存为.pdf文件(save corresponding fingerprint plot as a .pdf file)，然后在


![](../imgs/p712_262.png)

<!-- p.713 -->


打开它你会看到

由于这一次我们只考虑了中央尿素中的四个氢，它们纯粹表现为氢供体，因此在图的左侧只能观察到一个尖峰。上方图中的灰色点对应于整个 Hirshfeld 表面上但不在当前局域接触表面上的点。

检查局域接触表面的形状很有意思。为此，在关闭指纹图后，我们选择选项 4，将局域接触表面上的所有点导出为当前文件夹下的 finger.pqr。按照 4.12.5 节所述的方法在 VMD 中绘制它们，你会看到

显然，该表面很好地展示了中央尿素中的氢与周围尿素中的原子之间的接触。表面上有四个红色区域，它们对应于四个氢键，其中中央尿素中的 H 原子表现为氢键供体。

接下来，我们检查中央尿素中的氢与上图中黄色箭头所标记的氧

![](../imgs/p713_263.png)

![](../imgs/p713_264.png)

<!-- p.714 -->


原子之间的指纹图。输入以下命令

!!! terminal "Multiwfn 交互"

    - **-1** — 返回上一级菜单(Return to upper level of menu)
    - **1** — 设置要考虑的内侧原子(Set the inside atoms to consider) [按 ENTER 键(Press ENTER button)]

内侧原子必须是氢(The inside atoms must be hydrogen)

!!! terminal "Multiwfn 交互"

    - **2** — 设置要考虑的外侧原子(Set the outside atoms to consider)
    - **76** — 周围某个尿素中氧的序号(The index of the oxygen in one of surrounding urea)
    - **[按 ENTER 键(Press ENTER button)]** — 不设置元素过滤条件(Do not set element filter condition)
    - **0** — 开始指纹分析(Start fingerprint analysis)

从屏幕上输出的信息中，你可以发现这次产生的局域接触表面为 6.8 Å²，占总接触表面积的 7.2%。然后我们绘制指纹图及相应的表面顶点，如下所示

在指纹图中可以看到表面点的分布范围较窄，且尖峰非常明显，表明由于 H 与 O 的接触而具有很强的氢键特征。

指纹图对于比较不同晶体中的分子间相互作用特别有用，相关讨论见 CrystEngComm, 11, 19 (2009)。

获取每种元素对之间的接触面积 Multiwfn 还能够同时打印每种元素对之间的接触面积，并给出其占总接触面积的百分比。为此，在进入选项“20 指纹图与局域接触分析(Fingerprint plot and local contact analyses)”后，选择选项“3 计算不同元素之间的接触面积(Calculate contact area between different elements)”，随后将立即打印以下信息：


```text
Inside element, outside element, their contact area (Angstrom^2) and percentage (%)
 H-H        42.602      45.076
 H-C         3.355       3.550
 H-N         4.101       4.339
 H-O        15.581      16.486
 C-H         4.943       5.230
 N-H         7.156       7.572
 O-H        16.774      17.748

The same as above, but do not distinguish inside and outside elements
```

![](../imgs/p714_266.png)

![](../imgs/p714_265.png)

<!-- p.715 -->




```text
 H-H              42.602      45.076
 H-C/C-H           8.298       8.780
 H-N/N-H          11.257      11.910
 H-O/O-H          32.355      34.234

Area of total contact surface is    94.511 Angstrom^2
```

这些信息很容易理解。例如，如黄色高亮所示，内侧 H 原子与外侧 O 原子之间的接触面积为 15.581 Å²，内侧 O 原子与外侧 H 原子之间的接触面积为 16.774 Å²，分别占总接触面积（94.511 Å²）的 16.486% 和 17.748%。它们合计的百分比贡献为 16.486% + 17.748% = 34.234%。

为了更直观地查看，你可以将 Multiwfn 打印的数据复制并导入例如 Origin 软件，然后绘制如下饼图：

显然，H-N/N-H 和 H-O/O-H 类型的接触对应于典型的分子间氢键，从饼图中可以看到近一半的接触面积与氢键有关。虽然 H-H 接触占 Hirshfeld 表面的 45.1%，但它显然不对应于有利的分子间相互作用，因为氢显正电，因此 H-H 接触是静电排斥的。

使用 VMD 绘制 Hirshfeld/Becke 表面的颜色映射等值面 这里我介绍如何轻松绘制由电子密度以 promolecular 近似映射的非常漂亮的 Hirshfeld 表面，这种图比上面所示的那些要好看得多。仍以尿素簇为例。

启动 Multiwfn 并输入 examples\Urea_crystal.pdb

!!! terminal "Multiwfn 交互"

    - **12** — 定量分子表面分析(Quantitative molecular surface analysis)
    - **1** — 改变表面定义(Change surface definition)
    - **5** — 使用 Hirshfeld 表面(Use Hirshfeld surface) 16,36,58,2,77,55,34,13

开始计算(Start calculation)

!!! terminal "Multiwfn 交互"

    - **-2** — 将用于定义 Hirshfeld 表面的格点数据导出为当前文件夹下的 surf.cub(Export the grid data used to define Hirshfeld surface as surf.cub in current folder)
    - **13** — 计算映射函数的格点数据并导出为当前文件夹下的 mapfunc.cub(Calculate grid data of mapped function and export it to mapfunc.cub in current folder)

现在你在当前文件夹下得到了 surf.cub 和 mapfunc.cub，将它们移动到 VMD 文件夹。然后将 examples\scripts\hirsh_rho.vmd 文件复制到 VMD 文件夹。启动 VMD，在 VMD 命令窗口中输入 source hirsh_rho.vmd 以运行该脚本。对于当前情形，最好还在命令窗口中输入 material change diffuse Translucent 0.8 以使表面更亮。


![](../imgs/p715_267.png)

<!-- p.716 -->


最后，你可以看到如下图形。注意绘图脚本将颜色过渡设为蓝-白-红，对应于电子密度从 0.0 到 0.015 a.u. 变化。显然，从图中可以很容易识别出明显的分子间相互作用区域。

顺便提一下，有时需要微调颜色标尺。默认值可以在 hirsh_rho.vmd 中修改。你也可以在 VMD 中直接这样定义：进入“Graphics”-“Representation”，选择与等值面对应的表示，然后点击“Trajectory”选项卡，在两个文本框中输入下限和上限，然后按 ENTER 键使其生效。

基于 4.12.5 节中使用的 GC.wfn，你可以用上述相同方法绘制电子密度映射的 Hirshfeld 表面，见下图。

通过非常类似的步骤，你还可以绘制 dnorm 映射的 Hirshfeld 或 Becke 表面，与上述情形相比只有两处不同：(1) 在主功能 12 中，在选择选项 1 切换到 Hirshfeld 或 Becke 表面后，需要选择选项 2 并选择 dnorm 作为映射函数(mapped function)；(2) 应使用 examples\scripts\hirsh_dnorm.vmd 脚本代替上面使用的 hirsh_rho.vmd。

关于 Hirshfeld/Becke 分析的更多例子和相关技巧可以在我的博客文章 http://sobereva.com/701（中文）中找到。


### 4.12.7 预测 FOX-7 分子晶体的密度

如 3.15.1 节所介绍，基于静电势（ESP）定量分子表面分析的结果可以

![](../imgs/p716_268.png)

![](../imgs/p716_269.png)

<!-- p.717 -->


预测分子的许多凝聚相性质。例如，在 Mol. Phys., 107, 2095 (2009) 中，Politzer 等人表明，仅含 C、H、N、O 的分子的晶体密度可预测为


$$\rho=\alpha\frac{M}{V_{\mathrm{m}}}+\beta(v\sigma_{\mathrm{tot}}^{2})+\gamma$$

<!-- formula-ocr: formula_p717_339.png 已替换为LaTeX, 原图保留备查 -->

其中当波函数在 B3PW91/6-31G** 水平下生成且 M/Vm 和 𝜈𝜎tot 2 的单位分别为 g/cm³ 和 (kcal/mol)² 时，α = 0.9183，β = 0.0028，γ = 0.0443。在本节中，我举例说明如何用上述公式预测 FOX-7（1,1-二氨基-2,2-二硝基乙烯）的分子晶体密度，它是一种不敏感高能炸药。关于性质预测的更多说明可以在我的博客文章“使用 Multiwfn 预测晶体密度、汽化热、沸点和溶剂化自由能”（中文，http://sobereva.com/337）中找到。

首先，我们在 B3PW91/6-31G** 水平下优化 FOX-7 的几何并产生波函数文件，这是 Politzer 等人在其 Mol. Phys. 论文中使用的水平。所得的 FOX-7.wfn 已作为 examples\FOX-7.wfn 提供。

启动 Multiwfn 并输入以下命令： examples\FOX-7.wfn

!!! terminal "Multiwfn 交互"

    - **12** — 定量分子表面分析(Quantitative molecular surface analysis)
    - **0** — 在默认表面（电子密度 0.001 a.u. 等值面）上对默认实空间函数（ESP）开始分析(Start analysis for default real space function (ESP) on default surface (0.001 a.u. isosurface of electron density))

稍候，你会在屏幕上发现以下输出


```text
 Volume:   942.48700 Bohr^3  ( 139.66220 Angstrom^3)
 Estimated density according to mass and volume (M/V):    1.7606 g/cm^3
...[ignored]
 Product of sigma^2_tot and miu:   0.00020164 a.u.^2 (   79.40119 (kcal/mol)^2)
 Internal charge separation (Pi):   0.03740373 a.u. (     23.47121 kcal/mol)
```

从输出中，我们发现 M/Vm=1.7606 g/cm³ 且 2totνσ=79.40119 (kcal/mol)²，因此

密度可预测为 0.9183*1.7606+0.0028*79.40119+0.0443=1.883 g/cm³。FOX-7 晶体的实验密度为 1.885 g/cm³，可在其相应的 wiki 页面（https://en.wikipedia.org/wiki/FOX-7）上查到。显然，我们的预测非常成功，误差仅为 -0.002 g/cm³！然而，这出奇好的结果在很大程度上是偶然的，因为根据 Mol. Phys. 论文中的测试，使用上述预测公式的均方根误差为 0.047 g/cm³。


### 4.12.8 硫代甲酸分子表面上轨道重叠距离函数 D(r) 的定量分析


### on thioformic acid molecular surface

本节内容由 Arshad Mehmood 热心提供，并经 Tian Lu 稍作修改。

本例是 4.5.7 节的延续。这里我举例说明在硫代甲酸的分子电子密度等值面上对轨道重叠长度函数 D(r) 的定量分析。

启动 Multiwfn 并输入以下命令：


<!-- p.718 -->



!!! terminal "Multiwfn 交互"

    - **examples\ThioformicAcid.wfn** — 在 B3LYP/6-311++G(2d,2p) 下优化的硫代甲酸(Thioformic acid optimized at B3LYP/6-311++G(2d,2p))
    - **12** — 分子表面的定量分析(Quantitative analysis of molecular surface)
    - **2** — 选择映射函数(Select mapped function)
    - **6** — 轨道重叠距离函数 D(r)，其使 EDR(r;d) 关于 d 最大(Orbital overlap distance function D(r), which maximizes EDR(r;d) with respect to d)
    - **2** — 使用 EDR 指数的总数、起始值和增量的默认值(Use default value of total number, start and increment of EDR exponents)。更多信息请参阅 4.5.7 节(Please consult Section 4.5.7 for more information)。

0 // 现在开始分析(Start analysis now!) 现在分析开始。这一步需要一些时间。计算完成后，屏幕上将连同其它信息打印以下结果：


```text
Global surface minimum:  2.789918 a.u. at   1.983402  -0.346198   1.757884 Ang
Global surface maximum:  3.541349 a.u. at  -2.861073  -1.074395  -0.095237 Ang

 The number of surface minima:     4
   #             Value           X/Y/Z coordinate(Angstrom)
     1          3.296958      -1.622302   2.055665   0.423383
     2          3.218284       0.950838   2.841231   0.010991
*    3          2.789918       1.983402  -0.346198   1.757884
     4          2.790103       2.078805  -0.344424  -1.731277

 The number of surface maxima:    10
   #             Value           X/Y/Z coordinate(Angstrom)
*    1          3.541349      -2.861073  -1.074395  -0.095237
     2          3.401958      -0.539716   2.324441   0.014652
     3          3.502485       0.041422  -2.239222  -0.308278
     4          3.502696       0.089030  -2.257271   0.004859
     5          3.494004       0.207205  -2.075594  -0.673828
     6          3.496480       0.164501  -2.070255   0.707373
     7          3.359381       0.542328   1.465019  -1.650518
     8          3.358980       0.496994   1.456262   1.657761
     9          3.311711       2.030429   1.904600   0.023877
    10          2.918240       2.847314  -1.370280   0.021275
```

现在选择 0 以查看表面极小值和极大值：

该图显示了分子结构和表面极值（红色和蓝色小球分别对应表面极大值和极小值）。可以看到，由于紧凑的孤对电子，氧

![](../imgs/p718_270.png)

<!-- p.719 -->


原子上存在表面极小值，而由于硫更弥散、束缚较弱的孤对电子，表面极大值位于硫原子上。


### 4.12.9 评估整个体系以及单个片段的 vdW 表面积

注：本节的中文版是我的博客文章“使用 Multiwfn 和 VMD 计算分子表面积和片段表面积”（http://sobereva.com/487，中文），其中还包含更多讨论。

在阅读 4.12.1 节之后，你一定已经知道如何评估分子 vdW 表面的面积。在本节中，我将进一步讨论这个话题。将以多巴胺为例，其妥善优化后的几何如下所示

评估对应于凝聚相的多巴胺 vdW 表面积

根据 Bader 的论文 J. Am. Chem. Soc., 109, 7968 (1987)，ρ = 0.001 和 0.002 a.u. 等值面可分别定义为气相和凝聚相中的 vdW 表面。后者的体积小于前者，因为在凝聚相中由于分子间相互作用，vdW 表面的穿透必然很明显。这里我们将为多巴胺计算对应于凝聚相的 vdW 表面面积。启动 Multiwfn 并输入

examples\dopamine.wfn // 使用 B3LYP/6-31G* 水平生成。通常该水平下的密度质量绝对足够(Generated using B3LYP/6-31G* level. Commonly the quality of density at this level is absolutely adequate)

!!! terminal "Multiwfn 交互"

    - **12** — 分子表面的定量分析(Quantitative analysis of molecular surface)
    - **1** — 选择定义表面的方式(Select the way to define surface)
    - **1** — 电子密度的等值面(Isosurface of electron density)
    - **0.002** — 等值面数值（a.u.）(Isovalue (a.u.))
    - **6** — 不考虑映射函数，开始分析(Start analysis without consideration of mapped function) 你只需注意输出中的下面一行：


```text
Overall surface area:         648.64293 Bohr^2  ( 181.63855 Angstrom^2)
```

也就是说，整个分子的面积为 181.6 Å²。

评估多巴胺中氨基的表面积 接下来，我举例说明如何计算特定片段的表面积，以多巴胺中的氨基为例。在后处理菜单中，我们输入

!!! terminal "Multiwfn 交互"

    - **12** — 输出特定片段的表面性质(Output surface properties of specific fragment)
    - **3,19,20** — 氨基中原子的序号(The indices of the atoms in the amino group) 你会看到


```text
Overall surface area:          99.67659 Bohr^2  (  27.91229 Angstrom^2)
```

氨基对整个 vdW 表面的贡献 thus 可计算为 27.9/181.6*100%=15.4%。


![](../imgs/p719_271.png)

<!-- p.720 -->


如果想将归属于氨基的 vdW 表面可视化，我们应输入 y 让 Multiwfn 在当前文件夹下导出 locsurf.pqr。然后将该文件载入 VMD 可视化程序（http://www.ks.uiuc.edu/Research/vmd/），在“Graphics”-“Representation”中将“Drawing method”设为“Points”，将“Coloring method”设为“ResID”，然后将当前体系的结构文件（examples\dopamine.xyz）也载入 VMD 以在图中同时绘制分子几何，稍作调整后你会看到

在上图中，每个点表示一个组成 0.002 a.u. 电子密度等值面的顶点，蓝色区域对应于属于氨基的局域区域。显然，整个 vdW 表面的划分非常合理，因此 Multiwfn 输出的氨基面积必定是可靠且有意义的。

在没有波函数信息时评估 vdW 表面积 有时由于各种原因我们难以生成波函数文件，在这种情况下我们仍可用 Multiwfn 评估 vdW 表面积。此时，我们采用的电子密度应为 promolecular 密度，即按照分子中原子的坐标，将每个原子孤立态的电子密度简单叠加而近似构建的分子电子密度。

例如，我们手头只有 examples\dopamine.xyz，你可以启动 Multiwfn 并载入该文件，然后输入

!!! terminal "Multiwfn 交互"

    - **12** — 分子表面的定量分析(Quantitative analysis of molecular surface)
    - **1** — 选择定义表面的方式(Select the way to define surface)
    - **2** — 特定实空间函数的等值面(Isosurface of a specific real space function)
    - **1** — Promolecular 电子密度(Promolecular electron density)
    - **0.002** — 等值面数值（a.u.）(Isovalue (a.u.))
    - **6** — 不考虑映射函数，开始分析(Start analysis without consideration of mapped function) 计算结果为


```text
Overall surface area:         697.18104 Bohr^2  ( 195.23060 Angstrom^2)
```

显然结果是合理的，195.2 Å² 的值与我们之前基于 B3LYP/6-31G* 波函数计算的 181.6 Å² 定性一致。

如果接着计算氨基部分的面积，结果为 31.5 Å²，也接近基于 DFT 密度计算的 27.9 Å²。特别地，该基团的占比 31.5/195.2*100%=16.1% 甚至与我们之前计算的 15.4% 近乎定量一致。


![](../imgs/p720_272.png)

<!-- p.721 -->




### 4.12.10 sigma-hole 与 pi-hole 面积的定量

简介

σ-hole 和 π-hole 分别对应于由于 σ 电子和 π 电子耗尽而在范德华（vdW）表面上具有明显正静电势（ESP）的局域区域。对应于这些空穴的区域可作为电子受体（局域 Lewis 酸）形成以静电吸引为主导的非共价相互作用，例如卤键。如果你对这两个概念不熟悉，建议阅读综述文章 J. Comput. Chem., 39, 464 (2017)。

推荐阅读。在文献中，σ-hole 和 π-hole 通常通过分析 vdW 表面上的 ESP 极值来揭示，相应极值处的 ESP 值常被用作电子受体潜在强度的定量度量。

在本节中，我将展示还可以用 Multiwfn 计算选定 σ-hole 和 π-hole 所对应的表面积，同时基于输出的文件，相应的局域表面可直接在 VMD 中可视化。建议你阅读 3.15.2.2 节的第 2 部分，其中描述了本分析中使用的算法。这里以 ClPO2 为例

它在氯原子末端含有 σ-hole，在磷原子上下方含有 π-hole。

vdW 表面上 ESP 的定量分析 首先，我们对 vdW 表面上的 ESP 进行常规定量分析。启动 Multiwfn 并输入

!!! terminal "Multiwfn 交互"

    - **examples\ClPO2.fch** — 几何与波函数在 PBE0/def2-TZVP 下产生(Geometry and wavefunction were produced at PBE0/def2-TZVP)
    - **12** — 定量分子表面分析(Quantitative molecular surface analysis)
    - **0** — 开始分析，映射函数默认为 ESP(Start analysis, the mapped function is default to ESP) 从输出中可以看到，在 vdW 表面上找到了三个 ESP 极大值，它们的 ESP 值和坐标如下所示：


```text
   #       a.u.         eV      kcal/mol           X/Y/Z coordinate(Angstrom)
     1  0.07562734    2.057924   47.456909      -1.949844  -0.043516  -0.320257
     2  0.04258971    1.158925   26.725470       0.015842  -0.054525   3.395121
*    3  0.07568641    2.059532   47.493977       1.945305   0.044502  -0.234288
```

现在进入选项 0 检查表面 ESP 极大值的序号并直观查看其位置，见下图左侧（所有表面极小值均已隐藏）。如果你按照 4.A.13 节所述方法绘制 ESP 着色的 vdW 表面以及表面极值，可得到下图右侧，其中红色和蓝色分别对应于正、负 ESP。


<!-- p.722 -->


从上图可以看出，表面极大值 1 和 3 对应于两侧的 π-hole，而极大值 1 对应于 σ-hole。[注：原文如此，依上下文此处应为极大值 2 对应 σ-hole]

检查对应于正 ESP 值的表面区域

由于 σ-hole 和 π-hole 对应于明显为正的 ESP 值，很自然地，围绕表面极大值的正 ESP 区域的面积就是 σ/π-hole 尺寸的直接度量。现在假设我们想测量对应于极大值 3 的 π-hole 的面积，在后处理菜单中应输入以下命令

!!! terminal "Multiwfn 交互"

    - **14** — 计算表面极值周围区域内的面积与函数平均值(Calculate area and function average in a region around a surface extreme)
    - **2** — 表面极大值(Surface maximum)

!!! terminal "Multiwfn 交互"

    - **3** — 选择极大值 3（对应于其中一个 π-hole）(Select maximum 3 (corresponding to one of π-holes))
    - **0** — 将判据设为 0 a.u.(Set criterion as 0 a.u.) 现在我们可以发现以下输出


```text
Number of surface vertices in selected surface region:      4307
Area of selected surface region:    55.946 Angstrom^2
Average value of selected surface region:     0.02650 a.u.
Product of above two values:         1.48230 a.u.*Angstrom^2
```

输出表明，有 4307 个与极大值 3 直接或间接相连且 ESP 值大于 0（即正 ESP）的表面顶点，该局域表面的面积为 55.94 Å²，平均 ESP 为 0.0265 a.u.。根据化学直觉，与预期的 π-hole 面积相比，计算的面积显然

太大，原因是什么？

在当前文件夹中，你可以找到名为 selsurf.pqr 的文件，它包含所有选定表面顶点的坐标，其“Charge”列对应于以 a.u. 为单位的 ESP。现在我们将该文件载入 VMD 程序。此外，在 Multiwfn 的后处理菜单中，我们选择选项 5 导出包含分子几何的 pdb 文件，然后也将其载入 VMD。在 VMD 的“Graphics”-“Representation”面板中，我们将分子的“Drawing Method”设为“Licorice”并将“Bond Radius”设为 0.2，然后将表面顶点的“Drawing Method”设为“Point”并将“Size”设为 16，再将“Coloring Method”设为“Charge”。此时的图形应如下所示


![](../imgs/p722_273.png)

![](../imgs/p722_274.png)

<!-- p.723 -->


在该图中，点越蓝，ESP 值越高。很明显，我们当前选定的

局域表面不仅对应于一个 π-hole，而是对应于整个正 ESP 表面区域。

计算对应于 π-hole 的表面积 显然，如果只想研究对应于一个 π-hole 的区域，ESP 判据应设为大于 0 但小于该 π-hole 表面极大值处 ESP 值（0.0756 a.u.，见上文）的一个较大值。为了找到合适的判据，在“Graphics”-“Representation”面板中，我们将“Selected Molecule”切换到与 selsurf.pqr 对应的条目，然后在“Selected Atoms”文本框中输入 charge > 0.04，此时图形窗口变为：

从图中可以看出，0.04 a.u. 的判据适合定义当前体系 π-hole 所对应的局域表面

上面的图包含两个蓝色局域表面，因为磷原子的每一侧都有一个 π-hole。要计算每个 π-hole 的面积，我们输入

!!! terminal "Multiwfn 交互"

    - **14** — 计算表面极值周围区域内的面积与函数平均值(Calculate area and function average in a region around a surface extreme)
    - **2** — 表面极大值(Surface maximum)

!!! terminal "Multiwfn 交互"

    - **3** — 选择极大值 3（对应于其中一个 π-hole）(Select maximum 3 (corresponding to one of π-holes))
    - **0.04** — 将判据设为 0.04 a.u.(Set criterion as 0.04 a.u.) 结果为


```text
 Number of surface vertices in selected surface region:       271
 Area of selected surface region:     3.570 Angstrom^2
 Average value of selected surface region:     0.05772 a.u.
 Product of above two values:         0.20608 a.u.*Angstrom^2
```

计算得到的 3.57 Å² 是一个非常合理的典型 π-hole 面积。如果你用 VMD 将生成的 selsurf.pqr 可视化以检查选定的局域表面，你会发现该区域恰好对应

上面表面图中所示的两个 π-hole 之一。显然，当前体系中 π-hole 的总面积应为 2*3.57=7.14 Å²。


![](../imgs/p723_275.png)

![](../imgs/p723_276.png)

<!-- p.724 -->


计算对应于 σ-hole 的表面积 接下来，我们用类似方法计算氯原子末端 σ-hole 的面积。此时不应使用 0.04 a.u. 作为判据，因为该 σ-hole 表面极大值处的 ESP 值仅为 0.0425 a.u.。在 VMD 中，我们可通过输入 charge > xxx 尝试不同判据，直到

找到最能代表 σ-hole 的最佳值。经过几次尝试，发现 0.03 a.u. 是合理值，因此我们在后处理菜单中输入以下命令

!!! terminal "Multiwfn 交互"

    - **14** — 计算表面极值周围区域内的面积与函数平均值(Calculate area and function average in a region around a surface extreme)
    - **2** — 表面极大值(Surface maximum)

!!! terminal "Multiwfn 交互"

    - **2** — 选择极大值 2（对应于 σ-hole）(Select maximum 2 (corresponding to the σ-hole))
    - **0.03** — 将判据值设为 0.03 a.u.(Set criterion value as 0.03 a.u.) 发现面积为 4.88 Å²，而该区域内的平均 ESP 值为 0.03617 a.u.，

明显小于 π-hole 的平均值。如果你将导出的 selsurf.pqr 在 VMD 中绘制为点，并将颜色标尺设为 0.0~0.05（在“Representation”面板中选择“Trajectory”选项卡，然后设置“Color Scale Data Range”），你会看到如下图，确实选定的表面区域很好地展示了

预期的 σ-hole 特征。

需要指出的是，计算的面积直接依赖于判据的选择，而没有唯一的方法确定完美判据。在实际研究中，你可以尝试将判据定义为例如相应表面极大值处 ESP 值的 60%，或考虑将判据定义为比表面极大值低例如 10 kcal/mol 的值。

值得注意的是，选项 14 不仅能测量表面极大值周围的面积，还能计算表面极小值周围的面积。因此，你可以尝试用该功能定量各种孤对电子所对应的面积。


### 4.12.11 静电势的分子表面的盆状分析


### potential

正如整个三维分子空间可基于例如电子密度和电子定域函数划分为盆，从而讨论局域区域的特征一样，也可以用类似思想基于特定的映射函数将整个分子表面划分为各自的局域表面，从而获得化学上感兴趣的信息。在本例中，我们将把 ClPO2 的整个 vdW 表面分解为源自其表面 ESP 极小值和极大值的贡献。请阅读 3.15.2.2 节的第 3 部分以了解本分析所用算法的基本知识。ClPO2 已在 4.12.10 节中通过分子表面分析进行了研究，如果尚未阅读请先阅读。


![](../imgs/p724_277.png)

<!-- p.725 -->



!!! terminal "Multiwfn 交互"

    - **启动 Multiwfn 并输入 examples\ClPO2.fch** — 几何与波函数在 PBE0/def2-TZVP 下产生(Geometry and wavefunction were produced at PBE0/def2-TZVP)
    - **12** — 定量分子表面分析(Quantitative molecular surface analysis)
    - **0** — 开始分析，映射函数默认为 ESP(Start analysis, the mapped function is default to ESP)
    - **15** — 表面的盆状划分并计算面积(Basin-like partition of surface and calculate areas) 然后你可以在屏幕上发现以下输出


```text
Minimum   1  N_vert:  1596,  19.615 Angstrom^2  Avg. value:   -0.023076 a.u.
Minimum   2  N_vert:  1613,  19.874 Angstrom^2  Avg. value:   -0.022824 a.u.

Maximum   1  N_vert:  1312,  16.689 Angstrom^2  Avg. value:    0.028729 a.u.
Maximum   2  N_vert:  1753,  21.539 Angstrom^2  Avg. value:    0.023524 a.u.
Maximum   3  N_vert:  1244,  16.040 Angstrom^2  Avg. value:    0.029336 a.u.
```

上述输出给出了对应于不同表面极值的“表面盆”（即局域分子表面）的信息。“N_vert”表示属于该表面盆的表面顶点数，同时还显示了该表面盆中的面积以及映射函数的平均值。Multiwfn 还在当前文件夹下导出了名为 surfbasin.pdb 的文件，它包含所有表面顶点，其 B-factor 对应于顶点所属表面盆的序号（正、负 Beta 值分别对应表面极大值和极小值的序号）。表面盆的序号与相应表面极值的序号相同，每个表面盆包含且仅包含一个表面极值。注意，具有正值的表面极小值和具有负值的表面极大值没有伴随的表面盆，如果你正确理解了 3.15.2.2 节所述的算法，这很容易理解。

为了生动地查看表面盆，你可以将 surfbasin.pdb 载入 VMD，然后将绘制方式设为“Points”，着色方式设为“Beta”。同时，我们在 Multiwfn 中选择相应选项导出分子结构的 pdb 文件（选项 5）和表面极值的 pdb 文件（选项 2），然后在 VMD 中显示它们。最后，你可以得到下图，计算数据也已标出

在当前图中，最小值 1 周围的红色点共同展示了表面盆 1 的区域，而灰色和冰蓝色点分别显示对应于极大值 1 和 2 的表面盆，


![](../imgs/p725_278.png)

<!-- p.726 -->


分别。显然，通过我们目前采用的分析，能够清楚阐明不同极值对整个正或负表面区域的内在贡献。例如，由氯原子的 σ-hole 导致的极大值 2 对正表面区域的百分比贡献为

21.539/(16.689+21.539+16.040)×100%=39.7%。

所有极大值（极小值）的面积之和与“表面分析总结(Summary of surface analysis)”部分输出的正（负）表面积并不完全相同，因为存在一些边界表面片，其三个顶点不具有相同的归属。在计算表面盆的面积和函数平均值时忽略了这些面片。

顺便提一下，你也可以让 VMD 仅显示特定的表面盆。例如，在 VMD 的“Graphics”-“Representation”面板的“Selected Atoms”文本框中分别输入 beta=-1 和 beta=2 并将颜色设为橙色，你将分别观察到对应于最小值 1 和极大值 2 的表面盆：

值得注意的是，由于 C2v 分子对称性，最小值 1 和 2 应具有相同数值，极大值 1 和 3 也应具有相同数值。如上述计算数据所示，这种等价性的轻微破坏是由于数值方面的原因。当你报告对应于 π-hole（极大值 1 和 3）的表面盆数据时，取它们的平均是合理的，即每一侧的面积应为 (16.040+16.689)/2=16.4 Å²。


### 4.12.12 估算小分子的动力学直径

注：本节的中文版及更多讨论是我的博客文章“使用 Multiwfn 计算分子的动力学直径”（http://sobereva.com/503）。

动力学直径是气体分离研究中的重要量。小分子动力学直径最常引用的值取自 Breck 的书 Zeolite Molecular Sieves; Structure, Chemistry and Use，该书出版于 1974 年。在 J. Phys. Chem. A, 118, 1150 (2014) 中，作者提出了一种纯粹基于电子密度等值面计算动力学直径的通用方法。如下例所示（改编自该 J. Phys. Chem. A 论文），两黑色箭头所夹的距离可用于定义动力学直径


![](../imgs/p726_280.png)

![](../imgs/p726_279.png)

<!-- p.727 -->


在该论文中发现，当在波函数生成中使用 PBE0/def2-TZVP 时，若电子密度的等值面数值设为 0.0015 a.u.，计算值与 Breck 值符合得最好。

在本节中，我将展示如何使用定量分子表面分析模块实现上述方法，以计算典型分子 CO 的动力学直径。在 PBE0/def2-TZVP 水平下优化任务产生的 .fch 文件已作为 examples\CO.fch 提供。

在进行计算之前，我们应使用主功能 0 检查 CO.fch 中分子的取向，如下所示

显然，分子轴恰好平行于 Z 轴，因此动力学直径可计算为具有最大正 X 值的表面顶点与具有最大负 X 值的表面顶点之差（表面定义为电子密度 0.0015 a.u. 等值面）。

现在我们进行计算。启动 Multiwfn 并输入 examples\CO.fch

!!! terminal "Multiwfn 交互"

    - **12** — 分子表面的定量分析(Quantitative analysis of molecular surface)
    - **1** — 选择定义表面的方式(Select the way to define surface)
    - **1** — 电子密度的等值面(Isosurface of electron density)
    - **0.0015** — 等值面数值(Isovalue)
    - **6** — 不考虑映射函数，开始分析(Start analysis without consideration of mapped function) 适当上翻后，你可以发现以下输出：


```text
Among all surface vertices:
Min-X:     -1.7527  Max-X:    1.7528 Angstrom
Min-Y:     -1.7527  Max-Y:    1.7528 Angstrom
```

![](../imgs/p727_281.png)

![](../imgs/p727_282.png)

<!-- p.728 -->




```text
Min-Z:     -2.5093  Max-Z:    2.0951 Angstrom
```

这意味着动力学直径可计算为 1.7528-(-1.7527)=3.505 Å。根据该 J. Phys. Chem. A 论文表 2，拟合斜率为 1.025，因此最终估计值应为 3.505/1.025=3.42 Å，与 Breck 值（3.76 Å）定性一致。

CO 是非常简单的情况，而对于复杂得多的分子，必须使用 VMD（http://www.ks.uiuc.edu/Research/vmd/）测量两个合适表面顶点之间的距离以估计动力学直径。仍以 CO 为例，在后处理菜单中，选择选项 6 在当前文件夹下导出 vtx.pdb，它记录了所有表面顶点。然后将该文件载入 VMD，在“Graphics”-“Representation”中，将“Drawing method”设为“Points”。然后在 VMD 主窗口中，选择“Display”-“Orthographic”。之后，激活 VMD 图形窗口，按键盘上的按钮 2，然后点击位于合适位置的两个顶点。从下图可以发现，两顶点之间的距离为 3.47 Å，与上面给出的 3.505 Å 非常接近。

选择合适的表面顶点并不太容易，请务必耐心。如果顶点选错，可进入“Graphics”-“Labels”，然后删除不需要的原子标签和键标签。


### 4.12.13 使用局域电子亲和势和局域电子附着能揭示亲电区域

注：关于本主题的更多讨论和例子见我的博客文章“使用 Multiwfn 通过局域电子附着能（LEAE）研究亲核反应的优先位点与难易以及弱相互作用”（http://sobereva.com/676，中文）。

我们已在 4.12.2 节研究了平均局域电离能（IEL），如果尚未阅读请先阅读，因为本节可视为该节的扩展。有两个与 IEL 密切相关的函数，即局域电子亲和势（EAL）和局域电子附着能（Eatt），将在本节中介绍和举例说明。

J. Mol. Model., 9, 342 (2003) 提出了局域电子亲和势 IEL 并定义为


![](../imgs/p728_283.png)

<!-- p.729 -->


$$E A_{\mathrm{L}}(\mathbf{r})=\frac{-\sum_{i\in\mathrm{v i r}}\left|\varphi_{i}(\mathbf{r})\right|^{2}\varepsilon_{i}}{\sum_{i\in\mathrm{v i r}}\left|\varphi_{i}(\mathbf{r})\right|^{2}}$$

<!-- formula-ocr: formula_p729_340.png 已替换为LaTeX, 原图保留备查 -->

i ∈ vir

其中 ε 表示轨道能量，φ 为轨道波函数。EAL 对应于 Multiwfn 中的自定义函数 27。

EAL 基于 Koopmans 近似近似揭示给定点处的电子亲和。预期某点处的 EAL 越正，该区域的亲电性越强。显然，这一性质使 EAL 具有一定的揭示亲核进攻有利位点的能力。

展示 EAL 分布的最佳方式应是通过不同颜色将其映射到分子表面上。在 4.12.2 节中我已说明如何基于 Multiwfn 输出文件利用 VMD 程序的脚本绘制 IEL 映射的分子表面，下面我将说明如何用几乎相同的方式绘制 EAL 的这种图。

将以 examples\CH3Cl.fchk 为例，它在 B3LYP/6-31G* 水平下生成。注意，仅当未使用弥散函数时 EAL 才有意义。此外，你必须使用包含虚轨道的文件作为输入文件，例如 .mwfn、.fch 和 .molden，因为 EAL 计算涉及虚轨道。

要绘制该图，你应做以下事情（以下流程仅适用于 Windows 平台，对于 Linux 平台你应自行编写类似脚本）

- 将 LEA_isoext.bat 和 LEA_isoext.txt 从 "examples\scripts\local_EA" 文件夹复制到当前文件夹。用文本编辑器编辑 .bat 文件，将 VMD 路径设为你机器上实际的 VMD 文件夹，并将 Multiwfn 的输入文件路径设为其实际路径，即 examples\CH3Cl.fchk。

- 将 LEA_isoext.vmd 从 "examples\scripts\local_EA" 文件夹复制到 VMD 文件夹
- 双击 LEA_isoext.bat 运行它。然后将调用 Multiwfn 生成 density.cub（ρ 的 cube 文件）、userfunc.cub（EAL 的 cube 文件）和 surfanalysis.pdb（包含 ρ = 0.01 a.u. 等值面上的 EAL 表面极值点），然后它们将被自动移至 VMD 文件夹

启动 VMD 并在 VMD 控制台窗口中输入 source LEA_isoext.vmd 以运行此脚本，然后你将看到下图

此图显示了映射了 EAL 的 ρ = 0.01 a.u. 等值面，颜色标尺为 -0.80（蓝色）到 -0.30（红色）a.u.，青色小球对应于此表面上 EAL 的极大值点。可以看到，氢周围的区域具有最正的 EAL，表明它们是该分子最亲电的

![](../imgs/p729_284.png)

<!-- p.730 -->


分子部分。这些区域的存在源于氢带有正电荷的事实。在 Cl 原子末端也存在一个 EAL 相对更正的区域，这

表明 Cl 原子的 σ-hole 的存在。

要查询表面极值点的确切数值，你应激活 VMD 的 OpenGL 窗口，然后点击键盘上的 0 按钮进入查询模式，然后点击一个表面极值点的中心，例如，上图中顶部处的极值点，你将在 VMD 控制台窗口中找到它的索引（index 9）。然后在 VMD 控制台窗口中输入 [atomselect top "index 9"] get beta，你将发现其值为 -12.49，单位为 eV，对应于 -12.49/27.2114 = -0.46 a.u.。

值得注意的是，EAL 最合适的颜色标尺通常因体系而异。如果你发现整个等值面呈单色，或不同区域的颜色无法清晰区分，你应适当调整颜色标尺的下限和上限。例如，如果你在 VMD 控制台窗口中输入 mol scaleminmax 0 1 -1.0 -0.4，则颜色标尺将变为 -1.0 ~ -0.4 a.u.。

顺便提一下，为了充分理解该脚本的工作原理，鼓励你将记录在 LEA_isoext.txt 中的命令逐条手动输入到 Multiwfn 窗口中。

Local electron attachment energy 该函数在 J. Phys. Chem. A., 120, 10023 (2016) 中定义为

$$E_{\mathrm{att}}(\mathbf{r})=\frac{n\sum\limits_{i=LUMO}^{\varepsilon_{i}<0}\left|\varphi_{i}(\mathbf{r})\right|^{2}\varepsilon_{i}}{\rho(\mathbf{r})}$$

<!-- formula-ocr: formula_p730_341.png 已替换为LaTeX, 原图保留备查 -->

其中 i 遍历所有能量为负的非占据轨道。对于限制性和非限制性波函数，n 分别等于 2 和 1。Eatt 对应于 Multiwfn 中的自定义函数 -27，你可以在 Multiwfn 中通过多种方式研究它。

该函数的特征与 LEA 高度类似，但主要是因为计算中不涉及高能量非占据分子轨道（完全缺乏化学意义），该函数比 LEA 更稳健，且允许使用弥散函数。然而，要使用该函数，必须保证至少 LUMO 具有负能量，否则该函数在全空间将恒为零。在原始论文中发现 Eatt 在 B3LYP/6-31+G(d,p) 波函数下表现合理。因此，我们将使用在此水平下生成的波函数来说明 Eatt 的分析。值得注意的是，在 B3LYP/6-31G* 水平下，即使 LUMO 也具有正能量，因此至少在这种情况下添加弥散函数是必需的！

我们将像上面的 EAL 例子一样为 CH3Cl 绘制 Eatt 着色的分子表面。分子表面将定义为 0.004 a.u.，这是因为 Eatt 的原始论文建议在此表面上研究 Eatt。你应做以下事情（在 Windows 下）

- 将 LEAE_isoext.bat 和 LEAE_isoext.txt 从 "examples\scripts\local_EA" 文件夹复制到当前文件夹。用文本编辑器打开 .bat 文件，将 VMD 路径设为你机器上实际的 VMD 文件夹，并将 Multiwfn 的输入文件路径设为其实际路径，即 examples\CH3Cl_631+Gxx.fch，它是通过 Gaussian 16 以 B3LYP/6-31+G(d,p)//B3LYP/6-31G(d) 计算生成的。

- 将 LEAE_isoext.vmd 从 "examples\scripts\local_EA" 文件夹复制到 VMD 文件夹。
- 双击 LEAE_isoext.bat 运行它。然后将调用 Multiwfn 生成 density.cub（ρ 的 cube 文件）、userfunc.cub（Eatt 的 cube 文件）和 surfanalysis.pdb（包含表面

## Multiwfn

> 格点数据处理、AdNDP、模糊原子空间、电荷分解、盆分析、激发分析、轨道定域

> 英文原文见同目录 `08_教程4.13-4.19.md`｜图片目录：`../mw_imgs/`

---
