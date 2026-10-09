# 3.27 (Hyper)polarizability analysis (24)

> Multiwfn manual, p.361–376. Images: `../imgs/`.

---

<!-- p.361 -->

degenerated, namely having exactly the same eigenvalues; in this case their order (index) is arbitrary, and the automatically determined correspondence between NOCV pairs and orbitals may be unexpected. In this case you can use option -6 to choose a NOCV pair, and then manually input indices of the two orbitals that the pair should correspond to. This option can be used multiple times to redefine multiple NOCV pairs.

Abundant examples of ETS-NOCV analysis are given in Section 4.23.


## 3.27 (Hyper)polarizability analysis (24)

Main function 24 is a collection of functions of studying polarizability and hyperpolarizability. The subfunctions are described in this section. It is noteworthy that atomic polarizability can be calculated by fuzzy analysis module, which is described in Section 3.18.12.


### 3.27.1 Parse output of (hyper)polarizability task of Gaussian and evaluate relevant quantities



The output of (hyper)polarizability task of Gaussian (polar keyword) is difficult to understand, at least for beginners. This function is used to parse these outputs and then print them in a more readable format, and at the same time some quantities relating to (hyper)polarizability are outputted. Currently this function is formally compatible with Gaussian 09 and 16.

Basic concepts and theory backgrounds Energy of a system can be written as Taylor expansion with respect to uniform external electric field F

$$\begin{align*}E(\mathbf{F})&=E(\mathbf{0})+\frac{\partial E}{\partial\mathbf{F}}\bigg|_{\mathbf{F}=0}\mathbf{F}+\frac{1}{2}\frac{\partial^{2}E}{\partial\mathbf{F}^{2}}\bigg|_{\mathbf{F}=0}\mathbf{F}^{2}+\frac{1}{6}\frac{\partial^{3}E}{\partial\mathbf{F}^{3}}\bigg|_{\mathbf{F}=0}\mathbf{F}^{3}+\frac{1}{24}\frac{\partial^{4}E}{\partial\mathbf{F}^{4}}\bigg|_{\mathbf{F}=0}\mathbf{F}^{4}+\ldots\\&\equiv E(\mathbf{0})-\boldsymbol{\mu}_{0}\mathbf{F}-\frac{1}{2}\boldsymbol{\alpha}\mathbf{F}^{2}-\frac{1}{6}\boldsymbol{\beta}\mathbf{F}^{3}-\frac{1}{24}\boldsymbol{\gamma}\mathbf{F}^{4}-\frac{1}{120}\delta\mathbf{F}^{5}-\frac{1}{720}\varepsilon\mathbf{F}^{6}\ldots\end{align*}$$


$$\begin{align*}E(\mathbf{F})&=E(\mathbf{0})+\frac{\partial E}{\partial\mathbf{F}}\bigg|_{\mathbf{F}=0}\mathbf{F}+\frac{1}{2}\frac{\partial^{2}E}{\partial\mathbf{F}^{2}}\bigg|_{\mathbf{F}=0}\mathbf{F}^{2}+\frac{1}{6}\frac{\partial^{3}E}{\partial\mathbf{F}^{3}}\bigg|_{\mathbf{F}=0}\mathbf{F}^{3}+\frac{1}{24}\frac{\partial^{4}E}{\partial\mathbf{F}^{4}}\bigg|_{\mathbf{F}=0}\mathbf{F}^{4}+\ldots\\&\equiv E(\mathbf{0})-\boldsymbol{\mu}_{0}\mathbf{F}-\frac{1}{2}\boldsymbol{\alpha}\mathbf{F}^{2}-\frac{1}{6}\boldsymbol{\beta}\mathbf{F}^{3}-\frac{1}{24}\boldsymbol{\gamma}\mathbf{F}^{4}-\frac{1}{120}\delta\mathbf{F}^{5}-\frac{1}{720}\varepsilon\mathbf{F}^{6}\ldots\end{align*}$$

<!-- formula-ocr: formula_p361_256.png 已替换为LaTeX, 原图保留备查 -->

where μ0 is permanent dipole moment, which is a vector; α is polarizability, which is a matrix (second rank tensor); β is first hyperpolarizability, which is a third rank tensor and known as second-order nonlinear optical response (NLO) coefficient; γ is second hyperpolarizability, which is a fourth rank tensor and known as third-order NLO coefficient. The higher terms such as δ and ε are very unimportant and thus rarely discussed. The (hyper)polarizability tensors are directly correlated to the frequency of external field F. If F has zero-frequency (static electric field), then the (hyper)polarizabilities are known as static or frequency-independent ones. The dynamic or frequency-dependent (hyper)polarizabilities correspond to those at external electromagnetic fields with non-zero frequency.


<!-- p.362 -->

- Polarizability (α) Dipole moment of a system in uniform electric field can be written as

$$\mathbf{\mu}=-\frac{\partial E}{\partial\mathbf{F}}=\mathbf{\mu}_{0}+\underbrace{\mathbf{\alpha}\mathbf{F}}_{\mathbf{\mu}_{1}}+\underbrace{(1/2)\mathbf{\beta}\mathbf{F}^{2}}_{\mathbf{\mu}_{2}}+\underbrace{(1/6)\mathbf{\gamma}\mathbf{F}^{3}}_{\mathbf{\mu}_{3}}+\ldots$$

The linear response of dipole moment with respect to F, namely the μ1 term, can be explicitly written as below

$$\boldsymbol{\mu}_{1}=\boldsymbol{\alpha}\cdot\mathbf{F}\quad\Rightarrow\quad\begin{bmatrix}\mu_{x}\\ \mu_{y}\\ \mu_{z}\end{bmatrix}=\begin{bmatrix}\alpha_{xx}&\alpha_{xy}&\alpha_{xz}\\ \alpha_{yx}&\alpha_{yy}&\alpha_{yz}\\ \alpha_{zx}&\alpha_{zy}&\alpha_{zz}\end{bmatrix}\begin{bmatrix}F_{x}\\ F_{y}\\ F_{z}\end{bmatrix}$$

The polarizability α is a symmetric matrix rather than a scalar, implying the difference of polarizability in different directions. In order to facilitate comparison of overall polarizability between various systems, it is convenient to define the isotropic average polarizability


$$\boldsymbol{\mu}_{1}=\boldsymbol{\alpha}\cdot\mathbf{F}\quad\Rightarrow\quad\begin{bmatrix}\mu_{x}\\ \mu_{y}\\ \mu_{z}\end{bmatrix}=\begin{bmatrix}\alpha_{xx}&\alpha_{xy}&\alpha_{xz}\\ \alpha_{yx}&\alpha_{yy}&\alpha_{yz}\\ \alpha_{zx}&\alpha_{zy}&\alpha_{zz}\end{bmatrix}\begin{bmatrix}F_{x}\\ F_{y}\\ F_{z}\end{bmatrix}$$

<!-- formula-ocr: formula_p362_257.png 已替换为LaTeX, 原图保留备查 -->

Anisotropy of polarizability can be defined in various ways: Definition 1: See Chem. Phys., 410, 90 (2013) for example


$$\langle\alpha\rangle=\mathrm{T r}(\mathbf{a})/3=(\alpha_{x x}+\alpha_{y y}+\alpha_{z z})/3$$

<!-- formula-ocr: formula_p362_258.png 已替换为LaTeX, 原图保留备查 -->

Definition 2: This definition is the most commonly used one, see J. Chem. Phys., 98, 3022 (1993) for example


$$\Delta\alpha=\sqrt{[(\alpha_{xx}-\alpha_{yy})^{2}+(\alpha_{xx}-\alpha_{zz})^{2}+(\alpha_{yy}-\alpha_{zz})^{2}+6(\alpha_{xy}^{2}+\alpha_{xz}^{2}+\alpha_{yz}^{2})]/2}$$

<!-- formula-ocr: formula_p362_259.png 已替换为LaTeX, 原图保留备查 -->

Definition 3: {ε} stand for eigenvalues of α ranking from small to large


$$\Delta\alpha=\sqrt{[(\alpha_{xx}-\alpha_{yy})^{2}+(\alpha_{xx}-\alpha_{zz})^{2}+(\alpha_{yy}-\alpha_{zz})^{2}]}/2$$

<!-- formula-ocr: formula_p362_260.png 已替换为LaTeX, 原图保留备查 -->

The α value along each of the three Cartesian axes can be defined as

- First hyperpolarizability (β) First hyperpolarizability β is a third rank tensor that can be described by a 3×3×3 matrix. Gaussian is capable of calculating both static and dynamic β. For the latter case, dc-Pockels form β(-ω;ω,0) and SHG form β(-2ω;ω,ω) can be evaluated.

$$\boldsymbol{\mu}_{1}=\boldsymbol{\alpha}\cdot\mathbf{F}\quad\Rightarrow\quad\begin{bmatrix}\mu_{x}\\ \mu_{y}\\ \mu_{z}\end{bmatrix}=\begin{bmatrix}\alpha_{xx}&\alpha_{xy}&\alpha_{xz}\\ \alpha_{yx}&\alpha_{yy}&\alpha_{yz}\\ \alpha_{zx}&\alpha_{zy}&\alpha_{zz}\end{bmatrix}\begin{bmatrix}F_{x}\\ F_{y}\\ F_{z}\end{bmatrix}$$

The β value in one of the three Cartesian axes can be calculated by the general equation


<!-- p.363 -->


$$\beta_{i}=(1/3)\sum_{j}(\beta_{i j j}+\beta_{j j i}+\beta_{j i j})\quad i,j=\left\{x,y,z\right\}$$

<!-- formula-ocr: formula_p363_261.png 已替换为LaTeX, 原图保留备查 -->

The magnitude of β is defined as

$$\mathrm{d e f}2:\quad<\gamma>=(1/5)(\gamma_{x x x x}+\gamma_{y y y y}+\gamma_{z z z z}+\gamma_{x x y y}+\gamma_{x x z z}+\gamma_{y y z z}+\gamma_{y y x x}+\gamma_{z z x x}+\gamma_{z z y y})$$


$$\boldsymbol{\beta}_{\mathrm{p r j}}=\sum_{i}\frac{\mu_{i}\boldsymbol{\beta}_{i}}{\left|\boldsymbol{\mu}\right|}\qquad\boldsymbol{\beta}_{\parallel}=(3/5)\boldsymbol{\beta}_{\mathrm{p r j}}$$

<!-- formula-ocr: formula_p363_262.png 已替换为LaTeX, 原图保留备查 -->

Some people prefer to discuss the perpendicular and parallel components of β with respect to Z axis, they are defined respectively as


$$\gamma_{i}=(1/15)\sum_{j}(\gamma_{ijji}+\gamma_{ijij}+\gamma_{iijj})\quad i,j=\left\{x,y,z\right\}$$

<!-- formula-ocr: formula_p363_263.png 已替换为LaTeX, 原图保留备查 -->

For static case, we can explicitly write out β in x, y and z directions as

and zZββ)5/1()(=⊥.

- Second hyperpolarizability (γ) Second hyperpolarizability γ is a fourth rank tensor of 3×3×3×3 form. Gaussian can calculate its static limit form γ(0;0,0,0); while for dynamic case, Gaussian is capable of calculating its EOKO (Electro-optic Kerr effect) form γ(-ω;ω,0,0) and SHG form γ(-2ω;ω,ω,0).

The i components of γ is defined as


$$\gamma_{\perp}=(1/15)\sum_{i}\sum_{j}(2\gamma_{i j j i}-\gamma_{i i j j})\quad i,j=\left\{x,y,z\right\}$$

<!-- formula-ocr: formula_p363_264.png 已替换为LaTeX, 原图保留备查 -->

$$\mathrm{d e f}2:\quad<\gamma>=(1/5)(\gamma_{x x x x}+\gamma_{y y y y}+\gamma_{z z z z}+\gamma_{x x y y}+\gamma_{x x z z}+\gamma_{y y z z}+\gamma_{y y x x}+\gamma_{z z x x}+\gamma_{z z y y})$$

There are two definitions of average of γ, as shown below. Definition 1 is more common, and it is equivalent to γ||

$$\mathrm{d e f}2:\quad<\gamma>=(1/5)(\gamma_{x x x x}+\gamma_{y y y y}+\gamma_{z z z z}+\gamma_{x x y y}+\gamma_{x x z z}+\gamma_{y y z z}+\gamma_{y y x x}+\gamma_{z z x x}+\gamma_{z z y y})$$

The γ_|_ is defined as


$$\gamma_{\perp}=(1/15)\sum_{i}\sum_{j}(2\gamma_{ijij}-\gamma_{ijji})\quad i,j=\{x,y,z\}$$

Most of above-mentioned equations about γ can be found in Chapter 5 of Reviews in Computational Chemistry, Vol. 12 (1998).

- Hyper-Rayleigh scattering (HRS) and depolarization ratio (DR) The Hyper-Rayleigh Scattering (HRS) technique was developed as an alternative method to EFISHG for the measurement of molecular hyperpolarizabilities. HRS can be used to directly


<!-- p.364 -->

measure β of all molecules, including nonpolar molecules, which cannot be studied by EFISHG. See Acc. Chem. Res., 31, 675 (1998) for introduction.

According to intensity of incident light at given frequency (ω) and that of scattered light with doubled frequency (2ω) detected at 90 angle, the βHRS could be determined, which correlates components of frequency-dependent β tensor as follows. See Phys. Chem. Chem. Phys., 10, 6223 (2008) for more details.

$$\beta_{\mathrm{H R S}}(-2\omega;\omega,\omega)=\sqrt{\left\langle\beta_{Z Z Z}^{2}\right\rangle+\left\langle\beta_{X Z Z}^{2}\right\rangle}$$

$$\begin{aligned}\left\langle\beta_{X Z Z}^{2}\right\rangle=&\frac{1}{35}\sum_{\zeta}\beta_{\zeta\varsigma\varsigma}^{2}+\frac{4}{105}\sum_{\varsigma\neq\eta}\beta_{\varsigma\varsigma\varsigma}\beta_{\varsigma\eta\eta}-\frac{2}{35}\sum_{\varsigma\neq\eta}\beta_{\varsigma\varsigma\varsigma}\beta_{\eta\eta\varsigma}+\frac{8}{105}\sum_{\varsigma\neq\eta}\beta_{\varsigma\varsigma\eta}^{2}\\ &+\frac{3}{35}\sum_{\zeta\neq\eta}\beta_{\varsigma\eta\eta}^{2}-\frac{2}{35}\sum_{\zeta\varsigma\eta}\beta_{\varsigma\varsigma\eta}\beta_{\eta\varsigma\varsigma}+\frac{1}{35}\sum_{\zeta\neq\eta\neq\xi}\beta_{\varsigma\eta\eta}\beta_{\varsigma\varsigma\xi}-\frac{2}{105}\sum_{\zeta\neq\eta\neq\xi}\beta_{\varsigma\varsigma\varsigma}\beta_{\eta\eta\varsigma}\\ &-\frac{2}{105}\sum_{\varsigma\neq\eta\neq\xi}\beta_{\varsigma\varsigma\eta}\beta_{\eta\varsigma\varsigma}+\frac{2}{35}\sum_{\varsigma\neq\eta\neq\xi}\beta_{\varsigma\eta\xi}^{2}-\frac{2}{105}\sum_{\zeta\neq\eta\neq\xi}\beta_{\varsigma\eta\varsigma}\beta_{\eta\varsigma\varsigma}\end{aligned}$$


$$\beta_{\mathrm{H R S}}(-2\omega;\omega,\omega)=\sqrt{\left\langle\beta_{Z Z Z}^{2}\right\rangle+\left\langle\beta_{X Z Z}^{2}\right\rangle}$$

<!-- formula-ocr: formula_p364_266.png 已替换为LaTeX, 原图保留备查 -->

$$\begin{aligned}\left\langle\beta_{X Z Z}^{2}\right\rangle=&\frac{1}{35}\sum_{\zeta}\beta_{\zeta\varsigma\varsigma}^{2}+\frac{4}{105}\sum_{\varsigma\neq\eta}\beta_{\varsigma\varsigma\varsigma}\beta_{\varsigma\eta\eta}-\frac{2}{35}\sum_{\varsigma\neq\eta}\beta_{\varsigma\varsigma\varsigma}\beta_{\eta\eta\varsigma}+\frac{8}{105}\sum_{\varsigma\neq\eta}\beta_{\varsigma\varsigma\eta}^{2}\\ &+\frac{3}{35}\sum_{\zeta\neq\eta}\beta_{\varsigma\eta\eta}^{2}-\frac{2}{35}\sum_{\zeta\varsigma\eta}\beta_{\varsigma\varsigma\eta}\beta_{\eta\varsigma\varsigma}+\frac{1}{35}\sum_{\zeta\neq\eta\neq\xi}\beta_{\varsigma\eta\eta}\beta_{\varsigma\varsigma\xi}-\frac{2}{105}\sum_{\zeta\neq\eta\neq\xi}\beta_{\varsigma\varsigma\varsigma}\beta_{\eta\eta\varsigma}\\ &-\frac{2}{105}\sum_{\varsigma\neq\eta\neq\xi}\beta_{\varsigma\varsigma\eta}\beta_{\eta\varsigma\varsigma}+\frac{2}{35}\sum_{\varsigma\neq\eta\neq\xi}\beta_{\varsigma\eta\xi}^{2}-\frac{2}{105}\sum_{\zeta\neq\eta\neq\xi}\beta_{\varsigma\eta\varsigma}\beta_{\eta\varsigma\varsigma}\end{aligned}$$

The associated depolarization ratio (DR) is defined as

2DR β= β ZZZ XZZ 2

Molecules with Td point group have DR exactly equals 1.5. If the half of wavelength of incident light is close to absorption band of the current system calculated at same level using TDDFT, the printed DR may be lower than 1.5 due to SHG resonance.

There are some relevant quantities about HRS could be studied, as shown below, see also J. Chem. Phys., 136, 024506 (2012) for more information. Note that for consistency, the ZXX in the equations of this paper have been replaced with XZZ, they are numerically identical in the present context.

2〉 can be regarded as contributed by two components, dipolar (J=1) and octupolar (J=3): The 〈𝛽𝑍𝑍𝑍 2〉 and 〈𝛽𝑋𝑍𝑍


$$\left\langle\beta_{X Z Z}^{2}\right\rangle=\frac{1}{45}\mid\beta_{J=1}\mid^{2}+\frac{4}{105}\mid\beta_{J=3}\mid^{2}$$

<!-- formula-ocr: formula_p364_267.png 已替换为LaTeX, 原图保留备查 -->


<!-- p.365 -->

clearly the two components can be evaluated as follows


$$\begin{aligned}&|\boldsymbol{\beta}_{J=1}|=\sqrt{6\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle-9\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle}\\&|\boldsymbol{\beta}_{J=3}|=\sqrt{\frac{1}{2}\left(-7\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle+63\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle\right)}\\ \end{aligned}$$

<!-- formula-ocr: formula_p365_268.png 已替换为LaTeX, 原图保留备查 -->

$$\begin{aligned}&|\boldsymbol{\beta}_{J=1}|=\sqrt{6\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle-9\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle}\\&|\boldsymbol{\beta}_{J=3}|=\sqrt{\frac{1}{2}\left(-7\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle+63\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle\right)}\\ \end{aligned}$$


$$\rho = |\beta_{J=3}| / |\beta_{J=1}|$$

<!-- formula-ocr: formula_p365_269.png 已替换为LaTeX, 原图保留备查 -->

For small molecules, the one with larger dipole moment tends to have larger (βJ=1), higher DR and lower ρ, while the one with smaller dipole moment tends to have larger (βJ=3), lower DR and higher ρ.

Assuming a general elliptically polarized incident light propagating along the X direction, with

a state of polarization characterized by two angles (, δ), the intensity of the harmonic light scattered at 90° along the Y direction and vertically (V) polarized along the Z-axis are given by Bersohn’s

expression (the phase retardation δ is assumed to be π/2)


$$\mathrm{I}_{\Psi\mathrm{V}}^{2\omega}\propto\left\langle\beta_{X Z Z}^{2}\right\rangle\cos^{4}\Psi+\left\langle\beta_{Z Z Z}^{2}\right\rangle\sin^{4}\Psi+\sin^{2}\Psi\cos^{2}\Psi\left\langle(\beta_{Z X Z}+\beta_{Z Z X})^{2}-2\beta_{Z Z Z}\beta_{X Z Z}\right\rangle$$

<!-- formula-ocr: formula_p365_270.png 已替换为LaTeX, 原图保留备查 -->

$$\begin{aligned}&|\boldsymbol{\beta}_{J=1}|=\sqrt{6\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle-9\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle}\\&|\boldsymbol{\beta}_{J=3}|=\sqrt{\frac{1}{2}\left(-7\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle+63\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle\right)}\\ \end{aligned}$$

incident light beam.

According to theoretically calculated SHG form of β tensor, all above-mentioned quantities could be readily predicted. The variation of 𝐼V 2𝜔 with respect to  could be scanned and plotted as curve map.

Input file and usage In this function, Multiwfn outputs all components of dipole moment, polarizability and 1st/2nd hyperpolarizability (if available) with explicit labels, as well as all of their relevant quantities introduced above, such as isotropic polarizability, polarizability anisotropy, hyperpolarizability in

$$\begin{aligned}&|\boldsymbol{\beta}_{J=1}|=\sqrt{6\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle-9\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle}\\&|\boldsymbol{\beta}_{J=3}|=\sqrt{\frac{1}{2}\left(-7\left\langle\boldsymbol{\beta}_{ZZZ}^{2}\right\rangle+63\left\langle\boldsymbol{\beta}_{XZZ}^{2}\right\rangle\right)}\\ \end{aligned}$$

The polar keyword in Gaussian is specific for calculating α, β and γ based on analytic derivatives (by means of coupled-perturbed SCF equation) or numerical derivatives (by means of finite field treatment). Notice that in the Gaussian input file you must specify #P, otherwise Multiwfn cannot properly parse relevant information.

After you enter present function of Multiwfn, you should select actual case of your Gaussian (hyper)polarizability calculation, so that Multiwfn can successfully parse the outputted information and show valuable data for you. As can be seen on the menu, there are seven options corresponding to different situations:

(1) polar keyword + methods supporting analytic 3-order derivatives (HF/DFT/Semi-empirical


<!-- p.366 -->

methods)

(2) polar keyword + methods supporting analytic 2-order derivatives (e.g. MP2) (3) polar=Cubic keyword + methods supporting analytic 2-order derivatives (4) polar keyword + methods supporting analytic 1-order derivatives (CISD, QCISD, CCSD, MP3, MP4(SDQ), etc.)

(5) polar=DoubleNumer (equivalent to Polar=EnOnly) keyword + methods supporting analytic 1-order derivatives

(6) polar keyword + methods only supporting energy calculation (CCSD(T), QCISD(T), MP4(SDTQ), MP5, etc.)

(7) polar=gamma keyword + methods supporting analytic 3-order derivatives (HF/DFT/Semi-empirical methods)

All options print polarizability and relevant data, only options (1), (3) and (5) also print first hyperpolarizability, only (7) also prints second hyperpolarizability.

For case (1), if CPHF=RdFreq is specified along with polar or you used polar=DCSHG, and meantime the external field frequencies (e.g. 0.05 0.07 0.1 or 532 nm 680 nm) are provided after molecular geometry with a blank line in front of it, Gaussian will calculate and output frequency-dependent (hyper)polarizabilities along with static (hyper)polarizability. The CPHF=RdFreq polar

`HRS_angle.txt`

For cases (1) and (7), by default Multiwfn only parses static (hyper)polarizability. If you wish to parse the frequency-dependent ones instead of the static one, before selecting option 1 or 7 to start parsing, you should select option “-1 Toggle loading frequency-dependent result for options 1 and 7” first. Then after starting parsing, user can choose the result at which frequency will be parsed.

Note that in the case (1) if you choose to parse β(-2ω;ω,ω), you must employ polar=DCSHG keyword in Gaussian input file.

The quantities related to hyper-Rayleigh scattering (HRS) experiment mentioned above are

also automatically printed when you request Multiwfn to parse frequency-dependent β(-2ω;ω,ω) based on output file of polar=DCSHG. After that, you can also let Multiwfn scan 𝐼V 2𝜔 versus , then the generated HRS_angle.txt could be plotted using Origin and so on.

It is noteworthy that, it is well known that the sign of all hyperpolarizability components outputted by Gaussian are wrong and should be multiplied by -1, Multiwfn automatically accounts for this problem.

Before carrying out parsing, via option -3 of interface of present function, you can choose the unit in the output. Atomic unit, SI unit and esu unit can be chosen. The conversion factors are

SI esu

μ 1 a.u. 8.47835×10-30 C m 2.54175 ×10-18 esu α 1 a.u. 1.6488×10-41 C2m2J-1 1.4819×10-25 esu β 1 a.u. 3.20636×10-53 C3m3J-2 8.63922×10-33 esu γ 1 a.u. 6.23538×10-65 C4m4J-3 5.03670×10-40 esu

The polarizability α is often expressed in terms of "polarizability volume" (α'), which has volume unit. α (1 a.u.)=α' (0.14818470 Å3).


<!-- p.367 -->

An example is given in Section 4.24.1. More discussion and examples about this function can be found in my blog article "Using Multiwfn to analyze polarizability and hyperpolarizability outputted by Gaussian" (http://sobereva.com/231, in Chinese)


### 3.27.2 Study (hyper)polarizability by sum-over-states (SOS) method and two- or three-level model analyses



This function is used to calculate polarizability, first, second, and third hyperpolarizabilities based on the well-known sum-over-states (SOS) method, as described below. In addition, the popular two-level model analysis for the first hyperpolarizability as well as its extension (three-level model) can also be realized in this module, as introduced in Section 3.27.2.2.

3.27.2.1 Calculation of (hyper)polarizability

A brief survey of the theories for evaluating (hyper)polarizability Some basic concepts of (hyper)polarizability are introduced in Section 3.27.1. There are a few different ways to calculate (hyper)polarizability, including derivative method, sum-over-states (SOS) and response method

(1) Derivative method: This is the most straightforward and commonly used one. The derivatives needed by static (hyper)polarizability can be evaluated analytically by means of coupled-perturbed SCF (CPSCF) equation; specifically, CPHF for HF and CPKS for KS-DFT. These derivatives can also be evaluated numerically by means of finite difference technique, which is also known as finite field (FF) method. Evidently FF is much slower and not as accurate as CPSCF, however it is still useful, because high-order of analytic derivatives, especially the ones at sophisticated post-HF levels, are not widely supported by many quantum chemistry programs due to the difficulties in coding. When all requested derivatives are available analytically, derivative method will be very efficient. The frequency-dependent variant of CPSCF equation enables the derivative method to evaluate dynamic (hyper)polarizability, but there is no way to evaluate dynamic (hyper)polarizability in terms of FF treatment. The polar keyword in Gaussian, as discussed carefully in Section 3.27.1, corresponds to this derivative method.

(2) SOS method: This method for evaluating static and dynamic (hyper)polarizability is relatively inefficient, because in principle it involves a sum over all excited states (in practical applications, taking 60-120 lowest states into account are often enough), while determination of a large number of excited states is usually quite time consuming in ab initio cases (e.g. CIS and TDDFT), especially for large system (e.g. > 40 atoms). Due to the high computational cost, SOS is generally not recommended for evaluation of (hyper)polarizability when derivative method can be carried out analytically. The only advantages of SOS may be that the contribution from different states can be separated and discussed respectively, and when transition dipole moments between different excited states are available in hand, the (hyper)polarizability at different frequencies can be evaluated rather rapidly. It is noteworthy that the SOS based on the cheap semi-empirical ZINDO calculation (SOS/ZINDO) is very popular for evaluating (hyper)polarizability of large systems.

(3) Response method: This method is specific for dynamic (hyper)polarizability and also known as propagator method. TDHF and TDDFT are its two practical realizations. This method is not prevalently supported by mainstream quantum chemistry codes.


<!-- p.368 -->

Working equations of SOS method The explicit SOS equations for evaluating polarizability and 1st/2nd/3rd hyperpolarizability can be found in J. Chem. Phys., 99, 3738 (1993), the idea was originally proposed by Orr and Ward in Mol. Phys., 20, 512 (1971).

The equations for polarizability α and first hyperpolarizability β are (all units are in a.u.)

$$\alpha_{_{AB}}(-\omega;\omega)=\sum_{i\neq0}\left[\frac{\mu_{0i}^{A}\mu_{i0}^{B}}{\Delta_{i}-\omega}+\frac{\mu_{0i}^{B}\mu_{i0}^{A}}{\Delta_{i}+\omega}\right]=\hat{P}[A(-\omega),B(\omega)]\sum_{i\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}}{\Delta_{i}-\omega}$$

$$\beta_{A B C}(-\omega_{\sigma};\omega_{1},\omega_{2})=\hat{P}[A(-\omega_{\sigma}),B(\omega_{1}),C(\omega_{2})]\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i j}^{B}\mu_{j0}^{C}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{j}-\omega_{2})}$$

where


$$\beta_{A B C}(-\omega_{\sigma};\omega_{1},\omega_{2})=\hat{P}[A(-\omega_{\sigma}),B(\omega_{1}),C(\omega_{2})]\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i j}^{B}\mu_{j0}^{C}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{j}-\omega_{2})}$$

<!-- formula-ocr: formula_p368_271.png 已替换为LaTeX, 原图保留备查 -->

i

A,B,C... denote one of directions {x,y,z}; ω is energy of external fields, ω=0 corresponds to static electric field; Δi stands for excitation energy of state i with respect to ground state 0. 𝑃̂ is permutation operator, for α and β evidently there are 2!=2 and 3!=6 permutations, respectively. 𝜇𝑖𝑗 𝐴 is A

component of transition dipole moment between state i and j; when i=j the term simply corresponds to electric dipole moment of state i. 𝜇̂ is dipole moment operator, e.g. 𝜇̂ 𝑥≡−𝑥.

The SOS equation for second hyperpolarizability γ is

$$\begin{aligned}\gamma_{ABCD}(-\boldsymbol{\omega}_{\sigma};\boldsymbol{\omega}_{1},\boldsymbol{\omega}_{2},\boldsymbol{\omega}_{3})&=\hat{P}[A(-\boldsymbol{\omega}_{\sigma}),B(\boldsymbol{\omega}_{1}),C(\boldsymbol{\omega}_{2}),D(\boldsymbol{\omega}_{3})](\boldsymbol{\gamma}^{\mathrm{I}}-\boldsymbol{\gamma}^{\mathrm{II}})\\\boldsymbol{\gamma}^{\mathrm{I}}&=\sum_{i\neq0}\sum_{j\neq0}\sum_{k\neq0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{j}-\boldsymbol{\omega}_{2}-\boldsymbol{\omega}_{3})(\Delta_{k}-\boldsymbol{\omega}_{3})}\\\boldsymbol{\gamma}^{\mathrm{II}}&=\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{i}-\boldsymbol{\omega}_{1})(\Delta_{j}-\boldsymbol{\omega}_{3})}\end{aligned}$$

$$\begin{aligned}\gamma_{ABCD}(-\boldsymbol{\omega}_{\sigma};\boldsymbol{\omega}_{1},\boldsymbol{\omega}_{2},\boldsymbol{\omega}_{3})&=\hat{P}[A(-\boldsymbol{\omega}_{\sigma}),B(\boldsymbol{\omega}_{1}),C(\boldsymbol{\omega}_{2}),D(\boldsymbol{\omega}_{3})](\boldsymbol{\gamma}^{\mathrm{I}}-\boldsymbol{\gamma}^{\mathrm{II}})\\\boldsymbol{\gamma}^{\mathrm{I}}&=\sum_{i\neq0}\sum_{j\neq0}\sum_{k\neq0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{j}-\boldsymbol{\omega}_{2}-\boldsymbol{\omega}_{3})(\Delta_{k}-\boldsymbol{\omega}_{3})}\\\boldsymbol{\gamma}^{\mathrm{II}}&=\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{i}-\boldsymbol{\omega}_{1})(\Delta_{j}-\boldsymbol{\omega}_{3})}\end{aligned}$$

$$\begin{aligned}\gamma_{ABCD}(-\boldsymbol{\omega}_{\sigma};\boldsymbol{\omega}_{1},\boldsymbol{\omega}_{2},\boldsymbol{\omega}_{3})&=\hat{P}[A(-\boldsymbol{\omega}_{\sigma}),B(\boldsymbol{\omega}_{1}),C(\boldsymbol{\omega}_{2}),D(\boldsymbol{\omega}_{3})](\boldsymbol{\gamma}^{\mathrm{I}}-\boldsymbol{\gamma}^{\mathrm{II}})\\\boldsymbol{\gamma}^{\mathrm{I}}&=\sum_{i\neq0}\sum_{j\neq0}\sum_{k\neq0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{j}-\boldsymbol{\omega}_{2}-\boldsymbol{\omega}_{3})(\Delta_{k}-\boldsymbol{\omega}_{3})}\\\boldsymbol{\gamma}^{\mathrm{II}}&=\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{i}-\boldsymbol{\omega}_{1})(\Delta_{j}-\boldsymbol{\omega}_{3})}\end{aligned}$$

The SOS equation for third hyperpolarizability δ is


$$\begin{aligned}\gamma_{ABCD}(-\boldsymbol{\omega}_{\sigma};\boldsymbol{\omega}_{1},\boldsymbol{\omega}_{2},\boldsymbol{\omega}_{3})&=\hat{P}[A(-\boldsymbol{\omega}_{\sigma}),B(\boldsymbol{\omega}_{1}),C(\boldsymbol{\omega}_{2}),D(\boldsymbol{\omega}_{3})](\boldsymbol{\gamma}^{\mathrm{I}}-\boldsymbol{\gamma}^{\mathrm{II}})\\\boldsymbol{\gamma}^{\mathrm{I}}&=\sum_{i\neq0}\sum_{j\neq0}\sum_{k\neq0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{j}-\boldsymbol{\omega}_{2}-\boldsymbol{\omega}_{3})(\Delta_{k}-\boldsymbol{\omega}_{3})}\\\boldsymbol{\gamma}^{\mathrm{II}}&=\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{i}-\boldsymbol{\omega}_{1})(\Delta_{j}-\boldsymbol{\omega}_{3})}\end{aligned}$$

<!-- formula-ocr: formula_p368_272.png 已替换为LaTeX, 原图保留备查 -->

$$\begin{aligned}\gamma_{ABCD}(-\boldsymbol{\omega}_{\sigma};\boldsymbol{\omega}_{1},\boldsymbol{\omega}_{2},\boldsymbol{\omega}_{3})&=\hat{P}[A(-\boldsymbol{\omega}_{\sigma}),B(\boldsymbol{\omega}_{1}),C(\boldsymbol{\omega}_{2}),D(\boldsymbol{\omega}_{3})](\boldsymbol{\gamma}^{\mathrm{I}}-\boldsymbol{\gamma}^{\mathrm{II}})\\\boldsymbol{\gamma}^{\mathrm{I}}&=\sum_{i\neq0}\sum_{j\neq0}\sum_{k\neq0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{j}-\boldsymbol{\omega}_{2}-\boldsymbol{\omega}_{3})(\Delta_{k}-\boldsymbol{\omega}_{3})}\\\boldsymbol{\gamma}^{\mathrm{II}}&=\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{i}-\boldsymbol{\omega}_{1})(\Delta_{j}-\boldsymbol{\omega}_{3})}\end{aligned}$$

)0( ≠

$$\begin{aligned}\gamma_{ABCD}(-\boldsymbol{\omega}_{\sigma};\boldsymbol{\omega}_{1},\boldsymbol{\omega}_{2},\boldsymbol{\omega}_{3})&=\hat{P}[A(-\boldsymbol{\omega}_{\sigma}),B(\boldsymbol{\omega}_{1}),C(\boldsymbol{\omega}_{2}),D(\boldsymbol{\omega}_{3})](\boldsymbol{\gamma}^{\mathrm{I}}-\boldsymbol{\gamma}^{\mathrm{II}})\\\boldsymbol{\gamma}^{\mathrm{I}}&=\sum_{i\neq0}\sum_{j\neq0}\sum_{k\neq0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{j}-\boldsymbol{\omega}_{2}-\boldsymbol{\omega}_{3})(\Delta_{k}-\boldsymbol{\omega}_{3})}\\\boldsymbol{\gamma}^{\mathrm{II}}&=\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{i}-\boldsymbol{\omega}_{1})(\Delta_{j}-\boldsymbol{\omega}_{3})}\end{aligned}$$

$$\begin{aligned}\gamma_{ABCD}(-\boldsymbol{\omega}_{\sigma};\boldsymbol{\omega}_{1},\boldsymbol{\omega}_{2},\boldsymbol{\omega}_{3})&=\hat{P}[A(-\boldsymbol{\omega}_{\sigma}),B(\boldsymbol{\omega}_{1}),C(\boldsymbol{\omega}_{2}),D(\boldsymbol{\omega}_{3})](\boldsymbol{\gamma}^{\mathrm{I}}-\boldsymbol{\gamma}^{\mathrm{II}})\\\boldsymbol{\gamma}^{\mathrm{I}}&=\sum_{i\neq0}\sum_{j\neq0}\sum_{k\neq0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\overline{\mu_{jk}^{C}}\mu_{k0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{j}-\boldsymbol{\omega}_{2}-\boldsymbol{\omega}_{3})(\Delta_{k}-\boldsymbol{\omega}_{3})}\\\boldsymbol{\gamma}^{\mathrm{II}}&=\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}\mu_{0j}^{C}\mu_{j0}^{D}}{(\Delta_{i}-\boldsymbol{\omega}_{\sigma})(\Delta_{i}-\boldsymbol{\omega}_{1})(\Delta_{j}-\boldsymbol{\omega}_{3})}\end{aligned}$$

Input file Two kinds of input files could be used:


<!-- p.369 -->

- Plain text file containing excitation energies and transition dipole moments for all involved states. Polarizability, first, second and third hyperpolarizabilities can be calculated in this case. Below format should be satisfied (assume a very simple case, only 2 excited states).


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

You can directly utilize the function introduced in Section 3.21.5 to generate such a plain text file based on output file of electron excitation task of Gaussian or other codes.

If merely polarizability is the quantity of interest, only the content before the line "1 1" is needed to be provided, all other contents can be omitted; in this case, the number of excited states should be written as a negative number (-2 in above case) to tell Multiwfn do not to load them.

- Gaussian output file of common CIS, TDHF, TDDFT or ZINDO task. Since Gaussian does not output all transition dipole moments needed by SOS hyperpolarizability calculation, only polarizability will be calculated by Multiwfn in this case. In order to obtain accurate polarizability, the number of calculated states should be large enough. If nstates keyword is specified to a very large value, e.g. 1000000, then all states will be calculated. #P is suggested to be used, since the excitation energy will then be printed in a higher precision format.

Usage After you enter this function you will see a menu, there are three kinds of functions:

- Options 1~4: Used to calculate α, β, γ and δ at given frequencies, respectively. Users need to input frequency of each external field. The inputted frequencies may be negative. For example, to

compute hyperpolarizability β(-(0.25-0.32);0.25,-0.32), one should input 0.25,-0.32 in option 2. The default unit is a.u., if you prefer to input the frequencies in nm, you should add corresponding suffix, for example, 182.25,-142.385 nm.

Since calculation of γ and especially δ is often time-consuming, in these cases users will be prompted to input the number of states in consideration, smaller number leads to lower cost, but too small number may give rise to poor result.

- Options 5~7: Used to study the variation of α, β and γ with respect to the number of states in consideration. Users need to input frequency of each external field. For α and β, the number of states taken into account ranges from 1 to all states loaded, the stepsize is 1. While for γ, since the computational cost may be quite high, users are allowed to define the ending value and stepsize. The result will be outputted to plain text file in current folder, the meaning of each column is clearly indicated in command-line window.

- Options 15~17: Used to study the variation of the α, β and γ with respect to frequency of external fields. For α, users need to input initial value, ending value and stepsize of external field frequencies. For β and γ, users should write a plain text file, each row corresponds to a pair of frequency (in a.u.) to be calculated. Multiwfn will prompt users to input the path of the file. Below


<!-- p.370 -->

is an example file used to study how γ(-0;0,ω,-ω) varies as ω goes from 0 to 0.2 a.u. with stepsize of 0.02


```text
0.0  0.0  0.0
0.0  0.02  -0.02
0.0  0.04  -0.04
...[ignored]
0.0  0.2  -0.2
```

Since the computational cost for evaluating γ may be quite high, in this case users are allowed to set the number of states into consideration. The result will be outputted to plain text files in current folder, the meaning of each column is clearly indicated in command-line window.

- Option 19: This option is used to scan both ω1 and ω2 of β(-(ω1+ω2);ω1,ω2). You only need to input initial frequency, ending frequency and number of steps for ω1 and ω2. Then after a while, β at different ω1 and ω2 frequencies will be outputted to plain text files in current folder, the meaning of each column is clearly indicated in command-line window. Then you can use third-part software

to plot relief map of "β vs. ω1,ω2".

Multiwfn not only outputs the tensor of (hyper)polarizability, but also outputs many related quantities, such as anisotropy, magnitude and the component along Z axis. The quantities involving

$$\beta_{ABC}(-\omega_{\sigma};\omega_{1},\omega_{2})=\hat{P}[A(-\omega_{\sigma}),B(\omega_{1}),C(\omega_{2})]\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{ij}^{B}\mu_{j0}^{C}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{j}-\omega_{2})}$$

An example is given in Section 4.24.2.1. More discussion and examples about this function can be found in my blog article "Using Multiwfn to calculate polarizability and hyperpolarizability based on sum-over-states (SOS) method" (http://sobereva.com/232, in Chinese)

3.27.2.2 Two-level and three-level model analyses for hyperpolarizability

Theory From the SOS expression of β, it is clear that magnitude of β is completely determined by character of excited states. Clearly it is a useful idea to interpret the nature of difference in β between different systems from excited state point of view. Indeed, this analysis has been prevalently employed in literature, such my works J. Comput. Chem., 38, 1574 (2017) and Phys. Chem. Chem. Phys., 27, 11993 (2025). Let us see how to derive such an analysis model.

Recall the SOS formula for β

$$\beta_{ABC}(-\omega_{\sigma};\omega_{1},\omega_{2})=\hat{P}[A(-\omega_{\sigma}),B(\omega_{1}),C(\omega_{2})]\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{A}\mu_{ij}^{B}\mu_{j0}^{C}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{j}-\omega_{2})}$$

Assume that only the ZZZ component is of our interest and we only focus on static limit case

(ω=0), the equation simplifies to

$$\beta_{ZZZ}^{SOS}=6\sum_{i\neq0}\sum_{j\neq0}\frac{\mu_{0i}^{Z}\overline{\mu_{ij}^{Z}}\mu_{j0}^{Z}}{\Delta_{i}\Delta_{j}}$$

Given that 00AAAijijijμμμδ=− , when i=j, this term corresponds to variation of dipole moment

between excited state i and ground state, namely 00AAAAiiiiiμμμμ=−= Δ; while if i≠j , this term


<!-- p.371 -->

AAijijμμ= corresponds to transition dipole moment between excited state i and j.

With the fact that 𝜇𝑖𝑗 𝐴= 𝜇𝑗𝑖 𝐴, the 𝛽𝑍𝑍𝑍 SOS shown above can be written as sum of contribution of

individual excited states and cross term contribution between various excited states:

$$\beta_{ZZZ}^{\mathrm{sos}}=\sum_{i}6\frac{\left(\mu_{0i}^{Z}\right)^{2}\Delta\mu_{i}^{Z}}{\Delta_{i}^{2}}+\sum_{i}\sum_{j>i}12\frac{\mu_{0i}^{Z}\mu_{0j}^{Z}\mu_{ij}^{Z}}{\Delta_{i}\Delta_{j}}$$

The two-level model is very popular, it assumes that the βZZZ is dominated by ground state and only one excited state:


$$\beta_{ZZZ}^{\mathrm{sos}}=\sum_{i}6\frac{\left(\mu_{0i}^{Z}\right)^{2}\Delta\mu_{i}^{Z}}{\Delta_{i}^{2}}+\sum_{i}\sum_{j>i}12\frac{\mu_{0i}^{Z}\mu_{0j}^{Z}\mu_{ij}^{Z}}{\Delta_{i}\Delta_{j}}$$

<!-- formula-ocr: formula_p371_273.png 已替换为LaTeX, 原图保留备查 -->

The excited state i is usually referred to as crucial state and commonly corresponds to the lowest-lying one with large oscillator strength (strictly speaking, in the present context, the crucial state should refer to the lowest-lying one with large Z component of transition dipole moment, however, the crucial state determined in this way is commonly identical to that determined according to oscillator strength).

Often the two-level model is equivalently expressed in terms of oscillator strength:

$$\beta_{Z Z Z}^{\mathrm{S O S}}=9\Delta\mu_{i}^{Z}f_{i}^{Z}/\Delta_{i}^{3}$$

where 20(2 / 3)()ZZiiifμ=Δ is Z component of oscillator strength. Furthermore, with assumption

that only Z component of transition dipole moment and variation of dipole moment are relatively

prominent, we have SOS3/iiifβμΔΔ . Obviously, now one can easily analyze the source of

difference of β between various systems by comparing the ∆𝜇𝑖 𝑍, fi and Δi terms. Occasionally, there is no well-defined crucial state. For example, both the 1st and 2nd excited states have large 𝜇0𝑖 𝑍, while their energy separation is marginal (nearly degenerate), in this case we should not simply ignore either one, the two excited states should be simultaneously taken into account, I define this model as three-level model:

$$\beta_{ZZZ}^{\mathrm{sos}}=\sum_{i}6\frac{\left(\mu_{0i}^{Z}\right)^{2}\Delta\mu_{i}^{Z}}{\Delta_{i}^{2}}+\sum_{i}\sum_{j>i}12\frac{\mu_{0i}^{Z}\mu_{0j}^{Z}\mu_{ij}^{Z}}{\Delta_{i}\Delta_{j}}$$

Usage In the SOS module (subfunction 2 of main function 24), the suboption 20 is used to carry out the two- and three-level model analyses, all involved terms in the models will be reported so that you can easily compare them among different systems. The input file of this function is completely the same as that used for SOS calculation of first hyperpolarizability, as described in the last section.

After entering this option, if you only input index of one excited state, then two-level model analysis will be carried out, if indices of two excited states are inputted, then three-level model analysis will be performed. If you input a range, e.g. 1-20, then two-level analysis will be performed for each excited state in the range.

An example is given in Section 4.24.2.2.


<!-- p.372 -->


### 3.27.3 Study (hyper)polarizability density

Blog article introducing (hyper)polarizability density is "Using Multiwfn to calculate (hyper)polarizability density" (http://sobereva.com/305, in Chinese).

(Hyper)polarizability density can be very easily plotted by Multiwfn as plane map and isosurface map. This quantity is quite useful in discussing nature of (hyper)polarizability of a given molecule. If this feature is used in your work, citing my paper J. Comput. Chem., 38, 1574 (2017) is recommended, in which the (hyper)polarizability density analysis is involved and brief introduction is given. My other publications also present illustrative applications of this method: Carbon, 165, 461 (2020), J. Phys. Chem. C, 124, 7353 (2020), J. Phys. Chem. A, 124, 5563 (2020), J. Phys. Chem. C, 124, 845 (2020).

Theory of (hyper)polarizability density and spatial contribution to (hyper)polarizability There is a well-known Taylor expansion for (electric) dipole moment


$$\mathbf{\mu}(\mathbf{F})=-\frac{\partial E}{\partial\mathbf{F}}=\mathbf{\mu}_{0}+\mathbf{\alpha}\mathbf{F}+(1/2)\mathbf{\beta}\mathbf{F}^{2}+(1/6)\mathbf{\gamma}\mathbf{F}^{3}+\ldots$$

<!-- formula-ocr: formula_p372_274.png 已替换为LaTeX, 原图保留备查 -->

where F is external electric field vector, E is system total energy, μ and μ0 are current electric dipole moment and permanent dipole moment, respectively. α, β and γ are polarizability, the first and second hyperpolarizability tensors, respectively.

Similarly, Taylor expansion with respect to F can be applied to electron density


$$\boldsymbol{\mu}(\mathbf{F}) = \int -\rho(\mathbf{r}, \mathbf{F}) \mathbf{r} \, \mathrm{d} \mathbf{r}$$

<!-- formula-ocr: formula_p372_275.png 已替换为LaTeX, 原图保留备查 -->

$$\mathbf{\mu}_{0}=-\frac{\partial E}{\partial\mathbf{F}}\bigg|_{\mathbf{F}=0}\quad\mathbf{a}=-\frac{\partial^{2}E}{\partial\mathbf{F}^{2}}\bigg|_{\mathbf{F}=0}\quad\mathbf{\beta}=-\frac{\partial^{3}E}{\partial\mathbf{F}^{3}}\bigg|_{\mathbf{F}=0}\quad\mathbf{\gamma}=-\frac{\partial^{4}E}{\partial\mathbf{F}^{4}}\bigg|_{\mathbf{F}=0}$$


$$\mathbf{\boldsymbol{\beta}}=\int-\mathbf{\boldsymbol{\rho}}^{(2)}(\mathbf{r})\mathbf{r}\mathrm{d}\mathbf{r}\qquad\boldsymbol{\gamma}=\int-\mathbf{\boldsymbol{\rho}}^{(3)}(\mathbf{r})\mathbf{r}\mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p372_276.png 已替换为LaTeX, 原图保留备查 -->

where ρ(1) is known as polarizability density, while ρ(2) and ρ(3) are known as the first and second hyperpolarizability densities, respectively. Using (hyper)polarizability densities, we can easily investigate contribution of various spatial regions to total molecular (hyper)polarizabilities.

The second hyperpolarizability density ρ(3) is a third-order tensor function, it can be explicitly represented as


$$\rho_{ijk}^{(3)}(\mathbf{r})=\frac{\partial^{3}\rho(\mathbf{r})}{\partial F_{i}\partial F_{j}\partial F_{k}}\bigg|_{\mathbf{F}=0}$$

<!-- formula-ocr: formula_p372_277.png 已替换为LaTeX, 原图保留备查 -->

It is impossible to discuss all of its components, since there are as many as 3×3×3=27 components. Assume that the γZZZZ is the most crucial component of γ, we can simply study ρZZZ(r):


<!-- p.373 -->


$$\rho_{zzz}^{(3)}(\mathbf{r})=\frac{\partial^{3}\rho(\mathbf{r})}{\partial F_{z}^{3}}\bigg|_{F_{z}=0}$$

<!-- formula-ocr: formula_p373_278.png 已替换为LaTeX, 原图保留备查 -->

which relates to γZZZZ via

(3)(𝐫) is the contribution of point r to the γZZZZ. If it is plotted as isosurface map or plane map, the source of γZZZZ can be intuitively revealed. However, the disadvantage of −𝑧𝜌𝑧𝑧𝑧 Clearly, −𝑧𝜌𝑧𝑧𝑧 (3)(𝐫) is that it depends on the choice origin, which is somewhat arbitrary, therefore 𝜌𝑧𝑧𝑧 (3) has its own value to study as it is independent of origin.

(3) is using finite difference method (see my article http://sobereva.com/305 on how to derive it) The easiest way of obtaining the 𝜌𝑧𝑧𝑧

FFFF−−−+−=ρρρρρ zzzF 3)3( )2()(2)(2)2( zzzz )(2 z

where Fz is strength of the external electric field applied along Z axis. The functions such as ρ(Fz) and ρ(-Fz) denote the electron density distribution yielded when Fz is applied along positive and negative directions of Z-axis, respectively. The Fz in this case corresponds to finite difference step size, it should not be too large or too small, otherwise numerical error will be significant. According to my experience, 0.003 a.u. is a good choice of Fz.

Similarly, one can easily derive the equation for polarizability density


$$\gamma_{z z z z}=\int-z\rho_{z z z}^{(3)}(\mathbf{r})\mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p373_279.png 已替换为LaTeX, 原图保留备查 -->

and that for first hyperpolarizability density

Use Multiwfn to study (hyper)polarizability density Via subfunction 3 of main function 24, one can very conveniently plot plane map and isosurface map of any kind of (hyper)polarizability density as well as spatial contribution to (hyper)polarizability. Once grid data of the latter is generated by Multiwfn and exported to .cub file, one can further evaluate atom or fragment contribution to (hyper)polarizability, as shown in the example in Section 4.24.3.

This function is used via the following steps (1) Boot up Multiwfn and load a file containing atom information of the studied system, such as .xyz, .pdb, .mwfn, .fch and so on, see Section 2.5.

(2) Enter subfunction 3 of main function 24. (3) Choose the quantity you hope to study (4) Choose the direction of interest (X or Y or Z) Assume that you chose “second hyperpolarizability density and spatial contribution to second

hyperpolarizability” in step (3) and choose “Z” in step (4), then you can study −𝑧𝜌𝑧𝑧𝑧 (3) and 𝜌𝑧𝑧𝑧 (3) later.


<!-- p.374 -->

(5) Choose option 1 to generate Gaussian input files of single point calculations under different external electric fields. You can manually modify the default keywords in these files. By default, the calculations are conducted at PBE0/aug-cc-pVTZ level.

(6) Run the .gjf files by Gaussian manually, then .wfx files will be generated (7) Choose option 2 to load the .wfx files (8) Now you can choose what you want to do. If you choose to calculate grid data of (hyper)polarizability or spatial contribution to (hyper)polarizability, then you can directly visualize their isosurface map or export grid data as .cub file. Also, you can choose to plot plane maps of these functions.

About molecular orientation It is important to note that in practice, what we are actually interested in is often the component along the direction of molecular dipole moment, which is often not parallel to any Cartesian axis. In this case, before using the present function, you should reorientate the system so that the dipole moment is exactly parallel to a Cartesian axis, such as Z. Multiwfn can easily realize the reorientation via the function described in Section 3.300.7. Namely you should load wavefunction file of the present system after booting up Multiwfn, and then input

300 //Other function (Part 3) 7 //Geometry operation on the present system 7 //Make electric dipole moment parallel to a vector or Cartesian axis 3 //Parallel to Z axis -1 //Output system to .xyz file Then you can use the exported .xyz file as input file for studying (hyper)polarizability density. See Section 4.24.3 for example of studying (hyper)polarizability density and spatial contribution to (hyper)polarizability.


### 3.27.5 Visualize (hyper)polarizability via unit sphere and vector representations



If you are not familiar with (hyper)polarizability, please check Section 3.27.1 first to gain basic knowledge. In this section, the unit sphere representation will be introduced, it was proposed in J. Comput. Chem., 32,1128 (2011) to intuitively represent first-order hyperpolarizability tensor, while I also extended this idea to polarizability and second-order hyperpolarizability.

Theory Recall the relationship between molecular dipole moment and external field

$$\mathbf{p}=\mathbf{p}_{0}+\mathbf{a}\cdot\mathbf{F}+(1/2)\mathbf{β}\cdot\mathbf{F}\cdot\mathbf{F}+(1/6)\mathbf{\gamma}\cdot\mathbf{F}\cdot\mathbf{F}\cdot\mathbf{F}+\ldots$$

The β is known as first order hyperpolarizability tensor, the component βABC is proportional to the magnitude of induced dipole moment in direction A caused by combination of two incident electric fields respectively in directions B and C.

In the unit sphere representation, effective dipole vector is defined as

$$\boldsymbol{\beta}^{\mathrm{e f f}}(\theta,\phi)=\boldsymbol{\beta}\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)$$


<!-- p.375 -->

where θ and φ are angles of spherical polar coordinate, e(θ,φ) is unit vector normal to the sphere surface. More specifically, the components of βeff can be explicitly written as


$$\boldsymbol{\beta}_{i}^{\mathrm{e f f}}=\sum_{j}\sum_{k}\beta_{i,j,k}\boldsymbol{e}_{k}\boldsymbol{e}_{j}\quad i,j,k=\{\boldsymbol{x},\boldsymbol{y},\boldsymbol{z}\}$$

<!-- formula-ocr: formula_p375_280.png 已替换为LaTeX, 原图保留备查 -->

The orientation and length of βeff(θ,φ) vector respectively reflect the direction and magnitude of induced dipole moment caused by combination of two incident electric fields exerted in the

direction of (θ,φ). If βeff is calculated at every vertex of a sphere surface enclosing the molecule, one can clearly and vividly understand the response of molecular dipole moment with respect to external electric field exerted in various directions. The original paper only employs this representation to

second harmonic generation (SHG) type of β, in fact it can also be applied to other kinds of β, including both static and dynamic ones (in the latter case, the exerted external field with varying strength comes from incident electromagnetic wave, and its direction is perpendicular to the propagation direction of the electromagnetic wave).

Based on the same idea of βeff, I defined below quantities

$$\boldsymbol{\alpha}^{\mathrm{eff}}(\theta,\phi)$$

$$\begin{aligned}\mathbf{a}^{\mathrm{eff}}(\theta,\phi)&=\mathbf{a}\cdot\mathbf{e}(\theta,\phi)\\\boldsymbol{\gamma}^{\mathrm{eff}}(\theta,\phi)&=\boldsymbol{\gamma}\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\end{aligned}$$

$$\begin{aligned}\mathbf{a}^{\mathrm{eff}}(\theta,\phi)&=\mathbf{a}\cdot\mathbf{e}(\theta,\phi)\\\boldsymbol{\gamma}^{\mathrm{eff}}(\theta,\phi)&=\boldsymbol{\gamma}\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\end{aligned}$$

$$\begin{aligned}\mathbf{a}^{\mathrm{eff}}(\theta,\phi)&=\mathbf{a}\cdot\mathbf{e}(\theta,\phi)\\\boldsymbol{\gamma}^{\mathrm{eff}}(\theta,\phi)&=\boldsymbol{\gamma}\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\end{aligned}$$

The so-called vector representation of β corresponds to plotting (βx, βy, βz) vector as an arrow, the components are defined as


$$\beta_{i}=(1/3)\sum_{j}(\beta_{i j j}+\beta_{j j i}+\beta_{j i j})\quad i,j=\left\{x,y,z\right\}$$

<!-- formula-ocr: formula_p375_281.png 已替换为LaTeX, 原图保留备查 -->

$$\begin{aligned}\mathbf{a}^{\mathrm{eff}}(\theta,\phi)&=\mathbf{a}\cdot\mathbf{e}(\theta,\phi)\\\boldsymbol{\gamma}^{\mathrm{eff}}(\theta,\phi)&=\boldsymbol{\gamma}\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\end{aligned}$$

I also proposed vector representation for α, the situation is very different to the vector representation of β. Double sided arrows are drawn along X, Y and Z axes, and their lengths respectively represent magnitude of α in the corresponding directions, which are defined as


$$(\gamma_{x},\gamma_{y},\gamma_{z})$$

<!-- formula-ocr: formula_p375_282.png 已替换为LaTeX, 原图保留备查 -->

Similarly, vector representation for γ corresponds to drawing double sided arrows along X, Y and Z axes, and their lengths respectively represent magnitude of γ in the corresponding directions (γx, γy, γz), which are calculated as


$$\gamma_{i}=(1/15)\sum_{j}(\gamma_{ijji}+\gamma_{ijij}+\gamma_{iijj})\quad i,j=\left\{x,y,z\right\}$$

<!-- formula-ocr: formula_p375_283.png 已替换为LaTeX, 原图保留备查 -->


<!-- p.376 -->

Usage

Multiwfn is able to perform unit sphere representation analysis for α, β and γ, namely generating plotting script of VMD software (http://www.ks.uiuc.edu/Research/vmd/) based on loaded (hyper)polarizability tensor. In addition, plotting script corresponding to vector

representation can also be generated for β.

After booting up Multiwfn, you should load a file containing atom information for the molecule under study. For example, .xyz, .pdb and .fch can be used, see Section 2.5. The atom information will be used to determine proper radius of the sphere involved in the unit sphere representation.

After entering present module (subfunction 5 of main function 24), you can use many options to adjust parameters of unit sphere and vector representations, such as scale factor of arrow length, radius of arrow and so on, they are fully self-explanatory. By choosing options 1 or 2 or 3, Multiwfn

will respectively load α or β or γ tensor from a specific file (see below), then VMD plotting script corresponding to unit sphere representation will be generated in current folder (alpha.tcl, beta.tcl and gamma.tcl, respectively), and those corresponding to vector representation will also be generated (alpha_vec.tcl, beta_vec.tcl and gamma_vec.tcl). Then, using VMD to run the scripts, the corresponding graph will be immediately obtained.

It is worth mentioning that there is an option "-8 Toggle making longest arrow on sphere has specific length". If you select it once to switch its status to "Yes", then after selecting option 1 or 2 or 3, you will be asked to input the expected length of longest arrow on the sphere. Via this option, you can make map plotted by VMD for systems that have very different magnitude of (hyper)polarizability easily comparable.

Preparation of the file containing (hyper)polarizability tensor

The file containing α or β or γ tensor can be directly generated by subfunction 1 of main function 24 by extracting corresponding data from output file of "polar" task of Gaussian. In that function, you should choose option "-4 Export (hyper)polarizability as .txt file after parsing" once

to switch its status to "Yes", then after parsing data via corresponding option, α will be exported to alpha.txt, β will be exported to beta.txt, and γ will be exported to gamma.txt in current folder, they are what you need in the present function.

The files containing (hyper)polarizability can also be manually prepared, in this case the data can be generated by quantum chemistry codes other than Gaussian. The format of the file is free, the sequence of the tensor components is shown as follows (represented in Fortran grammar)

- Polarizability: ((α(i,j),j=1,3),i=1,3)
- First-order hyperpolarizability: (((β(i,j,k),k=1,3),j=1,3),i=1,3)
- Second-order hyperpolarizability: ((((γ(i,j,k,l),l=1,3),k=1,3),j=1,3),i=1,3) where the cycle of index i is the slowest. For example, below is a file recording α tensor (highlighted texts are comments):


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
