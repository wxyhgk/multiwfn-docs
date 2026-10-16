# **3.25 概念密度泛函理论 (conceptual density functional theory, CDFT) 分析 (22)**

概念密度泛函理论 (CDFT) 最初由 Robert Parr 提出，并经众多研究者发展，是一个旨在揭示化学体系反应活性的理论框架。CDFT 包含众多概念和物理量，其中一些可用于预测有利的反应位点和反应特征，另一些可用于比较不同化学物种之间的反应活性。由于 CDFT 在量子化学中非常流行且具有重要地位，加之相关的有意义的物理量众多，我相信开发一个能以最少步骤计算 CDFT 中所有常用物理量的模块是非常有用的。

在本节的第一部分，我将简要描述可通过本模块研究的所有物理量的定义；然后在第二部分，我将展示如何使用本模块。本模块还能计算所谓的轨道加权物理量，将在第三部分专门介绍。

注意，除 CDFT 外，Multiwfn 还支持许多其他揭示反应位点的方法，概述见[4.A.4 节](sec-4-A-special-topics-and-advanced-tutorials.md#4a4-反应位点预测方法概述)。

如果您在研究中使用了本节所述的功能，请不仅引用 Multiwfn 的原始文献，还请引用下面这篇全面介绍本模块功能与实现的书章节：

Tian Lu, Qinxue Chen, Realization of Conceptual Density Functional Theory and Information-Theoretic Approach in Multiwfn Program. In *Conceptual Density Functional Theory*, WILEY-VCH GmbH: Weinheim (2022); pp 631-647. DOI: [10.1002/9783527829941.ch31](https://doi.org/10.1002/9783527829941.ch31)

## **3.25.1 理论**

要得到下面所有物理量，必须能获得 $N$、$N+1$ 和 $N-1$ 电子态的电子能量 ($E$) 和电子密度。通常 $N$ 指化学体系处于最稳定状态时所带的电子数。所有计算均采用针对 *N* 电子态优化过的几何结构。

- **整体指数**

  - 第一垂直电离势 ($I_1$)：$E(N-1)$ − $E(N)$

  - 第一垂直电子亲和势 ($A$)：$E(N)-E(N+1)$

  - Mulliken 电负性 (*χ*)：($I_1+A$)/2

  - 化学势 (*µ*)：−*χ*

  - 硬度 (*η*)：$I_1-A$，也等价于基本带隙。见 *J. Am. Chem. Soc.*, **105**, 7512 (1983)。注意，按照许多 CDFT 文献采用的惯例，*η* 原始定义中 1/2 的前缀被略去。

  - 软度 ($S$)：1/*η*。见 *Proc. Nati. Acad. Sci.*, **82**, 6723 (1985)

  - 亲电性 (electrophilicity) 指数 (*ω*)：*µ*²/(2*η*)。见 *J. Am. Chem. Soc.*, **121**, 1922 (1999)

  - 亲核性 (nucleophilicity) 指数 ($N_{\mathrm{Nu}}$)：$E_{\mathrm{HOMO}}$ (Nu) − $E_{\mathrm{HOMO}}$ (TCE)，其中 Nu 表示亲核试剂，TCE 表示四氰基乙烯，其 HOMO 能量几乎是所有有机分子中最低的，因此被选作参考体系。见 *J. Org. Chem.*, **73**, 4615 (2008)。

- **实空间函数**

  - Fukui 函数 (Fukui function) $f(\mathbf{r})$ 和对偶描述符 (dual descriptor) Δ $f(\mathbf{r})$：详细介绍见[4.5.4 节](sec-4-5-generate-grid-data-and-view-isosurface-map.md#454-用福井函数和对偶描述符研究苯酚亲电进攻的有利位点)

  - 局域软度：亲核、亲电、自由基攻击分别对应 $s^+(\mathbf{r})$ = $Sf^+(\mathbf{r})$、$s^-(\mathbf{r})$ = $Sf^-(\mathbf{r})$、$s^0(\mathbf{r})$ = $Sf^0(\mathbf{r})$，其中 $f(\mathbf{r})$ 为相应类型的 Fukui 函数。见 *Proc. Nati. Acad. Sci.*, **82**, 6723 (1985)

  - 局域超软度：$s^{(2)}$ ≈ $S^2$ Δ $f(\mathbf{r})$，见 *J. Math. Chem.*, **62**, 461 (2024)

  - 局域亲电性指数：${\omega}_{}^{\mathrm{loc}}(\mathbf{r})=\omega{f}^{+}(\mathbf{r})$

  - 局域亲核性指数：${N}_{\mathrm{Nu}}^{\mathrm{loc}}(\mathbf{r})={N}_{\mathrm{Nu}}^{}{f}^{-}(\mathbf{r})$

- **原子指数**

  - 凝聚 Fukui 函数 ($f$ *$_{A}$*) 和对偶描述符 (Δ $f$ *$_{A}$*)：详细介绍见[4.7.3 节](sec-4-7-population-analysis-and-atomic-charge-calculation.md#473-计算凝聚fukui函数和凝聚对偶描述符)

  - 凝聚局域软度

    - 亲核攻击：${s}_{A}^{+}=S{f}_{A}^{+}$

    - 亲电攻击：${s}_{A}^{-}=S{f}_{A}^{-}$

    - 自由基攻击：${s}_{A}^{0}=S{f}_{A}^{0}$

  - 相对亲电性指数：${s}_{A}^{+}/{s}_{A}^{-}$，见 *J. Phys. Chem. A*, **102**, 3746 (1998)

  - 相对亲核性指数：${s}_{A}^{-}/{s}_{A}^{+}$，见 *J. Phys. Chem. A*, **102**, 3746 (1998)

  - 凝聚局域亲电性指数：${\omega}^{A}=\omega{f}_{A}^{+}$

  - 凝聚局域亲核性指数：${N}_{\mathrm{Nu}}^{A}={N}_{\mathrm{Nu}}^{}{f}_{A}^{-}$

  - 凝聚局域超软度：${s}_{A}^{(2)}\approx {S}^{2}\Delta {f}_{A}$

- **键对偶描述符 (BDD)**

  BDD 是为每根化学键定义的指数，负（正）BDD 意味着该键是亲核性（亲电性）的，越负（越正），亲核性（亲电性）越强。

  BDD 本质上是键级 ($P$) 在外势恒定时对电子数的一阶导数。根据 *J. Math. Chem.*, **63**, 1588 (2025)，利用有限差分近似，键 $A$ - $B$ 的 BDD 可计算为 ${BDD}_{A,B}={f}_{A,B}^{+}-{f}_{A,B}^{-}$，其中 ${f}_{A,B}^{+}$ 和 ${f}_{A,B}^{-}$ 为两种类型的键 Fukui 函数，按下式计算

  
$$
{f}_{A,B}^{+}={P}_{A,B}\left( N+1 \right)-{P}_{A,B}\left( N \right)
$$

  
$$
{f}_{A,B}^{-}={P}_{A,B}\left( N \right)-{P}_{A,B}(N-1)
$$

  在 *J. Math. Chem.*, **63**, 1588 (2025) 中作者采用基于自然原子轨道的 Wiberg 键级作为 $P$，但在当前 Multiwfn 实现中，采用基于 Hirshfeld 划分的模糊 (fuzzy) 键级（详见[3.11.6 节](sec-3-11-bond-order-analysis.md#3116-模糊键级fuzzy-bond-order-7)）作为 $P$ 来计算 BDD，因为该键级对基组不敏感（在这方面远好于 Mayer 键级），表现合理（根据我的测试），且相对容易实现。

- ***ω*$_{cubic}$** **亲电性指数**

  *J. Phys. Chem. A*, **124**, 2090 (2020) 引入的亲电性指数 *ω*$_{cubic}$ 有些特殊，它还依赖于 $N-2$ 电子态。与前述亲电性指数 *ω* 相比，它包含了更高阶的项。其定义为

  
$$
\omega_{\mathrm{cubic}}=\omega\left(1+\frac{\mu}{3\eta^2}\gamma\right)
$$

  实际计算为

  
$$
\omega_{\mathrm{cubic}}=\frac{(\mu_{\mathrm{cubic}})^2}{2\eta_{\mathrm{cubic}}}\left[1+\frac{\mu_{\mathrm{cubic}}}{3(\eta_{\mathrm{cubic}})^2}\gamma_{\mathrm{cubic}}\right]
$$

  其中

  
$$
\begin{gathered}\mu_{\mathrm{cubic}}=(1/6)(-2A-5I_1+I_2)\\\eta_{\mathrm{cubic}}=I_1-A\\\gamma_{\mathrm{cubic}}=2I_1-I_2-A\end{gathered}
$$

  其中 $I_2$ 为第二垂直电离势，定义为 $E(N-2)$ − $E(N-1)$。相应地，存在立方形式的凝聚局域亲电性指数 ${\omega}_{\mathrm{cubic}}^{A}={\omega}_{\mathrm{cubic}}{f}_{A}^{+}$。*J. Phys. Chem. A*, **124**, 2090 (2020) 表明，卤键二聚体 R-X···NH₃ 中卤素原子（因其 σ-hole 而表现为 Lewis 酸）的 ${\omega}_{\mathrm{cubic}}^{A}$ 值与计算的结合能具有极好的相关性（但注意，他们采用 AIM 划分原子空间，而非本模块所用的 Hirshfeld 划分）。

- **亲电描述符 (*ε*)**

  亲电描述符 (*ε*) 在 *Int. J. Quantum Chem.*, **124**, e27366 (2024) 中被引入，在由 35 个有机分子组成的测试集上，它与 Mayr 亲电参数 ($E$) 的相关性显著优于亲电性指数 (*ω*)。与仅基于体系能量二阶 Taylor 展开推导的 *ω* 不同，*ε* 的推导基于三阶展开，这使得 *ε* 显式地包含超硬度。与 *ω*$_{cubic}$ 一样，*ε* 的计算也依赖于 $N-2$ 电子态。

  计算 *ε* 的工作方程如下

  
$$
\varepsilon=\chi\left(\frac{\phi}{\gamma}\right)-\left(\frac{\phi}{\gamma}\right)^2\left(\frac{\eta}{2}+\frac{\phi}{6}\right)
$$

  其中

  
$$
\phi=\sqrt{\eta^2-2\gamma\mu}-\eta
$$

  重要的一点是，上述方程中涉及的 *η*、*γ*、*χ*、*µ* 应采用与前面所述不同的方式计算，即

  
$$
\begin{aligned}
&\mu=a\\
&\chi=-a\\
&\eta=2(b-ac)\\
&\gamma=-3c(b-ac)
\end{aligned}
$$

  其中

  
$$
\begin{aligned}
&c=\frac{I_2-2I_1+A'}{2I_2-I_1-A'}\\
&b=\frac{I_1-A'}{2}-\frac{I_1+A'}{2}c\\
&a=-\frac{I_1+A'}{2}+\frac{I_1-A'}{2}c
\end{aligned}
$$

  其中 $A$ ’ = $E(N+1)$ − $E(N)$，即电子亲和势，但符号与标准定义相反。

- **Fukui 势与对偶描述符势**

  Fukui 势的定义与物理意义在 *J. Phys. Chem. A*, **115**, 2325 (2011) 和 *Int. J. Quantum Chem.*, **101**, 520 (2005) 中被仔细讨论过。Fukui 势是对 ESP 的补充，有助于理解电子转移不可忽略时化学反应早期的能量变化。例如，当亲电体受到亲核试剂攻击时，亲电体感受到的由亲核试剂产生的外势为

  
$$
{v}_{N\mathrm{-phile}}\left( \mathbf{r} \right)\approx {V}_{N-\mathrm{phile}}^{\mathrm{ESP}}\left( \mathbf{r} \right)-\Delta N\int \frac{{f}_{N-\mathrm{phile}}^{-}(\mathbf{r'})}{|\mathbf{r}-\mathbf{r}'|}\mathrm{d}\mathbf{r'}
$$

  其中 Δ $N$ 为从亲电体转移到亲核试剂的电子数（此情形下为负值），${f}_{N-\mathrm{phile}}^{-}$ 为亲核试剂的 Fukui 函数 $f^-$。三类 Fukui 势定义如下

  
$$
{V}_{{f}^{-/+/0}}(\mathbf{r})=\int \frac{{f}^{-/+/0}(\mathbf{r'})}{|\mathbf{r}-\mathbf{r}'|}\mathrm{d}\mathbf{r}'
$$

  ESP 只能在假设没有电子转移的前提下预测由静电效应主导的区域选择性，但显然该假设对一般化学反应而言远非成立（但对许多非共价相互作用基本成立）。显然，在研究一般反应、尤其是有显著电子转移的反应时，应更多关注 Fukui 势。

  Fukui 势在预测区域选择性方面比 Fukui 函数更严格，正如 *J. Phys. Chem. A*, **115**, 2325 (2011) 所强调的：“决定反应位点的是 Fukui 势的值，而非 Fukui 函数本身的值”。然而，Fukui 势不如 Fukui 函数流行，因为二者的分布特征通常一致，而计算 Fukui 势需要计算两次 ESP，比计算两次电子密度昂贵得多。根据 Fukui 函数的有限差分定义，例如 ${V}_{{f}^{-}}$ 可计算为

  
$$
{V}_{{f}^{-}}(\mathbf{r})=\int \frac{{f}^{-}(\mathbf{r'})}{|\mathbf{r}-\mathbf{r}'|}\mathrm{d}\mathbf{r'}=\int \frac{{\rho}_{N}\left( \mathbf{r'} \right)-{\rho}_{N-1}(\mathbf{r'})}{|\mathbf{r}-\mathbf{r}'|}\mathrm{d}\mathbf{r'=}{V}_{N-1}^{\mathrm{ESP}}(\mathbf{r})-{V}_{N}^{\mathrm{ESP}}(\mathbf{r})
$$

  此外，对偶描述符势 (DDP) 在 *J. Math. Chem.*, **62**, 1094 (2024) 中被引入，定义为

  
$$
DDP\left( \mathbf{r} \right)=\int \frac{\Delta f\left( {\mathbf{r}}^{'} \right)}{\left| \mathbf{r}-{\mathbf{r}}^{'} \right|}\mathrm{d}{\mathbf{r}}^{'}=\int \frac{{f}^{+}\left( {\mathbf{r}}^{'} \right)-{f}^{-}\left( {\mathbf{r}}^{'} \right)}{\left| \mathbf{r}-{\mathbf{r}}^{'} \right|}\mathrm{d}{\mathbf{r}}^{'}={V}_{{f}^{+}}\left( \mathbf{r} \right)-{V}_{{f}^{-}}(\mathbf{r})
$$

  与常有许多节面妨碍讨论的对偶描述符不同，DDP 的分布平滑得多，使研究者更容易识别优先的反应位点。

  与 Fukui 函数一样，${V}_{{f}^{+}}$ 在某区域越正，该区域越可能发生亲核反应；${V}_{{f}^{-}}$ 越正的区域，越可能发生亲电反应。与对偶描述符类似，DPP 在某区域越正、越负，该区域分别越易于发生亲核和亲电攻击。

## **3.25.2 用法**

使用本模块（即主功能 22）时，启动 Multiwfn 后载入的文件相对任意，唯一要求是该文件中的原子信息与所研究的体系相同。

进入本模块后会看到一个菜单，其中选项 2、3 和 9 用于计算上述物理量。使用它们之前，一般应在当前目录下提供 *N.wfn*、*N-1.wfn* 和 *N+1.wfn*，它们分别包含当前体系 $N$、$N-1$ 和 $N+1$ 态的波函数和电子能量，几何结构必须相同且对应于 $N$ 态的优化几何。三个文件的计算级别也必须相同。若缺少三个 .wfn 文件中的任何一个，Multiwfn 会要求您手动输入相应态的 .wfn 文件路径（.wfx、.fch 和 .mwfn 文件也被允许，因为它们同样携带波函数和电子能量信息）。

- **选项 2**：用于计算前述所有整体指数和原子指数，结果将导出到当前目录下的 *CDFT.txt*。如[4.7.3 节](sec-4-7-population-analysis-and-atomic-charge-calculation.md#473-计算凝聚fukui函数和凝聚对偶描述符)所述，Hirshfeld 方法是计算凝聚 Fukui 函数乃至其他相关原子指数的理想选择，因此会自动计算 Hirshfeld 电荷并用于所有原子指数的计算。亲核性指数及其局域版本依赖于 TCE 的 HOMO 能量，应采用与当前体系相同的级别计算，注意本模块打印的这些指数直接采用在常用 B3LYP/6-31G\* 级别下计算的 $E_{\mathrm{HOMO}}$ (TCE) = -0.335198 Hartree（显然，若想得到更可靠的结果而当前计算级别不是 B3LYP/6-31G\*，您应自行计算 $E_{\mathrm{HOMO}}$ (TCE) 再手动计算这些指数）。

- **选项 3**：用于计算 Fukui 函数、对偶描述符及相关函数的格点数据 (grid data)，然后可直接可视化它们的等值面 (isosurface) 图，格点数据可导出为当前目录下的 cube 文件。在此选项中可设置乘到所算格点数据上的缩放因子。例如，若将缩放因子设为选项 2 输出的整体软度，则缩放后的 $f^-(\mathbf{r})$ Fukui 函数即对应于 $s^-(\mathbf{r})$。

- **选项 9**：与选项 3 类似，但用于计算 Fukui 势和对偶描述符势的格点数据。由于每个带电态都需要计算 ESP 的格点数据，通常开销较大，应选择合适的格点设置以避免过于耗时。

- **选项 10**：用于计算键对偶描述符。Multiwfn 会依次载入不同电子态的 .wfn 文件并计算模糊键级，最后计算并打印 BDD 值。开销一般很低。

### **.wfn 文件的生成**

您可以手动准备选项 2 和 3 所用的 .wfn 文件，或者使用本模块的选项 1 自动完成准备工作。

选择选项 1 后，会提示输入单点任务的 Gaussian 关键词，然后 Multiwfn 依次要求输入 $N$、$N+1$ 和 $N-1$ 态的电荷与自旋多重度，随后在当前目录下生成 Gaussian 单点输入文件 *N.gjf*、*N+1.gjf* 和 *N-1.gjf*（这些文件中的几何结构对应于 Multiwfn 输入文件中的几何）。之后您可以手动用 Gaussian 运行它们得到 *N.wfn*、*N+1.wfn* 和 *N-1.wfn*；若您的电脑已安装 Gaussian，也可直接让 Multiwfn 调用 Gaussian 计算它们（此时 *settings.ini* 中的 "gaupath" 参数必须已设为 Gaussian 可执行文件的实际路径），计算完成后三个 .wfn 文件会出现在当前目录下。

有时需要使用混合基组，此时应在当前目录下准备一个名为 *basis.txt* 的文件，记录基组的定义（也可附带赝势定义）。若输入的关键词包含 "gen" 或 "genecp"，则 *basis.txt* 的内容会自动追加到所生成的 .gjf 文件末尾。

Multiwfn 也能生成 ORCA 输入文件以产生这三个 .wfn 文件。应选择选项 -2 并选择 ORCA，然后选项 1 将生成 *N.inp*、*N-1.inp* 和 *N+1.inp*。若已将 *settings.ini* 中的“orcapath”设为 ORCA 可执行文件的实际路径，可直接让 Multiwfn 调用 ORCA 运行它们得到 *N.wfn*、*N-1.wfn* 和 *N+1.wfn*；或者手动用 ORCA 运行，再将得到的 *N.wfn*、*N-1.wfn* 和 *N+1.wfn* 放到当前目录下。

用本模块研究大有机体系时，通常我建议使用 B3LYP/6-31G\* 级别，因为该级别便宜，而所得物理量的质量已令人满意。

### **关于计算 *ω*$_{cubic}$ 和 *ε* 的说明**

默认情况下 Multiwfn 不计算 *ω*$_{cubic}$ 和 *ε*，因为它们依赖于 $N-2$ 电子态。若需要，应先选择选项 -1 将状态切换为 "Yes"。然后可用选项 1 帮助准备 $N$、$N+1$、$N-1$、$N-2$ 电子态的 .wfn 文件，或手动提供。之后选择选项 2，所得 *CDFT.txt* 文件将包含凝聚局域 *ω*$_{cubic}$、整体 *ω*$_{cubic}$、*ε* 以及 $I_2$。

使用本模块计算苯酚各种 CDFT 物理量的例子见[4.22.1 节](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md#4221-自动计算苯酚的概念密度泛函理论量)。绘制马来酸酐 Fukui 势和对偶描述符势的例子见[4.22.4 节](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md#4224-绘制-fukui-势和对偶描述符势的例子)。计算键对偶描述符的例子见[4.22.5 节](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md#4225-计算键对偶描述符-bond-dual-descriptor-bdd-的例子)。

## **3.25.3 专题 1：轨道加权 Fukui 函数与对偶描述符**

### **理论**

当初级前线分子轨道（准）简并时，原本定义的 Fukui 函数和对偶描述符效果不好。例如，当 HOMO 与 HOMO-1 能量非常接近或完全相同时，Fukui 函数 $f^-$ 可能无法给出有意义的结果，或结果完全误导；此外，当体系具有点群对称性时，如 C₆₀ 富勒烯，$f^-$ 的分布常与分子对称性不一致，这显然是出乎意料的。

为解决这些问题，*J. Comput. Chem.*, **38**, 481 (2017) 的作者提出了轨道加权 Fukui 函数，*J. Phys. Chem. A*, **123**, 10556 (2019) 中他们进一步提出了轨道加权对偶描述符，总结如下（${f}_{w}^{0}$ 由我定义）

$$
\begin{gathered}f_w^+(\mathbf{r})=\sum_{i=\mathrm{LUMO}}^{\infty}w_i\left|\varphi_i(\mathbf{r})\right|^2\qquad w_i=\frac{\exp\left[-\left(\frac{\mu-\varepsilon_i}{\Delta}\right)^2\right]}{\sum_{i=\mathrm{LUMO}}^{\infty}\exp\left[-\left(\frac{\mu-\varepsilon_i}{\Delta}\right)^2\right]}\\f_w^-(\mathbf{r})=\sum_{i}^{\mathrm{HOMO}}w_i\left|\varphi_i(\mathbf{r})\right|^2\qquad w_i=\frac{\exp\left[-\left(\frac{\mu-\varepsilon_i}{\Delta}\right)^2\right]}{\sum_{i}^{\mathrm{HOMO}}\exp\left[-\left(\frac{\mu-\varepsilon_i}{\Delta}\right)^2\right]}\\f_w^0(\mathbf{r})=\left[f_w^+(\mathbf{r})+f_w^-(\mathbf{r})\right]/2\\\Delta f_w(\mathbf{r})=f_w^+(\mathbf{r})-f_w^-(\mathbf{r})\end{gathered}
$$

其中 $ε_{i}$ 和 $\varphi$ *$_{i}$* 分别为轨道 $i$ 的能量和波函数；*µ* 为化学势，在上式中近似按 ($E_{\mathrm{HOMO}}$ + $E_{\mathrm{LUMO}}$)/2 计算。Δ 为可调参数，原则上其最佳值是能使函数具有理想局域反应活性预测能力的值。显然最合适的 Δ 依赖于实际体系，通常 0.1 Hartree 是值得一试的初猜。若发现该取值下的轨道加权函数效果不好，可尝试适当改变它并重新计算。

与 $f^-$ 的冻结轨道近似形式，即 $f^-(\mathbf{r})=\left|\varphi_{\mathrm{HOMO}}(\mathbf{r})\right|^2$ 相比，${f}_{w}^{-}$ 的优点在于它以不同权重考虑了所有轨道。由表达式可见，能量越接近 HOMO 能量的低占据轨道权重越大。显然简并轨道具有相同权重。公式中的 Gaussian 函数起衰减函数的作用，Δ 越大，低占据轨道对 ${f}_{w}^{-}$ 的贡献越高。当 HOMO 与 HOMO-1 能量差显著时，就没有理由用 ${f}_{w}^{-}$ 代替 $f^-$。${f}_{w}^{+}$、${f}_{w}^{0}$ 和 $\Delta {f}_{w}$ 的情况类似。

### **用法**

由于轨道加权函数涉及虚轨道，应使用 .mwfn、.fch、.molden 或 .gms 文件作为输入文件。通常，输入文件中的几何结构应对应于 $N$ 电子态的优化几何；但也可研究非平衡结构，如内禀反应坐标 (IRC) 上的某一点。

只接受闭壳层单行列式波函数。若打算计算 ${f}_{w}^{+}$、${f}_{w}^{0}$ 和 $\Delta {f}_{w}$，不应使用弥散函数，因为它们利用虚轨道，而使用弥散函数时虚轨道的化学意义可能严重受损。

在主功能 22 中，有四个选项与轨道加权计算相关：

- 选项 4：设置后续轨道加权计算中使用的 Δ 参数

- 选项 5：打印权重最高的前 10 个权重（即上述公式中的 {$w$}）。该选项有助于检查当前 Δ 参数是否合理，并帮助用户更好地理解轨道加权方法的工作方式

- 选项 6：计算凝聚的 ${f}_{w}^{+}$、${f}_{w}^{-}$、${f}_{w}^{0}$ 和 $\Delta{f}_{w}^{}$ 值，即计算这些函数在 Hirshfeld 原子空间中的积分。结果有助于定量考察各原子上这些函数的净贡献。默认的径向和角向积分点通常已足够精细，若发现凝聚 ${f}_{w}^{+}$ 或 ${f}_{w}^{-}$ 之和明显偏离 1.0，应将 *settings.ini* 中的 "iautointgrid" 参数设为 0，再适当增大 "radpot" 和 "sphpot" 参数。

- 选项 7：计算 ${f}_{w}^{+}$、${f}_{w}^{-}$、${f}_{w}^{0}$ 和 $\Delta{f}_{w}^{}$ 函数的格点数据，然后可直接可视化它们的等值面，或将其导出为 cube 文件以便用 VMD 和 ChimeraX 等第三方软件渲染。

使用本模块计算轨道加权 Fukui 函数和轨道加权对偶描述符的例子见[4.22.2 节](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md#4222-轨道加权-fukui-函数和轨道加权对偶描述符研究示例)。

## **3.25.4 专题 2：基于电子密度的（准）简并 Fukui 函数与对偶描述符**

### **3.25.4.1 闭壳层情形**

#### **理论**

上一节介绍了轨道加权 Fukui 函数和对偶描述符，适用于前线分子轨道（准）简并的情形。但它们基于轨道近似定义，即未考虑轨道弛豫效应，而该效应并非总能安全忽略。*J. Comput. Chem.*, **37**, 2279 (2016) 提出了一种适用于（准）简并 HOMO/LUMO 情形的 Fukui 函数和对偶描述符的替代形式，该形式直接基于电子密度定义，即如同原始 Fukui 函数和对偶描述符一样，完全考虑了轨道弛豫效应。这种基于电子密度的（准）简并 Fukui 函数和对偶描述符将分别记为 $f_{\mathrm{Q}}$ 和 Δ $f_{\mathrm{Q}}$。

$f_{\mathrm{Q}}$ 的思想很简单。若在电子态 $N$ 下 LUMO 和 HOMO 的简并度分别为 $p$ 和 $q$，则三类 $f_{\mathrm{Q}}$ 按下式计算

$$
\begin{gathered}f_{\mathrm{Q}}^+(\mathbf{r})=\frac{\rho_{N+p}(\mathbf{r})-\rho_N(\mathbf{r})}{p}\\f_{\mathrm{Q}}^-(\mathbf{r})=\frac{\rho_N(\mathbf{r})-\rho_{N-q}(\mathbf{r})}{q}\\f_{\mathrm{Q}}^0(\mathbf{r})=\left[f_{\mathrm{Q}}^+(\mathbf{r})+f_{\mathrm{Q}}^-(\mathbf{r})\right]/2\end{gathered}
$$

Δ $f_{\mathrm{Q}}$ 可如常基于 ${f}_{\mathrm{Q}}^{+}$ 和 ${f}_{\mathrm{Q}}^{-}$ 计算

$$
\Delta f_{\mathrm{Q}}(\mathbf{r})=f_{\mathrm{Q}}^+(\mathbf{r})-f_{\mathrm{Q}}^-(\mathbf{r})
$$

显然，若 HOMO 和 LUMO 均非简并，则 $f_{\mathrm{Q}}$ 和 Δ $f_{\mathrm{Q}}$ 将分别等价于原始形式的 Fukui 函数和对偶描述符 $f$ 与 Δ $f$。

要合理计算 $f_{\mathrm{Q}}$ 和 Δ $f_{\mathrm{Q}}$，关键是正确确定 $p$ 和 $q$。通常可通过查看几个最低未占据 MO 和几个最高占据 MO 的能量来指定。若某占据（未占据）MO 与 HOMO (LUMO) 的能量差很小，*例如*小于 0.01 eV，则可视为简并。显然，判断轨道简并没有严格的能量阈值，有时需综合多种因素判断，*例如* HOMO-LUMO 带隙、实际计算结果的合理性、轨道形状等。

注意 $f_{\mathrm{Q}}$ 和 Δ $f_{\mathrm{Q}}$ 仅对闭壳层情形定义。

Multiwfn 不仅能计算 $f_{\mathrm{Q}}$ 和 Δ $f_{\mathrm{Q}}$，还能基于它们计算[3.25.1 节](#3251-理论)所述的局域性质（*ω*$_{cubic}$ 除外）。例如，考虑简并时的局域软度为整体软度与 $f_{\mathrm{Q}}$ 的乘积。注意，所涉及的第一垂直电子亲和势和电离势仍按常规计算，即 VEA = $E(N) - E(N+1)$，VIP = $E(N-1) - E(N)$。

计算 $N+p$ 和 $N-q$ 态波函数文件时必须正确选择自旋多重度，通常应设为 $p+1$ 和 $q+1$，详见 *J. Comput. Chem.*, **37**, 2279 (2016) 的讨论。该设置通常能保证附加（脱离）的电子平均进入（离开）所有简并的 LUMO (HOMO)。

#### **用法**

在主功能 22 中，$p$ 和 $q$ 默认均为 1，即不考虑前线分子轨道 (FMO) 的简并。要手动设置 $p$ 和 $q$ 从而在后续计算中考虑（准）简并效应，应先选择选项“-3 设置 FMO 简并度”。此时屏幕上会列出 10 个最低未占据 MO 和 10 个最高占据 MO 的信息（若输入文件包含波函数信息），应根据列出的 MO 能量合理输入 $p$ 和 $q$。

设置好 $p$ 和 $q$ 后，可用选项 1 让 Multiwfn 帮助生成 Gaussian 或 ORCA 代码单点任务的输入文件，分别对应 $N$、$N+p$ 和 $N-q$ 态，会要求输入这些态的净电荷与自旋多重度。此外，若 $p$ 或 $q$ 不等于 1，Multiwfn 还会询问是否为 $N+1$ 和/或 $N-1$ 态也生成输入文件，因为选项 2 计算第一电离势、电子亲和势及相关量时需要 $E(N+1)$ 和 $E(N-1)$。运行这些输入文件后即得到各态的 .wfn 文件。当然，也可用您喜欢的任何量子化学代码手动生成各态的波函数文件。

最后，可用相应选项计算 CDFT 框架下定义的各种物理量或函数，输出内容与默认的非简并情形完全相同，只是当前情形已合理考虑了 $p$ 和 $q$。注意，若 $p$ 或 $q$ 不等于 1，同时当前目录下没有 *N+1.wfn* 或 *N-1.wfn*，则选项 2 不会计算和输出与第一电离势和电子亲和势相关的量。

例子见[4.22.3 节](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md#4223-准简并-homolumo-情形的-cdft-分析实例)。

### **3.25.4.2 开壳层情形**

#### **理论**

对于开壳层情形，Martínez Araya 在 *Chem. Phys. Lett.*, **506**, 104 (2011) 中基于自旋极化概念 DFT 的形式提出了计算对偶描述符的工作方程。该方程随后被进一步推广（私人交流），总结如下，其中 $\Delta {N}_{S}$ 对应自旋数变化 (${N}_{S}={N}_{\alpha}-{N}_{\beta}$)，**B** 表示外磁场；${p}_{\alpha}$ 和 ${p}_{\beta}$ 分别为 LUMO(α) 和 LUMO(β) 的简并度；${q}_{\alpha}$ 和 ${q}_{\beta}$ 分别为 HOMO(α) 和 HOMO(β) 的简并度。

计算 ${f}^{+}={\left( \frac{\partial \rho\left( \mathbf{r} \right)}{\partial N} \right)}_{v\left( \mathbf{r} \right),\mathbf{B}\left( \mathbf{r} \right)}^{+}$ 的不同形式，即自旋多重度增加、减小和近似不变：

$$
\begin{gathered}
{f}_{\Delta{N}_{S}<0}^{+}\left( \mathbf{r} \right)=\frac{{\rho}_{N+{p}_{\beta}}\left( \mathbf{r} \right)-{\rho}_{N}\left( \mathbf{r} \right)}{{p}_{\beta}}\\
{f}_{\Delta{N}_{S}>0}^{+}\left( \mathbf{r} \right)=\frac{{\rho}_{N+{p}_{\alpha}}\left( \mathbf{r} \right)-{\rho}_{N}\left( \mathbf{r} \right)}{{p}_{\alpha}}\\
{f}_{\Delta{N}_{S}\approx 0}^{+}\left( \mathbf{r} \right)=\frac{{f}_{\Delta{N}_{S}>0}^{+}\left( \mathbf{r} \right)+{f}_{\Delta{N}_{S}<0}^{+}\left( \mathbf{r} \right)}{2}
\end{gathered}
$$

计算 ${f}^{-}={\left( \frac{\partial \rho\left( \mathbf{r} \right)}{\partial N} \right)}_{v\left( \mathbf{r} \right),\mathbf{B}\left( \mathbf{r} \right)}^{-}$ 的不同形式：

$$
\begin{gathered}
{f}_{\Delta{N}_{S}<0}^{-}\left( \mathbf{r} \right)=\frac{{\rho}_{N}\left( \mathbf{r} \right)-{\rho}_{N-{q}_{\alpha}}\left( \mathbf{r} \right)}{{q}_{\alpha}}\\
{f}_{\Delta{N}_{S}>0}^{-}\left( \mathbf{r} \right)=\frac{{\rho}_{N}\left( \mathbf{r} \right)-{\rho}_{N-{q}_{\beta}}\left( \mathbf{r} \right)}{{q}_{\beta}}\\
{f}_{\Delta{N}_{S}\approx 0}^{-}\left( \mathbf{r} \right)=\frac{{f}_{\Delta{N}_{S}>0}^{-}\left( \mathbf{r} \right)+{f}_{\Delta{N}_{S}<0}^{-}\left( \mathbf{r} \right)}{2}
\end{gathered}
$$

计算对偶描述符的不同形式：

$$
\begin{gathered}
\Delta{f}_{\Delta{N}_{S}<0}\left( \mathbf{r} \right)={f}_{\Delta{N}_{S}<0}^{+}\left( \mathbf{r} \right)-{f}_{\Delta{N}_{S}<0}^{-}\left( \mathbf{r} \right)\\
\Delta{f}_{\Delta{N}_{S}>0}\left( \mathbf{r} \right)={f}_{\Delta{N}_{S}>0}^{+}\left( \mathbf{r} \right)-{f}_{\Delta{N}_{S}>0}^{-}\left( \mathbf{r} \right)\\
\Delta{f}_{\Delta{N}_{S}\approx 0}\left( \mathbf{r} \right)={f}_{\Delta{N}_{S}\approx 0}^{+}\left( \mathbf{r} \right)-{f}_{\Delta{N}_{S}\approx 0}^{-}\left( \mathbf{r} \right)
\end{gathered}
$$

原则上 $\Delta{f}_{\Delta{N}_{S}\approx 0}$ 应是最理想的选择，因为它满足保持自旋数不变的限制。但还有两种同样保持自旋数不变的方式，分别只涉及 α 和 β 电子的变化，但它们在文献中尚未被检验。$\Delta{f}_{\alpha}\left( \mathbf{r} \right)={f}_{\Delta{N}_{S}>0}^{+}\left( \mathbf{r} \right)-{f}_{\Delta{N}_{S}<0}^{-}\left( \mathbf{r} \right)$ $\Delta{f}_{\beta}\left( \mathbf{r} \right)={f}_{\Delta{N}_{S}<0}^{+}\left( \mathbf{r} \right)-{f}_{\Delta{N}_{S}>0}^{-}\left( \mathbf{r} \right)$

#### **用法**

CDFT 模块的子功能 12 专门用于计算上述所有函数。启动 Multiwfn 后，通常应：

- (1) 载入包含基函数信息和所有轨道的波函数文件

- (2) 进入主功能 22 的子功能 12

- (3) 若该体系前线 MO 存在简并，选择选项 1 设置简并度

- (4) 选择选项 2 生成所有相关电子态的 Gaussian 单点任务输入文件。然后可让 Multiwfn 调用 Gaussian 直接计算它们，或手动计算。再将所得 .wfn 文件（与 .gjf 文件同名）放到当前目录下。

- (5) 选择选项 3 生成不同电子态电子密度的格点数据。在后处理菜单中，可直接可视化所选形式的 Fukui 函数或对偶描述符的等值面图，或将相应格点数据导出为 .cub 文件。

例子见[4.22.3.3 节](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md#42233-开壳层分子-o₂-的-fukui-函数和对偶描述符)。

## **3.25.5 专题 3：亲核与亲电超离域性**

### **理论**

亲核与亲电离域性也称为亲核与亲电超离域性，由 Schüürmann 在 *Environ. Toxicof. Chem.*, **9**, 417 (1990) 和 *Quant. Struct.-Act. Relat.*, **9**, 326 (1990) 中提出，曾被用作构建定量构效关系 (QSAR) 方程的分子描述符。在 Schüürmann 的工作中，原子 *A* 的亲核超离域性 ($D^{\mathrm{N}}$) 和亲电超离域性 ($D^{\mathrm{E}}$) 分别定义为

$$
\begin{gathered}D^{\mathrm{N}}(A)=2\sum_{i}^{\mathrm{unocc}}\sum_{\mu\in A}\frac{C_{\mu,i}^2}{\alpha-\varepsilon_i}\\D^{\mathrm{E}}(A)=2\sum_{i}^{\mathrm{occ}}\sum_{\mu\in A}\frac{C_{\mu,i}^2}{\varepsilon_i-\alpha}\end{gathered}
$$

其中 $ε_{i}$ 为分子轨道 $i$ 的能量，*α* = ($E_{\mathrm{HOMO}}$ + $E_{\mathrm{LUMO}}$)/2，*µ*∈ $A$ 表示原子 *A* 的基函数 *µ*，**C** 为系数矩阵。显然 $D^{\mathrm{N}}$ 和 $D^{\mathrm{E}}$ 均为负值。

然而，Schüürmann 的超离域性表达式只适用于采用正交基函数的半经验计算。*Sci. Rep.*, **5**, 13695 (2015) 提出了一种不同版本的亲电超离域性，与非正交基函数兼容。该工作表明，原子的亲电超离域性与其原子极化率密切相关。

上述超离域性的定义基于分子轨道展开系数；相比之下，Multiwfn 中超离域性基于原子空间的 Hirshfeld 划分计算，该形式更稳健且与弥散函数完全兼容。具体地，Multiwfn 中亲核与亲电超离域性按下式计算

$$
\begin{gathered}D^{\mathrm{N}}(A)=2\sum_{i}^{\mathrm{unocc}}\frac{\Theta_{A,i}}{\alpha-\varepsilon_i}\\D^{\mathrm{E}}(A)=2\sum_{i}^{\mathrm{occ}}\frac{\Theta_{A,i}}{\varepsilon_i-\alpha}\end{gathered}
$$

其中 Θ*$_{A,i}$* 为按 Hirshfeld 方法计算的原子 *A* 在轨道 $i$ 中的组成，详见[3.10.5 节](sec-3-10-orbital-composition-analysis.md#3105-用-hirshfeld-或-hirshfeld-i-方法计算原子和片段贡献-810)。Multiwfn 还计算不含 *α* 位移参数的超离域性，即

$$
\begin{gathered}D^{\mathrm{N0}}(A)=2\sum_{i}^{\mathrm{unocc}}\frac{\Theta_{A,i}}{-\varepsilon_i}\\D^{\mathrm{E0}}(A)=2\sum_{i}^{\mathrm{occ}}\frac{\Theta_{A,i}}{\varepsilon_i}\end{gathered}
$$

### **用法**

由于超离域性涉及虚轨道，应使用 .mwfn、.fch、.molden 或 .gms 文件作为输入文件。只接受闭壳层单行列式波函数。若打算计算 $D^{\mathrm{N}}$ 和 $D^{\mathrm{N0}}$，不应使用弥散函数，因为它利用虚轨道，而使用弥散函数时虚轨道的化学意义可能严重受损。

载入输入文件后，进入主功能 22，再选择选项 8，即可得到所有原子的 $D^{\mathrm{N}}$、$D^{\mathrm{E}}$、$D^{\mathrm{N0}}$ 和 $D^{\mathrm{E0}}$。输出示例（*examples\oxirane.fchk*）：

```text
    Atom             D_N                D_E              D_N_0             D_E_0
    1(C )        -26.56182        -10.85916        -35.92863         -8.75591
    2(C )        -26.56182        -10.85916        -35.92863         -8.75591
    3(O )        -20.09086        -19.14131        -25.62598        -14.71454
    4(H )        -10.19410         -2.66387        -14.52037         -2.13024
    5(H )        -10.19410         -2.66387        -14.52037         -2.13024
    6(H )        -10.19410         -2.66387        -14.52037         -2.13024
    7(H )        -10.19410         -2.66387        -14.52037         -2.13024

Sum of D_N:        -113.99092 /Hartree
Sum of D_E:         -51.51513 /Hartree
Sum of D_N_0:      -155.56471 /Hartree
Sum of D_E_0:       -40.74734 /Hartree
```

## **3.25.6 专题 4：对偶离域描述符**

### **理论**

对偶离域描述符 (DDD) 理论由 Samir Kenouche 在 *Phys. Chem. Chem. Phys.*, **28**, 19133 (2026) 中提出。该方法定量描述原子间离域指数 (DI) 对总电子数变化的响应。该理论与[3.25.1 节](#3251-理论)介绍的键对偶描述符 (BDD) 密切相关，本质上二者都展示了电子共享程度在得电子或失电子过程中的变化。但 BDD 基于两个电子态（$N$ 与 $N-1$，或 $N$ 与 $N+1$）之间键级的有限差分计算，而 DDD 具有解析形式，其计算只依赖于 $N$ 态的波函数，因此在计算开销上有优势。另一优点是 DDD 的各组分使人们能考察前线分子轨道对响应的作用，讨论见原始论文。注意 DDD 理论基于冻结轨道近似 (FOA) 推导，且只支持单行列式闭壳层波函数。

这里介绍 DDD 的关键思想与要素。该理论在 Ángyán-Loos-Mayer (ALM) 形式的 DI (*δ*) 下推导：

$$
{\delta}_{A,B}^{\mathrm{ALM}}=\sum_{i,j} {\eta}_{i}{\eta}_{j}{S}_{ij}(A){S}_{ij}(B)
$$

其中 *η* 为轨道占据数，**S** 为原子重叠矩阵 (AOM)，${S}_{ij}(A)$ 对应 MO $i$ 与 MO $j$ 乘积在原子 *A* 空间中的积分。$i$ 和 $j$ 遍历所有空间轨道。

DI 的导数在整数电子数处不连续。在 FOA 下并假设电子只能从 HOMO 离开，可证明 DI 的左侧一阶导数可表示为下式，反映了 DI 对 $N$ 减少的 HOMO 主导响应

$$
{\left( \frac{\partial {\delta}_{A,B}}{\partial N} \right)}^{-}=4\sum_{i<\mathrm{H}} {S}_{\mathrm{H}i}(A){S}_{\mathrm{H}i}(B)+4{S}_{\mathrm{HH}}(A){S}_{\mathrm{HH}}(B)
$$

其中第二项代表 HOMO 自贡献部分，第一项称为 ${f}_{AB}^{-}$，即 ${f}_{AB}^{-}=4\sum_{i<\mathrm{H}} {S}_{\mathrm{H}i}(A){S}_{\mathrm{H}i}(B)$。

DI 的右侧一阶导数为（$i$ 遍历所有双占据轨道）

$$
{\left( \frac{\partial {\delta}_{A,B}}{\partial N} \right)}^{+}={f}_{AB}^{+}=4\sum_{i\in \mathrm{occ}} {S}_{\mathrm{L}i}(A){S}_{\mathrm{L}i}(B)
$$

一阶对偶离域描述符定义为 ${f}_{AB}^{(1)}={f}_{AB}^{+}-{f}_{AB}^{-}$，表征 DI 对总电子数变化响应的不对称性，\>0 和 \<0 分别明确表示 LUMO 主导响应和 HOMO 主导响应。

$g$ 项与来自 HOMO 或 LUMO 的 DI 响应的二次贡献有关：

$$
{g}_{AB}^{+}={S}_{\mathrm{LL}}(A){S}_{\mathrm{LL}}(B)
$$

$$
{g}_{AB}^{-}={2S}_{\mathrm{HH}}(A){S}_{\mathrm{HH}}(B)
$$

$$
{\left( \frac{{\partial }^{2}{\delta}_{A,B}}{\partial {N}^{2}} \right)}^{+}=2{g}_{AB}^{+}
$$

$$
{\left( \frac{{\partial }^{2}{\delta}_{A,B}}{\partial {N}^{2}} \right)}^{-}={g}_{AB}^{-}
$$

当总电子数改变整数个时，DI 的变化可表示为

$$
{\Delta {\delta}_{AB}^{+}=f}_{AB}^{+}+{g}_{AB}^{+}
$$

$$
{\Delta {\delta}_{AB}^{-}=f}_{AB}^{-}+\frac{3}{2}{g}_{AB}^{-}
$$

应强调 $\Delta {\delta}_{AB}^{+}$ 和 $\Delta {\delta}_{AB}^{-}$ 只是 DI 准确变化的近似，准确变化可分别用有限差分计算为 ${\delta}^{+}=\delta\left( N+1 \right)-\delta(N)$ 和 ${\delta}^{-}=\delta\left( N \right)-\delta(N-1)$。

二阶对偶离域描述符定义为 ${f}_{AB}^{(2)}=\Delta {\delta}_{AB}^{+}-\Delta {\delta}_{AB}^{-}$，对应于得电子与失电子所致 DI 响应的不对称性。

当 HOMO 和/或 LUMO 简并时，上述各项按下式计算以考虑简并：

$$
{f}_{AB}^{+}=\frac{1}{{n}_{\mathrm{L}}}\sum_{l\in \mathrm{L}} {f}_{AB}^{+(l)} {f}_{AB}^{-}=\frac{1}{{n}_{\mathrm{H}}}\sum_{h\in \mathrm{H}} {f}_{AB}^{-(h)}
$$

$$
{g}_{AB}^{+}=\frac{1}{{n}_{\mathrm{L}}}\sum_{l\in \mathrm{L}} {g}_{AB}^{+(l)} {g}_{AB}^{-}=\frac{1}{{n}_{\mathrm{H}}}\sum_{h\in \mathrm{H}} {g}_{AB}^{-(h)}
$$

其中 $n_{\mathrm{L}}$ 和 $n_{\mathrm{H}}$ 分别为 LUMO 和 HOMO 的简并度，$l$ 和 $h$ 分别遍历所有简并的 LUMO 和 HOMO。带 ($l$) 或 ($h$) 上标的项指仅将 $l$ 视为 LUMO、将 $h$ 视为 HOMO 时计算的项。注意，计算 ${f}_{AB}^{-(h)}$ 时，轨道指标只遍历不属于简并 HOMO 的占据轨道。

### **用法**

Multiwfn 能计算体系中任意化学键的 ${f}_{AB}^{+}$、${f}_{AB}^{-}$、${f}_{AB}^{(1)}$、${g}_{AB}^{+}$、${g}_{AB}^{-}$、${f}_{AB}^{(2)}$。体系应为闭壳层，启动 Multiwfn 时应使用包含基函数信息的波函数文件（*例如* .fch、.molden）作为输入。

该功能对应主功能 22 的子功能 11。进入后，通常应选择选项 1 或选项 2，分别用原子空间的 AIM 划分或 Hirshfeld 划分计算 AOM，然后输入待研究的化学键，结果会立即显示在屏幕上。值得注意的是，若用 Hirshfeld 划分生成 AOM，所得 DI 也对应于模糊键级（[3.11.6 节](sec-3-11-bond-order-analysis.md#3116-模糊键级fuzzy-bond-order-7)），研究的就是模糊键级对 $N$ 的响应。

若已有由模糊分析模块或盆分析模块导出的、包含当前体系所有 MO 的 AOM 的 .txt 文件，在此功能中也可直接选择选项 3 载入使用，从而不在此处计算 AOM。注意，用模糊或盆分析模块生成 AOM 之前，应将 *settings.ini* 中的“ispecial”设为 3，否则 AOM 只涉及占据轨道。

例子见[4.22.6 节](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md#4226-计算对偶离域描述符-dual-delocalization-descriptor-ddd-的例子)。
