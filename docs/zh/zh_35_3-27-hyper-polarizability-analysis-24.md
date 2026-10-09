# (超)极化率分析[(Hyper)polarizability analysis] (24)

> Multiwfn manual, p.361–376.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.361 -->



简并，即具有完全相同的本征值；此时它们的顺序（序号）是任意的，自动确定的NOCV对与轨道的对应关系可能不符合预期。这种情况下你可用选项-6选择一个NOCV对，然后手动输入该对应该对应的两个轨道的序号。此选项可多次使用以重定义多个NOCV对。

第4.23节给出了丰富的ETS-NOCV分析实例。


## 3.27 (超)极化率分析[(Hyper)polarizability analysis] (24)

主功能24是研究极化率和超极化率的功能集合。本节介绍各子功能。值得注意的是，原子极化率可通过模糊分析模块计算，见第3.18.12节。


### 3.27.1 解析Gaussian的(超)极化率任务输出并[Parse output of (hyper)polarizability task of Gaussian and]


### 计算相关量[evaluate relevant quantities]

Gaussian的(超)极化率任务输出（polar关键词）难以理解，至少对初学者如此。本功能用于解析这些输出，然后以更易读的格式打印它们，同时输出一些与(超)极化率相关的量。目前本功能正式兼容Gaussian 09和16。

基本概念和理论背景 体系能量可写成关于均匀外电场F的Taylor展开

$$\begin{align*}E(\mathbf{F})&=E(\mathbf{0})+\frac{\partial E}{\partial\mathbf{F}}\bigg|_{\mathbf{F}=0}\mathbf{F}+\frac{1}{2}\frac{\partial^{2}E}{\partial\mathbf{F}^{2}}\bigg|_{\mathbf{F}=0}\mathbf{F}^{2}+\frac{1}{6}\frac{\partial^{3}E}{\partial\mathbf{F}^{3}}\bigg|_{\mathbf{F}=0}\mathbf{F}^{3}+\frac{1}{24}\frac{\partial^{4}E}{\partial\mathbf{F}^{4}}\bigg|_{\mathbf{F}=0}\mathbf{F}^{4}+\ldots\\&\equiv E(\mathbf{0})-\boldsymbol{\mu}_{0}\mathbf{F}-\frac{1}{2}\boldsymbol{\alpha}\mathbf{F}^{2}-\frac{1}{6}\boldsymbol{\beta}\mathbf{F}^{3}-\frac{1}{24}\boldsymbol{\gamma}\mathbf{F}^{4}-\frac{1}{120}\delta\mathbf{F}^{5}-\frac{1}{720}\varepsilon\mathbf{F}^{6}\ldots\end{align*}$$


$$\begin{align*}E(\mathbf{F})&=E(\mathbf{0})+\frac{\partial E}{\partial\mathbf{F}}\bigg|_{\mathbf{F}=0}\mathbf{F}+\frac{1}{2}\frac{\partial^{2}E}{\partial\mathbf{F}^{2}}\bigg|_{\mathbf{F}=0}\mathbf{F}^{2}+\frac{1}{6}\frac{\partial^{3}E}{\partial\mathbf{F}^{3}}\bigg|_{\mathbf{F}=0}\mathbf{F}^{3}+\frac{1}{24}\frac{\partial^{4}E}{\partial\mathbf{F}^{4}}\bigg|_{\mathbf{F}=0}\mathbf{F}^{4}+\ldots\\&\equiv E(\mathbf{0})-\boldsymbol{\mu}_{0}\mathbf{F}-\frac{1}{2}\boldsymbol{\alpha}\mathbf{F}^{2}-\frac{1}{6}\boldsymbol{\beta}\mathbf{F}^{3}-\frac{1}{24}\boldsymbol{\gamma}\mathbf{F}^{4}-\frac{1}{120}\delta\mathbf{F}^{5}-\frac{1}{720}\varepsilon\mathbf{F}^{6}\ldots\end{align*}$$

<!-- formula-ocr: formula_p361_256.png 已替换为LaTeX, 原图保留备查 -->

其中μ0是永久偶极矩，为矢量；α是极化率，为矩阵（二阶张量）；β是第一超极化率，为三阶张量，被称为二阶非线性光学(NLO)响应系数；γ是第二超极化率，为四阶张量，被称为三阶NLO系数。更高阶项如δ和ε非常不重要，因而很少讨论。(超)极化率张量与外电场F的频率直接相关。若F为零频率（静电场），则(超)极化率被称为静态或频率无关的。动态或频率相关的(超)极化率对应于非零频率外电磁场下的情形。


<!-- p.362 -->



- 极化率(α) 均匀电场中体系的偶极矩可写为

$$\mathbf{\mu}=-\frac{\partial E}{\partial\mathbf{F}}=\mathbf{\mu}_{0}+\underbrace{\mathbf{\alpha}\mathbf{F}}_{\mathbf{\mu}_{1}}+\underbrace{(1/2)\mathbf{\beta}\mathbf{F}^{2}}_{\mathbf{\mu}_{2}}+\underbrace{(1/6)\mathbf{\gamma}\mathbf{F}^{3}}_{\mathbf{\mu}_{3}}+\ldots$$

偶极矩关于F的线性响应，即μ1项，可显式写为

$$\boldsymbol{\mu}_{1}=\boldsymbol{\alpha}\cdot\mathbf{F}\quad\Rightarrow\quad\begin{bmatrix}\mu_{x}\\ \mu_{y}\\ \mu_{z}\end{bmatrix}=\begin{bmatrix}\alpha_{xx}&\alpha_{xy}&\alpha_{xz}\\ \alpha_{yx}&\alpha_{yy}&\alpha_{yz}\\ \alpha_{zx}&\alpha_{zy}&\alpha_{zz}\end{bmatrix}\begin{bmatrix}F_{x}\\ F_{y}\\ F_{z}\end{bmatrix}$$

极化率α是对称矩阵而非标量，意味着不同方向极化率不同。为便于比较不同体系的总极化率，方便起见定义各向同性平均极化率


$$\boldsymbol{\mu}_{1}=\boldsymbol{\alpha}\cdot\mathbf{F}\quad\Rightarrow\quad\begin{bmatrix}\mu_{x}\\ \mu_{y}\\ \mu_{z}\end{bmatrix}=\begin{bmatrix}\alpha_{xx}&\alpha_{xy}&\alpha_{xz}\\ \alpha_{yx}&\alpha_{yy}&\alpha_{yz}\\ \alpha_{zx}&\alpha_{zy}&\alpha_{zz}\end{bmatrix}\begin{bmatrix}F_{x}\\ F_{y}\\ F_{z}\end{bmatrix}$$

<!-- formula-ocr: formula_p362_257.png 已替换为LaTeX, 原图保留备查 -->

极化率各向异性有多种定义方式： 定义1：见例如Chem. Phys., 410, 90 (2013)


$$\langle\alpha\rangle=\mathrm{T r}(\mathbf{a})/3=(\alpha_{x x}+\alpha_{y y}+\alpha_{z z})/3$$

<!-- formula-ocr: formula_p362_258.png 已替换为LaTeX, 原图保留备查 -->

定义2：这是最常用的定义，见例如J. Chem. Phys., 98, 3022 (1993)


$$\Delta\alpha=\sqrt{[(\alpha_{xx}-\alpha_{yy})^{2}+(\alpha_{xx}-\alpha_{zz})^{2}+(\alpha_{yy}-\alpha_{zz})^{2}+6(\alpha_{xy}^{2}+\alpha_{xz}^{2}+\alpha_{yz}^{2})]/2}$$

<!-- formula-ocr: formula_p362_259.png 已替换为LaTeX, 原图保留备查 -->

定义3：{ε}代表α按从小到大排序的本征值


$$\Delta\alpha=\sqrt{[(\alpha_{xx}-\alpha_{yy})^{2}+(\alpha_{xx}-\alpha_{zz})^{2}+(\alpha_{yy}-\alpha_{zz})^{2}]}/2$$

<!-- formula-ocr: formula_p362_260.png 已替换为LaTeX, 原图保留备查 -->

沿三个笛卡尔轴每个轴的α值可定义为

- 第一超极化率(β) 第一超极化率β是可用3×3×3矩阵描述的三阶张量。Gaussian能计算静态和动态β。对于后者，可计算dc-Pockels形式β(-ω;ω,0)和SHG形式β(-2ω;ω,ω)。

$$\boldsymbol{\mu}_{1}=\boldsymbol{\alpha}\cdot\mathbf{F}\quad\Rightarrow\quad\begin{bmatrix}\mu_{x}\\ \mu_{y}\\ \mu_{z}\end{bmatrix}=\begin{bmatrix}\alpha_{xx}&\alpha_{xy}&\alpha_{xz}\\ \alpha_{yx}&\alpha_{yy}&\alpha_{yz}\\ \alpha_{zx}&\alpha_{zy}&\alpha_{zz}\end{bmatrix}\begin{bmatrix}F_{x}\\ F_{y}\\ F_{z}\end{bmatrix}$$

三个笛卡尔轴之一方向上的β值可用一般方程计算


<!-- p.363 -->




$$\beta_{i}=(1/3)\sum_{j}(\beta_{i j j}+\beta_{j j i}+\beta_{j i j})\quad i,j=\left\{x,y,z\right\}$$

<!-- formula-ocr: formula_p363_261.png 已替换为LaTeX, 原图保留备查 -->

β的大小定义为

$$\mathrm{d e f}2:\quad<\gamma>=(1/5)(\gamma_{x x x x}+\gamma_{y y y y}+\gamma_{z z z z}+\gamma_{x x y y}+\gamma_{x x z z}+\gamma_{y y z z}+\gamma_{y y x x}+\gamma_{z z x x}+\gamma_{z z y y})$$


$$\boldsymbol{\beta}_{\mathrm{p r j}}=\sum_{i}\frac{\mu_{i}\boldsymbol{\beta}_{i}}{\left|\boldsymbol{\mu}\right|}\qquad\boldsymbol{\beta}_{\parallel}=(3/5)\boldsymbol{\beta}_{\mathrm{p r j}}$$

<!-- formula-ocr: formula_p363_262.png 已替换为LaTeX, 原图保留备查 -->

有人更喜欢讨论β相对于Z轴的垂直和平行分量，它们分别定义为


$$\gamma_{i}=(1/15)\sum_{j}(\gamma_{ijji}+\gamma_{ijij}+\gamma_{iijj})\quad i,j=\left\{x,y,z\right\}$$

<!-- formula-ocr: formula_p363_263.png 已替换为LaTeX, 原图保留备查 -->

对于静态情形，我们可显式写出x、y和z方向的β为

和zZββ)5/1()(=⊥。

- 第二超极化率(γ) 第二超极化率γ是3×3×3×3形式的四阶张量。Gaussian可计算其静态极限形式γ(0;0,0,0)；而对动态情形，Gaussian能计算其EOKO（电光Kerr效应）形式γ(-ω;ω,0,0)和SHG形式γ(-2ω;ω,ω,0)。

γ的i分量定义为


$$\gamma_{\perp}=(1/15)\sum_{i}\sum_{j}(2\gamma_{i j j i}-\gamma_{i i j j})\quad i,j=\left\{x,y,z\right\}$$

<!-- formula-ocr: formula_p363_264.png 已替换为LaTeX, 原图保留备查 -->

$$\mathrm{d e f}2:\quad<\gamma>=(1/5)(\gamma_{x x x x}+\gamma_{y y y y}+\gamma_{z z z z}+\gamma_{x x y y}+\gamma_{x x z z}+\gamma_{y y z z}+\gamma_{y y x x}+\gamma_{z z x x}+\gamma_{z z y y})$$

γ的平均有两种定义，如下所示。定义1更常用，它等价于γ||

$$\mathrm{d e f}2:\quad<\gamma>=(1/5)(\gamma_{x x x x}+\gamma_{y y y y}+\gamma_{z z z z}+\gamma_{x x y y}+\gamma_{x x z z}+\gamma_{y y z z}+\gamma_{y y x x}+\gamma_{z z x x}+\gamma_{z z y y})$$

γ_|_定义为


$$\gamma_{\perp}=(1/15)\sum_{i}\sum_{j}(2\gamma_{ijij}-\gamma_{ijji})\quad i,j=\{x,y,z\}$$

上述关于γ的大多数方程可在Reviews in Computational Chemistry, Vol. 12 (1998)第5章中找到。

- 超瑞利散射(HRS)与退偏比(DR) 超瑞利散射(HRS)技术被发展为EFISHG的替代方法，用于测量分子超极化率。HRS可直接用于测量所有分子的β，包括不能用EFISHG研究的非极性分子。见Acc. Chem. Res., 31, 675 (1998)介绍。

根据给定频率(ω)入射光强度与在90角检测到的倍频(2ω)散射光强度，可确定βHRS，它与频率相关的β张量分量关联如下。更多细节见Phys. Chem. Chem. Phys., 10, 6223 (2008)。


<!-- p.364 -->



测量所有分子的β，包括非极性分子，后者不能用EFISHG研究。见Acc. Chem. Res., 31, 675 (1998)介绍。

根据给定频率(ω)入射光强度与在90角检测到的倍频(2ω)散射光强度，可确定βHRS，它与频率相关的β张量分量关联如下。更多细节见Phys. Chem. Chem. Phys., 10, 6223 (2008)。

$$\beta_{\mathrm{H R S}}(-2\omega;\omega,\omega)=\sqrt{\left\langle\beta_{Z Z Z}^{2}\right\rangle+\left\langle\beta_{X Z Z}^{2}\right\rangle}$$

$$\begin{aligned}\left\langle\beta_{X Z Z}^{2}\right\rangle=&\frac{1}{35}\sum_{\zeta}\beta_{\zeta\varsigma\varsigma}^{2}+\frac{4}{105}\sum_{\varsigma\neq\eta}\beta_{\varsigma\varsigma\varsigma}\beta_{\varsigma\eta\eta}-\frac{2}{35}\sum_{\varsigma\neq\eta}\beta_{\varsigma\varsigma\varsigma}\beta_{\eta\eta\varsigma}+\frac{8}{105}\sum_{\varsigma\neq\eta}\beta_{\varsigma\varsigma\eta}^{2}\\ &+\frac{3}{35}\sum_{\zeta\neq\eta}\beta_{\varsigma\eta\eta}^{2}-\frac{2}{35}\sum_{\zeta\varsigma\eta}\beta_{\varsigma\varsigma\eta}\beta_{\eta\varsigma\varsigma}+\frac{1}{35}\sum_{\zeta\neq\eta\neq\xi}\beta_{\varsigma\eta\eta}\beta_{\varsigma\varsigma\xi}-\frac{2}{105}\sum_{\zeta\neq\eta\neq\xi}\beta_{\varsigma\varsigma\varsigma}\beta_{\eta\eta\varsigma}\\ &-\frac{2}{105}\sum_{\varsigma\neq\eta\neq\xi}\beta_{\varsigma\varsigma\eta}\beta_{\eta\varsigma\varsigma}+\frac{2}{35}\sum_{\varsigma\neq\eta\neq\xi}\beta_{\varsigma\eta\xi}^{2}-\frac{2}{105}\sum_{\zeta\neq\eta\neq\xi}\beta_{\varsigma\eta\varsigma}\beta_{\eta\varsigma\varsigma}\end{aligned}$$


$$\beta_{\mathrm{H R S}}(-2\omega;\omega,\omega)=\sqrt{\left\langle\beta_{Z Z Z}^{2}\right\rangle+\left\langle\beta_{X Z Z}^{2}\right\rangle}$$

<!-- formula-ocr: formula_p364_266.png 已替换为LaTeX, 原图保留备查 -->

$$\begin{aligned}\left\langle\beta_{X Z Z}^{2}\right\rangle=&\frac{1}{35}\sum_{\zeta}\beta_{\zeta\varsigma\varsigma}^{2}+\frac{4}{105}\sum_{\varsigma\neq\eta}\beta_{\varsigma\varsigma\varsigma}\beta_{\varsigma\eta\eta}-\frac{2}{35}\sum_{\varsigma\neq\eta}\beta_{\varsigma\varsigma\varsigma}\beta_{\eta\eta\varsigma}+\frac{8}{105}\sum_{\varsigma\neq\eta}\beta_{\varsigma\varsigma\eta}^{2}\\ &+\frac{3}{35}\sum_{\zeta\neq\eta}\beta_{\varsigma\eta\eta}^{2}-\frac{2}{35}\sum_{\zeta\varsigma\eta}\beta_{\varsigma\varsigma\eta}\beta_{\eta\varsigma\varsigma}+\frac{1}{35}\sum_{\zeta\neq\eta\neq\xi}\beta_{\varsigma\eta\eta}\beta_{\varsigma\varsigma\xi}-\frac{2}{105}\sum_{\zeta\neq\eta\neq\xi}\beta_{\varsigma\varsigma\varsigma}\beta_{\eta\eta\varsigma}\\ &-\frac{2}{105}\sum_{\varsigma\neq\eta\neq\xi}\beta_{\varsigma\varsigma\eta}\beta_{\eta\varsigma\varsigma}+\frac{2}{35}\sum_{\varsigma\neq\eta\neq\xi}\beta_{\varsigma\eta\xi}^{2}-\frac{2}{105}\sum_{\zeta\neq\eta\neq\xi}\beta_{\varsigma\eta\varsigma}\beta_{\eta\varsigma\varsigma}\end{aligned}$$

相关的退偏比(DR)定义为

2DR β= β ZZZ XZZ 2

具有Td点群的分子DR恰好等于1.5。若入射光波长的一半接近当前体系在相同水平下用TDDFT计算的吸收带，打印的DR可能因SHG共振而低于1.5。

还有一些可研究的相关HRS量，如下所示，更多信息见J. Chem. Phys., 136, 024506 (2012)。注意为一致起见，该文方程中的ZXX已替换为XZZ，在当前语境下它们数值相同。

2〉可看作由偶极(J=1)和八极(J=3)两部分贡献：〈𝛽𝑍𝑍𝑍 2〉和〈𝛽𝑋𝑍𝑍


$$\left\langle\beta_{X Z Z}^{2}\right\rangle=\frac{1}{45}\mid\beta_{J=1}\mid^{2}+\frac{4}{105}\mid\beta_{J=3}\mid^{2}$$

<!-- formula-ocr: formula_p364_267.png 已替换为LaTeX, 原图保留备查 -->


<!-- p.365 -->



显然两部分可如下计算


$$\begin{aligned}&|\boldsymbol{\beta}_{J=1}|=\sqrt{6\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle-9\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle}\\&|\boldsymbol{\beta}_{J=3}|=\sqrt{\frac{1}{2}\left(-7\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle+63\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle\right)}\\ \end{aligned}$$

<!-- formula-ocr: formula_p365_268.png 已替换为LaTeX, 原图保留备查 -->

$$\begin{aligned}&|\boldsymbol{\beta}_{J=1}|=\sqrt{6\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle-9\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle}\\&|\boldsymbol{\beta}_{J=3}|=\sqrt{\frac{1}{2}\left(-7\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle+63\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle\right)}\\ \end{aligned}$$


$$\rho = |\beta_{J=3}| / |\beta_{J=1}|$$

<!-- formula-ocr: formula_p365_269.png 已替换为LaTeX, 原图保留备查 -->

对小分子，偶极矩越大者往往具有更大的(βJ=1)、更高的DR和更低的ρ，而偶极矩越小者往往具有更大的(βJ=3)、更低的DR和更高的ρ。

假设沿X方向传播的一般椭圆偏振入射光，其偏振态由两个角度(, δ)表征，沿Y方向在90°散射的、沿Z轴垂直(V)偏振的倍频光强度由Bersohn公式给出（假定相位延迟δ为π/2）


$$\mathrm{I}_{\Psi\mathrm{V}}^{2\omega}\propto\left\langle\beta_{X Z Z}^{2}\right\rangle\cos^{4}\Psi+\left\langle\beta_{Z Z Z}^{2}\right\rangle\sin^{4}\Psi+\sin^{2}\Psi\cos^{2}\Psi\left\langle(\beta_{Z X Z}+\beta_{Z Z X})^{2}-2\beta_{Z Z Z}\beta_{X Z Z}\right\rangle$$

<!-- formula-ocr: formula_p365_270.png 已替换为LaTeX, 原图保留备查 -->

$$\begin{aligned}&|\boldsymbol{\beta}_{J=1}|=\sqrt{6\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle-9\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle}\\&|\boldsymbol{\beta}_{J=3}|=\sqrt{\frac{1}{2}\left(-7\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle+63\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle\right)}\\ \end{aligned}$$

入射光束。

根据理论计算的SHG形式β张量，上述所有量都可方便地预测。𝐼V 2𝜔随的变化可被扫描并绘制为曲线图。

输入文件和用法 在本功能中，Multiwfn输出偶极矩、极化率以及第一/第二超极化率（若有）的所有分量并带显式标记，以及上文介绍的所有相关量，如各向同性极化率、极化率各向异性、超极化率在

$$\begin{aligned}&|\boldsymbol{\beta}_{J=1}|=\sqrt{6\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle-9\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle}\\&|\boldsymbol{\beta}_{J=3}|=\sqrt{\frac{1}{2}\left(-7\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle+63\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle\right)}\\ \end{aligned}$$

Gaussian中的polar关键词专门用于基于解析导数（通过耦合微扰SCF方程）或数值导数（通过有限场处理）计算α、β和γ。注意在Gaussian输入文件中必须指定#P，否则Multiwfn无法正确解析相关信息。

进入Multiwfn的本功能后，你应选择你的Gaussian (超)极化率计算的实际情况，以便Multiwfn能成功解析输出信息并为你显示有价值的数据。如菜单所示，有七个选项对应不同情形：

(1) polar关键词 + 支持解析三阶导数的方法(HF/DFT/半经验方法)


<!-- p.366 -->



方法)

(2) polar关键词 + 支持解析二阶导数的方法（例如MP2） (3) polar=Cubic关键词 + 支持解析二阶导数的方法 (4) polar关键词 + 支持解析一阶导数的方法(CISD、QCISD、CCSD、MP3、MP4(SDQ)等)

(5) polar=DoubleNumer（等价于Polar=EnOnly）关键词 + 支持解析一阶导数的方法

(6) polar关键词 + 仅支持能量计算的方法(CCSD(T)、QCISD(T)、MP4(SDTQ)、MP5等)

(7) polar=gamma关键词 + 支持解析三阶导数的方法(HF/DFT/半经验方法)

所有选项都打印极化率及相关数据，只有选项(1)、(3)和(5)还打印第一超极化率，只有(7)还打印第二超极化率。

对于情形(1)，若随polar指定了CPHF=RdFreq或用了polar=DCSHG，同时在分子几何之后空一行提供了外场频率（例如0.05 0.07 0.1或532 nm 680 nm），Gaussian将连同静态(超)极化率一起计算并输出频率相关(超)极化率。CPHF=RdFreq polar

`HRS_angle.txt`

对于情形(1)和(7)，默认Multiwfn只解析静态(超)极化率。若你希望解析频率相关的结果而非静态结果，在选择选项1或7开始解析之前，应先选择选项“-1 切换是否为选项1和7载入频率相关结果(-1 Toggle loading frequency-dependent result for options 1 and 7)”。然后开始解析后，用户可选择解析哪个频率下的结果。

注意在情形(1)中若选择解析β(-2ω;ω,ω)，必须在Gaussian输入文件中使用polar=DCSHG关键词。

上文提到的与超瑞利散射(HRS)实验相关的量在你要求Multiwfn基于polar=DCSHG输出文件解析频率相关β(-2ω;ω,ω)时也会自动打印。之后，你还可让Multiwfn扫描𝐼V 2𝜔随的变化，然后生成的HRS_angle.txt可用Origin等绘图。

值得注意的是，众所周知Gaussian输出的所有超极化率分量符号都是错的，应乘以-1，Multiwfn已自动处理此问题。

在解析之前，通过本功能界面的选项-3，你可选择输出中的单位。可选择原子单位、SI单位和esu单位。换算因子为

SI esu

μ 1 a.u. 8.47835×10-30 C m 2.54175 ×10-18 esu α 1 a.u. 1.6488×10-41 C2m2J-1 1.4819×10-25 esu β 1 a.u. 3.20636×10-53 C3m3J-2 8.63922×10-33 esu γ 1 a.u. 6.23538×10-65 C4m4J-3 5.03670×10-40 esu

极化率α常用“极化率体积”(α')表示，其具有体积单位。α (1 a.u.)=α' (0.14818470 Å3)。


<!-- p.367 -->



第4.24.1节给出了一个例子。关于本功能的更多讨论和例子见我的博客文章“使用Multiwfn分析Gaussian输出的极化率和超极化率”(http://sobereva.com/231，中文)


### 3.27.2 用态求和(SOS)方法研究(超)极化率[Study (hyper)polarizability by sum-over-states (SOS) method]


### 与二能级或三能级模型分析[and two- or three-level model analyses]

本功能用于基于著名的态求和方法(SOS)计算极化率、第一、第二和第三超极化率，如下所述。此外，第一超极化率的流行二能级模型分析及其扩展（三能级模型）也可在本模块实现，见第3.27.2.2节介绍。

### 3.27.2.1 (超)极化率的计算[Calculation of (hyper)polarizability]

计算(超)极化率理论简述 (超)极化率的一些基本概念见第3.27.1节介绍。计算(超)极化率有几种不同方法，包括导数法、态求和(SOS)和响应法

(1) 导数法：这是最直接最常用的方法。静态(超)极化率所需的导数可用耦合微扰SCF(CPSCF)方程解析计算；具体地，HF用CPHF，KS-DFT用CPKS。这些导数也可用有限差分技术数值计算，即所谓有限场(FF)方法。显然FF比CPSCF慢得多且精度不如，但仍有用，因为高阶解析导数、特别是在复杂post-HF水平下的解析导数，由于编码困难，许多量子化学程序并不广泛支持。当所有所需导数都有解析形式时，导数法将非常高效。CPSCF方程的频率相关变体使导数法能计算动态(超)极化率，但FF处理无法计算动态(超)极化率。Gaussian中的polar关键词，如第3.27.1节仔细讨论的，即对应此导数法。

(2) SOS方法：此方法用于计算静态和动态(超)极化率，效率相对较低，因为原则上涉及对所有激发态求和（实际应用中，考虑最低60-120个态往往已足够），而大量激发态的确定在从头算情形（如CIS和TDDFT）通常相当耗时，特别是对大体系（例如>40个原子）。由于计算成本高，当导数法可解析进行时，一般不推荐用SOS计算(超)极化率。SOS唯一的优点可能是不同态的贡献可分别分离讨论，且当不同激发态间的跃迁偶极矩已在手边时，不同频率下的(超)极化率可相当快地计算。值得注意的是，基于廉价半经验ZINDO计算的SOS(SOS/ZINDO)在计算大体系(超)极化率时非常流行。

(3) 响应法：此方法专门用于动态(超)极化率，也称为传播子方法。TDHF和TDDFT是它的两种实际实现。此方法未被主流量子化学程序广泛支持。


<!-- p.368 -->



SOS方法的工作方程 计算极化率和第1/2/3超极化率的显式SOS方程见J. Chem. Phys., 99, 3738 (1993)，其思想最初由Orr和Ward在Mol. Phys., 20, 512 (1971)中提出。

极化率α和第一超极化率β的方程为（均为a.u.单位）

$$\alpha_{_{AB}}(-\omega;\omega)=\sum_{i\neq0}\left[\frac{\mu_{0i}^{A}\mu_{i0}^{B}}{\Delta_{i}-\omega}+\frac{\mu_{0i}^{B}\mu_{i0}^{A}}{\Delta_{i}+\omega}\right]=\hat{P}[A(-\omega),B(\omega)]\sum_{i\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}}{\Delta_{i}-\omega}$$

$$\beta_{A B C}(-\omega_{\sigma};\omega_{1},\omega_{2})=\hat{P}[A(-\omega_{\sigma}),B(\omega_{1}),C(\omega_{2})]\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i j}^{B}\mu_{j0}^{C}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{j}-\omega_{2})}$$

其中


$$\beta_{A B C}(-\omega_{\sigma};\omega_{1},\omega_{2})=\hat{P}[A(-\omega_{\sigma}),B(\omega_{1}),C(\omega_{2})]\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i j}^{B}\mu_{j0}^{C}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{j}-\omega_{2})}$$

<!-- formula-ocr: formula_p368_271.png 已替换为LaTeX, 原图保留备查 -->

i

A、B、C...表示方向{x,y,z}之一；ω是外场能量，ω=0对应静电场；Δi代表激发态i相对于基态0的激发能。𝑃̂是置换算符，对α和β显然分别有2!=2和3!=6种置换。𝜇𝑖𝑗 𝐴是态i与j间跃迁偶极矩的A分量；当i=j时，该项恰好对应态i的电偶极矩。𝜇̂是偶极矩算符，例如𝜇̂ 𝑥≡−𝑥。

第二超极化率γ的SOS方程为

$$\begin{aligned}\gamma_{ABCD}(-\boldsymbol{\omega}_{\sigma};\boldsymbol{\omega}_{1},\boldsymbol{\omega}_{2},\boldsymbol{\omega}_{3})&=\hat{P}[A(-\boldsymbol{\omega}_{\sigma}),B(\boldsymbol{\omega}_{1}),C(\boldsymbol{\omega}_{2}),D(\boldsymbol{\omega}_{3})](\boldsymbol{\gamma}^{\mathrm{I}}-\boldsymbol{\gamma}^{\mathrm{II}})\\\boldsymbol{\gamma}^{\mathrm{I}}&=\sum_{i\neq0}\sum_{j\neq0}\sum_{k\neq0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{j}-\boldsymbol{\omega}_{2}-\boldsymbol{\omega}_{3})(\Delta_{k}-\boldsymbol{\omega}_{3})}\\\boldsymbol{\gamma}^{\mathrm{II}}&=\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{i}-\boldsymbol{\omega}_{1})(\Delta_{j}-\boldsymbol{\omega}_{3})}\end{aligned}$$

$$\begin{aligned}\gamma_{ABCD}(-\boldsymbol{\omega}_{\sigma};\boldsymbol{\omega}_{1},\boldsymbol{\omega}_{2},\boldsymbol{\omega}_{3})&=\hat{P}[A(-\boldsymbol{\omega}_{\sigma}),B(\boldsymbol{\omega}_{1}),C(\boldsymbol{\omega}_{2}),D(\boldsymbol{\omega}_{3})](\boldsymbol{\gamma}^{\mathrm{I}}-\boldsymbol{\gamma}^{\mathrm{II}})\\\boldsymbol{\gamma}^{\mathrm{I}}&=\sum_{i\neq0}\sum_{j\neq0}\sum_{k\neq0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{j}-\boldsymbol{\omega}_{2}-\boldsymbol{\omega}_{3})(\Delta_{k}-\boldsymbol{\omega}_{3})}\\\boldsymbol{\gamma}^{\mathrm{II}}&=\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{i}-\boldsymbol{\omega}_{1})(\Delta_{j}-\boldsymbol{\omega}_{3})}\end{aligned}$$

$$\begin{aligned}\gamma_{ABCD}(-\boldsymbol{\omega}_{\sigma};\boldsymbol{\omega}_{1},\boldsymbol{\omega}_{2},\boldsymbol{\omega}_{3})&=\hat{P}[A(-\boldsymbol{\omega}_{\sigma}),B(\boldsymbol{\omega}_{1}),C(\boldsymbol{\omega}_{2}),D(\boldsymbol{\omega}_{3})](\boldsymbol{\gamma}^{\mathrm{I}}-\boldsymbol{\gamma}^{\mathrm{II}})\\\boldsymbol{\gamma}^{\mathrm{I}}&=\sum_{i\neq0}\sum_{j\neq0}\sum_{k\neq0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{j}-\boldsymbol{\omega}_{2}-\boldsymbol{\omega}_{3})(\Delta_{k}-\boldsymbol{\omega}_{3})}\\\boldsymbol{\gamma}^{\mathrm{II}}&=\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{i}-\boldsymbol{\omega}_{1})(\Delta_{j}-\boldsymbol{\omega}_{3})}\end{aligned}$$

第三超极化率δ的SOS方程为


$$\begin{aligned}\gamma_{ABCD}(-\boldsymbol{\omega}_{\sigma};\boldsymbol{\omega}_{1},\boldsymbol{\omega}_{2},\boldsymbol{\omega}_{3})&=\hat{P}[A(-\boldsymbol{\omega}_{\sigma}),B(\boldsymbol{\omega}_{1}),C(\boldsymbol{\omega}_{2}),D(\boldsymbol{\omega}_{3})](\boldsymbol{\gamma}^{\mathrm{I}}-\boldsymbol{\gamma}^{\mathrm{II}})\\\boldsymbol{\gamma}^{\mathrm{I}}&=\sum_{i\neq0}\sum_{j\neq0}\sum_{k\neq0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{j}-\boldsymbol{\omega}_{2}-\boldsymbol{\omega}_{3})(\Delta_{k}-\boldsymbol{\omega}_{3})}\\\boldsymbol{\gamma}^{\mathrm{II}}&=\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{i}-\boldsymbol{\omega}_{1})(\Delta_{j}-\boldsymbol{\omega}_{3})}\end{aligned}$$

<!-- formula-ocr: formula_p368_272.png 已替换为LaTeX, 原图保留备查 -->

$$\begin{aligned}\gamma_{ABCD}(-\boldsymbol{\omega}_{\sigma};\boldsymbol{\omega}_{1},\boldsymbol{\omega}_{2},\boldsymbol{\omega}_{3})&=\hat{P}[A(-\boldsymbol{\omega}_{\sigma}),B(\boldsymbol{\omega}_{1}),C(\boldsymbol{\omega}_{2}),D(\boldsymbol{\omega}_{3})](\boldsymbol{\gamma}^{\mathrm{I}}-\boldsymbol{\gamma}^{\mathrm{II}})\\\boldsymbol{\gamma}^{\mathrm{I}}&=\sum_{i\neq0}\sum_{j\neq0}\sum_{k\neq0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{j}-\boldsymbol{\omega}_{2}-\boldsymbol{\omega}_{3})(\Delta_{k}-\boldsymbol{\omega}_{3})}\\\boldsymbol{\gamma}^{\mathrm{II}}&=\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{i}-\boldsymbol{\omega}_{1})(\Delta_{j}-\boldsymbol{\omega}_{3})}\end{aligned}$$

)0( ≠

$$\begin{aligned}\gamma_{ABCD}(-\boldsymbol{\omega}_{\sigma};\boldsymbol{\omega}_{1},\boldsymbol{\omega}_{2},\boldsymbol{\omega}_{3})&=\hat{P}[A(-\boldsymbol{\omega}_{\sigma}),B(\boldsymbol{\omega}_{1}),C(\boldsymbol{\omega}_{2}),D(\boldsymbol{\omega}_{3})](\boldsymbol{\gamma}^{\mathrm{I}}-\boldsymbol{\gamma}^{\mathrm{II}})\\\boldsymbol{\gamma}^{\mathrm{I}}&=\sum_{i\neq0}\sum_{j\neq0}\sum_{k\neq0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{j}-\boldsymbol{\omega}_{2}-\boldsymbol{\omega}_{3})(\Delta_{k}-\boldsymbol{\omega}_{3})}\\\boldsymbol{\gamma}^{\mathrm{II}}&=\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{i}-\boldsymbol{\omega}_{1})(\Delta_{j}-\boldsymbol{\omega}_{3})}\end{aligned}$$

$$\begin{aligned}\gamma_{ABCD}(-\boldsymbol{\omega}_{\sigma};\boldsymbol{\omega}_{1},\boldsymbol{\omega}_{2},\boldsymbol{\omega}_{3})&=\hat{P}[A(-\boldsymbol{\omega}_{\sigma}),B(\boldsymbol{\omega}_{1}),C(\boldsymbol{\omega}_{2}),D(\boldsymbol{\omega}_{3})](\boldsymbol{\gamma}^{\mathrm{I}}-\boldsymbol{\gamma}^{\mathrm{II}})\\\boldsymbol{\gamma}^{\mathrm{I}}&=\sum_{i\neq0}\sum_{j\neq0}\sum_{k\neq0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{j}-\boldsymbol{\omega}_{2}-\boldsymbol{\omega}_{3})(\Delta_{k}-\boldsymbol{\omega}_{3})}\\\boldsymbol{\gamma}^{\mathrm{II}}&=\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{i}-\boldsymbol{\omega}_{1})(\Delta_{j}-\boldsymbol{\omega}_{3})}\end{aligned}$$

输入文件 可使用两种输入文件：


<!-- p.369 -->



- 包含所有涉及态的激发能和跃迁偶极矩的纯文本文件。这种情况下可计算极化率、第一、第二和第三超极化率。应满足以下格式（假设一个非常简单情形，仅2个激发态）。


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

你可直接利用第3.21.5节介绍的功能基于Gaussian或其它程序的电子激发任务输出文件生成这样的纯文本文件。

若仅对极化率感兴趣，只需提供“1 1”行之前的内容即可，其它内容均可省略；此时激发态数应写为负数（上例中为-2），以告诉Multiwfn不要载入它们。

- 常见的CIS、TDHF、TDDFT或ZINDO任务的Gaussian输出文件。由于Gaussian不输出SOS超极化率计算所需的全部跃迁偶极矩，此时Multiwfn只计算极化率。为获得准确极化率，计算的态数应足够大。若nstates关键词指定为很大值，例如1000000，则将计算所有态。建议使用#P，因为此时激发能将以更高精度格式打印。

用法 进入本功能后你将看到一个菜单，有三类功能：

- 选项1~4：分别用于计算给定频率下的α、β、γ和δ。用户需输入每个外场的频率。输入的频率可为负。例如，要计算超极化率β(-(0.25-0.32);0.25,-0.32)，应在选项2中输入0.25,-0.32。默认单位为a.u.，若你更喜欢用nm输入频率，应加相应后缀，例如182.25,-142.385 nm。

由于γ特别是δ的计算往往耗时，此时会提示用户输入考虑的态数，较小的数目导致成本较低，但太小的数目可能导致结果较差。

- 选项5~7：用于研究α、β和γ随考虑的态数的变化。用户需输入每个外场的频率。对α和β，考虑的态数从1到载入的所有态，步长为1。而对γ，由于计算成本可能相当高，允许用户定义终止值和步长。结果将输出到当前文件夹下的纯文本文件，每列含义在命令行窗口清楚标示。

- 选项15~17：用于研究α、β和γ随外场频率的变化。对α，用户需输入外场频率的初值、终值和步长。对β和γ，用户应写一个纯文本文件，每行对应一对待计算的频率（a.u.单位）。Multiwfn会提示用户输入文件路径。下面


<!-- p.370 -->



是一个研究γ(-0;0,ω,-ω)如何随ω从0到0.2 a.u.以0.02步长变化的示例文件


```text
0.0  0.0  0.0
0.0  0.02  -0.02
0.0  0.04  -0.04
...[ignored]
0.0  0.2  -0.2
```

由于计算γ的成本可能相当高，此时允许用户设置考虑的态数。结果将输出到当前文件夹下的纯文本文件，每列含义在命令行窗口清楚标示。

- 选项19：此选项用于扫描β(-(ω1+ω2);ω1,ω2)的ω1和ω2。你只需输入ω1和ω2的起始频率、终止频率和步数。然后稍后，不同ω1和ω2频率下的β将输出到当前文件夹下的纯文本文件，每列含义在命令行窗口清楚标示。然后你可用第三方软件

绘制“β vs. ω1,ω2”浮雕图。

Multiwfn不仅输出(超)极化率张量，还输出许多相关量，如各向异性、大小和沿Z轴分量。涉及的量

$$\beta_{ABC}(-\omega_{\sigma};\omega_{1},\omega_{2})=\hat{P}[A(-\omega_{\sigma}),B(\omega_{1}),C(\omega_{2})]\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{ij}^{B}\mu_{j0}^{C}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{j}-\omega_{2})}$$

第4.24.2.1节给出了一个例子。关于本功能的更多讨论和例子见我的博客文章“使用Multiwfn基于态求和(SOS)方法计算极化率和超极化率”(http://sobereva.com/232，中文)

### 3.27.2.2 超极化率的二能级和三能级模型分析[Two-level and three-level model analyses for hyperpolarizability]

理论 从β的SOS表达式可清楚看到，β的大小完全由激发态特征决定。显然从激发态角度解释不同体系间β差异的来源是一个有用的想法。事实上，这种分析在文献中已被广泛采用，如我的工作J. Comput. Chem., 38, 1574 (2017)和Phys. Chem. Chem. Phys., 27, 11993 (2025)。让我们看看如何导出这样一个分析模型。

回顾β的SOS公式

$$\beta_{ABC}(-\omega_{\sigma};\omega_{1},\omega_{2})=\hat{P}[A(-\omega_{\sigma}),B(\omega_{1}),C(\omega_{2})]\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{ij}^{B}\mu_{j0}^{C}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{j}-\omega_{2})}$$

假设我们只关心ZZZ分量且只关注静态极限情形

(ω=0)，方程简化为

$$\beta_{ZZZ}^{SOS}=6\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{Z}\overline{\mu_{ij}^{Z}}\mu_{j0}^{Z}}{\Delta_{i}\Delta_{j}}$$

已知00AAAijijijμμμδ=−，当i=j时，此项对应激发态i与基态间偶极矩变化，即00AAAAiiiiiμμμμ=−= Δ；而若i≠j，此项


<!-- p.371 -->



AAijijμμ=对应于激发态i与j之间的跃迁偶极矩。

利用𝜇𝑖𝑗 𝐴= 𝜇𝑗𝑖 𝐴这一事实，上示𝛽𝑍𝑍𝑍 SOS可写成单个激发态贡献与不同激发态间交叉项贡献之和：

$$\beta_{ZZZ}^{\mathrm{sos}}=\sum_{i}6\frac{\left(\mu_{0i}^{Z}\right)^{2}\Delta\mu_{i}^{Z}}{\Delta_{i}^{2}}+\sum_{i}\sum_{j>i}12\frac{\mu_{0i}^{Z}\mu_{0j}^{Z}\mu_{ij}^{Z}}{\Delta_{i}\Delta_{j}}$$

二能级模型非常流行，它假设βZZZ由基态和仅一个激发态主导：


$$\beta_{ZZZ}^{\mathrm{sos}}=\sum_{i}6\frac{\left(\mu_{0i}^{Z}\right)^{2}\Delta\mu_{i}^{Z}}{\Delta_{i}^{2}}+\sum_{i}\sum_{j>i}12\frac{\mu_{0i}^{Z}\mu_{0j}^{Z}\mu_{ij}^{Z}}{\Delta_{i}\Delta_{j}}$$

<!-- formula-ocr: formula_p371_273.png 已替换为LaTeX, 原图保留备查 -->

激发态i通常被称为关键态(crucial state)， commonly对应于具有大振子强度的最低激发态（严格说，在当前语境下，关键态应指具有大Z分量跃迁偶极矩的最低激发态，然而，这样确定的关键态通常与按振子强度确定的相同）。

二能级模型常用振子强度等价表示为：

$$\beta_{Z Z Z}^{\mathrm{S O S}}=9\Delta\mu_{i}^{Z}f_{i}^{Z}/\Delta_{i}^{3}$$

其中20(2 / 3)()ZZiiifμ=Δ是振子强度的Z分量。此外，假设只有跃迁偶极矩和偶极矩变化的Z分量相对突出，我们有SOS3/iiifβμΔΔ。显然，此时可通过比较∆𝜇𝑖 𝑍、fi和Δi项轻松分析不同体系间β差异的来源。偶尔，不存在明确的关键态。例如，第1和第2激发态都有大的𝜇0𝑖 𝑍，而它们能量间隔很小（近简并），此时不应简单忽略任一个，应同时考虑这两个激发态，我将此模型定义为三能级模型：

$$\beta_{ZZZ}^{\mathrm{sos}}=\sum_{i}6\frac{\left(\mu_{0i}^{Z}\right)^{2}\Delta\mu_{i}^{Z}}{\Delta_{i}^{2}}+\sum_{i}\sum_{j>i}12\frac{\mu_{0i}^{Z}\mu_{0j}^{Z}\mu_{ij}^{Z}}{\Delta_{i}\Delta_{j}}$$

用法 在SOS模块（主功能24的子功能2）中，子选项20用于进行二能级和三能级模型分析，模型中涉及的所有项都会报告，以便你轻松比较不同体系。若只输入一个激发态序号，则进行二能级模型分析，若输入两个激发态序号，则进行三能级模型分析。若输入一个范围，例如1-20，则对范围内的每个激发态进行二能级分析。本功能的输入文件与上节所述用于SOS计算第一超极化率的完全相同。

进入此选项后，若只输入一个激发态序号，则进行二能级模型分析，若输入两个激发态序号，则进行三能级模型分析。若输入一个范围，例如1-20，则对范围内的每个激发态进行二能级分析。

第4.24.2.2节给出了一个例子。


<!-- p.372 -->




### 3.27.3 研究(超)极化率密度[Study (hyper)polarizability density]

介绍(超)极化率密度的博客文章是“使用Multiwfn计算(超)极化率密度”(http://sobereva.com/305，中文)。

(超)极化率密度可非常容易地用Multiwfn绘制为平面图和等值面图。此量在讨论给定分子(超)极化率本质时很有用。若你的工作中使用了此功能，建议引用我的论文J. Comput. Chem., 38, 1574 (2017)，其中涉及(超)极化率密度分析并给出了简要介绍。我的其它出版物也展示了此方法的示例应用：Carbon, 165, 461 (2020)、J. Phys. Chem. C, 124, 7353 (2020)、J. Phys. Chem. A, 124, 5563 (2020)、J. Phys. Chem. C, 124, 845 (2020)。

(超)极化率密度理论与对(超)极化率的空间贡献 有一个著名的(电)偶极矩Taylor展开


$$\mathbf{\mu}(\mathbf{F})=-\frac{\partial E}{\partial\mathbf{F}}=\mathbf{\mu}_{0}+\mathbf{\alpha}\mathbf{F}+(1/2)\mathbf{\beta}\mathbf{F}^{2}+(1/6)\mathbf{\gamma}\mathbf{F}^{3}+\ldots$$

<!-- formula-ocr: formula_p372_274.png 已替换为LaTeX, 原图保留备查 -->

其中F是外电场矢量，E是体系总能量，μ和μ0分别是当前电偶极矩和永久偶极矩，α、β和γ分别是极化率、第一和第二超极化率张量。

类似地，关于F的Taylor展开可应用于电子密度


$$\boldsymbol{\mu}(\mathbf{F}) = \int -\rho(\mathbf{r}, \mathbf{F}) \mathbf{r} \, \mathrm{d} \mathbf{r}$$

<!-- formula-ocr: formula_p372_275.png 已替换为LaTeX, 原图保留备查 -->

$$\mathbf{\mu}_{0}=-\frac{\partial E}{\partial\mathbf{F}}\bigg|_{\mathbf{F}=0}\quad\mathbf{a}=-\frac{\partial^{2}E}{\partial\mathbf{F}^{2}}\bigg|_{\mathbf{F}=0}\quad\mathbf{\beta}=-\frac{\partial^{3}E}{\partial\mathbf{F}^{3}}\bigg|_{\mathbf{F}=0}\quad\mathbf{\gamma}=-\frac{\partial^{4}E}{\partial\mathbf{F}^{4}}\bigg|_{\mathbf{F}=0}$$


$$\mathbf{\boldsymbol{\beta}}=\int-\mathbf{\boldsymbol{\rho}}^{(2)}(\mathbf{r})\mathbf{r}\mathrm{d}\mathbf{r}\qquad\boldsymbol{\gamma}=\int-\mathbf{\boldsymbol{\rho}}^{(3)}(\mathbf{r})\mathbf{r}\mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p372_276.png 已替换为LaTeX, 原图保留备查 -->

其中ρ(1)被称为极化率密度，而ρ(2)和ρ(3)分别被称为第一和第二超极化率密度。利用(超)极化率密度，我们可轻松考察不同空间区域对分子总(超)极化率的贡献。

第二超极化率密度ρ(3)是三阶张量函数，可显式表示为


$$\rho_{ijk}^{(3)}(\mathbf{r})=\frac{\partial^{3}\rho(\mathbf{r})}{\partial F_{i}\partial F_{j}\partial F_{k}}\bigg|_{\mathbf{F}=0}$$

<!-- formula-ocr: formula_p372_277.png 已替换为LaTeX, 原图保留备查 -->

不可能讨论它的所有分量，因为多达3×3×3=27个分量。假设γZZZZ是γ最关键的分量，我们可简单研究ρZZZ(r)：


<!-- p.373 -->




$$\rho_{zzz}^{(3)}(\mathbf{r})=\frac{\partial^{3}\rho(\mathbf{r})}{\partial F_{z}^{3}}\bigg|_{F_{z}=0}$$

<!-- formula-ocr: formula_p373_278.png 已替换为LaTeX, 原图保留备查 -->

它与γZZZZ的关系为

(3)(𝐫)是点r对γZZZZ的贡献。若将其绘制为等值面图或平面图，γZZZZ的来源可直观揭示。然而，−𝑧𝜌𝑧𝑧𝑧 Clearly, −𝑧𝜌𝑧𝑧𝑧 (3)(𝐫)的缺点是它依赖于原点的选择，原点有些任意，因此𝜌𝑧𝑧𝑧 (3)本身作为与原点无关的量也有其研究价值。

(3)是用有限差分法（如何推导见我的文章http://sobereva.com/305）获得𝜌𝑧𝑧𝑧的最容易方式

FFFF−−−+−=ρρρρρ zzzF 3)3( )2()(2)(2)2( zzzz )(2 z

其中Fz是沿Z轴施加的外电场强度。诸如ρ(Fz)和ρ(-Fz)等函数分别表示沿Z轴正负方向施加Fz时产生的电子密度分布。此情形下的Fz对应有限差分步长，不应太大或太小，否则数值误差会显著。根据我的经验，0.003 a.u.是Fz的良好选择。

类似地，可轻松导出极化率密度的方程


$$\gamma_{z z z z}=\int-z\rho_{z z z}^{(3)}(\mathbf{r})\mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p373_279.png 已替换为LaTeX, 原图保留备查 -->

以及第一超极化率密度的方程

用Multiwfn研究(超)极化率密度 通过主功能24的子功能3，可非常方便地绘制任何(超)极化率密度以及对(超)极化率空间贡献的平面图和等值面图。一旦Multiwfn生成后者的格点数据并导出为.cub文件，就可进一步计算原子或片段对(超)极化率的贡献，如第4.24.3节例子所示。

本功能按以下步骤使用 (1) 启动Multiwfn并载入包含所研究体系原子信息的文件，如.xyz、.pdb、.mwfn、.fch等，见第2.5节。

(2) 进入主功能24的子功能3。 (3) 选择你希望研究的量 (4) 选择感兴趣的方向(X或Y或Z) 假设你在步骤(3)中选择了“第二超极化率密度及对第二超极化率的空间贡献(second hyperpolarizability density and spatial contribution to second

hyperpolarizability)”而在步骤(4)中选择“Z”，则之后你可研究−𝑧𝜌𝑧𝑧𝑧 (3)和𝜌𝑧𝑧𝑧 (3)。

<!-- p.374 -->


(5) 选择选项 (option) 1，以生成不同外电场下单点计算的 Gaussian 输入文件。你可以手动修改这些文件中的默认关键词。默认情况下，计算在 PBE0/aug-cc-pVTZ 水平下进行。

(6) 手动用 Gaussian 运行 .gjf 文件，然后会生成 .wfx 文件 (7) 选择选项 (option) 2 以载入 .wfx 文件 (8) 现在你可以选择要做的事情。如果你选择计算(超)极化率的格点数据或(超)极化率的空间贡献，那么你可以直接可视化它们的等值面图，或将格点数据导出为 .cub 文件。此外，你还可以选择绘制这些函数的平面图。

关于分子取向 (About molecular orientation) 需要注意的是，在实际中，我们真正感兴趣的往往是沿分子偶极矩方向的分量，而偶极矩方向通常不与任何笛卡尔轴平行。在这种情况下，在使用本功能之前，你应该重新调整体系取向，使偶极矩恰好平行于某个笛卡尔轴，例如 Z 轴。Multiwfn 可以通过 3.300.7 节所述的功能轻松实现这种重取向。具体做法是，在启动 Multiwfn 后载入当前体系的波函数文件，然后输入

300 //Other function (Part 3) 7 //Geometry operation on the present system 7 //Make electric dipole moment parallel to a vector or Cartesian axis 3 //Parallel to Z axis -1 //Output system to .xyz file 然后你就可以用导出的 .xyz 文件作为研究(超)极化率密度的输入文件。关于研究(超)极化率密度及(超)极化率空间贡献的例子，见 4.24.3 节。

### 3.27.5 通过单位球和矢量表示法可视化(超)极化率 (Visualize (hyper)polarizability via unit sphere and vector representations)

如果你对(超)极化率还不熟悉，请先查阅 3.27.1 节以获得基础知识。在本节中，将介绍单位球表示法 (unit sphere representation)，它在 J. Comput. Chem., 32,1128 (2011) 中被提出，用于直观表示一阶超极化率张量，而我还把这一思想推广到了极化率和二阶超极化率。

理论 (Theory) 回顾分子偶极矩与外场之间的关系

$$\mathbf{p}=\mathbf{p}_{0}+\mathbf{a}\cdot\mathbf{F}+(1/2)\mathbf{β}\cdot\mathbf{F}\cdot\mathbf{F}+(1/6)\mathbf{\gamma}\cdot\mathbf{F}\cdot\mathbf{F}\cdot\mathbf{F}+\ldots$$

β 被称为一阶超极化率张量，分量 βABC 正比于分别沿 B 和 C 方向的两个入射电场组合所引起的沿 A 方向的诱导偶极矩的大小。

在单位球表示法中，有效偶极矢量 (effective dipole vector) 定义为

$$\boldsymbol{\beta}^{\mathrm{e f f}}(\theta,\phi)=\boldsymbol{\beta}\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)$$

<!-- p.375 -->


其中 θ 和 φ 是球极坐标的角度，e(θ,φ) 是垂直于球面的单位矢量。更具体地，βeff 的分量可以明确写为

$$\boldsymbol{\beta}_{i}^{\mathrm{e f f}}=\sum_{j}\sum_{k}\beta_{i,j,k}\boldsymbol{e}_{k}\boldsymbol{e}_{j}\quad i,j,k=\{\boldsymbol{x},\boldsymbol{y},\boldsymbol{z}\}$$

<!-- formula-ocr: formula_p375_280.png 已替换为LaTeX, 原图保留备查 -->

βeff(θ,φ) 矢量的取向和长度分别反映了沿 (θ,φ) 方向施加的两个入射外电场组合所引起的诱导偶极矩的方向和大小。如果在包围分子的球面每个顶点上都计算 βeff，就可以清晰、生动地理解分子偶极矩对外加在各个方向上的外电场的响应。原文只把这种表示法用于二次谐波产生 (second harmonic generation, SHG) 类型的 β，实际上它也可以应用于其他种类的 β，包括静态和动态情形 (在后一种情况下，强度随时间变化的外加电场来自入射电磁波，其方向垂直于电磁波的传播方向)。

基于 βeff 同样的思想，我定义了以下量

$$\boldsymbol{\alpha}^{\mathrm{eff}}(\theta,\phi)$$

$$\begin{aligned}\mathbf{a}^{\mathrm{eff}}(\theta,\phi)&=\mathbf{a}\cdot\mathbf{e}(\theta,\phi)\\\boldsymbol{\gamma}^{\mathrm{eff}}(\theta,\phi)&=\boldsymbol{\gamma}\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\end{aligned}$$

$$\begin{aligned}\mathbf{a}^{\mathrm{eff}}(\theta,\phi)&=\mathbf{a}\cdot\mathbf{e}(\theta,\phi)\\\boldsymbol{\gamma}^{\mathrm{eff}}(\theta,\phi)&=\boldsymbol{\gamma}\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\end{aligned}$$

$$\begin{aligned}\mathbf{a}^{\mathrm{eff}}(\theta,\phi)&=\mathbf{a}\cdot\mathbf{e}(\theta,\phi)\\\boldsymbol{\gamma}^{\mathrm{eff}}(\theta,\phi)&=\boldsymbol{\gamma}\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\end{aligned}$$

所谓 β 的矢量表示法 (vector representation) 对应于把 (βx, βy, βz) 矢量画成一个箭头，其分量定义为

$$\beta_{i}=(1/3)\sum_{j}(\beta_{i j j}+\beta_{j j i}+\beta_{j i j})\quad i,j=\left\{x,y,z\right\}$$

<!-- formula-ocr: formula_p375_281.png 已替换为LaTeX, 原图保留备查 -->

$$\begin{aligned}\mathbf{a}^{\mathrm{eff}}(\theta,\phi)&=\mathbf{a}\cdot\mathbf{e}(\theta,\phi)\\\boldsymbol{\gamma}^{\mathrm{eff}}(\theta,\phi)&=\boldsymbol{\gamma}\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\end{aligned}$$

我还提出了 α 的矢量表示法，情况与 β 的矢量表示法很不相同。沿 X、Y 和 Z 轴画双向箭头，其长度分别代表相应方向上 α 的大小，定义为

$$(\gamma_{x},\gamma_{y},\gamma_{z})$$

<!-- formula-ocr: formula_p375_282.png 已替换为LaTeX, 原图保留备查 -->

类似地，γ 的矢量表示法对应于沿 X、Y 和 Z 轴画双向箭头，其长度分别代表相应方向上 γ 的大小 (γx, γy, γz)，计算方式为

$$\gamma_{i}=(1/15)\sum_{j}(\gamma_{ijji}+\gamma_{ijij}+\gamma_{iijj})\quad i,j=\left\{x,y,z\right\}$$

<!-- formula-ocr: formula_p375_283.png 已替换为LaTeX, 原图保留备查 -->

<!-- p.376 -->


用法 (Usage)

Multiwfn 能够对 α、β 和 γ 进行单位球表示分析，即根据载入的(超)极化率张量生成 VMD 软件 (http://www.ks.uiuc.edu/Research/vmd/) 的绘图脚本。此外，还可以生成对应于矢量表示法 (vector representation) 的 β 的绘图脚本。

在启动 Multiwfn 后，你应该载入一个包含所研究分子原子信息的文件。例如，可以使用 .xyz、.pdb 和 .fch，见 2.5 节。原子信息将用于确定单位球表示中所涉及球体的合适半径。

进入本模块 (主功能 (main function) 24 的子功能 (subfunction) 5) 后，你可以用许多选项来调节单位球和矢量表示的参数，例如箭头长度的缩放因子、箭头半径等，它们都是完全自明的。通过选择选项 (option) 1 或 2 或 3，Multiwfn 将分别从特定文件载入 α 或 β 或 γ 张量 (见下文)，然后在当前文件夹下生成对应于单位球表示的 VMD 绘图脚本 (分别为 alpha.tcl、beta.tcl 和 gamma.tcl)，同时还会生成对应于矢量表示的脚本 (alpha_vec.tcl、beta_vec.tcl 和 gamma_vec.tcl)。然后，用 VMD 运行这些脚本，即可立即得到相应图形。

值得一提的是，有一个选项 (option) “-8 Toggle making longest arrow on sphere has specific length”(切换使球面上最长箭头具有特定长度)。如果你选择一次将其状态切换为 “Yes”，那么在选择选项 (option) 1 或 2 或 3 之后，程序会要求你输入球面上最长箭头的期望长度。通过该选项，你可以使具有很不相同(超)极化率大小的体系由 VMD 绘制的图易于相互比较。

包含(超)极化率张量的文件的准备 (Preparation of the file containing (hyper)polarizability tensor)

包含 α 或 β 或 γ 张量的文件可由主功能 (main function) 24 的子功能 (subfunction) 1 直接生成，方法是从 Gaussian 的 “polar” 任务输出文件中提取相应数据。在该功能中，你应该选择选项 (option) “-4 Export (hyper)polarizability as .txt file after parsing”(解析后将(超)极化率导出为 .txt 文件)一次，将其状态切换为 “Yes”，然后在通过相应选项解析数据后，α 会被导出到当前文件夹下的 alpha.txt，β 会被导出到 beta.txt，γ 会被导出到 gamma.txt，它们就是本功能所需要的文件。

包含(超)极化率的文件也可以手动准备，在这种情况下数据可以由 Gaussian 以外的量子化学程序产生。文件格式是自由的，张量分量的顺序如下 (用 Fortran 语法表示)

- 极化率 (Polarizability)：((α(i,j),j=1,3),i=1,3)
- 一阶超极化率 (First-order hyperpolarizability)：(((β(i,j,k),k=1,3),j=1,3),i=1,3)
- 二阶超极化率 (Second-order hyperpolarizability)：((((γ(i,j,k,l),l=1,3),k=1,3),j=1,3),i=1,3) 其中指标 i 的循环最慢。例如，下面是一个记录 α 张量的文件 (高亮文字为注释)：

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
