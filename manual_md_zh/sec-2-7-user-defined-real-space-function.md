# **2.7 自定义实空间函数**

在实空间函数选择菜单中，你会找到一项"自定义实空间函数 (User-defined real space function)"。为避免实空间函数列表过长，许多不常用的实空间函数没有明确列出。但若想用它们，可将 *settings.ini* 中的 "iuserfunc" 参数设为下述序号之一，自定义函数即被 pin 到相应函数。例如，运行 Multiwfn 前若将 "iuserfunc" 设为 2，则自定义实空间函数等价于 beta 电子密度。在主菜单输入 *iu* 是设置自定义函数的另一种方式，可输入自定义函数的序号。

实际上，自定义函数对应源文件 *function.f90* 中的 "userfunc" 函数。自己填入合适的代码即可轻松扩展 Multiwfn 支持的函数。例如，在 "function userfunc" 的合适位置填入代码 "userfunc=fgrad(x,y,z,'t')\*\*2/8/fdens(x,y,z)" 并重新编译 Multiwfn 后，Weizsäcker 动能泛函的被积函数，即 $\tau_\mathrm{W}[\rho]=\int\left|\nabla\rho(\mathbf{r})\right|^2/[8\rho(\mathbf{r})]\mathrm{d}\mathbf{r}$ ，即可用。自己写代码时可参考已有代码，内建函数列表见本手册[附录 2](sec-6-2-the-routines-for-evaluating-real-space-functions.md)。

## **预置的自定义函数**

**-2** 基于内建球化原子密度算得的 promolecular 密度。这些原子密度如何产生见[附录 3](sec-6-3-detail-of-built-in-atomic-densities.md)。主功能 6 的选项 -3 和 -4 可用于排除某些原子对 promolecular 密度的贡献。

> **注**
>
> 请注意该 promolecular 密度不同于实空间函数 14 和 16 用的 promolecular 密度，因为后者 H 到 Ar 的原子密度直接取自 NCI 方法原始论文，而非按[附录 3](sec-6-3-detail-of-built-in-atomic-densities.md)所述方法算得。

**-1** 由格点数据三线性插值求得的值。格点数据可由主功能 5 产生，或在 Multiwfn 启动时从 .cub/.grd/.vti 文件载入。该函数很有用。例如，利用它可分别经主功能 3 和 4 把格点数据绘制为曲线图和平面图；也可经 fuzzy 原子空间分析模块（主功能 15）的子功能 1 得到原子对总值的贡献。

**-3** 与 -1 相同，但用三维三次 B 样条插值代替。耗时高于三线性插值，但更光滑，特别在格点间距较大时通常更准确。

> **注**
>
> 但经三次 B 样条插值的函数在实际函数的变化不能被多项式很好近似处表现出不想要的特征，此时结果甚至比三线性插值更差。例如，核处电子密度的 cusp 特征不能被忠实表示。此外，当实际函数在小斜率区域附近呈陡斜率，或格点不足以表示实际函数时，该函数呈波动特征。

> **注**
>
> **关于自定义函数 -1 和 -3 的周期性考虑**：注意，若格点数据代表整个晶胞的实空间函数，且你想在插值时考虑周期性边界条件，应先选主功能 1000（隐藏功能）中的选项 18 把格点数据的盒子信息设为原胞信息再计算。或者，在要载入的 .cub 文件第一行加字符串 *box2cell* 以告知 Multiwfn 自动做此处理。
>
> 若不考虑周期性，被求值位置应完全在格点数据的空间范围内，否则无法插值，返回的函数值简单为 0。

**0** 该函数对应常量值 1.0

**1** Alpha 密度：$\rho^\alpha(\mathbf{r})=[\rho(\mathbf{r})+\rho^s(\mathbf{r})]/2$

**2** Beta 密度：$\rho^\beta(\mathbf{r})=[\rho(\mathbf{r})-\rho^s(\mathbf{r})]/2$

**3** 电子空间范围 $\langle r^{2}\rangle$ 的被积函数：$(x^2+y^2+z^2)\rho(\mathbf{r})$

**4** Weizsäcker 势（闭壳层形式）：$V_\mathrm{W}(\mathbf{r})=\frac{1}{8}\frac{\left|\nabla\rho(\mathbf{r})\right|^2}{\rho^2(\mathbf{r})}-\frac{1}{4}\frac{\nabla^2\rho(\mathbf{r})}{\rho(\mathbf{r})}$

**5** Weizsäcker 泛函的被积函数（闭壳层形式）：$\tau_\mathrm{W}(\mathbf{r})=\left|\nabla\rho(\mathbf{r})\right|^2/[8\rho(\mathbf{r})]$ ，它是任何单轨道体系（1 或 2 个电子，或任意数目的玻色子）的精确动能密度。若需自旋极化形式，用自定义函数 1200。

**6** 电子密度的径向分布函数：$4\pi\times\rho(\mathbf{r})\times(x^2+y^2+z^2)$ 。显然，假设了电子密度的球对称。

**7** 局域温度，以 Hartree/ $k_\mathrm{B}$ 为单位 (*PNAS*, **81**, 8028)：$T(\mathbf{r})=[2G(\mathbf{r})]/[3\rho(\mathbf{r})]$ 。注意，若 *ρ* 小于 *settings.ini* 中的 "uservar" 参数，则 *T* 视为 0。

**8** 平均局域静电势 (*J. Chem. Phys.*, **72**, 3027 (1980))：$V_{\mathrm{ESP}}(\mathbf{r})/\rho(\mathbf{r})$

**9** 形状函数：*ρ*(**r**)/*N*，其中 *N* 为总电子数

**10** 势能密度 (Virial 场)：$V(\mathbf{r})=-K(\mathbf{r})-G(\mathbf{r})=(1/4)\nabla^2\rho(\mathbf{r})-2G(\mathbf{r})$

**11** 电子能量密度：$E(\mathbf{r})=G(\mathbf{r})+V(\mathbf{r})=-K(\mathbf{r})$（有时 *E* 记为 *H*）。注意 *E*(**r**) 对全空间积分不严格等于量子化学程序打印的电子能量，因为实际中 virial 比总是多少被破坏。

**-11** 标度电子能量密度：$E_{\mathrm{scl}}(\mathbf{r})=-K(\mathbf{r})\times(R-1)$ ，其中 *R* 是从输入文件读取的 virial 比（注意并非所有输入文件都含该信息！fch/mwfn/wfx/wfn 格式有特定字段记录它）。$E_{\mathrm{scl}}$ (**r**) 对全空间积分严格等于量子化学程序打印的电子能量。[4.17.9节](sec-4-17-basin-analysis.md#4179-计算体系电子能量的原子贡献)展示了该函数的用处。

**12** 局域核吸引势能：$-\rho(\mathbf{r})\times V_{\mathrm{nuc}}(\mathbf{r})$

**13** 每个电子的动能密度：$G(\mathbf{r})/\rho(\mathbf{r})$。该量在键临界点处可区分共价成键与闭壳层相互作用，见 *J. Am. Soc. Chem.*, **120**, 13429 (1998)

**14** 电子产生的静电势：$V_{\mathrm{ele}}(\mathbf{r})=V_{\mathrm{ESP}}(\mathbf{r})-V_{\mathrm{nuc}}(\mathbf{r})=-\int\frac{\rho(\mathbf{r}')}{\left|\mathbf{r}-\mathbf{r}'\right|}\mathrm{d}\mathbf{r}'$ 。该函数的负值又称 Hartree 势，代表所有电子对 **r** 处一个电子产生的经典库仑势。

**15** 键金属性：$\xi_\mathrm{J}(\mathbf{r})=\rho(\mathbf{r})/\nabla^2\rho(\mathbf{r})$。在键临界点处，$\xi_\mathrm{J}>1$ 表明金属性相互作用，见 *J. Phys.: Condens. Matter*, **14**, 10251 (2002)。

**16** 无量纲键金属性：$\xi_\mathrm{m}(\mathbf{r})=\frac{36(3\pi^2)^{2/3}}{5}\frac{\rho(\mathbf{r})^{5/3}}{\nabla^2\rho(\mathbf{r})}$。在键临界点处，值越大对应键的金属性越强，见 *Chem. Phys. Lett.*, **471**, 174 (2009)。

**17** 每个电子的能量密度：*E*(**r**)/*ρ*(**r**)，该值在 BCP 处称为键度参数 (BD)，细节见 *J. Chem. Phys.*, **117**, 5529 (2002)，作者主张对共价键（即 $E_{\mathrm{BCP}}<0$），BD 给出共价程度，相互作用越强 BD 量级越大；而对闭壳层相互作用（即 $E_{\mathrm{BCP}}>0$），BD 可视为软化程度，相互作用越弱 BD 量级越大。

**18** 慢电子区域 (RoSE)，定义于 *Chem. Phys. Lett.*, **582**, 144 (2013)，图案与 ELF 很相似，值域为 \[-1,1\]：$\nu_\pm=\frac{D_0(\mathbf{r})-G(\mathbf{r})}{D_0(\mathbf{r})+G(\mathbf{r})}$

**19** 单指数衰减探测器 (SEDD)，与 ELF 高度类似。实现的是 *J. Chem. Theory Comput.*, **10**, 3745 (2014) 中的更新定义：$\mathrm{SEDD}(\mathbf{r})=\ln\left\{1+\left[\frac{\nabla(\nabla\rho(\mathbf{r})/\rho(\mathbf{r}))^2}{\rho(\mathbf{r})}\right]^2\right\}$

**20** 密度重叠区域指示函数 (DORI)，定义于 *J. Chem. Theory Comput.*, **10**, 3745 (2014)：$\mathrm{DORI}(\mathbf{r})=\theta(\mathbf{r})/[1+\theta(\mathbf{r})]$ ，其中 $\theta(\mathbf{r})=[\nabla(\nabla\rho(\mathbf{r})/\rho(\mathbf{r}))^2]^2/[\nabla\rho(\mathbf{r})/\rho(\mathbf{r})]^6$ 。DORI 主要用于揭示原子间相互作用区域，更多信息见[3.23.3节](sec-3-23-visual-study-of-weak-interaction.md#3233-平均-nci-分析-anci3)。IRI 比 DORI 好用得多。

**21** 电偶极矩 X 分量的被积函数：−*x*×*ρ*(**r**)

**22** 电偶极矩 Y 分量的被积函数：−*y*×*ρ*(**r**)

**23** 电偶极矩 Z 分量的被积函数：−*z*×*ρ*(**r**)

**24** 闭壳层 DFT 线性响应核的近似形式 (*Phys. Chem. Chem. Phys.*, **14**, 3960 (2012))：$\chi(\mathbf{r}_1,\mathbf{r}_2)\approx 4\sum_{i\in\mathrm{occ}}\sum_{j\in\mathrm{vir}}\frac{\varphi_i^*(\mathbf{r}_1)\varphi_j(\mathbf{r}_1)\varphi_j^*(\mathbf{r}_2)\varphi_i(\mathbf{r}_2)}{\varepsilon_i-\varepsilon_j}$

**25** 电子动量涨落的量级：$\tilde{P}(\mathbf{r})=\left|\nabla\rho(\mathbf{r})\right|/[2\rho(\mathbf{r})]$ ，又称定域电子探测器 (LED)，有助于讨论成键，与约化密度梯度很相似，见 *Theor. Chem. Acc.*, **127**, 393 (2010)

**26** Thomas-Fermi 动能泛函的被积函数（闭壳层形式）：$\tau_{\mathrm{TF}}(\mathbf{r})=C_{\mathrm{TF}}\rho(\mathbf{r})^{5/3}$，其中 $C_{\mathrm{TF}}=(3/10)(3\pi^2)^{2/3}=2.871234$。这是非相互作用均匀电子气的精确动能密度。若需自旋极化形式，用自定义函数 1200。

**27** 局域电子亲和能 (LEA)：$EA_\mathrm{L}(\mathbf{r})=\frac{-\sum_{i\in\mathrm{vir}}\left|\varphi_i(\mathbf{r})\right|^2\varepsilon_i}{\sum_{i\in\mathrm{vir}}\left|\varphi_i(\mathbf{r})\right|^2}$ ，与平均局域电离能很相似，但 *i* 遍历所有未占据轨道。见 *J. Mol. Model.*, **9**, 342 (2003)。对实际分子应用该函数的示例见[4.12.13节](sec-4-12-quantitative-analysis-of-molecular-surface.md#41213-使用局域电子亲和能-local-electron-affinity和局域电子附着能-local-electron-attachment-energy揭示亲电区域-electrophilic-regions)。

**-27** 局域电子附着能：$E_{\mathrm{att}}(\mathbf{r})=\frac{n\sum_{i=\mathrm{LUMO}}^{\varepsilon_i<0}\left|\varphi_i(\mathbf{r})\right|^2\varepsilon_i}{\rho(\mathbf{r})}$ 。*i* 遍历所有能量为负的未占据轨道。对限制性和非限制性波函数，*n* 分别等于 2 和 1。见 *J. Phys. Chem. A.*, **120**, 10023 (2016)。该函数与 LEA 用途相似但更稳健。对实际分子应用该函数的示例见[4.12.13节](sec-4-12-quantitative-analysis-of-molecular-surface.md#41213-使用局域电子亲和能-local-electron-affinity和局域电子附着能-local-electron-attachment-energy揭示亲电区域-electrophilic-regions)。

**28** 局域 Mulliken 电负性：$\chi_\mathrm{L}(\mathbf{r})=[\bar{I}(\mathbf{r})+EA_\mathrm{L}(\mathbf{r})]/2$ ，见 *J. Mol. Model.*, **9**, 342 (2003)

**29** 局域硬度：$\eta_\mathrm{L}(\mathbf{r})=[\bar{I}(\mathbf{r})-EA_\mathrm{L}(\mathbf{r})]/2$ ，见 *J. Mol. Model.*, **9**, 342 (2003)

**注**：要用 $EA_\mathrm{L}$ 、$E_{\mathrm{att}}$ 、$\chi_\mathrm{L}$ 和 $\eta_\mathrm{L}$，输入文件必须同时含单行列式波函数的占据和未占据轨道（但不支持限制性开壳层），应使用 .mwfn、.fch、.molden 和 .gms 等格式作输入文件。

一般地，$EA_\mathrm{L}$（从而 $\chi_\mathrm{L}$ 和 $\eta_\mathrm{L}$）与带弥散函数的基组不兼容，而求 $E_{\mathrm{att}}$ 可用任何基组。与增广基组好得多的兼容性是 $E_{\mathrm{att}}$ 相对 $EA_\mathrm{L}$ 的显著优点。但要用 $E_{\mathrm{att}}$ ，至少 LUMO 能量应为负，而常用水平下该条件常不满足。$E_{\mathrm{att}}$ 原论文发现该函数在 B3LYP/6-31+G(d,p) 轨道下工作合理。

**30** 电子密度的椭率：$\varepsilon(\mathbf{r})=[\lambda_1(\mathbf{r})/\lambda_2(\mathbf{r})]-1$ ，其中 *λ*₁ 和 *λ*₂ 分别是 *ρ* 的 Hessian 矩阵最低和次低本征值。在键临界点 (BCP)，*λ*₁ 和 *λ*₂ 均为负，体现垂直于键的两个正交方向上电子密度的曲率。BCP 处的 *ε* 常视为键周围电子密度非轴对称分布的指标，偏离轴对称分布越大，BCP 处 *ε* 值越大。

**31** eta 指数：$\eta(\mathbf{r})=\left|\lambda_1(\mathbf{r})\right|/\lambda_3(\mathbf{r})$ ，其中 *λ*₁ 和 *λ*₃ 分别是 *ρ* 的 Hessian 矩阵最低和最高本征值。据称键临界点处 *η* 值对闭壳层相互作用小于 1 并随共价性增强而增大，见 *Angew. Chem. Int. Ed.*, **53**, 2766 (2014)，讨论另见 *J. Phys. Chem. A*, **114**, 552 (2010)。

**32** Tian Lu 修改的 eta 指数：$\eta'(\mathbf{r})=\left|\lambda_1(\mathbf{r})\right|/\lambda_3(\mathbf{r})-1$ 。类似 *η*，但 *η*' 负值对应闭壳层相互作用。

**33** 分子中作用于单电子的势 (PAEM)，见 *J. Comput. Chem.*, **35**, 965 (2014)：$V_{\mathrm{PAEM}}(\mathbf{r})=-\sum_A\frac{Z_A}{\left|\mathbf{r}-\mathbf{R}_A\right|}+\frac{1}{\rho(\mathbf{r})}\int\frac{\pi(\mathbf{r},\mathbf{r}')}{\left|\mathbf{r}-\mathbf{r}'\right|}\mathrm{d}\mathbf{r}'$ ，*π* 是对密度。可进一步写为 $V_{\mathrm{PAEM}}(\mathbf{r})=-V_{\mathrm{ESP}}(\mathbf{r})+V_{\mathrm{XC}}(\mathbf{r})=-V_{\mathrm{ESP}}(\mathbf{r})+\frac{1}{\rho(\mathbf{r})}\int\frac{\Gamma_{\mathrm{XC}}^{\alpha,\mathrm{tot}}(\mathbf{r},\mathbf{r}')+\Gamma_{\mathrm{XC}}^{\beta,\mathrm{tot}}(\mathbf{r},\mathbf{r}')}{\left|\mathbf{r}-\mathbf{r}'\right|}\mathrm{d}\mathbf{r}'$ ，其中 $V_{\mathrm{ESP}}$ 是总分子静电势，$V_{\mathrm{XC}}$ 是交换-相关势。在 Multiwfn 中，交换-相关密度 Γ 按 Müller 近似求得，细节见[2.6节](sec-2-6-real-space-functions.md)第 17 部分。原论文表明 PAEM 可能有助于区分共价与非共价相互作用。PAEM 的应用例子见[4.3.3节](sec-4-3-output-and-plot-various-properties-in-a-line.md#433-用-paem-mo-方法研究原子间相互作用)。

**34** 与 **33** 相同，但 $V_{\mathrm{XC}}$ 直接对应 DFT 交换-相关势。其具体形式可经 "iDFTxcsel" 参数选择，本节末有细节。该形式的 PAEM 比 **33** 快得多，但只支持闭壳层波函数。对非常大的体系，**33** 的耗时在计算上不可接受，故 **34** 是唯一选择。

**35** $\left| V\left( \mathbf{r} \right) \right|/G(\mathbf{r})$ 。*J. Chem. Phys.*, **117**, 5529 (2002) 提出该量在 BCP 处可用于判别相互作用类型。<1 对应闭壳层相互作用；>2 对应共价相互作用；而 >1 且 <2 对应中间型相互作用。

**36** 在顶对密度，即对密度的两个位置相同：π(**r**,**r**)。讨论见如 *Int. J. Quantum Chem.*, **61**, 197 (1995)。"paircorrtype" 参数在 *settings.ini* 中提及会影响结果。

**37** *J. Phys. Chem. A*, **122**, 3087 (2018) 定义并在 *J. Mol. Model.*, **24**, 213 (2018) 进一步检验的强共价相互作用指数 (SCI)。该函数被证明对识别非常强的共价键很有用。SCI 表为 $\mathrm{SCI}(\mathbf{r})=1/\zeta(\mathbf{r})$，其中 $\zeta(\mathbf{r})=[\tau_{\mathrm{S}}(\mathbf{r})-\tau_{\mathrm{W}}(\mathbf{r})]/\tau_{\mathrm{TF}}$。*τ*$_{S}$、*τ*$_{W}$ 和 *τ*$_{TF}$ 的含义见介绍 ELF 的[2.6节](sec-2-6-real-space-functions.md)。易见 SCI 指数与 ELF 密切相关，后者可写为 $\mathrm{ELF}(\mathbf{r})=1/[1+\zeta^2(\mathbf{r})]$。

**38** 电子密度 Hessian 第二本征矢与给定平面法矢的夹角，平面可由主功能 1000 的选项 4 定义；屏幕会显示平面的单位法矢，假设你用三点 *A*、*B*、*C* 定义平面得到矢量 **u**，但你真正想要的是 -**u**，则按相反顺序重新输入这些点即可，即 *C*、*B*、*A*。在 *J. Phys. Chem. A*, **115**, 12512 (2011) 中用沿键路径的该量揭示了 π 相互作用。

**39** 不含特定核贡献的静电势：

$V_\mathrm{n}(\mathbf{r})=\sum_{A\neq K}\frac{Z_A}{\left|\mathbf{r}-\mathbf{R}_A\right|}-\int\frac{\rho(\mathbf{r}')}{\left|\mathbf{r}-\mathbf{r}'\right|}\mathrm{d}\mathbf{r}'$ ，其中核 *K* 可由主功能 1000（在主界面隐藏但可选）的选项 3 设置。$V_\mathrm{n}$ 是有用的量，例如若 *K* 取某氢的序号，则该值与其 p$K_{a}$ 相关，因为此时 $V_\mathrm{n}$ 近似反映质子在 *K* 位置与体系其余部分的结合能；此外，*J. Phys. Chem. A*, **118**, 1697 (2014) 表明 $V_\mathrm{n}$ 可用于定量预测以静电效应为主导的弱相互作用（即氢键、卤键、二氢键）的相互作用能，介绍和例子见[4.1.2节](sec-4-1-calculate-properties-at-a-point.md#412-计算核位置处静电势-esp以评估-h₂ohf-的相互作用强度)。

> **注**
>
> 值得一提的是，在主功能 1 中，当要求 Multiwfn 打印某原子核位置处的性质时，不含该原子核电荷贡献的静电势会自动打印。

**40** 空间位阻能密度：$\left|\nabla\rho(\mathbf{r})\right|^2/[8\rho(\mathbf{r})]$ ，等价于 Weizsäcker 泛函的被积函数。

**41** 空间位阻势：$\upsilon_\mathrm{s}(\mathbf{r})=\frac{1}{8}\frac{\left|\nabla\rho(\mathbf{r})\right|^2}{[\rho(\mathbf{r})+\delta]^2}-\frac{1}{4}\frac{\nabla^2\rho(\mathbf{r})}{\rho(\mathbf{r})+\delta}$ 。该量的负值又称单电子势 (OEP)。注意 *δ* 是人为引入以避免分母比分子更快趋于 0 的很小项。*δ* 的值可由 *settings.ini* 中的 "steric_addminimal" 确定。若 *δ* 设为 0，则恢复空间位阻势的原始表达式。

**42** 空间位阻电荷：$q_\mathrm{s}(\mathbf{r})=\nabla^2\upsilon_\mathrm{s}(\mathbf{r})/(-4\pi)$ 。由空间位阻力的有限差分求得。

**43** 空间位阻力的量级：$F_\mathrm{s}(\mathbf{r})=\left|-\nabla\upsilon_\mathrm{s}(\mathbf{r})\right|$ 。解析求得。

注意，上述 *δ* 项也影响空间位阻力和空间位阻电荷。空间位阻能/势/力/电荷的讨论见 *J. Chem. Phys.*, **126**, 244103 (2007)。

**44,45,46** 阻尼空间位阻势、基于阻尼空间位阻势的空间位阻力、直接阻尼空间位阻力：未公开记录

**47** 阻尼空间位阻电荷：未公开记录

**49** 相对 Shannon 熵密度，又称信息增益密度：$i_{\mathrm{G}}(\mathbf{r})=\rho(\mathbf{r})\ln\frac{\rho(\mathbf{r})}{\rho_{0}(\mathbf{r})}$ ，其中 *ρ*₀(**r**) 是 promolecular 密度。对该函数做任何分析或可视化之前，必须先进入主功能 1000（隐藏功能）再选子功能 17 构建 promolecular 波函数并存入内存中的特殊空间；该 promolecular 波函数通过为所有原子准备波函数文件（细节见[3.7.3节](sec-3-7-custom-operation-promolecular-and-deformation-properties.md#373-原子波函数的生成-generation-of-atomic-wavefunctions)）再组合在一起产生。注意在子功能 17 中，当 Multiwfn 问"你是否想让内存中的波函数信息对应刚产生的 promolecular 波函数？(y/n)"时，应输入 *n* 以避免当前波函数被 promolecular 波函数替换。

**50** Shannon 熵密度：$s_s(\mathbf{r})=-\rho(\mathbf{r})\ln\rho(\mathbf{r})$ 。

**51** Fisher 信息密度：$i_\mathrm{F}(\mathbf{r})=\left|\nabla\rho(\mathbf{r})\right|^2/\rho(\mathbf{r})$ 。注意该量与 Weizsäcker 泛函只差 1/8 常数因子。

**52** 第二 Fisher 信息密度：$i'_\mathrm{F}(\mathbf{r})=-\nabla^2\rho(\mathbf{r})\ln\rho(\mathbf{r})$ 。Shannon 熵与 Fisher 信息的关系见 *J. Chem. Phys.*, **126**, 191107 (2007)。该函数对全空间积分与 Fisher 信息密度的积分严格相同。

**53** Ghosh 熵密度或 Ghosh-Berkowitz-Parr (GBP) 熵密度，以 $k_\mathrm{B}$ 为单位 (*PNAS*, **81**, 8028 (1984))：$s(\mathbf{r})=(3/2)\rho(\mathbf{r})\{\lambda+\ln[t(\mathbf{r})/t_{\mathrm{TF}}(\mathbf{r})]\}$ ，其中 $\lambda=5/3+\ln(4\pi c_{\mathrm{k}}/3)$ ，$c_{k}$ 是 Thomas-Fermi 常数 $(3/10)(3\pi^2)^{2/3}=2.871234$，动能密度项 *t*(**r**) 取 Lagrangian 动能密度 *G*(**r**)。

**54** 与 53 相同，但 *t*(**r**) 取 *G*(**r**) − ∇²*ρ*(**r**)/8，即严格对应 *PNAS*, **81**, 8028 (1984) 方程 22 的动能密度。极少数情况下该定义的动能密度导致很小的负值，因这些点 $t_{\mathrm{TF}}$ (**r**) 也非常接近 0，为能正常得到结果，此时 $\ln[t(\mathbf{r})/t_{\mathrm{TF}}(\mathbf{r})]$ 简单置为 0。

**55** 二次型 Rényi 熵积分部分的被积函数：*ρ*²(**r**)。该函数对全空间积分对应二阶 Onicescu 信息。

**56** 三次型 Rényi 熵积分部分的被积函数：*ρ*³(**r**) 。该函数对全空间积分再除以 2 对应三阶 Onicescu 信息。

**57** $g_1(\mathbf{r})=\nabla^2\rho(\mathbf{r})\ln\frac{\rho(\mathbf{r})}{\rho_0(\mathbf{r})}$

**58** $g_2(\mathbf{r})=\rho(\mathbf{r})\left[\frac{\nabla^2\rho(\mathbf{r})}{\rho(\mathbf{r})}-\frac{\nabla^2\rho_0(\mathbf{r})}{\rho_0(\mathbf{r})}\right]$

**59** $g_3(\mathbf{r})=\rho(\mathbf{r})\left[\nabla\ln\frac{\rho(\mathbf{r})}{\rho_0(\mathbf{r})}\right]^2$
注意自定义函数 57、58、59 只能在主功能 3、4、5 中绘制为图来研究，同时 deformation 和 promolecular 图不可用。

**60** Pauli 势：$V_\mathrm{θ}$ 。Multiwfn 支持两种求该函数的方式，取决于 *settings.ini* 中的 "ispecial"：

- ispecial=0：按 *Comput. Theor. Chem.*, **1006**, 92 (2013) 的方程 17，$V_\mathrm{θ}$ = *µ* + $V_{\mathrm{ESP}}$ − $V_{\mathrm{XC}}$ − $V_\mathrm{W}$ ，其中 *µ* 是化学势（Multiwfn 假设为 0），$V_{\mathrm{ESP}}$ 是静电势（如[2.6节](sec-2-6-real-space-functions.md)所述），$V_{\mathrm{XC}}$ 是交换-相关势（其形式由 *settings.ini* 中的 "iDFTxcsel" 确定，见后）。

- ispecial=1：用原始定义，即 ${V}_\mathrm{θ}={V}_{\mathrm{S}}-{V}_{\mathrm{W}}=\delta{\tau}_{\mathrm{S}}\left[ \rho \right]/\delta\rho-\delta{\tau}_{\mathrm{W}}\left[ \rho \right]/\delta\rho$ ，其中 $V_\mathrm{S}$ 是非相互作用动能泛函（*τ*$_{S}$）的势，$V_\mathrm{W}$ 是 Weizsäcker 动能泛函（*τ*$_{W}$）的势。*τ*$_{S}$ 的形式可由 *settings.ini* 中的 "iKEDsel" 选择，见后；目前只支持 iKEDsel 为 3、5、7。

由于 Pauli 力和电荷由 Pauli 势经有限差分算得，而量子势/力/电荷基于 Pauli 势/力/电荷定义，自定义函数 61\~65 也受 "ispecial" 影响。

**61** Pauli 力的量级：$F_\mathrm{θ}(\mathbf{r})=\left|-\nabla V_\mathrm{θ}(\mathbf{r})\right|$

**62** Pauli 电荷：$q_\mathrm{θ}(\mathbf{r})=\nabla^2 V_\mathrm{θ}(\mathbf{r})/(-4\pi)$

**63** 量子势：$V_{\mathrm{q}}=V_\mathrm{θ}+V_{\mathrm{XC}}$ 。当 ispecial=0，显然在 Multiwfn 中它简单对应 $V_{\mathrm{ESP}}$ − $V_\mathrm{W}$

**64** 量子力的量级：$F_{\mathrm{q}}(\mathbf{r})=\left|-\nabla V_{\mathrm{q}}(\mathbf{r})\right|$

**65** 量子电荷：$q_{\mathrm{q}}(\mathbf{r})=\nabla^2 V_{\mathrm{q}}(\mathbf{r})/(-4\pi)$

**66** 静电力的量级：$F_{\mathrm{ESP}}(\mathbf{r})=\left|-\nabla[-V_{\mathrm{ESP}}(\mathbf{r})]\right|$ 。如 *Phys. Chem. Chem. Phys.*, **19**, 1496 (2017) 所讨论，空间位阻力、量子力和静电力（分别为自定义函数 43、64、66）之间有非常密切的关系。

**67** 静电荷：$q_{\mathrm{ESP}}(\mathbf{r})=\nabla^2[-V_{\mathrm{ESP}}(\mathbf{r})]/(-4\pi)$

**68** Shubin Liu 能量分解中静电项电子部分的能量密度：$\upsilon_e(\mathbf{r})=\rho(\mathbf{r})\left[\int\frac{\rho(\mathbf{r}')}{\left|\mathbf{r}-\mathbf{r}'\right|}\mathrm{d}\mathbf{r}'-\sum_A\frac{Z_A}{\left|\mathbf{r}-\mathbf{R}_A\right|}\right]=-V_{\mathrm{ESP}}(\mathbf{r})\rho(\mathbf{r})$ 。要了解 Shubin Liu 能量分解，见[3.24.2节](sec-3-24-energy-decomposition-analysis.md#3242-shubin-liu-能量分解)。

**69, -69** Shubin Liu 能量分解中量子部分的能量密度：*τ*$_{s}$(**r**) − *τ*$_{W}$(**r**) + *ε*$_{XC}$(**r**)，其中 *τ*$_{s}$ 是 Hamiltonian 动能密度（若 userfunc = 69）或 Lagrangian 动能密度（若 userfunc = -69）。*τ*$_{W}$ 是 Weizsäcker 泛函的被积函数（与 userfunc=5 相同），*ε*$_{XC}$ 是交换-相关能密度（与 userfunc=1000 相同），其形式可由 *settings.ini* 中的 "iDFTxcsel" 参数选择，细节见后。

**70** 相空间定义的 Fisher 信息密度 (PS-FID)：$i_{\mathrm{f}}(\mathbf{r})=\frac{3\rho(\mathbf{r})}{k_{\mathrm{B}}T(\mathbf{r})}=\frac{9}{2}\frac{\rho^2(\mathbf{r})}{G(\mathbf{r})}$ ，其中 *T*(**r**) 是上文的局域温度。该函数与 ELF 和 LOL 特征很相似，可清晰揭示电子对的空间定域。介绍和示例应用见 *Chem. Phys.*, **435**, 49 (2014)。

**71, 72, 73, 74** 三维表示的电子线动量密度 (EMD)。电子线动量算符是 $-i\nabla$ ，对某轨道 X 方向线动量的期望值是 $-i\left<\varphi\left|\nabla\right|\varphi\right>$ ，故波函数的 EMD 的 X 分量可定义为（忽略虚数符号）$p_x(\mathbf{r})=-\sum_i\eta_i\varphi_i^*(\mathbf{r})\partial\varphi_i(\mathbf{r})/\partial x$ ，Y 和 Z 分量类似。第 71、72、73 个自定义函数分别对应 X、Y、Z 分量。EMD 的量级 (74) 定义为 $p_{\mathrm{tot}}(\mathbf{r})=\sqrt{p_x^2(\mathbf{r})+p_y^2(\mathbf{r})+p_z^2(\mathbf{r})}$ 。

**75, 76, 77, 78** 磁偶极矩密度 (MDMD)。磁偶极矩的算符是角动量算符（见 *Theor. Chim. Acta*, **6**, 341 (1966)）：

$$
-i(\mathbf{r}\times\nabla)=-i\left[\mathbf{i}\left(y\frac{\partial}{\partial z}-z\frac{\partial}{\partial y}\right)+\mathbf{j}\left(z\frac{\partial}{\partial x}-x\frac{\partial}{\partial z}\right)+\mathbf{k}\left(x\frac{\partial}{\partial y}-y\frac{\partial}{\partial x}\right)\right]
$$

其中 **i**、**j**、**k** 分别是 X、Y、Z 方向的单位矢量。因此，MDMD 的 X、Y、Z 分量可定义如下（忽略虚数符号）：

$$
m_x(\mathbf{r})=-\sum_i\eta_i\varphi_i^*(\mathbf{r})\left[y\frac{\partial\varphi_i(\mathbf{r})}{\partial z}-z\frac{\partial\varphi_i(\mathbf{r})}{\partial y}\right]
$$

$$
m_y(\mathbf{r})=-\sum_i\eta_i\varphi_i^*(\mathbf{r})\left[z\frac{\partial\varphi_i(\mathbf{r})}{\partial x}-x\frac{\partial\varphi_i(\mathbf{r})}{\partial z}\right]
$$

$$
m_z(\mathbf{r})=-\sum_i\eta_i\varphi_i^*(\mathbf{r})\left[x\frac{\partial\varphi_i(\mathbf{r})}{\partial y}-y\frac{\partial\varphi_i(\mathbf{r})}{\partial x}\right]
$$

第 75、76、77 个自定义函数分别对应 X、Y、Z 分量。第 78 个自定义函数是 MDMD 的量级：$m_{\mathrm{tot}}(\mathbf{r})=\sqrt{m_x^2(\mathbf{r})+m_y^2(\mathbf{r})+m_z^2(\mathbf{r})}$ 。

**79** 电子能量密度的梯度模：$|\nabla E(\mathbf{r})|$

**80** 电子能量密度的拉普拉斯：∇²*E*(**r**)

**81, 82, 83** Hamiltonian 动能密度的 X、Y、Z 分量。

**84, 85, 86** Lagrangian 动能密度的 X、Y、Z 分量。

**87, 88, 89** 局域总、动态、非动态电子相关函数。介绍和计算例子见[4.A.7.2节](sec-4-A-special-topics-and-advanced-tutorials.md#4a72-局域电子相关函数)。

**90** Grimme 在 *Angew. Chem. Int. Ed.*, **54**, 1 (2015) 提出的分数占据数加权电子密度 (FOD)。FOD 的介绍和计算例子见[4.A.7.1节](sec-4-A-special-topics-and-advanced-tutorials.md#4a71-分数占据数加权电子密度fod)。

**91** 基于 Hirshfeld 划分的独立梯度模型 (IGMH) 方法定义的两个片段间的 $\delta g^{\mathrm{inter}}$，细节见[3.23.5节](sec-3-23-visual-study-of-weak-interaction.md#3235-基于前分子-promolecular密度的独立梯度模型-independent-gradient-model-igm分析-10)和[3.23.6节](sec-3-23-visual-study-of-weak-interaction.md#3236-基于电子密度-hirshfeld-分区的-igm-igmh分析-11)。要用该函数，应先进入主功能 1000 选选项 16 定义两个片段。

**92**、**93**、**94** 基于 UFF 力场参数的 van der Waals 势、排斥势和色散势，详细介绍见[3.23.7节](sec-3-23-visual-study-of-weak-interaction.md#3237-范德华势的可视化-6)。单位为 kcal/mol，探针原子可由 *settings.ini* 中的 "ivdwprobe" 设置。注意 **92** 与[2.6节](sec-2-6-real-space-functions.md)所述第 25 个函数相同。

**95**、**96**、**97**、**98** 轨道加权的 $f^{+}$、$f^{-}$、$f^{0}$ Fukui 函数以及轨道加权 dual descriptor。它们最初提出于 *J. Comput. Chem.*, **38**, 481 (2017) 和 *J. Phys. Chem. A*, **123**, 10556 (2019)。它们有助于研究前线分子轨道（准）简并体系的局域反应性，简介见[3.25.3节](sec-3-25-conceptual-density-functional-theory-analysis.md#3253-专题-1轨道加权-fukui-函数与对偶描述符)，示例见[4.22.2节](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md#4222-轨道加权-fukui-函数和轨道加权对偶描述符研究示例)。这些函数中的 Δ 参数可由主功能 1000（隐藏选项）的选项 6 设置。由于这些函数涉及虚轨道，应使用 mwfn/fch/molden/gms 作输入文件。只支持闭壳层单行列式波函数。

**99** 相互作用区域指示函数 (IRI)：与[2.6节](sec-2-6-real-space-functions.md)所述函数 24 相同。

**100** 非平衡度（又称半相似度）：${D}_{\mathrm{r}}\left( \mathbf{r} \right)={\rho}^{2}\left( \mathbf{r} \right)$ 。示例应用见 *Int. J. Quantum Chem.*, **113**, 2589 (2013)。

**101** ESP 的正部：${V}_{\mathrm{ESP}}^{+}$ 。在 $V_{\mathrm{ESP}}$ 为正的区域，${V}_{\mathrm{ESP}}^{+}={V}_{\mathrm{ESP}}$ ；ESP 为负处，${V}_{\mathrm{ESP}}^{+}=0$ 。

**102** ESP 的负部：${V}_{\mathrm{ESP}}^{-}$ ，定义与 ${V}_{\mathrm{ESP}}^{+}$ 类似。

**103** 电场量级 $|\mathbf{F}|$。由于电场矢量就是 ESP 的负梯度矢量，该量对应 ESP 梯度的模。

**110** Shubin Liu 能量分解分析（介绍见[3.24.2节](sec-3-24-energy-decomposition-analysis.md#3242-shubin-liu-能量分解)）定义的空间位阻、静电和量子分量的总能量密度，对应自定义函数 40、68、69 之和

**111** 空间位阻势、静电势和量子势之和。注意 *settings.ini* 中的 "ispecial"、"iDFTxcsel" 和 "iKEDsel" 影响本函数和下两个函数，细节见自定义函数 60 的描述。

**112** 空间位阻力、静电力和量子力矢量和的量级。

**113** 空间位阻电荷、静电荷和量子电荷之和。

**114** Pauli 动能密度：${\tau}_\mathrm{θ}(\mathbf{r})={\tau}_{\mathrm{S}}(\mathbf{r})-{\tau}_{\mathrm{W}}(\mathbf{r})$ ，其中 *τ*$_{S}$(**r**) 是可由 *settings.ini* 中的 "iKEDsel" 选择的动能密度（见后），*τ*$_{W}$(**r**) 是 Weizsäcker 动能密度。

**115** 硬度 $S=|{\lambda}_{1}|/|{\lambda}_{3}|$ ，其中 *λ*₁ < *λ*₂ < *λ*₃ 是电子密度 Hessian 矩阵的三个本征值。见 *J. Comput. Chem.*, **37**, 2722 (2016)。

**116**、**117**、**118**：应力张量硬度 ${S}_{\sigma}=|{\lambda}_{1\sigma}|/|{\lambda}_{3\sigma}|$ 、应力张量极化率 $P=|{\lambda}_{3\sigma}|/|{\lambda}_{1\sigma}|$ 、应力张量椭率 ${\epsilon}_{\sigma H}=|{\lambda}_{1\sigma}|/|{\lambda}_{2\sigma}|-1$ 。*λ*$_{1σ}$ < *λ*$_{2σ}$ < *λ*$_{3σ}$ 是应力张量 **σ** 的三个本征值。${S}_{\sigma}$ 和 *P* 见 *J. Comput. Chem.*, **37**, 2722 (2016)，${\epsilon}_{\sigma H}$ 见 <http://sobereva.com/wfnbbs/viewtopic.php?pid=4667> 。

对感兴趣的用户，这里简述应力张量 **σ**。它由 Bader 在 *J. Chem. Phys.*, **73**, 2871 (1980) 中定义如下（此处用原子单位表示）：

$$
\sigma(\mathbf{r})=-\frac{1}{4}\left[(\nabla\nabla'+\nabla'\nabla-\nabla\nabla-\nabla'\nabla')\Gamma^{(0)}(\mathbf{r},\mathbf{r}')\right]_{\mathbf{r}=\mathbf{r}'}
$$

明确地，其元素可写为：

$$
\sigma_{i,j}(\mathbf{r})=-\frac{1}{4}\left[\left(\frac{\partial^2}{\partial r_i\partial r'_j}+\frac{\partial^2}{\partial r'_i\partial r_j}-\frac{\partial^2}{\partial r_i\partial r_j}-\frac{\partial^2}{\partial r'_i\partial r'_j}\right)\Gamma^{(0)}(\mathbf{r},\mathbf{r}')\right]_{\mathbf{r}=\mathbf{r}'}
$$

其中 $r_{1}$ =*x*、$r_{2}$ =*y*、$r_{3}$ =*z*，实空间形式的单电子约化密度矩阵可基于轨道求为 ${\Gamma}^{\left( 1 \right)}(\mathbf{r},{\mathbf{r}}^{'})=\sum_{i} {\eta}_{i}{\varphi}_{i}^{*}(\mathbf{r}){\varphi}_{i}(\mathbf{r'})$ 。目前只考虑实波函数，故 Multiwfn 中应力张量的元素易求为：

$$
\sigma_{i,j}(\mathbf{r})=-\frac{1}{4}\sum_t\eta_t\left[2\frac{\partial\varphi_t(\mathbf{r})}{\partial r_i}\frac{\partial\varphi_t(\mathbf{r})}{\partial r_j}-2\frac{\partial^2\varphi_t(\mathbf{r})}{\partial r_i\partial r_j}\varphi_t(\mathbf{r})\right]
$$

若需得到整个应力张量，可在主功能 1 中输入坐标，应力张量会与其它量一起输出。

与应力张量密切相关的 path-packets 分析可用 Asdrubal Lozada 基于打补丁的 Multiwfn 代码贡献的 shell 脚本实现，相关信息见 <http://sobereva.com/wfnbbs/viewtopic.php?pid=4698> 和 <https://github.com/aslozada/Stress_tensor>。

**200** \[0,1) 的随机数。

**819** 超强相互作用 (USI)：$\mathrm{USI}(\mathbf{r})={\mathrm{\nabla }}^{2}\rho(\mathbf{r})/{\rho}^{5/3}(\mathbf{r})$ 。细节见 *J. Phys. Chem. A*, **126**, 2437 (2022)。

**820** 成键与非共价相互作用 (BNI)：$\mathrm{BNI}(\mathbf{r})=[G\left( \mathbf{r} \right)-{\tau}_{\mathrm{W}}\left( \mathbf{r} \right)]/{\tau}_{\mathrm{W}}(\mathbf{r})$ ，其中 *G*(**r**) 是 Lagrangian 动能密度。细节见 *J. Phys. Chem. A*, **126**, 2437 (2022)。

**900, 901, 902** X、Y、Z 坐标变量。

下面 910\~914 的函数计算原子权重函数。所算的原子由 *settings.ini* 中的 "uservar" 确定。除 Becke 原子权重函数外支持周期体系。

**910** Hirshfeld 原子权重函数。

**911,912** 分别用 Tian Lu 共价半径和 CSD 共价半径的 Becke 原子权重函数。边界锐度参数为 3。

**913** Tian Lu 误差函数型原子权重函数

**914** Tian Lu 高斯函数型原子权重函数

**999** 局域 Hartree-Fock 交换能（或 Hartree-Fock 交换能密度）。它对全空间积分对应 Hartree-Fock 交换能。

闭壳层情形：

$$
e_{\mathrm{HFX}}(\mathbf{r})=-\frac{1}{4}\sum_{bd}E_b(\mathbf{r})E_d(\mathbf{r})v_{bd}(\mathbf{r})
$$

其中：

$$
\begin{gathered}v_{bd}(\mathbf{r})=\int\chi_b(\mathbf{r}')\frac{1}{\left|\mathbf{r}-\mathbf{r}'\right|}\chi_d(\mathbf{r}')\mathrm{d}\mathbf{r}'\\ E_b(\mathbf{r})=\sum_i P_{ib}\chi_i(\mathbf{r})\\ E_d(\mathbf{r})=\sum_i P_{id}\chi_i(\mathbf{r})\end{gathered}
$$

其中 *χ* 是基函数，**P** 是总密度矩阵。

开壳层情形：$e_{\mathrm{HFX}}$ 是其 alpha 和 beta 部分之和

$$
\begin{gathered}e_{\mathrm{HFX}}^\alpha(\mathbf{r})=-\frac{1}{2}\sum_{bd}E_b^\alpha(\mathbf{r})E_d^\alpha(\mathbf{r})v_{bd}(\mathbf{r})\\ e_{\mathrm{HFX}}^\beta(\mathbf{r})=-\frac{1}{2}\sum_{bd}E_b^\beta(\mathbf{r})E_d^\beta(\mathbf{r})v_{bd}(\mathbf{r})\end{gathered}
$$

其中：

$$
\begin{gathered}E_b^r(\mathbf{r})=\sum_i P_{ib}^r\chi_i(\mathbf{r})\quad\quad r=\{\alpha,\beta\}\\ E_d^r(\mathbf{r})=\sum_i P_{id}^r\chi_i(\mathbf{r})\quad\quad r=\{\alpha,\beta\}\end{gathered}
$$

**1000** DFT 交换-相关泛函的被积函数，又称交换-相关能密度。

**1100** DFT 交换-相关势，只对闭壳层体系可用：$V_{\mathrm{XC}}(\mathbf{r})=\delta E_{\mathrm{XC}}/\delta\rho(\mathbf{r})$ ，其中 $E_{\mathrm{XC}}$ 是交换-相关能

**1101** α 电子的 DFT 交换-相关势，只对开壳层体系可用：

$$
V_{\mathrm{XC}}^\alpha(\mathbf{r})=\delta E_{\mathrm{XC}}/\delta\rho^\alpha(\mathbf{r})
$$

**1102** β 电子的 DFT 交换-相关势，只对开壳层体系可用：

$$
V_{\mathrm{XC}}^\beta(\mathbf{r})=\delta E_{\mathrm{XC}}/\delta\rho^\beta(\mathbf{r})
$$

对自定义函数 1000 和 1100/1101/1102，*settings.ini* 中的 "iDFTxcsel" 用于选择 XC 泛函，细节见下。0-29 只是 X 部分，30-69 只是 C 部分，70-99 是整个 XC。例如，若 iDFTxcsel=32，则 iuserfunc=1000 对应 LYP 相关泛函的被积函数，iuserfunc=1100 对应 LYP 势。

**"iDFTxcsel" 参数的可用选项**

目前只支持 LSDA 和一些 GGA 泛函

**0** LSDA 交换：$-(3/2)[3/(4\pi)]^{1/3}\left[\rho_\alpha(\mathbf{r})^{4/3}+\rho_\beta(\mathbf{r})^{4/3}\right]$ 。闭壳层情形的等价形式是 $-(3/4)(3/\pi)^{1/3}\rho(\mathbf{r})^{4/3}$ 。

**1** Becke 88 (B88) 交换，见 *Phys. Rev. A*, **38**, 3098 (1988)。

**2** Perdew-Burke-Ernzerhof (PBE) 交换，见 *Phys. Rev. Lett.*, **77**, 3865 (1996)。

**3** Perdew-Wang 91 (PW91) 交换，见 Electronic Structure of Solids '91; Ziesche, P., Eschig, H., Eds.; Akademie Verlag: Berlin, 1991; p. 11。

**30** Vosko-Wilk-Nusair V (VWN5) 相关，见 *Can. J. Phys.*, **58**, 1200 (1980)。

**31** Perdew 86 (P86) 相关，见 *Phys. Rev. B*, **33**, 8822 (1986)。

**32** Lee-Yang-Parr (LYP) 相关，见 *Phys. Rev. B*, **37**, 785 (1988)。

**33** Perdew-Wang 91 (PW91) 相关，见其交换对应物的文献。

**34** Perdew-Burke-Ernzerhof (PBE) 相关，见其交换对应物的文献。

**70** Becke 97 (B97) 交换-相关，见 *J. Chem. Phys.*, **107**, 8554 (1997)。

**71** Hamprecht-Cohen-Tozer-Handy 含 407 个训练分子 (HCTH407) 交换-相关，见 *J. Chem. Phys.*, **114**, 5497 (2001)。

**80** SVWN5 交换-相关。

**81** BP86 交换-相关。

**82** BLYP 交换-相关。

**83** BPW91 交换-相关。

**84** PBEPBE 交换-相关。

**85** PW91PW91 交换-相关。

## **关于 iuserfunc=1200**

动能密度 (KED) 指动能泛函的被积函数。自定义函数 1200 是 Multiwfn 支持的所有 KED 的集合，它们在 *J. Chem. Phys.*, **150**, 204106 (2019) 中被系统考察。*settings.ini* 中的 "iKEDsel" 用于选择 KED 的形式。

注意，若 "iKEDsel" 不是默认值 (0)，则 ELF 和强共价相互作用指数 (SCI) 中的 *τ*$_{S}$ 项（Lagrangian 动能密度）会被相应的 KED 替换。

主功能 1000（在主菜单隐藏）中有个子功能 92，它能计算所有 KED 对全空间的积分，即基于动能泛函求动能。只有 "iKEDsel" 设为 24 时才计算 GEA4 KED，因为它需要电子密度的拉普拉斯，而其它 KED 只需电子密度及其梯度。Hamiltonian KED 的积分不由该功能计算，因为结果与 Lagrangian KED 的相同。

- iKEDsel=1：Hamiltonian KED，与实空间函数 6 相同

- iKEDsel=2：Lagrangian KED，与实空间函数 7 相同

- iKEDsel=3：Thomas-Fermi KED：$\tau_{\mathrm{TF}}(\mathbf{r})=\sum_{\sigma=\alpha,\beta}\tau_{\mathrm{TF}}^\sigma=\sum_{\sigma=\alpha,\beta}C_{\mathrm{TF}}[\rho_\sigma(\mathbf{r})]^{5/3}$ ，其中 $C_{\mathrm{TF}}=\frac{3}{10}(6\pi^2)^{2/3}=4.557799872$ 是自旋极化情形的 Thomas-Fermi 常数。

- iKEDsel=4：Weizsäcker KED：$\tau_\mathrm{W}(\mathbf{r})=\sum_{\sigma=\alpha,\beta}\frac{\left|\nabla\rho_\sigma(\mathbf{r})\right|^2}{8\rho_\sigma(\mathbf{r})}$

下述多数 KED 可用一般形式 $\tau(\mathbf{r})=\sum_{\sigma=\alpha,\beta}\tau_{\mathrm{TF}}^\sigma(\mathbf{r})F^\sigma[s^\sigma(\mathbf{r})]$ 表示，其中 $s^\sigma(\mathbf{r})=\left|\nabla\rho^\sigma(\mathbf{r})\right|/\rho^\sigma(\mathbf{r})^{4/3}$ ，*F* 称为增强因子，细节见 *J. Chem. Phys.*, **127**, 144109 (2007)。该论文系统介绍并比较了多种已有的 KED。注意该论文给出的许多表达式是错的，而下面给出的公式绝对正确，且都明确写为自旋极化形式，若它们会出现在你的工作中，请引用我的论文 *J. Chem. Phys.*, **150**, 204106 (2019)；每个 KED 的引用也见该论文。关于 KED 的更多信息和比较见 *Phys. Rev. A*, **46**, 6920 (1992) 和 *J. Chem. Phys.*, **100**, 4446 (1994)。

- iKEDsel=5：二阶梯度展开近似，$F_{\mathrm{GEA2}}^\sigma=\left[1+\frac{1}{72C_{\mathrm{TF}}}s^\sigma(\mathbf{r})^2\right]$

- iKEDsel=6：Thomas-Fermi + 1/5 Weizsäcker KED，$F_{\mathrm{TF5W}}^\sigma=\left[1+\frac{1}{40C_{\mathrm{TF}}}s^\sigma(\mathbf{r})^2\right]$

- iKEDsel=7：Thomas-Fermi + Weizsäcker KED，$F_{\mathrm{TFvW}}^\sigma=\left[1+\frac{1}{8C_{\mathrm{TF}}}s^\sigma(\mathbf{r})^2\right]$

- iKEDsel=8：Thomas-Fermi + *b*/9 Weizsäcker KED，$F_{\mathrm{TF9W}}^\sigma=\left[1+\frac{1.067}{72C_{\mathrm{TF}}}s^\sigma(\mathbf{r})^2\right]$

- iKEDsel=9：*N* 依赖的 Thomas-Fermi KED，$F_{\mathrm{TF-N}}^\sigma=1+\frac{0.313}{N^{1/3}}-\frac{0.187}{N^{2/3}}$ ，其中 *N* 是体系的总电子数

- iKEDsel=10：Pearson KED，$\tau_{\mathrm{Pear}}^\sigma=\tau_{\mathrm{TF}}^\sigma+\frac{1}{1+[s_r^\sigma(\mathbf{r})/\zeta]^6}\frac{1}{72}\frac{\left|\nabla\rho^\sigma(\mathbf{r})\right|^2}{\rho^\sigma(\mathbf{r})}$ ，其中 *ζ* 固定为 1，$s_r^\sigma(\mathbf{r})=s^\sigma(\mathbf{r})/[2(6\pi^2)^{1/3}]$ ，下同

- iKEDsel=11：DePristo-Kress Pade KED，$F_{\mathrm{DK\ Pade}}^\sigma=\frac{9b_3x^4+a_3x^3+a_2x^2+a_1x+1}{b_3x^3+b_2x^2+b_1x+1}$ ，其中 $x=[s^\sigma(\mathbf{r})]^2/(72C_{\mathrm{TF}})$ ，$a_{1}$ = 0.95、$a_{2}$ = 14.28111、$a_{3}$ = −19.57962、$b_{1}$ = −0.05、$b_{2}$ = 9.99802、$b_{3}$ = 2.96085

- iKEDsel=12：Lee-Lee-Parr KED，$F_{\mathrm{LLP}}^\sigma=1+\frac{0.0044188[s^\sigma(\mathbf{r})]^2}{1+0.0253s^\sigma(\mathbf{r})\mathrm{arcsinh}[s^\sigma(\mathbf{r})]}$

- iKEDsel=13：Ou-Yang–Levy 1 KED，$F_{\mathrm{OL1}}^\sigma=1+\frac{1}{72C_{\mathrm{TF}}}[s^\sigma(\mathbf{r})]^2+0.00187s^\sigma(\mathbf{r})$

- iKEDsel=14：Ou-Yang–Levy 2 KED，$F_{\mathrm{OL2}}^\sigma=1+\frac{1}{72C_{\mathrm{TF}}}[s^\sigma(\mathbf{r})]^2+\frac{0.0245s^\sigma(\mathbf{r})}{1+2^{5/3}s^\sigma(\mathbf{r})}$

- iKEDsel=15：Thakkar KED，$F_{\mathrm{Thak}}^\sigma=1+\frac{0.0055[s^\sigma(\mathbf{r})]^2}{1+0.0253s^\sigma(\mathbf{r})\mathrm{arcsinh}[s^\sigma(\mathbf{r})]}-\frac{0.072s^\sigma(\mathbf{r})}{1+2^{5/3}s^\sigma(\mathbf{r})}$

- iKEDsel=16：Becke 86A KED，$F_{\mathrm{B86A}}^\sigma=1+0.0039\frac{[s^\sigma(\mathbf{r})]^2}{1+0.004[s^\sigma(\mathbf{r})]^2}$

- iKEDsel=17：Becke 86B KED，$F_{\mathrm{B86B}}^\sigma=1+0.00403\frac{[s^\sigma(\mathbf{r})]^2}{\{1+0.007[s^\sigma(\mathbf{r})]^2\}^{4/5}}$

- iKEDsel=18：DePristo-Kress 87 KED，$F_{\mathrm{DK87}}^\sigma=1+0.00132327[s^\sigma(\mathbf{r})]^2\frac{1+0.861504s^\sigma(\mathbf{r})}{1+0.044286[s^\sigma(\mathbf{r})]^2}$

- iKEDsel=19：Perdew-Wang 86 KED，$F_{\mathrm{PW86}}^\sigma=\{1+1.296[s_r^\sigma(\mathbf{r})]^2+14[s_r^\sigma(\mathbf{r})]^4+0.2[s_r^\sigma(\mathbf{r})]^6\}^{1/15}$

- iKEDsel=20：Perdew-Wang 91 KED，$F_{\mathrm{PW91}}^\sigma=\frac{1+a_1s_r^\sigma(\mathbf{r})\mathrm{arcsinh}[b\times s_r^\sigma(\mathbf{r})]+\{a_2-a_3e^{-100[s_r^\sigma(\mathbf{r})]^2}\}[s_r^\sigma(\mathbf{r})]^2}{1+a_1s_r^\sigma(\mathbf{r})\mathrm{arcsinh}[b\times s_r^\sigma(\mathbf{r})]+a_4[s_r^\sigma(\mathbf{r})]^4}$ ，其中 $a_{1}$ =0.19645、$a_{2}$ =0.2743、$a_{3}$ =0.1508、$a_{4}$ =0.004、*b*=7.7956

- iKEDsel=21：Lacks-Gordon 94 KED $F_{\mathrm{LG94}}^\sigma=\frac{\{1+a_2[s_r^\sigma(\mathbf{r})]^2+a_4[s_r^\sigma(\mathbf{r})]^4+a_6[s_r^\sigma(\mathbf{r})]^6+a_8[s_r^\sigma(\mathbf{r})]^8+a_{10}[s_r^\sigma(\mathbf{r})]^{10}+a_{12}[s_r^\sigma(\mathbf{r})]^{12}\}^b}{1+10^{-8}[s_r^\sigma(\mathbf{r})]^2}$ ，其中 $a_{2}$ =(10⁻⁸+0.1234)/0.024974、$a_{4}$ =29.790、$a_{6}$ =22.417、$a_{8}$ =12.119、$a_{10}$ =1570.1、$a_{12}$ =55.944、*b*=0.024974

- iKEDsel=22：Acharya-Bartolotti-Sears-Parr KED，$F_{\mathrm{ABSP}}^\sigma=\frac{1}{8C_{\mathrm{TF}}}[s^\sigma(\mathbf{r})]^2+1-\frac{1.412}{N^{1/3}}$

- iKEDsel=23：Gázquez-Robles KED，$F_{\mathrm{GR}}^\sigma=\frac{1}{8C_{\mathrm{TF}}}[s^\sigma(\mathbf{r})]^2+\left(1-\frac{2}{N}\right)\left(1-\frac{1.303}{N^{1/3}}+\frac{0.029}{N^{2/3}}\right)$

- iKEDsel=24：四阶梯度展开近似，

  

$$
\tau_{\mathrm{GE4}}^\sigma=\tau_{\mathrm{GEA2}}^\sigma+\frac{(6\pi^2)^{-2/3}}{540}[\rho^\sigma(\mathbf{r})]^{1/3}\left\{\left[\frac{\nabla^2\rho^\sigma(\mathbf{r})}{\rho^\sigma(\mathbf{r})}\right]^2-\frac{9}{8}\frac{\nabla^2\rho^\sigma(\mathbf{r})}{\rho^\sigma(\mathbf{r})}\left|\frac{\nabla\rho^\sigma(\mathbf{r})}{\rho^\sigma(\mathbf{r})}\right|^2+\frac{1}{3}\left|\frac{\nabla\rho^\sigma(\mathbf{r})}{\rho^\sigma(\mathbf{r})}\right|^4\right\}
$$

注意，若 *settings.ini* 中的 "uservar" 不为 0，上述所有 KED 会加上 "∇²*ρ* /uservar" 项。例如，当 iuserfunc=1200、iKEDsel=5 且 uservar=6，自定义函数对应 *τ*$_{GEA2}$+∇²*ρ* /6（对应 Tsirelson 型 ELF 和 LOL 采用的 KED，如[2.6节](sec-2-6-real-space-functions.md)所示）。

**1201** "iKEDsel" 所选 KED 与 Weizsäcker KED 之差。

**1202** "iKEDsel" 所选 KED 与 Lagrangian KED 之差。

**1203** "iKEDsel" 所选 KED 与 Lagrangian KED 之差的绝对值。

**1204** 局域温度 $T(\mathbf{r})=\frac{2\tau(\mathbf{r})}{3\rho(\mathbf{r})}$。该函数用的动能密度 *τ*(**r**) 由 "iKEDsel" 确定。相比之下，自定义函数 7 用 Lagrangian 动能密度。注意，若 *ρ* 小于 *settings.ini* 中的 "uservar" 参数，则 *T* 视为 0。

**1210** 动能泛函的势，其形式由 *settings.ini* 中的 "iKEDsel" 确定。只对闭壳层情形有效，可用于以下 KED：

iKEDsel=3：Thomas-Fermi

iKEDsel=5：二阶 GEA

iKEDsel=7：Thomas-Fermi + Weizsäcker

## **主实空间函数作为自定义函数**

出于灵活性考虑，主实空间函数也可作为自定义函数调用。若将 *settings.ini* 中的 "iuserfunc" 设为 10000+*i*，则第 *i* 个实空间函数被选为自定义函数。例如，若 "iuserfunc" 设为 10009，则第 9 个实空间函数 (ELF) 被选为自定义函数。
