# 生成格点数据并查看等值面图

> Multiwfn manual, p.541–557.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.541 -->



此外，在控制台窗口中，你可以找到极值的信息，包括在平面图中的X和Y坐标，以及极值处的ESP值


```text
 Contour line    1
 Minimum found at   -2.757166   -6.243420  Value:    0.0124521154
 Maximum found at   -6.422139   -4.124796  Value:    0.0208512768
 Minimum found at   -6.092997   -1.331264  Value:    0.0178074993
[...ignored]
 Maximum found at    0.000055   -8.122282  Value:    0.0174823731
 Total maxima:     5
 Total minima:     5
```

如果你按照4.4.4节中的步骤绘制填色的ESP图并同时显示vdW表面，你将很容易理解为什么ESP极值会出现在那些位置。此外，注意Multiwfn的主功能12能够确定三维分子表面上ESP或其它函数的极值，如4.12.1节所示。


## 4.5 生成格点数据并查看等值面图

本节包含Multiwfn主功能5的示例，所有示例都需要计算格点数据。一旦生成了格点数据，就可以将其可视化为等值面图，或导出


![](../imgs/p541_153.png)

<!-- p.542 -->



为.cub文件，以便用VMD等第三方工具渲染，或供其它分析程序进一步利用。

注意，使用我准备好的VMD脚本来渲染Multiwfn生成的cube文件非常容易，而图形质量非常好，关于如何实现请查看4.A.14节。


### 4.5.1 三氟化氯的电子定域函数

在本节中我们绘制三氟化氯的电子定域函数(electron localization function，ELF)的等值面图。启动Multiwfn并输入以下命令

examples\ClF3.wfn // 在B3LYP/6-31G*水平下生成(Generated at B3LYP/6-31G* level) 5 // 生成格点数据并查看等值面（Generate grid data and view isosurface） 9 // 电子定域函数（ELF）(Electron localization function (ELF)) 2 // 中等质量格点，将计算约512000个点，对于小体系此设置已足够精细，但对中等体系尤其是大体系则不够。关于格点设置的更多知识请查阅3.6节（Medium-quality grid）

现在Multiwfn开始计算格点数据。计算完成后，Multiwfn会输出一些统计信息。在新出现的菜单中有许多选项，你可以通过选择选项-1绘制等值面图，之后会弹出一个GUI窗口。在文本框中输入等值0.85并按回车键，你将看到如下等值面图

ELF等值面清晰地揭示了氟和氯原子的孤对电子区域。

如果你想把格点数据作为Gaussian cube文件导出到当前目录，应点击“Return”按钮关闭GUI窗口，然后选择选项2。

如果你用ChimeraX基于Multiwfn导出的ELF cube文件绘制等值面图，你将能够自由地为不同区域的各个域设置颜色。例如，下图是由ChimeraX绘制的乙酸ELF=0.83等值面，如果你仔细跟随此视频教程：“Plotting electron localization function (ELF) isosurface using Multiwfn and ChimeraX”(https://youtu.be/vC48iEB8PwI)，你就能很容易地重现此图。


![](../imgs/p542_154.png)

<!-- p.543 -->



有些论文绘制了按相应盆类型(单突触或双突触)着色的ELF等值面图，虽然你可以用上述方法实现，但有一个明显缺点：如果你改变等值，着色就会改变，而且，不可能用不同颜色为整个等值面的各个子区域着色以展示其对应于不同类型盆的各个子区域。4.17.10节所述方法完美地解决了这些问题，它需要使用盆分析模块。


### 4.5.2 1,3-丁二烯的电子密度拉普拉斯

电子密度拉普拉斯是另一个像ELF和LOL一样揭示电子结构的有用实空间函数。由于分辨能力较差，拉普拉斯在突出定域区域方面不如ELF和LOL。例如，比氪重的原子的壳层结构不能完全由拉普拉斯展示，如果你尝试用拉普拉斯分析三氟化氯，你会发现氟原子的孤对电子区域难以辨认。而且，拉普拉斯的取值范围太大，给可视化分析带来困难。然而，对于许多体系，电子密度的拉普拉斯仍然有用。在本例中我们将为1,3-丁二烯绘制该函数的等值面图。

启动Multiwfn并输入以下命令 examples\butadiene.fch // 在B3LYP/6-31G**水平下得到(Yielded at B3LYP/6-31G** level) 5 // 生成格点数据并查看等值面（Generate grid data and view isosurface） 3 // 电子密度拉普拉斯（Electron density Laplacian） 2 // 中等质量格点(如果你想获得更好的图形效果，请改选“高质量格点”)(Medium-quality grid)

-1 // 查看等值面（View isosurface） 在新出现的窗口中，把等值面值从默认值改为0.3，则绿色和蓝色等值面将分别对应于0.3和-0.3的等值。当前图形如下所示


![](../imgs/p543_155.png)

<!-- p.544 -->



C-C和C-H之间蓝色等值面的存在表明价壳层电子强烈集中在这些区域，这是共价键合的典型模式。如果你仔细检查碳原子之间的等值面，你会发现C6-C8或C1-C4之间的等值面比C4-C6之间的等值面更宽，这一现象反映了两条边界C-C共价键比中央那条更强。这一结论也可以用其它波函数分析方法验证，例如，Mayer键级(C6-C8之间的键级为1.863，而C4-C6之间的仅为1.136)。

我们在本节中得到的等值面图不太光滑，这是因为我们只用了中等质量格点。如果你改用高质量格点，将得到好得多的等值面。

### 4.5.3 计算ELF-σ和ELF-π以研究苯的芳香性

ELF-σ和ELF-π指数是常用的σ和π芳香性指数，它们定义为仅由σ轨道和π轨道贡献的ELF域的分叉点(即(3,-1)型临界点)处的ELF值，详见J. Chem. Phys., 120, 1670 (2004)和J. Chem. Theory Comput., 1, 83 (2005)。这两篇论文包含了运用

ELF-π分析π离域的非常好的例子：Theor. Chem. Acc., 139, 25 (2020)和Carbon, 165, 468 (2020)。

这些指数的理论基础是，分叉点处的ELF值衡量了相邻ELF域之间的相互作用，值越大意味着这些域之间的电子离域性越好。强的多中心离域通常被认为是芳香性的本质。据认为，如果ELF-π大于0.70，则分子具有π

芳香性。而如果ELF-π和ELF-σ的平均值大于0.70，则可说该分子是全局芳香的。在本例中，我们将计算苯的ELF-σ和ELF-π。

为了分离σ和π轨道，我们首先需要知道哪些轨道是π轨道。启动Multiwfn并输入以下命令

examples\benzene.wfn // 在B3LYP/6-311G*水平下优化(Optimized at B3LYP/6-311G* level) 0 // 查看分子轨道(View molecular orbitals (MOs)) 现在依次检查每个MO的轨道形状，我们发现第17、20和21个MO是π轨道，

如下所示。所有其它MO都被认定为σ轨道。


![](../imgs/p544_156.png)

![](../imgs/p544_157.png)

<!-- p.545 -->



我们先计算ELF-π。应略去σ轨道对ELF的贡献；这可以通过把所有σ轨道的占据数设为零来实现。

6 // 进入“修改并检查波函数”界面(Enter "Modify & Check wavefunction" interface) 26 // 为某些轨道设置占据数（Set occupation number for some orbitals） 0 // 选择所有轨道（Selecting all orbitals） 0 // 把所有轨道的占据数设为零（Set occupation number of all orbitals to zero） 17,20,21 // 选择MO 17、20和21，即所有π轨道(Select MO 17, 20 and 21) 2 // 把MO 17、20和21的占据数设为2.0(双占据)。如果你想检查占据数是否已正确设置，选择选项3。你会发现所有σ轨道的占据数(Set occupation numbers of MO 17, 20 and 21 to 2.0)

已变为零，即它们在后续计算的所有结果中将没有贡献（All other orbitals...）

q // 返回上一级菜单（Return to last menu） -1 // 返回主菜单（Return to main menu） 对于此体系，事实上还有一种更方便的方法把除π轨道之外的所有轨道的占据数设为零。步骤是：进入主功能100的子功能22，选择0，则所有π轨道将被自动识别，然后选择1把所有其它轨道的占据数设为零(若体系中涉及硅等较重元素则选择选项3)。最后，选择0返回主菜单。关于π轨道自动识别的更多细节见3.100.22节。

研究ELF-π 研究ELF-π有两种方式，方式1是直接检查ELF等值面，而方式2是进行拓扑分析。方式1更直观，但不如方式2准确。这里我先说明方式1。像往常一样用主功能5生成并查看ELF的等值面(回顾4.5.1节。推荐使用高质量格点)。这次ELF等值面只反映π电子定域特征。通过逐渐增大等值，你会发现两个圆环形ELF域在约0.91的等值处分叉为十二个类球形域(见下图)，意味着苯的ELF-π指数约为0.91。


![](../imgs/p545_158.png)

![](../imgs/p545_159.png)

<!-- p.546 -->



接下来，让我们用方式2重新评估ELF-π指数，这种方式比方式1更严格。选择0返回主菜单。

2 // 拓扑分析（Topology analysis） -11 // 选择实空间函数（Select real space function） 9 // ELF 6 // 起始点将依次分布在每个原子周围。这种搜索模式最适合定位ELF临界点（The starting points will be distributed around each atom in turn）

-1 // 开始临界点搜索（Start the CP search） -9 // 返回上一级菜单（Return to upper menu） 0 // 可视化结果（Visualize results）。结果图如下所示，两个(3,+1)临界点未显示

通过将此图与ELF等值面图比较，可以清楚看到(3,-1)临界点(橙色)是ELF域的分叉位置，而(3,-3)临界点(紫色)对应于十二个ELF域的极大值点。现在我们查看一个(3,-1)临界点处的ELF值，任选其一即可，因为它们都是等价的。

7 // 显示一个临界点处的所有性质（Show all properties at a CP） 23 // 临界点23(CP23) 从输出中，我们发现临界点23处的ELF值，即苯的ELF-π指数为0.91247，这一结果与Chem. Phys. Lett., 443, 439 (2007)中给出的0.913值非常吻合，注意我们的计算水平与该论文完全相同。显然，该值超过了π芳香性的标准(0.70)，表明苯具有强的π芳香性。

研究ELF-σ 现在我们计算苯的ELF-σ。重新启动Multiwfn并载入benzene.wfn，把MO 17、20和21的占据数设为零(用主功能100中的子功能22来做更方便)。然后像往常一样生成ELF的等值面，逐渐调节等值，试图找出

碳原子之间的σ键对应的域在哪个等值处分叉。最终可以发现，在等值等于0.71时该域分叉，表明ELF-

σ指数约为0.71。分叉点如下图中红箭头所示：


![](../imgs/p546_160.png)

<!-- p.547 -->



进入拓扑分析模块并搜索ELF临界点，就像我们在ELF-π分析的方式2中所做的那样。你将得到下图。为清楚起见，(3,+1)和(3,+3)临界点已被隐藏。

将临界点的位置与ELF等值面图比较，可以清楚看到诸如临界点

48和58的(3,-1)临界点对应于碳原子之间σ键域的分叉点。查看临界点48处的ELF值，得到0.70907，这就是精确的ELF-σ值。我们的结果与Chem. Phys. Lett., 443, 439 (2007)中的0.717值吻合良好。

ELF-σ和ELF-π的平均值为(0.70907+0.91247)/2=0.81077，大于全局芳香性的标准，因此苯具有全局芳香性特征。


### 4.5.4 用Fukui函数和对偶描述符研究苯酚


### 亲电进攻的有利位点

Multiwfn支持一批预测最活泼位点的方法，详见4.A.4节。在本节中，我将介绍如何实现Fukui函数和对偶描述符，这是最流行的两种揭示活泼位点的方法。

重要提示：在日常研究中，我强烈建议你直接用主功能22


![](../imgs/p547_161.png)

![](../imgs/p547_162.png)

<!-- p.548 -->



来自动计算Fukui函数和对偶描述符，因为步骤比下述步骤简单得多，同时还能得到概念密度泛函理论中的许多有用物理量作为副产品，介绍见3.25节，例子见4.22.1节。

### 4.5.4.1 Fukui函数

理论 Fukui函数是概念密度泛函理论中非常重要的概念，已被广泛用于预测活泼位点。Fukui函数定义如下，原始论文见J. Am. Chem. Soc., 106, 4049 (1984)，相关讨论和比较见我的论文Acta Phys. -Chim. Sin., 30, 628 (2014)。


$$f(\mathbf{r})=\left[\frac{\partial\rho(\mathbf{r})}{\partial N}\right]_{\nu}$$

<!-- formula-ocr: formula_p548_337.png 已替换为LaTeX, 原图保留备查 -->

其中N为当前体系中的电子数，偏导数中的常数项ν为外势。一般来说，外势只来自于核电荷，因此对于孤立化学体系ν可简单视为核坐标。据认为，活泼位点应比其它区域具有更大的Fukui函数值。由于N为整数时的不连续性，我们无法直接求该偏导数。通过有限差分近似，Fukui函数可针对三种情形明确地计算：

$$\mathrm{Nucleophilic~attack:}\;f^{+}(\mathbf{r})=\rho_{N+1}(\mathbf{r})-\rho_{N}(\mathbf{r})\approx\rho^{\mathrm{LUMO}}(\mathbf{r})$$

$$\mathrm{Nucleophilic~attack:}\;f^{+}(\mathbf{r})=\rho_{N+1}(\mathbf{r})-\rho_{N}(\mathbf{r})\approx\rho^{\mathrm{LUMO}}(\mathbf{r})$$

$$Radical~attack:f^{0}(\mathbf{r})=\frac{f^{+}(\mathbf{r})+f^{-}(\mathbf{r})}{2}=\frac{\rho_{N+1}(\mathbf{r})-\rho_{N-1}(\mathbf{r})}{2}\approx\frac{\rho^{\mathrm{HOMO}}(\mathbf{r})+\rho^{\mathrm{LUMO}}(\mathbf{r})}{2}$$

准备波函数文件 下面我们首先用上述所示的Fukui

函数f −揭示苯酚亲电进攻的活泼位点。这里不使用基于前线轨道的Fukui函数近似形式。

我们需要准备计算f −所需的文件。假设你是Gaussian用户，你可以用.wfn、.wfx或.fch作为当前目的的输入文件。在本例中，我们进行以下计算以生成所需的.wfn文件，所有计算都在B3LYP/6-31G*水平下进行，这是产生有意义结果的最低可接受水平(当然你可以用更好的水平来改进结果)：

(1) 优化中性状态苯酚的几何结构。所得几何将用于后续步骤

(2) 对中性状态苯酚做单点任务以产生phenol.wfn(见examples\phenol.gjf)

(3) 对N-1状态(即阳离子状态)苯酚做单点任务以产生phenol_N-1.wfn(见examples\phenol_N-1.gjf)

注意，在做N-1状态的单点任务之前不应优化N-1状态的几何，因为在Fukui函数的偏导数中ν(在此即核坐标)是常数。顺便说一下，事实上如果你在步骤(1)中直接指定out=wfn关键词和.wfn文件的输出路径，则可省略步骤(2)。

<!-- p.549 -->



计算Fukui函数f − 为了研究f −的等值面，我们需要恰当使用Multiwfn的“自定义操作”功能(详见3.7.1节)。启动Multiwfn并输入以下命令：

examples\phenol.wfn // 中性状态的苯酚（Phenol of neutral state） 5 // 计算格点数据（Calculate grid data） 0 // 设置自定义操作（Set custom operation） 1 // 只有一个文件将与已载入的文件(即phenol.wfn)进行操作（Only one file will be operated with the file that has been loaded） -,examples\phenol_N-1.wfn // “-”为减号。首先载入的文件(即phenol.wfn)的性质将减去phenol_N-1.wfn的相应性质（Property of the firstly loaded file will be subtracted by corresponding property）

1 // 电子密度（Electron density） 2 // 中等质量格点（Medium-quality grid） 现在Multiwfn开始计算phenol.wfn的电子密度格点数据，然后计算phenol_N-1.wfn的格点数据，最后求其差值以产生f −的格点数据。我们选择选项-1查看等值面，把等值调到合适的值(0.007)后，图形将为

在图中，绿色和蓝色等值面分别对应f −的正值和负值区域。显然，f −函数最正的部分定域在O12、C1、C3、C4和C5上，这意味着羟基的对位和邻位是亲电进攻的有利活泼位点，这一结论与常识一致，即羟基是邻对位定位基。

计算Fukui函数f 0 接下来，我以丙烯为例说明如何绘制自由基进攻的Fukui函数，

即f 0 = (ρN+1 − ρN-1)/2。当然，我们应产生对应于N+1状态和N-1状态的波函数文件。我们先优化中性状态的几何(examples\propylene\opt_N.gjf)，然后用此几何对N-1和N+1状态做单点任务以产生相应的.fch文件。

启动Multiwfn并输入： examples\propylene\N+1.fch // N+1电子状态，即-1带电状态（N+1 electrons state） 5 // 计算格点数据（Calculate grid data） 0 // 设置自定义操作（Set custom operation） 1 // 有一个文件将与propylene-1.fch进行操作（One file will be operated with propylene-1.fch） -,examples\propylene\N-1.fch // N-1电子状态，即+1带电状态（N-1 electrons state） 1 // 电子密度（Electron density）


![](../imgs/p549_163.png)

<!-- p.550 -->



2 // 中等质量格点（Medium-quality grid） 6 // 把所有格点数据除以一个因子（Divide all grid data by a factor） 2 // 除以2(Divided by 2) -1 // 可视化等值面图（Visualize isosurface map） f 0 = 0.01的等值面图如下所示

### 4.5.4.2 对偶描述符

理论 对偶描述符是另一个用于揭示活泼位点的有用函数，详见J. Phys. Chem. A,

109, 205 (2005)。形式上，对偶描述符Δf与Fukui函数有密切关系：

$$\\Delta f(\\mathbf{r})=f^{+}(\\mathbf{r})-f^{-}(\\mathbf{r})$$

$$=[\rho_{N+1}(\mathbf{r})-\rho_{N}(\mathbf{r})]-[\rho_{N}(\mathbf{r})-\rho_{N-1}(\mathbf{r})]=\rho_{N+1}(\mathbf{r})-2\rho_{N}(\mathbf{r})+\rho_{N-1}(\mathbf{r})$$

值得注意的是，对偶描述符也可以用自旋密度𝜌𝑠来求值。由于𝜌𝑁+1 −𝜌𝑁和𝜌𝑁−𝜌𝑁−1可分别近似为𝜌𝑁+1 𝑠，因此显然有∆𝑓(𝐫) ≈𝜌𝑁+1 𝑠(𝐫)。通常，基于三种状态(N+1、N、N-1)的电子密度求得的对偶描述符与基于两种状态(N+1、N-1)的自旋密度求得的对偶描述符之间没有明显的定性差别。𝑠(𝐫) −𝜌𝑁−1 𝑠和𝜌𝑁−1

与Fukui函数不同，通过Δf可同时揭示两种类型的活泼位点。据认为，若Δf > 0，则该位点有利于亲核进攻，而若Δf < 0，则该位点有利于亲电进攻。然而，根据我的经验，如果你的目的是在许多潜在位点中找出哪些更有利，你无需关心

Δf的符号，只需研究哪些位点的Δf更正或更负。如果位点A周围Δf的分布比另一位点B更正，则可说A是比B更有利的亲核进攻位点，同时B是比A更优先的亲电进攻位点。

基于自旋密度近似求值对偶描述符 这里我们基于N-1和N+1状态的自旋密度计算苯酚的对偶描述符。由于我们早已算得phenol_N-1.wfn，现在只需计算phenol_N+1.wfn(此文件及相应的输入文件phenol_N+1.gjf已在“example”文件夹中提供)。之后，启动Multiwfn并输入：

examples\phenol_N+1.wfn // N+1电子体系，即阴离子状态（N+1 electron system） 5 // 计算格点数据（Calculate grid data） 0 // 设置自定义操作（Set custom operation） 1 // 只有一个文件将与已载入的文件进行操作（Only one file will be operated with the file that has been loaded） -,examples\phenol_N-1.wfn // N-1电子体系，即阳离子状态（N-1 electron system）


![](../imgs/p550_164.png)

<!-- p.551 -->



5 // 电子自旋密度（Electron spin density） 2 // 中等质量格点（Medium-quality grid） -1 // 可视化对偶描述符的等值面（Visualize isosurface of dual descriptor） 我们逐渐改变等值，以便能清晰区分不同位点处的对偶描述符，我们发现0.02是合适的值，相应的等值面如下所示

可以看到，在环上(除不能参与反应的C4外)，对位

碳具有明显的Δf负值，同时两个邻位碳处的Δf不如两个间位碳那么正，因此Δf的结论与Fukui函数f −完全一致，即只有对位和邻位碳被羟基活化而利于亲电进攻。

基于电子密度精确求值对偶描述符

如果你想以其精确形式(基于三种状态的ρ)求值Δf，可按以下步骤：

examples\phenol_N+1.wfn // N+1电子体系（N+1 electron system） 5 // 计算格点数据（Calculate grid data） 0 // 设置自定义操作（Set custom operation） 3 // 有三个文件将与已载入的文件进行操作（Three files will be operated with the file that has been loaded） -,examples\phenol.wfn // N电子体系（N electron system） -,examples\phenol.wfn // N电子体系（N electron system） +,examples\phenol_N-1.wfn // N-1电子体系（N-1 electron system） 1 // 电子密度（Electron density） 2 // 中等质量格点（Medium-quality grid） -1 // 可视化对偶描述符的等值面（Visualize isosurface of dual descriptor） 对应于等值0.01的图如下所示


![](../imgs/p551_165.png)

<!-- p.552 -->



可见，虽然此图与基于自旋密度求得的Δf图定性一致，但邻位碳与间位碳之间的差别不那么显著，表明

这次Δf区分优先位点的能力不好。因此，用精确形式求值Δf不一定比用自旋密度近似求值Δf得到更好的结果！

关于“凝聚”Fukui函数和对偶描述符 上面我们用可视化方式考察了Fukui函数和对偶描述符并得到了预期的结论。然而，可视化分析有些含糊和主观。因此，有时我们希望Fukui函数和对偶描述符的讨论能够定量化，即为每个原子指定一个值以展示其作为活泼位点的程度。为此，应基于布居分析技术计算“凝聚”版Fukui函数和对偶描述符。由于布居分析在4.7节举例说明，凝聚Fukui函数和凝聚对偶描述符的计算方法将推迟到4.7.3节介绍。另一种研究Fukui函数和对偶描述符的方案是先把整个分子表面划分成对应于每个原子的局域表面，然后考察这些局域表面上的平均值。因为此方案依赖于定量分子表面分析技术，说明推迟到4.12.4节。


### 4.5.5 绘制电子密度差值图以研究咪唑配位卟啉镁的电子转移


###

在本例中，我将向你展示如何在Multiwfn中绘制片段电子密度差值。在咪唑与卟啉镁配位过程中，发生电子转移和极化，电子密度的变化可通过从整个体系(下称MN-NN)中减去孤立状态下咪唑(下称NN)和卟啉镁(下称MN)的电子密度而清晰揭示。MN-NN的几何如下所示：


![](../imgs/p552_166.png)

<!-- p.553 -->



examples\MN-NN.gjf是MN-NN体系的Gaussian输入文件(几何已优化)，修改最后一行的.wfn输出路径后用Gaussian运行，则将产生MN-NN.wfn。接下来，分别从MN-NN.gjf中删除MN和NN部分并恰当修改.wfn输出路径，然后保存为MN.gjf和NN.gjf(它们已在“example”文件夹中提供)。然后用Gaussian运行它们以获得MN.wfn和NN.wfn。应注意，默认情况下，Gaussian总是把体系放到标准取向，这使得MN.wfn和NN.wfn中的坐标与MN-NN.wfn不一致，从而密度差值将毫无意义。因此，必须在route部分指定nosymm关键词以避免坐标的自动调整。(MN.wfn、NN.wfn和MN-NN.wfn也可直接从这里载入：http://sobereva.com/multiwfn/extrafiles/MN-NN.zip)

现在我们用Multiwfn生成电子密度差值的格点数据。启动Multiwfn并输入以下命令

MN-NN.wfn 5 // 计算格点数据（Calculate grid data） 0 // 设置自定义操作（Set custom operation） 2 // 有两个文件将与MN-NN.wfn进行操作（Two files will be operated with MN-NN.wfn） -,MN.wfn // 将从MN-NN.wfn的性质中减去MN.wfn的性质（Will subtract property of MN.wfn from that of MN-NN.wfn） -,NN.wfn // 将从MN-NN.wfn的性质中减去NN.wfn的性质（Will subtract property of NN.wfn from that of MN-NN.wfn） 1 // 性质选为电子密度（The property is selected as electron density） 3 // 由于当前体系相对较大，我们需要比通常情形更多的格点，因此选择高质量格点(Since present system is relatively huge, we need more grid points than normal cases, so we choose high-quality grid)

计算完成后，你可选择选项-1，然后把等值设为约0.001以可视化格点数据的等值面，如下所示。


![](../imgs/p553_167.png)

<!-- p.554 -->


在VMD中绘制等值面图 Multiwfn在可视化格点数据方面不是很专业，对于尺寸较大的格点数据，可视化速度相对较慢。你可以选择选项2将格点数据导出为cube文件，然后用外部工具（如VMD）进行可视化。下面是由VMD（可在http://www.ks.uiuc.edu/Research/vmd/免费获得）基于Multiwfn生成的cube文件所作的图形。

红色和蓝色等值面（分别为+0.0012和-0.0012 a.u.）分别代表NN配位到MN之后电子密度增加和减少的区域。可以明显看出，电子密度从NN中氮背侧向镁原子转移，从而加强了配位键。此外可以看出，NN的出现并未显著扰动卟啉环的电子密度分布，只对MN中的四个配位氮产生了轻微极化。

在VMD中绘制上图的详细步骤：首先，将cube文件density.cub拖入VMD主窗口。选择“图形（Graphics）”-“表示（Representations）”，点击“创建表示（Create Rep）”按钮创建一个新的表示，将“绘制方法（Drawing method）”改为“等值面（Isosurface）”，将“绘制（Draw）”设为“实心表面（Solid Surface）”，将“显示（Show）”设为“等值面（Isosurface）”，将等值面值改为0.0012，将“着色方法（Coloring method）”设为“颜色编号（ColorID）”并选择红色。现在密度差正值部分的等值面已经显示出来。然后再次点击“创建表示（Create Rep）”按钮创建另一个表示，在“颜色编号（ColorID）”中选择蓝色

![](../imgs/p554_168.png)

![](../imgs/p554_169.png)

<!-- p.555 -->


并将等值面值改为-0.0012。如果你想使用白色背景而不是默认的黑色背景，请选择 图形（Graphics）-颜色（Colors）-显示（Display）-背景（Background）-8 白色（White）。

事实上，使用我提供的VMD作图脚本和批处理文件，只需少得多的步骤就能获得比上图好得多的效果。请务必查看第4.A.14节，其中说明了如何实现这一点。

绘制等高线图 接下来，我们在由原子16、14、9定义的平面内绘制电子密度差的等高线图。输入以下命令：

0 // 返回主菜单 4 // 绘制平面图 0 2 -,MN.wfn -,NN.wfn 1 2 // 等高线图 [按 ENTER 键使用默认格点设置] 4 // 由三个原子定义平面 16,14,9 等高线图会立即弹出。实线和虚线等高线分别表示电子密度增加和减少的位置。图中的等高线有点稀疏，因此我们调整等高线设置，使图形看起来更密，从而包含更多信息。关闭图形，然后输入

3 // 更改等高线设置 9 // 用几何级数生成等高线值 0.0001,2,30 // 分别为起始值、步长和步数 y // 清除已有等高线 9 -0.0001,2,30 // 设置负值等高线 n // 将新生成的等高线追加到已有等高线中 1 // 保存设置并返回 -1 // 重新绘制图形 下面是最终的图形，看起来很漂亮！

<!-- p.556 -->


提示：在完成等高线定义后，你可以选择选项6将设置保存到外部纯文本文件。下次可直接用选项7载入该设置。

注意，在Multiwfn中，电子密度或其它实空间函数的差值图的绘制可以很容易地推广到两个以上片段的情形，例子见第4.4.8节。

### 4.5.6 研究阴离子水二聚体的电子离域范围函数EDR(r;d)

本节由Arshad Mehmood撰写，经Tian Lu略作修改。

本例展示如何在用户自定义的长度尺度d下计算阴离子水团簇（H2O）2−的电子离域范围函数EDR(r;d)（参见Phys. Chem. Chem. Phys., 17, 18305 (2015)）。利用EDR(r;d)，我们可以生动地考察溶剂化电子的分布。

启动Multiwfn并输入以下命令： examples\solvatedelectron.wfn // 在B3LYP/6-311++G(2d,2p)水平下优化的阴离子水二聚体

5 // 计算格点数据 20 // EDR(r;d) 11.22 // 输入长度尺度d（Bohr）。这里我们考虑在d=11.22 Bohr时相对离域的溶剂化电子。更多细节见J. Chem. Phys., 141, 144104 (2014)。

2 // 中等质量格点 -1 // 显示等值面图

![](../imgs/p556_170.png)

<!-- p.557 -->


此时会弹出一个GUI窗口。在“等值面值（Isosurface value）”框中输入等值面值0.74并按ENTER键。将出现如下等值面。

该图表明，在d=11.22 Bohr的长度尺度下，溶剂化电子位于两个H2O分子之间。

### 4.5.7 研究硫代甲酸的轨道重叠距离函数D(r)

本节由Arshad Mehmood撰写，经Tian Lu略作修改。

本例将展示硫代甲酸的轨道重叠距离函数D(r)的计算过程，并将其映射到分子电子密度表面上。如果你对D(r)不熟悉，可以查看第2.6节条目21或J. Chem. Theory Comput., 12, 3185 (2016)。

启动Multiwfn并输入以下命令： examples\ThioformicAcid.wfn // 在B3LYP/6-311++G(2d,2p)下优化的硫代甲酸 5 // 计算格点数据 21 // 轨道重叠长度函数D(r)，即对d最大化EDR(r;d) 现在我们需要设置EDR指数αi=1/di2的输入总数、起始值和增量，因为重叠距离是用均匀递变指数网格拟合的。起始值为最大指数（α1），后续指数由αi+1/αi = 1/αinc产生，其中αinc为增量。默认设置（即n=20，α1=2.50，αinc=1.50）对常见体系已足够。在选择手动输入（选项1）或默认设置（选项2）后，将出现一个指数列表，将用于D(r)的求值

2 // 中等质量格点 此时Multiwfn开始计算。等待计算完成后，选择选项2将D(r)的格点数据导出为当前文件夹下的EDRDmax.cub。下一步是生成分子密度等值面。

0 // 返回主菜单 5 // 计算格点数据 1 // 电子密度 2 // 中等质量格点（格点设置必须与D(r)计算时相同） 然后通过选择选项2将电子密度的格点数据导出为当前文件夹下的density.cub。

基于EDRDmax.cub和density.cub，就可以用许多可视化程序（如VMD和GaussView）将D(r)格点数据映射到分子密度等值面上。下面

是由GaussView绘制的D(r)映射的电子密度等值面（ρ = 0.001 a.u.）（如果你不知道如何基于两个cube文件通过GaussView和VMD将一个实空间函数以多种颜色映射到另一个实空间函数的等值面上，可以参阅我的博客文章“基于Multiwfn生成的cube文件绘制染色等值面图的方法”（http://sobereva.com/402，中文）。

![](../imgs/p557_171.png)
