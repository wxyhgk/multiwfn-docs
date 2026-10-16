# **2.6 实空间函数**

本手册中的"实空间函数 (Real space functions)"指变量为当前体系三维空间坐标的函数。实空间函数分析是 Multiwfn 最重要的功能之一，支持的实空间函数列举如下。所有波函数均假设为实型，所有单位均为**原子单位 (a.u.)**。

注意，为加快计算（特别是对大体系），在求指数函数值时（某些实空间函数除外，如 12、14 和 16），若指数小于 -40，则跳过此次求值。默认截断值足够安全，即使在定量分析中也不会造成可察觉的精度损失，你也可以关闭该处理或调整截断值，见 *settings.ini* 中的 "expcutoff"。

## **1 电子密度**

$$
\rho(\mathbf{r})=\sum_i \eta_i\left|\varphi_i(\mathbf{r})\right|^2=\sum_i \eta_i\left|\sum_\mu C_{\mu,i}\chi_\mu(\mathbf{r})\right|^2
$$

其中 $η_{i}$ 是轨道 *i* 的占据数，$\varphi$ 是轨道波函数，*χ* 是基函数。*C* 是系数矩阵，第 *i* 行第 *j* 列的元素对应轨道 *j* 相对基函数 *i* 的展开系数。电子密度的原子单位可明确写为 1/Bohr³（对应于 6.74833/Å³，因为 1 Bohr = 0.529177Å）。

当输入文件不含 GTF 信息时，该函数按 promolecular 密度计算，即简单地将体系中所有原子的内建球平均自由态原子密度叠加而成的近似分子电子密度。内建原子密度如何得到见[附录 3](sec-6-3-detail-of-built-in-atomic-densities.md)。

值得注意的是，价电子密度的分布特征比电子密度信息丰富得多，该观点在我的工作 [*Acta Phys. -Chim. Sin.*, **34**, 503 (2018)](http://www.whxb.pku.edu.cn/EN/10.3866/PKU.WHXB201709252) DOI: 10.3866/pku.Whxb201709252 中有充分讨论。

## **2 电子密度的梯度模**

$$
\left|\nabla\rho(\mathbf{r})\right|=\sqrt{\left(\frac{\partial\rho(\mathbf{r})}{\partial x}\right)^2+\left(\frac{\partial\rho(\mathbf{r})}{\partial y}\right)^2+\left(\frac{\partial\rho(\mathbf{r})}{\partial z}\right)^2}
$$

## **3 电子密度的拉普拉斯**

$$
\nabla^2\rho(\mathbf{r})=\frac{\partial^2\rho(\mathbf{r})}{\partial x^2}+\frac{\partial^2\rho(\mathbf{r})}{\partial y^2}+\frac{\partial^2\rho(\mathbf{r})}{\partial z^2}
$$

该函数的正值和负值分别对应电子密度局域 depleted（耗尽）和局域 concentrated（集中）。${\mathrm{\nabla }}^{2}\rho$ 与价层电子对互斥 (VSEPR) 模型、化学键类型、电子定域和化学反应性之间的关系已由 Bader 和许多其它研究者建立。

注意，在一些其它程序如 AIMALL 和 AIM2000 中，电子密度的拉普拉斯定义为 $(-\frac{1}{4}){\mathrm{\nabla }}^{2}\rho$ ，与 Multiwfn 给出的值差一个 -1/4 因子。

若 *settings.ini* 中的 "laplfac" 设为非默认值 1.0 以外的值，${\mathrm{\nabla }}^{2}\rho$ 会乘以该值。

Multiwfn 输出的 ${\mathrm{\nabla }}^{2}\rho$ 为原子单位，可明确写为 1 Bohr⁻⁵（对应于 24.09874 Å⁻⁵，因为 1 Bohr = 0.529177 Å）。

## **4 轨道波函数值；44 轨道概率密度**

它们分别定义为：

$$
\begin{gathered}\varphi_i(\mathbf{r})=\sum_\mu C_{\mu,i}\chi_\mu(\mathbf{r})\\ \rho_i(\mathbf{r})=\left|\varphi_i(\mathbf{r})\right|^2\end{gathered}
$$

当你从函数列表中选择这些函数时，程序会提示输入感兴趣轨道的序号。

## **5 电子自旋密度**

自旋密度定义为 alpha 与 beta 密度之差：

$$
\rho^s(\mathbf{r})=\rho^\alpha(\mathbf{r})-\rho^\beta(\mathbf{r})
$$

若 *settings.ini* 中的 "ipolarpara" 设为 1，则返回自旋极化参数函数而非自旋密度：

$$
\zeta(\mathbf{r})=\frac{\rho^\alpha(\mathbf{r})-\rho^\beta(\mathbf{r})}{\rho^\alpha(\mathbf{r})+\rho^\beta(\mathbf{r})}
$$

*ζ* 的绝对值从 0 到 1 对应局域区域从非极化到完全极化。

## **6 Hamiltonian 动能密度 *K*(r)**

动能密度不是唯一定义的，因为动能算符的期望值 $\left<\varphi\left|-(1/2)\nabla^2\right|\varphi\right>$ 可通过积分不同定义的动能密度得到。常用定义之一是：

$$
K(\mathbf{r})=-\frac{1}{2}\sum_i \eta_i \varphi_i^*(\mathbf{r})\nabla^2\varphi_i(\mathbf{r})
$$

## **7 Lagrangian 动能密度 *G*(r)**

相对 *K*(**r**)，下面给出的局域动能定义处处保证为正，因而物理意义更明确，也更常用。*G*(**r**) 又称正定动能密度。

$$
G(\mathbf{r})=\frac{1}{2}\sum_i\eta_i\left|\nabla\varphi_i(\mathbf{r})\right|^2=\frac{1}{2}\sum_i\eta_i\left\{\left(\frac{\partial\varphi_i(\mathbf{r})}{\partial x}\right)^2+\left(\frac{\partial\varphi_i(\mathbf{r})}{\partial y}\right)^2+\left(\frac{\partial\varphi_i(\mathbf{r})}{\partial z}\right)^2\right\}
$$

由于 $\nabla\rho_i=\nabla(\eta_i\varphi_i^2)=2\eta_i\varphi_i\nabla\varphi_i$ ，*G*(**r**) 有等价形式：$\frac{1}{8}\sum_i\frac{\nabla\rho_i\cdot\nabla\rho_i}{\rho_i}$ 。

*K*(**r**) 与 *G*(**r**) 通过电子密度的拉普拉斯直接关联：

$$
\nabla^2\rho(\mathbf{r})/4=G(\mathbf{r})-K(\mathbf{r})
$$

## **8 核/原子电荷产生的静电势**

$$
V_{\mathrm{nuc}}(\mathbf{r})=\sum_A\frac{Z_A}{\left|\mathbf{r}-\mathbf{R}_A\right|}
$$

其中 $R_{A}$ 和 $Z_{A}$ 分别表示原子 A 的位置矢量和核电荷。若用赝势，则 *Z* 为明确表达的电子数。当用 .chg 文件作输入时，*Z* 代表文件中记录的原子电荷（第四列），此时 $V_{\mathrm{nuc}}$ 可用于分析精确静电势与原子电荷复现的静电势之差。

注意，在核位置处该函数为无穷大，可能在程序中引起数值问题，故在这些情况下该函数恒返回 1000 而非无穷大。

## **9 电子定域函数 (ELF)**

某区域电子定域性越大，电子运动被束缚在其中的可能性越大。若电子完全定域，则它们可与外部电子区分。Bader 发现电子定域性大的区域必有大的 Fermi hole 积分值。但 Fermi hole 是六维函数，难以直观研究。Becke 和 Edgecombe 注意到球平均的同自旋条件对概率与 Fermi hole 直接相关，进而在论文 *J. Chem. Phys.*, **92**, 5397 (1990) 中提出了电子定域函数 (ELF)。*Angew. Chem. Int. Ed.*, **137**, e202504895 (2025) DOI: [10.1002/anie.202504895](https://doi.org/10.1002/anie.202504895) 是一篇很好的综述，展示了 ELF 在解密电子结构中的巨大实用价值，*Theoretical Aspects of Chemical Reactivity* (2007) 第 5 章提供了一些额外信息。

Multiwfn 采用的 ELF 是我推广到自旋极化体系的形式，介绍见我的论文 [*Acta Phys. -Chim. Sin.*](http://www.whxb.pku.edu.cn/EN/10.3866/PKU.WHXB20112786)[, 27, 2786 (2011)](http://www.whxb.pku.edu.cn/EN/10.3866/PKU.WHXB20112786)。

$$
\mathrm{ELF}(\mathbf{r})=\frac{1}{1+[D(\mathbf{r})/D_0(\mathbf{r})]^2}
$$

其中：

$$
\begin{aligned}&D(\mathbf{r})=\frac{1}{2}\sum_i\eta_i\left|\nabla\varphi_i(\mathbf{r})\right|^2-\frac{1}{8}\left[\frac{\left|\nabla\rho_\alpha(\mathbf{r})\right|^2}{\rho_\alpha(\mathbf{r})}+\frac{\left|\nabla\rho_\beta(\mathbf{r})\right|^2}{\rho_\beta(\mathbf{r})}\right]\\ &D_0(\mathbf{r})=\frac{3}{10}(6\pi^2)^{2/3}\left[\rho_\alpha(\mathbf{r})^{5/3}+\rho_\beta(\mathbf{r})^{5/3}\right]\end{aligned}
$$

对闭壳层体系，由于 $\rho_\alpha=\rho_\beta=(1/2)\rho$ ，*D* 和 $D_{0}$ 项可简化为：

$$
\begin{aligned}&D(\mathbf{r})=\frac{1}{2}\sum_i\eta_i\left|\nabla\varphi_i(\mathbf{r})\right|^2-\frac{1}{8}\frac{\left|\nabla\rho(\mathbf{r})\right|^2}{\rho(\mathbf{r})}\\ &D_0(\mathbf{r})=(3/10)(3\pi^2)^{2/3}\rho(\mathbf{r})^{5/3}\end{aligned}
$$

Savin 等人从动能角度重新解释了 ELF，见 *Angew. Chem. Int. Ed. Engl.*, **31**, 187 (1992)，这使 ELF 对 Kohn-Sham DFT 波函数乃至多组态波函数也有意义。*D*(**r**) 第一项可视为 KS-DFT 理论定义的非相互作用电子体系的精确动能密度，即 $\tau_{\mathrm{S}}(\mathbf{r})=(1/2)\sum_i\eta_i\left|\nabla\varphi_i(\mathbf{r})\right|^2$ ，而第二项等价于 Weizsäcker 动能密度 $\tau_{\mathrm{W}}(\mathbf{r})=(1/8)\left|\nabla\rho\right|^2/\rho$ ，因此 $D(\mathbf{r})=\tau_{\mathrm{S}}(\mathbf{r})-\tau_{\mathrm{W}}(\mathbf{r})$ 揭示了由 Pauli 排斥导致的超额动能密度，称为 Pauli 动能密度。$D_{0}$ (**r**) 可解释为 Thomas-Fermi 动能密度 *τ*$_{TF}$，即非相互作用均匀电子气的精确动能密度。由于 $D_{0}$ (**r**) 在 ELF 中作为参考引入，ELF 揭示的实际是*相对*定域程度。

ELF 取值范围为 \[0,1\]。大的 ELF 值意味着电子高度定域，表明存在共价键、孤对或原子的内层。ELF 已广泛用于各类体系，如有机和无机小分子、原子晶体、配位化合物、团簇，也用于不同问题，如揭示原子壳层结构、化学键分类、验证电荷移键、研究芳香性。

> **注**
>
> 有人质疑 Multiwfn 对多组态波函数的 ELF 实现。以下段落是我在电子邮件中对一位 Multiwfn 用户的回复，论证了 Multiwfn 所用上面给出的 ELF 定义的合理性：
>
> 应注意 ELF 有不同解释，或说有不同的 ELF 推导方式。起初 Becke 等基于 HF 波函数的平均 Fermi hole 推导了 ELF，因此 ELF 的原始形式与 MP2、CASSCF、CCSD 等多组态波函数不兼容（它甚至不严格适用于 DFT 波函数！）。我注意到有人沿 Becke 的原始思想把 ELF 推广到多组态波函数，但相当复杂且难以实现，故 Multiwfn 未采用。
>
> 相比之下，对多组态波函数，Multiwfn 仅基于其自然轨道计算 ELF，如手册[2.6节](sec-2-6-real-space-functions.md)所述。我相信这绝非错误而是物理上合理的。在 *Angew. Chem. Int. Ed. Engl.*, 31, 187 (1992) 中，Savin 等从动能角度重新解释了 ELF 的物理意义，这为只要动能密度可得就可计算任何波函数的 ELF 铺平了道路。沿此观点，ELF 表达式中涉及的三种动能密度都基于自然轨道计算。虽然该实现的结果与上述（即基于多组态波函数严格推导 Fermi hole 的）实现不完全相同，但它也是严格且物理上有意义的。
>
> 简言之，对多组态波函数，ELF 的实现不是唯一的，取决于人们如何看待 ELF。

注意 ELF 有个缺陷，有时 **r** 从分子边界向外时，*D*(**r**) 比 $D_{0}$ (**r**) 下降更快，ELF 达到 1（完全定域）。为克服该问题，Multiwfn 自动给 *D*(**r**) 加一个极小值 10⁻⁵，该处理几乎不影响感兴趣区域的 ELF 值。你也可将 *settings.ini* 中的 "ELF_addminimal" 改为 0 以关闭该处理。

Tsirelson 和 Stash 在 *Chem. Phys. Lett.*, **351**, 142 (2002) 中提出了近似版 ELF，其中 *D*(**r**) 中的实际动能项用 Kirzhnits 型二阶梯度展开代替，即：

$$
(1/2)\sum_i\eta_i\left|\nabla\varphi_i(\mathbf{r})\right|^2\approx\tau_{\mathrm{TA}}(\mathbf{r})+(1/72)\left|\nabla\rho(\mathbf{r})\right|^2/\rho(\mathbf{r})+(1/6)\nabla^2\rho(\mathbf{r})
$$

从而 ELF 完全不依赖波函数，可用于分析 X 射线衍射数据的电子密度。当然，Tsirelson 的 ELF 也可用于分析量子化学计算的电子密度，但因动能项引入近似而不如 Becke 定义的 ELF 好，不过一般仍可恢复定性结论。若想用 Tsirelson 定义的 ELF，将 *settings.ini* 中的 "ELFLOL_type" 由 0 改为 1。

若 "ELFLOL_type" 设为 2，将用另一种形式：

$$
\frac{1}{1+D(\mathbf{r})/D_0(\mathbf{r})}
$$

与 ELF 密切相关的实空间函数是 SCI 指数，它对识别强共价键很有用，见[2.7节](sec-2-7-user-defined-real-space-function.md)自定义函数 37 的介绍。

## **10 定域轨道定位函数 (LOL)**

这是另一个类似 ELF 用于定位高定域区域的函数，由 Schmider 和 Becke 在论文 *J. Mol. Struct. (THEOCHEM)*, **527**, 51 (2000) 中定义：

$$
\mathrm{LOL}(\mathbf{r})=\frac{\tau(\mathbf{r})}{1+\tau(\mathbf{r})}
$$

其中：

$$
\tau(\mathbf{r})=\frac{D_0(\mathbf{r})}{(1/2)\sum_i\eta_i\left|\nabla\varphi_i(\mathbf{r})\right|^2}
$$

自旋极化体系和闭壳层体系的 $D_{0}$ (**r**) 定义与 ELF 中相同。

LOL 与 ELF 表达式相似。实际上，LOL 与 ELF 突出的化学重要区域一般定性可比。强烈推荐阅读我的综述 *Angew. Chem. Int. Ed.*, **137**, e202504895 (2025) DOI: [10.1002/anie.202504895](https://doi.org/10.1002/anie.202504895)，其中例证了 LOL 重要的实用价值。显然，LOL 可像 ELF 那样从动能角度解释，但 LOL 也可从定域轨道角度解释。小的（大的）LOL 值通常出现在定域轨道的边界（内部）区域，因为该区域轨道波函数的梯度大（小）。LOL 取值范围与 ELF 相同，即 \[0,1\]。

Multiwfn 也支持 Tsirelson 和 Stash 定义的近似版 LOL (*Acta. Cryst.*, **B58**, 780 (2002))，即实际动能项用二阶梯度展开代替，如同他们对 ELF 所做的那样。将 "ELFLOL_type" 设为 1 可激活该 Tsirelson 版 LOL。

出于特殊原因，若 *settings.ini* 中的 "ELFLOL_type" 由 0 改为 2，将用另一种形式：$\mathrm{LOL}(\mathbf{r})=\frac{1}{1+[1/\tau(\mathbf{r})]^2}$ 。

## **11 局域信息熵**

信息熵是对信息的量化，该理论由 Shannon 在研究噪声信道中的信息传输时提出，如今其应用已大幅扩展到其它领域，包括理论化学。例如，Aslangul 等人尝试通过最小化信息熵将双原子和三原子分子分解为互斥空间 (*Adv. Quantum Chem.*, **6**, 93 (1972))，Parr 等人讨论了信息熵与原子划分及分子相似性的关系 (*J. Phys. Chem. A*, **109**, 3957 (2005))，Noorizadeh 和 Shakerzadeh 建议用信息熵研究芳香性 (*Phys. Chem. Chem. Phys.*, **12**, 4742 (2010))。Shannon 熵公式为：

$$
S(x)=-\int P(x)\ln P(x)\,\mathrm{d}x
$$

对化学体系，若将 *P*(x) 替换为 *ρ*(**r**)/*N*，则被积函数可称为电子的局域信息熵：

$$
S(\mathbf{r})=-\frac{\rho(\mathbf{r})}{N}\ln\frac{\rho(\mathbf{r})}{N}
$$

其中 *N* 为当前体系的总电子数。对全空间积分该函数得信息熵。

## **12 总静电势 (ESP)**

$$
V_{\mathrm{ESP}}(\mathbf{r})=V_{\mathrm{nuc}}(\mathbf{r})+V_{\mathrm{ele}}(\mathbf{r})=\sum_A\frac{Z_A}{\left|\mathbf{r}-\mathbf{R}_A\right|}-\int\frac{\rho(\mathbf{r}')}{\left|\mathbf{r}-\mathbf{r}'\right|}\mathrm{d}\mathbf{r}'
$$

其中 *Z* 是核电荷，序号 *A* 遍历所有原子。若用赝势，则 $Z_{A}$ 为明确表达的电子数。ESP 的原子单位 (a.u.) 是 Hartree/e，其中 e 是元电荷。其它常用单位是 eV/e 和 kcal/(mol⋅e)，但为简单起见，在 Multiwfn 中它们分别打印为 eV 和 kcal/mol。以 eV/e 为单位的值等于以 SI 单位 (J/C) 计的值。

该函数衡量置于 **r** 处的单位点电荷与当前体系（不考虑电荷极化和转移）的静电相互作用能。正（负）值意味着当前位置由核（电子）电荷主导。分子静电势 (ESP) 长期以来广泛用于预测亲核和亲电位点。它在研究氢键、卤键、分子识别和芳香化合物的分子间相互作用中也有价值。此外，基于统计分析，Murray 等人发现了一组称为 GIPF 的函数，见 *J. Mol. Struct. (THEOCHEM)*, **307**, 55，它将分子表面 ESP 与宏观性质联系起来。……

顺便说，若你只想得到电子贡献的静电势，即 $V_{\mathrm{ele}}$ (**r**)，可用第 14 个自定义函数。若想在求 $V_{\mathrm{ESP}}$ (**r**) 时略去特定核的贡献，用第 39 个自定义函数。细节见[2.7节](sec-2-7-user-defined-real-space-function.md)相应条目。

> **注 1**
>
> 目前 Multiwfn 内部有两套计算 ESP 的代码，可由 *settings.ini* 中的 "iESPcode" 选择。iESPcode=1 对应 Tian Lu 编写的旧的慢代码，iESPcode=2（默认）对应 Jun Zhang 基于其 LIBRETA 电子排斥积分库提供的新的快代码。此外，在许多分析中，若你用 .fch/fchk 作输入文件且机器上装有 Gaussian，可让 Multiwfn 调用 Gaussian 包中的 cubegen 工具计算 ESP，若你的 CPU 核数少于 10，速度甚至比 "iESPcode=2" 更快，细节见[5.7节](sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md)。

> **注 2**
>
> Multiwfn 中有些功能会修改轨道占据。例如，用户可用主功能 6 的子功能 26 手动修改特定轨道的占据数。只有用内部代码 "iESPcode=1" 计算的 ESP 才直接反映占据修改的影响。用 "iESPcode=2" 时，为在 ESP 计算中体现修改的影响，应先将修改后的波函数导出为 .wfn/wfx/molden/mwfn（经主功能 100 的子功能 2），再重启 Multiwfn 并载入该文件。

## **13 约化密度梯度 (RDG)**

RDG 和 *sign*(*λ*₂)*ρ* 是揭示弱相互作用区域的一对非常重要函数，它们在 NCI 方法中联合使用，细节见 *J. Am. Chem. Soc.*, **132**, 6498 (2010)，应用例子见[3.23.1节](sec-3-23-visual-study-of-weak-interaction.md#3231-非共价相互作用-noncovalent-interaction-nci分析-1)。RDG 定义为：

$$
\mathrm{RDG}(\mathbf{r})=\frac{1}{2(3\pi^2)^{1/3}}\frac{\left|\nabla\rho(\mathbf{r})\right|}{\rho(\mathbf{r})^{4/3}}
$$

注意 *settings.ini* 中有个参数 "RDG_maxrho"，若设为 *x*，则电子密度大于 *x* 处的 RDG 函数会被设为任意大值 (100.0)。该机制使查看弱相互作用区域等值面时能屏蔽不感兴趣的区域。默认 *x* 为 0.05，将该参数设为 0 可取消该处理。

## **14 promolecular 近似下的约化密度梯度 (RDG)**

弱相互作用对大分子的构象、蛋白与配体的结合模式有显著影响；但对如此巨大的体系用 *ab initio* 复现电子密度并计算 RDG 的格点数据总是太耗时。幸运的是，发现 promolecular 密度下的弱相互作用分析仍是合理的。promolecular 密度简单地叠加自由态原子的电子密度，故求值极快：

$$
\rho^{\mathrm{pro}}(\mathbf{r})=\sum_A\rho_A^{\mathrm{free,fit}}(\mathbf{r}-\mathbf{R}_A)
$$

其中 ${\rho}_{A}^{\mathrm{free,fit}}(\mathbf{r})$ 是原子 *A* 的预拟合球平均电子密度。H\~Lr 的原子密度是 Multiwfn 的内建数据，其中 H\~Ar 的数据取自 *J. Am. Chem. Soc.*, **132**, 6498 (2010) 的补充材料，其它元素的按[附录 3](sec-6-3-detail-of-built-in-atomic-densities.md)所述求得。对重于 Lr 的元素目前没有 promolecular 近似。

> **注**
>
> 出于效率考虑，若 H、C、N 或 O 原子对某点函数值的贡献小于 0.00001，则不计算该贡献，对大体系该处理使效率提高数倍而结果几乎不受影响。将 *settings.ini* 中的 "atomdenscut" 设为 0 可关闭该处理。

*settings.ini* 中的参数 "RDGprodens_maxrho" 是 promolecular 近似下 "RDG_maxrho" 的对应物。

## **15 *sign*(*λ*₂)*ρ***

$$
\Omega(\mathbf{r})=sign[\lambda_2(\mathbf{r})]\rho(\mathbf{r})
$$

其中 *sign*\[*λ*₂(**r**)\] 指位置 **r** 处电子密度 Hessian 矩阵第二大本征值的符号。

## **16 promolecular 近似下的 *sign*(*λ*₂)*ρ***

用于求 *sign*\[*λ*₂(**r**)\] 的实际电子密度用 promolecular 电子密度近似，见实空间函数 14 的描述。

## **17 交换-相关密度、相关 hole 和相关因子**

这些函数涉及高级课题，为阐明其物理意义并避免各种论文所用符号的混淆，我认为值得用更多篇幅介绍理论背景。更详细的讨论请参考 *A Chemist's Guide to Density Functional Theory 2ed* 第 2 章和 *Methods of molecular quantum mechanics (2ed, McWeeny)* 第 5 章。

======= **理论基础** ======

***对密度 (Pair density)*** 定义为：

$$
\pi(\mathbf{r}_1,\mathbf{r}_2)=N(N-1)\int\cdots\int\left|\Psi(\mathbf{x}_1,\mathbf{x}_2,...\mathbf{x}_N)\right|^2\mathrm{d}\sigma_1\mathrm{d}\sigma_2\mathrm{d}\mathbf{x}_3\mathrm{d}\mathbf{x}_4...\mathrm{d}\mathbf{x}_N
$$

其中 Ψ 是体系波函数，**r** 是空间坐标，σ 是自旋坐标，**x** 是空间-自旋坐标。对密度表示在 $\mathbf{r}_{1}$ 找到一个电子同时在 $\mathbf{r}_{2,}$ 找到另一个电子的概率，不论自旋类型。若对全空间对对密度做双重积分，得 *N*(*N*-1)，反映当前体系有 *N*(*N*-1) 个电子对的本质。显然，对密度可分解为不同自旋类型电子对的贡献：

$$
\pi(\mathbf{r}_1,\mathbf{r}_2)=\pi^{\alpha\alpha}(\mathbf{r}_1,\mathbf{r}_2)+\pi^{\alpha\beta}(\mathbf{r}_1,\mathbf{r}_2)+\pi^{\beta\alpha}(\mathbf{r}_1,\mathbf{r}_2)+\pi^{\beta\beta}(\mathbf{r}_1,\mathbf{r}_2)
$$

若电子运动完全相互独立，则在 $\mathbf{r}_{1}$ 找到自旋 σ₁ 的电子同时在 $\mathbf{r}_{2}$ 找到自旋 σ₂ 的电子的概率密度应简单地为 $\rho^{\sigma_1}(\mathbf{r}_1)\rho^{\sigma_2}(\mathbf{r}_2)$ 。当然，现实中电子总是相互作用的，运动相关。对密度因而应由***交换-相关密度 (exchange-correlation density)*** **$\Gamma$** 修正：

$$
\pi^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)=\rho^{\sigma_1}(\mathbf{r}_1)\rho^{\sigma_2}(\mathbf{r}_2)+\Gamma_{\mathrm{XC}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)
$$

若已知自旋 σ₁ 的电子出现在 $\mathbf{r}_{1}$ ，则在 $\mathbf{r}_{2}$ 找到自旋 σ₂ 的另一电子的概率称为***条件概率 (conditional probability)***（该函数又称 **Lennard-Jones 函数**）：

$$
\Omega^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)=\frac{\pi^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)}{\rho^{\sigma_1}(\mathbf{r}_1)}=\rho^{\sigma_2}(\mathbf{r}_2)+\frac{\Gamma_{\mathrm{XC}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)}{\rho^{\sigma_1}(\mathbf{r}_1)}
$$

***相关 hole (correlation hole)*** 揭示当自旋 σ₁ 的电子出现在 $\mathbf{r}_{1}$ 时，由于电子相关效应在 $\mathbf{r}_{2}$ 找到自旋 σ₂ 的另一电子的概率降低：

$$
h_{\mathrm{XC}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)=\frac{\Gamma_{\mathrm{XC}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)}{\rho^{\sigma_1}(\mathbf{r}_1)}=\Omega^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)-\rho^{\sigma_2}(\mathbf{r}_2)=\frac{\pi^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)}{\rho^{\sigma_1}(\mathbf{r}_1)}-\rho^{\sigma_2}(\mathbf{r}_2)
$$

***相关因子 (correlation factor)*** 是与相关 hole 密切相关的函数：

$$
f_{\mathrm{XC}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)=\frac{h_{\mathrm{XC}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)}{\rho^{\sigma_2}(\mathbf{r}_2)}=\frac{\Gamma_{\mathrm{XC}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)}{\rho^{\sigma_1}(\mathbf{r}_1)\rho^{\sigma_2}(\mathbf{r}_2)}
$$

总之，可写出：

$$
\pi^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)=\rho^{\sigma_1}(\mathbf{r}_1)\rho^{\sigma_2}(\mathbf{r}_2)+\rho^{\sigma_1}(\mathbf{r}_1)h_{\mathrm{XC}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)=\rho^{\sigma_1}(\mathbf{r}_1)\rho^{\sigma_2}(\mathbf{r}_2)[1+f_{\mathrm{XC}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)]
$$

$\Gamma_{\mathrm{XC}}$ 可分解为交换相关（又称 Fermi 相关）部分 $\Gamma_{\mathrm{X}}$ 与库仑相关部分 $\Gamma_{\mathrm{C}}$ 之和，因此 $h_{\mathrm{XC}}$ 可直接分解为*交换 hole* $h_\mathrm{X}$（又称 Fermi hole）与*库仑 hole* $h_\mathrm{C}$。同样，$f_{\mathrm{XC}}$ 可分解为 $f_\mathrm{X}$ 与 $f_\mathrm{C}$：

$$
\begin{gathered}\Gamma_{\mathrm{XC}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)=\Gamma_{\mathrm{X}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)+\Gamma_{\mathrm{C}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)\\ h_{\mathrm{XC}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)=h_{\mathrm{X}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)+h_{\mathrm{C}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)\\ f_{\mathrm{XC}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)=f_{\mathrm{X}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)+f_{\mathrm{C}}^{\sigma_1\sigma_2}(\mathbf{r}_1,\mathbf{r}_2)\end{gathered}
$$

Fermi 相关只存在于同自旋电子之间；而库仑相关存在于任何两个电子之间。Fermi 相关远比库仑相关重要，即使在 Hartree-Fock 水平，由于 Slater 行列式的反对称要求，Fermi 相关总是很好地体现，而库仑完全被略去。只有 post-HF 波函数能同时体现 Fermi 和库仑相关效应。通常我们只关注 Fermi hole 而忽略库仑 hole。

只考虑交换相关或库仑相关时的对密度和条件概率也很容易得到。

易证 $h_\mathrm{X}$ 对全空间积分为严格 -1，故 Fermi 相关完美避免了可能显著升高体系能量的自配对问题；而 $h_\mathrm{C}$ 的积分为 0，这主要是库仑相关对体系能量影响较小的原因。

自旋为 σ 的电子（不论另一个电子的自旋）的总 π、Ω、$\Gamma_{\mathrm{XC}}$（或 $\Gamma_{\mathrm{X}}$、$\Gamma_{\mathrm{C}}$）和 $h_{\mathrm{XC}}$（或 $h_\mathrm{X}$、$h_\mathrm{C}$）可定义为：
$$
\begin{gathered}\pi^{\sigma,\mathrm{tot}}(\mathbf{r}_1,\mathbf{r}_2)=\pi^{\alpha\alpha}(\mathbf{r}_1,\mathbf{r}_2)+\pi^{\alpha\beta}(\mathbf{r}_1,\mathbf{r}_2)\\ \Omega^{\sigma,\mathrm{tot}}(\mathbf{r}_1,\mathbf{r}_2)=\Omega^{\alpha\alpha}(\mathbf{r}_1,\mathbf{r}_2)+\Omega^{\alpha\beta}(\mathbf{r}_1,\mathbf{r}_2)\\ \Gamma_{\mathrm{XC}}^{\sigma,\mathrm{tot}}(\mathbf{r}_1,\mathbf{r}_2)=\Gamma_{\mathrm{XC}}^{\alpha\alpha}(\mathbf{r}_1,\mathbf{r}_2)+\Gamma_{\mathrm{XC}}^{\alpha\beta}(\mathbf{r}_1,\mathbf{r}_2)\\ h_{\mathrm{XC}}^{\sigma,\mathrm{tot}}(\mathbf{r}_1,\mathbf{r}_2)=h_{\mathrm{XC}}^{\alpha\alpha}(\mathbf{r}_1,\mathbf{r}_2)+h_{\mathrm{XC}}^{\alpha\beta}(\mathbf{r}_1,\mathbf{r}_2)\end{gathered}
$$

======= **技术细节** ======

对单行列式波函数，α 电子的交换-相关密度可明确写为：

$$
\Gamma_{\mathrm{XC}}^{\alpha,\mathrm{tot}}(\mathbf{r}_1,\mathbf{r}_2)=\Gamma_{\mathrm{XC}}^{\alpha\alpha}(\mathbf{r}_1,\mathbf{r}_2)=-\sum_{i\in\alpha}^{\mathrm{occ}}\sum_{j\in\alpha}^{\mathrm{occ}}\varphi_i^*(\mathbf{r}_1)\varphi_j^*(\mathbf{r}_2)\varphi_j(\mathbf{r}_1)\varphi_i(\mathbf{r}_2)
$$

注意对此类波函数 $\Gamma_{\mathrm{XC}}^{\alpha\beta}(\mathbf{r}_1,\mathbf{r}_2)=\Gamma_{\mathrm{XC}}^{\beta\alpha}(\mathbf{r}_1,\mathbf{r}_2)=0$。β 电子的表达式只需将 α 换为 β，下同。

对 post-HF 波函数，精确求对密度需要二粒子密度矩阵 (2PDM)。不幸的是，2PDM 很难得到，包括 Gaussian 在内的主流量子化学程序都不能直接输出。在 Multiwfn 中，post-HF 波函数的交换-相关密度用自然轨道形式近似求得。注意近似方法不是唯一的，讨论见 *J. Chem. Theory Comput.*, **6**, 2736 (2010)。其中最流行的形式由 Müller 首先推导，Multiwfn 目前实现如下。见 *Phys. Lett. A*, **105**, 446 (1984)，另见 *Mol. Phys.*, **100**, 401 (2002)的广泛讨论（特别是方程 32）。

$$
\Gamma_{\mathrm{XC,approx}}^{\alpha,\mathrm{tot}}(\mathbf{r}_1,\mathbf{r}_2)=-\sum_{i\in\alpha}\sum_{j\in\alpha}\sqrt{\eta_i\eta_j}\varphi_i^*(\mathbf{r}_1)\varphi_j^*(\mathbf{r}_2)\varphi_j(\mathbf{r}_1)\varphi_i(\mathbf{r}_2)
$$

显然，若自然自旋轨道的占据数为整数（0 或 1），则 ${\Gamma}_{\mathrm{XC,approx}}^{\alpha\mathrm{,tot}}$ 约化为单行列式形式，故 ${\Gamma}_{\mathrm{XC,approx}}^{\alpha\mathrm{,tot}}$ 可视为求交换-相关密度的一般形式。注意 post-HF 波函数已考虑异自旋电子间的库仑相关，但无法从 ${\Gamma}_{\mathrm{XC,approx}}^{\alpha\mathrm{,tot}}$ 中分离出 ${\Gamma}_{\mathrm{XC,approx}}^{\alpha\alpha}$ 和 ${\Gamma}_{\mathrm{XC,approx}}^{\alpha\beta}$ 。

post-HF 波函数 $\Gamma$ 的纯交换部分可近似求为（当然，αβ 电子对间没有交换相关）：

$$
\Gamma_{\mathrm{X,approx}}^{\alpha,\mathrm{tot}}(\mathbf{r}_1,\mathbf{r}_2)=\Gamma_{\mathrm{X,approx}}^{\alpha\alpha}(\mathbf{r}_1,\mathbf{r}_2)=-\sum_{i\in\alpha}\sum_{j\in\alpha}\eta_i\eta_j\varphi_i^*(\mathbf{r}_1)\varphi_j^*(\mathbf{r}_2)\varphi_j(\mathbf{r}_1)\varphi_i(\mathbf{r}_2)
$$

故 $\Gamma$ 的纯库仑部分可求为（包括 αα 和 αβ 对贡献）：

$$
\begin{aligned}\Gamma_{\mathrm{C,approx}}^{\alpha,\mathrm{tot}}(\mathbf{r}_1,\mathbf{r}_2)&=\Gamma_{\mathrm{XC,approx}}^{\alpha,\mathrm{tot}}(\mathbf{r}_1,\mathbf{r}_2)-\Gamma_{\mathrm{X,approx}}^{\alpha\alpha}(\mathbf{r}_1,\mathbf{r}_2)\\ \quad\quad&=\sum_{i\in\alpha}\sum_{j\in\alpha}\left[(\eta_i\eta_j-\sqrt{\eta_i\eta_j})\varphi_i^*(\mathbf{r}_1)\varphi_j^*(\mathbf{r}_2)\varphi_j(\mathbf{r}_1)\varphi_i(\mathbf{r}_2)\right]\end{aligned}
$$

既然已有计算 $\Gamma_{\mathrm{XC}}$ 项的明确表达式，根据它们与 $\Gamma_{\mathrm{XC}}$ 的关系易求前文介绍的其它量。注意 $\rho^\sigma(\mathbf{r})=\sum_{i\in\sigma}\eta_i\left|\varphi_i(\mathbf{r})\right|^2$ 。

附言：可证 ${\Gamma}_{\mathrm{XC,approx}}^{\alpha\mathrm{,tot}}({\mathbf{r}}_{1},{\mathbf{r}}_{2})$ 也严格满足对 $r_{2}$ 在全空间积分为 $-{\rho}^{\alpha}({\mathbf{r}}_{1})$ 的要求。但一般地，对 ${\Gamma}_{\mathrm{X,approx}}^{\alpha\mathrm{,tot}}({\mathbf{r}}_{1},{\mathbf{r}}_{2})$ 和 ${\Gamma}_{\mathrm{C,approx}}^{\alpha\mathrm{,tot}}({\mathbf{r}}_{1},{\mathbf{r}}_{2})$ 在全空间积分 $r_{2}$ 会偏离 $-{\rho}^{\alpha}({\mathbf{r}}_{1})$ 和 0，而这两者分别是精确形式的 ${\Gamma}_{\mathrm{X}}^{\alpha\mathrm{,tot}}$ 和 ${\Gamma}_{\mathrm{C}}^{\alpha\mathrm{,tot}}$ 的基本性质。

======= **用法** ======

在 Multiwfn 中，$\mathbf{r}_{1}$ 视为参考点，$\mathbf{r}_{2}$ 视为变量，要定义参考点坐标，只需在启动前修改 *settings.ini* 中的 "refxyz"。

*settings.ini* 中的 "paircorrtype" 参数控制计算 $\Gamma$ 时考虑哪类相关效应。由于相关 hole 和相关因子基于 $\Gamma$ 计算，该设置也影响它们。对单行列式波函数，=1 与 =3 等价而 =2 无意义，因为库仑相关被完全略去。

- **=1：** 只考虑交换相关

- **=2：** 只考虑库仑相关

- **=3：** 同时考虑交换和库仑相关

*settings.ini* 中的 "pairfunctype" 参数控制实空间函数 17 计算哪个函数和哪个自旋，见下，括号中为单行列式波函数的情形。当然，对闭壳层体系，α 自旋结果与 β 自旋结果完全相同。注意 post-HF 波函数的相关因子无定义。

- **=1：** $h^{α,\mathrm{tot}}$ ( $h^{α,α}$ )

- **=2：** $h^{β,\mathrm{tot}}$ ( $h^{β,β}$ )

- **=4：** 未定义 (*f*$^{α,α}$)

- **=5：** 未定义 (*f*$^{β,β}$)

- **=7：** Γ$^{α,tot}$ (Γ$^{α,α}$)

- **=8：** Γ$^{β,tot}$ (Γ$^{β,β}$)

- **=10：** paircorrtype =1 时为 π$^{α,α}$ (π$^{α,α}$)

- **=11：** paircorrtype =1 时为 π$^{β,β}$ (π$^{β,β}$)

- **=12：** π$^{any,any}$ (π$^{any,any}$)

例如，若 paircorrtype=1 且 pairfunctype=2，对 post-HF 波函数，所求为 $h_X^{\beta,\mathrm{tot}}(\mathbf{r}_1,\mathbf{r}_2)$ ，因 βα 电子对没有交换相关，它等价于 $h_{\mathrm{X}}^{\beta\beta}(\mathbf{r}_1,\mathbf{r}_2)$。该量可解释为出现在 $\mathbf{r}_{1}$ 的 β 电子在 $\mathbf{r}_{2}$ 处引起的 Fermi hole。

## **18 平均局域电离能**

平均局域电离能记为 (*Can. J. Chem.*, **68**, 1440 (1990))：

$$
\bar{I}(\mathbf{r})=\frac{\sum_i\rho_i(\mathbf{r})\left|\varepsilon_i\right|}{\rho(\mathbf{r})}
$$

其中 $ρ_{i}$(**r**) 和 $ε_{i}$ 分别为第 *i* 个分子轨道的电子密度函数和轨道能量。Hartree-Fock 和 B3LYP 等典型 DFT 泛函都适合计算 $\bar{I}$ 。$\bar{I}$ 值越低表明该点电子束缚越弱。$\bar{I}$ 用途广泛，例如揭示原子壳层结构、度量电负性、预测 p$K_{a}$ 、量化局域极化率和硬度，但最重要的可能是预测亲电或自由基进攻的反应位点。已证明 vdW 表面上 ALIE 的极小值是揭示哪些原子更可能是亲电或自由基进攻优先位点的良好指标。$\bar{I}$ 还有许多潜在用途等待进一步发掘。Politzer 等人对 $\bar{I}$ 给出了很好的综述，见 *J. Mol. Model.*, **16**, 1731 (2010) 和 *Theoretical Aspects of Chemical Reactivity* (2007) 第 8 章。

由于 $\bar{I}$ 依赖于轨道能量，而 post-HF 波函数的轨道能量无定义，故用 post-HF 波函数时 $\bar{I}$ 处处简单输出为 0。

若 *settings.ini* 中的参数 "iALIEdecomp" 设为 1，在主功能 1 中不仅输出 $\bar{I}$ ，还输出每个占据 MO 的贡献，MO *i* 的贡献定义为：

$$
\bar{I}_i(\mathbf{r})=\frac{\rho_i(\mathbf{r})\left|\varepsilon_i\right|}{\rho(\mathbf{r})}
$$

## **19 源函数**

源函数由 Bader 和 Gatti 提出，见 *Chem. Phys. Lett.*, **287**, 233 (1998)。

$$
SF(\mathbf{r},\mathbf{r}')=-\frac{\nabla^2\rho(\mathbf{r}')}{4\pi\left|\mathbf{r}-\mathbf{r}'\right|}
$$

可证：

$$
\rho(\mathbf{r})=\int SF(\mathbf{r},\mathbf{r}')\mathrm{d}\mathbf{r}'
$$

其中 **r'** 遍历整个空间。该方程表明 *SF*(**r**,**r**') 代表 **r'** 处电子拉普拉斯对 **r** 处电子密度的影响。若 **r'** 处电子集中（即拉普拉斯为负，也意味着势能主导动能），则 **r'** 是 **r** 处电子密度的源；反之，若 **r'** 处电子 depleted，则 **r'** 降低 **r** 处的电子密度。若上式积分范围限于局域区域 Ω 并得到值 S(**r**,Ω)，则 S(**r**,Ω)/*ρ*(**r**)×100% 可视为区域 Ω 对 **r** 处电子密度的贡献。源函数有许多用途，当用它讨论成键问题时，通常取键临界点为 **r**。Gatti 在 *Struct. & Bond.*, **147**, 193 (2010) 对源函数的理论背景和应用给出了非常全面的综述。

在 Multiwfn 中，源函数有两种模式：(1) 若 *settings.ini* 中的 "srcfuncmode" 设为 1，则 **r'** 视为变量而 **r** 视为固定的参考点，其坐标由 *settings.ini* 中的 "refxyz" 确定。这是默认模式，用于研究各处电子拉普拉斯对特定点的影响；(2) 若 "srcfuncmode" 设为 2，则 **r** 为变量而 **r'** 为参考点，用于研究特定点处电子拉普拉斯对各处的影响。

当 **r**=**r**' 时，该函数返回 −∇²*ρ*(**r**')/0.001 以避免数值问题。

## **20,21 电子离域范围函数 EDR(r;*d*)和轨道重叠距离函数 D(r)**

> **注**
>
> 本节内容及 *EDR*(**r**;*d*) 和 *D*(**r**) 的全部分析代码由 Arshad Mehmood 慷慨贡献，再由 Tian Lu 稍作改编。

电子离域范围函数 *EDR*(**r**;*d*) (*J. Chem. Phys.*, **141**, 144104 (2014); *J. Chem. Theory Comput.*, **12**, 3185 (2016); *Angew. Chem. Int. Ed.*, **56**, 6878 (2017)) 量化波函数中 **r** 处电子占据尺寸为 *d* 的轨道瓣的程度。*EDR*(**r**;*d*) 由非局域单粒子约化密度矩阵 (1-RDM) $\gamma(\mathbf{r},\mathbf{r}')=\sum_i\eta_i\varphi(\mathbf{r})\varphi(\mathbf{r}')$ 构建为：

$$
\begin{gathered}EDR(\mathbf{r};d)=\int g_d(\mathbf{r},\mathbf{r}')\gamma(\mathbf{r},\mathbf{r}')\mathrm{d}\mathbf{r}'\\ g_d(\mathbf{r},\mathbf{r}')=\left(\frac{2}{\pi d^2}\right)^{3/4}\rho^{-1/2}(\mathbf{r})\exp\left(-\frac{\left|\mathbf{r}-\mathbf{r}'\right|^2}{d^2}\right)\end{gathered}
$$

这里 *ρ*(**r**) 是点 **r** 处的电子密度。前置因子保证 EDR 介于 -1 与 +1 之间。Multiwfn 实现在格点上求 EDR，对距离 *d* 用单个全局输入值。例子见[4.5.6节](sec-4-5-generate-grid-data-and-view-isosurface-map.md#456-研究阴离子水二聚体的电子离域范围函数-edrrd)。

每点处轨道重叠距离函数 *D*(**r**)=$\mathrm{argmax}_{d}$ *EDR*(**r**;*d*) 对应使 *EDR*(**r**;*d*) 最大的距离 *d*。小 *D*(**r**) 的紧凑、化学"硬"区域与大 *D*(**r**) 的弥散、化学"软"区域得以区分。价电子 *D*(**r**) 的原子平均补充了原子部分电荷得到的信息。在密度等值面上绘制 *D*(**r**) 及对此类表面的定量分析补充了分子静电势。Multiwfn 实现在距离网格 $d_{i}$ 上求 *EDR*(**r**; $d_{i}$ )，再用三点数值拟合找最大值。[4.5.7节](sec-4-5-generate-grid-data-and-view-isosurface-map.md#457-研究硫代甲酸的轨道重叠距离函数-dr)和[4.12.8节](sec-4-12-quantitative-analysis-of-molecular-surface.md#4128-硫代甲酸分子表面上轨道重叠距离函数-orbital-overlap-distance-function-dr的定量分析)展示了示例计算。

## **22, 23 独立梯度模型 (IGM) 方法定义的 δ*g* 函数**

δ*g* 函数在独立梯度模型 (IGM) 方法的原始论文 (*Phys. Chem. Chem. Phys.*, **19**, 17928 (2017)) 中定义如下：

$$
\delta g(\mathbf{r})=g^{\mathrm{IGM}}(\mathbf{r})-g(\mathbf{r})=\left|\sum_A \mathrm{abs}[\nabla\rho_A(\mathbf{r})]\right|-\left|\sum_A\nabla\rho_A(\mathbf{r})\right|
$$

其中 $ρ_{A}$ 代表原子 *A* 的原子密度，abs() 算符使三个梯度分量各取绝对值。具体地，Multiwfn 支持两种计算 δ*g* 的方式：

- 实空间函数 22：对应 promolecular 近似下算得的 δ*g*，即 $ρ_{A}$ 对应孤立态原子 *A* 的球形密度，此时输入文件只需提供几何信息，因为原子密度是 Multiwfn 的内建数据（细节见[附录 3](sec-6-3-detail-of-built-in-atomic-densities.md)）。

- 实空间函数 23：对应基于实际分子电子密度 Hirshfeld 划分算得的 δ*g*，故输入文件必须提供波函数。该定义由我在 *J. Comput. Chem.*, **43**, 539 (2022) 中提出，此时 $ρ_{A}$ 定义为 $w_{A}$ *ρ*，其中 *ρ* 是通常方式算得的分子电子密度，$w_{A}$ 是原子 *A* 的 Hirshfeld 权重函数（定义见[3.9.1节](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#391-hirshfeld-原子电荷-1)）。

弱相互作用区域键临界点处的 δ*g* 函数值与相互作用强度密切相关。该函数也可绘制为平面图或等值面图以揭示所有成键区域。IGM 方法的非常详细介绍见[3.23.5节](sec-3-23-visual-study-of-weak-interaction.md#3235-基于前分子-promolecular密度的独立梯度模型-independent-gradient-model-igm分析-10)，若要研究特定两个或多个片段间的弱相互作用，应使用本节所述函数。

## **24 相互作用区域指示函数 (IRI)**

IRI 由我在 *Chemistry—Methods*, **1**, 231 (2021) 中提出，对揭示化学体系的各类相互作用区域极其有用，细节见[3.23.8节](sec-3-23-visual-study-of-weak-interaction.md#3238-相互作用区域指示函数-interaction-region-indicator-iri与-iri-π-分析-4)。IRI 定义为：

$$
IRI(\mathbf{r})=\frac{\left|\nabla\rho(\mathbf{r})\right|}{[\rho(\mathbf{r})]^a}
$$

其中 *a* 对应 *settings.ini* 中的 "uservar"。设为 0 时用推荐值 1.1。IRI 的详细介绍见[3.23.8节](sec-3-23-visual-study-of-weak-interaction.md#3238-相互作用区域指示函数-interaction-region-indicator-iri与-iri-π-分析-4)。注意，若 *ρ* 等于或小于 *settings.ini* 中的 "IRI_rhocut"，IRI 被设为任意大值 (5.0)，从而不会在不感兴趣的极低 *ρ* 区域出现 IRI 等值面。若 "IRI_rhocut" 设为 0 则不用该处理。对 IRI 或 IRI-π 做 basin 分析和拓扑分析时，应将其设为 0 以避免该处理带来的人为极值点（Multiwfn 会自动处理）。

## **25 van der Waals 势**

van der Waals (vdW) 势对研究以 vdW 效应为主导的分子间相互作用非常重要，它的作用可与静电势对以静电效应为主导的分子间相互作用的作用相比。该函数的介绍见[3.23.7节](sec-3-23-visual-study-of-weak-interaction.md#3237-范德华势的可视化-6)。该函数的单位为 kcal/mol，探针原子可由 *settings.ini* 中的 "ivdwprobe" 设置。
