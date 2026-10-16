# **3.7 自定义操作、前分子与变形性质 (Custom operation, promolecular and deformation properties)（选项 0、-1、-2）**

## **3.7.1 多个波函数的自定义操作 (Custom operation for multiple wavefunctions)（0）**

在主功能 3、4 和 5 中，有一个子功能允许你为多个波函数设置自定义操作 (custom operation)。支持的运算符包括 +（加）、−（减）、\*（乘）、/（除），参与自定义操作的波函数数量没有上限。例如，如果启动 Multiwfn 后载入的第一个波函数是 *a.wfn*，然后在自定义操作的设置步骤中你输入了 *2*（*viz.* 有两个波函数将被放入“自定义操作列表”并依次与 *a.wfn* 进行运算），接着你输入了 *-,b.wfn* 和 *\*,c.wfn*，则你最终得到的性质将是 \[(property of *a.wfn*) - (property of *b.wfn*)\] \* (property of *c.wfn*)。如果你感到困惑，可以参考第 [4.5.4](sec-4-5-generate-grid-data-and-view-isosurface-map.md#454-用福井函数和对偶描述符研究苯酚亲电进攻的有利位点) 节和 [4.5.5](sec-4-5-generate-grid-data-and-view-isosurface-map.md#455-绘制电子密度差值图以研究咪唑配位镁卟啉的电子转移) 节中的例子。

有时第一个载入的文件中的分子结构与随后载入的文件中的不完全相同，你设置的格点将针对第一个载入的文件，所有其他文件将共用相同的格点设置。

避免将自定义操作与主功能 -4、-3 和 6 联用，否则你可能会得到荒谬的结果。

## **3.7.2 前分子与变形性质 (Promolecular and deformation properties)（-1、-2）**

如果在选择性质（*viz.* 实空间函数）之前，你在主功能 3、4 或 5 中选择了子功能 -1，那么你最终得到的就是前分子性质 (promolecular property)。前分子性质是处于自由状态 (free-state) 的各原子性质的叠加

$$
P^{\mathrm{pro}}(\mathbf{r})=\sum_A P_A^{\mathrm{free}}(\mathbf{r}-\mathbf{R}_A)
$$

如果所选的性质是电子密度，那么前分子性质通常被称为前分子密度 (promolecular density)

$$
\rho^{\mathrm{pro}}(\mathbf{r})=\sum_A \rho_A^{\mathrm{free}}(\mathbf{r}-\mathbf{R}_A)
$$

这是一种人为构造的密度，对应于分子已经形成但密度尚未弛豫时的状态。

变形性质 (deformation property) 是相同几何构型下分子的实际性质与前分子性质之差

$$
P^{\mathrm{def}}(\mathbf{r})=P^{\mathrm{mol}}(\mathbf{r})-P^{\mathrm{pro}}(\mathbf{r})
$$

如果所选的性质是电子密度，那么变形性质通常被称为变形密度 (deformation density)，也称为电子成键电荷分布 (electronic bonding charge distributions, BCD)，它对分析电荷转移和成键本质非常有用。变形密度的应用例子可参见我的论文 [*Acta Phys. -Chim. Sin.*](http://www.whxb.pku.edu.cn/EN/10.3866/PKU.WHXB201709252)[,](http://www.whxb.pku.edu.cn/EN/10.3866/PKU.WHXB201709252) [**34**](http://www.whxb.pku.edu.cn/EN/10.3866/PKU.WHXB201709252)[, 503 (2018)](http://www.whxb.pku.edu.cn/EN/10.3866/PKU.WHXB201709252) 和 *Angew. Chem. Int. Ed.*, **137**, e202504895 (2025) DOI: [10.1002/anie.202504895](https://doi.org/10.1002/anie.202504895)。

## **3.7.3 原子波函数的生成 (Generation of atomic wavefunctions)**

前分子与变形性质的计算以及 Multiwfn 中的某些功能需要原子波函数文件，例如计算 Hirshfeld、VDD 和 ADCH 电荷、模糊原子空间分析以及基于 Hirshfeld 划分的轨道成分分析等。生成原子 .wfn 文件的过程完全相同。

在选择子功能 -1 或 -2 以研究前分子与变形性质后，Multiwfn 会检查当前目录的“atomwfn”子目录中是否已存在本体系所涉及的所有元素的 .wfn 文件，如果没有，Multiwfn 会自动调用 Gaussian 生成缺失的元素 .wfn 文件，并对其密度做球化处理。如果 Gaussian 可执行文件的路径（*settings.ini* 中的“gaupath”参数）不正确或尚未定义，Multiwfn 会要求你输入 Gaussian 可执行文件的路径。生成元素波函数所用的基组可由用户任意设置，但建议使用与分子波函数相同的基组。

新生成的元素波函数文件或从“atomwfn”目录中取用的文件存放在当前目录的“wfntmp”子目录中。它们会被平移到本体系中原子的实际位置，同时 .wfn 文件名中会加上原子序号（*例如* "Cr 30.wfn"）。这些就是将直接用于计算前分子与变形性质的文件。

### **细节与技巧 (Details and skills)**

如果你想避免每次都重新生成元素波函数，可以把“wfntmp”目录中不带数字后缀的 .wfn 文件（如 *C .wfn*）移到“atomwfn”目录中（如果“atomwfn”目录不存在，请自行创建），下次如果 Multiwfn 检测到所需的元素 .wfn 文件已全部存在于“atomwfn”文件夹中，就会直接使用它们。Multiwfn 只会调用 Gaussian 计算缺失的元素 .wfn 文件。

“examples”目录下的“atomwfn”子目录中含有前四周期所有元素的波函数文件，它们是在 6-31G\* 下生成的，且已经过球化处理。如果想使用它们，只需把 "atomwfn" 目录复制到当前文件夹。

> **注记 (Note)**
>
> 有一种快速生成前四周期所有元素波函数文件的方法：“examples\genatmwfn.pdb”文件包含了前四周期的所有原子，将它载入 Multiwfn 并生成前分子性质，待元素波函数计算完成后，把“wfntmp”目录中不带后缀的 .wfn 文件复制到“atomwfn”目录即可。

如果你的体系包含比 Kr 重的元素，Multiwfn 无法通过调用 Gaussian 自动生成原子波函数文件并对其密度做球化处理；在这种情况下，你必须手动计算并球化原子波函数，然后把它们放入“atomwfn”目录，Multiwfn 会直接使用它们。

为前四周期的主族元素（序号 1 至 20 以及 31 至 36）生成波函数默认使用的理论方法是 ROHF，为第四周期的过渡金属使用的是 UB3LYP。一般而言，前分子与变形性质对理论方法不敏感。如果你想自行指定理论方法，可以用斜杠作为分隔符同时输入理论方法和基组，例如 *BLYP/6-311G\**。不要加“RO”或“U”前缀，因为它们会被自动添加。如果在生成原子波函数过程中出错，请仔细检查“wfntmp”目录中的 Gaussian 输入和输出文件。

注意，Gaussian 允许的 .wfn 文件路径的最大字符长度只有 60！如果长度超过该阈值，路径会被截断并导致错误。因此不要把 Multiwfn 放在路径太长的目录中！

## **3.7.4 原子波函数的球化 (Sphericalization of atom wavefunction)**

Multiwfn 支持前分子与变形性质的主要目的是生成前分子密度和变形密度，然而，大多数元素在自由基态下的电子密度并不具有球对称性，因而会导致取向依赖问题。为解决该问题，必须对原子电子密度做球化处理。然而，做球化的方式并不唯一。在 Multiwfn 中，通过人为修改原子波函数来球化原子电子密度，具体细节在此描述。如果你想跳过球化步骤，只需把 *settings.ini* 中的“ispheratm”设为 0。

对于 IV A 族元素，Multiwfn 默认用 $sp^{3}$ 组态代替 $s^{2}$ $p^{2}$ 基态。这种处理是合理的，因为在大多数分子中这些原子处于 $sp^{3}$ 杂化状态。对于 VI A、VII A 以及 Fe、Co、Ni，Multiwfn 将同一壳层内轨道的占据数平均化；例如，氧在基态有两个单占据的 2*p* 轨道和一个双占据的 2*p* 轨道，该壳层中的电子数为 4，因此 Multiwfn 把这三个轨道的占据数都设为 4/3。这种方法之所以可行，是因为占据轨道的形状几乎总是相同的，无论原来的占据数是一还是二。然而，虚轨道和占据轨道之间的差别很显著，因此 Multiwfn 对 III A 族元素以及 Sc、Ti 和 V 采用另一种方法球化电子密度。在该方法中，单占据轨道被复制并旋转。以硼为例，假设单占据的 2*p* 轨道沿 Z 轴方向，Multiwfn 把该轨道复制两次并分别转向 X 轴和 Y 轴，最后把这三个轨道的占据数都设为 1/3。（用户无需自行检查单占据轨道的取向）。如果希望 Multiwfn 对 IV A 族原子也用这种方式而不是用 $sp^{3}$ 组态做球化，把 *settings.ini* 中的“SpherIVgroup”设为 1 即可。

注意，Multiwfn 中使用的球化方法与波函数类型密切相关，如果对主族元素使用非限制性波函数，或对过渡金属使用限制性开壳波函数，这些方法会失效。如果对过渡金属使用 Hartree-Fock 方法，这些方法也会失效，因为 HF 给出的轨道顺序与大多数 DFT 情形不同（HF 的顺序是错的，4*s* 高于 3*d*）。
