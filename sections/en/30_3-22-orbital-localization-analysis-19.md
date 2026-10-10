# 3.22 Orbital localization analysis (19)

> Multiwfn manual, p.305–309. Images: `../imgs/`.

---

<!-- p.305 -->

An example is given in Section 4.18.18.


## 3.22 Orbital localization analysis (19)

Theory of orbital localization Canonical molecular orbitals (CMOs) often show strong delocalization character and thus do not convey useful information about chemical bonding. There are many ways to localize MOs, the most popular ones are Foster-Boys (FB) localization, Edmiston–Ruedenberg (ER) localization and Pipek–Mezey (PM) localization. The NLMO method supported in NBO program is also a kind of orbital localization algorithm. The resulting orbitals from these methods are known as localized molecular orbitals (LMOs). Both the LMOs and CMOs are orthonormal sets and have identical dimensions, they can be transformed to each other via unitary transformation.

The FB is the oldest orbital localization method; it was proposed in Rev. Mod. Phys., 32, 300 (1960). This method minimizes the quantity below, so that the spatial distribution range of all orbitals becomes as narrow as possible

$$\left\langle\Omega\right\rangle_{\mathrm{B o y s}}=\sum_{i}\iint\rho_{i}(\mathbf{r}_{1})(\mathbf{r}_{1}-\mathbf{r}_{2})^{2}\rho_{i}(\mathbf{r}_{2})\mathrm{d}\mathbf{r}_{1}\mathrm{d}\mathbf{r}_{2}\quad\rho_{i}=\mid\varphi_{i}\mid^{2}$$

The FB method is very popular and widely used, so it is supported by Multiwfn.

The ER localization proposed in Rev. Mod. Phys., 35, 457 (1963) is also a well-known method, it localizes orbitals via maximizing below quantity (orbital self-repulsion integral)


$$\left\langle\Omega\right\rangle_{\mathrm{E R}}=\sum_{i}\iint\rho_{i}(\mathbf{r}_{1})\frac{1}{\left|\mathbf{r}_{1}-\mathbf{r}_{2}\right|}\rho_{i}(\mathbf{r}_{2})\mathrm{d}\mathbf{r}_{1}\mathrm{d}\mathbf{r}_{2}$$

<!-- formula-ocr: formula_p305_212.png 已替换为LaTeX, 原图保留备查 -->

The ER method is highly deprecated, because it needs evaluation of two-electrons integral, which is very complicated; furthermore, transformation of the integral from AO basis to MO basis is very expensive. Although in a few papers some people argue that ER method has better physical meaning and the computational cost can be considerably reduced via introducing resolution-of-identity technique, I never think there is any convincing reason to employ ER method instead of FB, so ER method is not supported by Multiwfn.

The most popular orbital localization method is PM. The essence of PM localization is to maximize below quantity, so that distribution range of all orbitals can be shrunk as much as possible


$$p_{A}^{i}$$

<!-- formula-ocr: formula_p305_213.png 已替换为LaTeX, 原图保留备查 -->

iA

In the original paper of PM method J. Chem. Phys., 90, 4916 (1989), $p_{A}^{i}$ corresponds to Mulliken population of atom A in MO i. While in J. Chem. Theory Comput., 10, 642 (2014), it was shown that other population methods such as Löwdin, Hirshfeld, Becke, AIM can also be used in combination with PM and obtaining reasonable result. Currently PM method based on Mulliken, Löwdin and Becke populations are supported in Multiwfn.

Algorithm details If you are not interested in the implementation details of the orbital localization methods, you can safely skip this part.


<!-- p.306 -->

The maximization or minimization of above-mentioned quantities can be done via Jacob sweep algorithm, which is employed in the original paper of the orbital localization methods and still be prevalently used until now. This method has lower efficiency than the later developed sophisticated methods such as unitary optimization and trust region; however, the Jacob sweep is very simple and works well for most cases, in particular when only occupied orbitals are needed to be localized, therefore this algorithm is employed in Multiwfn.

The working equation of PM localization based on various population methods is largely identical, see Eq. 9 of J. Comput. Chem., 14, 736 (1993), they only differ in the definition of the term Q, which is needed to be computed in each iteration of Jacob sweep for every orbital pair.

For PM localization based on Mulliken population (PM-Mulliken method), the term Q corresponding to orbitals i and j for atom A is


$$\begin{array}{r}{Q_{A}^{i j}=\frac{1}{2}\displaystyle\sum_{\mu\in A}\displaystyle\sum_{v}[C_{v i}C_{\mu j}+C_{\mu i}C_{v j}]S_{\mu v}}\end{array}$$

<!-- formula-ocr: formula_p306_214.png 已替换为LaTeX, 原图保留备查 -->

where μ and ν correspond to basis function index and the latter cycles all basis functions.

For PM-Löwdin method, because the basis functions have been orthonormalized by Löwdin symmetrization, the term Q is simplified as ijAijAQC Cμμμ∈= 

The PM-Löwdin is seemingly much cheaper than PM-Mulliken; however, if properly programming, the cost of two methods are essentially identical, because the Q for PM-Mulliken case can be reformulated as


$$Q_{A}^{i j}=\frac{1}{2}\sum_{\mu\in A}[C_{\mu j}(\mathbf{S C})_{\mu i}+C_{\mu i}(\mathbf{S C})_{\mu j}]$$

<!-- formula-ocr: formula_p306_215.png 已替换为LaTeX, 原图保留备查 -->

If the SC matrix is calculated and stored in memory before Jacob sweep and updated frequently

during iteration, the summation for index ν can be completely ignored. In fact, because symmetric diagonalization step of Löwdin method is time-consuming for large system, the overall cost of PM-Mulliken is generally lower than PM-Löwdin.

In the PM-Becke, namely PM localization based on Becke population (see Section 3.9.8), the Q is written as


$$\boldsymbol{Q}_{A}^{ij}=\boldsymbol{\mathbf{c}}_{i}^{\mathrm{T}}\boldsymbol{\mathbf{S}}^{A}\boldsymbol{\mathbf{c}}_{j}$$

<!-- formula-ocr: formula_p306_216.png 已替换为LaTeX, 原图保留备查 -->

where SA is atomic overlap matrix between basis functions at atom A, the wA(r) is Becke weighting

function of atom A, the χ is basis function, ci stands for the column array of expansion coefficients of orbital i. The cost of PM-Becke method is high, especially for large systems, this is not only because calculating atomic overlap matrices for all atoms by numerical integration is quite time-consuming, but also the Q term is calculated numerous times during the whole localization process while each time expensive matrix multiplications are involved.

Regarding the FB method, because it involves transformation of dipole moment integrals from AO to MO basis, which requires large amount of arithmetic operations, it is more expensive compared to PM-Mulliken and PM-Löwdin, but the cost is significantly lower than PM-Becke.

Which orbital localization method should I use? Commonly, PM-Mulliken and PM-Löwdin are recommended to use, because their results are usually satisfactory and the cost is very low. However, when abundant diffuse functions are


<!-- p.307 -->

presented, these methods may (but not always) break down, as it is well known that diffuse functions severely breaks meaning of Löwdin and Mulliken populations.

If you need to use PM method and diffuse functions are dispensable for representing the electronic structure of present system (e.g. anion or a neutral molecule heavily polarized by a strong external electric field), you should use the more robust but significantly more expensive PM-Becke method instead.

FB localization is also compatible with diffuse functions, and it is not as expensive as PM-

Becke. However, the orbitals localized by FB method do not preserve σ-π separation character as PM orbitals, for example, the double-bond will be represented as two banana orbitals, which somewhat contradicts with common chemical intuition, you can use FB method if you do not care about this.

Usage of orbital localization module The input file must contain basis function information, thus you can use e.g. .mwfn, .fch, .molden or .gms as input file. This function only works for restricted and unrestricted SCF wavefunction.

Due to the robustness and very low cost of PM-Mulliken method, it is chosen as the default orbital localization method in Multiwfn. If you want to change to other methods, use option "-6 Set localization method".

In the interface, you can use option 1 to choose to localize occupied MOs only, or use option 2 to localize both occupied and unoccupied MOs (the two set of orbitals will be localized separately, i.e. no mixture between occupied and unoccupied orbitals is allowed). For unrestricted wavefunctions, the alpha and beta parts are treated separately. Via option 3 you can localize specific subset of MOs; in other words, only specific MOs are allowed to be mixed during localization. This feature enables you to realize special purposes, for example, obtaining fully or semi- localized MOs in certain region by selecting proper MOs.

Orbital localization is an iterative process, thus you should set criterion of convergence and maximum number of cycles. The default values are commonly appropriate and need not to be modified. The convergence status is printed during iteration, for all localizations methods, the

change of 2()iAiAPp= is used for judging convergence.

Once the localization is converged, orbital composition of all resulting LMOs will be calculated and major characters of the LMOs are printed. By default, the robust Hirshfeld method is employed for evaluating orbital compositions (see Section 3.9 for detail), but you can also change to other methods via option "-9 Set the method for calculating orbital composition" before the orbital localization.

Finally, the LMOs are exported to new.fch in current folder, and then Multiwfn automatically loads it, after that you can analyze the localized orbitals in various ways; for example, plotting them as isosurfaces by main function 0 or performing orbital composition analysis by main function 8. If you do not want to let Multiwfn automatically load the newly generated new.fch, you can choose option -3 once to switch the status.

Hints on performing orbital localization analysis In Multiwfn, the cost of PM-Löwdin and PM-Mulliken methods are proportional to $N_{\mathrm{orb}}2N_{\mathrm{bas}}$ while cost of FB is proportional to Norb2Nbas2, where Norb and Nbas are the number of orbitals to be localized and the number of basis functions, respectively. Clearly, FB is much more expensive. The


<!-- p.308 -->

PM-Becke method is already extremely expensive for medium-sized system with medium-quality basis set (e.g. C60 with 6-31G* basis set), so never consider to employ it for large systems.

Convergence is usually more difficult for unoccupied orbitals than occupied orbitals, more difficult for large systems than small systems, and more difficult for FB than PM method.

Without special reasons, you only need to localize occupied orbitals, since only occupied orbitals carry interesting information about electronic structure. Localization of unoccupied orbitals is much more time-consuming than localizing occupied orbitals, since the number of unoccupied orbitals is often very higher when extended basis set is used. Commonly, via PM-Mulliken/Löwdin method, occupied orbitals can be easily localized for a system containing up to 200 atoms with medium-sized basis set. While for FB, in general this work can only be realized for a system containing up to 100 atoms.

If you want to decrease the cost of localization of occupied orbitals, you can choose "-5 If also localizing core orbitals" once to switch the status from the default "Yes" to "No". Commonly, mix between valence orbitals and core orbitals is rather weak, therefore ignoring inner-core orbitals during localization of valence orbitals is safe. However, in rare cases, ignoring the inner-core orbitals may cause difficulty in convergence.

PM-Mulliken and PM-Löwdin method are not parallelized in Multiwfn, because I found that parallelization does not improve its speed evidently but sometimes make convergence more difficult. FB method is fully parallelized, thus using multi-cores CPU will reduce computational cost considerably.

Basis set of 2-zeta with polarization functions quality (e.g. 6-31G* and def2-SVP) is completely adequate for orbital localization analysis, using larger quality basis set never leads to detectably improved result.

Special topic 1: Evaluating LMO energies Despite LMO is not an eigenfunction of Fock operator, its energy may be evaluated as expectation of Fock operator, which can be solved via a matrix equation. Specifically, Fock matrix in the basis of LMOs can be obtained as

CFC$F_{AO}$TLMO =

where $F_{AO}$ is the Fock matrix in original basis functions, C(μ,i) corresponds to coefficient of basis function μ in LMO i. Energy of LMO i is simply the diagonal term FLMO(i,i).

If you want to obtain energy of LMOs in this way, you should choose option “-4 If calculating and print orbital energies” before starting orbital localization. Then you can choose two ways to provide the $F_{AO}$: (1) Generate it based on energies and coefficient matrix of MOs via FAO=SCEC-1 relationship (2) Input path of a file containing FAO, then the matrix will be loaded, see Appendix 7 of this manual for details.

Special topic 2: Revealing center of LMOs To facilitate capturing basic distribution character of the generated LMOs, Multiwfn is able to calculate center position of LMOs and add them as Bq atom (ghost atom) into current system, so that you can use main function 0 to easily visualize them. The center of LMO is evaluated as follows

iiiφφ=Rr

where r is coordinate vector.

To generate the LMO centers, you should choose “-8 If calculating center position and dipole


<!-- p.309 -->

moment of LMOs” once to switch its status to “Yes”. Then after generating LMOs, exporting .fch and reloa$d_i$ng it, the center positions of the LMOs will be evaluated and added as Bq atoms. The coordinate of LMO centers as well as the correspondence between LMO indices and Bq indices will be outputted to LMOcen.txt in current folder, meantime the setting of main function 0 will be set to the best status for showing LMO centers (as illustrated in Section 4.19.1). Since the newly added Bq atoms do not have accompanying basis functions, the current wavefunction should not be subjected to wavefunction analyses, otherwise Multiwfn may crash or the result is completely meaningless.

Note that if there are multiple bonds and PM localization algorithm is used, the Bq atom

correspon$d_i$ng to the center of σ-LMO and π-LMO of the same bond may overlay with each other. This can be avoided using FB algorithm instead, because FB represents multiple bond as multiple banana LMOs, whose center positions are evidently different with each other.

Special topic 3: Dipole moment analysis for occupied LMOs Once “-8 If calculating center position and $d_i$pole moment of LMOs” has been switched to “Yes”, after performing orbital localization, you will be asked to choose if also performing dipole moment analysis for occupied LMOs. If you input y, then you will have LMOdip.txt, which contains dipole moment analysis result for all occupied LMOs. In order to make you correctly understand the output, below I describe the details.

The contribution of electron of an occupied LMO to $d_i$pole moment of the whole system is


$$\mathbf{D}_{i}=\left\langle\boldsymbol{\varphi}_{i}\middle|-\mathbf{r}\middle|\boldsymbol{\varphi}_{i}\right\rangle$$

<!-- formula-ocr: formula_p309_217.png 已替换为LaTeX, 原图保留备查 -->

This vector for all LMOs is outputted as “Contributions of all occupied LMOs to system $d_i$pole moment” in the LMOdip.txt file.

However, this quantity is unable to be $d_i$rectly used to measure polarity of a LMO. Given that r = (r-$\mathbf{r} = (\mathbf{r} - \mathbf{r}_c) + \mathbf{r}_c$)+rc, where rc is a fixed point, the above quantity can be rewritten as follows

$$\mathbf{D}_{i}=\left\langle\varphi_{i}\left|-(\mathbf{r}-\mathbf{r}_{\mathrm{c}}^{i})\right|\varphi_{i}\right\rangle-\left\langle\varphi_{i}\left|\mathbf{r}_{\mathrm{c}}^{i}\right|\varphi_{i}\right\rangle=-\left\langle\varphi_{i}\left|\mathbf{r}-\mathbf{r}_{\mathrm{c}}^{i}\right|\varphi_{i}\right\rangle-\mathbf{r}_{\mathrm{c}}^{i}\left\langle\varphi_{i}\left|\varphi_{i}\right|\varphi_{i}\right\rangle=-\left\langle\varphi_{i}\left|\mathbf{r}-\mathbf{r}_{\mathrm{c}}^{i}\right|\varphi_{i}\right\rangle-\mathbf{r}_{\mathrm{c}}^{i}$$

we can define a quantity $d_i$, which measures dipole moment of the orbital with respect to the $\mathbf{r} = (\mathbf{r} - \mathbf{r}_c) + \mathbf{r}_c$:

cciiiiiiφφ= −−=+drrDr

If we properly choose the $\mathbf{r} = (\mathbf{r} - \mathbf{r}_c) + \mathbf{r}_c$ for an orbital, then the $d_i$ may be able to reflect polarity of the LMO.

For each LMO that identified as single-center one, the $\mathbf{r} = (\mathbf{r} - \mathbf{r}_c) + \mathbf{r}_c$ is automatically set to be the position of the atom having largest contribution to the LMO. Therefore, the $d_i$ represents deviation of centroid of the LMO electron distribution with respect to the nuclear position. These {d} are printed as “Single-center orbital dipole moments (a.u.)” in the LMOdip.txt.

For each LMO that identified as two-center one, assume that the two atoms with largest contributions are A and B, the $\mathbf{r} = (\mathbf{r} - \mathbf{r}_c) + \mathbf{r}_c$ is set to

RRRRRR=+++rr$\mathbf{r} = (\mathbf{r} - \mathbf{r}_c) + \mathbf{r}_c$ BAABABAB

where rA and RA are nuclear position and covalent ra$d_i$us of atom A, respectively. Similarly for atom B. The $\mathbf{r} = (\mathbf{r} - \mathbf{r}_c) + \mathbf{r}_c$ locates at center of the bonding region, therefore the di, which exhibits deviation of centroid of LMO electron distribution from rc, is capable of revealing the bond polarity. These {d} are printed as “Two-center orbital dipole moments (a.u.)” in the LMOdip.txt.
