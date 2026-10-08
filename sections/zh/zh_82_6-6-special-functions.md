# 特殊功能(Special functions)

> Multiwfn manual, p.1158–1158.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.1158 -->




### 6.6 特殊功能(Special functions)

Multiwfn中有一些特殊功能，它们主要用于调试、特殊目的，其中一些是应一些Multiwfn用户的要求而设。这里提及其中几个。

### 6.6.1 在特定位置添加Bq原子(Add Bq atoms at specific positions)

有时我们想在3D图上突出特殊位置，例如，参考点、实空间函数的质心位置、用于绘制局域DOS的位置等。为了实现这一点，你可以进入主功能1000，选择子功能12，并手动输入要添加的Bq原子（鬼原子）的X、Y、Z坐标。你可以添加任意数量的Bq原子。一旦所有Bq原子都已添加，输入q返回。然后在显示3D分子结构的GUI中你将看到Bq原子，它们显示为青色球。值得注意的是，在主功能0中，你可以通过选择其他设置(Other settings)-设置原子标签类型(Set atomic label type)中的相应项来选择是否显示Bq原子的标签。

### 6.6.2 计算片段与轨道之间的核吸引能(Calculate nuclear attractive energy between a fragment and an orbital)

你可以通过进入主功能1000的子功能90（在主菜单中隐藏）使用该功能。该功能计算用户定义片段中所有原子核与一个轨道之间的吸引能，即：

$$E_{\mathrm{M O}i-\mathrm{f r a g}}=\left\langle\varphi_{i}\right|\sum_{A\in\mathrm{f r a g}}\frac{Z_{A}}{\left|\mathbf{r}-\mathbf{R}_{A}\right|}\left|\varphi_{i}\right\rangle\equiv\int\left|\varphi_{i}(\mathbf{r})\right|^{2}\sum_{A\in\mathrm{f r a g}}\frac{Z_{A}}{\left|\mathbf{r}-\mathbf{R}_{A}\right|}\mathrm{d}\mathbf{r}$$

在计算过程中，原子对结果的贡献依次输出，例如，下面输出


```text
Processing center     2(H )   /     3
Accumulated value:       -8.3269642826  Current center:       -0.0629848533
```

意味着

$$E_{\mathrm{M O}i-\mathrm{f r a g}}^{\mathrm{2H}}=\int w_{2\mathrm{H}}(\mathbf{r})\left|\varphi_{i}(\mathbf{r})\right|^{2}\sum_{A\in\mathrm{f r a g}}\frac{Z_{A}}{\left|\mathbf{r}-\mathbf{R}_{A}\right|}\mathrm{d}\mathbf{r}=-0.06298$$

其中w2H(r)是由Becke划分定义的2H原子的原子权重函数。

该积分用Becke多中心积分方法求值，因此`settings.ini`中的“radpot”和“sphpot”影响积分精度。通常默认值已足够精确。注意，如上式所示，计算中不考虑轨道的占据数。

所需信息(Information needed)：GTF，原子坐标

### 6.6.3 输出Becke积分点(Output Becke's integration points)

J. Chem. Phys., 88, 2547 (1988)提出的Becke多中心数值积分算法已被几乎所有流行的量子化学程序用于积分
