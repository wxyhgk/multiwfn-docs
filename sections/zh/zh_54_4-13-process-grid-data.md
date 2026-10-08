# 处理格点数据 (Process grid data)

> Multiwfn manual, p.731–742.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.731 -->



在 ρ = 0.004 a.u. 等值面上的 Eatt 极值点)，然后它们会被自动移动到 VMD 文件夹

启动 VMD，并在 VMD 命令行窗口中输入 source LEAE_isoext.vmd 以运行该脚本。然而，在默认的颜色标尺下（从 -0.03 到 0.0 a.u.），分子表面不同区域的特征无法清晰区分。因此，我们在 VMD 命令行窗口中输入以下命令，将颜色标尺改为 [-0.015,0] a.u.：mol scaleminmax 0 1 -0.015 0，然后你将看到如下图所示，两幅为不同视角

在这张图中，颜色按蓝-白-红变化，区域越蓝（Eatt 越负），相应区域的亲电性越强。该图传达的信息本质上与

EAL 相同，即 -CH3 基团的末端亲电性最强，而 Cl 原子的 σ-hole 也显示出较弱的亲电性。

表面上的青色小球对应于 Eatt 的表面极值点。用与上一个例子相同的方法查询它们的数值，你可以发现位于 Cl 原子末端的表面极值点为 -0.29 eV，而位于 -CH3 一侧的为 -0.5 eV。


## 4.13 处理格点数据 (Process grid data)

主功能13 (Main function 13) 包含一系列子功能，利用它们你可以处理从 Gaussian 型 cube 文件 (.cub)、DMol3 格点文件 (.grd)、ParaView VTK Image Data 文件 (.vti) 载入的格点数据，或直接由例如 Multiwfn 的主功能5 (Main function 5) 生成的格点数据。在本节中我将介绍几个简单的应用，其它子功能请自行尝试。


### 4.13.1 提取平面内的数据点 (Extract data points in a plane)

在本例中，我们将 Z=28 到 Z=32 Å 之间的平均 XY 平面数据提取到纯文本文件中。

dens.cub // 由 Multiwfn 或某些外部程序生成的 cube 文件，由于 cube 文件一般较大，“examples”文件夹中未提供。你也可以使用由 Multiwfn 内部生成的格点数据，即先用主功能5 (Main function 5) 计算格点数据，然后选择 0 返回主菜单（刚才生成的格点数据仍保存在内存中）

13 // 处理格点数据 (Process grid data) 5 // 提取平均平面数据 (Extract average plane data) 28,32 // Z 的范围（单位为 Å）


![](../imgs/p731_285.png)

![](../imgs/p731_286.png)

<!-- p.732 -->



现在数据点已导出到当前文件夹下的 output.txt，其中包括 X、Y 坐标和数值。你可以将该文件导入 Sigmaplot 等绘图软件绘制平面图。

另一个例子，我们提取由原子 4、6、2 定义的平面上的数据点。dens.cub 13 // 处理格点数据 (Process grid data) 8 // 通过指定三个原子序号输出平面内数据 (Output data in a plane by specifying three atom indices)。该功能常用于提取倾斜平面，如果平面平行于 XY、YZ 或 XZ 平面，则应分别使用功能 1、2 或 3

0 // 使用自动确定的容差距离。如果任一点与你定义的平面之间的垂直距离小于容差距离，则该点将被输出

1 // 将你定义的平面内的数据点投影到 XY 平面，以便你可以直接将输出文件导入绘图软件绘制平面图

现在沿线的数据值连同坐标已导出到当前文件夹下的 output.txt。请注意，Multiwfn 在提取平面数据时不做插值，因此如果格点数据的质量不够精细（即点间距较大），则提取出的平面数据会很稀疏（对于不平行于 XY、YZ 或 XZ 平面的平面尤其严重）。


### 4.13.2 对格点数据进行数学运算 (Perform mathematical operation on grid data)

例1 假设我们有两个 cube 文件 A.cub 和 B.cub，在本例中我们得到它们的差值 cube 文件（即 A.cub 减 B.cub）。

启动 Multiwfn 并输入以下命令 A.cub // 将第一个 cube 文件载入内存 13 // 处理格点数据 (Process grid data) 11 // 格点数据计算 (Grid data calculation) 4 // 将内存中的格点数据减去另一份格点数据 (Subtract the grid data in memory by another grid data) B.cub // 包含另一份格点数据的 cube 文件。注意该 cube 文件必须与第一个 cube 文件具有完全相同的格点设置

现在内存中的格点数据已被更新，选择 0 将其导出为新的 cube 文件，即为我们所需的文件。

例2 假设我们有两个 cube 文件 MO1.cub 和 MO2.cub，每个文件记录了一个轨道的波函数值。在本例中我们将生成一个包含由这两个轨道产生的总电子密度的 cube 文件。根据 Born 几率诠释，轨道波函数值的平方即为其密度几率，因此我们需要的是两份格点数据平方之和。

启动 Multiwfn 并输入以下命令 MO1.cub 13 // 处理格点数据 (Process grid data) 11 // 格点数据计算 (Grid data calculation)


<!-- p.733 -->



10 // 执行 A2+B2=C 操作，其中 A 为当前格点数据 (MO1.cub)，B 为另一个 cube 文件 (MO2.cub)，C 为新的格点数据

MO2.cub // 载入另一个 cube 文件 计算完成后，内存中的格点数据已更新为 C。0 // 输出更新后的格点数据 totdes.cub // 新 cube 文件的文件名，其中包含这两个轨道的总电子密度


### 4.13.3 缩放格点数据的数值范围 (Scaling numerical range of grid data)

ELF 函数的数值范围为 [0,1]，在本例中，我们将其数值范围缩放到 [0,65535]（即无符号 16 位整数的取值范围）。我们首先如 4.5.1 节所述在 Multiwfn 中计算 ELF 格点数据，然后输入

0 // 从格点数据计算的后处理界面返回主菜单 13 // 处理格点数据 (Process grid data) 16 // 缩放数据范围 (Scale data range) 0,1 // 原始数据范围 0,65535 // 缩放后的范围。关于缩放算法的细节请阅读 3.16.12 节。

现在格点数据已被缩放。你可以选择功能 0 将更新后的格点数据导出为 Gaussian cube 文件，或用相应功能将平面数据提取为纯文本文件。


### 4.13.4 屏蔽局域区域内的等值面 (Screen isosurfaces in local regions)

有时我们不希望显示全空间的所有等值面，因为过多的等值面会干扰视线。本节我将展示如何屏蔽不感兴趣的等值面

### 4.13.4.1 屏蔽某个区域内侧或外侧的等值面 (Screen isosurfaces inside or outside a region)

本节我以苯酚二聚体的电子密度为例。首先，我们如下生成格点数据（你也可以直接载入 .cub/.grd 文件，然后进入主功能13 (Main function 13)）

examples\phenoldimer.wfn 5 // 计算格点数据 (Calculate grid data) 1 // 电子密度 (Electron density) 2 // 中等质量格点 (Medium-quality grid) -1 // 显示等值面 (Visualize isosurface) 如你所见，两个苯酚分子上都出现了等值面。


<!-- p.734 -->



假设我们只希望显示右侧苯酚周围的等值面，我们需要将靠近左侧苯酚的格点的值设为非常小的值，例如零。

关闭 Multiwfn 的图形界面窗口并输入 0 // 返回主菜单 (Return to main menu) 13 // 处理格点数据 (Process grid data) 13 // 设置远离/靠近某些原子的格点的值 (Set value of the grid points that far away from / close to some atoms) -0.7 // 这表示我们将把位于原子范德华半径 0.7 倍以内的格点的值进行设置。如果输入 0.7，则将把位于范德华半径 0.7 倍以外的格点的值进行设置

0 // 将值设为 0 2 // 定义模式。2 表示手动输入原子序号（若选择 1，则用外部文件包含的原子序号列表定义片段，格式见 3.16.9 节或下一个例子）

1-13 // 左侧苯酚的原子序号范围 现在格点数据已被更新，让我们选择选项 -2 显示当前格点数据的等值面。如你所见，左侧苯酚的等值面已经消失。

### 4.13.4.2 屏蔽两个片段重叠区域之外的等值面 (Screen isosurfaces outside overlap region of two fragments)

在用 NCI 方法（4.20.1 节）分析分子间相互作用时，我们只想研究分子间区域的等值面。为了屏蔽其它区域的等值面，我们可以将位于两个分子的缩放范德华区域叠加区域之外的格点的值设为非常大的值（至少大于当前格点数据中的最大值）。在本节中我将给出一个实际例子。

所谓“缩放范德华区域”是指片段中所有原子的缩放范德华球的叠加区域。而“缩放范德华球”是指与缩放后的范德华半径对应的球体。

下图为用 VMD 程序绘制的一段二聚蛋白（读完 4.20.2 节后你就会知道如何绘制类似的图形），红色和蓝色分别代表两条链的主链结构。约化密度梯度的等值面显示了弱相互作用区域。然而，这些等值面既包括分子间部分也包括分子内部分，它们相互交织，给两条链之间弱相互作用的直观研究带来困难。


![](../imgs/p734_287.png)

<!-- p.735 -->



为了屏蔽那些分子内的等值面，我们将使用 Multiwfn 主功能13 (Main function 13) 中的子功能14 (Subfunction 14)。首先，我们为两条链准备两个原子列表文件（每条链对应一个片段）。atmlist1.txt 包括链 1 的原子序号，该文件的头部和尾部为：


```text
159   <--- Total number of atoms in chain 1
1   <--- Atom index of the first atom in chain 1
2   <--- Atom index of the second atom in chain 1
...
159   <--- Atom index of the last atom in chain 1
```

类似地，atmlist2.txt 定义链 2 的原子列表，其头部和尾部为：


```text
159   <--- Chain 2 has 159 atoms too
160   <--- Atom index of the first atom in chain 2
161   <--- Atom index of the second atom in chain 2
...
318   <--- Atom index of the last atom in chain 2
```

然后启动 Multiwfn 并输入：RDG.cub // 与上图对应的约化密度梯度的 cube 文件 13 // 处理格点数据 (Process grid data) 14 // 设置位于两个片段的缩放范德华区域重叠区域之外的格点的值 (Set value of the grid points outside overlap region of the scaled vdW regions of the two fragments)

1.8 // 缩放范德华半径所用的值。在你的实际研究中，你可能需要多次尝试该值以找到合适的值

1000 // 将那些格点的值设为 1000，该值已足够大 1 // 定义模式，1 表示用外部文件定义片段 (using external file to define the fragment) atmlist1.txt // 链 1 的原子列表文件名


![](../imgs/p735_288.png)

<!-- p.736 -->



atmlist2.txt // 链 2 的原子列表文件名 等待片刻，格点数据将被更新。然后选择功能 0 将其导出为 cube 文件。用这个新的 cube 文件重新绘制上图，我们发现所有的分子内等值面都已消失，图形变得非常清晰。

事实上，当情况并不复杂时（如本例），并不需要准备原子列表文件，你可以选择定义模式为 2，然后直接输入原子序号（即链 1 为 1-159，链 2 为 160-318）。


### 4.13.5 获取分子轨道的质心 (Acquire barycenter of a molecular orbital)

在本例中，我们将计算一个分子轨道的质心。用类似的方法你也可以得到其它实空间函数的质心。质心的定义见 3.16.13 节。下图为苯酚第 10 个分子轨道的等值面。

在计算该分子轨道的质心之前，我们需要得到该分子轨道的格点数据。我们


![](../imgs/p736_289.png)

![](../imgs/p736_290.png)

<!-- p.737 -->



可以在 Multiwfn 中完成，即启动 Multiwfn 并输入以下命令：

examples/phenol.wfn 5 // 计算格点数据 (Calculate grid data) 4 // 选择轨道波函数 (Choose orbital wavefunction) 10 // 第 10 个轨道 (The 10th orbital) 2 // 中等质量格点。格点越精细，给出的质心位置越准确 (Finer quality of grid will give more accurate barycenter positions) 0 // 返回主菜单 (Return back to main menu) 现在格点数据已存入内存，我们现在对其进行分析 13 // 处理格点数据 (Process grid data) 17 // 显示统计数据 (Show statistic data) 1 // 选择所有点 (Select all points) 从输出中，我们可以发现该分子轨道正值部分的质心的 X、Y、Z 分量（单位为 Bohr）分别为 2.629、-0.408、0.000，而负值部分的则为 -2.603、-0.702、0.000。该轨道的总质心目前没有意义，因为该轨道的总积分为零。然而，该分子轨道绝对值的总质心是有用的，尤其对于大分子，由此我们可以了解该轨道主要位于何处。为了做到这一点，我们输入：

11 // 格点数据计算 (Grid data calculation) 13 // 取绝对值 (Get absolute value) 17 // 显示统计数据 (Show statistic data) 1 // 选择所有点 (Select all points) 我们发现该分子轨道总质心的 X、Y、Z 分别为 -0.043、-0.558、0.000 Bohr。由于现在已没有负值区域，负值部分的质心显示为 NaN（Not a Number，非数字）。


### 4.13.6 绘制电荷位移曲线 (Plot charge displacement curve)

Multiwfn 能够计算并绘制格点数据的积分曲线，介绍见 3.16.14 节。如果格点数据选为电子密度差，则该积分曲线通常称为电荷位移曲线 (charge displacement curve, CDC)，利用它可以直观且定量地研究电荷转移，非常适合线性体系。在本例中，我们将借助 CDC，研究在沿分子轴施加 0.03 a.u. 外电场时聚炔 (n=7) 中的分子间电荷转移。

“examples”文件夹中的 polyyne.wfn 和 polyyne_field.wfn 文件分别对应于孤立状态的聚炔和施加 0.03 a.u. 外电场的情况。计算使用 B3LYP/6-31G*，两种情况均使用在孤立状态下优化的几何结构。在 Gaussian 程序中，可通过关键词 field=z+300 开启电场。

在绘制 CDC 之前，我们必须先计算这两个文件之间的电子密度差格点数据。启动 Multiwfn 并输入以下命令：

examples\polyyne_field.wfn 5 // 计算格点数据 (Calculate grid data) 0 // 自定义操作 (Custom operation) 1 -,examples\polyyne.wfn //用 polyyne_field.wfn 的性质减去 polyyne.wfn 的性质 (Subtract the property of polyyne.wfn from polyyne_field.wfn) 1 // 电子密度 (Electron density) 2 // 中等质量格点 (Medium-quality grid)


<!-- p.738 -->



我们首先显示电子密度差的等值面。选择 -1 并将等值设为 0.004 后，我们将看到如下图所示

绿色和蓝色部分分别代表施加外电场后电子密度增加和减少的区域。可以看出，虽然绿色和蓝色部分相互交错，但总体趋势是电子转移到 Z 轴正向一侧（即朝向电场源方向）。接下来，我们将绘制 CDC，它能够定量刻画不同区域的电子转移。

点击图形界面中的 “Return”按钮，然后输入 0 // 返回主菜单 (Return to main menu) 13 // 处理格点数据 (Process grid data) 18 // 计算并绘制积分曲线 (Calculate and plot integral curve) Z // 将沿 Z 方向绘制曲线 (The curve will be plotted in Z direction) [按 ENTER 键] // 选择整个范围 (Select the entire range) 在菜单中，我们首先选择选项 2 绘制电子密度差格点数据的局域积分曲线。你将看到

从该图中我们可以考察不同 Z 坐标对应的 XY 平面内电子密度差的积分。Z 坐标和数值分别对应于图的 X 轴和 Y 轴。你可以直接将该曲线与上图所示的等值面图对照，低于和高于零（虚线）的峰分别对应于蓝色和绿色的等值面。注意，在命令行窗口中，现在你可以找到该曲线所有极小值和极大值的位置和数值。


![](../imgs/p738_291.png)

![](../imgs/p738_292.png)

<!-- p.739 -->



在图上点击鼠标右键关闭图形，然后选择选项 1，CDC 将立即显示

该图是由上一幅图所示曲线沿分子轴积分得到的。在其左半部分，虽然有一些起伏，但 CDC 逐渐变得越来越负，并在 X 轴中点（对应于聚炔中心）达到最小值 1.4，这意味着由于外电场，聚炔左半部分失去的电子数为 1.4。在图的右半部分，CDC 从 -1.4 逐渐增大并最终达到零，表明有 1.4 个电子转移到聚炔右半部分，而由于在整个分子空间中电子的增加量和减少量恰好相互抵消，电子总数没有变化（换言之，电子密度差在整个分子空间中的积分恰好为零）。


### 4.13.7 电子密度重叠的评估 (Evaluation of electron density overlap)

在本例中我们以甲烷二聚体为例，评估两个单体的电子密度在何处明显重叠。甲烷二聚体的结构为

我们首先为二聚体得到任意实空间函数的格点数据。启动 Multiwfn 并输入：

examples\rho_overlap\dimer.pdb 5 // 格点数据计算 (Grid data calculation) 100 // 自定义函数，默认情况下该函数不花费任何计算时间 (User define function)


![](../imgs/p739_293.png)

![](../imgs/p739_294.png)

<!-- p.740 -->



-10 // 设置格点延伸距离 (Set grid extension distance) 2 // 将距离减小到 2 Bohr，以避免在体系边界浪费格点 (Decrease the distance to 2 Bohr) 2 // 中等质量格点 (Medium-quality grid) 2 // 将格点数据导出为 userfunc.cub (Export grid data) 现在我们用 Gaussian 为两个单体计算波函数文件，输入文件为 examples\rho_overlap 文件夹中的 monomer1.gjf 和 monomer2.gjf。最终，我们得到 monomer1.wfn 和 monomer2.wfn。注意在 Gaussian 计算中必须使用 nosymm 关键词，以避免自动重定向和平移。

现在我们在全空间计算单体 1 的电子密度格点 monomer1.wfn 5 // 格点数据计算 (Grid data calculation) 1 // 电子密度 (Electron density) 8 userfunc.cub // 用该 cube 文件定义格点，它对应于全空间 (Use this cube file to define the grid) 2 // 导出格点数据 (Export grid data) 然后将得到的 density.cub 重命名为 density1.cub。对 monomer2 重复上述步骤得到 density2.cub。

现在我们计算 min(rho(1),rho(2)) 的格点数据，即在各处取两份电子密度的最小值。启动 Multiwfn 并输入：

density1.cub 13 // 处理格点数据 (Process grid data) 11 // 对格点数据的数学运算 (Mathematical operation on grid data) 21 // 取 min(rho(1),rho(2)) (Take min(rho(1),rho(2))) density2.cub 0 // 导出所得格点数据 (Export resulting grid data) overlap.cub 我们用文本编辑器打开 overlap.cub 和 density2.cub，从后者复制原子坐标到前者，同时修改原子数。然后 overlap.cub 的头部应如下所示（高亮文本为修改部分）


```text
Generated by Multiwfn
 Totally       531846 grid points
   10   -3.693194   -3.955866   -7.444301
   63    0.119334    0.000000    0.000000
   67    0.000000    0.119334    0.000000
  126    0.000000    0.000000    0.119334
    6    6.000000    0.000000    0.000000    3.371271
    1    1.000000    0.000000    0.000000    5.444301
    1    1.000000    0.000000    1.955867    2.677742
    1    1.000000   -1.693195   -0.976988    2.677742
    1    1.000000    1.693195   -0.976988    2.677742
    6    6.000000    0.000000    0.000000   -3.371271
    1    1.000000    1.693195    0.976988   -2.677742
    1    1.000000    0.000000    0.000000   -5.444301
    1    1.000000   -1.693195    0.976988   -2.677742
```


<!-- p.741 -->




```text
    1    1.000000    0.000000   -1.955867   -2.677742
```

启动 Multiwfn 并载入 overlap.cub，进入主功能0 (Main function 0)，将等值改为较小的值如 0.0005，你将清楚地看到密度重叠区域：

值得注意的是，如果接着你进入主功能13 (Main function 13)，选择子功能17 (Subfunction 17) 然后输入 1，你将能够得到密度重叠函数在全空间的积分值，即 “Integral of all data”。显然，该积分越大，单体密度相互重叠的程度越高。

顺便提一下，如果你觉得上述步骤过于冗长，你可以充分利用 Multiwfn 的静默模式显著减少操作步骤，见 5.2 节。


### 4.13.8 在圆柱区域内积分电子密度 (Integrate electron density in a cylindrical region)

Multiwfn 能够在特定的空间和数值范围内获得统计信息（积分、体积、最大最小值等）。为说明该功能的用法，在本例中我们首先计算乙炔的电子密度，然后在围绕 C-C 键的圆柱区域内积分电子密度。

启动 Multiwfn 并输入 examples\C2H2.wfn 5 // 计算格点数据 (Calculate grid data) 1 // 电子密度 (Electron density) 3 // 高质量格点 (High-quality grid) 0 // 返回主菜单 (Return to main menu) 13 // 处理格点数据 (Process grid data) 17 // 显示格点统计数据 (Show statistic data of grid points) 2 // 获取特定空间和数值范围内格点的统计数据 (Obtain statistic data for grid points in specific spatial and value ranges) [直接按 ENTER 键] // 不设置数值范围的约束条件 (Do not set constraint condition of value range) 2 // 圆柱区域 (Cylindrical region) 0.000000 0.000000 0.602676 // 作为圆柱第 1 个端点的 C1 的坐标（单位为 Å）(Coordinate of C1 as the 1st terminal of the cylinder) 0.000000 0.000000 -0.602676 // 作为圆柱第 2 个端点的 C3 的坐标（单位为 Å）(Coordinate of C3 as the 2nd terminal of the cylinder) 2 // 圆柱半径设为 2 Å (Radius of the cylinder is set to be 2 Å) 现在你可以找到所定义区域内格点数据的统计信息：


```text
The minimum value:  0.27234472E-17 at   -6.000000   -6.000000   -9.152823 Bohr
```


![](../imgs/p741_295.png)

<!-- p.742 -->




```text
The maximum value:  0.70592762E+02 at   -0.013983   -0.013983   -1.094723 Bohr
Differential element:   0.0015254705 Bohr^3
Average value:  0.24053135E-02
Root mean square (RMS):  0.11805020E+00
Standard deviation:  0.11800212E+00

Volume of positive value space:                103.2133362853 Bohr^3
Volume of negative value space:                  0.0000000000 Bohr^3
Volume of all space:                           103.2133362853 Bohr^3

Summing up positive values:               4242.9729279471
Summing up negative values:                  0.0000000000
Summing up all values:                    4242.9729279471

Integral of positive data:                  6.4725301753
Integral of negative data:                  0.0000000000
Integral of all data:                       6.4725301753

X,Y,Z of barycenter (in Bohr)
Positive part:         -0.00015137         -0.00015137         -0.00320043
Negative part:                 NaN                 NaN                 NaN
Total:                 -0.00015137         -0.00015137         -0.00320043
```

如黄色高亮所示，当前格点数据即电子数在圆柱区域内的积分为 6.472。现在 Multiwfn 会询问你是否将参与统计的格点导出为当前文件夹下的 grid.xyz 文件，我们选择 y。然后我们用 VMD 程序显示 grid.xyz 和分子结构。将图形效果调整为使格点显示为粉色小点后，你将看到如下图所示。显然格点确实分布在我们预期的区域内。


![](../imgs/p742_296.png)
