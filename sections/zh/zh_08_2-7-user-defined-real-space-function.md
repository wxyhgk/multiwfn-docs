# 用户自定义实空间函数（User-defined real space function）

> Multiwfn manual, p.54–69.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.54 -->


24 相互作用区域指示器（IRI）（Interaction region indicator (IRI)）IRI由我在Chemistry—Methods, 1, 231 (2021)中提出，对揭示化学体系各类相互作用区域极其有用。详见3.23.8节。IRI定义为


$$IRI(\mathbf{r})=\frac{|\nabla\rho(\mathbf{r})|}{\left[\rho(\mathbf{r})\right]^{a}}$$

<!-- formula-ocr: formula_p54_032.png 已替换为LaTeX, 原图保留备查 -->

其中a对应`settings.ini`中的“uservar”。设为0时采用推荐值1.1。IRI的详细介绍见3.23.8节。注意若ρ等于或小于`settings.ini`中的“IRI_rhocut”，IRI被设为任意大值（5.0），从而不会在不感兴趣的极低ρ区域出现IRI等值面。若“IRI_rhocut”设为0则不做此处理。对IRI或IRI-π做盆分析和拓扑分析时，应设为0以避免此处理带来的人为极值点（Multiwfn会自动处理）。

25 范德华势（van der Waals potential）范德华（vdW）势对研究vdW效应主导的分子间相互作用非常重要，其作用堪比静电势对静电主导的分子间相互作用的作用。见3.23.7节对此函数的介绍。该函数单位为kcal/mol，探针原子可用`settings.ini`中的“ivdwprobe”设置。


## 2.7 用户自定义实空间函数（User-defined real space function）

在实空间函数选择菜单中，可找到一项“用户自定义实空间函数（User-defined real space function）”。为避免实空间函数列表过长，许多不常用的实空间函数未显式列出。但若想使用它们，可在运行前将`settings.ini`中的“iuserfunc”参数设为下面序号之一，用户自定义函数即对应相应函数。例如，运行Multiwfn前若将“iuserfunc”设为2，用户自定义实空间函数即等同于beta电子密度。设置用户自定义函数的另一种方式是在主菜单（main menu）中输入iu，可输入用户自定义函数的序号。

实际上，用户自定义函数对应源文件function.f90中的“userfunc”函数。自行填入适当代码即可容易扩展Multiwfn支持的函数。例如，在function.f90中“function userfunc”的适当位置填入代码“userfunc=fgrad(x,y,z,'t')**2/8/fdens(x,y,z)”并重新编译Multiwfn，Weizsäcker动能

泛函的被积函数，即2W[ ]( ) /[8 ( )]dτρρρ=rrr，即可使用。写自己的代码时可参考已有代码，内置函数列表见本手册附录2。

预置的用户自定义函数


<!-- p.55 -->


-2 基于内置球化原子密度计算的promolecular密度。原子密度如何产生见附录3。主功能（main function）6的选项（options）-3和-4可用于排除某些原子对promolecular密度的贡献。

请注意，此promolecular密度与实空间函数14和16用的promolecular密度不同，因为后者H至Ar的原子密度直接取自NCI方法原始论文，而非按附录3所述方法计算。

-1 由格点数据三线性插值得到的值。格点数据可由主功能（main function）5产生，或Multiwfn启动时从.cub/.grd/.vti文件载入。该函数很有用。例如，利用该函数可经主功能（main function）3和4分别将格点数据绘制为曲线图和平面图；也可经模糊原子空间分析模块（主功能（main function）15）的子功能（subfunction）1得到对总值的原子贡献。-3 与-1相同，但用3D三次B样条插值代替。代价高于三线性插值，但更光滑，格点间距较大时通常更准确。

但三次B样条插值的函数在实际函数变化不能被多项式很好近似处会表现出不希望的特征，此时结果甚至比三线性插值更差。例如，核处电子密度的cusp特征不能被忠实表示。此外，当实际函数在小斜率区域附近呈陡斜率，或格点不足以表示实际函数时，该函数呈波动特征。

关于用户自定义函数-1和-3的周期性考虑：注意若格点数据表示整个晶胞中的实空间函数，且想在插值中考虑周期边界条件，应在计算前选主功能（main function）1000（隐藏功能）中的选项（option）18将格点数据的盒子信息设为晶胞信息。或者，在待载入.cub文件的第一行加入字符串box2cell，告知Multiwfn自动处理。

不考虑周期性时，待计算位置应完全在格点数据的空间范围内，否则无法插值，返回的函数值简单为零。

0 该函数对应常数值1.0

1 Alpha密度： $\rho^{\alpha}(\mathbf{r}) = [\rho(\mathbf{r}) + \rho^{s}(\mathbf{r})] / 2$

2 Beta密度： $\rho^{\beta}(\mathbf{r}) = [\rho(\mathbf{r}) - \rho^{s}(\mathbf{r})] / 2$

3 电子空间范围<r2>的被积函数： $<r^2>$ $(x^2 + y^2 + z^2)\rho(\mathbf{r})$

4 Weizsäcker势（闭壳层形式）： $V_{\mathrm{w}}(\mathbf{r}) = \frac{1}{8} \frac{\left|\nabla \rho (\mathbf{r})\right|^2}{\rho^2 (\mathbf{r})} - \frac{1}{4} \frac{\nabla^2 \rho (\mathbf{r})}{\rho (\mathbf{r})}$

5 Weizsäcker泛函的被积函数（闭壳层形式）： $\tau_{\mathrm{w}}(\mathbf{r})=\left|\nabla\rho(\mathbf{r})\right|^{2}/[8\rho(\mathbf{r})]$

6 电子密度的径向分布函数： $4\pi \times \rho(\mathbf{r}) \times (x^2 + y^2 + z^2)$

假设电子密度球对称。

7 局域温度，以Hartree/kB为单位（PNAS, 81, 8028）： $T(\mathbf{r})=[2G(\mathbf{r})]/[3\rho(\mathbf{r})]$

`settings.ini`中的“uservar”参数，则T视为0。

8 平均局域静电势（J. Chem. Phys., 72, 3027 (1980)）： $V_{\mathrm{ESP}}(\mathbf{r}) / \rho(\mathbf{r})$

9 形状函数： $\rho(\mathbf{r})/N$


<!-- p.56 -->


10 势能密度（Virial场）： $V(\mathbf{r}) = -K(\mathbf{r}) - G(\mathbf{r}) = (1/4)\nabla^2 \rho(\mathbf{r}) - 2G(\mathbf{r})$

11 电子能量密度： $E(\mathbf{r}) = G(\mathbf{r}) + V(\mathbf{r}) = -K(\mathbf{r})$ $E(\mathbf{r})$ $E_{\mathrm{scl}}(\mathbf{r}) = -K(\mathbf{r}) \times (R - 1)$ $E_{scl}(\mathbf{r})$

-11 标度电子能量密度：scl( )( ) (1)EKR= −×−rr，其中R为从输入文件载入的virial比（注意并非所有输入文件都含此信息！fch/mwfn/wfx/wfn格式有特定字段记录它）。Escl(r)在全空间积与量子化学程序打印的电子能量精确相同。4.17.9节阐明了此函数的用处。

12 局域核吸引势能： $-\rho(\mathbf{r}) \times V_{\mathrm{nuc}}(\mathbf{r})$

13 每个电子的动能密度： $G(\mathbf{r}) / \rho(\mathbf{r})$

14 来自电子的静电势： $V_{\mathrm{ele}}(\mathbf{r}) = V_{\mathrm{ESP}}(\mathbf{r}) - V_{\mathrm{nuc}}(\mathbf{r}) = -\int \frac{\rho(\mathbf{r}^{\prime})}{|\mathbf{r} - \mathbf{r}^{\prime}|} \, \mathrm{d}\mathbf{r}^{\prime}$

此函数的负值亦称Hartree势，表示r处电子受所有电子的经典Coulomb势。

15 键金属性： $\xi_J(\mathbf{r}) = \rho(\mathbf{r}) / \nabla^2 \rho(\mathbf{r})$ $\xi_J > 1$

相互作用，见J. Phys.: Condens. Matter, 14, 10251 (2002)。

16 无量纲键金属性： $\xi_{\mathrm{m}}(\mathbf{r})=\frac{36(3\pi)^{-2}}{5}\frac{\rho(\mathbf{r})}{\nabla^{2}\rho(\mathbf{r})}$

值对应键的金属性越强，见Chem. Phys. Lett., 471, 174 (2009)。

17 每个电子的能量密度： $E(\mathbf{r})/\rho(\mathbf{r})$ $E_{\mathrm{BCP}}<0$ $E_{\mathrm{BCP}}>0$

图案与ELF很相似，值域为[-1,1]：$$\nu_{\pm} = \frac{D_{0}(\mathbf{r})-G(\mathbf{r})}{D_{0}(\mathbf{r})+G(\mathbf{r})}$$

19 单指数衰减探测器（SEDD），与ELF高度类似。在J. Chem. Theory Comput., 10, 3745 (2014)中更新的定义已实现：


$$\mathrm{SEDD}(\mathbf{r})=\ln\left\{1+\frac{\left[\nabla\left(\nabla\rho(\mathbf{r})/\rho(\mathbf{r})\right)^{2}\right]^{2}}{\rho(\mathbf{r})}\right\}$$

<!-- formula-ocr: formula_p56_033.png 已替换为LaTeX, 原图保留备查 -->

20 密度重叠区域指示器（DORI），定义于J. Chem. Theory Comput., 10, 3745 (2014)： $\theta(r) / [1 + \theta(r)]$ $\theta(r) = [\nabla(\nabla\rho(r) / \rho(r))^2]^2 / [\nabla\rho(r) / \rho(r)]^6$


<!-- p.57 -->


$$E_{\mathrm{att}}(\mathbf{r}) = \frac{n \sum_{i=LUMO}^{E_i < 0} |\varphi_i(\mathbf{r})|^2 \varepsilon_i}{\rho(\mathbf{r})}$$

主要用于揭示原子间相互作用区域，更多信息见3.23.3节。IRI效果远好于DORI。

21 电偶极矩X分量的被积函数： $-x\times\rho(\mathbf{r})$

$$\begin{array}{r l r l}{{3}960\mathrm{(2012))}\mathrm{:}}&{\chi(\mathbf{r}_{1},\mathbf{r}_{2})\approx4\displaystyle\sum_{i\in\mathrm{o c c}}\displaystyle\sum_{j\in\mathrm{v i r}}\frac{\varphi_{i}^{*}(\mathbf{r}_{1})\varphi_{j}(\mathbf{r}_{1})\varphi_{j}^{*}(\mathbf{r}_{2})\varphi_{i}(\mathbf{r}_{2})}{\varepsilon_{i}-\varepsilon_{j}}}\end{array}$$

25 电子动量涨落幅值： $\tilde{P}(\mathbf{r}) = |\nabla\rho(\mathbf{r})| / [2\rho(\mathbf{r})]$

定域电子探测器（LED），有助于讨论成键，与约化密度梯度很相似，见Theor. Chem. Acc., 127, 393 (2010)

26 Thomas-Fermi动能泛函的被积函数（闭壳层形式）： $\tau_{\mathrm{TF}}(\mathbf{r}) = C_{\mathrm{TF}}\rho(\mathbf{r})^{5/3}$ $C_{\mathrm{TF}}=(3/10)(3\pi^{2})^{2/3}=2.871234$

27 局域电子亲和（LEA）： $EA_{\mathrm{L}}(\mathbf{r}) = \frac{-\sum_{i \in \mathrm{vir}} |\varphi_i(\mathbf{r})|^2 \varepsilon_i}{\sum_{i \in \mathrm{vir}} |\varphi_i(\mathbf{r})|^2}$ $E_{\mathrm{att}}(\mathbf{r}) = \frac{n \sum_{i=LUMO}^{E_i < 0} |\varphi_i(\mathbf{r})|^2 \varepsilon_i}{\rho(\mathbf{r})}$

i  vir

局域电离能，但i遍历所有未占据轨道。见J. Mol. Model., 9, 342 (2003)。对实际分子的应用示例见4.12.13节。

-27 局域电子附着能：iiinE LUMOatt ( )( )( ) ==rrr ε i  0 ρ φε 2。i遍历所有能量为负的未占据

轨道。对限制性和非限制性波函数，n分别等于2和1。见J. Phys. Chem. A., 120, 10023 (2016)。该函数与LEA用途相似但更稳健。对实际分子的应用示例见4.12.13节。

28 局域Mulliken电负性： $\chi_{\mathrm{L}}(\mathbf{r}) = [\bar{I}(\mathbf{r}) + EA_{\mathrm{L}}(\mathbf{r})] / 2$

(2003)

29 局域硬度： $\eta_{\mathrm{L}}(\mathbf{r})=[\overline{I}(\mathbf{r})-EA_{\mathrm{L}}(\mathbf{r})]/2$ $EA_{L}$ $E_{\mathrm{att}}$ $\chi_{L}$ $\eta_{L}$ $EA_{\mathrm{L}}$ $\chi_{\mathrm{L}}$ $\eta_{\mathrm{L}}$ $E_{\mathrm{att}}$ $E_{\mathrm{att}}$ $EA_{\mathrm{L}}$ $E_{\mathrm{att}}$ $E_{att}$

注：要使用EAL、Eatt、χL和ηL，输入文件必须同时含单行列式波函数的占据和未占据轨道（但不支持限制性开壳层），应以.mwfn、.fch、.molden和.gms作输入文件。

一般，EAL（从而χL和ηL）与含弥散函数的基组不兼容，而计算Eatt可用任何基组。与augmented（弥散）基组更好的兼容性是Eatt相对EAL的显著优点。但要使用Eatt，至少LUMO应


<!-- p.58 -->


有负能量，而常用水平下此条件常不满足。Eatt原始论文发现该函数在B3LYP/6-31+G(d,p)轨道下工作合理。

30 电子密度的椭率： $\varepsilon(\mathbf{r})=[\lambda_{1}(\mathbf{r})/\lambda_{2}(\mathbf{r})]-1$

ρ的Hessian矩阵的第二低本征值。在键临界点（BCP），λ1和λ2均为负，体现垂直于键的两正交方向电子密度的曲率。BCP处的ε常视为键周围电子密度非轴对称分布的指标，偏离轴对称分布越大，

BCP处ε值越大。

31 eta指数： $\eta(\mathbf{r}) = |\lambda_1(\mathbf{r})| / \lambda_3(\mathbf{r})$ $\lambda_1$ $\lambda_3$

32 Tian Lu改进的eta指数： $\eta'(\mathbf{r}) = |\lambda_1(\mathbf{r})| / \lambda_3(\mathbf{r}) - 1$

η'对应闭壳层相互作用。33 分子中作用于一个电子的势（PAEM），见J. Comput. Chem., 35, 965 (2014)：

$$V_{\mathrm{P A E M}}(\mathbf{r})=-V_{\mathrm{E S P}}(\mathbf{r})+V_{\mathrm{X C}}(\mathbf{r})=-V_{\mathrm{E S P}}(\mathbf{r})+\frac{1}{\rho(\mathbf{r})}\int\frac{\Gamma_{\mathrm{X C}}^{\alpha,\mathrm{tot}}(\mathbf{r},\mathbf{r}^{\prime})+\Gamma_{\mathrm{X C}}^{\beta,\mathrm{tot}}(\mathbf{r},\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime},\mathrm{w h e r e}V_{\mathrm{E S P}}(\mathbf{r}^{\prime})=\Gamma_{\mathrm{X C}}(\mathbf{r}^{\prime})+\Gamma_{\mathrm{X C}}(\mathbf{r}),$$

$$V_{\mathrm{P A E M}}(\mathbf{r})=-V_{\mathrm{E S P}}(\mathbf{r})+V_{\mathrm{X C}}(\mathbf{r})=-V_{\mathrm{E S P}}(\mathbf{r})+\frac{1}{\rho(\mathbf{r})}\int\frac{\Gamma_{\mathrm{X C}}^{\alpha,\mathrm{tot}}(\mathbf{r},\mathbf{r}^{\prime})+\Gamma_{\mathrm{X C}}^{\beta,\mathrm{tot}}(\mathbf{r},\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime},\mathrm{w h e r e}V_{\mathrm{E S P}}(\mathbf{r}^{\prime})=\Gamma_{\mathrm{X C}}(\mathbf{r}^{\prime})+\Gamma_{\mathrm{X C}}(\mathbf{r}),$$

为总分子静电势，VXC为交换相关势。在Multiwfn中，交换相关密度Γ按Müller近似计算，详见2.6节第17部分。原始论文表明PAEM可能有助于区分共价与非共价相互作用。PAEM的应用例子见4.3.3节。34 与33相同，但VXC直接对应DFT交换相关势。其具体形式可经“iDFTxcsel”参数选择，详见本节末。此形式的PAEM比33便宜得多，但仅支持闭壳层波函数。对非常大的体系，33的代价在计算上不可行，故34是唯一选择。35 |𝑉(𝐫)|/𝐺(𝐫)。J. Chem. Phys., 117, 5529 (2002)提出可用BCP处此量判别相互作用类型。<1对应闭壳层相互作用；>2对应共价相互作用；而>1且<2对应中间相互作用。

36 On-top对密度，即对密度的两位置相同： $\pi(\mathbf{r},\mathbf{r})$

$$V_{\mathrm{P A E M}}(\mathbf{r})=-V_{\mathrm{E S P}}(\mathbf{r})+V_{\mathrm{X C}}(\mathbf{r})=-V_{\mathrm{E S P}}(\mathbf{r})+\frac{1}{\rho(\mathbf{r})}\int\frac{\Gamma_{\mathrm{X C}}^{\alpha,\mathrm{tot}}(\mathbf{r},\mathbf{r}^{\prime})+\Gamma_{\mathrm{X C}}^{\beta,\mathrm{tot}}(\mathbf{r},\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime},\mathrm{w h e r e}V_{\mathrm{E S P}}(\mathbf{r}^{\prime})=\Gamma_{\mathrm{X C}}(\mathbf{r}^{\prime})+\Gamma_{\mathrm{X C}}(\mathbf{r}),$$


<!-- p.59 -->


τW(r)]/τTF。τS、τW和τTF的含义见介绍ELF的2.6节。易见SCI指数与ELF密切相关，可写作ELF(r) = 1/[1+ζ 2(r)]。38 电子密度Hessian的第二本征矢与给定平面法矢的夹角，可由主功能（main function）1000的选项（option）4定义平面；屏幕上会显示平面的单位法矢，假设你用三点A、B、C定义平面得到矢量u，但你真正想要的是-u，则可按相反顺序重新输入点，即C、B、A。J. Phys. Chem. A, 115, 12512 (2011)沿键路径用此量揭示π相互作用。39 不含特定核贡献的静电势：

$$V_{\mathrm{n}}(\mathbf{r}) = \sum_{A \neq K} \frac{Z_A}{|\mathbf{r} - \mathbf{R}_A|} - \int \frac{\rho(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|} \, \mathrm{d}\mathbf{r}'$$

1000（在主界面隐藏但可选）。Vn是很有用的量，例如若K选为氢的序号，则该值与其pKa相关，因为此时Vn近似反映K位置质子与体系其余部分的结合能；此外，J. Phys. Chem. A, 118, 1697 (2014)表明Vn可用于定量预测静电主导的弱相互作用（即氢键、卤键、二氢键）的相互作用能，介绍与例子见4.1.2节。

值得一提的是，在主功能（main function）1中，当要求Multiwfn打印某原子的核位置性质时，会自动打印不含该原子核电荷贡献的静电势。

40 空间位阻能密度： $\left|\nabla\rho(\mathbf{r})\right|^2 / [8\rho(\mathbf{r})]$

泛函。

41 空间位阻势： $\upsilon_{s}(\mathbf{r}) = \frac{1}{8} \frac{|\nabla \rho(\mathbf{r})|^2}{[\rho(\mathbf{r}) + \delta]^2} - \frac{1}{4} \frac{\nabla^2 \rho(\mathbf{r})}{\rho(\mathbf{r}) + \delta}$

亦称单电子势（OEP）。注意δ是为避免分母比分子更快趋于零而人为引入的很小项。δ的值可由`settings.ini`中的“steric_addminimal”决定。若δ设为0，则恢复空间位阻势的原始表达式。

42 空间位阻电荷： $q_{\mathrm{s}}(\mathbf{r}) = \nabla^{2} \upsilon_{\mathrm{s}}(\mathbf{r}) / (-4\pi)$

43 空间位阻力幅值： $F_{\mathrm{S}}(\mathbf{r}) = | - \nabla v_{\mathrm{S}}(\mathbf{r}) |$

注意，上述δ项也影响空间位阻力和空间位阻电荷。空间位阻能/势/力/电荷的讨论见J. Chem. Phys., 126, 244103 (2007)。44、45、46 阻尼空间位阻势、基于阻尼空间位阻势的空间位阻力、直接阻尼空间位阻力：私下记录 47 阻尼空间位阻电荷：私下记录

49 相对Shannon熵密度，亦称信息增益密度： $i_{G} = \rho(\mathbf{r})\ln\frac{\rho(\mathbf{r})}{\rho_{0}(\mathbf{r})}$

其中ρ0(r)为promolecular密度。对此函数做任何分析或可视化前，必须进入主功能（main function）1000（隐藏功能）再选子功能（subfunction）17以构建promolecular波函数并存入内存特定空间；此promolecular



<!-- p.60 -->


波函数通过为所有原子准备波函数文件（详见3.7.3节）再组合在一起产生。注意在子功能（subfunction）17中，当Multiwfn问“Do you want to make wavefunction information in memory correspond to the just generated promolecular wavefunction? (y/n)”时，应输入n以避免当前波函数被promolecular波函数替换。

50 Shannon熵密度： $s_{\mathrm{S}}(\mathbf{r}) = -\rho(\mathbf{r}) \ln \rho(\mathbf{r})$

51 Fisher信息密度： $i_{\mathrm{F}}(\mathbf{r}) = |\nabla\rho(\mathbf{r})|^2 / \rho(\mathbf{r})$ $i_{\mathrm{F}}^{\prime}(\mathbf{r}) = -\nabla^{2} \rho(\mathbf{r}) \ln \rho(\mathbf{r})$

52 第二Fisher信息密度：$i_{\mathrm{F}}^{\prime}(\mathbf{r}) = -\nabla^{2} \rho(\mathbf{r}) \ln \rho(\mathbf{r})$。

Shannon熵与Fisher信息见J. Chem. Phys., 126, 191107 (2007)。该函数在全空间积分与Fisher信息密度积分完全相同。53 Ghosh熵密度或Ghosh-Berkowitz-Parr (GBP)熵密度，以kB为单位（PNAS, 81, 8028

$$s(\mathbf{r}) = (3/2)\rho(\mathbf{r})\{\lambda + \ln[t(\mathbf{r})/t_{\mathrm{TF}}(\mathbf{r})]\}$$

Thomas-Fermi常数（3/10)(3π2)2/3=2.871234，动能密度项t(r)选用Lagrange动能密度G(r)。

54 与53相同，但t(r)采用G(r) − 2ρ(r)/8，即精确对应PNAS, 81, 8028 (1984)方程22的动能密度定义。极少数情况下此动能密度定义导致很小的负值，因此时tTF(r)也非常接近零，为能正常得到结果，此时ln[t(r)/tTF(r)]简单设为零。

55 Rényi熵二次方形式的积分部分的被积函数： $\rho^2(\mathbf{r})$

56 Rényi熵三次方形式的积分部分的被积函数： $\rho^3(\mathbf{r})$ $$\mathbf{57}\;g_{1}(\mathbf{r})=\nabla^{2}\rho(\mathbf{r})\ln\frac{\rho(\mathbf{r})}{\rho_{0}(\mathbf{r})}$$ $$g_{2}(\mathbf{r})=\rho(\mathbf{r})\left[\frac{\nabla^{2}\rho(\mathbf{r})}{\rho(\mathbf{r})}-\frac{\nabla^{2}\rho_{0}(\mathbf{r})}{\rho_{0}(\mathbf{r})}\right]$$ $$59~g_{3}(\mathbf{r})=\rho(\mathbf{r})\bigg[\nabla\ln\frac{\rho(\mathbf{r})}{\rho_{0}(\mathbf{r})}\bigg]^{2}$$

57 $$g_{1}(\mathbf{r})=\nabla^{2}\rho(\mathbf{r})\ln\frac{\rho(\mathbf{r})}{\rho_{0}(\mathbf{r})}$$

58 $$g_{2}(\mathbf{r})=\rho(\mathbf{r})\left[\frac{\nabla^{2}\rho(\mathbf{r})}{\rho(\mathbf{r})}-\frac{\nabla^{2}\rho_{0}(\mathbf{r})}{\rho_{0}(\mathbf{r})}\right]$$

59 $$g_{3}(\mathbf{r})=\rho(\mathbf{r})\bigg[\nabla\ln\frac{\rho(\mathbf{r})}{\rho_{0}(\mathbf{r})}\bigg]^{2}$$

注意用户自定义函数57、58、59只能在主功能（main functions）3、4、5中绘制为图作研究，同时deformation（变形）与promolecular图不可用。

60 Pauli势： $V_{\theta}$

- ispecial=0：按Comput. Theor. Chem., 1006, 92 (2013)方程17，Vθ = μ + VESP − VXC − VW，其中μ为化学势（Multiwfn假设为零），VESP为静电势

<!-- p.61 -->


（如2.6节所述），VXC为交换相关势（其形式由`settings.ini`中的“iDFTxcsel”决定，见后）。

- ispecial=1：用原始定义，即𝑉θ = 𝑉S −𝑉W = 𝛿𝜏S[𝜌]/𝛿𝜌−𝛿𝜏W[𝜌]/𝛿𝜌，其中VS为非相互作用动能泛函（τS）的势，VW为Weizsäcker动能泛函（τW）的势。τS的形式可由settings.ini中的“iKEDsel”选择，见后；目前仅支持iKEDsel为3、5、7。

由于Pauli力与电荷基于Pauli势由有限差分计算，而量子势/力/电荷基于Pauli势/力/电荷定义，用户自定义函数61~65也受“ispecial”影响。

61 Pauli力幅值：θθ( ) |( ) |FV= −rr

62 Pauli电荷：$$q_\theta(\mathbf{r}) = \nabla^2 V_\theta(\mathbf{r}) / (-4\pi)$$

63 量子势：qθXCVVV=+. 当ispecial=0时，显然在Multiwfn中它简单对应

VESP − VW

64 量子力幅值：|)(|)(qqrrVF−=


$$\upsilon_{\mathrm{e}}(\mathbf{r})=\rho(\mathbf{r})\left[\int\frac{\rho(\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime}-\sum_{A}\frac{Z_{A}}{|\mathbf{r}-\mathbf{R}_{A}|}\right]=-V_{\mathrm{ESP}}(\mathbf{r})\rho(\mathbf{r})\mathrm{d}\mathbf{r}^{\prime}\mathrm{d}\mathbf{r}\mathrm{d}\mathbf{r}^{\prime}\mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p61_034.png 已替换为LaTeX, 原图保留备查 -->

66 静电力幅值：ESPESP( ) |[( )]|FV= −−rr。如Phys. Chem.

Chem. Phys., 19, 1496 (2017)所讨论，空间位阻力、量子力与静电力（分别为用户自定义函数43、64和66）之间有非常密切的关系。

67 静电电荷：2ESPESP( )[( )] / ( 4 )qVπ= −−rr

68 Shubin Liu能量分解中静电项的电子部分的能量密度：

$$\upsilon_{\mathrm{e}}(\mathbf{r})=\rho(\mathbf{r})\left[\int\frac{\rho(\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime}-\sum_{A}\frac{Z_{A}}{|\mathbf{r}-\mathbf{R}_{A}|}\right]=-V_{\mathrm{ESP}}(\mathbf{r})\rho(\mathbf{r})\mathrm{d}\mathbf{r}^{\prime}\mathrm{d}\mathbf{r}\mathrm{d}\mathbf{r}^{\prime}\mathrm{d}\mathbf{r}$$

Liu能量分解见3.24.2节。

69、-69 Shubin Liu能量分解中量子部分的能量密度：τs(r) − τW(r) + εXC(r)，其中τs为Hamilton动能密度（若userfunc = 69）或Lagrange动能密度（若userfunc = -69）。τW为Weizsäcker泛函的被积函数（与userfunc=5相同），εXC为交换相关能密度（与userfunc=1000相同），其形式可由`settings.ini`中的“iDFTxcsel”参数选择，详见后。


**r** 70 相空间定义的Fisher信息密度（PS-FID）：)( rrrrGTkiρρ== , Bfr )(3)( )(29)( 2

其中T(r)为上示局域温度。该函数与ELF和LOL特征很相似，可清楚揭示电子对的空间定域。介绍与示例应用见Chem. Phys., 435, 49 (2014)。


<!-- p.62 -->


71、72、73、74 3D表示的电子线动量密度（EMD）。电子线动量算子为−i，对轨道X方向线动量的期望值为

$$m_{\mathrm{tot}}(\mathbf{r}) = \sqrt{m_x^2(\mathbf{r}) + m_y^2(\mathbf{r}) + m_z^2(\mathbf{r})}$$

$$m_{\mathrm{tot}}(\mathbf{r}) = \sqrt{m_x^2(\mathbf{r}) + m_y^2(\mathbf{r}) + m_z^2(\mathbf{r})}$$

定义函数分别对应X、Y、Z分量。EMD的幅值（74）为


$$m_{\mathrm{tot}}(\mathbf{r}) = \sqrt{m_x^2(\mathbf{r}) + m_y^2(\mathbf{r}) + m_z^2(\mathbf{r})}$$

<!-- formula-ocr: formula_p62_035.png 已替换为LaTeX, 原图保留备查 -->

75、76、77、78 磁偶极矩密度（MDMD）。磁偶极矩算子即角动量算子（见Theor. Chim. Acta, 6, 341 (1966)）


$$m_{x}(\mathbf{r})=-\sum_{i}\eta_{i}\varphi_{i}^{*}(\mathbf{r})\Bigg[y\frac{\partial\varphi_{i}(\mathbf{r})}{\partial z}-z\frac{\partial\varphi_{i}(\mathbf{r})}{\partial y}\Bigg]$$

<!-- formula-ocr: formula_p62_036.png 已替换为LaTeX, 原图保留备查 -->

其中i、j、k分别为X、Y、Z方向单位矢。因此，MDMD的X、Y、Z分量可定义如下（忽略虚数符号）


$$m_{y}(\mathbf{r})=-\sum_{i}\eta_{i}\varphi_{i}^{*}(\mathbf{r})\Bigg[z\frac{\partial\varphi_{i}(\mathbf{r})}{\partial x}-x\frac{\partial\varphi_{i}(\mathbf{r})}{\partial z}\Bigg]$$

<!-- formula-ocr: formula_p62_037.png 已替换为LaTeX, 原图保留备查 -->

第75、76、77个用户自定义函数分别对应X、Y、Z分量。第78个

用户自定义函数为MDMD的幅值：)()()()(222totrrrrzyxmmmm++=。

79 电子能量密度的梯度模：|E(r)| 80 电子能量密度的Laplacian：2E(r) 81、82、83 分别为Hamilton动能密度的X、Y、Z分量。84、85、86 分别为Lagrange动能密度的X、Y、Z分量。

87、88、89 分别为局域总、动态、非动态电子相关函数。这些函数的介绍与计算例子见4.A.7.2节。90 Grimme在Angew. Chem. Int. Ed., 54, 1 (2015)中提出的部分占据数加权电子密度（FOD）。FOD的介绍与计算例子见4.A.7.1节。

91 基于Hirshfeld划分的独立梯度模型（IGMH）方法定义的两 fragment（片段）间的δginter，详见3.23.5节和3.23.6节。要用此函数，应先进入主功能（main function）1000选选项（option）16定义两片段。


<!-- p.63 -->


92、93、94 基于UFF力场参数的范德华势、排斥势和色散势，详细介绍见3.23.7节。单位为kcal/mol，探针原子可用`settings.ini`中的“ivdwprobe”设置。注意92与2.6节所述第25个函数相同。

95、96、97、98 分别为轨道加权的f +、f −、f 0 Fukui函数以及轨道加权的dual descriptor（对描述符）。它们最初提出于J. Comput. Chem., 38, 481 (2017)和J. Phys. Chem. A, 123, 10556 (2019)。对前线分子轨道（准）简并体系研究局域反应性有用，简要介绍见3.25.3节，示例见

4.22.2节。这些函数中的Δ参数可用主功能（main function）1000（隐藏选项）的选项（option）6设置。由于这些函数涉及虚轨道，应以mwfn/fch/molden/gms作输入文件。仅支持闭壳层单行列式波函数。99 相互作用区域指示器（IRI）：与2.6节所述函数24相同。100 Disequilibrium（亦称semi-similarity）：𝐷r(𝐫) = 𝜌2(𝐫)。示例应用见Int. J. Quantum Chem., 113, 2589 (2013)。101 ESP正部：𝑉ESP += 𝑉ESP；在ESP为负处，𝑉ESP += 0。102 ESP负部：𝑉ESP +。103 电场幅值|F|。由于电场矢量即ESP的负梯度矢量，因此该量对应ESP梯度的模。−，定义类似𝑉ESP +。在VESP为正的区域，𝑉ESP

110 Shubin Liu能量分解分析中定义的空间位阻、静电和量子分量的总能量密度（介绍见3.24.2节），对应用户自定义函数40、68和69之和 111 空间位阻势、静电势与量子势之和。注意`settings.ini`中的“ispecial”、“iDFTxcsel”和“iKEDsel”影响本函数和下两函数，详见用户自定义函数60的说明。112 空间位阻力、静电力与量子力的矢量和的幅值。113 空间位阻电荷、静电电荷与量子电荷之和。

114 Pauli动能密度：𝜏θ(𝐫) = 𝜏S(𝐫) −𝜏W(𝐫)，其中τS(r)为可由`settings.ini`中的“iKEDsel”选择的动能密度（见后），τW(r)为Weizsäcker动能密度。

115 Stiffness 𝑆= |𝜆1|/|𝜆3|，其中λ1 < λ2 < λ3为电子密度Hessian矩阵的三本征值。见J. Comput. Chem., 37, 2722 (2016)。

116、117、118：应力张量stiffness 𝑆𝜎= |𝜆1𝜎|/|𝜆3𝜎|、应力张量极化率𝑃= |𝜆3𝜎|/|𝜆1𝜎|、

$$\epsilon_{\sigma H} = |\lambda_{1\sigma}| / |\lambda_{2\sigma}| - 1$$

对感兴趣的用户，这里简述应力张量σ。它由Bader在J. Chem. Phys., 73, 2871 (1980)中定义如下（此处以a.u.表示）


$$\mathbf{\sigma}(\mathbf{r})=-\frac{1}{4}\Big[\big(\nabla\nabla^{\prime}+\nabla^{\prime}\nabla-\nabla\nabla-\nabla^{\prime}\nabla^{\prime}\big)\Gamma^{(1)}(\mathbf{r},\mathbf{r}^{\prime})\Big]_{\mathbf{r}=\mathbf{r}^{\prime}}$$

<!-- formula-ocr: formula_p63_038.png 已替换为LaTeX, 原图保留备查 -->


<!-- p.64 -->


显式，其元素可写作


$$\sigma_{i,j}(\mathbf{r})=-\frac{1}{4}\Biggl[\Biggl(\frac{\partial^{2}}{\partial r_{i}^{\phantom{*}}\partial r_{j}^{\prime}}+\frac{\partial^{2}}{\partial r_{i}^{\phantom{*}}\partial r_{j}^{\phantom{*}}}-\frac{\partial^{2}}{\partial r_{i}^{\phantom{*}}\partial r_{j}^{\phantom{*}}}-\frac{\partial^{2}}{\partial r_{i}^{\phantom{*}}\partial r_{j}^{\prime}}\Biggr)\Gamma^{(1)}(\mathbf{r},\mathbf{r}^{\prime})\Biggr]_{\mathbf{r}=\mathbf{r}^{\prime}}$$

<!-- formula-ocr: formula_p64_039.png 已替换为LaTeX, 原图保留备查 -->

其中r1=x、r2=y、r3=z，实空间形式的单电子约化密度矩阵可

基于轨道计算为Γ(1)(𝐫,𝐫′) = ∑𝜂𝑖𝜑𝑖 ∗(𝐫)𝜑𝑖(𝐫′)𝑖。目前只考虑实波函数，故Multiwfn中应力张量元素易计算为

$$\sigma_{i,j}(\mathbf{r})=-\frac{1}{4}\sum_{t}\eta_{t}\left[2\frac{\partial\varphi_{t}(\mathbf{r})}{\partial r_{i}}\frac{\partial\varphi_{t}(\mathbf{r})}{\partial r_{j}}-2\frac{\partial^{2}\varphi_{t}(\mathbf{r})}{\partial r_{i}\partial r_{j}}\varphi_{t}(\mathbf{r})\right]$$

若需得到整个应力张量，可在主功能（main function）1中输入坐标，应力张量将与其它量一起输出。
与应力张量密切相关的path-packets分析，可用Asdrubal Lozada基于patch版Multiwfn代码贡献的shell脚本实现，相关信息见http://sobereva.com/wfnbbs/viewtopic.php?pid=4698，地址为https://github.com/aslozada/Stress_tensor。200 [0,1)随机数。

819 超强相互作用（USI）：USI(𝐫) = ∇2𝜌(𝐫)/𝜌5/3(𝐫)。详见J. Phys. Chem. A, 126, 2437 (2022)。820 成键与非共价相互作用（BNI）：BNI(𝐫) = [𝐺(𝐫) −𝜏W(𝐫)]/𝜏W(𝐫)，其中G(r)为Lagrange动能密度。详见J. Phys. Chem. A, 126, 2437 (2022)。900、901、902 分别为X、Y和Z坐标变量。

函数910~914计算原子权重函数。计算的原子由`settings.ini`中的“uservar”决定。除Becke原子权重函数外均支持周期体系。910 Hirshfeld原子权重函数。911、912 分别为用Tian Lu共价半径和CSD共价半径的Becke原子权重函数。边界锐度参数为3 913 Tian Lu误差函数型原子权重函数 914 Tian Lu Gaussian函数型原子权重函数

999 局域Hartree-Fock交换能（或Hartree-Fock交换能密度）。其在全空间积对应Hartree-Fock交换能。

闭壳层情形：

bdbdbdeEEv= −rrrr HFX 1( )( )( )( )4

其中


<!-- p.65 -->


$$E_{b}(\mathbf{r})=\sum_{i}P_{i b}\chi_{i}(\mathbf{r})$$


$$E_{d}(\mathbf{r})=\sum_{i}P_{id}\chi_{i}(\mathbf{r})$$

<!-- formula-ocr: formula_p65_040.png 已替换为LaTeX, 原图保留备查 -->

其中χ为基函数，P为总密度矩阵。

开壳层情形：eHFX为其alpha与beta部分之和

$$e_{\mathrm{H F X}}^{\alpha}(\mathbf{r})=-\frac{1}{2}\sum_{b d}E_{b}^{\alpha}(\mathbf{r})E_{d}^{\alpha}(\mathbf{r})v_{b d}(\mathbf{r})$$

其中

$$E_{b}(\mathbf{r})=\sum_{i}P_{i b}\chi_{i}(\mathbf{r})$$

1000 DFT交换相关泛函的被积函数，亦称交换相关能密度。1100 DFT交换相关势，仅闭壳层体系可用：

$$V_{\mathrm{XC}}(\mathbf{r}) = \delta E_{\mathrm{XC}} / \delta\rho(\mathbf{r})$$

1101 α电子的DFT交换相关势，仅开壳层体系可用：

$$V_{\mathrm{XC}}(\mathbf{r}) = \delta E_{\mathrm{XC}} / \delta\rho(\mathbf{r})$$

1102 β电子的DFT交换相关势，仅开壳层体系可用：

$$V_{\mathrm{XC}}(\mathbf{r}) = \delta E_{\mathrm{XC}} / \delta\rho(\mathbf{r})$$

对用户自定义函数1000和1100/1101/1102，用`settings.ini`中的“iDFTxcsel”选XC泛函。0-29仅X部分，30-69仅C部分，70-99为整个XC。例如，若iDFTxcsel=32，则iuserfunc=1000对应LYP相关泛函的被积函数，iuserfunc=1100对应LYP势。

[详见下]


<!-- p.66 -->



**“iDFTxcsel”参数的可用选项（Available options of "iDFTxcsel" parameter）** 目前仅支持LSDA和部分GGA泛函




0 LSDA交换：$$-(3/2)\left[3/(4\pi)\right]^{1/3}[\rho_{\alpha}(\mathbf{r})^{4/3}+\rho_{\beta}(\mathbf{r})^{4/3}]$$。闭壳层情形的等价形式为$$-(3/4)(3/\pi)^{1/3}\rho(\mathbf{r})^{4/3}$$。

1 Becke 88 (B88)交换，见Phys. Rev. A, 38, 3098 (1988)。2 Perdew-Burke-Ernzerhof (PBE)交换，见Phys. Rev. Lett., 77, 3865 (1996)。3 Perdew-Wang 91 (PW91)交换，见Electronic Structure of Solids '91; Ziesche, P., Eschig, H., Eds.; Akademie Verlag: Berlin, 1991; p. 11。30 Vosko-Wilk-Nusair V (VWN5)相关，见Can. J. Phys., 58, 1200 (1980)。31 Perdew 86 (P86)相关，见Phys. Rev. B, 33, 8822 (1986)。32 Lee-Yang-Parr (LYP)相关，见Phys. Rev. B, 37, 785 (1988)。33 Perdew-Wang 91 (PW91)相关，见其交换对应文献。34 Perdew-Burke-Ernzerhof (PBE)相关，见其交换对应文献。70 Becke 97 (B97)交换相关，见J. Chem. Phys., 107, 8554 (1997)。71 Hamprecht-Cohen-Tozer-Handy with 407 training molecules (HCTH407)交换相关，见J. Chem. Phys., 114, 5497 (2001)。80 SVWN5交换相关。81 BP86交换相关。82 BLYP交换相关。83 BPW91交换相关。84 PBEPBE交换相关。85 PW91PW91交换相关。

关于iuserfunc=1200 动能密度（KED）表示动能泛函的被积函数。用户自定义函数1200是Multiwfn支持的所有KED的集合，已在J. Chem. Phys., 150, 204106 (2019)中系统考察。`settings.ini`中的“iKEDsel”用于选择KED的形式。

注意若“iKEDsel”不为默认值（0），则ELF与强共价相互作用指数（SCI）的τS项（Lagrange动能密度）将被相应KED替换。

主功能（main function）1000（在主菜单隐藏）中有子功能（subfunction）92，可计算所有KED在全空间积分，即基于动能泛函计算动能。仅当“iKEDsel”设为24时计算GEA4 KED，因其需电子密度的Laplacian，而其它KED只需电子密度及其梯度。Hamilton KED的积分不由此函数计算，因其结果与Lagrange KED相同。

- iKEDsel=1：Hamilton KED，与实空间函数6相同


<!-- p.67 -->


- iKEDsel=2：Lagrange KED，与实空间函数7相同

- iKEDsel=3：Thomas-Fermi KED：σσаβσαβττρ 5/3TFTFTF,,( )[( )]Cσ ====rr,

其中22/33TF10 (6)4.557799872Cπ==为自旋极化情形的Thomas-Fermi常数。

- iKEDsel=4：Weizsäcker KED： σρρτ W)(8 )()(rrr = βασσ = , 2

下面提到的大多数KED可用一般形式表示

$$\bullet\mathrm{iKEDsel}=10:\mathrm{Pearson}\mathrm{KED},\tau_{\mathrm{Pear}}^{\sigma}=\tau_{\mathrm{TF}}^{\sigma}+\frac{1}{1+[s_{r}^{\sigma}(\mathbf{r})/\zeta]^{6}}\frac{1}{72}\frac{\left|\nabla\rho^{\sigma}(\mathbf{r})\right|^{2}}{\rho^{\sigma}(\mathbf{r})},\mathrm{where}\zeta\mathrm{is}\mathrm{fixed}\mathrm{to}1,$$

因子，详见J. Chem. Phys., 127, 144109 (2007)。该论文系统介绍并比较了多种已有KED。注意该论文给出的许多表达式是错的，而下面给出的公式绝对正确，且都显式写为自旋极化形式，若在工作中涉及，请引用我的论文J. Chem. Phys., 150, 204106 (2019)；每种KED的引用也在该论文中给出。更多KED信息与比较见Phys. Rev. A, 46, 6920 (1992)和J. Chem. Phys., 100, 4446 (1994)。

- iKEDsel=5：二阶梯度展开近似， 11rσσsCF TF2GEA)(72 +=2 

- iKEDsel=6：Thomas-Fermi + 1/5 Weizsäcker KED， 11rσσsCF TFW5TF)(40 +=2 

- iKEDsel=7：Thomas-Fermi + Weizsäcker KED， 11rσσsCF TFTFvW)(8 +=2 

- iKEDsel=8：Thomas-Fermi + b/9 Weizsäcker KED， 067.11rσσsCF TFW9TF)(72 +=2 

- iKEDsel=9：N依赖的Thomas-Fermi KED，3/23/1NTF 187.0313.01NNF−+=−σ，其中N为

体系总电子数

- iKEDsel=10：Pearson KED，)( ζττ σσσ 6TFPearr ++= 1]/)([1 rs 1 rσ 72  ρ ρ σ )( r 2，其中ζ固定为1，

$$s_{r}^{\sigma}(\mathbf{r})=s^{\sigma}(\mathbf{r})/[2(6\pi^{2})^{1/3}],\mathrm{similarly}\mathrm{hereinafter}$$

- iKEDsel=11：DePristo-Kress Pade KED，1 xaxaxaxbFσ，其中1223343PadeDK+++ ++++=xbxbxb 19 12233

)72/()]([TF2Csxrσ=，a1 = 0.95，a2 = 14.28111，a3 = −19.57962，b1 = −0.05，b2 = 9.99802，

b3=2.96085


<!-- p.68 -->


- iKEDsel=12：Lee-Lee-Parr KED，0.0044188[( )]110.0253( )arcsinh[( )]sFss LLP σσ σσ= + + rrr 2

- iKEDsel=13：Ou-Yang–Levy 1 KED，11[( )]0.00187( )72FssC 2OL1 σσσ= ++rr TF

- iKEDsel=14：Ou-Yang–Levy 2 KED，)(21 sssCF+++= TF2OLrrrσ σσσ 113/52 )(0245.0)]([72

- iKEDsel=15：Thakkar KED，Thak5/30.0055[( )]0.072( )110.0253( )arcsinh[( )]12( )ssFsss σσσ σσσ= +−++rrrrr 2

- iKEDsel=16：Becke 86A KED，B86A2[( )]10.003910.004[( )]sFs σσ σ= ++ r 2 r

- iKEDsel=17：Becke 86B KED，B86B24/5[( )]10.00403{10.007[( )] }sFs σσ σ= ++ r 2 r

- iKEDsel=18：DePristo-Kress 87 KED，


$$\bullet\mathrm{i K E D s e l=12:L e e-L e e-P a r r~K E D},F_{\mathrm{L L P}}^{\sigma}=1+\frac{0.0044188[s^{\sigma}(\mathbf{r})]^{2}}{1+0.0253s^{\sigma}(\mathbf{r})\operatorname{a r c s i n h}[s^{\sigma}(\mathbf{r})]}$$

<!-- formula-ocr: formula_p68_042.png 已替换为LaTeX, 原图保留备查 -->

- iKEDsel=19：Perdew-Wang 86 KED，

$$F_{\mathrm{P W86}}^{\sigma}=\left\{1+1.296[s_{r}^{\sigma}(\mathbf{r})]^{2}+14[s_{r}^{\sigma}(\mathbf{r})]^{4}+0.2[s_{r}^{\sigma}(\mathbf{r})]^{6}\right\}^{1/15}$$

- iKEDsel=20：Perdew-Wang 91 KED，

$$F_{\mathrm{P W}91}^{\sigma}=\frac{1+a_{1}s_{r}^{\sigma}(\mathbf{r})\operatorname{a r c s i n h}[b\times s_{r}^{\sigma}(\mathbf{r})]+\{a_{2}-a_{3}e^{-100[s_{r}^{\sigma}(\mathbf{r})]^{2}}\}[s_{r}^{\sigma}(\mathbf{r})]^{2}}{1+a_{1}s_{r}^{\sigma}(\mathbf{r})\operatorname{a r c s i n h}[b\times s_{r}^{\sigma}(\mathbf{r})]+a_{4}[s_{r}^{\sigma}(\mathbf{r})]^{4}}\;,\;\mathrm{w h e r e}\quad a_{1}{=}0.19645,$$

a2=0.2743，a3=0.1508，a4=0.004，b=7.7956

- iKEDsel=21：Lacks-Gordon 94 KED

$$F_{\mathrm{LG}94}^{\sigma}=\frac{\left\{1+a_{2}[s_{r}^{\sigma}(\mathbf{r})]^{2}+a_{4}[s_{r}^{\sigma}(\mathbf{r})]^{4}+a_{6}[s_{r}^{\sigma}(\mathbf{r})]^{6}+a_{8}[s_{r}^{\sigma}(\mathbf{r})]^{8}+a_{10}[s_{r}^{\sigma}(\mathbf{r})]^{10}+a_{12}[s_{r}^{\sigma}(\mathbf{r})]^{12}\right\}^{b}}{1+10^{-8}[s_{r}^{\sigma}(\mathbf{r})]^{2}}$$

，其中a2=(10-8+0.1234)/0.024974，a4=29.790，a6=22.417，a8=12.119，a10=1570.1，a12=55.944，b=0.024974

- iKEDsel=22：Acharya-Bartolotti-Sears-Parr KED，11.412[( )]18FsCN 2ABSP1/3TF σσ=+ −r

- iKEDsel=23：Gázquez-Robles KED，+−−+=3/23/12 NNNsCFrσσ TFGR 029.0303.1121)]([8 1

- iKEDsel=24：四阶梯度展开近似，


<!-- p.69 -->


$$\tau_{\mathrm{GEA4}}^{\sigma}=\tau_{\mathrm{GEA2}}^{\sigma}+\frac{(6\pi^{2})^{-2/3}}{540}\left[\rho^{\sigma}(\mathbf{r})\right]^{1/3}\left\{\left[\frac{\nabla^{2}\rho^{\sigma}(\mathbf{r})}{\rho^{\sigma}(\mathbf{r})}\right]^{2}-\frac{9}{8}\frac{\nabla^{2}\rho^{\sigma}(\mathbf{r})}{\rho^{\sigma}(\mathbf{r})}\left|\frac{\nabla\rho^{\sigma}(\mathbf{r})}{\rho^{\sigma}(\mathbf{r})}\right|^{2}+\frac{1}{3}\left|\frac{\nabla\rho^{\sigma}(\mathbf{r})}{\rho^{\sigma}(\mathbf{r})}\right|^{4}\right\}$$

注意若`settings.ini`中的“uservar”不为零，上述所有KED都将加上“2ρ /uservar”项。例如，当iuserfunc=1200、iKEDsel=5且uservar=6时，用户自定义函数对应τGEA2+2ρ /6（即2.6节所示Tsirelson型ELF和LOL所用的KED）。

1201 “iKEDsel”选定的KED与Weizsäcker KED之差。1202 “iKEDsel”选定的KED与Lagrange KED之差。1203 “iKEDsel”选定的KED与Lagrange KED的绝对差。

1204 局域温度T(r)=[2τ(r)]/[3ρ(r)]。此函数用的动能密度τ(r)由“iKEDsel”决定。相比之下，用户自定义函数7用Lagrange动能

密度。注意若ρ小于`settings.ini`中的“uservar”参数，则T视为0。1210 动能泛函的势，其形式由`settings.ini`中的“iKEDsel”决定。仅闭壳层情形有效，仅对以下KED可用：iKEDsel=3：Thomas-Fermi；iKEDsel=5：二阶GEA；iKEDsel=7：Thomas-Fermi + Weizsäcker

主实空间函数作为用户自定义函数 为灵活性考虑，主实空间函数也可作为用户自定义函数调用。若将`settings.ini`中的“iuserfunc”设为10000+i，则第i个实空间函数被选为用户自定义函数。例如，若“iuserfunc”设为10009，则第9个实空间函数（ELF）被选为用户自定义函数。
