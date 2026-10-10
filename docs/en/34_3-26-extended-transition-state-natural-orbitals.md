# 3.26 Extended Transition State - Natural Orbitals for Chemical Valence (ETS-NOCV) analysis (23)

> Multiwfn manual, p.354–360. Images: `../imgs/`.

---

<!-- p.354 -->

An example is given in Section 4.22.6.


## 3.26 Extended Transition State - Natural Orbitals for Chemical Valence (ETS-NOCV) analysis (23)



The Extended Transition State - Natural Orbitals for Chemical Valence (ETS-NOCV) method was proposed in J. Chem. Theory Comput., 5, 962 (2009) by Ziegler et al., it is a combination of the NOCV method proposed in J. Phys. Chem. A, 112, 1933 (2008) and the idea of ETS proposed in Theor. Chim. Acta, 46, 1 (1977). ETS-NOCV has been widely employed in studying chemical bonds and weak interactions between fragments. Briefly speaking, ETS-NOCV enables one to gain a deep insight into interfragment interaction by visual decomposition analysis of the variation of density matrix caused by the interaction.

I will first introduce the theory of ETS-NOCV as clearly and detailedly as possible in Section 3.26.1, and then some implementation details of this analysis in Multiwfn will be mentioned in Section 3.26.2. In Section 3.26.3 I will describe the functions and usage of the ETS-NOCV module in Multiwfn. Application examples of ETS-NOCV analysis are provided in Section 4.23.


### 3.26.1 Theory

The ETS-NOCV analysis in Multiwfn supports arbitrary number of fragments. However, for simplicity, only two fragments are involved when I introduce the theory of ETS-NOCV below.

Physical components of interfragment interaction energy I first review the physical components of interfragment interaction energy, this is important preliminary knowledge for understanding ETS-NOCV.

Total energy variation due to interfragment interaction between fragments A and B may be expressed as (fragments mentioned below are in complex structure, so deformation energy due to distortion of fragment structure during combination is not taken into account in this context):

0 + ∆𝐸Pauli + ∆𝐸orb where EAB is the complex electronic energy, EA and EB are electronic energies of A and B at complex geometry. The four physical components are defined as follows ∆𝐸int = 𝐸𝐴𝐵−𝐸𝐴−𝐸𝐵= ∆𝐸els + ∆𝐸XC

- ∆𝐸els : Interfragment electrostatic interaction energy. It is evaluated as classical Coulomb interaction energy between original wavefunctions of A and B (Ψ𝐴 and Ψ𝐵).

0 : Change in exchange-correlation (XC) energy during combination from Ψ𝐴 and Ψ𝐵 to $\Psi_{A}$. It also accounts for interfragment dispersion interaction since dispersion effect is essentially interfragment Coulomb correlation.
- ∆𝐸XC

- ∆𝐸Pauli: Energy increase due to Pauli repulsion between electrons of the two fragments. It is also known as exchange-repulsion term.

- ∆𝐸orb : Orbital interaction energy due to mix of fragment orbitals, which accounts for polarization effect (intrafragment mix of occupied and unoccupied orbitals) and charge-transfer effect (interfragment mix of occupied and unoccupied orbitals).


<!-- p.355 -->

Specifically, the $\Delta E_{Pauli}$ is expressed as

0 ] −𝐸[Ψ𝐴Ψ𝐵] where E[ ] denotes the energy functional of the complex. Ψ𝐴 $\Psi_B$ are original wavefunctions of A and B. Ψ𝐴Ψ𝐵 may be referred to as promolecular wavefunction, it is the Hartree product of Ψ𝐴 and Ψ𝐵, and it simply corresponds to the Slater determinant directly constructed by all occupied orbitals of A and B. $\Psi_{AB}$ 0 is denoted as frozen state wavefunction, it is defined as antisymmetric product of Ψ𝐴 and Ψ𝐵 ; specifically, it corresponds to the Slater determinant constructed by all occupied orbitals of A and B, and Löwdin orthonormalization has been employed among these orbitals to make them to be orthonormal with each other. The frozen state can be viewed as an artificial intermediate state comes from the fact that when two fragments are combined together to form an identical particle system, all electron orbitals must constitute an orthonormal set, or occupied orbitals of a fragment must be orthogonal to those of another fragment to comply Pauli exclusion principle. The interfragment Löwdin orthonormalization brings additional nodal plane(s) to original fragment orbitals, this phenomenon evidently makes kinetic energy of the orbitals ∆𝐸Pauli = 𝐸[Ψ𝐴𝐵

increase, this is mainly why $\Delta E_{Pauli}$ must be a positive value and plays a destabilization effect.

$\Delta E_{orb}$ is expressed as

0 ] $\Psi_{AB}$ is the actual complex wavefunction yielded after self-consistent field (SCF) convergence. The change from Ψ𝐴𝐵 0 to Ψ𝐴𝐵 arises from intrafragment and interfragment orbital mixing (also known as orbital relaxation). $\Delta E_{\mathrm{orb}}$ is always a negative term and thus stabilizes the complex. The ETS-NOCV method focuses on gaining deep chemical insights into the ΔEorb term. ∆𝐸orb = 𝐸[Ψ𝐴𝐵] −𝐸[Ψ𝐴𝐵

In summary, aforementioned terms can be organized as the following relationship

𝐸𝐴 iso + 𝐸𝐵 iso $\Delta E_{prep}$→ 𝐸𝐴[Ψ𝐴] + 𝐸𝐵[Ψ𝐵] 0→ 𝐸[Ψ𝐴Ψ𝐵] Δ𝐸els+Δ𝐸XC $\Delta E_{Pauli}$→ 𝐸[$\Psi_{AB}$ 0 ] $\Delta E_{\mathrm{orb}}$→ 𝐸[Ψ𝐴𝐵]

$\Delta E_{prep}$ is known as preparation energy, it includes distortion energy of fragments A and B from their isolated geometries to complex geometry, and it also includes the energy change of their

electronic states from most stable states to reference state ΨA $\Psi_B$ (for example, to use ETS-NOCV to study the double bond of H2Ge=GeH2, the reasonable fragment reference state should be triplet, however most stable state of GeH2 in its isolated status is singlet. This difference should be

incorporated into the $\Delta E_{prep}$). Clearly the choice of reference states of the fragments affects result of ETS-NOCV analysis while it is somewhat arbitrary in certain cases.

Frankly speaking, in my viewpoint, the above commonly accepted partition of interaction energy is not completely rigorous. Because during transformation of complex wavefunction from

promolecular (reference) state ΨAΨB to actual state $\Psi_{AB}$, the electrostatic interaction energy and exchange-correlation energy must also markedly change, therefore the $\Delta E_{\mathrm{orb}}$ term should not be regarded as solely reflecting the contribution to interaction energy due to orbital mix effect.

0 + ∆𝐸Pauli is sometimes referred to as steric term ΔEsteric in literature for convenience in discussion. Multiwfn is unable to directly evaluate it or its component, but you can $\Delta E_{\mathrm{els}} + \Delta E_{\mathrm{XC}}^{0} + \Delta E_{\mathrm{Pauli}}$

calculate ΔEsteric by Gaussian in combination with Multiwfn, see Section 3.100.8. The $\Delta E_{prep}$ can be directly manually calculated via any quantum chemistry code.

NOCV theory First, we look at the natural orbitals for chemical valence (NOCV) theory. The orbital interaction between the two fragments leads to a density matrix difference


<!-- p.356 -->

0 ] where P and P0 are density matrices of actual complex state and frozen state, respectively; they can be easily generated based on coefficient matrix of occupied orbitals in corresponding state. The $\Delta P^{\text{orb}}$ = 𝐏−𝐏0 = 𝐏[Ψ𝐴𝐵] −𝐏[Ψ𝐴𝐵

NOCV method diagonalizes the $\Delta P^{\text{orb}}$ to solve its eigenvalues and eigenvectors, namely one has the following relationship (the matrices are expressed in Löwdin orthogonalized basis functions)

$\Delta P^{\text{orb}}$𝐂NOCV = 𝐂NOCV𝐯 where CNOCV is the coefficient matrix of NOCV orbitals, each of its columns corresponds to expansion coefficients of a NOCV orbital with respect to Löwdin orthogonalized basis functions. v is a diagonal matrix, $\mathbf{v}$ corresponds to eigenvalue of the ith NOCV orbital. One can also say NOCV orbitals are eigenfunctions of density matrix difference operator, namely

∆𝑃̂orb𝜑𝑖= 𝑣𝑖𝜑𝑖 Note that the number of NOCV orbitals (N) is equal to the number of basis functions. Hence, usually the N is large, but only very few NOCV orbitals have notable magnitude of eigenvalues and which are what one should focus on during analysis.

Orbital interaction results in variation of electron density, which can be represented as “orbital deformation density”

0 ] The ∆𝜌orb can be decomposed as contributions of various NOCV densities {𝑣𝑖𝜑𝑖 ∆𝜌orb(𝐫) = 𝜌(𝐫) −𝜌0(𝐫) = 𝜌[Ψ𝐴𝐵] −𝜌[Ψ𝐴𝐵 2}


$$\Delta\rho^{\mathrm{o r b}}(\mathbf{r})=\sum_{i=1}^{N}v_{i}\varphi_{i}^{2}(\mathbf{r})$$

<!-- formula-ocr: formula_p356_250.png 已替换为LaTeX, 原图保留备查 -->

Because $\Delta P^{\text{orb}}$ is a traceless matrix represented under a set of orthonormal basis, a noteworthy feature of NOCV orbitals is that they occur in pairs, that is if the eigenvalues are sorted from most

positive to most negative, then vN+1-i = −vi. For simplicity, N+1−i will be abbreviated to −i later. So, $\Delta\rho^{\mathrm{orb}}$ can also be decomposed as NOCV pair contributions for easier analysis and discussion


$$\Delta\rho^{\mathrm{o r b}}(\mathbf{r})=\sum_{i=1}^{N/2}v_{i}\varphi_{i}^{2}(\mathbf{r})+v_{-i}\varphi_{-i}^{2}(\mathbf{r})=\sum_{i=1}^{N/2}v_{i}[\varphi_{i}^{2}(\mathbf{r})-\varphi_{-i}^{2}(\mathbf{r})]$$

<!-- formula-ocr: formula_p356_251.png 已替换为LaTeX, 原图保留备查 -->

Obviously, the NOCV analysis allows us to look into the details of the orbital deformation density in terms of NOCV orbitals or densities to better understand the nature of the orbital interaction.

ETS and ETS-NOCV theory The extended transition state (ETS) theory shows that


$$\Delta E_{\mathrm{orb}}=\mathrm{Tr}\big(\Delta\mathbf{P}^{\mathrm{orb}}\mathbf{F}^{\mathrm{TS}}\big)=\sum_{\mu}^{N}\sum_{\nu}^{N}\Delta P_{\mu\nu}^{\mathrm{orb}}F_{\mu\nu}^{\mathrm{TS}}$$

<!-- formula-ocr: formula_p356_252.png 已替换为LaTeX, 原图保留备查 -->

∆𝐸orb = Tr(Δ𝐏orb𝐅TS) = ∑∑∆𝑃𝜇𝜈orb𝐹𝜇𝜈TS

where μ and ν are indices of Löwdin orthogonalized basis functions. FTS is the so-called extended transition state Fock matrix (or Kohn-Sham matrix in KS-DFT case), which is the Fock matrix constructed using average of Ψ𝐴𝐵 and Ψ𝐴𝐵 0 . Note that the “extended transition state” in this context is very different to the transition state in common sense, in the present context it refers to the artificial electronic structure at midpoint between Ψ𝐴𝐵 and Ψ𝐴𝐵 0 , where orbital interaction takes place only half.

ETS-NOCV theory shows that


<!-- p.357 -->


$$\Delta E_{\mathrm{orb}}=\sum_{i=1}^{N}\Delta E_{i}^{\mathrm{orb}}=\sum_{i=1}^{N}\nu_{i}\tilde{F}_{i,i}^{\mathrm{TS}}$$

<!-- formula-ocr: formula_p357_253.png 已替换为LaTeX, 原图保留备查 -->

where i is index of NOCV, and 𝐹̃𝑖,𝑖 TS is the ith diagonal term of Fock matrix in the basis of NOCV

orbitals; in other words, it corresponds to energy of the ith NOCV orbital estimated using 𝐹̂TS operator, namely 𝐹̃𝑖,𝑖 TS = ⟨𝜑𝑖|𝐹̂TS|𝜑𝑖⟩. Again, because NOCV orbitals are paired, the $\Delta E_{orb}$ can be decomposed as contributions of NOCV pairs


$$\Delta E_{\mathrm{orb}}=\sum_{i=1}^{N/2}v_{i}\big[\tilde{F}_{i,i}^{\mathrm{TS}}-\tilde{F}_{-i,-i}^{\mathrm{TS}}\big]$$

<!-- formula-ocr: formula_p357_254.png 已替换为LaTeX, 原图保留备查 -->

From the energy contributions, we can determine which NOCV pairs play a major role in orbital interaction and then analyze their characters emphatically. The NOCV pairs with very small eigenvalues or energies can be ignored during discussion.

Deformation density Finally, three kinds of deformation densities are summarized below, they are involved in ETS-NOCV analysis in Multiwfn, note that ρ, ρ$\rho, \rho^{0}, \rho_{A}$ ρA and ρB correspond to electron density of Ψ𝐴𝐵, Ψ𝐴𝐵 0 , Ψ𝐴 and Ψ𝐵, respectively.

Pauli deformation density:

∆𝜌Pauli(𝐫) = 𝜌0(𝐫) −[𝜌𝐴(𝐫) + 𝜌𝐵(𝐫)] Orbital deformation density:

∆𝜌orb(𝐫) = 𝜌(𝐫) −𝜌0(𝐫) Total deformation density:


$$\Delta\rho(\mathbf{r})=\Delta\rho^{\mathrm{o r b}}(\mathbf{r})+\Delta\rho^{\mathrm{P a u l i}}(\mathbf{r})=\rho(\mathbf{r})-[\rho_{A}(\mathbf{r})+\rho_{B}(\mathbf{r})]$$

<!-- formula-ocr: formula_p357_255.png 已替换为LaTeX, 原图保留备查 -->


### 3.26.2 Implementation details

Features The ETS-NOCV module in Multiwfn has the following capabilities:

- Calculate NOCV orbital wavefunctions, eigenvalues and energies
- Visualize NOCV orbitals and export corresponding cube files
- Calculate energy contributions to ΔEorb of NOCV pairs
- Visualize NOCV pair densities and export corresponding cube files
- Calculate composition of NOCV pair and orbitals using SCPA method
- Visualize promolecular, frozen state and actual complex orbitals
- Visualize ΔρPauli, Δρorb, and Δρ isosurfaces The ETS-NOCV module supports defining arbitrary number of fragments. If you defined M fragments, then the ETS-NOCV will analyze the total interaction between all the M fragments.

Only Hartree-Fock and Kohn-Sham DFT wavefunctions are supported. Multiconfiguration wavefunctions such as coupled-cluster, CASSCF, and double-hybrid functional wavefunctions are not supported.

Only restricted closed-shell or unrestricted open-shell wavefunctions are acceptable. Restricted open-shell wavefunction is not supported.


<!-- p.358 -->

If complex is open-shell, or any fragment is open-shell, the ETS-NOCV analysis will be automatically conducted in open-shell form. In this case, the alpha and beta NOCV orbitals are solved independently, and their energies are estimated using alpha and beta Fock matrices respectively.

The energies of NOCV orbitals in Multiwfn are not calculated in the strict way of the standard ETS-NOCV method as described above! This is because the $\mathbf{F}^{\mathrm{TS}}$ in ETS-NOCV analysis currently is not available in Multiwfn. In the post-processing menu of ETS-NOCV module, you can choose to load a file containing the actual Fock matrix of the complex outputted by a quantum chemistry code, or you can also choose to let Multiwfn directly generate the actual Fock matrix of the complex based on the orbital energies and coefficients recorded in input file via $\mathbf{F}=\mathbf{SCEC}^{-1}$ relationship, then for example the ith NOCV orbital energy will be evaluated as ⟨𝜑𝑖|𝐹̂|𝜑𝑖⟩ , where 𝐹̂ is the Fock operator corresponding to the loaded or generated Fock matrix. According to my comparison with some published ETS-NOCV data and result of ORCA code, the NOCV energies evaluated in this

approximated way using 𝐹̂ is close to the NOCV energies in strict sense derived based on 𝐹̂TS (especially for weak interaction case), at least this discrepancy does not qualitatively affect your identification of dominant NOCV orbitals/pairs. Notice that due to this difference, the sum of

energies of all NOCV orbitals or pairs given by Multiwfn is not exactly equal to $\Delta E_{\mathrm{orb}}$

Input files You need to provide wavefunction files of the complex and that of each fragment. The file should contain basis function information, for example you can use .fch, .mwfn, .molden, and so on; however, .wfn and .wfx cannot be used since they do not contain basis function information. If you are confused, see Section 2.5.

To prepare the wavefunction files needed by ETS-NOCV analysis for a system, commonly you should do following steps

(1) Optimize the geometry of the complex first by your favourite quantum chemistry code, and meantime obtain wavefunction file of the complex

(2) Extract coordinate of each fragment from the optimized complex, and then save them as input files of single point task. If you are using Gaussian, do not forget to add nosymm keyword to avoid automatic reorientation during the calculation.

(3) Run input file of every fragment to obtain their wavefunction files. Evidently, the calculation level of the fragments must be identical to that of complex. If there is no special reason, using diffuse functions is not only completely unnecessary but also deprecated. Usually, using a 3-zeta basis set such as def2-TZVP is absolutely adequate, while using a 2-zeta basis set such as 6-31G* and def2-SVP is also sufficient for qualitative study.

After arranging the atoms in each fragment according to the loading order of the fragments in ETS-NOCV module, the order of the atoms must be consistent with that in the complex. Obviously, this requires that the order of atoms in fragment files must be the same as that in the complex, and the atoms of each fragment must occur consecutively in the complex.

Usually, using an implicit solvation model should be avoided, it makes situation much more complicated.


<!-- p.359 -->


### 3.26.3 Usage

The general process of using the ETS-NOCV module is: (1) Boot up Multiwfn, and load wavefunction file of the complex (2) Enter main function 23 (3) Input the number of fragments (4) Input file path of wavefunction file of each fragment. The loading order should be in line with the occurrence order of the fragments in the complex

Note that if a fragment is found to be unrestricted open-shell, you will also be asked to choose if flipping spin. If you choose y, then the wavefunctions and occupancies of alpha and beta orbitals will be exchanged. You should properly set spin flipping so that the sum of number of alpha (beta) electrons of all fragments is identical to that of the complex.

(5) Now the NOCV orbital wavefunctions and eigenvalues are calculated, and NOCVs are automatically paired. From the NOCV information on screen, you can directly find NOCV pair indices and corresponding NOCV indices as well as their eigenvalues. Currently NOCV energies have not been evaluated.

After that a post-processing menu occurs, and you can choose corresponding option according to your requirement, they are briefly mentioned below.

If you want to view NOCV information again, choose “0 Print NOCV information”. By default, the printing threshold of NOCV eigenvalues is 0.001, the NOCVs with absolute eigenvalue less than this threshold are not shown to avoid too lengthy output. You can manually change the threshold via “-3 Set printing threshold of NOCV eigenvalues”.

To obtain NOCV energies, you need to select either “-1 Load Fock/KS matrix and evaluate NOCV orbital energies” to load a file containing Fock matrix of the current complex calculated at the same level (see Appendix 7 of this manual for detail), or select “-2 Generate Fock/KS matrix and evaluate NOCV orbital energies” to generate Fock matrix of current complex based on the energies and coefficients of molecular orbitals in the complex wavefunction file (i.e. the file loaded after booting up Multiwfn). Then Multiwfn will calculate NOCV energies, and then NOCV information with energies will be shown on screen.

“1 Show isosurface of NOCV orbitals” is used to visualize NOCV orbitals. After selecting this option, NOCV information will be shown on screen for user’s convenience, and a GUI window appears, you can select corresponding NOCV orbital from the list at the bottom right corner of the window, you can also directly input the index of the NOCV orbital that you want to view in the text box at the bottom right corner of the window.

“2 Show isosurface of NOCV pair density” is used to visually examine density of NOCV pair(s). After choosing it, NOCV information will be shown on screen for user’s convenience, and then you can input the NOCV pair index of interest. For example, if then you input 6, then grid data of 𝑣6[𝜑6 2 (𝐫)] will be calculated and its isosurface map will be shown in a GUI window. It is important to note that you can input a range of pair indices to obtain their total density; for example, if you input 2,4-6,9, then the grid data of ∑𝑣𝑖[𝜑𝑖 2 (𝐫)]𝑖=2,4,5,6,9 will be calculated and plotted as isosurface. If there are e.g. 50 NOCVs in total and you input 1-50, then the grid data 2(𝐫) −𝜑−6 2(𝐫) −𝜑−𝑖

will simply correspond to the orbital deformation density $\Delta\rho^{\text{rb}}$. In addition, it is worth to note that for open-shell case, pair index of alpha and beta spins is different (as shown on screen), therefore you can input proper indices to view sum of specific alpha and beta NOCV pair(s).

If you want to visualize the $\Delta\rho^{\mathrm{Pauli}}$ mentioned above, you can respectively select


<!-- p.360 -->

“3 Show isosurface of Pauli deformation density”, “4 Show isosurface of orbital deformation density”

and “5 Show isosurface of total deformation density”. The $\Delta\rho^{\text{Pauli}}$ allows you to vividly understand how electrons are repulsed in the region between fragments due to Pauli repulsion. Δρorb enables you to graphically examine electron concentration between fragments due to formation of covalent interaction or electron transfer between fragments due to mix of occupied orbitals of fragment(s)

and unoccupied orbitals of other fragments. The Δρ is simply the sum of $\Delta\rho^{\text{Pauli}}$ and Δρorb, in fact it can also be calculated by making use of the custom operation feature of main function 5 (Section 3.7.1).

The grid data of a NOCV orbital, NOCV pair(s), $\Delta\rho^{\text{Pauli}}$, Δρorb, and Δρ can also be exported as .cub file so that you can visualize them in third-part visualization softwares, you just need to select corresponding one of options 6~10.

When selecting options 2 to 8 to visualize or export various kinds of densities, if you have not defined grid setting by “-5 Set grid for calculation of various densities”, you will be automatically asked to set grid first. Next time you will not need to set the grid again, but you can still change grid setting anytime via option -5.

0 and $\Psi_A \Psi_B$ mentioned in Section 3.26.1, you can respectively select “11 Visualize promolecular orbitals”, “12 Visualize frozen state orbitals” and “13 Visualize actual complex orbitals” to visualize the corresponding orbital isosurfaces. The orbitals of Ψ𝐴Ψ𝐵 are simply the orbitals in the fragment wavefunction files, the orbitals of Ψ𝐴𝐵 are simply those in the complex wavefunction file. By comparing the orbitals in Ψ𝐴𝐵 0 and those in Ψ𝐴Ψ𝐵 , you can examine how Pauli repulsion between electrons of the fragments (realized by Löwdin orthogonalization as mentioned earlier) deform the occupied fragment molecular orbitals. If isovalue has been set to a small enough value, you will be able to observe the additional nodal plane(s) on the fragment orbitals of Ψ𝐴𝐵 0 caused by the Löwdin orthogonalization. Note that the orthogonalization is not applied to unoccupied orbitals during ETS-NOCV analysis in Multiwfn, hence the unoccupied orbitals in Ψ𝐴𝐵 0 and Ψ𝐴Ψ𝐵 are exactly the same. Studying composition of NOCV pairs and that of corresponding NOCV orbitals is often useful when you want to better understand their nature. If you choose option “14 Calculate composition of NOCV orbitals and pairs”, you will be asked to choose a NOCV pair, then contributions from every basis function, shell, angular moment, and atom to the NOCV pair and corresponding NOCV orbitals will be printed on screen. The compositions of NOCV orbitals are evaluated using the SCPA method mentioned in Section 3.10.3. The composition of NOCV pair is calculated as 𝑣𝑖Θ𝑖+ 𝑣𝑗Θ𝑗, If you are interested in the occupied orbitals of $\Psi_A \Psi_B$

where i and j are indices of the two paired NOCV orbitals, 𝑣𝑗= −𝑣𝑖, and Θ is orbital composition

evaluated by SCPA method. This option is useful in studying electron transfer. For example, if using this option you find contribution of atoms A and B to NOCV pair 1 is 34.12% and -20.53%, respectively, that means atom A gained 0.3412 electron and atom B lost 0.2053 electron due to the interaction characterized by NOCV pair 1. Note that diffuse functions should never be used since SCPA method is incompatible with them. If you really have to use diffuse functions, after performing ETS-NOCV analysis, you should return to main menu (in this case the orbitals in memory are NOCV orbitals) and then use main function 8 to compute orbital composition via e.g. Hirshfeld or Becke method, which works normally when diffuse functions are presented.

Option “-6 Manually define correspondence between NOCV pairs and orbitals” is sometimes useful. Multiwfn automatically constructs NOCV pairs according to NOCV orbitals sorted by eigenvalues. For symmetric systems (e.g. linear system Ne...BeO), some NOCV orbitals may be
