# **6.6 特殊功能**

Multiwfn 中有一些特殊功能（special functions），它们主要用于调试、特殊目的，其中一些是应部分 Multiwfn 用户的要求而加入的。这里介绍其中的几个。

## **6.6.1 在指定位置添加 Bq 原子**

有时我们想在三维图上标出特殊位置，例如，参考点、实空间函数的质心位置、用于绘制局域态密度（local DOS）的位置等。为此，你可以进入主功能 1000，选择子功能 12，手动输入要添加的 Bq 原子（ghost atoms，幽灵原子）的 X、Y、Z 坐标。可以添加任意数目的 Bq 原子。添加完所有 Bq 原子后，输入 *q* 返回。然后在显示三维分子结构的图形界面中会看到 Bq 原子，它们以青色小球显示。值得注意的是，在主功能 0 中，可通过 "Other settings" - "Set atomic label type" 中的相应选项选择是否显示 Bq 原子的标签。

## **6.6.2 计算一个碎片与一条轨道之间的核吸引能**

可通过进入主功能 1000 的子功能 90（在主菜单中隐藏）使用该功能。该功能计算用户定义碎片中的全部原子核与一条轨道之间的吸引能，即：

$$
E_{\mathrm{MO}i\text{-frag}}=\langle\varphi_{i}|\sum_{A\in \mathrm{frag}}\frac{Z_{A}}{|\mathbf{r}-\mathbf{R}_{A}|}|\varphi_{i}\rangle\equiv\int|\varphi_{i}(\mathbf{r})|^{2}\sum_{A\in \mathrm{frag}}\frac{Z_{A}}{|\mathbf{r}-\mathbf{R}_{A}|}\mathrm{d}\mathbf{r}
$$

计算过程中，各原子对结果的贡献会依次输出，例如，下面的输出

```text
Processing center     2(H )   /     3
Accumulated value:       -8.3269642826  Current center:       -0.0629848533
```

表示

$$
E_{\mathrm{MO}i\text{-frag}}^{2\mathrm{H}}=\int w_{2\mathrm{H}}(\mathbf{r})|\varphi_{i}(\mathbf{r})|^{2}\sum_{A\in \mathrm{frag}}\frac{Z_{A}}{|\mathbf{r}-\mathbf{R}_{A}|}\mathrm{d}\mathbf{r}=-0.06298
$$

其中 $w_{\mathrm{2H}}(\mathbf{r})$ 是由 Becke 划分（Becke's partition）定义的 2H 原子的原子权重函数（atomic weighting function）。

该积分采用 Becke 多中心积分方法计算，因此 *settings.ini* 中的 "radpot" 和 "sphpot" 会影响积分精度。通常默认值已足够精确。注意，如上式所示，计算中不考虑轨道的占据数。

> **所需信息（Information needed）**
>
> GTFs, atom coordinates

## **6.6.3 输出 Becke 积分点**

提出于 *J. Chem. Phys.*, **88**, 2547 (1988) 的 Becke 多中心数值积分算法已被几乎所有流行的量子化学程序用于积分交换相关泛函，Multiwfn 的许多波函数分析功能也采用该算法，例如，计算 Hirshfeld 电荷和 ADCH 电荷、模糊原子空间分析（主功能 15）等。

通过主功能 1000 的子功能 93（一个隐藏功能），可将 Becke 算法的积分点导出到当前目录下的 *intpt.txt*。导出后各列的含义会在屏幕上明确显示。积分点的数目由 *settings.ini* 中的 "radpot" 和 "sphpot" 决定。角向格点的位置和权重由 Lebedev 方法决定，径向格点的位置和权重由第二类 Gauss-Chebyshev 方法决定。

进入该功能后，Multiwfn 会询问是否同时输出 Becke 积分权重。若输入 *y*，则权重会一并计算并输出。

> **所需信息（Information needed）**
>
> Atom coordinates

## **6.6.4 使轨道等同于基函数**

该功能是主功能 1000 的子功能 15。通过该功能，可使轨道等同于基函数（basis functions），轨道序号将与基函数序号对应。使用该功能后，可用主功能 0 观察基函数的等值面图以了解其空间分布，也可用主功能 3 和 4 分别绘制基函数的曲线图和平面图。

> **所需信息（Information needed）**
>
> Basis functions

## **6.6.5 生成前分子波函数**

如果你想生成前分子波函数（promolecular wavefunction），以便研究各种前分子性质，可使用 Multiwfn 为此专门提供的特殊功能：首先在启动时载入当前体系的实际波函数文件，然后进入主功能 1000 的子功能 17。Multiwfn 将为当前体系中的所有原子准备 .wfn 文件，情形与第 [3.7.3](sec-3-7-custom-operation-promolecular-and-deformation-properties.md#373-原子波函数的生成-generation-of-atomic-wavefunctions) 节所述完全相同。注意，用于原子波函数文件的基组必须与当前体系实际波函数所用的基组完全一致。成功生成前分子波函数后，若选择 *y*，内存中的波函数信息将对应于前分子波函数。也就是说，例如，若按主功能 5 中的常规步骤计算 ELF 格点数据，最终将得到对应于前分子状态的 ELF 格点数据。
