# 态密度图(DOS)、光电子

> Multiwfn manual, p.155–162.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.155 -->


所需信息：原子坐标(Atom coordinates)、基函数(Basis functions)

## 3.12 态密度图(DOS)、光电子

## 谱(PES)与 COHP 绘制(Plotting density-of-states (DOS), photoelectron)

## 谱(spectrum (PES)), 与 COHP((10)和 COHP (10))

TDOS、PDOS 和 OPDOS 是最常研究的 DOS 类型，其定义和在 Multiwfn 中的绘制方法将在第 3.12.1 节(Section 3.12.1)、第 3.12.2 节(Section 3.12.2)和第 3.12.3 节(Section 3.12.3)中描述。局域 DOS(LDOS)是一种特殊的 DOS，将在第 3.12.4 节(Section 3.12.4)中介绍。由于 TDOS 与光电子谱(PES)密切相关，该模块也能绘制 PES，这将在第 3.12.5 节(Section 3.12.5)中介绍。在第 3.12.6 节(Section 3.12.6)中，将介绍晶体轨道 Hamilton 布居(COHP)，它与 OPDOS 密切相关。

### 3.12.1 理论(Theory)

态密度(DOS)是固体物理的重要概念，代表单位能量间隔内的状态数，由于能级是连续的，故 DOS 可绘制为曲线图。在孤立体系（如分子）中，能级是分立的，DOS 概念值得商榷，有人认为此时 DOS 完全没有价值。但若把分立能级人工展宽为曲线，DOS 图可用作分析电子结构本质的有价值工具。

孤立体系的总 DOS(TDOS)可写为

$$\mathrm{TDOS}(E)=\sum_{i}\delta(E-\varepsilon_{i})$$

<!-- formula-ocr: formula_p155_091.png 已替换为LaTeX, 原图保留备查 -->

其中 {ε} 为单粒子 Hamilton 的本征值集，δ 为 Dirac delta 函数。若把 δ 替换为展宽函数 F(x)，如 Gaussian、Lorentzian 和 pseudo-Voigt 函数，就得到展宽后的 TDOS。

归一化 Gaussian 函数定义为

xecxG 221)(c −= π 2 2 其中 2ln22 FWHM=c

FWHM 为“半高全宽(full width at half maximum)”的缩写，是 Multiwfn 中的可调参数。FWHM 越大，TDOS 图越平滑，但关于能级分布的细节信息丢失得越多。

归一化 Lorentzian 函数定义为

12FWHM)(×+=xxLπ 22FWHM25.0

Pseudo-Voigt 函数为 Gaussian 函数与 Lorentzian 函数的加权线性组合：

GaussGauss( )( )(1) ( )P xwG xwL x=+−

显然，若 G(x) 和 L(x) 归一化，则 P(x) 的归一化条件恒成立

<!-- p.156 -->


与 wGauss 的选择无关。

展宽后的部分 DOS(PDOS)与重叠 DOS(OPDOS)的曲线图对轨道成分的可视化研究很有价值。片段 A 的 PDOS 定义为

$$\mathrm{P D O S}_{A}(E)=\sum_{i}\Theta_{i,A}F(E-\varepsilon_{i})$$

<!-- formula-ocr: formula_p156_092.png 已替换为LaTeX, 原图保留备查 -->

其中 Θi,A 为片段 A 在轨道 i 中的成分。注意一些文献中用的 “projected DOS” 一词本质上等价于部分 DOS(partial DOS)。

片段 A 与 B 之间的 OPDOS 定义为

$$\mathrm{OPDOS}_{A,B}(E)=\sum_{i}\mathrm{X}_{A,B}^{i}F(E-\varepsilon_{i})$$

<!-- formula-ocr: formula_p156_093.png 已替换为LaTeX, 原图保留备查 -->

其中 X𝐴,𝐵 𝑖 为轨道 i 中片段 A 与 B 间总交叉项的成分。我已

在第 3.10.3 节(Section 3.10.3)中讨论了如何计算 Θ 和 。

在 Multiwfn 中，OPDOS 也可在所有最近邻原子间计算。此时，OPDOS 计算为

$$\mathrm{OPDOS}^{\mathrm{near}}(E)=\sum_{i}\sum_{A}n_{A,A_{\mathrm{adj}}}^{i}F(E-\varepsilon_{i})$$

其中 A 遍历所有原子，Aadj 表示体系中离 A 最近的原子。𝑛𝐴,𝐴adj 𝑖 对应

于轨道 i 中 A 与 Aadj 之间的重叠布居。

当用户定义了一个或多个片段时，Multiwfn 将按下式自动计算每个片段 PDOS 的中心，并在显示 DOS 图时打印在命令行窗口中

$$\mathcal{E}_{c,F}=\frac{\displaystyle\int_{\mathrm{low}}^{\mathrm{high}}E\times\mathrm{PDOS}_{F}(E)\mathrm{d}E}{\displaystyle\int_{\mathrm{low}}^{\mathrm{high}}\mathrm{PDOS}_{F}(E)\mathrm{d}E}$$

其中 low 和 high 为当前 X 轴（能量范围）的下限和上限，F 表示所考虑的片段。经由该功能，可轻松计算 d 带中心(d-band center)，这在研究过渡金属表面化学吸附时很重要。例子见第 4.10.6 节(Section 4.10.6)。

DOS 示例：二茂铁(Illustration of DOS: Ferrocene) 下面是典型分子二茂铁的 DOS 图，对铁用 Lanl2DZ 基组结合 Lanl2 赝势，而对其他元素用 6-31G*。该体系中 Z 轴垂直于环戊二烯基。

<!-- p.157 -->


该图清晰地展示了不同能量范围内的轨道特征，每条分立线对应一个分子轨道(MO)。曲线是对分立线施加展宽函数后得到的。左、右Y轴分别对应曲线和分立线。注意，曲线的相对高度而非绝对高度才是有意义的。可以明显看出，碳的s、px和py原子轨道(品红色曲线)的主要贡献来自低能MO，而非前线MO。在-0.25 a.u.附近的MO的主要组成来自碳的pz轨道(蓝色曲线)和铁原子(红色曲线)。观察代表碳pz与铁原子之间成键的绿色OPDOS曲线，可以认为碳pz轨道对二茂铁的稳定性非常重要，因为OPDOS在这些区间具有很大的正值。HOMO几乎完全由铁轨道贡献，但其与碳pz轨道的轻微重叠仍有利于成键。对于所有虚MO，OPDOS曲线处于负值区域，呈现反键特征，这是由于轨道相位的不利重叠所致，从LUMO等值面图也可以看出这一点。

### 3.12.2 输入文件 (Input file)

.mwfn/.fch/.molden/.gms文件均可用作输入文件。也可以使用Gaussian程序单点任务的输出文件作为输入(必须指定pop=full关键词)。

为通用起见，Multiwfn还支持使用纯文本文件作为输入文件，格式自由，对轨道数目没有上限。文件格式应为

nmo inp

energy occ [strength] [FWHM]  对于轨道1 energy occ [strength] [FWHM]  对于轨道2 energy occ [strength] [FWHM]  对于轨道3 ...

energy occ [strength] [FWHM]  对于轨道nmo 其中energy和occ分别表示轨道能量和占据数。nmo是该文件中记录的轨道数目。inp是输入类型，有以下四种情况：

![](../imgs/p157_022.png)

<!-- p.158 -->


- 1：只载入能量(单位为a.u.)和占据数，而所有轨道的strength和FWHM将分别自动设为1.0和0.25 a.u.
- 2：与1相同，但你还必须为每个轨道指定第3列和第4列的strength和FWHM，因为在这种情况下它们也会被载入。如果某轨道的strength设为k，则该轨道展宽出的曲线将被归一化为k而非1(默认值)
- 3：与1相同，但能量单位为eV。

- 4：与2相同，但能量单位为eV。

### 3.12.3 绘制DOS的选项与基本用法 (Options for plotting DOS and basic usage)

当你进入绘制DOS的界面时，将看到以下选项。注意，只有当输入文件包含基函数信息时，才会出现选项-1和7，也就是说，如果你想绘制PDOS和OPDOS图，必须使用.mwfn/.fch/.molden/.gms文件作为输入。

还请注意，在此界面中，你可以输入s将当前状态(绘图设置、碎片定义和轨道信息)保存到指定文件，也可以输入l从指定文件载入状态，从而无需重复设置即可快速重绘图形。

-6 设置能级位移 (Set shift of energy levels)：在此选项中，可将轨道能量平移一个输入值。如果你输入H，则位移将被设为HOMO能量的负值，从而使DOS图中的HOMO对应于0的位置。

-5 自定义指定MO的能级、占据数、强度和半峰宽 (Customize energy levels, occupations, strengths and FWHMs for specific MOs)：通过此选项，你可以手动设置指定轨道的能量、占据数、强度(strengths)和半峰宽(FWHMs)。例如，如果你只想绘制少数几个MO的DOS，可以将其余MO的strength设为零(默认情况下，所有MO的strength均为1.0)。

-4 显示所有轨道信息 (Show all orbital information)：在屏幕上打印所有轨道的信息。 -3 将能级、强度、半峰宽导出为纯文本文件 (Export energy levels, strengths, FWHMs to plain text file)：将每个轨道的能量、强度和半峰宽导出到当前目录下的orginfo.txt，该文件符合上一节介绍的格式，因此可直接用作输入文件。

-2 为MO-PDOS定义MO碎片 (Define MO fragments for MO-PDOS)：“MO-PDOS”是一种特殊的PDOS，用于揭示不同MO集合(而非原子或基函数)所贡献的DOS，不同MO集合对应的DOS曲线和分立线用不同颜色绘制。此选项用于定义“MO-PDOS”作图中所涉及的不同MO集合。示例见4.10.5节。

-1 为PDOS/OPDOS定义碎片 (Define fragments for PDOS/OPDOS)：在此选项中，你最多可定义10个碎片，从而绘制PDOS和OPDOS。进入此选项后，屏幕上会显示当前碎片的信息。你可以输入x来定义碎片x，输入-x取消碎片x的定义，或输入i,j交换碎片i和j的定义。输入0或q离开此界面。通过选项0，将为此选项中定义的每个碎片绘制PDOS。只有当碎片1和2均已定义时，才能绘制OPDOS。

值得注意的是，在绘制OPDOS时，所定义的碎片1和碎片2可以共用一个或多个基函数，两个碎片甚至可以具有相同的定义。此时只计算基函数之间的交叉项，而忽略局域项(表征on-site相互作用)。

0 绘制TDOS/PDOS/OPDOS图形 (Draw TDOS/PDOS/OPDOS graph)：选择此选项后，TDOS图将立即显示在屏幕上。如果已定义任何碎片，将绘制TDOS+PDOS。如果碎片1和2均已定义，将绘制TDOS+PDOS+OPDOS，但在这种情况下你也可以选择选项-0以仅绘制TDOS+PDOS。

<!-- p.159 -->


00 绘制TDOS与最近邻原子间的OPDOS (Draw TDOS and OPDOS between nearest atoms)：如果你尚未定义任何碎片，则可见此选项。选择后，将同时绘制TDOS和3.12.1节所述的OPDOSnear。

1 选择展宽函数 (Select broadening function)：选择将使用的展宽函数，可选择Lorentzian、Gaussian或Pseudo-Voigt函数。默认为Gaussian。

2 设置能量范围与步长 (Set energy range and step)：此选项用于设置X轴的下限、上限以及标签间隔。

3 设置半峰全宽(FWHM) (Set full width at half maximum (FWHM))：顾名思义。 4 设置DOS曲线的缩放比例 (Set scale ratio for DOS curve)：如果此选项设为k，则所有曲线的高度将在整个能量范围内乘以k。

5 设置Gaussian加权系数 (Set Gaussian-weighting coefficient)：此选项设置上一节提到的wgauss，仅当选择Pseudo-Voigt函数时才出现。

6 选择轨道自旋 (Choose orbital spin)：仅当载入的文件包含基函数信息且波函数为非限制性时才出现此选项。此选项决定计入哪组轨道(alpha、beta，或alpha和beta两者)。

7 设置计算PDOS的方法 (Set the method for calculating PDOS)：支持Mulliken、SCPA、Hirshfeld和Becke方法计算用于绘制PDOS的轨道组成，可通过此选项选择其中之一。Hirshfeld和Becke方法比Mulliken和SCPA方法更稳健，尤其对未占据MO而言，但可惜计算代价更高，且此时无法绘制OPDOS(即碎片只能定义为原子集合)。非常重要的一点是，当存在弥散函数时，基于Mulliken或SCPA方法绘制的PDOS图将毫无意义！如果由于特殊原因无法忽略弥散函数，必须采用Hirshfeld或Becke方法。

对于孤立体系，默认方法为Mulliken；而对于周期性体系，默认方法为SCPA，因为对大的周期性单胞计算重叠矩阵可能非常耗时，而SCPA不需要重叠矩阵。

8 在a.u.与eV之间切换单位 (Switch unit between a.u. and eV)：可通过此选项切换DOS图X轴的单位。eV更为常用。

9 切换是否用线高表示轨道简并 (Toggle using line height to show orbital degeneracy)：如果你想在DOS图中显示轨道简并，可选择此选项启用该效果，然后会被要求输入判定简并的能量差阈值。此功能可用于绘制TDOS和MO-PDOS，但不能用于绘制PDOS。

一旦在DOS模块中选择选项0，Multiwfn即开始计算数据，随后弹出DOS图。你可以看到有一条垂直虚线，标示了HOMO能级的位置。注意，有人认为这是Fermi能量，但这对孤立体系而言是一个定义不清的概念，任何满足 EHOMO且< ELUMO的能量都可视为“Fermi能量”。

关闭图形后，屏幕上会出现一个后处理菜单，其中包含许多选项，这些选项都是自解释的，可用于调整各种绘图参数。更改参数后，可选择“1 Show graph again(再次显示图形)”查看效果。值得注意的是，有一个名为“Set scale factor of Y-axis range for OPDOS(OPDOS的Y轴范围缩放因子)”的选项，如果该值设为k，且左轴(对应TDOS/PDOS)范围设为例如[-3.5, 2.0]，则右轴(对应OPDOS)范围将变为[-3.5*k, 2.0*k]。Multiwfn使用双轴的原因是OPDOS的量级一般远小于TDOS和PDOS。你还可以

<!-- p.160 -->


选择将DOS图导出为当前文件夹中的图形文件，或将DOS的X-Y数据集导出为纯文本文件，以便用第三方软件(如Origin)重绘图形。通过选择选项0可返回上一界面，通过反复调整可逐步改善DOS图的质量，直至满意为止。

DOS曲线的绝对值没有明显的实际意义，只有曲线在不同能量区域的相对高度才有意义。因此，在恰当设置各项绘图参数后，可在后处理菜单中选择选项“13 Toggle showing labels and ticks on Y-axis(切换是否显示Y轴标签和刻度)”将其状态切换为“No”。

在4.10.1节给出了绘制TDOS、PDOS和OPDOS的非常详细的示例，而4.10.3节说明了如何通过Multiwfn结合Origin软件绘制开壳层体系的DOS以获得更好效果。

### 3.12.4 局域DOS (Local DOS)

有一种特殊的DOS称为局域DOS(local DOS, LDOS)，也称为空间DOS(spatial DOS)。给定点r处的LDOS曲线按下式计算：

$$\mathrm{L D O S}(\mathbf{r},E)=\sum_{i}\varphi_{i}^{2}(\mathbf{r})f(E-\varepsilon_{i})$$

<!-- formula-ocr: formula_p160_094.png 已替换为LaTeX, 原图保留备查 -->

值得注意的是，在一些第一性原理书籍和论文中，“Local DOS”一词实际上指的是3.12.1节介绍的PDOS，不要混淆！

要绘制LDOS图，在进入主功能10后选择选项“10 Draw local DOS for a point(为一点绘制局域DOS)”，然后会被提示输入点r的坐标。

还可以将一条直线上均匀放置的一组点的LDOS绘制为颜色填充图，X轴对应能量，Y轴对应直线上相对于起点的坐标。要绘制这种LDOS图，选择选项“11 Draw local DOS along a line(沿一条线绘制局域DOS)”，你会被提示输入定义该直线的起点和终点坐标，以及组成该直线的点的数目。

在DOS模块中，控制FWHM、能量单位、能量范围和缩放比例的选项会影响所得LDOS图形。

注意，碎片定义不影响LDOS的结果，即LDOS始终对应于总DOS。然而，如果你想分离对LDOS的角动量贡献，可以使用主功能6的子功能25将所有MO中不需要的GTF的系数置零，则它们将不对LDOS产生贡献。

绘制LDOS的示例见4.10.2节。

### 3.12.5 光电子能谱 (Photoelectron spectrum)

基于(广义)Koopmans定理绘制光电子能谱(PES)谱与绘制TDOS密切相关。由于PES是经常研究的一种谱，在DOS模块中提供了专门的界面，用于方便地生成理论模拟的PES谱。

<!-- p.161 -->


理论 (Theory) PES谱中峰的位置反映了各种N-1态与原始N电子态之间的能量差。如果体系为中性，体系通常处于中性电子态的振动基态。电离出一个电子后，体系可处于阳离子态的不同振动状态。因此，PES具有精细结构，反映了振动耦合效应。然而，为简化问题，我们常常忽略核运动的量子效应，并假设电离是从初态势能面极小点出发的垂直过程。此时，PES中的峰位等价于当前体系不同壳层电子的垂直电离能(VIP)。显然，只要优化体系并计算VIP，就可模拟PES。

第1 VIP对应于电离掉最外层电子所需的能量，通常计算为在N电子态势能面极小点几何下含N个电子体系的E(N-1) - E(N)；其中E表示电子能量。内层电子对应的VIP也可以理论计算，但需要特殊方法，如OVGF、IP-EOM-CC、ADC等。

绘制PES最简单的方法基于Koopmans定理，该定理指出电子的电离能等于相应壳层轨道能量的负值。注意这只是一种近似关系，它完全忽略了电子相关和轨道弛豫效应。在Koopmans定理下，模拟的PES简单对应于由所有占据MO展宽得到的TDOS曲线，只是在展宽前应将轨道能量反号(对应于“电子结合能”)。

由于Koopmans定理对大多数常用DFT泛函(除QTP17等特殊泛函外)效果不好，MO能量的负值与实际VIP明显偏离，导致与实验谱相比效果较差。幸运的是，有所谓的广义Koopmans定理，若将其应用于PES的理论模拟，其实质相当于在绘制PES前对所有电子结合能加上一个位移值，该位移值定义为1st VIP + E(HOMO)。计入该位移后，模拟PES的第一个峰将恰好对应于第1 VIP，只要DFT泛函和基组选择得当、几何已充分优化，且计算的电子态对应于实际基态，它与实验PES的第一个峰就不会明显偏离。

用法 (Usage) PES绘制界面作为选项12嵌入在DOS模块中，允许用户极其方便地基于(广义)Koopmans定理绘制PES谱。任何用于绘制DOS的输入文件也可用于PES绘制。

如果你想基于Koopmans定理绘制PES，进入PES绘制界面后只需选择选项1。如果你想采用广义Koopmans定理，应先选择选项3设置位移值再绘图。

PES绘制界面中有许多与DOS绘制界面类似的参数和选项，如X和Y轴的范围与步长、FWHM、是否显示分立线等，但多数参数在两个界面间并不共用。注意，PES绘制只能使用eV单位和Gaussian展宽函数。如果当前波函数为非限制开壳层，不区分轨道自旋类型。

<!-- p.162 -->


如果你想调整PES曲线与各结合能级对应分立线之间的相对高度，可以使用“11 Set scale ratio for PES curve(设置PES曲线的缩放比例)”设置缩放比例。比例越小，曲线越低。

若选择选项1绘制PES谱后没有任何显示，你应：

- 选择选项“-2 Show all binding energy level information(显示所有结合能级信息)”然后检查结合能的数值是否正确。

- 检查X轴范围是否设置得当。要绘制PES，当前X轴范围内必须至少有一个结合能。默认情况下，所有轨道具有相同的强度(1.0)和FWHM(0.2 eV)，后者可在PES界面中通过选项6直接设置。如果你想调整个别轨道的强度和FWHM，可以选择“-3 Export occupied MO energies, strengths and FWHMs to plain text file(将占据MO能量、强度和半峰宽导出为纯文本文件)”，则符合3.12.2节所述格式的文件PESinfo.txt将被导出到当前文件夹。然后你可以在该文件中手动调整某些轨道的强度和FWHM，再将此文件用作输入文件绘制PES，从而使模拟的PES更接近实验谱。

PES曲线的绝对值没有实际意义。因此，在恰当设置Y轴范围后，可选择“13 Toggle showing labels and ticks on Y-axis(切换是否显示Y轴标签和刻度)”将其状态切换为“No”。

绘制PES的示例见4.10.4节。所需信息：对于PDOS、OPDOS和局域DOS，见3.12.2节。对于TDOS和PES谱，使用.mwfn/.fch/.molden/.gms文件，或带pop=full的Gaussian输出文件，或符合3.12.2节所述格式的纯文本文件。

### 3.12.6 COHP

理论 (Theory) 在第一性原理研究领域，OPDOS常被称为晶体轨道重叠布居(crystal orbital overlap population, COOP)，而与其密切相关的一个概念称为晶体轨道Hamilton布居(crystal overlap Hamilton populations, COHP)。COHP最初提出于J. Phys. Chem., 97, 8617 (1993)，在理解固体成键和材料设计中有广泛应用，综述见J. Phys. Chem. A, 115, 5461 (2011)和Angew. Chem. Int. Ed., 39, 1560 (2000)。

对于以原子中心基函数表示的波函数，如Gaussian和CP2K产生的波函数，COHP可简单视为将COOP中的重叠矩阵替换为Kohn-Sham矩阵，因此COHP从能量角度与原子或碎片间的相互作用相关。每个MO对所关注的相互作用都有其COOP和COHP值，正的COOP和负的COHP均表明该MO被占据时对原子间或碎片间成键有正贡献(即成键态)，且COOP越正、COHP越负，贡献越大。相反，反键态的MO具有负的COOP和正的COHP。COHP由于考虑了能量因素，可能比COOP与原子间/碎片间成键强度的相关性更好。然而，我发现COHP曲线对所用基组有些敏感。因此，在比较不同情形的COHP时，应使用完全相同的基组。
