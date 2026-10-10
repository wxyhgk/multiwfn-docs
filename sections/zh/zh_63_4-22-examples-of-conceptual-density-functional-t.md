# 概念密度泛函理论

> Multiwfn manual, p.931–948.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.931 -->



在本节末尾强调，在做原子色散能贡献或色散密度的差值分析时，为两个体系选择的感兴趣原子范围内的原子数必须相同，且原子的顺序也必须相同，否则显然在对两个体系取差值时原子贡献的色散能会混淆。


## 4.22 概念密度泛函理论

## (CDFT) 分析示例


### 4.22.1 自动计算苯酚的概念密度泛函理论

### 量

注：本节的中文版是我的博文“使用 Multiwfn 轻松计算概念密度泛函理论中定义的各种量”（http://sobereva.com/484）。

本节我将展示如何非常方便地计算概念密度泛函理论（CDFT）框架下定义的几乎所有量。以苯酚为例。由于苯酚是中性分子，N、N+1 和 N-1 电子态分别对应于中性、阴离子和阳离子态。

在跟随本例之前，请先阅读第 3.25 节，其中介绍了将要计算的所有量和基本用法。

所需波函数文件的准备 应首先优化中性态的苯酚，请自行完成。examples\phenol.xyz 是在广泛使用的 B3LYP/6-31G* 水平下优化的苯酚几何结构，其质量对当前研究已足够好。

启动 Multiwfn 并输入以下命令： examples\phenol.xyz 22 // 计算概念密度泛函理论中的各种量(Calculate various quantities in conceptual density functional theory)


![](../imgs/p931_464.png)

<!-- p.932 -->



1 // 生成 N、N+1 和 N-1 电子态的 .wfn 文件(Generate .wfn files for N, N+1 and N-1 electrons states) [直接按 ENTER 键] //生成的 .gjf 文件将对应于 B3LYP/6-31G* 水平的单点任务

[直接按 ENTER 键] //使用默认电荷和自旋多重度，即 N 态为 0 1，N+1 态为 -1 2，N-1 态为 1 2

现在当前文件夹中已生成 N.gjf、N+1.gjf 和 N-1.gjf，它们是分别用于生成 N.wfn、N+1.wfn 和 N-1.wfn 的单点任务输入文件。现在你可以手动用 Gaussian 运行它们。如果不改变这些文件中 .wfn 文件的生成路径，运行后对于 Linux 版 Gaussian 它们将生成在当前文件夹中，而对于 Windows 版则将生成在 Gaussian 临时(scratch)文件夹中。

你也可以让 Multiwfn 直接调用 Gaussian 来运行 .gjf 文件。假设我们已将 `settings.ini` 中的 "gaupath" 参数设为 Gaussian 可执行文件的实际路径，现在你可以在 Multiwfn 窗口中输入 y，然后 .gjf 文件将被 Gaussian 执行，得到的 .wfn 文件将出现在当前文件夹中，之后 .gjf 和 .out 文件将被自动删除。

Multiwfn 还能生成 ORCA 程序的输入文件以生成 .wfn 文件。为此，你应先选择选项 -2 一次，然后选择选项 1，然后将生成三个 ORCA 输入文件。用 ORCA 手动运行它们后，将得到 N.wfn、N-1.wfn、N+1.wfn，你应将它们移动到 Multiwfn 文件夹中。

计算全局和原子指数 由于当前文件夹中已提供了 N.wfn、N+1.wfn 和 N-1.wfn，现在我们可以开始计算 CDFT 量。我们选择选项“2 计算各种定量指标(Calculate various quantitative indices)”，然后 Multiwfn 开始计算 Hirshfeld 电荷并从 .wfn 文件中提取信息，结果输出到当前文件夹中的 CDFT.txt。其内容如下所示，都是自明的。该文件也已作为 examples\CDFT.txt 提供。


```text
 Hirshfeld charges, condensed Fukui functions and condensed dual descriptors
 Units used below are "e" (elementary charge)
     Atom     q(N)    q(N+1)   q(N-1)     f-       f+       f0      CDD
     1(C )  -0.0587  -0.1185   0.0852   0.1439   0.0598   0.1018  -0.0841
     2(C )  -0.0390  -0.1674   0.0268   0.0658   0.1284   0.0971   0.0626
     3(C )  -0.0597  -0.1873   0.0319   0.0916   0.1276   0.1096   0.0360
...[ignored]

 Condensed local electrophilicity/nucleophilicity index (e*eV)
     Atom              Electrophilicity          Nucleophilicity
     1(C )                  0.02576                  0.45535
     2(C )                  0.05533                  0.20827
     3(C )                  0.05496                  0.28982
...[ignored]

Condensed
local
softness
(e/Hartree),
relative
electrophilicity/nucleophilicity
(dimensionless) and condensed local hyper-softness (e/Hartree^2)
     Atom         s-          s+          s0        s+/s-       s-/s+       s(2)
     1(C )      0.3761      0.1562      0.2661      0.4154      2.4075     -0.5746
     2(C )      0.1720      0.3355      0.2538      1.9501      0.5128      0.4271
     3(C )      0.2392      0.3333      0.2863      1.3933      0.7177      0.2459
```


<!-- p.933 -->




```text
...[ignored]

 E(N):     -307.464860 Hartree
 E(N+1):     -307.383614 Hartree
 E(N-1):     -307.163438 Hartree
 E_HOMO(N):     -0.218913 Hartree,   -5.9569 eV
 E_HOMO(N+1):    0.161297 Hartree,    4.3891 eV
 E_HOMO(N-1):   -0.464864 Hartree,  -12.6496 eV
 First vertical IP:     0.301421 Hartree,    8.2021 eV
 First vertical EA:    -0.081246 Hartree,   -2.2108 eV
 Mulliken electronegativity:     0.110088 Hartree,    2.9956 eV
 Chemical potential:            -0.110088 Hartree,   -2.9956 eV
 Hardness (=fundamental gap):    0.382667 Hartree,   10.4129 eV
 Softness:      2.613235 Hartree^-1,    0.0960 eV^-1
 Softness^2:    6.828998 Hartree^-2,    0.0092 eV^-2
 Electrophilicity index:    0.015835 Hartree,    0.4309 eV
 Nucleophilicity index:     0.116285 Hartree,    3.1643 eV
```

你可以将上面显示的凝聚 Fukui 函数和对偶描述符与第 4.7.3 节中手工计算的结果比较，你会发现数据完全一致。显然，使用当前模块计算 CDFT 量比手工计算容易得多！

坦率地说，涉及 N+1 态能量的输出值，如垂直电子亲和势、Mulliken 电负性等不是很准确，因为众所周知，要获得相对准确的阴离子体系能量，必须使用弥散函数。因此，如果你需要这些量的更好结果，当你用 Multiwfn 准备 Gaussian 输入文件时，建议选择至少 6-311+G* 水平的基组。

计算 Fukui 函数和对偶描述符

接下来，我们研究 Fukui 函数（f）和对偶描述符（Δf），它们是实空间函数。选择选项“3 计算 Fukui 函数、对偶描述符及相关函数的格点数据(Calculate grid data of Fukui function, dual descriptor and related functions)”，然后选择“中等质量格点(Medium-quality grid)”，然后 Multiwfn 自动计算 N、N+1 和 N-1 态的电子密度格点数据。之后，你可以选择相应选项来可视化 Fukui 函数或对偶描述符，或将它们作为 cube 文件导出到当前文件夹中。Multiwfn 绘制的各种类型的 f

和 Δf 共同显示在下图中，所有等值都设为 0.007 a.u.：


<!-- p.934 -->



从上图可以发现，当前模块自动生成的 f 和 Δf 与第 4.5.3 节中通过主功能 5 的自定义运算功能手工得到的结果完全一致。毫无疑问使用当前模块要方便得多！

如第 4.5.4 节所述，对偶描述符也可以基于 N-1 和 N+1 态的自旋密度近似评估，然而在当前模块中，对偶描述符及其凝聚形式是以精确方式评估的。

值得注意的是，如果我们通过相应选项将格点数据导出为 cube 文件，那么我们可以用第 4.A.14 节所述的方法非常快速方便地用 VMD 以最高质量将上述函数绘制为

等值面图。例如，下面是由 VMD 渲染的 f − 函数。

计算局域（超）软度和局域亲电性/亲核性指数 上面介绍的模块还可用于导出或可视化局域软度、局域超软度、局域亲电性指数和局域亲核性指数。

例如，我们将导出局域亲电性指数的 cube 文件，回想其定义只是将 f + 乘以全局亲电性指数。因此，我们选择选项“-1 设置各种格点数据的比例因子(Set the scale


![](../imgs/p934_465.png)

![](../imgs/p934_466.png)

<!-- p.935 -->



factor to various grid data)”，输入 0.4309（即选项 2 输出的以 eV 为单位的全局亲电性指数，见 CDFT.txt），然后选择选项“5 导出按比例缩放的 f+ 格点数据为当前文件夹中的 f+.cub(Export grid data of scaled f+ as f+.cub in current folder)”。现在，导出的 f+.cub 对应于局域亲电性指数，单位为 eV/Bohr3。

下一个例子，我们将导出局域超软度（LHS）的 cube 文件，其定义和实际价值在 J. Math. Chem., 62, 461 (2024) 中有仔细讨论。它可以简单地通过将 Δf 乘以全局软度的平方来评估

求得。因此，我们选择选项“-1 设置各种格点数据的比例因子(Set the scale factor to various grid data)”并输入 6.828998（即选项 2 输出的 softness2，以 Hartree-2 为单位，见前述 CDFT.txt），然后选择选项“5 导出按比例缩放的对偶描述符格点数据为当前文件夹中的 DD.cub(Export grid data of scaled dual descriptor as DD.cub in current folder)”。现在，导出的 DD.cub 对应于 LHS，单位为 1/(Bohr3Hartree2) 或简写为 a.u.。

ωcubic 和 ε 的计算 如第 3.25 节所述，亲电性指数 ωcubic 在研究弱相互作用时很有用，至少对卤键如此，而亲电描述符 ε 是比 ω 与亲电性相关性更好的量。如果你还想计算它们，进入当前模块后应先选择选项 -1 将其状态切换为“Yes”，然后只需按上面所示的例子操作（即借助选项 1 准备 .wfn 文件，然后用选项 2 进行计算），然后

选项 2 输出的 CDFT.txt 将包含 ωcubic、其在每个原子上的凝聚值以及 ε。还打印了一个中间量，即第二垂直电离势。

更具体地，对于当前例子，进入当前模块后你应输入

-1 // 切换是否计算 ωcubic 和 ε(Toggle calculating ωcubic and ε) 1 // 生成 N、N+1、N-1、N-2 电子态的 .wfn 文件(Generate .wfn files for N, N+1, N-1, N-2 electronic states) [直接按 ENTER 键] //使用 B3LYP/6-31G* 水平 [直接按 ENTER 键] //使用默认电荷和自旋多重度，即 N 态为 0 1，N+1 态为 -1 2，N-1 态为 1 2，N-2 态为 2 1

现在运行新生成的四个 .gjf 文件以获得 N.wfn、N+1.wfn、N-1.wfn 和 N-2.wfn，然后选择选项 2。从输出的 CDFT.txt 中，你可以找到：


```text
Cubic electrophilicity index (w_cubic):    0.021716 Hartree,    0.5909 eV
Electrophilic descriptor (epsilon):        0.080522 Hartree,    2.1911 eV
```


### 4.22.2 研究轨道加权 Fukui 函数和

### 轨道加权对偶描述符示例

注：本节的中文版及扩展讨论和更多示例是我的博文“通过轨道加权 Fukui 函数和轨道加权对偶描述符预测亲核和亲电反应位点”（http://sobereva.com/533）。

请先阅读第 3.25.3 节，其中介绍了轨道加权 Fukui 函数（𝑓𝑤+ 和 𝑓𝑤−）和对偶描述符 ∆𝑓𝑤，也给出了一些重要注释。本节我们将用这些函数研究几个体系。

第 1 部分：C60 在本部分我们将用轨道加权函数揭示 C60 的反应位点，它具有高点群对称性，其前线分子轨道高度简并。像这样的分子无法用标准形式的 Fukui 函数和对偶描述符合理研究。该体系在 B3LYP/6-31G* 水平下生成的 .fch 文件可从以下地址下载


<!-- p.936 -->



http://sobereva.com/multiwfn/extrafiles/C60.zip，它是当前分析的输入文件。

启动 Multiwfn 并输入以下命令 C60.fch 22 // 计算概念密度泛函理论中的各种量(Calculate various quantities in conceptual density functional theory)

在当前菜单中，你可以用选项 4 设置后续轨道加权计算中使用的 Δ 参数，在本例中我们保持默认值（0.1 Hartree）不变，只有当你发现结果不满意时才应适当改变。

我们首先可视化轨道加权函数的等值面。输入以下命令 7 // 计算 OW Fukui 函数和 OW 对偶描述符的格点数据(Calculate grid data of OW Fukui function and OW dual descriptor) 2 // 中等质量(Medium quality) 然后你可以用相应选项可视化 𝑓𝑤+、𝑓𝑤−、𝑓𝑤0 和 ∆𝑓𝑤 的等值面，它们共同显示如下。注意应将等值改为适当的值，否则等值面甚至可能不可见。下面绘图使用了 0.0003 a.u. 的等值面。

在上图中，绿色和蓝色等值面分别代表正值和负值部分。如你所见，所有轨道加权函数的分布都符合分子点群对称性，这是轨道加权形式独有的优势。相比之下，如果你绘制 HOMO 的密度（对应于 f − 的冻结轨道形式）或计算并绘制通过有限差分（ρN − ρN-1）得到的 f −，你会发现它们的分布是反直觉的（与分子对称性不一致），因此在揭示反应位点方面毫无用处。如第 4.5.4 节所述，具有大正 f − 的区域或具有显著负 Δf 的区域对应于具有显著亲核性的位点，或等价地，易受亲电攻击。从上图我们发现，最易发生亲电攻击的位点是 [6,6] 型 C-C 键（即由两个相邻六元环共用的键）上方的区域。该观察与实验发现完全一致（见 ∆𝑓𝑤 的原始论文，即 J. Phys. Chem. A, 123, 10556 (2019)，其中有广泛讨论），根据 vdW 表面上平均局域电离能极小值的分布也可以进一步证实这一结论，见第 4.12.2 节关于如何进行这类分析。

轨道加权形式的 Fukui 函数和对偶描述符由多个轨道贡献。如果你想查看权重以更好地理解轨道加权函数的工作方式，在当前模块中你可以选择“5 打印当前轨道加权(OW)计算中使用的轨道权重(Print current orbital weights used in orbital-weighted (OW) calculation)”，然后你将看到


```text
 10 Highest weights in orbital-weighted f+
```


![](../imgs/p936_467.png)

<!-- p.937 -->




```text
 Orbital   181 (LUMO  )   Weight:  12.47 %   E_diff:     1.752 eV
 Orbital   182 (LUMO+1)   Weight:  12.47 %   E_diff:     1.752 eV
 Orbital   183 (LUMO+2)   Weight:  12.47 %   E_diff:     1.752 eV
 Orbital   184 (LUMO+3)   Weight:   6.32 %   E_diff:     2.847 eV
 Orbital   185 (LUMO+4)   Weight:   6.32 %   E_diff:     2.847 eV
 Orbital   186 (LUMO+5)   Weight:   6.32 %   E_diff:     2.847 eV
 Orbital   187 (LUMO+6)   Weight:   4.70 %   E_diff:     3.207 eV
 Orbital   188 (LUMO+7)   Weight:   4.70 %   E_diff:     3.207 eV
 Orbital   189 (LUMO+8)   Weight:   4.70 %   E_diff:     3.207 eV

 10 Highest weights in orbital-weighted f-
 Orbital   180 (HOMO  )   Weight:   9.06 %   E_diff:    -1.752 eV
 Orbital   179 (HOMO-1)   Weight:   9.06 %   E_diff:    -1.752 eV
 Orbital   178 (HOMO-2)   Weight:   9.06 %   E_diff:    -1.752 eV
 Orbital   177 (HOMO-3)   Weight:   9.06 %   E_diff:    -1.752 eV
 Orbital   176 (HOMO-4)   Weight:   9.06 %   E_diff:    -1.752 eV
 Orbital   175 (HOMO-5)   Weight:   5.02 %   E_diff:    -2.728 eV
 Orbital   174 (HOMO-6)   Weight:   5.02 %   E_diff:    -2.728 eV
 Orbital   173 (HOMO-7)   Weight:   5.02 %   E_diff:    -2.728 eV
 Orbital   172 (HOMO-8)   Weight:   5.02 %   E_diff:    -2.728 eV
 Orbital   171 (HOMO-9)   Weight:   5.02 %   E_diff:    -2.728 eV
```

其中“E_diff”是轨道能量与化学势之差，化学势近似取为E(HOMO)与E(LUMO)的平均值。显然，轨道能量越接近化学势，该轨道的权重就越高。

你也可以计算凝聚的𝑓𝑤+、𝑓𝑤−、𝑓𝑤0和∆𝑓𝑤，从而可以定量地研究每个原子位点上的数值。为此，在当前模块中应选择“6 计算凝聚的轨道加权Fukui函数和轨道加权对偶描述符(Calculate condensed OW Fukui function and OW dual descriptor)”。不过，对于上面研究的C60而言，这些凝聚量没有意义，因为所有原子在空间上都是等价的。

顺便值得一提的是，𝑓𝑤+、𝑓𝑤−、𝑓𝑤0和∆𝑓𝑤在分子表面上的极值点可以通过定量分子表面分析模块精确定位，从而可以定量比较不同区域的数值。使用该模块的许多例子已在

4.12节中给出。下面我们将考察∆𝑓𝑤在ρ = 0.01 a.u.等值面上的极值。首先，将`settings.ini`中的“iuserfunc”参数设为98，因为如2.7节所述，∆𝑓𝑤对应第98个自定义函数。然后启动Multiwfn并输入

!!! terminal "Multiwfn 交互"

    - **C60.fch 12** — 定量分析分子表面(Quantitative analysis of molecular surface)
    - **1** — 选择定义表面的方式(Select the way to define surface)
    - **1** — 电子密度的等值面(Isosurface of electron density)

!!! terminal "Multiwfn 交互"

    - **0.01** — 使用ρ = 0.01 a.u.等值面定义表面(Use ρ = 0.01 a.u. isosurface to define the surface)
    - **2** — 选择映射的函数(Select mapped function)
    - **-1** — 自定义实空间函数(User-defined real space function)，此时对应∆𝑓𝑤
    - **3** — 生成分子表面时格点的间距(Spacing of grid points for generating molecular surface)


<!-- p.938 -->



0.25 // 使用比默认值稍大的格点间距以降低耗时。此设置对当前研究已足够精细(Use slightly larger grid spacing than default to reduce cost. This setting is already fine enough for present investigation)

0 // 开始分析(Start analysis) 计算完成后，在后处理菜单中选择选项0以可视化极值点。为了使图形更清晰，我们在图形界面中将“原子尺寸比例(Ratio of atomic size)”改为3.0以放大原子球。图形界面窗口中的图形如下所示。标注了∆𝑓𝑤的几个极小值点（蓝色小球）的值，这些值可在文本窗口中找到。红色小球对应极大值点。

可以看出，[6,6]键上方的∆𝑓𝑤比其他区域明显更负，因此这些位置具有最高的亲电反应活性。虽然每个五元环中心上方也有表面极小值，但数值略为正，因此五元环没有明显的参与亲电反应的倾向。

第二部分：环[18]碳 环[18]碳在我的工作Carbon, 165, 468 (2020)、Carbon, 165, 461 (2020)以及http://sobereva.com/carbon_ring.html中得到了非常系统的研究，更多内容见后者。该体系具有高对称性（D9h），因此非常适合用轨道加权函数进行研究。该体系的.fchk可直接通过http://sobereva.com/multiwfn/extrafiles/C18.zip下载，

该文件是在ωB97XD/def2-TZVP水平下生成的。该体系∆𝑓𝑤=0.0008 a.u.的等值面如下所示。


![](../imgs/p938_468.png)

<!-- p.939 -->



环[18]碳含有两种C-C键，一种短键和一种长键，它们交替出现。两条短键用红色箭头标出。从上图可以清楚地看到，短C-C键和长C-C键分别容易受到亲电和亲核攻击，因为前者被负等值面包围，而后者被正等值面包围。

在Multiwfn中，也可以将∆𝑓𝑤绘制为平面图。作为例子，我们将在环[18]碳的分子平面上把∆𝑓𝑤绘制为颜色填充图。我们先将`settings.ini`中的“iuserfunc”参数设为98，然后启动Multiwfn并输入

!!! terminal "Multiwfn 交互"

    - **C18.fchk 4** — 绘制平面图(Plot plane map)
    - **100** — 自定义实空间函数(User-defined real space function)，此时对应∆𝑓𝑤
    - **1** — 颜色填充图(Color-filled map) [按回车键使用默认格点设置(Press ENTER button to use default grid setting)]
    - **1** — XY平面(XY plane)
    - **0** — Z=0 我们关闭弹出的图，然后在后处理菜单中调整一些设置并重新绘制，之后你将看到如下的图。蓝色等值线对应vdW表面。


![](../imgs/p939_469.png)

<!-- p.940 -->



从上图可以发现，环的内侧边缘比外侧边缘更具反应活性，因为内侧边缘的∆𝑓𝑤绝对值更大。

第三部分：CH3Cl 最后，我们用∆𝑓𝑤研究CH3Cl的反应活性。输入文件为examples\CH3Cl.fchk。我们用与上面例子相同的方法计算∆𝑓𝑤的格点数据，不过为了获得更好的图形效果，这次我们不直接在Multiwfn中可视化等值面，而是通过相应选项将∆𝑓𝑤的格点数据导出为OW_DD.cub，然后用4.A.14节所述方法通过VMD程序方便地将其渲染为等值面图。0.008 a.u.的等值面如下所示。

可以看出，在Cl原子周围出现了环形负区域，表明该区域表现出Lewis碱特征。在C-Cl键的两端，∆𝑓𝑤明显为正，表明碳一端容易受到亲核攻击（例如SN2反应），而

Cl一端表现为Lewis酸，这与存在σ-hole区域的事实一致。

顺便提一下，你也可以像C60的例子那样研究∆𝑓𝑤在分子表面上的极值，从而在定量水平上讨论∆𝑓𝑤。


![](../imgs/p940_470.png)

![](../imgs/p940_471.png)

<!-- p.941 -->



### 4.22.3 （准）简并HOMO/LUMO情形下CDFT分析的例子


### HOMO/LUMO case

如3.25.4节所述，除了采用轨道加权形式外，当HOMO和/或LUMO（准）简并时，Multiwfn还支持另一种形式来进行CDFT分析。这种形式仅依赖于电子密度，因此理论上比轨道加权形式更严格，代价是需要额外的计算量，因为还需计算N+p和N-q态的波函数文件，其中p和q分别为LUMO和HOMO的简并度。接下来，我将给出两个例子。

### 4.22.3.1 苯的Fukui函数和对偶描述符

本节我将以苯为例说明如何考虑HOMO/LUMO简并来计算Fukui函数和对偶描述符。因为需要根据轨道能量确定简并度，所以我们应先为所研究的构型生成一个波函数文件。examples\benzene.fch是由Gaussian 16在B3LYP/6-31G*水平下做几何优化任务产生的波函数文件。

启动Multiwfn并输入examples\benzene.fch 22 // 计算概念密度泛函理论中的各种量(Calculate various quantities in conceptual density functional theory) -3 // 设置前线分子轨道简并度(Set degree of frontier molecular orbital degeneracy) 现在屏幕上显示最低10个未占据MO的信息，以帮助你确定LUMO简并度


```text
...[ignored]
Orbital    25 (LUMO+3)   Energy:     3.838 eV  E_diff:     3.737 eV
Orbital    24 (LUMO+2)   Energy:     2.346 eV  E_diff:     2.246 eV
Orbital    23 (LUMO+1)   Energy:     0.100 eV  E_diff:     0.000 eV
Orbital    22 (LUMO  )   Energy:     0.100 eV
```

从轨道能量可以清楚地看出，LUMO与LUMO+1完全简并，而LUMO+2能量明显更高，因此LUMO简并度为2。于是，我们在此输入2（注意Multiwfn提示你若直接按回车键，将使用简并度2。这是因为Multiwfn通过统计有多少个未占据轨道能量与LUMO相差小于0.01 eV来自动确定LUMO简并度）。

然后屏幕上显示最高10个占据MO的信息：


```text
Orbital    21 (HOMO  )   Energy:    -6.720 eV
Orbital    20 (HOMO-1)   Energy:    -6.720 eV  E_diff:     0.000 eV
Orbital    19 (HOMO-2)   Energy:    -9.234 eV  E_diff:    -2.514 eV
Orbital    18 (HOMO-3)   Energy:    -9.234 eV  E_diff:    -2.514 eV
...[ignored]
```

发现HOMO与HOMO-1能量完全相同，因此现在我们输入2以表明HOMO简并度为2（你也可以直接按回车键使用自动确定的简并度2）。

接下来，你可以用自己喜欢的量子化学程序手动生成N、N+2和N-2态的波函数文件。为方便起见，这里我们让Multiwfn帮我们准备输入文件。输入以下命令：


<!-- p.942 -->



1 // 将准备用于生成N、N+2、N-2态.wfn文件的Gaussian单点输入文件(Single point input files of Gaussian for generating .wfn files for N, N+2, N-2 states will be prepared)（若你是ORCA用户，可在选此选项前先选选项-2切换为ORCA程序(If you are an ORCA user, you can choose option -2 to change to ORCA program before selecting this option)）

[按回车键(Press ENTER button)] //使用默认的B3LYP/6-31G*水平做单点计算(Use the default B3LYP/6-31G* level for single point calculation) [按回车键(Press ENTER button)] //如提示所述，直接按回车键将对N、N+2和N-2态分别使用(0 1)、(-2 3)和(2 3)的净电荷与自旋多重度(As mentioned in prompt, pressing ENTER button directly will use net charge and spin multiplicity of (0 1), (-2 3) and (2 3) for the N, N+2 and N-2 states, respectively)。这些组合对当前情形是合理的(These combinations are reasonable for present case)

因为目前N+1和N-1态尚未定义，而选项2中计算第一垂直电离能、垂直电子亲和能及其相关量（如软度）时需要E(N+1)和E(N-1)，所以Multiwfn还会要求你输入这两个态的净电荷与自旋多重度。然而，在本例中我们只想计算Fukui函数和对偶描述符，它们与这些能量量无关，所以我们按两次回车键跳过这两个态的定义。

现在当前文件夹中已生成N.gjf、N+2.gjf和N-2.gjf，你可以手动用Gaussian运行它们，或直接输入y让Multiwfn调用你机器上的Gaussian运行它们（此时`settings.ini`中的“gaupath”须已正确设置）。计算全部完成后，当前文件夹中将有N.wfn、N+2.wfn和N-2.wfn。

然后我们绘制考虑HOMO和LUMO简并的Fukui函数和对偶描述符的等值面图。输入以下命令

3 // 计算Fukui函数和对偶描述符的格点数据(Calculate grid data of Fukui function and dual descriptor)（若当前文件夹中没有N.wfn、N+2.wfn和N-2.wfn，Multiwfn会要求你输入三个态的波函数文件路径(if N.wfn, N+2.wfn and N-2.wfn are not present in current folder, Multiwfn will ask you to input path of wavefunction files of the three states)）

2 // 中等质量格点(Medium-quality grid)

2 // 可视化f−等值面(Visualize isosurface of f −) 将等值改为0.005 a.u.后，你将看到如下的图

从上图可以看出，考虑HOMO简并的f−分布，即(ρN − ρN-2)/2，完全符合分子对称性。正区域（绿色等值面所示）主要出现在碳原子上下方的分子平面两侧，

从而正确表明π电子云容易发生亲电攻击。相比之下，若你用通常方式绘制f−，即ρN − ρN-1，你会发现其分布明显违背实际分子对称性，从而对亲电攻击优先位点得出误导性结论。

类似地，你可以用选项1、3和4分别可视化考虑前线MO简并下计算的f+、f0和对偶

描述符Δf的等值面图。


![](../imgs/p942_472.png)

<!-- p.943 -->



关于f+和对偶描述符计算水平选择的说明 对于苯体系，若你用带弥散函数的B3LYP基组（如6-311+G*）生成波函数文件，你会发现算得的

（准）简并f+和Δf分布极其弥散（表现出很强的Rydberg特征）且不完全符合分子对称性。这是因为该泛函严重的自相互作用误差（SIE）问题使N+2态的电子过度弥散，而当前基组有能力描述远离分子的空间区域。此时得到的f+

和Δf行为不好，不能用于讨论优先反应位点。

值得注意的是，在Chem. Phys. Lett., 724, 29 (2019)中发现，若基于有限差分评估Fukui函数和对偶描述符（与当前情形相同），即使不带弥散函数的3-zeta基组基本上也能得到有意义的对偶描述符。

尽管如本例所用的B3LYP/6-31G*水平给出

看似合理的f+和Δf分布，若你追求更严格的结果，我推荐使用长程校正DFT泛函如ωB97XD结合不带弥散函数的3-zeta基组，例如6-311G*。ωB97XD的SIE问题比常用的B3LYP弱得多，因此在阴离子态电子束缚得更紧；不带弥散函数的3-zeta基组足以描述价层电子结构，同时电子被

迫束缚在价层区域内，保证f+和Δf只代表化学感兴趣的区域。

### 4.22.3.2 C60富勒烯的局域软度和局域超软度

本节我将说明C60

富勒烯局域软度和局域超软度的计算。它们在J. Math. Chem., 62, 461 (2024)中是在ωB97XD/6-311+G*水平下给出的，但在本节中，我们改用6-311G*以大大节省计算量。由Gaussian 16在ωB97XD/6-311G*水平下几何优化产生的.fchk文件

（C60_wB97XD_opt.fchk）可从http://sobereva.com/multiwfn/extrafiles/C60_wB97XD_opt.7z下载。

启动Multiwfn并输入C60_wB97XD_opt.fchk 22 // 计算概念密度泛函理论中的各种量(Calculate various quantities in conceptual density functional theory) -3 // 设置前线分子轨道简并度(Set degree of frontier molecular orbital degeneracy) [直接按回车键(Press ENTER button directly)] // 使用自动确定的LUMO简并度3(Use automatically determined LUMO degeneracy of 3) [直接按回车键(Press ENTER button directly)] // 使用自动确定的HOMO简并度5(Use automatically determined HOMO degeneracy of 5) 1 // 生成各种电子态的.wfn文件(Generate .wfn files for various electrons states) wB97XD/6-311G* symm=loose scf=conver=7 // 执行Gaussian单点任务的关键词(Keywords for performing single point task of Gaussian)。“symm=loose”确保Gaussian将利用C60的Ih点群以大大降低耗时。“scf=conver=7”略放宽SCF收敛阈值以更容易收敛(The “symm=loose” ensures that Gaussian will utilize Ih point group of C60 to greatly reduce cost. “scf=conver=7” slightly loosens SCF convergence threshold to make it easier to reach)

[按回车键(Press ENTER button)] //对N、N+3和N-5态使用默认净电荷与自旋多重度(0 1)、(-3 4)和(5 6)(Use default net charge and spin multiplicity of (0 1), (-3 4) and (5 6) for the N, N+3 and N-5 states, respectively)

-1,2 // N+1态的净电荷与自旋多重度(Net charge and spin multiplicity of N+1 state) 1,2 // N-1态的净电荷与自旋多重度(Net charge and spin multiplicity of N-1 state) 现在当前文件夹中已生成N.gjf、N-1.gjf、N+1.gjf、N-3.gjf和N+5.gjf，输入y让Multiwfn调用Gaussian执行计算（或手动计算它们）。计算后，当前文件夹中将有N.wfn、N-1.wfn、N+1.wfn、N-3.wfn和N+5.wfn。

然后选择选项2计算各种CDFT量并打印到当前文件夹的CDFT.txt中。从中我们找到软度及其平方：


<!-- p.944 -->




```text
 Softness:      4.638426 Hartree^-1,    0.1705 eV^-1
 Softness^2:   21.514996 Hartree^-2,    0.0291 eV^-2
```

接下来，输入以下命令获得局域超软度，它是软度平方与对偶描述符的乘积

!!! terminal "Multiwfn 交互"

    - **3** — 计算Fukui函数、对偶描述符及相关函数的格点数据(Calculate grid data of Fukui function, dual descriptor and related functions)
    - **-10** — 设置扩展距离(Set extension distance)
    - **6** — 6 Bohr，比默认值稍大，以避免等值设得很小时等值面在盒子边界处被截断(6 Bohr, which is slightly larger than the default one to avoid isosurface truncation at box boundary when isovalue is set to a small value)

3 // 因C60不小，我们用高质量格点以保证格点间距不会太大从而导致等值面图质量差(Since C60 is not small, we use high-quality grid to guarantee that grid spacing will not be too large and thus leading to poor isosurface map)

!!! terminal "Multiwfn 交互"

    - **-1** — 设置各类格点数据的缩放因子(Set the scale factor to various grid data)
    - **21.514996** — Hartree-2单位的软度平方(Square of softness in Hartree-2)
    - **8** — 将缩放后的对偶描述符格点数据导出为当前文件夹中的DD.cub(Export grid data of scaled dual descriptor as DD.cub in current folder) 现在当前文件夹中新生成的DD.cub对应单位为1/(Bohr3Hartree2)的局域超软度。用VMD将其绘制为等值0.001的等值面图，你将看到如下的图，它与J. Math. Chem., 62, 461 (2024)的图4基本完全相同，尽管当前基组6-311G*与该工作中用的昂贵得多的6-311+G*不同。同时，值得注意的是，此图的主要特征与4.22.2节得到的C60的∆𝑓𝑤相当。

用类似方法，我们可以得到局域软度，其定义为软度与Fukui函数的乘积。输入以下命令

!!! terminal "Multiwfn 交互"

    - **-1** — 设置各类格点数据的缩放因子(Set the scale factor to various grid data)
    - **4.638426** — Hartree-1单位的软度(Softness in Hartree-1)
    - **6** — 将缩放后的f-格点数据导出为当前文件夹中的f-.cub(Export grid data of scaled f- as f-.cub in current folder)

现在新生成的f-.cub对应局域软度s−，单位为1/(Bohr3Hartree)。下图是用VMD绘制的s−的0.005和0.003等值面，前者与J. Math. Chem., 62, 461 (2024)的图2完全相同，而后者更清楚地区分最容易发生亲电攻击的键（即两个六元环共用的键），它看起来与4.22.2节中C60的𝑓𝑤−图非常相似。


![](../imgs/p944_473.png)

<!-- p.945 -->



### 4.22.3.3 开壳层分子O2的Fukui函数和对偶描述符

请先阅读3.25.4.2节以熟悉评估开壳层情形各种形式Fukui函数和对偶描述符的工作方程。本例我们计算O2的函数，它是具有前线MO简并的代表性开壳层分子（三重态基态）。

!!! terminal "Multiwfn 交互"

    - **启动Multiwfn并输入examples\O2.fch** — 基态O2在B3LYP/6-31G*水平下的波函数文件(Wavefunction file of ground state O2 at B3LYP/6-31G* level)
    - **22** — 计算概念密度泛函理论中的各种量(Calculate various quantities in conceptual density functional theory)
    - **12** — 基于概念自旋极化DFT框架计算Fukui函数和对偶描述符(Calculate Fukui function and dual descriptor based on formalism of conceptual spin-polarized DFT)

1 // 设置前线分子轨道简并度(Set degeneracy of frontier molecular orbitals)

[直接按回车键(Press ENTER button directly)] // 使用建议的LUMO(α)简并度(Use suggested degeneracy of LUMO(alpha)) [直接按回车键(Press ENTER button directly)] // 使用建议的HOMO(α)简并度(Use suggested degeneracy of HOMO(alpha)) [直接按回车键(Press ENTER button directly)] // 使用建议的LUMO(β)简并度(Use suggested degeneracy of LUMO(beta)) [直接按回车键(Press ENTER button directly)] // 使用建议的HOMO(β)简并度(Use suggested degeneracy of HOMO(beta)) 现在你可以看到前线MO简并度的汇总：


```text
Degeneracy of LUMO(alpha):  1
Degeneracy of HOMO(alpha):  2
Degeneracy of LUMO(beta):   2
Degeneracy of HOMO(beta):   2
```

接下来，我们输入2 //生成各种电子态的.wfn文件(Generate .wfn files for various electrons states) [直接按回车键(Press ENTER button directly)] // 使用默认B3LYP/6-31G*作为生成Gaussian输入文件的计算水平(Use the default B3LYP/6-31G* as computational level for generating Gaussian input files)

现在你会发现当前文件夹中已生成state0_3.gjf、state-1_4.gjf、state-2_1.gjf、state2_1.gjf和state2_5.gjf，它们是用于生成本次研究涉及的各种电子态.wfn文件的Gaussian单点任务输入文件。例如，state-1_4.gjf对应净电荷-4、自旋多重度4。若你的本地机器装有Gaussian，你可以输入y请Multiwfn调用Gaussian计算它们；或者，手动用Gaussian计算它们，然后把得到的.wfn文件放入当前文件夹。

现在选择选项3并选中等质量格点开始计算不同态电子密度的格点数据。之后，在后处理菜单中，选择将你感兴趣的实空间函数可视化为等值面图，或将格点数据导出为.cub文件。例如，我们选择选项7绘制Δ𝑓Δ𝑁𝑆<0形式的对偶描述符，在把等值面改为0.0005 a.u.并将

材质设为透明后，你将看到如下的图，它与Chem. Phys. Lett., 506, 104 (2011)图7中的DUAL-UDFT情形完全相同。


![](../imgs/p945_474.png)

![](../imgs/p945_475.png)

<!-- p.946 -->



不同态的电子密度(Electron density of different states)。之后，在后处理菜单中，选择将你感兴趣的实空间函数可视化为等值面图，或将格点数据导出为.cub文件。例如，我们选择选项7绘制Δ𝑓Δ𝑁𝑆<0形式的对偶描述符，在把等值面改为0.0005 a.u.并将

材质设为透明后，你将看到如下的图，它与Chem. Phys. Lett., 506, 104 (2011)图7中的DUAL-UDFT情形完全相同。


### 4.22.4 绘制Fukui势和对偶描述符势的例子


### potential

本例说明为马来酸酐绘制Fukui势和对偶描述符势，后者也见于J. Math. Chem., 62, 1094 (2024)，它是在M06-2X/6-311++G(d,p)水平下计算的，所以我们将用同样水平重现该结果。若你对这两种势不熟悉，请先查看3.25.1节。

启动Multiwfn并输入examples\maleic_anhydride.xyz //几何构型在M06-2X/6-311++G(d,p)水平下优化(Geometry was optimized at M06-2X/6-311++G(d,p) level)

!!! terminal "Multiwfn 交互"

    - **22** — 概念DFT(CDFT)分析(Conceptual DFT (CDFT) analysis)
    - **1** — 生成N、N+1、N-1电子态的.wfn文件(Generate .wfn files for N, N+1, N-1 electrons states) M062X/6-311++G(d,p)

对N、N+1和N-1态使用(0 1)、(-1 2)和(1 2)(Use (0 1), (-1 2) and (1 2) for N, N+1 and N-1 states) y // 调用Gaussian计算这三个态(Invoke Gaussian to calculate the three states)（假设你已在`settings.ini`中正确设置“gaupath”(assume that you have properly set “gaupath” in `settings.ini`)）

9 // 计算Fukui势和对偶描述符势的格点数据(Calculate grid data of Fukui potential and dual descriptor potential) 1 // 因计算ESP格点数据相对昂贵，所以这里选择用低质量格点(Because calculating ESP grid data is relatively expensive, so here we choose to use low-quality grid)

现在，你可以选择相应选项可视化各种Fukui势和对偶描述符势（DDP），𝑉𝑓+、𝑉𝑓−和𝐷𝐷𝑃= 𝑉𝑓+ −𝑉𝑓−的等值面图

如下所示，正、负部分分别显示为绿色和蓝色。DDP图与J. Math. Chem., 62, 1094 (2024)的图5完全一致。DDP图的绿色部分表明C4和C5最容易发生亲核攻击。实验上已知马来酸酐的这两个原子可与亲核的顺式-1,3-丁二烯发生D-A加成反应。


![](../imgs/p946_476.png)

<!-- p.947 -->




### 4.22.5 计算键对偶描述符（BDD）的例子

注：用Multiwfn计算键对偶描述符研究不同化学键反应活性请见“使用Multiwfn计算键对偶描述符以研究不同化学键的反应性”(Using Multiwfn to calculate bond dual descriptor to study reactivity of different chemical bonds)”（http://sobereva.com/766）。

请先阅读3.25.1节中关于键对偶描述符（BDD）的简要介绍，并阅读4.22.1节了解概念DFT分析模块的基本用法。本节我将说明以丙烯腈为例计算BDD，其在B3LYP/6-31G*水平下优化的结构如下所示，结构文件为examples\acrylonitrile.xyz。

启动Multiwfn，载入examples\acrylonitrile.xyz，然后输入22 // 概念DFT(CDFT)分析(Conceptual DFT (CDFT) analysis) 1 // 生成N、N+1、N-1电子态的.wfn文件(Generate .wfn files for N, N+1, N-1 electrons states) [直接按回车键(Press ENTER button directly)] // 生成的.gjf文件将对应B3LYP/6-31G*水平的单点任务(The generated .gjf files will correspond to single point task at B3LYP/6-31G* level)

[直接按回车键(Press ENTER button directly)] // 使用默认电荷与自旋多重度，即N态为0 1，N+1态为-1 2，N-1态为1 2(Use default charge and spin multiplicity, namely 0 1 for N state, -1 2 for N+1 state, and 1 2 for N-1 state)

然后在当前文件夹中用Gaussian手动运行N.gjf、N-1.gjf、N+1.gjf，或请Multiwfn调用Gaussian计算它们，之后当前文件夹中将有N.wfn、N-1.wfn和N+1.wfn。然后选择选项“10 计算键对偶描述符(BDD)(Calculate bond dual descriptor (BDD))”。之后，Multiwfn依次载入.wfn文件并计算每个电子态的模糊键级，然后打印BDD，见下文。为便于研究，仅直接给出10个最正和最负的值。


```text
10 most negative BDD values:
    1(C )     3(C ):    -0.562
    6(C )     7(N ):    -0.365
    3(C )     7(N ):    -0.029
```


![](../imgs/p947_477.png)

![](../imgs/p947_478.png)

<!-- p.948 -->




```text
    1(C )     4(H ):    -0.008
    1(C )     5(H ):    -0.008
    4(H )     7(N ):    -0.001
    4(H )     5(H ):    -0.000
    5(H )     7(N ):    -0.000
    2(H )     4(H ):     0.000

10 most positive BDD values:
    1(C )     6(C ):     0.312
    1(C )     7(N ):     0.166
    3(C )     6(C ):     0.064
    3(C )     5(H ):     0.016
    3(C )     4(H ):     0.016
    2(H )     6(C ):     0.006
    2(H )     7(N ):     0.004
    5(H )     6(C ):     0.003
    4(H )     6(C ):     0.003
    1(C )     2(H ):     0.001
```

以上结果表明，C1-C3是最容易受到亲电攻击的键（该键表现出最强的亲核性），其次是C6-N7。C1-C6是最容易受到亲核攻击的键（该键表现出最强的亲电性）。上面给出的有些数据不对应直接成键的原子，如C1-N7和C3-C6；这些可直接忽略。

然后Multiwfn会询问你是否要将所有键的BDD按原子编号顺序导出到当前目录的BDD.txt，并将所有键的BDD按数值排序导出到当前目录的BDD_sorted.txt。你可选择y导出。

注意，BDD计算功能也支持前线分子轨道简并的情形，就像4.22.3节所示的情况。对于这些体系，你应在生成.wfn文件和计算BDD之前先用选项-3设置HOMO和LUMO的简并度。


### 4.22.6 计算对偶离域描述符（DDD）的例子

请先认真阅读3.25.6节以获得关于对偶离域描述符（DDD）的基本知识。本节我将说明如何计算氨基苯体系在DDD

框架下定义的量。该体系在ωB97XD/6-311G(d,p)下计算的.fch文件可从http://sobereva.com/multiwfn/extrafiles/aminobenzene_DDD.7z下载，计算水平和几何构型与DDD原始论文Phys. Chem. Chem. Phys., 28, 19133 (2026)中用的完全相同。我们将用Hirshfeld划分定义用于评估原子重叠矩阵（AOM）的原子空间，DDD原始论文中也用了该划分。

!!! terminal "Multiwfn 交互"

    - **启动Multiwfn并输入aminobenzene_DDD.fch** — 上述压缩包中的文件(The file in the compressed package mentioned above)
    - **22** — 概念DFT(CDFT)分析(Conceptual DFT (CDFT) analysis)
    - **11** — 计算对偶离域描述符(DDD)(Calculate dual delocalization descriptor (DDD))
