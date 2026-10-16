# **3.27 （超）极化率分析 (24)**

本主功能是研究极化率 (polarizability)与超极化率 (hyperpolarizability)的一系列子功能的集合。各子功能在本节介绍。值得注意的是，原子极化率可通过模糊空间分析模块计算，见第 [3.18.12](sec-3-18-fuzzy-atomic-space-analysis.md#31812-原子有效体积自由体积极化率与-c₆-系数-13) 节。

## **3.27.1 解析 Gaussian 的（超）极化率任务输出并计算相关量**

Gaussian 的（超）极化率任务（*polar* 关键词）输出难以理解，至少对初学者如此。本功能用于解析这些输出，并以更易读的格式打印，同时输出一些与（超）极化率相关的量。目前本功能正式兼容 Gaussian 09 与 16。

### **基本概念与理论背景**

体系能量可写成对均匀外电场 **F** 的 Taylor 展开：

$$
\begin{gathered} E(\mathbf{F}) = E(\mathbf{0}) + \left.\frac{\partial E}{\partial \mathbf{F}}\right|_{\mathbf{F} = 0} \mathbf{F} + \frac{1}{2}\left.\frac{\partial^2 E}{\partial \mathbf{F}^2}\right|_{\mathbf{F} = 0} \mathbf{F}^2 + \frac{1}{6}\left.\frac{\partial^3 E}{\partial \mathbf{F}^3}\right|_{\mathbf{F} = 0} \mathbf{F}^3 + \frac{1}{24}\left.\frac{\partial^4 E}{\partial \mathbf{F}^4}\right|_{\mathbf{F} = 0} \mathbf{F}^4 + \dots \\ \equiv E(\mathbf{0}) - \boldsymbol{\mu}_0 \mathbf{F} - \frac{1}{2}\boldsymbol{\alpha}\mathbf{F}^2 - \frac{1}{6}\boldsymbol{\beta}\mathbf{F}^3 - \frac{1}{24}\boldsymbol{\gamma}\mathbf{F}^4 - \frac{1}{120}\boldsymbol{\delta}\mathbf{F}^5 - \frac{1}{720}\boldsymbol{\epsilon}\mathbf{F}^6 \dots \end{gathered}
$$

$$
\boldsymbol{\mu}_0 = -\left.\frac{\partial E}{\partial \mathbf{F}}\right|_{\mathbf{F} = 0} \quad\quad \boldsymbol{\alpha} = -\left.\frac{\partial^2 E}{\partial \mathbf{F}^2}\right|_{\mathbf{F} = 0} \quad\quad \boldsymbol{\beta} = -\left.\frac{\partial^3 E}{\partial \mathbf{F}^3}\right|_{\mathbf{F} = 0} \quad\quad \boldsymbol{\gamma} = -\left.\frac{\partial^4 E}{\partial \mathbf{F}^4}\right|_{\mathbf{F} = 0}
$$

其中 **µ**₀ 为永久偶极矩，是矢量；**α** 为极化率，是矩阵（二阶张量）；**β** 为第一超极化率，是三阶张量，也称为二阶非线性光学响应（NLO）系数；**γ** 为第二超极化率，是四阶张量，也称为三阶 NLO 系数。更高阶项如 **δ** 与 **ε** 非常不重要，因此很少讨论。（超）极化率张量与外电场 **F** 的频率直接相关。若 **F** 为零频率（静电场），则（超）极化率称为静态或与频率无关的（超）极化率。动态或与频率相关的（超）极化率对应于非零频率外电磁场下的情形。

#### **极化率 (α)**

均匀电场中体系的偶极矩可写为

$$
\boldsymbol{\mu} = -\frac{\partial E}{\partial \mathbf{F}} = \boldsymbol{\mu}_0 + \underbrace{\boldsymbol{\alpha}\mathbf{F}}_{\boldsymbol{\mu}_1} + \underbrace{(1/2)\boldsymbol{\beta}\mathbf{F}^2}_{\boldsymbol{\mu}_2} + \underbrace{(1/6)\boldsymbol{\gamma}\mathbf{F}^3}_{\boldsymbol{\mu}_3} + \dots
$$

偶极矩对 **F** 的线性响应，即 **µ**₁ 项，可明确写为

$$
\boldsymbol{\mu}_1 = \boldsymbol{\alpha} \cdot \mathbf{F} \Rightarrow \begin{bmatrix} \mu_x \\ \mu_y \\ \mu_z \end{bmatrix} = \begin{bmatrix} \alpha_{xx} & \alpha_{xy} & \alpha_{xz} \\ \alpha_{yx} & \alpha_{yy} & \alpha_{yz} \\ \alpha_{zx} & \alpha_{zy} & \alpha_{zz} \end{bmatrix}\begin{bmatrix} F_x \\ F_y \\ F_z \end{bmatrix}
$$

极化率 **α** 是对称矩阵而非标量，意味着不同方向极化率不同。为了便于比较不同体系的总体极化率，方便起见定义各向同性平均极化率

$$
\langle \alpha \rangle = \mathrm{Tr}(\boldsymbol{\alpha})/3 = (\alpha_{xx} + \alpha_{yy} + \alpha_{zz})/3
$$

极化率各向异性有多种定义方式：

- 定义 1：见 *Chem. Phys.*, **410**, 90 (2013)

$$
\Delta\alpha = \sqrt{[(\alpha_{xx} - \alpha_{yy})^2 + (\alpha_{xx} - \alpha_{zz})^2 + (\alpha_{yy} - \alpha_{zz})^2 + 6(\alpha_{xy}^2 + \alpha_{xz}^2 + \alpha_{yz}^2)]/2}
$$

- 定义 2：这是最常用的定义，见 *J. Chem. Phys.*, **98**, 3022 (1993)

$$
\Delta\alpha = \sqrt{[(\alpha_{xx} - \alpha_{yy})^2 + (\alpha_{xx} - \alpha_{zz})^2 + (\alpha_{yy} - \alpha_{zz})^2]/2}
$$

- 定义 3：{*ε*} 代表 **α** 的本征值，按从小到大排列

$$
\Delta\alpha = \varepsilon_3 - (\varepsilon_1 + \varepsilon_2)/2
$$

沿三个笛卡尔轴的 **α** 值可定义为

$$
\begin{gathered} \alpha_x = \alpha_{xx} + \alpha_{xy} + \alpha_{xz} \\ \alpha_y = \alpha_{yx} + \alpha_{yy} + \alpha_{yz} \\ \alpha_z = \alpha_{zx} + \alpha_{zy} + \alpha_{zz} \end{gathered}
$$

#### **第一超极化率 (β)**

第一超极化率 **β** 是三阶张量，可用 3×3×3 矩阵描述。Gaussian 既能计算静态 **β**，也能计算动态 **β**。对后者，可计算 dc-Pockels 形式 **β**(-ω;ω,0)与 SHG 形式 **β**(-2ω;ω,ω)。

值得注意的是，对 $β_{i,j,k}$(-ω;ω,0)，$i$ 与 $j$ 指标可自由交换，而对 $β_{i,j,k}$(-2ω;ω,ω)，$j$ 与 $k$ 指标可自由交换，因此 3\*3\*3=27 个分量可化简为 18 个独立分量。对静态情形，即 $β_{i,j,k}$(0;0,0)，由于三个指标均可交换（称为 Kleinman 对称性，例如 *β*$_{xyy}$=*β*$_{yxy}$=*β*$_{yyx}$……），只有 10 个分量是独立的。Kleinman 对称性仅近似适用于低频外电场下的动态 **β**。

沿三个笛卡尔轴之一的 **β** 值可用一般公式计算

$$
\beta_i = (1/3)\sum_j (\beta_{iij} + \beta_{jii} + \beta_{jij}) \quad\quad i, j = \{x, y, z\}
$$

**β** 的大小定义为

$$
\beta_{\mathrm{tot}} = \sqrt{\beta_x^2 + \beta_y^2 + \beta_z^2}
$$

*β*$_{prj}$（也称为 *β*$_{vec}$）是 **β** 在偶极矩矢量 **µ** 上的投影，可通过实验测定（电场诱导二次谐波 (EFISHG) 实验）。*β*$_{||}$ 是沿 **µ** 方向的 **β** 分量

$$
\beta_{\mathrm{prj}} = \sum_i \frac{\mu_i\beta_i}{|\boldsymbol{\mu}|} \quad\quad \beta_{\parallel} = (3/5)\beta_{\mathrm{prj}}
$$

有人更愿意讨论 **β** 相对 Z 轴的垂直与平行分量，分别定义为

$$
\beta_{\perp(Z)} = (1/5)\sum_j (2\beta_{zjj} - 3\beta_{jzj} + 2\beta_{jjz}) \quad\quad \beta_{\parallel(Z)} = (3/5)\beta_z
$$

对静态情形，可将 x、y、z 方向的 **β** 明确写为

$$
\begin{gathered} \beta_x = \beta_{xxx} + \beta_{xyy} + \beta_{xzz} \\ \beta_y = \beta_{yxx} + \beta_{yyy} + \beta_{yzz} \\ \beta_z = \beta_{zxx} + \beta_{zyy} + \beta_{zzz} \end{gathered}
$$

而 $\beta_{\perp(Z)} = (1/5)\beta_z$。

#### **第二超极化率 (γ)**

第二超极化率 **γ** 是 3×3×3×3 形式的四阶张量。Gaussian 可计算其静态极限形式 **γ**(0;0,0,0)；对动态情形，Gaussian 能计算其 EOKO（电光 Kerr 效应）形式 **γ**(-ω;ω,0,0)与 SHG 形式 **γ**(-2ω;ω,ω,0)。

**γ** 的 $i$ 分量定义为

$$
\gamma_i = (1/15)\sum_j (\gamma_{ijji} + \gamma_{ijij} + \gamma_{iijj}) \quad\quad i, j = \{x, y, z\}
$$

γ 的总大小用 $\gamma_{\mathrm{tot}} = \sqrt{\gamma_x^2 + \gamma_y^2 + \gamma_z^2}$ 度量。

**γ** 的平均值有两种定义，如下所示。定义 1 更常用，它等价于 γ$_{||}$

$$
\begin{aligned}\mathrm{def\ 1:} \quad \langle \gamma \rangle &= \gamma_x + \gamma_y + \gamma_z\\\mathrm{def\ 2:} \quad \langle \gamma \rangle &= (1/5)(\gamma_{xxxx} + \gamma_{yyyy} + \gamma_{zzzz} + \gamma_{xxyy} + \gamma_{xxzz} + \gamma_{yyzz} + \gamma_{yyxx} + \gamma_{zzxx} + \gamma_{zzyy})\end{aligned}
$$

$\gamma_{\perp}$ 定义为

$$
\gamma_{\perp} = (1/15)\sum_i\sum_j (2\gamma_{ijji} - \gamma_{iijj}) \quad\quad i, j = \{x, y, z\}
$$

上述关于 γ 的多数方程可见 *Reviews in Computational Chemistry* 第 12 卷（1998）第 5 章。

#### **超 Rayleigh 散射 (HRS)与退偏比 (DR)**

超 Rayleigh 散射 (Hyper-Rayleigh Scattering, HRS) 技术是作为 EFISHG 测量分子超极化率的替代方法发展起来的。HRS 可直接测量所有分子的 *β*，包括不能用 EFISHG 研究的非极性分子。见 *Acc. Chem. Res.*, **31**, 675 (1998) 中的介绍。

根据给定频率 (ω) 入射光强度与在 90° 角探测到的倍频 (2ω)散射光强度，可确定 *β*$_{HRS}$，它与与频率相关的 **β** 张量分量的关系如下。更多细节见 *Phys. Chem. Chem. Phys.*, **10**, 6223 (2008)。

$$
\beta_{\mathrm{HRS}}(-2\omega; \omega, \omega) = \sqrt{\left\langle \beta_{ZZZ}^2 \right\rangle + \left\langle \beta_{XZZ}^2 \right\rangle}
$$

其中（指标 *ζ* 依次循环 { $x$ , $y$ , $z$ }，*η* 与 *ξ* 类似）

$$
\begin{aligned}\left\langle \beta_{ZZZ}^2 \right\rangle &= \frac{1}{7}\sum_\zeta \beta_{\zeta\zeta\zeta}^2 + \frac{4}{35}\sum_{\zeta \neq \eta} \beta_{\zeta\zeta\eta}^2 + \frac{2}{35}\sum_{\zeta \neq \eta} \beta_{\zeta\zeta\zeta}\beta_{\zeta\eta\eta} + \frac{4}{35}\sum_{\zeta \neq \eta} \beta_{\eta\zeta\zeta}\beta_{\zeta\zeta\eta}\\&+ \frac{4}{35}\sum_{\zeta \neq \eta} \beta_{\zeta\zeta\zeta}\beta_{\eta\eta\zeta} + \frac{1}{35}\sum_{\zeta \neq \eta} \beta_{\eta\zeta\zeta}^2 + \frac{4}{105}\sum_{\zeta \neq \eta \neq \xi} \beta_{\zeta\zeta\eta}\beta_{\eta\xi\xi} + \frac{1}{105}\sum_{\zeta \neq \eta \neq \xi} \beta_{\eta\zeta\zeta}\beta_{\eta\xi\xi}\\&+ \frac{4}{105}\sum_{\zeta \neq \eta \neq \xi} \beta_{\zeta\zeta\eta}\beta_{\xi\xi\eta} + \frac{2}{105}\sum_{\zeta \neq \eta \neq \xi} \beta_{\zeta\eta\xi}^2 + \frac{4}{105}\sum_{\zeta \neq \eta \neq \xi} \beta_{\zeta\eta\xi}\beta_{\eta\xi\zeta}\end{aligned}
$$

$$
\begin{aligned}\left\langle \beta_{XZZ}^2 \right\rangle &= \frac{1}{35}\sum_\zeta \beta_{\zeta\zeta\zeta}^2 + \frac{4}{105}\sum_{\zeta \neq \eta} \beta_{\zeta\zeta\zeta}\beta_{\zeta\eta\eta} - \frac{2}{35}\sum_{\zeta \neq \eta} \beta_{\zeta\zeta\zeta}\beta_{\eta\eta\zeta} + \frac{8}{105}\sum_{\zeta \neq \eta} \beta_{\zeta\zeta\eta}^2\\&+ \frac{3}{35}\sum_{\zeta \neq \eta} \beta_{\zeta\eta\eta}^2 - \frac{2}{35}\sum_{\zeta \neq \eta} \beta_{\zeta\zeta\eta}\beta_{\eta\xi\xi} + \frac{1}{35}\sum_{\zeta \neq \eta \neq \xi} \beta_{\zeta\eta\eta}\beta_{\zeta\xi\xi} - \frac{2}{105}\sum_{\zeta \neq \eta \neq \xi} \beta_{\zeta\zeta\zeta}\beta_{\eta\eta\xi}\\&- \frac{2}{105}\sum_{\zeta \neq \eta \neq \xi} \beta_{\zeta\zeta\eta}\beta_{\eta\xi\xi} + \frac{2}{35}\sum_{\zeta \neq \eta \neq \xi} \beta_{\zeta\eta\xi}^2 - \frac{2}{105}\sum_{\zeta \neq \eta \neq \xi} \beta_{\zeta\eta\xi}\beta_{\eta\xi\zeta}\end{aligned}
$$

*ζ*≠*η*≠*ξ* 指 *ζ*≠*η* 且同时 *η*≠*ξ*。尖括号表示对所有可能

分子取向的平均。若假设 Kleinman 对称性近似成立，上述方程可化简为更简单的形式，见 *J. Chem. Phys.*, **136**, 024506 (2012) 的 Eq. 6。

相关的退偏比 (DR) 定义为

$$
\mathrm{DR} = \frac{\left\langle \beta_{ZZZ}^2 \right\rangle}{\left\langle \beta_{XZZ}^2 \right\rangle}
$$

具有 T$_{d}$ 点群的分子 DR 恰好等于 1.5。若入射光波长之半接近用 TDDFT 在同样水平下算得的当前体系吸收带，由于 SHG 共振，打印的 DR 可能低于 1.5。

还有一些与 HRS 相关的量可供研究，如下所示，更多信息见 *J. Chem. Phys.*, **136**, 024506 (2012)。注意为一致起见，该文方程中的 *ZXX* 已替换为 *XZZ*，在当前语境下二者数值相同。

$\left\langle {\beta}_{ZZZ}^{2} \right\rangle$ 与 $\left\langle {\beta}_{XZZ}^{2} \right\rangle$ 可看作由偶极（$J$=1）与八极（$J$=3）两个分量贡献：

$$
\begin{aligned}\left\langle \beta_{ZZZ}^2 \right\rangle &= \frac{9}{45}\left| \beta_{J = 1} \right|^2 + \frac{6}{105}\left| \beta_{J = 3} \right|^2\\\left\langle \beta_{XZZ}^2 \right\rangle &= \frac{1}{45}\left| \beta_{J = 1} \right|^2 + \frac{4}{105}\left| \beta_{J = 3} \right|^2\end{aligned}
$$

显然两分量可如下求得

$$
\begin{aligned}\left| \beta_{J = 1} \right| &= \sqrt{6\left\langle \beta_{ZZZ}^2 \right\rangle - 9\left\langle \beta_{XZZ}^2 \right\rangle}\\\left| \beta_{J = 3} \right| &= \sqrt{\frac{1}{2}\left( -7\left\langle \beta_{ZZZ}^2 \right\rangle + 63\left\langle \beta_{XZZ}^2 \right\rangle \right)}\end{aligned}
$$

非线性各向异性参数为 *ρ* = $\left|\beta_{J=3}\right|$ / $\left|\beta_{J=1}\right|$。

偶极相对贡献，即 Φ($β_{J}$$_{=1}$)，与八极相对贡献，即 Φ($β_{J}$$_{=3}$)，定义如下。显然 Φ($β_{J}$$_{=1}$)+Φ($β_{J}$$_{=3}$)=1

$$
\begin{gathered} \Phi(\beta_{J = 1}) = 1/(1 + \rho) \\ \Phi(\beta_{J = 3}) = \rho/(1 + \rho) \end{gathered}
$$

对小分子，偶极矩越大的往往 Φ($β_{J}$$_{=1}$) 越大、DR 越高而 *ρ* 越低，偶极矩越小的往往 Φ($β_{J}$$_{=3}$) 越大、DR 越低而 *ρ* 越高。

假设沿 X 方向传播的一般椭圆偏振入射光，其偏振态由两角度 (Ψ, *δ*) 表征，则沿 Y 方向在 90° 处散射的、沿 Z 轴垂直 (V) 偏振的倍频光强度由 Bersohn 公式给出（假设相位延迟 *δ* 为 π/2）

$$
\mathrm{I}_{\Psi\mathrm{V}}^{2\omega} \propto \left\langle \beta_{XZZ}^2 \right\rangle \cos^4 \Psi + \left\langle \beta_{ZZZ}^2 \right\rangle \sin^4 \Psi + \sin^2 \Psi \cos^2 \Psi \left\langle (\beta_{ZXZ} + \beta_{ZZX})^2 - 2\beta_{ZZZ}\beta_{XZZ} \right\rangle
$$

其中 $\left\langle (\beta_{ZXZ} + \beta_{ZZX})^2 - 2\beta_{ZZZ}\beta_{XZZ} \right\rangle = 7\left\langle \beta_{XZZ}^2 \right\rangle - \left\langle \beta_{ZZZ}^2 \right\rangle$ ，Ψ 为入射光束的偏振角。

根据理论计算的 SHG 形式 **β** 张量，上述所有量都可直接预测。可扫描 ${I}_{\Psi V}^{2\omega}$ 随 Ψ 的变化并绘制为曲线图。

### **输入文件与用法**

在本功能中，Multiwfn 输出偶极矩、极化率与第一/第二超极化率（如有）的带明确标记的所有分量，以及上文介绍的所有相关量，如各向同性极化率、极化率各向异性、三个轴向的超极化率（$β_{x}$、$β_{y}$、$β_{z}$）、超极化率大小（*β*$_{tot}$）等。Multiwfn 打印的 **α** 与 **β** 分量对应标准取向，而打印的 **γ** 分量对应输入取向。

Gaussian 中的 *polar* 关键词专用于基于解析导数（通过耦合微扰 SCF 方程）或数值导数（通过有限场处理）计算 **α**、**β** 与 **γ**。注意 Gaussian 输入文件中必须指定 **\#P**，否则 Multiwfn 无法正确解析相关信息。

进入 Multiwfn 的本功能后，应选择你的 Gaussian（超）极化率计算的实际情况，以便 Multiwfn 成功解析输出信息并为你展示有价值的数据。如菜单所见，有七个选项对应不同情形：

- (1) *polar* 关键词 + 支持解析三阶导数的方法（HF/DFT/半经验方法）

- (2) *polar* 关键词 + 支持解析二阶导数的方法（例如 MP2）

- (3) *polar=Cubic* 关键词 + 支持解析二阶导数的方法

- (4) *polar* 关键词 + 支持解析一阶导数的方法（CISD、QCISD、CCSD、MP3、MP4(SDQ) 等）

- (5) *polar=DoubleNumer*（等价于 *Polar=EnOnly*）关键词 + 支持解析一阶导数的方法

- (6) *polar* 关键词 + 仅支持能量计算的方法（CCSD(T)、QCISD(T)、MP4(SDTQ)、MP5 等）

- (7) *polar=gamma* 关键词 + 支持解析三阶导数的方法（HF/DFT/半经验方法）

所有选项都打印极化率及相关数据，只有选项 (1)、(3) 与 (5) 还打印第一超极化率，只有 (7) 还打印第二超极化率。

对情形 (1)，若随 *polar* 指定了 *CPHF=RdFreq*，或用了 *polar=DCSHG*，且同时在分子几何之后空一行给出外电场频率（例如 *0.05 0.07 0.1* 或 *532 nm 680 nm*），Gaussian 将连同静态（超）极化率一起计算并输出与频率相关的（超）极化率。*CPHF=RdFreq polar* 情形只计算 **β**(-ω;ω,0) 值，而 *polar=DCSHG* 情形同时计算 **β**(-ω;ω,0) 与 **β**(-2ω;ω,ω) 值。对情形 (7)，Gaussian 计算 **γ**(0;0,0,0)、**γ**(-ω;ω,0,0) 与 **γ**(-2ω;ω,ω,0)，你必须在输入文件末尾提供外电场频率。

对情形 (1) 与 (7)，默认 Multiwfn 只解析静态（超）极化率。若希望解析与频率相关的量而非静态量，在选择选项 1 或 7 开始解析之前，应先选择选项“-1 Toggle loading frequency-dependent result for options 1 and 7”。然后开始解析后，用户可选择解析哪个频率处的结果。注意在情形 (1) 中若选择解析 **β**(-2ω;ω,ω)，必须在 Gaussian 输入文件中使用 *polar=DCSHG* 关键词。

当你要求 Multiwfn 基于 *polar=DCSHG* 输出文件解析与频率相关的 **β**(-2ω;ω,ω) 时，上述与超 Rayleigh 散射 (HRS) 实验相关的量也会自动打印。之后，还可让 Multiwfn 扫描 ${I}_{\Psi V}^{2\omega}$ 随 Ψ 的变化，生成的 *HRS_angle.txt* 可用 Origin 等作图。

值得注意的是，众所周知 Gaussian 输出的所有超极化率分量符号都是错的，应乘以 -1，Multiwfn 已自动处理此问题。

在解析之前，通过本功能界面的选项 -3 可选择输出单位。可选原子单位、SI 单位与 esu 单位。换算因子为

|     |        | SI                    | esu                |
|-----|--------|-----------------------|--------------------|
| *µ* | 1 a.u. | 8.47835×10⁻³⁰ C m     | 2.54175 ×10⁻¹⁸ esu |
| *α* | 1 a.u. | 1.6488×10⁻⁴¹ C²m²J⁻¹  | 1.4819×10⁻²⁵ esu   |
| *β* | 1 a.u. | 3.20636×10⁻⁵³ C³m³J⁻² | 8.63922×10⁻³³ esu  |
| *γ* | 1 a.u. | 6.23538×10⁻⁶⁵ C⁴m⁴J⁻³ | 5.03670×10⁻⁴⁰ esu  |

极化率 *α* 常用“极化率体积”（*α*'）表示，具有体积单位。*α* (1 a.u.)=*α*' (0.14818470 Å³)。

例子见第 [4.24.1](sec-4-24-examples-of-hyperpolarizability-analyses.md#4241-解析-gaussian-polar-任务的输出文件得到-超极化率并计算相关量) 节。关于本功能的更多讨论与例子见我的博客文章“Using Multiwfn to analyze polarizability and hyperpolarizability outputted by Gaussian”（<http://sobereva.com/231>，中文）。

## **3.27.2 用态求和 (SOS) 方法研究（超）极化率及两/三能级模型分析**

本功能用于基于著名的态求和 (sum-over-states, SOS) 方法计算极化率、第一、第二与第三超极化率，如下所述。此外，本模块还可实现流行的第一超极化率两能级模型分析及其扩展（三能级模型），见第 [3.27.2.2](#32722-超极化率的两能级与三能级模型分析) 节。

### **3.27.2.1 （超）极化率的计算**

#### **计算（超）极化率的理论简述**

（超）极化率的一些基本概念已在第 [3.27.1](#3271-解析-gaussian-的超极化率任务输出并计算相关量) 节介绍。计算（超）极化率有几种不同方法，包括导数法、态求和 (SOS) 法与响应法

- (1) 导数法：这是最直接、最常用的一种。静态（超）极化率所需的导数可通过耦合微扰 SCF (CPSCF) 方程解析求得；具体地，对 HF 为 CPHF，对 KS-DFT 为 CPKS。这些导数也可用有限差分技术数值求得，即所谓有限场 (FF) 方法。显然 FF 比 CPSCF 慢得多且精度不如，但仍有用，因为高阶解析导数、特别是在复杂 post-HF 水平下的解析导数，由于编码困难，许多量子化学程序并不广泛支持。当所有需要的导数都有解析形式时，导数法将非常高效。CPSCF 方程的与频率相关形式使导数法能计算动态（超）极化率，但 FF 处理无法计算动态（超）极化率。Gaussian 中的 *polar* 关键词，如第 [3.27.1](#3271-解析-gaussian-的超极化率任务输出并计算相关量) 节仔细讨论的，对应此导数法。

- (2) SOS 方法：这种计算静态与动态（超）极化率的方法相对低效，因为原则上它涉及对所有激发态求和（实际应用中，考虑最低的 60-120 个态通常已足够），而确定大量激发态在 *ab initio* 情形（如 CIS 与 TDDFT）通常相当耗时，特别是对大体系（如大于 40 个原子）。由于计算成本高，当导数法可解析进行时，一般不推荐用 SOS 计算（超）极化率。SOS 唯一的优点可能是可分别给出不同态的贡献并分别讨论，而且当不同激发态间的跃迁偶极矩已在手边时，可相当快地计算不同频率处的（超）极化率。值得注意的是，基于便宜的半经验 ZINDO 计算的 SOS（SOS/ZINDO）在计算大体系（超）极化率时非常流行。

- (3) 响应法：此方法专用于动态（超）极化率，也称为传播子方法。TDHF 与 TDDFT 是它的两种实际实现。此方法在主流量子化学程序中支持并不普遍。

#### **SOS 方法的工作方程**

计算极化率与第一/第二/第三超极化率的显式 SOS 方程可见 *J. Chem. Phys.*, **99**, 3738 (1993)，其思想最初由 Orr 与 Ward 在 *Mol. Phys.*, **20**, 512 (1971) 中提出。

极化率 *α* 与第一超极化率 *β* 的方程为（均为原子单位）

$$
\begin{gathered}\alpha_{AB}(-\omega;\omega)=\sum_{i\ne 0}\left[\frac{\mu_{0i}^{A}\mu_{i0}^{B}}{\Delta_{i}-\omega}+\frac{\mu_{0i}^{B}\mu_{i0}^{A}}{\Delta_{i}+\omega}\right]=\hat{P}[A(-\omega),B(\omega)]\sum_{i\ne 0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}}{\Delta_{i}-\omega}\end{gathered}
$$

$$
\begin{gathered}\beta_{ABC}(-\omega_{\sigma};\omega_{1},\omega_{2})=\hat{P}[A(-\omega_{\sigma}),B(\omega_{1}),C(\omega_{2})]\sum_{i\ne 0}\sum_{j\ne 0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\mu_{j0}^{C}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{j}-\omega_{2})}\end{gathered}
$$

其中

$$
\begin{gathered}
\mu_{ij}^{A}=\left\langle i\middle|\hat{\mu}^{A}\middle|j\right\rangle\\
\overline{\mu_{ij}^{A}}=\mu_{ij}^{A}\\
\omega_{\sigma}=\sum_{i}\omega_{i}
\end{gathered}
$$

*A、B、C……* 代表 {x,y,z} 之一方向；*ω* 为外电场能量，*ω*=0 对应静电场；Δ*$_{i}$* 代表激发态 $i$ 相对基态 0 的激发能。$\hat{P}$ 为置换算符，对 *α* 与 *β* 显然分别有 2!=2 与 3!=6 种置换。${\mu}_{ij}^{A}$ 为态 $i$ 与 $j$ 间跃迁偶极矩的 $A$ 分量；当 $i$ = $j$ 时该项即为态 $i$ 的电偶极矩。$\hat{\mu}$ 为偶极矩算符，例如 ${\hat{\mu}}^{x}\equiv -x$。

第二超极化率 *γ* 的 SOS 方程为

$$
\begin{gathered}\gamma_{ABCD}(-\omega_{\sigma};\omega_{1},\omega_{2},\omega_{3})=\hat{P}[A(-\omega_{\sigma}),B(\omega_{1}),C(\omega_{2}),D(\omega_{3})](\gamma^{\mathrm{I}}-\gamma^{\mathrm{II}})\\\gamma^{\mathrm{I}}=\sum_{i\ne 0}\sum_{j\ne 0}\sum_{k\ne 0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{j}-\omega_{2}-\omega_{3})(\Delta_{k}-\omega_{3})}\\\gamma^{\mathrm{II}}=\sum_{i\ne 0}\sum_{j\ne 0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{i}-\omega_{1})(\Delta_{j}-\omega_{3})}\end{gathered}
$$

第三超极化率 *δ* 的 SOS 方程为

$$
\begin{gathered}\delta_{ABCDE}(-\omega_{\sigma};\omega_{1},\omega_{2},\omega_{3},\omega_{4})=\hat{P}[A(-\omega_{\sigma}),B(\omega_{1}),C(\omega_{2}),D(\omega_{3}),E(\omega_{4})](\delta^{\mathrm{I}}-\delta^{\mathrm{II}}-\delta^{\mathrm{III}})\\\delta^{\mathrm{I}}=\sum_{i,j,k,l\,(\ne 0)}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\overline{\mu_{kl}^{D}}\mu_{l0}^{E}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{j}-\omega_{\sigma}+\omega_{1})(\Delta_{k}-\omega_{3}-\omega_{4})(\Delta_{l}-\omega_{4})}\\\delta^{\mathrm{II}}=(1/2)\sum_{i,j,k\,(\ne 0)}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\overline{\mu_{jk}^{D}}\mu_{k0}^{E}}{(\Delta_{j}+\omega_{2})(\Delta_{k}-\omega_{4})}\left(\frac{1}{\Delta_{i}-\omega_{\sigma}}+\frac{1}{\Delta_{i}-\omega_{1}}\right)\left(\frac{1}{\Delta_{j}-\omega_{3}-\omega_{4}}+\frac{1}{\Delta_{k}+\omega_{2}+\omega_{3}}\right)\\\delta^{\mathrm{III}}=(1/2)\sum_{i,j,k\,(\ne 0)}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\overline{\mu_{jk}^{D}}\mu_{k0}^{E}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{i}-\omega_{1})}\left[\frac{1}{(\Delta_{j}-\omega_{3}-\omega_{4})(\Delta_{k}-\omega_{4})}+\frac{1}{(\Delta_{j}+\omega_{2})(\Delta_{k}+\omega_{2}+\omega_{3})}\right]\end{gathered}
$$

#### **输入文件**

可用两种输入文件：

- 包含所有相关态的激发能与跃迁偶极矩的纯文本文件。此时可计算极化率、第一、第二与第三超极化率。应满足以下格式（假设非常简单情形，只有 2 个激发态）。

  ```text
  2      // The number of excited states
  1  1.1        // Excited state 1, its index and excitation energy (eV)
  2  3.2
  0 0  0.845 0.2 0.4    // Electric dipole moment of ground in X,Y,Z (a.u.)
  0 1  0.231 0.3 0.7    // Transition dipole moment between ground and excited state 1
  0 2  0.112 0.564 0.21
  1 1  0.021 0.465 0.0    // Electric dipole moment of excited state 1
  1 2  0.001 0.3 0.11     // Transition dipole moment between excited states 1 and 2
  2 2  0.432 0.14 0.42
  ```

  你可直接利用第 [3.21.5](sec-3-21-electron-excitation-analysis.md#3215-计算所有态之间的跃迁电磁偶极矩和每个态的偶极矩-5) 节介绍的功能，基于 Gaussian 或其他程序的电子激发任务输出文件生成这样的纯文本文件。

  若只关心极化率，只需提供 "1 1" 行之前的内容，其余内容均可省略；此时激发态数目应写成负数（上例中为 -2），以告诉 Multiwfn 不加载它们。

- 常见的 CIS、TDHF、TDDFT 或 ZINDO 任务的 Gaussian 输出文件。由于 Gaussian 不输出 SOS 超极化率计算所需的全部跃迁偶极矩，此时 Multiwfn 只计算极化率。为得到准确的极化率，计算的态数目应足够大。若 *nstates* 关键词指定为很大的值，例如 1000000，则计算所有态。建议使用 \#P，因为此时激发能将以更高精度的格式打印。

#### **用法**

进入本功能后将看到一个菜单，有三类功能：

- 选项 1\~4：分别用于计算给定频率处的 α、β、γ 与 δ。用户需输入每个外电场的频率。输入的频率可为负。例如，要计算超极化率 β(-(0.25-0.32);0.25,-0.32)，应在选项 2 中输入 *0.25,-0.32*。默认单位为原子单位，若想以 nm 输入频率，应加相应后缀，例如 *182.25,-142.385 nm*。

  由于 γ 特别是 δ 的计算常耗时，此时会提示用户输入考虑的态数目，数目越小成本越低，但太小可能导致结果差。

- 选项 5\~7：用于研究 α、β 与 γ 随考虑的态数目的变化。用户需输入每个外电场的频率。对 α 与 β，考虑的态数目从 1 到加载的全部态，步长为 1。而对 γ，由于计算成本可能很高，允许用户定义终值与步长。结果将输出到当前目录的纯文本文件，各列含义在命令行窗口清楚标明。

- 选项 15\~17：用于研究 α、β 与 γ 随外电场频率的变化。对 α，用户需输入外电场频率的初值、终值与步长。对 β 与 γ，用户应写一个纯文本文件，每行对应一对要计算的频率（原子单位）。Multiwfn 会提示用户输入文件路径。下面是研究 γ(-0;0,ω,-ω) 随 ω 从 0 到 0.2 a.u.（步长 0.02）变化的示例文件

  ```text
  0.0  0.0  0.0
  0.0  0.02  -0.02
  0.0  0.04  -0.04
  ...[ignored]
  0.0  0.2  -0.2
  ```

  由于计算 γ 的成本可能很高，此时允许用户设置考虑的态数目。结果将输出到当前目录的纯文本文件，各列含义在命令行窗口清楚标明。

- 选项 19：此选项用于同时扫描 β(-(ω₁+ω₂);ω₁,ω₂) 的 ω₁ 与 ω₂。只需输入 ω₁ 与 ω₂ 的起始频率、终止频率与步数。然后过一会儿，不同 ω₁、ω₂ 频率处的 β 将输出到当前目录的纯文本文件，各列含义在命令行窗口清楚标明。然后可用第三方软件绘制“β 对 ω₁、ω₂”的 relief 图。

Multiwfn 不仅输出（超）极化率张量，还输出许多相关量，如各向异性、大小与沿 Z 轴分量。涉及 α、β 与 γ 的量已在第 [3.27.1](#3271-解析-gaussian-的超极化率任务输出并计算相关量) 节介绍。

例子见第 [4.24.2.1](sec-4-24-examples-of-hyperpolarizability-analyses.md#42421-计算-nh₃-的极化率和超极化率) 节。关于本功能的更多讨论与例子见我的博客文章“Using Multiwfn to calculate polarizability and hyperpolarizability based on sum-over-states (SOS) method”（<http://sobereva.com/232>，中文）。

### **3.27.2.2 超极化率的两能级与三能级模型分析**

#### **理论**

从 *β* 的 SOS 表达式可清楚看到，*β* 的大小完全由激发态性质决定。显然，从激发态角度解释不同体系间 *β* 差异的来源是很有用的想法。事实上，此分析在文献中已被广泛采用，如我的工作 *J. Comput. Chem.*, **38**, 1574 (2017) 与 *Phys. Chem. Chem. Phys.*, **27**, 11993 (2025)。下面看如何导出这样的分析模型。

回顾 *β* 的 SOS 公式

$$
\begin{gathered}\beta_{ABC}(-\omega_{\sigma};\omega_{1},\omega_{2})=\hat{P}[A(-\omega_{\sigma}),B(\omega_{1}),C(\omega_{2})]\sum_{i\ne 0}\sum_{j\ne 0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\mu_{j0}^{C}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{j}-\omega_{2})}\end{gathered}
$$

假设只关心 ZZZ 分量且只关注静态极限情形（*ω*=0），方程简化为

$$
\beta_{ZZZ}^{\mathrm{SOS}}=6\sum_{i\ne 0}\sum_{j\ne 0}\frac{\mu_{0i}^{Z}\overline{\mu_{ij}^{Z}}\mu_{j0}^{Z}}{\Delta_{i}\Delta_{j}}
$$

已知 $\overline{\mu_{ij}^{A}}=\mu_{ij}^{A}-\mu_{00}^{A}\delta_{ij}$ ，当 $i$ = $j$ 时，此项对应激发态 $i$ 与基态间偶极矩的变化，即 $\overline{\mu_{ii}^{A}}=\mu_{ii}^{A}-\mu_{00}^{A}=\Delta\mu_{i}^{A}$ ；而若 $i$ ≠ $j$ ，此项 $\overline{\mu_{ij}^{A}}=\mu_{ij}^{A}$ 对应激发态 $i$ 与 $j$ 间的跃迁偶极矩。

利用 ${\mu}_{ij}^{A}={\mu}_{ji}^{A}$ ，上示 ${\beta}_{ZZZ}^{\mathrm{SOS}}$ 可写成单个激发态贡献与不同激发态间交叉项贡献之和：

$$
\beta_{ZZZ}^{\mathrm{SOS}}=\sum_{i}6\frac{(\mu_{0i}^{Z})^{2}\Delta\mu_{i}^{Z}}{\Delta_{i}^{2}}+\sum_{i}\sum_{j>i}12\frac{\mu_{0i}^{Z}\mu_{0j}^{Z}\mu_{ij}^{Z}}{\Delta_{i}\Delta_{j}}
$$

**两能级模型**非常流行，它假设 *β*$_{ZZZ}$ 由基态与仅一个激发态主导：

$$
\beta_{ZZZ}^{\mathrm{SOS}}\approx 6\frac{(\mu_{0i}^{Z})^{2}\Delta\mu_{i}^{Z}}{\Delta_{i}^{2}}
$$

激发态 $i$ 通常称为关键态，一般对应振子强度大的最低激发态（严格说，在当前语境下，关键态应指跃迁偶极矩 Z 分量大的最低激发态，但这样确定的关键态通常与按振子强度确定的相同）。

两能级模型常用振子强度等价地表示为：

$$
\beta_{ZZZ}^{\mathrm{SOS}}=9\Delta\mu_{i}^{Z}f_{i}^{Z}/\Delta_{i}^{3}
$$

其中 $f_{i}^{Z}=(2/3)\Delta_{i}(\mu_{0i}^{Z})^{2}$ 为振子强度的 Z 分量。进一步假设只有跃迁偶极矩与偶极矩变化的 Z 分量相对突出，则有 $\beta^{\mathrm{SOS}}\propto\Delta\mu_{i}f_{i}/\Delta_{i}^{3}$ 。显然，现在通过比较 $\Delta {\mu}_{i}^{Z}$ 、$f$ *$_{i}$* 与 Δ*$_{i}$* 项，可容易分析不同体系间 *β* 差异的来源。

偶尔没有明确的关键态。例如，第 1 与第 2 激发态都有大的 ${\mu}_{0i}^{Z}$ ，而它们能量间隔很小（近简并），此时不应简单忽略任何一个，应同时考虑这两个激发态，我将此模型定义为**三能级模型**：

$$
\beta_{ZZZ}^{\mathrm{SOS}}=6\frac{(\mu_{0i}^{Z})^{2}\Delta\mu_{i}^{Z}}{\Delta_{i}^{2}}+12\frac{\mu_{0i}^{Z}\mu_{0j}^{Z}\mu_{ij}^{Z}}{\Delta_{i}\Delta_{j}}+6\frac{(\mu_{0j}^{Z})^{2}\Delta\mu_{j}^{Z}}{\Delta_{j}^{2}}
$$

#### **用法**

在 SOS 模块（主功能 24 的子功能 2）中，子选项 20 用于进行两能级与三能级模型分析，模型中涉及的所有项都会给出，以便你在不同体系间比较。本功能的输入文件与上一节 SOS 计算第一超极化率所用的完全相同。

进入此选项后，若只输入一个激发态序号，则进行两能级模型分析，若输入两个激发态序号，则进行三能级模型分析。若输入一个范围，如 *1-20*，则对范围内每个激发态逐个进行两能级分析。

例子见第 [4.24.2.2](sec-4-24-examples-of-hyperpolarizability-analyses.md#42422-对-nh₂-biphenyl-no₂-的第一超极化率做二能级和三能级模型分析) 节。

## **3.27.3 研究（超）极化率密度**

> **注**
>
> 介绍（超）极化率密度的博客文章是“Using Multiwfn to calculate (hyper)polarizability density”（<http://sobereva.com/305>，中文）。

（超）极化率密度可用 Multiwfn 很容易地绘制为平面图与等值面 (isosurface)图。此量在讨论给定分子（超）极化率本质时很有用。若在工作中用了此功能，建议引用我的论文 *J. Comput. Chem.*, **38**, 1574 (2017)，其中涉及（超）极化率密度分析并给出了简要介绍。我的其他发表工作也给出了此方法的示例性应用：*Carbon*, **165**, 461 (2020)、*J. Phys. Chem. C*, **124**, 7353 (2020)、*J. Phys. Chem. A*, **124**, 5563 (2020)、*J. Phys. Chem. C*, **124**, 845 (2020)。

### **（超）极化率密度理论与（超）极化率的空间贡献**

有一个著名的（电）偶极矩 Taylor 展开

$$
\begin{gathered}\boldsymbol{\mu}(\mathbf{F})=- \frac{\partial E}{\partial \mathbf{F}}=\boldsymbol{\mu}_0+\boldsymbol{\alpha}\mathbf{F}+(1/2)\boldsymbol{\beta}\mathbf{F}^2+(1/6)\boldsymbol{\gamma}\mathbf{F}^3+\dots\\\boldsymbol{\mu}_0=-\left.\frac{\partial E}{\partial \mathbf{F}}\right|_{\mathbf{F}=0}\quad\quad\boldsymbol{\alpha}=-\left.\frac{\partial^2 E}{\partial \mathbf{F}^2}\right|_{\mathbf{F}=0}\quad\quad\boldsymbol{\beta}=-\left.\frac{\partial^3 E}{\partial \mathbf{F}^3}\right|_{\mathbf{F}=0}\quad\quad\boldsymbol{\gamma}=-\left.\frac{\partial^4 E}{\partial \mathbf{F}^4}\right|_{\mathbf{F}=0}\end{gathered}
$$

其中 **F** 为外电场矢量，$E$ 为体系总能量，**µ** 与 **µ**₀ 分别为当前电偶极矩与永久偶极矩。**α**、**β** 与 **γ** 分别为极化率、第一与第二超极化率张量。

类似地，对电子密度可作对 **F** 的 Taylor 展开

$$
\begin{gathered}\rho(\mathbf{r},\mathbf{F})=\rho^{(0)}(\mathbf{r})+\rho^{(1)}(\mathbf{r})\mathbf{F}+(1/2)\rho^{(2)}(\mathbf{r})\mathbf{F}^2+(1/6)\rho^{(3)}(\mathbf{r})\mathbf{F}^3+\dots\\\rho^{(1)}(\mathbf{r})=\left.\frac{\partial \rho(\mathbf{r})}{\partial \mathbf{F}}\right|_{\mathbf{F}=0}\quad\quad\rho^{(2)}(\mathbf{r})=\left.\frac{\partial^2 \rho(\mathbf{r})}{\partial \mathbf{F}^2}\right|_{\mathbf{F}=0}\quad\quad\rho^{(3)}(\mathbf{r})=\left.\frac{\partial^3 \rho(\mathbf{r})}{\partial \mathbf{F}^3}\right|_{\mathbf{F}=0}\end{gathered}
$$

由于 $\boldsymbol{\mu}(\mathbf{F})=\int-\rho(\mathbf{r},\mathbf{F})\mathbf{r}\,\mathrm{d}\mathbf{r}$ ，比较上述方程，可得

$$
\begin{gathered}\boldsymbol{\mu}_0=\int-\rho^{(0)}(\mathbf{r})\mathbf{r}\,\mathrm{d}\mathbf{r}\quad\quad\boldsymbol{\alpha}=\int-\rho^{(1)}(\mathbf{r})\mathbf{r}\,\mathrm{d}\mathbf{r}\\\boldsymbol{\beta}=\int-\rho^{(2)}(\mathbf{r})\mathbf{r}\,\mathrm{d}\mathbf{r}\quad\quad\boldsymbol{\gamma}=\int-\rho^{(3)}(\mathbf{r})\mathbf{r}\,\mathrm{d}\mathbf{r}\end{gathered}
$$

其中 **ρ**$^{(1)}$ 称为极化率密度，而 **ρ**$^{(2)}$ 与 **ρ**$^{(3)}$ 分别称为第一与第二超极化率密度。利用（超）极化率密度，可容易考察各空间区域对分子总（超）极化率的贡献。

第二超极化率密度 **ρ**$^{(3)}$ 是三阶张量函数，可明确表示为

$$
\rho_{ijk}^{(3)}(\mathbf{r})=\left.\frac{\partial^3 \rho(\mathbf{r})}{\partial F_i\partial F_j\partial F_k}\right|_{\mathbf{F}=0}
$$

不可能讨论它的所有分量，因为多达 3×3×3=27 个分量。假设 *γ*$_{ZZZZ}$ 是 **γ** 中最关键的分量，可简单研究 *ρ*$_{ZZZ}$(**r**)：

$$
\rho_{zzz}^{(3)}(\mathbf{r})=\left.\frac{\partial^3 \rho(\mathbf{r})}{\partial F_z^3}\right|_{F_z=0}
$$

它与 *γ*$_{ZZZZ}$ 的关系为

$$
\boldsymbol{\gamma}_{zzzz}=\int-z\rho_{zzz}^{(3)}(\mathbf{r})\,\mathrm{d}\mathbf{r}
$$

显然，$-z{\rho}_{zzz}^{\left( 3 \right)}(\mathbf{r})$ 是点 **r** 对 *γ*$_{ZZZZ}$ 的贡献。若将其绘制为等值面图或平面图，可直观揭示 *γ*$_{ZZZZ}$ 的来源。但 $-z{\rho}_{zzz}^{\left( 3 \right)}(\mathbf{r})$ 的缺点是它依赖原点的选取，而原点选取有一定任意性，因此 ${\rho}_{zzz}^{\left( 3 \right)}$ 本身也有研究价值，因为它与原点无关。

得到 ${\rho}_{zzz}^{(3)}$ 的最容易方法是用有限差分法（推导见我的文章 <http://sobereva.com/305>）

$$
\rho_{zzz}^{(3)}=\frac{\rho(2F^z)-2\rho(F^z)+2\rho(-F^z)-\rho(-2F^z)}{2(F^z)^3}
$$

其中 $F$ *$^{z}$* 为沿 $Z$ 轴施加的外电场强度。*ρ*( $F$ *$^{z}$*) 与 *ρ*(- $F$ *$^{z}$*) 等函数分别代表沿 Z 轴正、负方向施加 $F$ *$^{z}$* 时得到的电子密度分布。此情形 $F$ *$^{z}$* 对应有限差分步长，不应太大或太小，否则数值误差显著。按我的经验，0.003 a.u. 是 $F$ *$^{z}$* 的好选择。

类似地，可容易导出极化率密度的方程

$$
\begin{gathered}\rho_z^{(1)}=\frac{\rho(F^z)-\rho(-F^z)}{2F^z}\\\boldsymbol{\gamma}_{zz}=\int-\rho_z^{(1)}(\mathbf{r})z\,\mathrm{d}\mathbf{r}\end{gathered}
$$

以及第一超极化率密度的方程

$$
\begin{gathered}\rho_{zz}^{(2)}=\frac{\rho(F^z)-2\rho(0)+\rho(-F^z)}{(F^z)^2}\\\boldsymbol{\beta}_{zzz}=\int-\rho_{zz}^{(2)}(\mathbf{r})z\,\mathrm{d}\mathbf{r}\end{gathered}
$$

### **用 Multiwfn 研究（超）极化率密度**

通过主功能 24 的子功能 3，可非常方便地绘制任何（超）极化率密度以及（超）极化率空间贡献的平面图与等值面图。一旦 Multiwfn 生成后者的格点数据 (grid data)并导出为 .cub 文件，就可进一步计算原子或片段 (fragment)对（超）极化率的贡献，如第 [4.24.3](sec-4-24-examples-of-hyperpolarizability-analyses.md#4243-研究-超极化率密度的例子) 节例子所示。

本功能按以下步骤使用

- (1) 启动 Multiwfn 并加载含所研究体系原子信息的文件，如 .xyz、.pdb、.mwfn、.fch 等，见第 [2.5](sec-2-5-input-files-and-wavefunction-types.md) 节。

- (2) 进入主功能 24 的子功能 3。

- (3) 选择希望研究的量

- (4) 选择感兴趣的方向（X 或 Y 或 Z）

  假设你在步骤 (3) 选了“第二超极化率密度与第二超极化率的空间贡献”，在步骤 (4) 选了“Z”，则之后可研究 $-z{\rho}_{zzz}^{\left( 3 \right)}$ 与 ${\rho}_{zzz}^{\left( 3 \right)}$。

- (5) 选选项 1 生成不同外电场下单点计算的 Gaussian 输入文件。可手动修改这些文件的默认关键词。默认在 PBE0/aug-cc-pVTZ 水平计算。

- (6) 手动用 Gaussian 运行 .gjf 文件，然后生成 .wfx 文件

- (7) 选选项 2 加载 .wfx 文件

- (8) 现在可选择要做的事。若选择计算（超）极化率或（超）极化率空间贡献的格点数据，则可直接可视化其等值面图或将格点数据导出为 .cub 文件。也可选择绘制这些函数的平面图。

### **关于分子取向**

重要的是注意，实际中我们真正感兴趣的往往是沿分子偶极矩方向的分量，而偶极矩方向常不平行于任何笛卡尔轴。此时，在用本功能之前，应重取向体系使偶极矩恰平行于某笛卡尔轴，如 Z。Multiwfn 可通过第 [3.300.7](sec-3-300-other-functions-part-3.md#33007-当前体系的几何相关操作) 节所述功能容易实现重取向。即在启动 Multiwfn 后加载当前体系的波函数文件，然后输入

```text
300  //Other function (Part 3)
7  //Geometry operation on the present system
7  //Make electric dipole moment parallel to a vector or Cartesian axis
3  //Parallel to Z axis
-1  //Output system to .xyz file
```

然后可用导出的 .xyz 文件作为研究（超）极化率密度的输入文件。

研究（超）极化率密度与（超）极化率空间贡献的例子见第 [4.24.3](sec-4-24-examples-of-hyperpolarizability-analyses.md#4243-研究-超极化率密度的例子) 节。

## **3.27.5 通过单位球与矢量表示可视化（超）极化率**

若你不熟悉（超）极化率，请先看第 [3.27.1](#3271-解析-gaussian-的超极化率任务输出并计算相关量) 节掌握基础知识。本节介绍单位球表示 (unit sphere representation)，它在 *J. Comput. Chem.*, **32**, 1128 (2011) 中提出，用于直观表示一阶超极化率张量，而我还把此思想扩展到了极化率与二阶超极化率。

### **理论**

回顾分子偶极矩与外电场的关系

$$
\boldsymbol{\mu}=\boldsymbol{\mu}_0+\boldsymbol{\alpha}\cdot\mathbf{F}+(1/2)\boldsymbol{\beta}\cdot\mathbf{F}\cdot\mathbf{F}+(1/6)\boldsymbol{\gamma}\cdot\mathbf{F}\cdot\mathbf{F}\cdot\mathbf{F}+\dots
$$

**β** 称为一阶超极化率张量，分量 $β_{ABC}$ 正比于分别沿 $B$ 与 $C$ 方向的两束入射电场组合在 $A$ 方向引起的诱导偶极矩大小。

在单位球表示中，有效偶极矢量定义为

$$
\boldsymbol{\beta}^{\mathrm{eff}}(\theta,\phi)=\boldsymbol{\beta}\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)
$$

其中 *θ* 与 *φ* 为球极坐标角度，**e**(*θ*,*φ*) 为垂直于球面的单位矢量。更具体地，**β**$^{eff}$ 的分量可明确写为

$$
\beta_i^{\mathrm{eff}}=\sum_j\sum_k\beta_{i,j,k}e_ke_j\quad\quad i,j,k=\{x,y,z\}
$$

**β**$^{eff}$(*θ*,*φ*) 矢量的取向与长度分别反映沿 (*θ*,*φ*) 方向施加的两束入射电场组合引起的诱导偶极矩的方向与大小。若在包围分子的球面每个顶点处都计算 **β**$^{eff}$，就可清楚生动地理解分子偶极矩对沿各方向施加的外电场的响应。原文只把此表示用于二次谐波 (SHG) 型 **β**，实际上它也可用于其他 **β**，包括静态与动态（后者情形，随强度变化的外电场来自入射电磁波，其方向垂直于电磁波传播方向）。

基于 **β**$^{eff}$ 的同样思想，我定义了以下量

$$
\begin{gathered}\boldsymbol{\alpha}^{\mathrm{eff}}(\theta,\phi)=\boldsymbol{\alpha}\cdot\mathbf{e}(\theta,\phi)\\\boldsymbol{\gamma}^{\mathrm{eff}}(\theta,\phi)=\boldsymbol{\gamma}\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\end{gathered}
$$

**α**$^{eff}$(*θ*,*φ*) 矢量反映沿 (*θ*,*φ*) 方向施加的入射电场引起的诱导偶极矩的方向与大小，而 **γ**$^{eff}$(*θ*,*φ*) 矢量反映同时沿 (*θ*,*φ*) 方向施加的三束入射电场组合引起的诱导偶极矩的方向与大小。类似地，通过在球面每个顶点绘制 **α**$^{eff}$(*θ*,*φ*) 或 **γ**$^{eff}$(*θ*,*φ*)，分别得到 **α** 与 **γ** 的单位球表示图。

**β** 的所谓矢量表示对应把 (*β*$_{x}$, *β*$_{y}$, *β*$_{z}$) 矢量画成箭头，各分量定义为

$$
\beta_i=(1/3)\sum_j(\beta_{ijj}+\beta_{jji}+\beta_{jij})\quad\quad i,j=\{x,y,z\}
$$

此表示很简单，可近似表示 **β** 的主要特征，但各向异性特征不能在此表示中明确展示。例如，*β*$_{x}$ 显示 *β*$_{xxx}$、*β*$_{xyy}$、*β*$_{xzz}$……分量的集体效应，其中 *β*$_{xyy}$ 与 *β*$_{xzz}$ 描述各向异性响应特征，因为所施加的两束电场与它们组合效应产生的诱导偶极矩不共线。

我还提出了 **α** 的矢量表示，情形与 **β** 的矢量表示很不同。沿 X、Y、Z 轴画双向箭头，其长度分别代表相应方向 **α** 的大小，定义为

$$
\begin{gathered} \alpha_x = \alpha_{xx} + \alpha_{xy} + \alpha_{xz} \\ \alpha_y = \alpha_{yx} + \alpha_{yy} + \alpha_{yz} \\ \alpha_z = \alpha_{zx} + \alpha_{zy} + \alpha_{zz} \end{gathered}
$$

类似地，γ 的矢量表示对应沿 X、Y、Z 轴画双向箭头，其长度分别代表相应方向 **γ** 的大小（$γ_{x}$、$γ_{y}$、$γ_{z}$），计算为

$$
\gamma_i=(1/15)\sum_j(\gamma_{ijji}+\gamma_{ijij}+\gamma_{iijj})\quad\quad i,j=\{x,y,z\}
$$

### **用法**

Multiwfn 能对 **α**、**β** 与 **γ** 做单位球表示分析，即基于加载的（超）极化率张量生成 VMD 软件（<http://www.ks.uiuc.edu/Research/vmd/>）的绘图脚本。此外，还可为 **β** 生成对应矢量表示的绘图脚本。

启动 Multiwfn 后，应加载含所研究分子原子信息的文件。例如，可用 .xyz、.pdb 与 .fch，见第 [2.5](sec-2-5-input-files-and-wavefunction-types.md) 节。原子信息将用于确定单位球表示中球的合适半径。

进入本模块（主功能 24 的子功能 5）后，可用许多选项调节单位球与矢量表示的参数，如箭头长度比例因子、箭头半径等，都是自明的。通过选选项 1 或 2 或 3，Multiwfn 将分别从特定文件（见下）加载 **α** 或 **β** 或 **γ** 张量，然后在当前目录生成对应单位球表示的 VMD 绘图脚本（分别为 *alpha.tcl*、*beta.tcl* 与 *gamma.tcl*），对应矢量表示的脚本也会生成（*alpha_vec.tcl*、*beta_vec.tcl* 与 *gamma_vec.tcl*）。然后用 VMD 运行脚本，即可立即得到相应图形。

> **注**
>
> 值得一提的是，有个选项“-8 Toggle making longest arrow on sphere has specific length”。若选一次将其状态切换为“Yes”，则在选选项 1 或 2 或 3 后，会要求输入球面上最长箭头的期望长度。通过此选项，可使 VMD 为（超）极化率大小很不同的体系绘制的图容易比较。

### **含（超）极化率张量的文件的准备**

含 **α** 或 **β** 或 **γ** 张量的文件可由主功能 24 的子功能 1 通过从 Gaussian 的“polar”任务输出文件中提取相应数据直接生成。在该功能中，应选一次选项“-4 Export (hyper)polarizability as .txt file after parsing”将其状态切换为“Yes”，然后通过相应选项解析数据后，**α** 将导出到当前目录的 *alpha.txt*，**β** 将导出到 *beta.txt*，**γ** 将导出到 *gamma.txt*，它们就是本功能所需的。

含（超）极化率的文件也可手动准备，此时数据可由 Gaussian 之外的量子化学程序产生。文件格式自由，张量分量顺序如下（用 Fortran 语法表示）

- 极化率：((**α**(i,j),j=1,3),i=1,3)

- 一阶超极化率：(((**β**(i,j,k),k=1,3),j=1,3),i=1,3)

- 二阶超极化率：((((**γ**(i,j,k,l),l=1,3),k=1,3),j=1,3),i=1,3)

  其中指标 $i$ 的循环最慢。例如，下面是记录 **α** 张量的文件（高亮文字为注释）：

  ```text
   3.62370000E+001   XX
  -2.20999000E+000   XY
   0.00000000E+000   XZ
  -2.20999000E+000   YX
   3.91836000E+001   YY
   0.00000000E+000   YZ
   0.00000000E+000   ZX
   0.00000000E+000   ZY
   2.54054000E+001   ZZ
  ```

用本功能研究实际分子的例子见第 [4.24.5](sec-4-24-examples-of-hyperpolarizability-analyses.md#4245-用单位球表示直观研究-超极化率的例子) 节。
