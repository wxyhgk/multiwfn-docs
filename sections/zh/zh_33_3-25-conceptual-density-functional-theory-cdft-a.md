# 概念密度泛函理论 (CDFT) 分析

> Multiwfn manual, p.341–353.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.341 -->



本分析的例子见 4.21.4 节。


## 3.25 概念密度泛函理论 (CDFT) 分析


## (22)

由 Robert Parr 创立并由众多研究者拓展的概念密度泛函理论 (conceptual density functional theory，CDFT) 是旨在揭示化学体系反应活性的理论框架。CDFT 包含众多概念和量，其中一些可用于预测有利反应位点和反应特征，一些可比较不同化学物种间的反应性。由于 CDFT 在量子化学中的高流行度和重要作用，以及有如此多有意义的相关量，我相信开发一个用最少步骤计算 CDFT 中所有常用量的模块非常有用。

在本节 Part 1 中，我将简要描述经本模块可研究的所有量的定义；然后在 Part 2 中，我将展示如何使用本模块。本模块能够计算所谓轨道加权量，将在 Part 3 中专门描述。

注意，除 CDFT 外，Multiwfn 还支持许多其他揭示反应位点的方法，概述见 4.A.4 节。

若本节所述功能用于你的研究，请不仅引用 Multiwfn 的原始论文，而且引用如下书章节，该章全面介绍了本模块的特点和实现：

Tian Lu, Qinxue Chen, Realization of Conceptual Density Functional Theory and Information-Theoretic Approach in Multiwfn Program. In Conceptual Density Functional Theory, WILEY-VCH GmbH: Weinheim (2022); pp 631-647. DOI: 10.1002/9783527829941.ch31


### 3.25.1 理论

要得到下面所有量，必须有 N、N+1 和 N-1 电子态的电子能量 (E) 和电子密度。对 N 电子态优化的几何用于所有计算。N 通常指化学体系在其最稳定状态所带电子数。

➢ 全局指标

- 第一垂直电离势 (I1)：E(N-1) − E(N)
- 第一垂直电子亲和能 (A)：E(N) − E(N+1)
- Mulliken 电负性 (χ)：(I1+A)/2
- 化学势 (μ)：−χ
- 硬度 (η)：I1−A，亦等价于基本带隙。见 J. Am. Chem. Soc., 105, 7512 (1983)。注意按许多 CDFT 论文采用的惯例，η 原始定义中 1/2 的前缀被略去。

<!-- p.342 -->


- 软度 (Softness) (S)：1/η。见 Proc. Nati. Acad. Sci., 82, 6723 (1985)
- 亲电性指数 (Electrophilicity index) (ω)：μ2/(2η)。见 J. Am. Chem. Soc., 121, 1922 (1999)
- 亲核性指数 (Nucleophilicity index) (NNu)：EHOMO(Nu) − EHOMO(TCE)，其中 Nu 表示亲核试剂，TCE 表示四氰基乙烯，其 HOMO 能量几乎是所有有机分子中最低的，因此被选作参考体系。见 J. Org. Chem., 73, 4615 (2008)。

➢ 实空间函数 (Real space functions)

- Fukui 函数 f(r) 与对偶描述符 (dual descriptor) Δf(r)：详细介绍见 4.5.4 节
- 局域软度 (Local softness)：对于亲核、亲电、自由基进攻分别为 s+(r) = Sf +(r)、s−(r) = Sf −(r)、s0(r) = Sf 0(r)，其中 f(r) 为相应类型的 Fukui 函数。见 Proc. Nati. Acad. Sci., 82, 6723 (1985)

- 局域超软度 (Local hyper-softness)：s(2)  S2Δf(r)，见 J. Math. Chem., 62, 461 (2024)
- 局域亲电性指数 (Local electrophilicity index)：𝜔loc(𝐫) = 𝜔𝑓+(𝐫)

- 局域亲核性指数 (Local nucleophilicity index)：𝑁Nu loc(𝐫) = 𝑁Nu𝑓−(𝐫) ➢ 原子指数 (Atom indices)

- 凝聚 Fukui 函数 (Condensed Fukui function) (fA) 与对偶描述符 (dual descriptor) (ΔfA)：详细介绍见 4.7.3 节

- 凝聚局域软度 (Condensed local softness) 对于亲核进攻：𝑠𝐴 + 对于亲电进攻：𝑠𝐴 − 对于自由基进攻：𝑠𝐴 0
- 相对亲电性指数 (Relative electrophilicity index)：𝑠𝐴 −，见 J. Phys. Chem. A, 102, 3746 (1998)
- 相对亲核性指数 (Relative nucleophilicity index)：𝑠𝐴 +，见 J. Phys. Chem. A, 102, 3746 (1998)
- 凝聚局域亲电性指数 (Condensed local electrophilicity index)：𝜔𝐴= 𝜔𝑓𝐴 + = 𝑆𝑓𝐴 −= 𝑆𝑓𝐴 0 = 𝑆𝑓𝐴 −/𝑠𝐴 +/𝑠𝐴 +

(2) ≈𝑆2∆𝑓𝐴 ➢ 键对偶描述符 (Bond dual descriptor) (BDD) BDD 是为每根键定义的指数，负（正）BDD 意味着该键是亲核性（亲电性）的，越负（正），亲核性（亲电性）越强
- 凝聚局域亲核性指数 (Condensed local nucleophilicity index)：𝑁Nu −
- 凝聚局域超软度 (Condensed local hyper-softness)：𝑠𝐴 𝐴= 𝑁Nu𝑓𝐴

BDD 本质上是在外势不变条件下键级 (P) 对电子数的一阶导数。根据 J. Math. Chem., 63, 1588 (2025)，利用有限差分近似，键 A-B 的 BDD 可计算为 𝐵𝐷𝐷𝐴,𝐵= 𝑓𝐴,𝐵 + 和 𝑓𝐴,𝐵 − 是两种类型的键 Fukui 函数，按下式计算 + −𝑓𝐴,𝐵 −，其中 𝑓𝐴,𝐵


$$f_{A,B}^{+}=P_{A,B}(N+1)-P_{A,B}(N)$$

<!-- formula-ocr: formula_p342_231.png 已替换为LaTeX, 原图保留备查 -->

在 J. Math. Chem., 63, 1588 (2025) 中作者采用了基于原子自然轨道的 Wiberg 键级作为 P，但在当前 Multiwfn 的实现中，采用基于 Hirshfeld 分割的模糊键级 (fuzzy bond order)（详见 3.11.6 节）作为 P 来计算 BDD，因为该键级对基组不敏感（在这方面远优于 Mayer 键级），表现合理（根据我的测试），且相对容易实现。


<!-- p.343 -->



➢ ωcubic 亲电性指数 (ωcubic electrophilicity index) 在 J. Phys. Chem. A, 124, 2090 (2020) 中引入的亲电性指数 ωcubic 有些特殊，它还依赖于 N-2 电子态。它比前述

亲电性指数 ω 包含更高阶的项。其定义为


$$\omega_{cubic}=\omega\left(1+\frac{\mu}{3\eta^{2}}\gamma\right)$$

<!-- formula-ocr: formula_p343_232.png 已替换为LaTeX, 原图保留备查 -->

实际计算时为

$$\omega_{cubic}=\frac{\left(\mu_{cubic}\right)^{2}}{2\eta_{cubic}}\left[1+\frac{\mu_{cubic}}{3\left(\eta_{cubic}\right)^{2}}\gamma_{cubic}\right]$$

其中

$$\mu_{cubic}=(1/6)(-2A-5I_{1}+I_{2})$$

$$\eta_{cubic}=I_{1}-A$$

$$\gamma_{cubic}=2I_{1}-I_{2}-A$$

其中 I2 为第二垂直电离势，定义为 E(N-2) − E(N-1)。相应地，存在凝聚局域亲电性指数的立方形式 𝜔cubic +。在 J. Phys. Chem. A, 124, 2090 (2020) 中表明，卤键二聚体 R-X···NH3 中卤素原子（因其 σ-hole 而表现为 Lewis 酸）的 𝜔cubic 𝐴 值与计算的结合能具有极好的相关性（但请注意，他们采用的是 AIM 分割原子空间，而非本模块所用的 Hirshfeld 分割）。𝐴= 𝜔cubic𝑓𝐴

➢ 亲电描述符 (Electrophilic descriptor) (ε) 亲电描述符 (ε) 在 Int. J. Quantum Chem., 124, e27366 (2024) 中被引入，用由 35 个有机分子组成的测试集表明，它与 Mayr 亲电参数 (E) 的相关性显著优于

亲电性指数 (ω)。与仅基于体系能量二阶 Taylor 展开推导的 ω 不同，ε 的推导基于三阶展开，这使得 ε 显式地包含超硬度 (hyperhardness)。与 ωcubic 一样，ε 的计算也依赖于 N-2 电子态。

计算 ε 的工作方程如下


$$\varepsilon=\chi\left(\frac{\phi}{\gamma}\right)-\left(\frac{\phi}{\gamma}\right)^{2}\left(\frac{\eta}{2}+\frac{\phi}{6}\right)$$

其中

$$\phi=\sqrt{\eta^{2}-2\gamma\mu}-\eta$$

需要注意的是，上述方程中所涉及的 η、γ、χ、μ 应以与前述不同的方式计算，即


$$\begin{aligned}&\mu=a\\&\chi=-a\\&\eta=2(b-ac)\\&\gamma=-3c(b-ac)\\ \end{aligned}$$

<!-- formula-ocr: formula_p343_234.png 已替换为LaTeX, 原图保留备查 -->


<!-- p.344 -->



其中


$$b=\frac{I_{1}-A^{\prime}}{2}-\frac{I_{1}+A^{\prime}}{2}c$$

<!-- formula-ocr: formula_p344_235.png 已替换为LaTeX, 原图保留备查 -->

其中 A’ = E(N+1) − E(N)，即电子亲和势，但符号与标准定义相差一个负号。

➢ Fukui 势 (Fukui potential) 与对偶描述符势 (dual descriptor potential) Fukui 势的定义与物理意义在 J. Phys. Chem. A, 115, 2325 (2011) 和 Int. J. Quantum Chem., 101, 520 (2005) 中有仔细讨论。Fukui 势是对 ESP 的补充，可用于理解当电子转移不可忽略时化学反应早期的能量变化。例如，当亲电试剂受到亲核试剂进攻时，亲电试剂感受到的由亲核试剂产生的外势为

𝑣𝑁−phile(𝐫) ≈𝑉𝑁−phile ESP(𝐫) −∆𝑁∫ 𝑓𝑁−phile −(𝐫′) |𝐫−𝐫′|d𝐫′

其中 ΔN 为从亲电试剂转移到亲核试剂的电子数（在此情形下为负值），𝑓𝑁−phile − 为亲核试剂的 Fukui 函数 f−。三类 Fukui 势定义

如下


$$v_{N-\mathrm{p h i l e}}(\mathbf{r})\approx V_{N-\mathrm{p h i l e}}^{\mathrm{E S P}}(\mathbf{r})-\Delta N\int\frac{f_{N-\mathrm{p h i l e}}^{-}(\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime}$$

<!-- formula-ocr: formula_p344_236.png 已替换为LaTeX, 原图保留备查 -->

ESP 仅能在假设没有电子转移的前提下预测由静电效应主导的区域选择性，然而，显然该假设对一般化学反应而言远非成立（但对许多非共价相互作用基本成立）。显然，在研究一般反应时，尤其是对有显著电子转移的反应，应更多关注 Fukui 势。

如 J. Phys. Chem. A, 115, 2325 (2011) 所强调的“决定反应位点的是 Fukui 势的值，而非 Fukui 函数本身的值”，Fukui 势在预测区域选择性方面比 Fukui 函数更严格。然而，Fukui 势不如 Fukui 函数流行，因为它们的分布特征通常彼此吻合，而计算 Fukui 势需要计算两次 ESP，比计算两次电子密度要昂贵得多。根据 Fukui 函数的有限差分定义，例如，𝑉𝑓− 可计算为


$$V_{f^{-}}(\mathbf{r})=\int\frac{f^{-}(\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime}=\int\frac{\rho_{N}(\mathbf{r}^{\prime})-\rho_{N-1}(\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime}=V_{N-1}^{\mathrm{ESP}}(\mathbf{r})-V_{N}^{\mathrm{ESP}}(\mathbf{r})$$

<!-- formula-ocr: formula_p344_237.png 已替换为LaTeX, 原图保留备查 -->

此外，对偶描述符势 (dual descriptor potential) (DDP) 在 J. Math. Chem., 62, 1094 (2024) 中被引入，其定义为


$$D D P(\mathbf{r})=\int\frac{\Delta f(\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime}=\int\frac{f^{+}(\mathbf{r}^{\prime})-f^{-}(\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime}=V_{f^{+}}(\mathbf{r})-V_{f^{-}}(\mathbf{r})$$

<!-- formula-ocr: formula_p344_238.png 已替换为LaTeX, 原图保留备查 -->

与常常有许多节面而妨碍讨论的对偶描述符不同，DDP 的分布光滑得多，使研究者更容易识别优先反应位点。

与 Fukui 函数一样，𝑉𝑓+ 在某区域越正，该区域越


<!-- p.345 -->



可能发生亲核反应，而 𝑉𝑓− 在某区域越正，该区域越

可能发生亲电反应。与对偶描述符类似，DPP 在某区域越正、越负，该区域分别越易于发生亲核和亲电进攻。


### 3.25.2 用法 (Usage)

要使用本模块，即主功能 22 (main function 22)，启动 Multiwfn 后载入的文件相对任意，唯一要求是该文件中的原子信息与所研究的体系相同。

进入本模块后，你将看到一个菜单，其中选项 2 (Option 2)、选项 3 (Option 3) 和选项 9 (Option 9) 用于计算上述量。在使用它们之前，一般应在当前目录下提供 N.wfn、N-1.wfn 和 N+1.wfn，分别包含当前体系 N、N-1 和 N+1 态的波函数和电子能量，几何结构必须相同且对应于 N 态的优化几何。三个文件的计算级别也必须相同。若三个 .wfn 文件中有缺失，Multiwfn 会要求你手动输入相应态的 .wfn 文件路径（.wfx、.fch 和 .mwfn 文件也被允许，因为它们同样携带波函数和电子能量信息）。

选项 2 (Option 2)：用于计算所有前述全局指数和原子指数，结果将导出到当前目录下的 CDFT.txt。如 4.7.3 节所述，Hirshfeld 方法是计算凝聚 Fukui 函数乃至其它相关原子指数的理想选择，因此会自动计算 Hirshfeld 电荷并用于计算所有原子指数。亲核性指数及其局域版本依赖于 TCE 的 HOMO 能量，应使用与当前体系相同的级别计算，注意本模块中打印的这些指数简单地采用了常用 B3LYP/6-31G* 级别下计算的 EHOMO(TCE) = -0.335198 Hartree（显然，若你想要更可靠的结果且当前计算级别不是 B3LYP/6-31G*，你应自行计算 EHOMO(TCE) 然后再手动计算这些指数）。

选项 3 (Option 3)：用于计算 Fukui 函数、对偶描述符及与其相关函数的格点数据，然后可直接可视化其等值面图，格点数据可导出为当前目录下的 cube 文件。在此选项中你可以设置乘到所算格点数据上的比例因子。例如，若你将比例因子设为选项 2 (Option 2) 输出的全局软度，则

缩放后的 f −(r) Fukui 函数将对应于 s−(r)。

选项 9 (Option 9)：与选项 3 (Option 3) 类似，但用于计算 Fukui 势和对偶描述符势的格点数据。由于每个带电态都需要计算 ESP 格点数据，代价常常较高，你应选择合适的格点设置以免过于耗时。

选项 10 (Option 10)：用于计算键对偶描述符 (bond dual descriptor)。Multiwfn 将依次载入不同电子态的 .wfn 文件并计算模糊键级 (fuzzy bond order)，最后计算并打印 BDD 值。代价一般很低。

.wfn 文件的生成 你可以手动准备选项 2 (Option 2) 和选项 3 (Option 3) 所用的 .wfn 文件，或者，你也可以用本模块的选项 1 (Option 1) 自动完成准备工作。

选择选项 1 (Option 1) 后，将提示你输入 Gaussian 单点任务的关键词，然后 Multiwfn 依次要求你输入 N、N+1 和 N-1 态的电荷与自旋多重度，随后将在当前目录下生成 Gaussian 单点输入文件 N.gjf、N+1.gjf 和 N-1.gjf（这些文件中的几何结构对应于 Multiwfn 输入文件中的几何）。然后，你可以手动用 Gaussian 运行它们以得到 N.wfn、N+1.wfn 和 N-1.wfn，或者若你的电脑上已安装 Gaussian，可直接让 Multiwfn 调用 Gaussian 来计算它们（此时 `settings.ini` 中的 "gaupath" 参数必须已设为 Gaussian 可执行文件的实际路径），计算完成后三个 .wfn 文件将出现在当前目录下。

有时我们需要使用混合基组，此时应在当前目录下准备一个名为 basis.txt 的文件，其中记录基组的定义（也可能附带赝势定义）。若输入的关键词包含 "gen" 或 "genecp"，则 basis.txt 的内容会自动追加到所生成的 .gjf 文件末尾。

Multiwfn 也能生成 ORCA 输入文件以产生三个 .wfn 文件。你应选择选项 -2 (Option -2) 并选择 ORCA，然后选择选项 1 (Option 1) 将生成 N.inp、N-1.inp 和 N+1.inp。若你已在 `settings.ini` 中将 “orcapath” 设为 ORCA 可执行文件的实际路径，你可直接让 Multiwfn 调用 ORCA 运行它们以产生 N.wfn、N-1.wfn 和 N+1.wfn；或者，你也可以手动用 ORCA 运行它们，然后将所得的 N.wfn、N-1.wfn 和 N+1.wfn 放到当前目录下。

要用本模块研究大有机体系，通常我建议使用 B3LYP/6-31G* 级别，因为该级别便宜，而所得量的质量已足够令人满意。

关于计算 ωcubic 与 ε 的注记 默认情况下，Multiwfn 不计算 ωcubic 和 ε，因为它们依赖于 N-2 电子态。若你需要它们，应先选择选项 -1 (Option -1) 将状态切换为 "Yes"。然后你可以用选项 1 (Option 1) 帮你准备 N、N+1、N-1、N-2 电子态的 .wfn 文件，或手动提供它们。然后选择选项 2 (Option 2) 后，所得的 CDFT.txt 文件将包含凝聚局域


<!-- p.346 -->



任务，然后 Multiwfn 依次要求你输入 N、N+1 和 N-1 态的电荷与自旋多重度，随后将在当前目录下生成 Gaussian 单点输入文件 N.gjf、N+1.gjf 和 N-1.gjf（这些文件中的几何结构对应于 Multiwfn 输入文件中的几何）。然后，你可以手动用 Gaussian 运行它们以得到 N.wfn、N+1.wfn 和 N-1.wfn，或者若你的电脑上已安装 Gaussian，可直接让 Multiwfn 调用 Gaussian 来计算它们（此时 `settings.ini` 中的 "gaupath" 参数必须已设为 Gaussian 可执行文件的实际路径），计算完成后三个 .wfn 文件将出现在当前目录下。

有时我们需要使用混合基组，此时应在当前目录下准备一个名为 basis.txt 的文件，其中记录基组的定义（也可能附带赝势定义）。若输入的关键词包含 "gen" 或 "genecp"，则 basis.txt 的内容会自动追加到所生成的 .gjf 文件末尾。

Multiwfn 也能生成 ORCA 输入文件以产生三个 .wfn 文件。你应选择选项 -2 (Option -2) 并选择 ORCA，然后选择选项 1 (Option 1) 将生成 N.inp、N-1.inp 和 N+1.inp。若你已在 `settings.ini` 中将 “orcapath” 设为 ORCA 可执行文件的实际路径，你可直接让 Multiwfn 调用 ORCA 运行它们以产生 N.wfn、N-1.wfn 和 N+1.wfn；或者，你也可以手动用 ORCA 运行它们，然后将所得的 N.wfn、N-1.wfn 和 N+1.wfn 放到当前目录下。

要用本模块研究大有机体系，通常我建议使用 B3LYP/6-31G* 级别，因为该级别便宜，而所得量的质量已足够令人满意。

关于计算 ωcubic 和 ε 的注记 默认情况下，Multiwfn 不计算 ωcubic 和 ε，因为它们依赖于 N-2 电子态。如果你需要它们，你应先选择选项 -1 (Option -1) 将状态切换为 "Yes"。然后你可以用选项 1 (Option 1) 来帮你准备 N、N+1、N-1、N-2 电子态的 .wfn 文件，或手动提供它们。然后在选择选项 2 (Option 2) 后，所得的 CDFT.txt 文件将包含凝聚局域

ωcubic、全局 ωcubic、ε 以及 I2。

用本模块计算苯酚各种 CDFT 量的例子见 4.22.1 节。计算马来酸酐 Fukui 势和对偶描述符势的例子见 4.22.4 节。计算键对偶描述符的例子见 4.22.5 节。


### 3.25.3 专题 1：轨道加权 Fukui 函数与对偶

### 描述符 (Special topic 1: Orbital-weighted Fukui function and dual descriptor)

理论 (Theory) 原始定义的 Fukui 函数和对偶描述符在前线分子轨道（准）简并时表现不好。例如，当 HOMO 与 HOMO-1 能量非常

接近或完全相同时，Fukui 函数 f − 可能无法给出有意义的结果或结果完全误导；此外，当体系具有点群对称性时，例如

C60 富勒烯，f − 的分布通常与分子对称性不一致，这显然是出乎意料的观察。

为了解决这些问题，在 J. Comput. Chem., 38, 481 (2017) 中，作者提出了


<!-- p.347 -->



轨道加权 Fukui 函数 (orbital-weighted Fukui function)，在 J. Phys. Chem. A, 123, 10556 (2019) 中，他们进一步提出了轨道加权对偶描述符 (orbital-weighted dual descriptor)，总结如下（𝑓𝑤0 由我定义）

$$\begin{array}{r l r l}&{f_{w}^{+}(\mathbf{r})=\displaystyle\sum_{i=\mathrm{L U M O}}^{\infty}w_{i}\mid\varphi_{i}(\mathbf{r})\mid^{2}}&{}&{w_{i}=\frac{\exp[-\left(\frac{\mu-\varepsilon_{i}}{\Delta}\right)^{2}]}{\displaystyle\sum_{i=\mathrm{L U M O}}^{\infty}\exp[-\left(\frac{\mu-\varepsilon_{i}}{\Delta}\right)^{2}]}}\end{array}$$

$$\begin{array}{r l}{f_{w}^{-}(\mathbf{r})=\displaystyle\sum_{i}^{\mathrm{H O M O}}w_{i}\mid\varphi_{i}(\mathbf{r})\mid^{2}}&{{}\quad w_{i}=\frac{\exp[-\left(\frac{\mu-\varepsilon_{i}}{\Delta}\right)^{2}]}{\displaystyle\sum_{i}^{\mathrm{H O M O}}\exp[-\left(\frac{\mu-\varepsilon_{i}}{\Delta}\right)^{2}]}}\end{array}$$

i

fff www 0 ( )[( )( )]/ 2 rrr =+ +−

Δ=− fff www ( )( )( ) rrr +−

其中 εi 和 φi 为轨道 i 的能量与波函数；μ 为化学势，在上述公式中近似计算为 (EHOMO+ELUMO)/2。Δ 为可调参数，原则上其最佳值是能使函数具有理想局域反应性预测能力的值。

显然最合适的 Δ 依赖于实际体系，通常 0.1 Hartree 是值得一试的猜测。若你发现此值下的轨道加权函数表现不好，你可以尝试适当改变它并重新计算。

与 f − 的冻结轨道近似形式，即 f −(r)=|φHOMO(r)|2 相比，𝑓𝑤− 的优点在于它以不同权重考虑了所有轨道。由表达式可知，低占据轨道能量越接近 HOMO 能量，其权重越大。显然简并轨道具有相同权重。公式中涉及的 Gaussian 函数

表现为衰减函数，Δ 越大，低占据轨道对 𝑓𝑤− 的贡献越高。当 HOMO 与 HOMO-1 之间能量差显著时，将没有理由

用 𝑓𝑤− 代替 f −。对 𝑓𝑤+、𝑓𝑤0 和 ∆𝑓𝑤 情形类似。

用法 (Usage) 由于轨道加权函数涉及虚轨道，你应用 .mwfn、.fch、.molden 或 .gms 文件作为输入文件。通常，输入文件中的几何结构应对应于 N 电子态的优化几何；但研究非平衡结构也是可能的，例如内禀反应坐标 (IRC) 上的某一点。

仅闭壳层单行列式波函数可接受。若你打算计算 𝑓𝑤+、𝑓𝑤0 和 ∆𝑓𝑤，不应使用弥散函数，因为它们利用虚轨道，而使用弥散函数时其化学意义可能被严重破坏。

在主功能 22 (main function 22) 中，有四个选项与轨道加权计算相关：

- 选项 4 (Option 4)：设置后续轨道加权计算中使用的 Δ 参数
- 选项 5 (Option 5)：打印最高的 10 个权重（即上述公式中的 {w}），此选项有助于检查当前 Δ 参数是否合理，并帮助用户更好地理解轨道加权方法的工作方式

- 选项 6 (Option 6)：计算凝聚的 𝑓𝑤+、𝑓𝑤−、𝑓𝑤0 和 Δ𝑓𝑤 值，换言之，计算这些函数在 Hirshfeld 原子空间中的积分。该结果有助于定量考察各原子上这些函数的净量。默认的径向和角度积分点通常已足够精细，若你发现凝聚 𝑓𝑤+ 或 𝑓𝑤− 之和明显偏离 1.0，你应在 `settings.ini` 中将 "iautointgrid" 参数设为 0，然后适当增大 "radpot" 和 "sphpot" 参数。


<!-- p.348 -->



- 选项 7 (Option 7)：计算 𝑓𝑤+、𝑓𝑤−、𝑓𝑤0 和 Δ𝑓𝑤 函数的格点数据，然后你可直接可视化其等值面或将其导出为 cube 文件，以便用 VMD 和 ChimeraX 等第三方软件渲染。

用本模块计算轨道加权 Fukui 函数和轨道加权对偶描述符的例子见 4.22.2 节。


### 3.25.4 专题 2：基于电子密度的（准）简并 Fukui 函数与对偶

### 描述符 (Special topic 2: (Quasi-)degenerate Fukui function and dual descriptor based on electron density)

### 3.25.4.1 闭壳层情形 (Closed-shell case)

理论 (Theory) 在上一节，我介绍了轨道加权 Fukui 函数和对偶描述符，它们适用于前线分子轨道（准）简并的情形。但它们基于轨道近似定义，即没有考虑轨道弛豫效应，而该效应并非总能安全忽略。在 J. Comput. Chem., 37, 2279 (2016) 中，提出了适用于（准）简并 HOMO/LUMO 情形的另一形式的 Fukui 函数和对偶描述符，该形式直接基于电子密度定义，即如同原始 Fukui 函数和对偶描述符一样完全考虑了轨道弛豫效应。这种基于电子密度的（准）简并 Fukui 函数和对偶描述符将分别称为

fQ 和 ΔfQ。

fQ 的思想非常简单。若在 N 电子态 LUMO 与 HOMO 的简并度分别为 p 和 q，则三类 fQ 按下式计算

fp Q ++ ( )( )( ) rrr −= ρρ NpN

fq Q −− ( )( )( ) rrr −= ρρ NN q

fff 0QQQ ( )[( )( )] / 2 rrr =+ +−

ΔfQ 可如常基于 𝑓Q + 和 𝑓Q − 计算

QQQ( )( )( )fff+−Δ=−rrr

显然，若 HOMO 与 LUMO 均非简并，则 fQ 和 ΔfQ 将分别等价于原始形式的 Fukui 函数和对偶描述符 f 与 Δf。

要合理计算 fQ 和 ΔfQ，正确确定 p 和 q 至关重要。通常可通过考察几个最低未占据 MO 和几个最高占据 MO 的能量来指定。若某占据（未占据）MO 与 HOMO (LUMO) 的能量差很小，例如小于 0.01 eV，则可视为简并。显然，判断轨道简并没有严格的能量阈值，在某些情形下你可能需要综合多种因素判断，例如 HOMO-LUMO 间隙、实际计算结果的合理性、轨道形状等。

注意 fQ 和 ΔfQ 仅对闭壳层情形定义。Multiwfn 不仅能计算 fQ 和 ΔfQ，还能基于它们计算


<!-- p.349 -->



### 3.25.1 节所述的局域性质（ωcubic 除外）。例如，考虑简并的局域软度为全局软度与 fQ 的乘积。注意其中涉及的第一垂直电子亲和势 (VEA)

和垂直电离势 (VIP) 仍如常计算，即 VEA = E(N) − E(N+1)，VIP = E(N-1) − E(N)。

计算 N+p 和 N-q 态波函数文件时必须正确选择自旋多重度，通常应设为 p+1 和 q+1，详见 J. Comput. Chem., 37, 2279 (2016) 中的详细讨论。该设置通常能保证附加（脱离）电子平均进入（离开）所有简并的 LUMO (HOMO)。

用法 (Usage) 在主功能 22 (main function 22) 中，p 和 q 默认均为 1，即不考虑前线分子轨道 (FMO) 的简并。要手动设置 p 和 q 从而在后续计算中考虑（准）简并效应，你应先选择选项 “-3 设置 FMO 简并度 (Set degree of FMO degeneracy)”。然后屏幕上将列出 10 个最低未占据 MO 和 10 个最高占据 MO 的信息（若输入文件包含波函数信息），你应根据所列 MO 能量合理输入 p 和 q。

设置 p 和 q 后，你可用选项 1 (Option 1) 让 Multiwfn 帮你生成 Gaussian 或 ORCA 代码单点任务的输入文件，分别对应 N、N+p 和 N-q 态，将要求你输入这些态的净电荷与自旋多重度。此外，若 p 或 q 不等于 1，则 Multiwfn 还会询问是否也为 N+1 和/或 N-1 态生成输入文件，因为在选项 2 (Option 2) 中计算第一 VIP、VEA 及相关量需要 E(N+1) 和 E(N-1)。运行这些输入文件后，将产生各态的 .wfn 文件。当然，你也可以用自己喜欢的任重量子化学程序手动生成各态的波函数文件。

最后，你可用相应选项计算 CDFT 框架下定义的各种量或函数，输出内容与默认非简并情形完全相同，只是当前情形已合理考虑了 p 和 q。注意若 p 或 q 不等于 1，同时当前目录下没有 N+1.wfn 或 N-1.wfn，则选项 2 (Option 2) 将不计算输出与第一 VIP 和 VEA 相关的量。

例子见 4.22.3 节。

### 3.25.4.2 开壳层情形 (Open-shell case)

理论 (Theory) 对开壳层情形，Martínez Araya 在 Chem. Phys. Lett., 506, 104 (2011) 中基于自旋极化概念 DFT 的形式提出了计算对偶描述符的工作方程。这些方程随后被进一步推广（私人交流）并总结如下，其中 ∆𝑁𝑆 对应于自旋数变化 (𝑁𝑆= 𝑁𝛼−𝑁𝛽)，B 表示外磁场；𝑝α

和 𝑝𝛽 分别为 LUMO(α) 和 LUMO(β) 的简并度；𝑞𝛼 和 𝑞𝛽 分别为

HOMO(α) 和 HOMO(β) 的简并度。

计算 𝑓+ = ( 𝜕𝜌(𝐫) 𝜕𝑁) + 𝑣(𝐫),𝐁(𝐫) 的不同形式，即自旋多重度增加、减小、

和近似不变：


$$f^{+}_{\Delta N_{S}<0}(\mathbf{r})=\frac{\rho_{N+p_\beta}(\mathbf{r})-\rho_{N}(\mathbf{r})}{p_\beta}$$

<!-- formula-ocr: formula_p349_239.png 已替换为LaTeX, 原图保留备查 -->


<!-- p.350 -->




$$f^{+}_{\Delta N_{S}>0}(\mathbf{r})=\frac{\rho_{N+p_{\alpha}}(\mathbf{r})-\rho_{N}(\mathbf{r})}{p_{\alpha}}$$

<!-- formula-ocr: formula_p350_240.png 已替换为LaTeX, 原图保留备查 -->

计算 𝑓−= ( 𝜕𝜌(𝐫) 𝜕𝑁) − 𝑣(𝐫),𝐁(𝐫) 的不同形式：


$$f_{\Delta N_{S}<0}^{-}(\mathbf{r})=\frac{\rho_{N}(\mathbf{r})-\rho_{N-q_{\alpha}}(\mathbf{r})}{q_{\alpha}}$$

<!-- formula-ocr: formula_p350_241.png 已替换为LaTeX, 原图保留备查 -->

计算对偶描述符的不同形式：

−(𝐫) 原则上，Δ𝑓Δ𝑁𝑆≈0 应是最理想的选择，因为它遵循 −(𝐫) Δ𝑓Δ𝑁𝑆>0(𝐫) = 𝑓Δ𝑁𝑆>0 Δ𝑓Δ𝑁𝑆<0(𝐫) = 𝑓Δ𝑁𝑆<0 −(𝐫) Δ𝑓Δ𝑁𝑆≈0(𝐫) = 𝑓Δ𝑁𝑆≈0 +(𝐫) −𝑓Δ𝑁𝑆<0 +(𝐫) −𝑓Δ𝑁𝑆>0 +(𝐫) −𝑓Δ𝑁𝑆≈0

保持自旋数不变的限制。但还有两种仅分别涉及 α 和 β 电子变化而保持自旋数

不变的方式，文献中尚未考察。


$$f_{\Delta N_{S}>0}^{-}(\mathbf{r})=\frac{\rho_{N}(\mathbf{r})-\rho_{N-q_{\beta}}(\mathbf{r})}{q_{\beta}}$$

<!-- formula-ocr: formula_p350_242.png 已替换为LaTeX, 原图保留备查 -->

用法 (Usage) CDFT 模块的子功能 12 (Subfunction 12) 专用于计算上述所有函数。启动 Multiwfn 后，通常你应：

(1) 载入包含基函数信息和所有轨道的波函数文件 (2) 进入主功能 22 (main function 22) 的子功能 12 (subfunction 12) (3) 若该体系前线 MO 有简并，选择选项 1 (Option 1) 设置简并度 (4) 选择选项 2 (Option 2) 生成所有涉及电子态的 Gaussian 单点任务输入文件。然后你可以让 Multiwfn 调用 Gaussian 直接计算它们，或手动计算它们。然后将所得 .wfn 文件（与 .gjf 文件同名）放到当前目录下。

(5) 选择选项 3 (Option 3) 生成不同电子态电子密度的格点数据。在后处理菜单中，你可直接可视化所选形式的 Fukui 函数或对偶描述符的等值面图，或将相应格点数据导出为 .cub 文件。

例子见 4.22.3.3 节。

### 3.25.5 专题 3：亲核与亲电

### 超离域性 (Special topic 3: Nucleophilic and electrophilic superdelocalizabilities)

理论 (Theory)


<!-- p.351 -->



亲核与亲电离域性也称为亲核与亲电超离域性 (superdelocalizabilities)，由 Schüürmann 在 Environ. Toxicof. Chem., 9, 417 (1990) 和 Quant. Struct.-Act. Relat., 9, 326 (1990) 中提出，曾被用作构建定量构效关系 (QSAR) 方程的分子描述符。在 Schüürmann 的工作中，原子 A 的亲核超离域性 (DN) 与亲电超离域性 (DE) 分别定义为

$$D^{N}(A)=2\sum_{i}^{unocc}\sum_{\mu\in A}\frac{C_{\mu,i}^{2}}{\alpha-\varepsilon_{i}}$$

其中 εi 为分子轨道 i 的能量，α = (EHOMO + ELUMO)/2，μA 表示原子 A 的基函数 μ，C 为系数矩阵。显然，DN 和 DE 均为负值。

然而，Schüürmann 的超离域性表达式仅适用于采用正交基函数的半经验计算。在 Sci. Rep., 5, 13695 (2015) 中，提出了另一版本的亲电超离域性，它兼容非正交基函数。在该工作中表明，原子的亲电超离域性与其原子极化率密切相关。

上述超离域性定义基于分子轨道展开系数；相比之下，在 Multiwfn 中，超离域性基于原子空间的 Hirshfeld 分割计算，该形式更稳健且与弥散函数完全兼容。具体而言，在 Multiwfn 中，亲核与亲电超离域性按如下计算


$$D^{N}(A)=2\sum_{i}^{unocc}\frac{\Theta_{A,i}}{\alpha-\varepsilon_{i}}$$

<!-- formula-ocr: formula_p351_243.png 已替换为LaTeX, 原图保留备查 -->

其中 ΘA,i 为 Hirshfeld 方法计算的轨道 i 中原子 A 的组成，详见 3.10.5 节。Multiwfn 还计算不含 α 移位参数的超离域性，即


$$D^{N}(A)=2\sum_{i}^{unocc}\frac{\Theta_{A,i}}{\alpha-\varepsilon_{i}}$$

<!-- formula-ocr: formula_p351_244.png 已替换为LaTeX, 原图保留备查 -->

用法 (Usage) 由于超离域性涉及虚轨道，你应用 .mwfn、.fch、.molden 或 .gms 文件作为输入文件。仅闭壳层单行列式波函数可接受。若你打算计算 DN 和 DN0，不应使用弥散函数，因为它利用虚轨道，而使用弥散函数时其化学意义可能被严重破坏。

载入输入文件后，进入主功能 22 (main function 22)，然后选择选项 8 (Option 8)，你将得到所有原子的 DN、DE、DN0 和 DE0。输出示例 (examples\oxirane.fchk)：


```text
    Atom             D_N                D_E              D_N_0             D_E_0
    1(C )        -26.56182        -10.85916        -35.92863         -8.75591
```


<!-- p.352 -->




```text
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


### 3.25.6 专题 4：对偶离域描述符 (Special topic 4: Dual delocalization descriptor)

理论 (Theory) 对偶离域描述符 (dual delocalization descriptor) (DDD) 的理论由 Samir Kenouche 在 Phys. Chem. Chem. Phys., 28, 19133 (2026) 中提出。该方法定量描述了原子间离域指数 (DI) 对总电子数变化的响应。该理论与 3.25.1 节介绍的键对偶描述符 (BDD) 密切相关，本质上二者都展示了在得电子或失电子过程中电子共享程度如何变化。但 BDD 基于两电子态（N 与 N-1，或 N 与 N+1）之间键级的有限差分计算，而 DDD 具有解析形式，其计算仅依赖 N 态波函数，因此在计算代价上有优势。另一优势是 DDD 的分量使人能考察前线分子轨道对响应的作用，详见原文讨论。注意 DDD 理论基于冻结轨道近似 (FOA) 推导，且仅支持单行列式闭壳层波函数。

这里我描述 DDD 的关键思想与要素。该理论在 Ángyán-

Loos-Mayer (ALM) 形式的 DI (δ) 下推导：


$$\delta_{A,B}^{\mathrm{A L M}}=\sum_{i,j}\eta_{i}\eta_{j}S_{i j}(A)S_{i j}(B)$$

<!-- formula-ocr: formula_p352_245.png 已替换为LaTeX, 原图保留备查 -->

其中 η 为轨道占据数，S 为原子重叠矩阵 (AOM)，故 𝑆𝑖𝑗(𝐴) 对应于 MO i 与 MO j 在原子 A 空间中乘积的积分。i 和 j 遍历所有空间轨道。

DI 的导数在整数电子数处不连续。在 FOA 下并假设电子只能从 HOMO 离开，可证明 DI 的左侧一阶导数可表示为下式，它反映了 DI 随 N 减小以 HOMO 为主导的响应


$$\left(\frac{\partial\delta_{A,B}}{\partial N}\right)^{-}=4\sum_{i<H}S_{\mathrm{H}i}(A)S_{\mathrm{H}i}(B)+4S_{\mathrm{H H}}(A)S_{\mathrm{H H}}(B)$$

<!-- formula-ocr: formula_p352_246.png 已替换为LaTeX, 原图保留备查 -->

其中第二项代表 HOMO 自贡献部分，而第一项称为 𝑓𝐴𝐵 −，即 𝑓𝐴𝐵 −= 4 ∑𝑆H𝑖(𝐴)𝑆H𝑖(𝐵)𝑖<H。右侧一阶导数为 (i 遍历所有双占据轨道)


$$\left(\frac{\partial\delta_{A,B}}{\partial N}\right)^{+}=f_{A B}^{+}=4\sum_{i\in\mathrm{o c c}}S_{\mathrm{L}i}(A)S_{\mathrm{L}i}(B)$$

<!-- formula-ocr: formula_p352_247.png 已替换为LaTeX, 原图保留备查 -->

一阶对偶离域描述符定义为 𝑓𝐴𝐵 (1) = 𝑓𝐴𝐵 + −𝑓𝐴𝐵 −，它表征


<!-- p.353 -->



DI 对总电子数变化响应的不对称性，>0 和 <0 分别明确指示 LUMO 主导的响应和 HOMO 主导的响应。

g 项与来自 HOMO 或 LUMO 的 DI 响应的二次贡献有关：


$$\begin{aligned}\boldsymbol{g}_{AB}^{+}&=\boldsymbol{S}_{\mathrm{LL}}(A)\boldsymbol{S}_{\mathrm{LL}}(B)\\\boldsymbol{g}_{AB}^{-}&=2\boldsymbol{S}_{\mathrm{HH}}(A)\boldsymbol{S}_{\mathrm{HH}}(B)\\\left(\frac{\partial^{2}\delta_{A,B}}{\partial N^{2}}\right)^{+}&=2\boldsymbol{g}_{AB}^{+}\\ \left(\frac{\partial^{2}\delta_{A,B}}{\partial N^{2}}\right)^{-}&=\boldsymbol{g}_{AB}^{-}\end{aligned}$$

<!-- formula-ocr: formula_p353_248.png 已替换为LaTeX, 原图保留备查 -->

当总电子数改变整数个时，DI 的变化可表示为

必须强调 ∆𝛿𝐴𝐵 − 只是 DI 精确变化的近似，可分别用有限差分计算为 𝛿+ = 𝛿(𝑁+ 1) −𝛿(𝑁) 和 𝛿−=𝛿(𝑁) −𝛿(𝑁−1)。+ 和 ∆𝛿𝐴𝐵

−，它对应于加电子与去电子所致 DI 响应的不对称性。二阶对偶离域描述符定义为 𝑓𝐴𝐵 (2) = ∆𝛿𝐴𝐵 + −∆𝛿𝐴𝐵

当 HOMO 和/或 LUMO 简并时，上述各项按如下计算以考虑简并：


$$\begin{aligned}f_{AB}^{+}&=\frac{1}{n_{\mathrm{L}}}\sum_{l\in\mathrm{L}}f_{AB}^{+(l)}\quad&f_{AB}^{-}&=\frac{1}{n_{\mathrm{H}}}\sum_{h\in\mathrm{H}}f_{AB}^{-(h)}\\g_{AB}^{+}&=\frac{1}{n_{\mathrm{L}}}\sum_{l\in\mathrm{L}}g_{AB}^{+(l)}\quad&g_{AB}^{-}&=\frac{1}{n_{\mathrm{H}}}\sum_{h\in\mathrm{H}}g_{AB}^{-(h)}\end{aligned}$$

<!-- formula-ocr: formula_p353_249.png 已替换为LaTeX, 原图保留备查 -->

其中 nL 和 nH 为 LUMO 与 HOMO 的简并度，l 和 h 分别遍历所有简并的 LUMO 和 HOMO。带 (l) 或 (h) 上标的项指仅

−(ℎ)，轨道指标仅遍历不属于简并 HOMO 的占据轨道。将 l 视为 LUMO、h 视为 HOMO 计算所得。注意在计算 𝑓𝐴𝐵

用法 (Usage)

(2) 对体系中任一键。该体系应为闭壳层，启动 Multiwfn 时应用包含基函数信息的波函数文件（如 .fch、.molden）作为输入。Multiwfn 能计算 𝑓𝐴𝐵 +、𝑓𝐴𝐵 −、𝑓𝐴𝐵 (1)、𝑔𝐴𝐵 +、𝑔𝐴𝐵 −、𝑓𝐴𝐵

该功能对应于主功能 22 (main function 22) 的子功能 11 (subfunction 11)。进入后，通常你应选择选项 1 (Option 1) 或选项 2 (Option 2) 分别用原子空间的 AIM 分割或 Hirshfeld 分割计算 AOM，然后将要求你输入待研究的键，结果将立即显示在屏幕上。值得注意的是，若用 Hirshfeld 分割产生 AOM，所得 DI 也对应于模糊键级 (fuzzy bond order)（3.11.6 节），因而研究的是模糊键级对 N 的响应。

若你已有由模糊分析 (fuzzy analysis) 模块或盆分析 (basin analysis) 模块导出的包含当前体系所有 MO 的 AOM 的 .txt 文件，在此功能中你也可直接选择选项 3 (Option 3) 载入使用，从而不再此处计算 AOM。注意在用模糊或盆分析模块产生 AOM 之前，你应将 `settings.ini` 中的 “ispecial” 设为 3，否则 AOM 中将只涉及占据轨道。
