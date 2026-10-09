# 其它功能，第3部分(300)(Other functions, part 3 (300))

> Multiwfn manual, p.437–457.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.437 -->



MOs 的能量与系数矩阵经 F=SCEC-1 关系产生 (2) 输入含有 F 的文件的路径，然后将加载该矩阵，详见本手册 Appendix 7。此后，产生 NAdOs 期间将评价 NAdOs 能量并记录到 NAdOs.mwfn。

用 BOD 与 NAdO 分析实际化学体系的实例见 Section 4.200.20。

所需信息：原子坐标、基函数。


### 3.200.21 在占据轨道间执行 Löwdin 正交化

有时，占据轨道彼此不正交归一。例如，经 Section 3.100.19 所述功能由多个单体波函数组合的波函数就是一例。本功能在占据轨道间执行 Löwdin 正交化，使它们形成正交归一集。内存中的系数矩阵与密度矩阵将在本功能中更新。

本功能仅支持单行列式波函数的限制性闭壳层与非限制性开壳层形式。对后者，分别在 α 占据轨道间与 β 占据轨道间执行 Löwdin 正交化。

所需信息：原子坐标、基函数。


## 3.300 其它功能，第3部分(300)(Other functions, part 3 (300))


### 3.300.1 查看晶胞中的自由区域并计算自由体积

本功能用于可视化由分子动力学模拟产生的晶胞或实验晶体中的自由区域。也可计算自由区域的体积。本功能特别适用于表征含孔体系的结构，如多孔材料与煤。

算法 本功能计算以下两种格点数据，其等值面用于图形化展示自由区域，换言之，即未被原子占据的区域。

(1) 原始格点数据 所有格点值初始设为 1，然后循环所有格点，若某格点与任何原子的距离小于该原子的 Bondi van der Waals (vdW) 半径，则该格点值置为 0，表示已被占据。

自由区域的体积，即自由体积，以占据格点总数乘以格点体积计算。占据百分比以自由体积除以整个晶胞体积得到。

(2) 平滑格点数据

<!-- p.438 -->


原始网格数据的等值面始终是不光滑的，因此图形效果很差。为了避开这一问题，可以计算平滑后的网格数据。其思想很简单：每个原子没有明确的边界，而是表示为一个平滑变化的开关函数(switching function)。支持三种开关函数，它们都随着距原子核的径向距离从0到无穷大而从1.0衰减到0.0，其衰减行为受相关参数影响：

- 高斯函数(Gaussian function)（未归一化）。关于高斯函数的原始表达式见Wikipedia。半高全宽(FWHM)越大，函数衰减得越慢

- Becke函数（变换后）。该函数的原始表达式见3.18.0节。迭代次数越小，函数衰减得越慢

- 误差函数(Error function)（变换后）。关于误差函数的原始表达式见Wikipedia。比例因子(scale factor)越大，函数衰减得越慢

为了直观比较它们，下图将这些函数的特征绘制在一起。它们等于0.5的位置被设为碳的vdW半径

如你所见，高斯函数衰减缓慢，而变换后的Becke函数和误差函数变化相对陡峭，其陡峭程度取决于参数。

有了开关函数，平滑后的网格数据很容易计算：对于任一格点，其值初始设为1.0，然后减去每个原子的开关函数值；之后若发现该值为负，则将其置为零。0.0和1.0的值分别意味着该格点被完全占据和完全空闲；而0.0与1.0之间的值表示该格点被部分占据，值越低占据程度越高。为了基于平滑后的网格数据可视化空闲区域，通常可将等值(isovalue)设为0.5，但也可以适当调整以改善图形效果。

用法(Usage) 本功能支持任何种类的晶胞，包括非正交晶胞。你可以使用任何包含晶胞信息的文件作为输入文件，例如.cif、.gro、带CRYST1字段的.pdb等，关于此点的完整介绍见2.9.3节。其它载有原子信息的文件也可作为输入文件，但晶胞将被假定为正交晶胞。

载入输入文件后，应进入主功能300的子功能1，然后你会看到一个菜单，各选项说明如下

- 1 设置网格并开始计算(Set grid and start calculation)：选择此选项后，Multiwfn会要求你定义


![](../imgs/p438_071.png)

<!-- p.439 -->


计算用的网格，你需要输入网格数据的原点坐标、三个方向的长度和格点间距。若输入文件包含晶胞信息，则三个方向将与晶胞的三条边一致；若不包含，则三个方向将被假定为X、Y和Z。

之后，Multiwfn开始计算上述网格数据，然后输出自由体积(free volume)和空闲区域在整个晶胞中所占的百分比。在后处理菜单中，你可以直接可视化等值面以查看空闲区域，或将网格数据导出为cube文件。

- 2 切换是否考虑周期性边界条件(Toggle considering periodic boundary condition)：当此选项状态为“Yes”时，在计算网格数据期间将考虑盒子中原子的周期性镜像。这种处理使计算开销大得多，但得到的数据真实得多。

- 3 切换是否计算空闲区域的平滑网格数据(Toggle calculating smoothed grid data of free regions)：默认情况下，Multiwfn同时生成原始网格数据和平滑网格数据。若将此选项状态设为“No”，则只生成前者，从而成本会降低一部分。

- 4 设置平滑方法(Set method of smoothing)：在此选项中可选择用于计算平滑网格数据的开关函数。默认是比例因子为1.0的误差函数，通常这是合适的选择。

- 5 切换是否使等值面在边界处闭合(Toggle making isosurface closed at boundary)：当状态设为“Yes”时，若在盒子边界处存在等值面，等值面看起来会闭合。若将状态切换为“No”，则等值面在边界处看起来是敞开的。

- 6 设置用于计算自由体积和原始空闲区域的vdW半径比例因子(Set scale factor of vdW radii for calculating free volume and primitive free region)：若此选项的值不是默认的1.0而是设为值x，则用于计算原始网格数据的vdW半径将被缩放x倍。显然此选项会影响原始网格数据的等值面和计算出的自由体积。

本功能的代码效率很高，甚至可以用它研究包含数万个原子的体系。当你发现计算成本太高而无法承受时，应考虑以下解决办法：

(1) 使用更好的CPU。本功能的代码已完全并行化，因此CPU核心越多，计算时间越低。

(2) 使用更大的格点间距。显然，间距越大，等值面图越差，输出的自由体积精度越低。

(3) 不考虑周期性边界条件。成本将降低一个数量级，但某些边界区域的等值面会变得不真实，自由体积甚至会产生误导。

使用本模块的一个例子见4.300.1节。所需信息：原子坐标


### 3.300.2 将原子径向密度拟合为多个STOs或GTFs的线性组合

本功能用于将原子径向密度拟合为多个1s型Slater


<!-- p.440 -->


型轨道(STOs)或S型Gaussian型函数(GTFs)的线性组合，从而之后可用解析方式求值原子径向密度。拟合涉及许多技术细节，将在3.300.2.1节介绍，然后本模块的用法将在4.300.2.2节描述。使用本模块进行拟合的实际例子见4.300.2节。

### 3.300.2.1 算法与技术细节

基本思想(Basic idea) 本功能的目的是进行如下拟合

$$\rho(r)\approx\rho^{\mathrm{f i t}}(r)\quad\forall r$$

$$\rho^{\mathrm{fit}}(r)\left\{\begin{aligned}&\sum_{i\in\mathrm{STO}}c_{i}e^{-\zeta r}\\ &\sum_{i\in\mathrm{GTF}}c_{i}e^{-\zeta r^{2}}\end{aligned}\right.$$

其中{c}为待拟合系数，{ζ}为待拟合指数，r为到核位置的径向距离。

拟合类型(Fitting type) 为实现拟合，应定义一组拟合点。拟合本质上对应于最小化最小二乘残差，该残差衡量拟合点处实际密度与拟合密度之间的总体误差。有三种定义残差的方式，对应不同的拟合类型：

$$\mathrm{(3)}Minimizing~error~of~radial~distribution~function~(RDF):\sum_{i}\Big[4\pi r_{i}^{2}\Big(\rho_{i}-\rho_{i}^{\mathrm{fit}}\Big)\Big]^{2}$$

$$\mathrm{(3)}Minimizing~error~of~radial~distribution~function~(RDF):\sum_{i}\Big[4\pi r_{i}^{2}\Big(\rho_{i}-\rho_{i}^{\mathrm{fit}}\Big)\Big]^{2}$$

$$\mathrm{(3)}Minimizing~error~of~radial~distribution~function~(RDF):\sum_{i}\Big[4\pi r_{i}^{2}\Big(\rho_{i}-\rho_{i}^{\mathrm{fit}}\Big)\Big]^{2}$$

在上述公式中，{i}为置于不同径向距离处的拟合点，ri表示点i的径向距离

ρi是基于载入的波函数文件在点i处计算的球平均化(即球面平均)电子密度。在Multiwfn中，使用170个Lebedev角向格点进行球平均。

通常，拟合类型2优于其它类型，因此为默认，因为这样拟合的密度能在整个范围内复现实际密度，包括电子密度相当小的尾部区域。类型1拟合的密度只能很好地代表非常靠近原子核的区域，因为该区域的电子密度明显大于其它区域。当通过目视检查拟合密度曲线发现拟合类型2效果不好时，改用类型3可能得到更好的结果。若类型2和3效果都不好，有时先用类型1再用类型2（即把类型1的拟合参数作为类型2的初猜）会很有用，或先用类型3再用类型2。

拟合函数(Fitting functions) 在本模块中支持作为拟合函数的STO和GTF，它们是量子化学计算中最重要的函数。

拟合质量对拟合函数的数目相当敏感。显然，原则上


<!-- p.441 -->


拟合函数越多，拟合误差越小，拟合期间的时间成本越高。

在Multiwfn中，最小二乘型拟合通过Levenberg-Marquardt (LM)算法进行，该算法是一种迭代方法，通过逐步优化参数直至达到收敛容限来最小化残差。需要注意的是，该算法本质上是局域最小化方法，因此，得到的拟合系数和指数可能依赖于初猜。

拟合函数的系数应始终参与拟合，然而，指数既可一起拟合，也可固定在初猜以减小参数空间维度从而使收敛更容易。显然，对于给定数目的拟合函数，若其指数在拟合期间可变，原则上拟合质量应好于指数固定的情形。

当拟合函数数目较大时（例如>20），通常不建议同时拟合指数和系数，因为此时收敛往往相当困难，成本相当高，有时执行LM算法的例程不能正常工作。

删除冗余拟合函数(Removing redundant fitting functions) 为了达到好的拟合质量，通常应采用数十个具有从小到大固定指数的拟合函数，这些指数常以均匀递增(even-tempered)方式生成，

即ζi=a×bi。例如，ζi=0.05×2(i-1)，i=1, 2, 3 ... 30。在这种情况下，有时一个或多个拟合函数是冗余的，因为其指数过大或过小，导致严重的数值问题。为了识别并删除具有不合理指数的有害冗余拟合函数，当选择GTF作为拟合函数时，Multiwfn默认采用以下三条规则：

(1) 删除具有相对不显著系数的陡峭拟合函数(ζ>105且同时c<5)和具有可忽略系数的平坦拟合函数(ζ<3且c<10-4)。

(2) 显然，拟合密度在任何地方都应为正。若在某个检测点发现拟合密度为负，则删除对该点负贡献最大的拟合函数。检测点包括所有拟合点以及相邻均匀放置的拟合点之间的中点。通常过大的指数易导致非常靠近原子核区域出现负值，而过小的指数易导致尾部区域出现负值。

(3) 电子密度的变化应随径向距离增大而单调减小。该要求在使用前一半拟合点所跨范围内的双倍稠密网格检查；若违反，则删除指数最大的拟合函数，因为该问题通常由过大的指数引起。

每次只删除一个冗余函数。删除后，Multiwfn将重新拟合。拟合重复进行，直至找不到冗余拟合函数。

有时从结果中你可能发现两个拟合函数具有非常接近的指数，这表明可删除其中之一再重新拟合，结果不会明显变差。然而，这种冗余拟合函数不会被Multiwfn自动删除，你可以在重新拟合前在设置初猜的界面中合并它们。

缩放系数(Scaling coefficients) 拟合密度在全空间的积分可能偏离实际电子数(Nelec)，显然这破坏了拟合密度的物理意义，使其在许多场景下无用。为解决该问题，拟合系数应按一个因子缩放：


<!-- p.442 -->


$$\lambda=\frac{N_{elec}}{\int4\pi r^{2}\rho^{fit}(r)\mathrm{d}r}$$

在Multiwfn中，分母中的积分用100个积分点的第二类Chebyshev Gaussian求积来求值。

拟合点的数目与步长(Number and stepsize of fitting points) 通常感兴趣的原子径向区域是r = 0-4 Å，因此拟合点应充分覆盖该区域。拟合点之间的间距越小，拟合质量越高。默认情况下，Multiwfn采用相当精细的网格，格点间距为0.001 Å，相应地，默认格点数为4000。拟合点的默认设置相当合适，无特殊理由不应更改。的确，适当增大格点间距并相应减少拟合点数目可节省计算时间，然而，鉴于单原子的电子密度计算通常很便宜，增大格点间距不是好主意。

通常，使用小间距的均匀放置拟合点已完全足以达到满意的拟合质量，然而，Multiwfn也支持将第二类Gauss-Chebyshev点加入拟合点。这种点在原子核周围采样非常密集，但在长程稀疏采样；换言之，格点间距与径向距离正相关。显然，将第二类Gauss-Chebyshev点考虑在内会或多或少改善非常靠近原子核区域的拟合质量。然而，只要均匀放置网格的间距足够小（例如默认的0.001 Å），改善并不显著，因此默认拟合中不包含这种点。

检查拟合质量(Examining fitting quality) 拟合后，检查拟合质量至关重要，以确保输出的系数和指数在实践中确实可靠且有意义。有几种检查方法：

(1) 检查均方根误差(RMSE)，其定义为

$$RMSE=\sqrt{\frac{\sum_{i}^{N}(\rho_{i}-\rho_{i}^{fit})^{2}}{N}}$$

其中N为拟合点数。RMSE越低，总体拟合质量越好。你也可用该量比较各种拟合设置之间的拟合精度。

(2) 拟合点处拟合密度与实际密度之间的Pearson相关系数(r)和r2。值越接近1，拟合质量越好。

(3) 目视比较实际密度与拟合密度曲线。这是最严格的检查拟合质量的方法。两条曲线应充分接近。

(4) 检查拟合密度的积分。积分应在不同数目的求积点下求值，例如60, 80 ... 300。若拟合系数和指数确实合理，在所有情况下积分都应非常接近原子的实际电子数。

(5) 用比拟合点稠密一倍或两倍的网格在宽广范围内检查拟合密度。不应发现负密度，拟合密度应单调变化。


<!-- p.443 -->


### 3.300.2.2 用法(Usage)

拟合的常用步骤(Common steps of fitting) 要使用本功能进行拟合，通常应做以下步骤(1) 载入原子的波函数文件。文件应至少包含GTF信息（例如.mwfn/.wfn/.fch/.molden），原子必须位于原点。

(2) 进入主功能300的子功能2。(3) 选择选项3并选择一种定义初猜的方式，然后简要检查屏幕上打印的初猜，再返回上一级菜单。

(4) 选择选项1开始拟合。(5) 仔细检查屏幕上打印的信息，然后你可用适当的选项进一步检查拟合质量。

拟合前的选项(Options before fitting) 本模块界面中选项的含义与细节说明如下

- 开始拟合(Start fitting)：选择此选项后，Multiwfn将做以下事情（某些过程可能按用户要求跳过）

· 打印拟合函数的初猜 · 计算拟合点处的球平均径向原子密度 · 使用Levenberg-Marquardt算法优化拟合函数的系数/指数。在此过程中可能删除一些冗余拟合函数

· 按指数对拟合函数排序 · 计算拟合密度的积分并相应缩放系数 · 打印拟合函数的最终系数和指数 · 打印误差统计 然后你会看到用于检查拟合质量或导出数据的菜单，各选项将在后面描述。

- 切换拟合函数类型(Switch type of fitting functions)：你可用此选项在STO与GTF之间切换拟合函数类型

- 检查或设置系数与指数初猜(Check or set initial guess of coefficients and exponents)：进入此选项后，首先显示当前拟合函数的信息。默认情况下未设置拟合函数，因此在开始拟合前你应用以下选项之一定义它们：

· 1 从文本文件载入初猜(Load initial guess from text file)：经由此选项，将从给定的纯文本文件载入系数和指数，其格式应如下所示：


```text
4.0 1000
2.0 100
1.0 1.5
```

此文件定义了三个拟合函数，第一列和第二列分别为初始系数和指数。显然，这是定义拟合函数数目与初始参数的最灵活方式。

以下选项为方便起见采用预置设置（精度与函数数目：3>4>5>7>2）：

· 2 用少数指数可变的STOs进行粗略拟合(Crude fitting by a few STOs with variable exponents)：此选项旨在进行粗略拟合，只采用少数STOs。指数将在拟合期间优化以使拟合质量更好。具体而言，当元素分别位于周期表第一、第二、


<!-- p.444 -->



第三&四行及之后各行时，分别采用1、2、4、6个STOs。此选项设置的拟合函数初始参数通常合理，然而，拟合偶尔可能因初始参数不合适而失败，此时你应尝试用选项1载入手动提供的参数代替。

· 3 用30个指数固定的GTFs进行理想拟合(Ideal fitting by 30 GTFs with fixed exponents)：若想在整个范围内准确拟合实际密度，使用此选项设置的拟合函数通常是最佳选择。将采用30个GTFs，为保证数值稳定性并显著降低拟合成本，只拟合系数，而指数保持在初始值，初始值按

ζi=0.05×2(i-1)生成，其中整数i从1变到30。

· 4 用15个指数可变的GTFs进行精细拟合(Fine fitting by 15 GTFs with variable exponents)：此选项使用的GTFs数目比选项3少，但指数同时优化。即使指数可变，此选项的拟合质量不如选项3完美，同时拟合成本更高，且存在Levenberg-Marquardt算法迭代无法收敛的危险。

· 5 用10个指数可变的GTFs进行精细拟合(Fine fitting by 10 GTFs with variable exponents)：比选项4便宜，拟合精度略有降低。

· 7 用不超过10个指数可变的GTFs进行较精细拟合(Relatively fine fitting by no more than 10 GTFs with variable exponents)：此选项以最经济的方式用GTFs拟合，前18号元素用6个GTFs，更重的元素用10个GTFs。虽然便宜，但通常此选项已足够满意。

最后，选项“10 合并两个拟合函数(10 Combine two fitting functions together)”能用一个新函数替换两个特定的拟合函数，新函数的指数为二者平均值，系数为二者之和。此选项主要用于手动删除线性相关函数。

- 设置拟合容限(Set fitting tolerance)：值越小，拟合的数值精度越好而拟合成本越高。通常默认值能保证高数值精度。

- “设置均匀放置拟合点数目(Set number of evenly placed fitting points)”和“设置拟合点间距(Set spacing between fitting points)”：默认的均匀放置点数(4000)足够大，默认间距(0.001 Å)足够精细，相应的拟合点分布于r = 0.001至4.0 Å。若想将更长程的点纳入拟合，或想降低拟合成本（时间成本基本与拟合点数成正比），可适当调整这两个选项。

- 切换是否将系数缩放到实际电子数(Toggle scaling coefficients to actual number of electrons)：当此选项状态为“Yes”（默认）时，在计算拟合密度积分后，将按上一节所述方式缩放拟合函数的系数。始终建议进行缩放。

- 选择拟合类型(Select fitting type)：你可用此选项选择如何进行拟合，包括“最小化绝对误差(Minimizing absolute error)”、“最小化相对误差(Minimizing relative error)”和“最小化径向分布函数(RDF)误差(Minimizing radial distribution function (RDF) error)”，它们已在上一节介绍。第二种通常最推荐，因此为默认。

- 切换是否固定指数(Toggle fixing exponents)：当此选项状态设为“Yes”时，Multiwfn将在拟合过程中同时优化拟合函数的系数和指数。若想把指数保持在其初猜，此选项应切换为“No”。

- 切换是否按指数排序函数(Toggle sorting functions according to exponents)：当此选项状态为“Yes”（默认）时，Multiwfn将重排拟合函数使其指数从低到高排列。

- 切换是否删除冗余拟合函数(Toggle removing redundant fitting functions)：当此选项状态为“Yes”（默认）时，如上一节所述，拟合期间将自动删除冗余拟合函数。这对保证数值稳定性和结果合理性很重要，因此


<!-- p.445 -->



通常应启用。

- 设置第二类Gauss-Chebyshev拟合点数(Set number of second kind Gauss-Chebyshev fitting points)：如上一节所述，若想把对近核区域重采样的点加入拟合，可将均匀分布点与一些第二类Gauss-Chebyshev点组合作为实际采用的拟合点。此选项控制采用的第二类Gauss-Chebyshev点数。当值设为0（默认）时，将不采用这种点。

- 设置最大函数调用次数(Set maximum number of function calls)：此选项设置误差最小化期间的最大函数调用次数。若最小化达到此条件仍未收敛，最小化将停止并报告未收敛结果。

拟合后的选项(Options after fitting) 在拟合完成后出现的菜单中，有许多用于检查或导出结果的选项，也有一些用于检查拟合质量的选项。由于大多数不言自明，只在这里描述少数几个：

- 使用对数标度可视化实际密度与拟合密度曲线(Visualize actual density and fitted density curves using logarithmic scaling)：此选项在目视检查拟合质量时很有用，蓝色和黑色曲线分别显示拟合密度和实际密度。显然，两条曲线越接近，拟合质量越好。从此图你也可了解哪些区域拟合得好或不好。

- 将0至10 Angstrom的拟合密度用双倍稠密网格导出到当前文件夹的fitdens.txt(Export fitted density from 0 to 10 Angstrom with double dense grid to fitdens.txt in current folder)：此选项在宽广范围内检查拟合密度质量时有用。你可用此选项导出fitdens.txt文件，若从中发现拟合密度如预期变化（例如无负值、平滑单调衰减），则拟合密度应可靠可用。

- 检查拟合密度的积分(Check integral of fitted density)：此选项用不同数目的求积点（从40到300，步长20）的Gaussian积分计算拟合密度的径向积分。若结果都接近实际电子数，则意味着拟合密度应可靠。

- 检查给定径向距离处的拟合密度(Check fitted density at a given radial distance)：经由此选项，你可通过输入其值来检查特定径向距离处的拟合密度。这也是使拟合密度合理化的有用方式。

- 将系数与指数以Fortran代码形式输出到.txt文件(Output coefficients and exponents as Fortran code to a .txt file)：此选项以Fortran代码形式写入拟合系数和指数，然后你可把导出文件中的信息复制到你的Fortran程序中以利用该数据。

使用本模块进行拟合的实际例子见4.300.2节。所需信息：原子坐标，GTFs


### 3.300.4 模拟扫描隧道显微镜(STM)图像

理论(Theory) 扫描隧道显微镜(STM)是在原子水平成像化学体系的相当常见的实验技术，也与样品的电子结构密切相关，更多信息见wiki页面。在STM成像过程中，将导电针尖置于样品上方，同时在二者之间施加偏压(V)。由于量子隧道


<!-- p.446 -->



效应，在适当的距离间隔（通常4~7 Å）和V下，针尖与样品之间可形成隧道电流(I)。在不同位置，由于针尖与样品之间相互作用不同，I不同，本质上观测到的STM图像表征函数I(r)。STM实验可用下图说明

STM有两种模式：

- 恒高模式(Constant height mode)：针尖的z坐标固定在给定值而扫描x和y。此时的二维STM图像对应于I(x,y)函数。

- 恒流模式(Constant current mode)：进行x和y的二维扫描，对每个(x,y)，逐步调节针尖的z坐标直至找到I等于特定值的z位置(zc)。给定电流下此模式的STM图像对应于zc(x,y)函数。显然，生成恒流模式的STM图像比恒高模式更耗时，因为需要考虑额外的维度(z)。

尽管有许多计算模拟STM图像的方法，唯一流行的是Tersoff和Hamann推导的模型，见Phys. Rev. B, 31, 805 (1985)和书Introduction to Scanning Tunneling Microscopy (2ed, Julian Chen, 2008)第6章。原则上，要确定I必须知道针尖的真实特征，而这通常未知。Tersoff-Hamann模型的关键点是把针尖替换为点探针，从而推导I的公式大为简化（Tersoff和Hamann也讨论了针尖局部为特定半径球面的情形，但这里不考虑）。原始Tersoff-Hamann模型对应于小V和低温极限，且只适用于周期体系；若显式考虑有限V，孤立体系的I可表示为


$$I(\mathbf{r})\propto\sum_{a}^{E_{\mathrm{F}}\rightarrow E_{\mathrm{F}}+e V}|\varphi_{a}(\mathbf{r})|^{2}\qquad(V>0)$$

<!-- formula-ocr: formula_p446_327.png 已替换为LaTeX, 原图保留备查 -->

其中i表示能量在EF+eV与EF之间的占据MOs，a表示能量在EF与EF+eV之间的非占据MOs。EF为Fermi能级，对孤立体系没有明确定义，但通常取为EHOMO与ELUMO的平均值。e为元电荷，为


![](../imgs/p446_072.png)

<!-- p.447 -->


正值(1.602E-19 C)。当V为正时，针尖中的电子隧穿到样品的空态；当V为负时，电子从样品的占据态隧穿出来进入针尖。

注：有些文献用-eV而非+eV，这是因为这些文献中的e对应于电子所带电荷而非元电荷。虽然上述公式通常被称为Tersoff-Hamann模型，严格说并非Tersoff和Hamann提出的形式。

上述公式表明I(r)与r处由EF+eV与EF之间（V<0时）或EF与EF+eV之间（V>0时）的MOs贡献的局域态密度(LDOS)成正比（注意此处的LDOS与3.12.4节介绍的定义不同），因此，若轨道波函数可得从而可计算LDOS，则STM图像可直接得到。在以此方式讨论模拟STM图像时，建议把I的单位写作LDOS的单位，在Multiwfn中对应于a.u.。

以上述方式模拟的STM图像不能与实验严格比较，因为未考虑STM针尖的实际特征而简化为点（因此模拟STM图像具有无限高分辨率）。还注意由于引入近似，用现有模型无法确定I的量级，故只有不同位置间I的相对差异有意义并可讨论。

用法(Usage) 要在Multiwfn中模拟STM图像，建议使用包含基函数信息的文件，例如.mwfn、.fch和.molden。也可接受只含GTF信息如.wfn的格式，然而此时不能模拟V>0的STM图像，因为它们只含占据MOs信息。

由于STM模拟基于分子轨道，理论方法只支持HF和KS-DFT（双杂化泛函除外），而不支持MP2和CASSCF等多组态方法。限制性闭壳层、限制性开壳层和非限制性开壳层都支持。

主功能300的子功能4对应于STM模拟功能。进入此功能后，请仔细阅读屏幕上的提示，它告诉你默认Fermi能级和偏压如何确定。在界面中，你可自定义EF、V、格点数、STM的空间范围。也可选择STM图像的模式，恒高（默认）与恒流模式都可用。在设置合适后，可选择选项0开始计算绘制STM图所需的数据，计算中考虑的MOs将显示在屏幕上，以便你检查EF和V是否已恰当定义。注意计算成本完全由格点数决定，格点越多，图像越光滑，而成本越高。

恒高与恒流模式模拟STM图像的方式有所不同，如下所述：

- 恒高模式(Constant height mode)：计算前，应恰当设置X和Y的范围，默认由边界原子的位置外扩3 Bohr确定。待计算平面的默认Z位置比最高原子（即Z坐标最大的原子）高0.7 Å。选择选项0计算二维平面每一点的电流后，你会看到绘制STM图像的界面，所有选项不言自明故不再描述（选项与主功能4后处理菜单中的很相似）。默认情况下，色标下限为0，而上限自动设为平面数据中的最大I。

- 恒流模式(Constant current mode)：应先选择一次选项1以将模式从


<!-- p.448 -->



默认的恒高模式切换到恒流模式。然后应恰当定义X、Y和Z的计算范围。默认X和Y范围与恒高模式相同，Z的默认下限和上限分别比最高原子高0.7和2.5 Å。选择选项0后，Multiwfn将开始计算I的三维网格数据，然后你可用相应选项可视化隧道电流的等值面图、将网格数据导出为cube文件，或可视化二维STM图像。对于后者，需输入隧道电流的值，然后Multiwfn将在每个(x,y)点估计I等于该值的z值(zc)，得到的平面数据zc(x,y)便可经由屏幕上的相应选项直接绘制为平面图。

模拟STM图像的例子见4.300.4节。所需信息：原子坐标，GTFs


### 3.300.5 计算电偶极/多极矩与电子空间范围

本功能基于解析求值的积分（或基于原子电荷，见后）计算电偶极、四极、八极和十六极矩以及电子空间范围<r2>。注意3.18.3节描述的功能也能计算偶极、四极和八极矩，然而它是基于积分格点数值计算数据，因此显然更慢，其精度略低于本功能。本功能打印的信息如下所示。

偶极矩(Dipole moment)：


$$\mathbf{\mu}=\left[\begin{matrix}{\mu_{x}}\\ {\mu_{y}}\\ {\mu_{z}}\\ \end{matrix}\right]=\sum_{A}q_{A}\left[\begin{matrix}{X_{A}}\\ {Y_{A}}\\ {Z_{A}}\\ \end{matrix}\right]-\int\left[\begin{matrix}{x}\\ {y}\\ {z}\\ \end{matrix}\right]\rho(\mathbf{r})\mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p448_328.png 已替换为LaTeX, 原图保留备查 -->

其中XA、YA和ZA为原子A的三个笛卡尔坐标。qA为原子A的核电荷。x、y和z为电子位置的三个笛卡尔坐标。

四极矩(标准笛卡尔形式)(Quadrupole moment (standard Cartesian form))：

$$\mathbf{\mu}=\left[\begin{matrix}{\mu_{x}}\\ {\mu_{y}}\\ {\mu_{z}}\\ \end{matrix}\right]=\sum_{A}q_{A}\left[\begin{matrix}{X_{A}}\\ {Y_{A}}\\ {Z_{A}}\\ \end{matrix}\right]-\int\left[\begin{matrix}{x}\\ {y}\\ {z}\\ \end{matrix}\right]\rho(\mathbf{r})\mathrm{d}\mathbf{r}$$

四极矩(无迹笛卡尔形式)(Quadrupole moment (traceless Cartesian form))：

$$\mathbf{\mu}=\left[\begin{matrix}{\mu_{x}}\\ {\mu_{y}}\\ {\mu_{z}}\\ \end{matrix}\right]=\sum_{A}q_{A}\left[\begin{matrix}{X_{A}}\\ {Y_{A}}\\ {Z_{A}}\\ \end{matrix}\right]-\int\left[\begin{matrix}{x}\\ {y}\\ {z}\\ \end{matrix}\right]\rho(\mathbf{r})\mathrm{d}\mathbf{r}$$

$$\mathbf{\mu}=\left[\begin{matrix}{\mu_{x}}\\ {\mu_{y}}\\ {\mu_{z}}\\ \end{matrix}\right]=\sum_{A}q_{A}\left[\begin{matrix}{X_{A}}\\ {Y_{A}}\\ {Z_{A}}\\ \end{matrix}\right]-\int\left[\begin{matrix}{x}\\ {y}\\ {z}\\ \end{matrix}\right]\rho(\mathbf{r})\mathrm{d}\mathbf{r}$$


<!-- p.449 -->



$$\Theta_{xyz}=\sum_{A}q_{A}X_{A}Y_{A}Z_{A}-\int xyz\rho(\mathbf{r})\mathrm{d}\mathbf{r}$$

注意由于笛卡尔形式的四极矩是对称矩阵，只有6个分量是唯一的。

电子空间范围定义为〈𝑟2〉= ∫(𝑥2 + 𝑦2 + 𝑧2)𝜌(𝐫)d𝐫。本质上，它就对应于电子贡献的四极矩张量（笛卡尔形式）的迹的负值。Multiwfn不仅打印〈𝑟2〉，还打印它的三个笛卡尔分量，以便你了解其来源。关于〈𝑟2〉的非常详细的介绍见我的博客文章：http://sobereva.com/616（中文）。

四极矩(球谐形式)(Quadrupole moment (spherical harmonic form))：


$$\Theta_{xyz}=\sum_{A}q_{A}X_{A}Y_{A}Z_{A}-\int xyz\rho(\mathbf{r})\mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p449_329.png 已替换为LaTeX, 原图保留备查 -->

笛卡尔形式的八极矩是三阶张量，有3×3×3=27个分量，然而只有10个元素是唯一的。例如，XYZ分量按如下计算，其它分量类似计算


$$\Theta_{x y z z}=\sum_{A}q_{A}X_{A}Y_{A}Z_{A}Z_{A}-\int x y z z\rho(\mathbf{r})\mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p449_330.png 已替换为LaTeX, 原图保留备查 -->

球谐形式的八极矩：

Q 3,0 =Θ−Θ (1/ 2)(53) zzzrrz

$$\Theta_{xyz}=\sum_{A}q_{A}X_{A}Y_{A}Z_{A}-\int xyz\rho(\mathbf{r})\mathrm{d}\mathbf{r}$$

$$\mathcal{Q}_{2,-1}=\sqrt{3}\Theta_{yz}\qquad\mathcal{Q}_{2,1}=\sqrt{3}\Theta_{xz}$$

QQ 3, 33,3 − =Θ−Θ=Θ−Θ 5 / 8(3)5 / 8(3) xxyyyyxxxyyx

$$\Theta_{xyz}=\sum_{A}q_{A}X_{A}Y_{A}Z_{A}-\int xyz\rho(\mathbf{r})\mathrm{d}\mathbf{r}$$


$$|\mathbf{Q}_{3}|=\sqrt{\sum_{m=-3}^{3}(Q_{3,m})^{2}}$$

笛卡尔形式的十六极矩是四阶张量，有3×3×3×3=81个分量，然而只有15个元素是唯一的。例如，XYZZ分量按如下计算，其它分量类似计算


$$\Theta_{xyzz}=\sum_{A}q_{A}X_{A}Y_{A}Z_{A}Z_{A}-\int xyzz\rho(\mathbf{r})\mathrm{d}\mathbf{r}$$


<!-- p.450 -->



本功能还打印正电荷中心。其X分量定义为


$$\mathbf{\mu}=\left[\begin{matrix}{\mu_{x}}\\ {\mu_{y}}\\ {\mu_{z}}\\ \end{matrix}\right]=\sum_{A}q_{A}\left[\begin{matrix}{X_{A}}\\ {Y_{A}}\\ {Z_{A}}\\ \end{matrix}\right]$$

<!-- formula-ocr: formula_p450_333.png 已替换为LaTeX, 原图保留备查 -->

还打印负电荷中心。例如，X分量按如下求值

基于原子电荷的求值(Evaluation based on atomic charges) 若你的输入文件是.chg或.pqr，本功能也可使用，但偶极与多极矩都基于文件中记录的原子电荷计算。例如，此时偶极矩表示为


$$\boldsymbol{\mu}=\begin{bmatrix}\mu_{x}\\mu_{y}\\mu_{z}\end{bmatrix}=\sum_{A}q_{A}\begin{bmatrix}X_{A}\\Y_{A}\\Z_{A}\end{bmatrix}$$

其中在此语境下qA代表原子A的原子电荷。

本功能的一个简单例子见4.300.5节。所需信息：原子坐标，GTF信息或基函数或原子电荷。


### 3.300.6 通过输入Fock矩阵计算现有轨道的能量

本功能是主功能300的子功能6，它是用于求值现有轨道（即内存中存储的轨道）能量的通用模块。你的输入文件中必须有基函数信息，进入本功能后，需向Multiwfn提供Fock或Kohn-Sham (KS)矩阵（详见本手册附录7），然后轨道的能量将作为Fock或KS算符的期待值求值。

本功能应用于计算自然跃迁轨道(NTO)能量的说明见4.300.6节。

所需信息：基函数，含Fock/KS矩阵的纯文本文件


### 3.300.7 与当前体系相关的几何操作

注：本节的中文版及丰富例子是我的博客文章“介绍Multiwfn中非常有用的几何操作与坐标变换功能”(http://sobereva.com/610)。

本功能是主功能300的子功能7，旨在对当前体系进行各种与几何相关的操作，这些操作可能涉及特殊目的研究。注意


<!-- p.451 -->



轨道系数矩阵因旋转与反演操作引起的变换未被本功能考虑。

在本功能中，你可进行许多几何操作，它们将在下面简要提及。你可多次使用它们，效果将累积。你可随时选择选项0在GUI窗口中可视化当前几何。你也可用选项-1、-2、-3和-4分别将当前几何导出到.xyz、.pdb、.gjf和.cif文件。经由选项-9，你可恢复从输入文件载入的初始几何。

- 1 按平移矢量平移选定原子(Translate selected atoms according to a translation vector) 将要求你选择一组原子并输入平移矢量，选定原子将用该矢量平移

- 2 平移体系使选定原子的中心位于原点(Translate the system such that the center of selected atoms is at origin) 将要求你选择一组原子并选择其中心类型（几何中心、质心或核电荷中心），然后整个体系将被平移使它们的中心恰好位于原点。

- 3 绕笛卡尔轴或化学键旋转选定原子(Rotate selected atoms around a Cartesian axis or a bond) 将要求你选择一组原子，它们将绕笛卡尔轴、或化学键、或由你指定的特定角度的矢量旋转。用于进行坐标变换的旋转矩阵也将显示在屏幕上。

- 4 应用给定旋转矩阵旋转选定原子(Rotate selected atoms by applying a given rotation matrix) 将要求你选择一组原子并手动输入旋转矩阵(M)，然后每个选定原子的几何将依次经由vnew=Mvold变换，其中v是由原子的X、Y和Z坐标组成的列矢量，或经由wnew=woldM，其中w是由原子的X、Y和Z坐标组成的行矢量。

- 5 使化学键平行于矢量或笛卡尔轴(Make a bond parallel to a vector or Cartesian axis) 体系将被重新取向，使由两个选定原子定义的化学键平行于特定矢量或笛卡尔轴。

- 6 使矢量平行于矢量或笛卡尔轴(Make a vector parallel to a vector or Cartesian axis) 体系将被重新取向，使原坐标系中的矢量平行于特定矢量或笛卡尔轴。例如，你已进行了电子激发计算，想使某激发的跃迁偶极矩恰好平行于X轴，你可用此功能。

- 7 使电偶极矩平行于矢量或笛卡尔轴(Make electric dipole moment parallel to a vector or Cartesian axis) 电偶极矩将自动计算，体系将被重新取向以使电偶极矩平行于特定矢量或笛卡尔轴。此功能仅当你的输入文件包含波函数信息时可用。

- 8 使选定原子的最长轴平行于矢量或笛卡尔轴(Make longest axis of selected atoms parallel to a vector or Cartesian axis) 将要求你选择一组原子，整个体系将被重新取向，使选定原子的最长轴（惯性矩最小的主轴）平行于特定矢量或笛卡尔轴。

- 9 对选定原子作镜面反演(Mirror inversion for selected atoms) 将要求你选择一组原子并选择平面（XY、YZ或XZ），然后对选定原子进行关于该平面的镜面反演。

- 10 对选定原子作中心反演(Center inversion for selected atoms) 将要求你选择一组原子，然后它们的X、Y和Z坐标的符号将


<!-- p.452 -->



被反转。

- 11 使选定原子定义的平面平行于笛卡尔平面(Make the plane defined by selected atoms parallel to a Cartesian plane) 将要求你选择一组原子，用它们的坐标拟合一个平面。然后将要求你选择笛卡尔平面（XY、YZ或XZ），整个体系将被重新取向以使拟合平面平行于选定的笛卡尔平面。

- 12 缩放选定原子的笛卡尔坐标(Scale Cartesian coordinates of selected atoms) 将要求你选择一组原子、要缩放的坐标类型（X或Y或Z或全部）以及要应用的比例因子。然后相应坐标将乘以该比例因子。比例因子也可为负或零。

若你的输入文件包含晶胞信息，在缩放原子坐标后，还将要求你选择是否也缩放晶胞矢量的相应分量。例如，若之前已选择缩放X坐标，则所有晶胞矢量的X分量也将被缩放。

- 13 重排原子顺序(Reorder atom sequence) 此选项支持不同规则重排原子：(1) 按X或Y或Z坐标值 (2) 把非氢原子排在氢之前 (3) 按成键，即让每个孤立片段中的原子序号连续 (4) 按元素序号 (5) 交换两个特定原子 (6) 输入含所有原子新顺序的文件（其格式见屏幕提示） (7) 输入一批原子的序号，然后它们将出现在其它原子之前。在此功能中，你也可选-1以反转原子顺序。

- 15 添加原子(Add an atom)：将要求你输入元素和XYZ坐标，一个新原子将被添加（作为最后一个原子）。

- 16 删除一些原子(Remove some atoms)：将要求你输入原子列表，它们将从当前体系中删除。

- 17 裁剪出一些原子(Crop some atoms)：将要求你输入原子列表，不属于该列表的原子将被删除。

- 18 生成随机位移的几何(Generate randomly displaced geometries) 你可经由此功能获得多个随机位移的几何，新几何将导出到当前文件夹的new.xyz。在生成中，每个选定原子的笛卡尔坐标将被随机位移，位移满足正态分布，标准差由用户输入。位移的考虑方向可由用户设置，例如仅X方向、Y和Z两个方向、所有方向等。若只生成一个几何，每个原子的位移矢量将明确显示在屏幕上。

以下选项与周期体系相关，仅当可从输入文件获得晶胞信息时可用，哪些文件能向Multiwfn提供晶胞信息见2.9.3节。

- 19 平移并复制晶胞（构建超胞）(Translate and duplicate cell (construct supercell)) 此选项用于构建超胞。将要求你输入每个方向的重复数，数目可为正值或负值。例如，在一个方向上，若你输入3，则体系将沿正方向复制两次，从而该方向将有三个重复；若你输入-3，则体系将沿负方向复制三次，最终将有四个重复。

- 20 按晶胞边界使截断分子完整(Make truncated molecules by cell boundary whole) 对于实验分子晶体文件，晶胞边界把分子截断


<!-- p.453 -->



为各自片段是很常见的，这给可视化分子结构带来很大不利。本功能能使每个被截断的分子完整。

- 21 缩放晶胞长度并相应缩放原子坐标(Scale cell length and atom coordinates correspondingly) 将要求你选择方向并输入比例因子，然后该方向的晶胞长度以及原子坐标将被缩放。此选项在你需手动调节晶胞密度时特别有用。

- 22 把晶胞外的所有原子包回晶胞(Wrap all atoms outside the cell into the cell) 有时一些原子位于晶胞外，此选项用于把它们包回当前晶胞；换言之，晶胞外的原子将被晶胞矢量适当平移，使其分数坐标在0.0~1.0范围内。

- 23 沿晶胞轴按给定距离平移体系(Translate system along cell axes by given distances) 将要求你输入每个方向的平移距离（可为正或负），然后体系中的所有原子将被相应平移。注意晶胞不动，因此平移后一些原子可能在晶胞外，然后你可用选项22把它们包回晶胞。

- 24 平移体系使选定部分居于晶胞中心(Translate system to center selected part in the cell) 将要求你输入一批原子的序号，然后整个体系将被平移，使选定原子的几何中心移到晶胞中心。之后，一些原子可能在晶胞外，然后你可用选项22把它们包回晶胞。

- 25 提取分子团簇（中心分子+邻近分子）(Extract a molecular cluster (central molecule + neighbouring ones)) 将要求你输入一个原子的序号，并输入判据（见下），然后整个分子以及与其相邻的第一层其它分子将被提取为分子团簇。此外，团簇中中心分子的原子序号将显示在屏幕上。若想用例如IGMH、IRI和Hirshfeld面分析研究晶体中的分子间相互作用，此功能特别有用。注意若邻近分子的一个原子与所选分子的最近距离小于它们的vdW半径之和乘以你输入的判据，则邻近分子将被纳入提取。通常判据1.2合适，增大它可能得到更大的团簇。

- 26 设置晶胞信息(Set cell information) 经由此选项，你可手动设置当前晶胞的a、b、c大小和α、β、γ角值。你也可手动定义晶胞的三个平移矢量。

- 27 添加边界原子(Add boundary atoms) 边界原子，即位于晶胞壁或棱上的原子，将被检测并作为真实原子添加到当前体系。

- 28 轴互换(Axes interconversion) 你可选择进行互换a ↔ b、a ↔ c或b ↔ c。选定两个分量的原子分数坐标和晶胞矢量长度将被交换。若想改变二维材料的取向，此功能特别有用：若晶胞正交且材料层当前平行于XY平面，而你希望使层平行于YZ平面，则你可用本功能互换a和c轴。

所需信息：原子坐标

<!-- p.454 -->


### 3.300.8 绘制表面距离投影图 (Plot surface distance projection map)

由本功能绘制的表面距离投影图在直观表征分子结构方面非常直观，在识别位阻效应 (steric effect) 方面特别有帮助。它也可用于直观表征固体表面的结构。

简而言之，本功能绘制的是 XY 平面的颜色填充图，其数值对应体系表面相对于给定 Z 层的相对 Z 位置，见下图示意。在每一个 (x,y) 点处，程序从 Zstart 向 Zend 扫描 Z 坐标，直到到达表面为止，终止点的 Z 值相对于起始点的 Z 值即为要绘制的函数值。

在本功能中，当通过相应选项正确设置好所有参数后，你可以选择选项 0 (option 0) 开始计算，随后会进入一个菜单，在其中可以绘制该图，并有许多用于微调图形效果的选项。

显然，为了得到有用的分子表面距离投影图，输入文件中的体系必须置于合适的取向，这是用户的责任。本功能同样适用于诸如二维材料等周期性体系，可以正确考虑周期性边界条件。

一些细节 定义体系表面的方法有三种，可通过本功能界面中的选项 1 (option 1) 选择：

(1) 准分子电子密度的等值面 (Isosurface of promolecular electron density) (2) 基于波函数信息的电子密度的等值面 (Isosurface of electron density based on wavefunction information) (3) 由标度后的原子 Bondi 范德华半径叠加定义的 vdW 表面 (vdW surface defined by superposition of scaled atomic Bondi van der Waals radii)，标度因子可手动输入

如果你的输入文件只包含原子信息，可使用 (1) 和 (3)；若有 GTF 信息可用，也可使用 (2)。计算开销为 (2) > (1) > (3)。通常推荐 (1)，因为其表面比 (3) 光滑得多，即使对相当大的体系其开销也不高，而且任何包含原子信息的文件都可作为输入文件。选择 (1) 或 (2) 后可输入电子密度的等值面值，等值面值的选择在很大程度上是任意的，默认值 0.05 a.u. 能够显示体系的主要轮廓，而若要展示位阻效应，可以使用例如 0.001 或 0.002 a.u.，这对应于 Bader 对 vdW 的定义

![](../imgs/p454_073.png)

<!-- p.455 -->


表面 (surface)。

在本功能中，你可以分别用选项 2 (option 2) 和选项 3 (option 3) 定义绘图平面的 X 轴和 Y 轴范围，默认范围是自动确定的，以使该图能覆盖整个体系。X 和 Y 方向的格点数可分别通过选项 3 (option 3) 和选项 4 (option 4) 手动设置，计算开销与二者数量的乘积成正比。格点数越大，所得图形越精细。

Zstart 和 Zend 可分别由选项 7 (option 7) 和选项 8 (option 8) 定义。默认情况下，它们分别对应于 Z 值最正和最负的原子的 Z 坐标。Z 扫描的步数可通过选项 6 (option 6) 修改，该值越小，投影距离越精确，但计算开销越高。

默认情况下，在绘制的颜色填充图上会附加等值线 (contour lines)，在 Zend − Zstart 与 0 之间自动均匀生成 25 条等值线，它们分别对应于默认的颜色条 (color bar) 下限和上限。自动生成的等值线数量可通过选项 9 (option 9) 修改。

本功能从不限于分子体系，它也完全兼容周期性体系，因此你可以用本功能生动地揭示固体表面各种位点的相对 Z 位置。在这种情况下，输入文件应包含晶胞信息，何种结构文件和波函数文件能提供晶胞信息已分别在 2.9.3 节和 2.9.2 节中说明。

绘制这类图的一个例子见 4.300.8 节。所需信息：原子坐标 (Atom coordinates)

### 3.300.9 确定费米能级 (Determine Fermi level)

本功能用于基于指定温度和轨道能量，通过 Fermi-Dirac 分布确定费米能级。

原理 (Theory) 根据 Fermi-Dirac 分布，在给定温度 (T) 下，轨道 i 的占据数可按如下计算

$$n_{i}=\frac{\eta}{1+\exp[(E_{i}-E_{f})/(k_{B}T)]}$$

<!-- formula-ocr: formula_p455_335.png 已替换为LaTeX, 原图保留备查 -->

其中 Ei 为轨道 i 的能量，Ef 为费米能级 (Fermi-level)，kB 为 Boltzmann 常数，若轨道由限制性与非限制性计算产生，η 分别为 2.0 和 1.0。Ef 对应于占据概率为 50% 的假想能级。

用上述方式指定轨道占据数后，你会发现所有轨道的总电子数取决于 Ef 的选择。显然，物理上有意义的 Ef 是使总电子数与当前体系实际电子数相同的取值；因此，在 Multiwfn 的本功能中，正是基于这一事实确定 Ef（这与 CP2K 程序在启用 smearing 时确定 Ef 的方式相同）。

<!-- p.456 -->


具体而言，Multiwfn 使用二分算法 (bisection algorithm) 迭代调整 Ef，直到当前总电子数与预期总电子数之间的偏差小于 1E-6。最大迭代次数为 1000，通常在几十个循环内即可收敛。

Ef 与温度有关，因此在本功能中你需要输入一个温度。值得注意的是，在 T = 0 K 的情况下 Ef 是定义不良的 (ill defined)，因为此时 Fermi-Dirac 函数为阶跃函数，HOMO 与 LUMO 能量之间的任何值都可能是可接受的。

用法 (Usage) 要使用本功能，只需载入一个同时包含占据轨道和虚轨道的波函数文件（例如可用 .mwfn、.fch、.molden 等，不能使用 .wfn 格式，因为它通常不记录虚轨道），然后进入主功能 300 (main function 300) 的子功能 9 (subfunction 9)，再输入一个温度即可。

例如，启动 Multiwfn 并输入 examples\Li6.fch 300 //其它功能（第 3 部分）[Other function (Part 3)] 9 //确定费米能级 [Determine Fermi level] 3000 //温度 (K) [Temperature (K)] 你将看到

```text
 Iter:    1  Nelec:     18.00331025  Dev.:  0.33102D-02  Ef:   -0.09099563 a.u.
 Iter:    2  Nelec:     17.49559527  Dev.: -0.50440D+00  Ef:   -0.10918015 a.u.
 Iter:    3  Nelec:     17.81870305  Dev.: -0.18130D+00  Ef:   -0.10008789 a.u.
...ignored
 Iter:   17  Nelec:     17.99999281  Dev.: -0.71905D-05  Ef:   -0.09117931 a.u.
 Iter:   18  Nelec:     17.99999782  Dev.: -0.21801D-05  Ef:   -0.09117904 a.u.
 Iter:   19  Nelec:     18.00000033  Dev.:  0.32506D-06  Ef:   -0.09117890 a.u.
 Converged! Fermi level is   -0.09117890 Hartree     -2.481104 eV
```

即 Ef 为 -2.481 eV。

Multiwfn 采用 HOMO 与 LUMO 能量的平均值作为初始猜测。孤立体系通常具有相对较大的带隙，因此若指定的温度不够高，迭代将在 1 个循环内收敛。例如，若在上例中仅将温度设为 500 K，Ef 将为 -2.476 eV，这正是 HOMO 与 LUMO 的平均值。

使用纯文本文件作为输入文件 若你所用的量子化学或第一性原理程序无法产生 Multiwfn 支持的波函数文件，你仍可使用本功能。你只需将轨道信息手动写入纯文本并将其用作输入文件。对于闭壳层情形，格式应如下所示：

```text
5 20
 -19.138047
  -0.997376
  -0.514852
[...ignored]
   3.531811
   3.692553
```

第一行中，5 和 20 分别表示占据和虚 MO 的数目。其它部分

<!-- p.457 -->


以 Hartree 为单位、按自由格式 (free format) 按从低到高记录轨道能量。为方便起见，也允许将占据和虚轨道能量分别写在两行，例如：

```text
5 20
 -19.138047 -0.997376 -0.514852 -0.371177 -0.291987
   0.065333 0.151203 0.756610 [...ignored] 3.307120 3.531811 3.692553
```

对于开壳层情形，纯文本文件的格式应如下所示：

```text
6 13 4 15
-19.33565   //The first alpha orbital
 -1.18124
 -0.66585
[...ignored]
  2.13855
  2.46757
  3.40210   //The last alpha orbital
-19.30115   //The first beta orbital
 -1.09028
 -0.63075
[...ignored]
  2.49486
  3.45566   // The last beta orbital
```

第一行依次记录 alpha 占据、alpha 虚、beta 占据和 beta 虚轨道的数目，随后部分依次记录这四类轨道的能量。

## Multiwfn

> 序言、输入文件、轨道显示、点性质、拓扑实例、直线/平面作图、格点数据、波函数修改、布居电荷、轨道成分

> 英文原文见同目录 `06_教程4.0-4.8.md`｜图片目录：`../mw_imgs/`

---
