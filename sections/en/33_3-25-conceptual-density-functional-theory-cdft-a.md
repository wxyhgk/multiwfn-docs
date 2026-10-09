# 3.25 Conceptual density functional theory (CDFT) analysis (22)

> Multiwfn manual, p.341–353. Images: `../imgs/`.

---

<!-- p.341 -->

Examples of this analysis are given in Section 4.21.4.


## 3.25 Conceptual density functional theory (CDFT) analysis (22)



The conceptual density functional theory (CDFT) originally developed by Robert Parr and extended by numerous researchers is a theory framework aiming for unraveling reactivity of chemical systems. CDFT contains numerous concepts and quantities, some of them can be used to predict favorable reactive sites and reactive character, and some of them can compare reactivity among different chemical species. Due to the high popularity and important role of CDFT in quantum chemistry, as well as there are so many meaningful relevant quantities, I believe it is very useful to develop a module to calculate all commonly employed quantities involved in CDFT with minimal steps.

In Part 1 of this section, I will briefly describe the definition of all quantities that can be studied via this module; then in Part 2, I will show how to use this module. This module is able to calculate the so-called orbital-weighted quantities, which will be specifically described in Part 3.

Note that aside from CDFT, Multiwfn also supports many other methods for revealing reactive sites, see Section 4.A.4 for overview.

If the functions described in this section are used in your research, please NOT ONLY cite original papers of Multiwfn, BUT ALSO cite the following book chapter, which comprehensively introduces feature and implementation of this module:

Tian Lu, Qinxue Chen, Realization of Conceptual Density Functional Theory and Information-Theoretic Approach in Multiwfn Program. In Conceptual Density Functional Theory, WILEY-VCH GmbH: Weinheim (2022); pp 631-647. DOI: 10.1002/9783527829941.ch31


### 3.25.1 Theory

To yield all below quantities, electronic energy (E) and electron density of N, N+1 and N-1 electronic states must be available. Commonly N refers to the number of electrons carried by a chemical system at its most stable status. Geometry optimized for N-electrons state is employed for all calculations.

➢ Global indices

- First vertical ionization potential (I1): E(N-1) − E(N)
- First vertical electron affinity (A): E(N) − E(N+1)
- Mulliken electronegativity (χ): (I1+A)/2
- Chemical potential (μ): −χ
- Hardness (η): I1−A, which is also equivalent to fundamental gap. See J. Am. Chem. Soc., 105, 7512 (1983). Note that according to the convention employed by many CDFT papers, the prefix of

1/2 in original definition of η is dropped.


<!-- p.342 -->

- Softness (S): 1/η. See Proc. Nati. Acad. Sci., 82, 6723 (1985)
- Electrophilicity index (ω): μ2/(2η). See J. Am. Chem. Soc., 121, 1922 (1999)
- Nucleophilicity index (NNu): EHOMO(Nu) − EHOMO(TCE), where Nu denotes nucleophile, TCE denotes tetracyanoethylene, whose HOMO energy is almost the lowest one among all organic molecules and therefore it is chosen as reference system. See J. Org. Chem., 73, 4615 (2008).

➢ Real space functions

- Fukui function f(r) and dual descriptor Δf(r): See Section 4.5.4 for detailed introduction
- Local softness: s+(r) = Sf +(r), s−(r) = Sf −(r), s0(r) = Sf 0(r) for nucleophilic, electrophilic, radical attacks, respectively, where f(r) is Fukui function of corresponding type. See Proc. Nati. Acad. Sci., 82, 6723 (1985)

- Local hyper-softness: s(2) ≈ S2Δf(r), see J. Math. Chem., 62, 461 (2024)
- Local electrophilicity index: 𝜔loc(𝐫) = 𝜔𝑓+(𝐫)

- Local nucleophilicity index: 𝑁Nu loc(𝐫) = 𝑁Nu𝑓−(𝐫) ➢ Atom indices

- Condensed Fukui function (fA) and dual descriptor (ΔfA): See Section 4.7.3 for detailed introduction

- Condensed local softness For nucleophilic attack: 𝑠𝐴 + For electrophilic attack: 𝑠𝐴 − For radical attack attack: 𝑠𝐴 0
- Relative electrophilicity index: 𝑠𝐴 −, see J. Phys. Chem. A, 102, 3746 (1998)
- Relative nucleophilicity index: 𝑠𝐴 +, see J. Phys. Chem. A, 102, 3746 (1998)
- Condensed local electrophilicity index: 𝜔𝐴= 𝜔𝑓𝐴 + = 𝑆𝑓𝐴 −= 𝑆𝑓𝐴 0 = 𝑆𝑓𝐴 −/𝑠𝐴 +/𝑠𝐴 +

(2) ≈𝑆2∆𝑓𝐴 ➢ Bond dual descriptor (BDD) BDD is an index defined for each bond, negative (positive) BDD implies the bond is nucleophilic (electrophilic), and the more negative (positive), the stronger the nucleophilicity (electrophilicity)
- Condensed local nucleophilicity index: 𝑁Nu −
- Condensed local hyper-softness: 𝑠𝐴 𝐴= 𝑁Nu𝑓𝐴

BDD essentially is the first derivative of bond order (P) with respect to number of electrons under constant external potential. According to J. Math. Chem., 63, 1588 (2025), using finite-difference approximation, BDD for bond A-B can be calculated as 𝐵𝐷𝐷𝐴,𝐵= 𝑓𝐴,𝐵 + and 𝑓𝐴,𝐵 − are two types of bond Fukui function and evaluated as follows + −𝑓𝐴,𝐵 −, where 𝑓𝐴,𝐵


$$f_{A,B}^{+}=P_{A,B}(N+1)-P_{A,B}(N)$$

<!-- formula-ocr: formula_p342_231.png 已替换为LaTeX, 原图保留备查 -->

In J. Math. Chem., 63, 1588 (2025) the author employed Wiberg bond order based on atomic natural orbitals as P, but in the current implementation of Multiwfn, fuzzy bond order based on Hirshfeld partition (see Section 3.11.6 for details) is used as P for evaluating BDD, because this bond order is insensitive to basis set (much better than Mayer bond order in this regards), works reasonably (according to my test), and relatively easy to realize.


<!-- p.343 -->

➢ ωcubic electrophilicity index The electrophilicity index ωcubic introduced in J. Phys. Chem. A, 124, 2090 (2020) is somewhat special, it also relies on N-2 electronic states. It includes higher-order terms than the aforementioned

electrophilicity index ω. Its definition is


$$\omega_{cubic}=\omega\left(1+\frac{\mu}{3\eta^{2}}\gamma\right)$$

<!-- formula-ocr: formula_p343_232.png 已替换为LaTeX, 原图保留备查 -->

In practice, it is calculated as

$$\omega_{cubic}=\frac{\left(\mu_{cubic}\right)^{2}}{2\eta_{cubic}}\left[1+\frac{\mu_{cubic}}{3\left(\eta_{cubic}\right)^{2}}\gamma_{cubic}\right]$$

where

$$\mu_{cubic}=(1/6)(-2A-5I_{1}+I_{2})$$

$$\eta_{cubic}=I_{1}-A$$

$$\gamma_{cubic}=2I_{1}-I_{2}-A$$

where I2 is the second vertical ionization potential and defined as E(N-2) − E(N-1). Correspondingly, there is a cubic form of condensed local electrophilicity index 𝜔cubic +. In J. Phys. Chem. A, 124, 2090 (2020) is shown that 𝜔cubic 𝐴 value of halogen atom (which behaves as Lewis acid due to its σ-hole) in halogen-bond dimers R-X···NH3 has excellent correlation with calculated binding energies (however, note that they employed AIM partition for atomic spaces rather than the Hirshfeld partition utilized in the present module). 𝐴= 𝜔cubic𝑓𝐴

➢ Electrophilic descriptor (ε) The electrophilic descriptor (ε) was introduced in Int. J. Quantum Chem., 124, e27366 (2024), it was shown to correlate with Mayr’s electrophilic parameter (E) significantly better than the

electrophilicity index (ω) using a test set consisting of 35 organic molecules. In contrast to ω, whose derivation is only based on second-order Taylor expansion of system energy, derivation of ε is based on third-order expansion, which makes ε explicitly involve hyperhardness. Like ωcubic, calculation of ε also relies on N-2 electronic state.

The working equation for computing ε is as follows


$$\varepsilon=\chi\left(\frac{\phi}{\gamma}\right)-\left(\frac{\phi}{\gamma}\right)^{2}\left(\frac{\eta}{2}+\frac{\phi}{6}\right)$$

with

$$\phi=\sqrt{\eta^{2}-2\gamma\mu}-\eta$$

It is important to note that the η, γ, χ, μ involved in above equations should be calculated in a different way than those described earlier, namely


$$\begin{aligned}&\mu=a\\&\chi=-a\\&\eta=2(b-ac)\\&\gamma=-3c(b-ac)\\ \end{aligned}$$

<!-- formula-ocr: formula_p343_234.png 已替换为LaTeX, 原图保留备查 -->


<!-- p.344 -->

where


$$b=\frac{I_{1}-A^{\prime}}{2}-\frac{I_{1}+A^{\prime}}{2}c$$

<!-- formula-ocr: formula_p344_235.png 已替换为LaTeX, 原图保留备查 -->

with A’ = E(N+1) − E(N), which is electron affinity but differs with standard definition by the sign.

➢ Fukui potential and dual descriptor potential Definition and physical meaning of Fukui potential were carefully discussed in J. Phys. Chem. A, 115, 2325 (2011) and Int. J. Quantum Chem., 101, 520 (2005). Fukui potential is complementary to ESP in understanding energy variation in the early stage of chemical reaction when electron transfer is nonnegligible. For example, when an electrophile is attacked by a nucleophile, the external potential generated by the nucleophile felt by the electrophile is

𝑣𝑁−phile(𝐫) ≈𝑉𝑁−phile ESP(𝐫) −∆𝑁∫ 𝑓𝑁−phile −(𝐫′) |𝐫−𝐫′|d𝐫′

where ΔN is number of transferred electrons from the electrophile to nucleophile (negative value in this case), 𝑓𝑁−phile − is Fukui function f− of the nucleophile. Three kinds of Fukui potential are defined

as follows


$$v_{N-\mathrm{p h i l e}}(\mathbf{r})\approx V_{N-\mathrm{p h i l e}}^{\mathrm{E S P}}(\mathbf{r})-\Delta N\int\frac{f_{N-\mathrm{p h i l e}}^{-}(\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime}$$

<!-- formula-ocr: formula_p344_236.png 已替换为LaTeX, 原图保留备查 -->

ESP is only able to predict regioselectivity dominated by electrostatics effect with assumption that there is no electron transfer, however, evidently this assumption is far from true for general chemical reactions (but basically true for many noncovalent interactions). Clearly, Fukui potential should be more focused on in studying general reactions, especially for those with significant electron transfer.

Fukui potential is more rigorous than Fukui function in predicting regioselectivity, as emphasized in J. Phys. Chem. A, 115, 2325 (2011) that “It is the value of the Fukui potential, more than the value of the Fukui function itself, that determines the reactive site”. However, Fukui potential is not so popular as Fukui function, because their distribution characteristics usually coincide with each other, while evaluation of Fukui potential needs calculating ESP twice, which is considerably more expensive than evaluating electron density twice. According to finite difference definition of Fukui function, for example, 𝑉𝑓− can be evaluated as


$$V_{f^{-}}(\mathbf{r})=\int\frac{f^{-}(\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime}=\int\frac{\rho_{N}(\mathbf{r}^{\prime})-\rho_{N-1}(\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime}=V_{N-1}^{\mathrm{ESP}}(\mathbf{r})-V_{N}^{\mathrm{ESP}}(\mathbf{r})$$

<!-- formula-ocr: formula_p344_237.png 已替换为LaTeX, 原图保留备查 -->

Furthermore, dual descriptor potential (DDP) was introduced in J. Math. Chem., 62, 1094 (2024), which is defined as


$$D D P(\mathbf{r})=\int\frac{\Delta f(\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime}=\int\frac{f^{+}(\mathbf{r}^{\prime})-f^{-}(\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}^{\prime}=V_{f^{+}}(\mathbf{r})-V_{f^{-}}(\mathbf{r})$$

<!-- formula-ocr: formula_p344_238.png 已替换为LaTeX, 原图保留备查 -->

Unlike dual descriptor, which often has many nodal planes hindering discussion, distribution of DDP is much smoother, enabling researchers to identify preferential reactive sites easier.

Like the Fukui function, the more positive the 𝑉𝑓+ is in a region, the more likely it is for


<!-- p.345 -->

nucleophilic reaction to occur, and the region where the 𝑉𝑓− is more positive, the more likely it is

for electrophilic reaction to occur. Similar to dual descriptor, the more positive and negative the DPP is in a region, the more likely this region is susceptible to undergo nucleophilic and electrophilic attacks, respectively.


### 3.25.2 Usage

For using the present module, namely main function 22, the file loaded after booting up Multiwfn is relatively arbitrary, the only requirement is that the atomic information in this file is identical to the system under study.

After entering the present module, you will see a menu, in which options 2, 3 and 9 are used to calculate above quantities. Before using them, generally you should provide N.wfn, N-1.wfn and N+1.wfn in current folder, which contain wavefunction and electronic energy of N, N-1 and N+1 states respectively for present system, the geometries must be the same and correspond to the optimized geometry of N state. The calculation level of the three files must also be the same. If any of the three .wfn files is missing, Multiwfn will ask you to manually input path of .wfn file for corresponding state (.wfx, .fch and .mwfn files are also allowed, since they also carry wavefunction and electronic energy information).

Option 2: Used to calculate all aforementioned global indices and atomic indices, the result will be exported to CDFT.txt in current folder. Because as mentioned in Section 4.7.3, Hirshfeld method is an ideal choice for calculating condensed Fukui functions and may be other relevant atomic indices, therefore Hirshfeld charges are automatically calculated and used for evaluation of all atomic indices. Nucleophilicity index as well as its local version are dependent of HOMO energy of TCE, which should be calculated using the same level for present system, notice that these indices printed in present module simply employ the EHOMO(TCE) = -0.335198 Hartree calculated at the commonly used B3LYP/6-31G* level (clearly, if you want to get more reliable result and your current calculation level is not B3LYP/6-31G*, you should calculate EHOMO(TCE) yourself and then manually evaluate these indices).

Option 3: Used to calculate grid data of Fukui function, dual descriptor and functions related to them, then their isosurface maps can be directly visualized, the grid data can be exported to cube files in current folder. In this option you can set the scale factor to be multiplied to the calculated grid data. For example, if you set the scale factor to the global softness outputted by option 2, then

the scaled f −(r) Fukui function will correspond to s−(r).

Option 9: Similar to option 3, but used to calculate grid data of Fukui potential and dual descriptor potential. Because grid data of ESP needs to be calculated for each charged state, which is often expensive, you should choose a proper grid setting to avoid being too time consuming.

Option 10: Used to calculate bond dual descriptor. Multiwfn will load .wfn file of different electronic states and calculate fuzzy bond orders in turn, and finally evaluate and print BDD values. The cost is generally low.

Generation of .wfn files You can manually prepare the .wfn files used by options 2 and 3, alternatively, you can use option 1 of present module to automatically realize the preparation work.

After choosing option 1, you will be prompted to input Gaussian keywords for single point


<!-- p.346 -->

task, then Multiwfn asks you to input charge and spin multiplicity for N, N+1 and N-1 states in turn, then Gaussian single point input files N.gjf, N+1.gjf and N-1.gjf will be generated in current folder (the geometry in these files correspond to the geometry in the input file of Multiwfn). Then, you can manually use Gaussian to run them to obtain N.wfn, N+1.wfn and N-1.wfn, or if Gaussian has been installed on your computer, you can directly let Multiwfn to invoke Gaussian to calculate them (in this case the "gaupath" parameter in `settings.ini` must have been set to actual path of Gaussian executable file), after calculations the three .wfn files will appear in current folder.

Sometimes we need to use mixed basis set, in this case you should prepare a file named basis.txt in current folder, which records the definition of basis set (may be also accompanied by pseudopotential definition). If the inputted keyword contains "gen" or "genecp", then the content of basis.txt will be automatically appended to the end of the generated .gjf files.

Multiwfn is also able to generate input files of ORCA for producing the three .wfn files. You should choose option -2 and select ORCA, then choosing option 1 will generate N.inp, N-1.inp and N+1.inp. If you have set “orcapath” in `settings.ini` to actual path of ORCA executable file, you can directly let Multiwfn to invoke ORCA to run them to yield N.wfn, N-1.wfn and N+1.wfn; alternatively, you can run them by ORCA manually, and then put the resulting N.wfn, N-1.wfn and N+1.wfn in current folder.

To use present module to study large organic systems, commonly I suggest using B3LYP/6-31G* level, because this level is inexpensive, while the quality of the yielded quantities is already satisfactory.

Note on calculating ωcubic and ε By default, Multiwfn does not calculate ωcubic and ε, because they rely on N-2 electronic state. If you need them, you should first select option -1 to switch the status to "Yes". Then you can use option 1 to help you to prepare .wfn file for N, N+1, N-1, N-2 electronic states, or you manually provide them. Then after selecting option 2, the resulting CDFT.txt file will contain condensed local

ωcubic, global ωcubic, ε, as well as I2.

An example of using present module to calculate various CDFT quantities for phenol is provided in Section 4.22.1. Example of calculating Fukui potential and dual descriptor potential for maleic anhydride is given in Section 4.22.4. Examples of calculating bond dual descriptor are given in Section 4.22.5.


### 3.25.3 Special topic 1: Orbital-weighted Fukui function and dual descriptor



Theory The originally defined Fukui function and dual descriptor do not work well when frontier molecular orbitals are (quasi-)degenerate. For example, when HOMO and HOMO-1 have very

similar or exactly identical energies, the Fukui function f − may be unable to give meaningful result or the result is fully misleading; in addition, when the system shows point group symmetry, such as

C60 fullerene, the distribution of f − is usually not in consistency with molecular symmetry, this is an apparently unexpected observation.

In order to address these problems, in J. Comput. Chem., 38, 481 (2017), the authors proposed


<!-- p.347 -->

orbital-weighted Fukui function, and in J. Phys. Chem. A, 123, 10556 (2019), they further proposed orbital-weighted dual descriptor, they are summarized below (the 𝑓𝑤0 is defined by me)

$$\begin{array}{r l r l}&{f_{w}^{+}(\mathbf{r})=\displaystyle\sum_{i=\mathrm{L U M O}}^{\infty}w_{i}\mid\varphi_{i}(\mathbf{r})\mid^{2}}&{}&{w_{i}=\frac{\exp[-\left(\frac{\mu-\varepsilon_{i}}{\Delta}\right)^{2}]}{\displaystyle\sum_{i=\mathrm{L U M O}}^{\infty}\exp[-\left(\frac{\mu-\varepsilon_{i}}{\Delta}\right)^{2}]}}\end{array}$$

$$\begin{array}{r l}{f_{w}^{-}(\mathbf{r})=\displaystyle\sum_{i}^{\mathrm{H O M O}}w_{i}\mid\varphi_{i}(\mathbf{r})\mid^{2}}&{{}\quad w_{i}=\frac{\exp[-\left(\frac{\mu-\varepsilon_{i}}{\Delta}\right)^{2}]}{\displaystyle\sum_{i}^{\mathrm{H O M O}}\exp[-\left(\frac{\mu-\varepsilon_{i}}{\Delta}\right)^{2}]}}\end{array}$$

i

fff www 0 ( )[( )( )]/ 2 rrr =+ +−

Δ=− fff www ( )( )( ) rrr +−

where εi and φi are energy and wavefunction of orbital i; μ is chemical potential and approximately calculated as (EHOMO+ELUMO)/2 in the above formulae. The Δ is an adjustable parameter, in principle its best value is the one able to make the functions have ideal predictability of local reactivity.

Clearly the most appropriate Δ is dependent on practical system, usually 0.1 Hartree is a worth-trying guess. If you find the orbital-weighted functions under this value do not work well, you can try to properly change it and redo calculations.

Compared to the frozen orbital approximation form of f −, namely f −(r)=|φHOMO(r)|2, the advantage of 𝑓𝑤− is that it takes all orbitals into account with different weights. From the expression it can be seen that the closer a low-lying orbital energy is to the HOMO energy, the greater its weight. Evidently degenerate orbitals share the same weight. The Gaussian function involved in the formula

behaves as a decay function, the larger the Δ, the higher the contribution of low-lying orbitals to the 𝑓𝑤−. When energy difference between HOMO and HOMO-1 is significant, there will be no reason

to use 𝑓𝑤− instead of f −. The situation is similar for 𝑓𝑤+, 𝑓𝑤0 and ∆𝑓𝑤.

Usage Since orbital-weighted functions involve virtual orbitals, you should use .mwfn, .fch, .molden or .gms file as input file. Commonly, the geometry in the input file should correspond to the optimized geometry of N-electronic state; however, it is also possible to study them for nonequilibrium structure, such as a point in intrinsic reaction coordinate (IRC).

Only closed-shell single-determinant wavefunction is acceptable. Diffuse functions should not be used if you intend to calculate 𝑓𝑤+, 𝑓𝑤0and ∆𝑓𝑤, since they utilize virtural orbitals, whose chemical meaning may be severely broken when diffuse functions are employed.

In main function 22, four options are related to the orbital-weighted calculation:

- Option 4: Set the Δ parameter used in the subsequent orbital-weighted calculations
- Option 5: Print the highest 10 weights (i.e. the {w} in the aforementioned formulae) involved in the orbital-weighted calculations. This option is useful to check if current Δ parameter is reasonable and helps users to better understand how the orbital-weighted method works

- Option 6: Calculating condensed 𝑓𝑤+ , 𝑓𝑤− , 𝑓𝑤0 and Δ𝑓𝑤 values, in other words, calculating integration of these functions in Hirshfeld atomic spaces. The result is useful in quantitatively examining net amount of these functions at various atoms. The default radial and angular integration points are usually fine enough, if you find the sum of condensed 𝑓𝑤+ or 𝑓𝑤− deviates from 1.0 evidently, you should set "iautointgrid" parameter in `settings.ini` to 0 and then properly enlarge "radpot" and "sphpot" parameters.


<!-- p.348 -->

- Option 7: Calculating grid data of 𝑓𝑤+ , 𝑓𝑤− , 𝑓𝑤0 and Δ𝑓𝑤 functions, then you can directly visualize their isosurfaces or export them as cube files so that you can render them via third-part softwares such as VMD and ChimeraX.

Examples of using this module to calculate orbital-weighted Fukui function and orbital-weighted dual descriptor are provided in Section 4.22.2.


### 3.25.4 Special topic 2: (Quasi-)degenerate Fukui function and dual descriptor based on electron density



3.25.4.1 Closed-shell case

Theory In the last section, I have introduced orbital-weighted Fukui function and dual descriptor, which are suitable when frontier molecular orbitals are (quasi-)degenerate. However, they are defined based on orbital approximation, namely the orbital relaxation effect is not taken into account, while this effect cannot be always safely overlooked. In J. Comput. Chem., 37, 2279 (2016), an alternative form of Fukui function and dual descriptor that work for (quasi-)degenerate HOMO/LUMO case was proposed, and this form is defined directly based on electron density, that means orbital relaxation effect is fully taken into account as the original Fukui function and dual descriptor. This (quasi-)degenerate Fukui function and dual descriptor based on electron density will be referred to

as fQ and ΔfQ, respectively.

The idea of fQ is very simple. If at electronic state N the degree of degeneracy of LUMO and HOMO is p and q, respectively, then three forms of fQ are evaluated as follows

fp Q ++ ( )( )( ) rrr −= ρρ NpN

fq Q −− ( )( )( ) rrr −= ρρ NN q

fff 0QQQ ( )[( )( )] / 2 rrr =+ +−

ΔfQ can be evaluated based on 𝑓Q + and 𝑓Q − as usual

QQQ( )( )( )fff+−Δ=−rrr

Clearly, if both HOMO and LUMO are nondegenerate, then fQ and ΔfQ will be equivalent to the original form of Fukui function and dual descriptor, f and Δf, respectively.

To reasonably calculate fQ and ΔfQ, it is crucial to properly determine p and q. Commonly they can be assigned by inspecting energies of several lowest unoccupied MOs and several highest occupied MOs, respectively. If energy difference between an occupied (unoccupied) MO and HOMO (LUMO) is very small, e.g. less than 0.01 eV, then they may be regarded as degenerate. Obvious, there is no strict energy threshold for judging orbital degeneracy, and in some cases you may need to judge by considering various factors, e.g. HOMO-LUMO gap, reasonableness of actual calculation result, orbital shape, etc.

Note that fQ and ΔfQ are defined only for closed-shell case. Multiwfn is not only able to calculate fQ and ΔfQ, but also able to calculate local properties


<!-- p.349 -->

described in Section 3.25.1 (except for ωcubic) based on them. For example, local softness with consideration of degeneracy is product of global softness and fQ. Note that the involved first VEA

and VIP are still evaluated as usual, namely VEA = E(N) − E(N+1) and VIP = E(N-1) − E(N).

Spin multiplicity must be properly chosen for calculating wavefunction file of N+p and N-q states, usually they should be set to p+1 and q+1, see J. Comput. Chem., 37, 2279 (2016) for detailed discussion. This setting commonly is able to guarantee that the attached (detached) electrons equally enter (leave from) all degenerate LUMOs (HOMOs).

Usage In main function 22, both p and q are defaulted to be 1, namely degeneracy of frontier molecular orbitals (FMOs) is not taken into account. To manually set p and q and thus consider the (quasi-)degeneracy effect in the subsequent calculations, you should choose option “-3 Set degree of FMO degeneracy” first. Then information of 10 lowest unoccupied MOs and that of 10 highest occupied MOs will be listed on screen (in the case that the input file contains wavefunction information), you should properly input p and q according to the listed MO energies.

After setting p and q, you can use option 1 to use Multiwfn to help you generate input files of single point task of Gaussian or ORCA code for N, N+p and N-q states, you will be asked to input net charge and spin multiplicity for these states. In addition, if either p or q is not equal to 1, then Multiwfn will also ask you if also generating input file for N+1 and/or N-1 states, because E(N+1) and E(N-1) are needed to evaluate first VIP, VEA and related quantities in option 2. After running these input files, .wfn files of the states will be yielded. Of course, you can also manually generate wavefunction files for the states via any of your favourite quantum chemistry codes.

Finally, you can use corresponding options to calculate various quantities or functions that defined in the CDFT framework, the output content is exactly identical to the default nondegenerate case, though p and q have been properly considered in the current situation. Note that if p or q is not equal to 1, and at the same time either N+1.wfn or N-1.wfn is not available in current folder, then quantities related to first VIP and VEA will not be calculated and outputted by option 2.

An example is given in Section 4.22.3.

3.25.4.2 Open-shell case

Theory For open-shell cases, Martínez Araya proposed working equations of evaluating dual descriptor in Chem. Phys. Lett., 506, 104 (2011) based on the formalism of spin-polarized conceptual DFT. The equations were then further generalized (private communication) and summarized below, where ∆𝑁𝑆 corresponds to change in spin number (𝑁𝑆= 𝑁𝛼−𝑁𝛽), B denotes external magnetic field; 𝑝α

and 𝑝𝛽 are degeneracy of LUMO(α) and LUMO(β), respectively; 𝑞𝛼 and 𝑞𝛽 are degeneracy of

HOMO(α) and HOMO(β), respectively.

Different forms to evaluate 𝑓+ = ( 𝜕𝜌(𝐫) 𝜕𝑁) + 𝑣(𝐫),𝐁(𝐫) , namely spin multiplicity increases, decreases,

and approximately unchanged:


$$f^{+}_{\Delta N_{S}<0}(\mathbf{r})=\frac{\rho_{N+p_\beta}(\mathbf{r})-\rho_{N}(\mathbf{r})}{p_\beta}$$

<!-- formula-ocr: formula_p349_239.png 已替换为LaTeX, 原图保留备查 -->


<!-- p.350 -->


$$f^{+}_{\Delta N_{S}>0}(\mathbf{r})=\frac{\rho_{N+p_{\alpha}}(\mathbf{r})-\rho_{N}(\mathbf{r})}{p_{\alpha}}$$

<!-- formula-ocr: formula_p350_240.png 已替换为LaTeX, 原图保留备查 -->

Different forms to evaluate 𝑓−= ( 𝜕𝜌(𝐫) 𝜕𝑁) − 𝑣(𝐫),𝐁(𝐫) :


$$f_{\Delta N_{S}<0}^{-}(\mathbf{r})=\frac{\rho_{N}(\mathbf{r})-\rho_{N-q_{\alpha}}(\mathbf{r})}{q_{\alpha}}$$

<!-- formula-ocr: formula_p350_241.png 已替换为LaTeX, 原图保留备查 -->

Different forms of evaluating dual descriptor:

−(𝐫) In principle, Δ𝑓Δ𝑁𝑆≈0 should be the most ideal choice, because it follows the restriction of −(𝐫) Δ𝑓Δ𝑁𝑆>0(𝐫) = 𝑓Δ𝑁𝑆>0 Δ𝑓Δ𝑁𝑆<0(𝐫) = 𝑓Δ𝑁𝑆<0 −(𝐫) Δ𝑓Δ𝑁𝑆≈0(𝐫) = 𝑓Δ𝑁𝑆≈0 +(𝐫) −𝑓Δ𝑁𝑆<0 +(𝐫) −𝑓Δ𝑁𝑆>0 +(𝐫) −𝑓Δ𝑁𝑆≈0

keeping the spin-number constant. However, there are two ways to also keep the spin-number

constant, which only involve change in α and β electrons, respectively, but they are not examined in literature.


$$f_{\Delta N_{S}>0}^{-}(\mathbf{r})=\frac{\rho_{N}(\mathbf{r})-\rho_{N-q_{\beta}}(\mathbf{r})}{q_{\beta}}$$

<!-- formula-ocr: formula_p350_242.png 已替换为LaTeX, 原图保留备查 -->

Usage Subfunction 12 of the CDFT module is dedicated to evaluating all aforementioned functions. After booting up Multiwfn, usually you should:

(1) Load a wavefunction file containing basis function information and all orbitals (2) Enter subfunction 12 of main function 22 (3) If this system has degeneracy in frontier MOs, choose option 1 to set up degeneracy (4) Choose option 2 to generate input files of single point task of Gaussian for all involved electronic states. Then you can ask Multiwfn to invoke Gaussian to directly calculate them, or manually calculate them. Then put the resulting .wfn files (with the same names as the .gjf files) into the current folder.

(5) Choose option 3 to generate grid data of electron density of different electronic states. In the post-processing menu, you can directly visualize isosurface map of Fukui function or dual descriptor of selected form, or export corresponding grid data as .cub file.

An example is given in Section 4.22.3.3.

3.25.5 Special topic 3: Nucleophilic and electrophilic


### superdelocalizabilities

Theory


<!-- p.351 -->

Nucleophilic and electrophilic delocalizabilities are also known as nucleophilic and electrophilic superdelocalizabilities, they were proposed by Schüürmann in Environ. Toxicof. Chem., 9, 417 (1990) and Quant. Struct.-Act. Relat., 9, 326 (1990), and have been employed as molecular descriptors for building quantitative structure-activity relationship (QSAR) equations. In the Schüürmann’s work, nucleophilic superdelocalizability (DN) and electrophilic superdelocalizability (DE) of atom A are defined as follows, respectively

$$D^{N}(A)=2\sum_{i}^{unocc}\sum_{\mu\in A}\frac{C_{\mu,i}^{2}}{\alpha-\varepsilon_{i}}$$

where εi is energy of molecular orbital i, α = (EHOMO + ELUMO)/2, μA stands for basis function μ of atom A, and C is coefficient matrix. Evidently, both DN and DE are negative.

However, the expression of superdelocalizabilities by Schüürmann is only suitable for semi-empirical calculation, which employs orthonormal basis functions. In Sci. Rep., 5, 13695 (2015), a different version of electrophilic superdelocalizability was proposed and it is compatible with non-orthonormal basis functions. In this work, it was shown that electrophilic superdelocalizability of an atom is closely related to its atomic polarizability.

The above definitions of superdelocalizability are based on molecular orbital expansion coefficients; in contrast, in Multiwfn, superdelocalizabilities are evaluated based on Hirshfeld partition of atomic spaces, this form is more robust and fully compatible with diffuse functions. Specifically, in Multiwfn, the nucleophilic and electrophilic superdelocalizabilities are calculated as follows


$$D^{N}(A)=2\sum_{i}^{unocc}\sum_{\mu\in A}\frac{C_{\mu,i}^{2}}{\alpha-\varepsilon_{i}}$$

<!-- formula-ocr: formula_p351_243.png 已替换为LaTeX, 原图保留备查 -->

where ΘA,i is composition of atom A in orbital i calculated by Hirshfeld method, see Section 3.10.5 for detail. Multiwfn also calculates the superdelocalizabilities without the α shift parameter, namely


$$D^{N}(A)=2\sum_{i}^{unocc}\frac{\Theta_{A,i}}{\alpha-\varepsilon_{i}}$$

<!-- formula-ocr: formula_p351_244.png 已替换为LaTeX, 原图保留备查 -->

Usage Since superdelocalizabilities involve virtual orbitals, you should use .mwfn, .fch, .molden or .gms file as input file. Only closed-shell single-determinant wavefunction is acceptable. Diffuse functions should not be used if you intend to calculate DN and DN0, since it utilizes virtual orbitals, whose chemical meaning may be severely broken when diffuse functions are employed.

After loading input file, enter main function 22, then choose option 8, you will obtain DN, DE, DN0, and DE0 for all atoms. Example of output (examples\oxirane.fchk):


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


### 3.25.6 Special topic 4: Dual delocalization descriptor

Theory The theory of dual delocalization descriptor (DDD) was proposed in Phys. Chem. Chem. Phys., 28, 19133 (2026) by Samir Kenouche. This method quantifies responses of the interatomic delocalization index (DI) to variations in the total electron number. This theory is closely related to the bond dual descriptor (BDD) introduced in Section 3.25.1, essentially both of them exhibit how degree of electron sharing changes in the course of electron attachment or removal. However, BDD is calculated based on finite difference of bond orders between two electronic states (N and N-1, or N and N+1), while DDD has an analytical form and its calculation only relies on wavefunction of N state, therefore it has advantage in computational cost. Another advantage is that the components of DDD enable one to examine the role played by frontier molecular orbitals on the response, see original paper for discussions. Note that DDD theory was derived based on frozen orbital approximation (FOA), and only single-determinant closed-shell wavefunctions are supported.

Here I describe key ideas and ingredients of DDD. This theory was derived under the Ángyán-

Loos-Mayer (ALM) formulation of DI (δ):


$$\delta_{A,B}^{\mathrm{A L M}}=\sum_{i,j}\eta_{i}\eta_{j}S_{i j}(A)S_{i j}(B)$$

<!-- formula-ocr: formula_p352_245.png 已替换为LaTeX, 原图保留备查 -->

where η is orbital occupation number, S is atomic overlap matrix (AOM), so 𝑆𝑖𝑗(𝐴) corresponds to

integral of product of MO i and MO j in the space of atom A. i and j loop over all spatial orbitals.

Derivatives of DI have discontinuity at integer number of electrons. With FOA and assuming that electrons can only leave from HOMO, it is shown that left-sided 1st derivative of DI can be expressed as follows, which reflects HOMO-driven response of DI with respect to decrease in N


$$\left(\frac{\partial\delta_{A,B}}{\partial N}\right)^{-}=4\sum_{i<H}S_{\mathrm{H}i}(A)S_{\mathrm{H}i}(B)+4S_{\mathrm{H H}}(A)S_{\mathrm{H H}}(B)$$

<!-- formula-ocr: formula_p352_246.png 已替换为LaTeX, 原图保留备查 -->

in which the second term represents HOMO self-contribution part, while the first term is referred to as 𝑓𝐴𝐵 −, namely 𝑓𝐴𝐵 −= 4 ∑𝑆H𝑖(𝐴)𝑆H𝑖(𝐵)𝑖<H. Right-sided 1st derivative of DI is (i loops over all doubly occupied orbitals)


$$\left(\frac{\partial\delta_{A,B}}{\partial N}\right)^{+}=f_{A B}^{+}=4\sum_{i\in\mathrm{o c c}}S_{\mathrm{L}i}(A)S_{\mathrm{L}i}(B)$$

<!-- formula-ocr: formula_p352_247.png 已替换为LaTeX, 原图保留备查 -->

First-order dual delocalization descriptor is defined as 𝑓𝐴𝐵 (1) = 𝑓𝐴𝐵 + −𝑓𝐴𝐵 −, which characterizes


<!-- p.353 -->

the asymmetry in the response of DI to variations in the total electron number, >0 and <0 clearly indicate LUMO-dominated response and HOMO-dominated response, respectively.

g terms are related to quadratic contributions to the DI response from HOMO or LUMO:


$$\begin{aligned}\boldsymbol{g}_{AB}^{+}&=\boldsymbol{S}_{\mathrm{LL}}(A)\boldsymbol{S}_{\mathrm{LL}}(B)\\boldsymbol{g}_{AB}^{-}&=2\boldsymbol{S}_{\mathrm{HH}}(A)\boldsymbol{S}_{\mathrm{HH}}(B)\\left(\frac{\partial^{2}\delta_{A,B}}{\partial N^{2}}\right)^{+}&=2\boldsymbol{g}_{AB}^{+}\\ \left(\frac{\partial^{2}\delta_{A,B}}{\partial N^{2}}\right)^{-}&=\boldsymbol{g}_{AB}^{-}\end{aligned}$$

<!-- formula-ocr: formula_p353_248.png 已替换为LaTeX, 原图保留备查 -->

When the total number of electrons changes by an integer, variation of DI can be expressed as

It should be emphasized that ∆𝛿𝐴𝐵 − are just approximation to accurate variations of DI, which can be respectively evaluated using finite-difference as 𝛿+ = 𝛿(𝑁+ 1) −𝛿(𝑁) and 𝛿−=𝛿(𝑁) −𝛿(𝑁−1). + and ∆𝛿𝐴𝐵

− , which corresponds to the asymmetry of the response of DI resulting from the addition and removal of an electron. Second-order dual delocalization descriptor is defined as 𝑓𝐴𝐵 (2) = ∆𝛿𝐴𝐵 + −∆𝛿𝐴𝐵

When HOMO and/or LUMO are degenerated, the aforementioned terms are calculated as follows to take the degeneracy into account:


$$\begin{aligned}f_{AB}^{+}&=\frac{1}{n_{\mathrm{L}}}\sum_{l\in\mathrm{L}}f_{AB}^{+(l)}\quad&f_{AB}^{-}&=\frac{1}{n_{\mathrm{H}}}\sum_{h\in\mathrm{H}}f_{AB}^{-(h)}\g_{AB}^{+}&=\frac{1}{n_{\mathrm{L}}}\sum_{l\in\mathrm{L}}g_{AB}^{+(l)}\quad&g_{AB}^{-}&=\frac{1}{n_{\mathrm{H}}}\sum_{h\in\mathrm{H}}g_{AB}^{-(h)}\end{aligned}$$

<!-- formula-ocr: formula_p353_249.png 已替换为LaTeX, 原图保留备查 -->

where nL and nH are degeneracy of LUMO and HOMO, l and h loop over all degenerated LUMOs and HOMOs, respectively. The terms with (l) or (h) superscript refer to those calculated with only

−(ℎ), orbital index only loops over the occupied orbitals that do not belong to the degenerated HOMOs. viewing l as LUMO and h and HOMO, respectively. Note that when calculating 𝑓𝐴𝐵

Usage

(2) for any bond in the system. The system should be closed-shell, and a wavefunction file containing basis function information (e.g. .fch, .molden) should be used as input when Multiwfn boots up. Multiwfn is able to calculate 𝑓𝐴𝐵 + , 𝑓𝐴𝐵 −, 𝑓𝐴𝐵 (1), 𝑔𝐴𝐵 + , 𝑔𝐴𝐵 −, 𝑓𝐴𝐵

This function corresponds to subfunction 11 of main function 22. After entering it, usually you should choose option 1 or option 2 to calculate AOM using AIM partition or Hirshfeld partition of atomic spaces, respectively, then you will be asked to input the bond to be studied, then results will be immediately shown on screen. It is worth noting that if Hirshfeld partition is used to generate AOM, the resulting DI also corresponds to fuzzy bond order (Section 3.11.6), and hence response of fuzzy bond order to N is studied.

If you already have a .txt file containing AOM of all MOs of the present system exported by fuzzy analysis module or basin analysis module, in this function you can also directly choose option 3 to load and use it, so that AOM will not be calculated here. Note that before generating AOM using fuzzy or basin analysis module, you should set “ispecial” in `settings.ini` to 3, otherwise only occupied orbitals will be involved in the AOM.
