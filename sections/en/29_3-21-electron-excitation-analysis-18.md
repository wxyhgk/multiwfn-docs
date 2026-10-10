# 3.21 Electron excitation analysis (18)

> Multiwfn manual, p.257–304. Images: `../imgs/`.

---

<!-- p.257 -->

basin defined by a cube file named basin.cub in current folder, in which the grid value corresponds to basin index. This option aims to obtain atomic contribution to population of ELF bond basins (or other type of basins) based on AIM partition. Please check Section 4.17.7 for example.

- 10 Calculate high ELF localization domain population and volume (HELP, HELV): This option is used to calculate the HELP and HELV, which were defined in ChemPhysChem, 14, 3714 (2013) to characterize lone pair electrons. This option appears only when the real space function used to partition basin is ELF. See Section 4.17.8 for example on using this option to calculate HELP and HELV.

- 11 Calculate orbital compositions contributed by various basins: Via this option, you can calculate contribution to specific orbital contributed by AIM basins or other kinds of basins, such as ELF basins. See Section 4.8.6 for example.

- 12 Assign ELF basin labels: This option is used to automatically assign labels for all basins when the real space function used to generate basins is ELF, the basin volumes and populations are also printed together. Examples of assigned labels: C(F2), V(O3), V(S5,F7), V(Li1,Li2,Li3). The labels are outputted twice, at the first time the data are outputted according to basin indices, at the second time the data are outputted according to sorted basin labels. See Section 4.17.2 for example.

Algorithm detail of automatic assignment of ELF basin labels: Core basins are assigned first. If distance between an ELF attractor and a nucleus is smaller than a threshold, then the corresponding basin will be assigned as core type. The threshold distances are built-in and different for different elements. For an element, the threshold was determined as the position of outermost minimum of radial curve of spherically averaged ELF of the atom based on high-quality atomic wavefunction of ground state. The built-in thresholds have been determined for H~Lr, therefore if the system contains element(s) heavier than Lr then this option cannot be used, namely you have to manually determine the labels by visualizing attractor positions and/or spatial range of basins.

After that, all other basins will be labelled as valence type. If any grid of an attractor is next to a grid of a core basin, then the atom corresponding to the core basin will be added to the member list of this attractor. Assume that finally an attractor has members of C1 and O2, then its label will be V(C1,O2). H and Ne are relatively special, if distance between an attractor and nucleus of H or Ne is smaller than 0.2 Bohr, then the atom will be added to the member list.

Notice that basin labels cannot be correctly assigned for elements using pseudopotential, because in this case core basins cannot be assigned.

For options 3, 4, 5, 7 and 8, if the input file you used does not contain GTF information (e.g. .cub file is used as input file and you directly use the grid data carried by it to generate basins), then Multiwfn will prompt you to input a new file, which should contain GTF information of present system, you can use for example mwfn/.wfn/.wfx/.fch/.molden/.gms as input.

Many examples of this module can be found in Section 4.18. Information needed: GTFs or grid data loaded from external file (e.g. .cub), atom coordinates


## 3.21 Electron excitation analysis (18)


### 3.21.A Basic information about electron excitation analysis module

3.21.A.1 Overview

Main function 18 contains a lot of subfunctions aiming for electron excitation analysis, namely characterizing the electron excitation in various ways. All functions in this category fully support


<!-- p.258 -->

single-reference methods (i.e. reference wavefunction for generating excited state wavefunction is single Slater-determinant), including TDDFT, TDA-DFT, CIS and TDHF, while ZINDO is also supported by transition density matrix plotting function. Other kinds of methods for excited state problems such as EOM-CCSD, LR-CC2/3, CASSCF, CASPT2 and MRCI are not formally supported. Examples of some of these electron excitation analysis functions are provided in Section 4.18.

Both closed-shell and open-shell systems are fully supported by all kinds of electron excitation analyses of Multiwfn.

3.21.A.2 Basic knowledge about single-reference methods

Excited state wavefunction ($\Psi^{exc}$) of CIS and TDA-DFT methods can be represented as


$$\Psi^{\mathrm{e x c}}=\sum_{i\rightarrow a}w_{i}^{a}\Phi_{i}^{a}\equiv\sum_{i}^{\mathrm{o c c}}\sum_{a}^{\mathrm{v i r}}w_{i}^{a}\Phi_{i}^{a}$$

<!-- formula-ocr: formula_p258_158.png 已替换为LaTeX, 原图保留备查 -->

where i and a respectively run over all occupied and all virtual MOs, similarly hereafter in. Φ𝑖 𝑎 is the configuration state wavefunction corresponding to moving an electron from originally occupied MO i to virtual MO a. w is known as configuration coefficient. The electron excitation in CIS or TDA-DFT framework therefore can be represented as linear combination of orbital pair transitions. The weighting coefficients w satisfy this normalization condition:


$$100\% \times (w_i^a)^2$$

<!-- formula-ocr: formula_p258_159.png 已替换为LaTeX, 原图保留备查 -->

Clearly, the i→a orbital pair transition has contribution of 100% × (𝑤𝑖 𝑎)2 to the electron excitation. While for TDHF and TDDFT, excited state wavefunction also contains so-called de-excitation part:


$$\Psi^{\mathrm{e x c}}=\sum_{i\rightarrow a}w_{i}^{a}\Phi_{i}^{a}+\sum_{i\leftarrow a}w_{i}^{\prime a}\Phi_{i}^{a}$$

<!-- formula-ocr: formula_p258_160.png 已替换为LaTeX, 原图保留备查 -->

where w and w' correspond to configuration coefficient of excitation and de-excitation, respectively. In this case, the normalization condition becomes:


$$\sum_{i\rightarrow a}(w_{i}^{a})^{2}-\sum_{i\leftarrow a}(w_{i}^{\prime a})^{2}=1$$

<!-- formula-ocr: formula_p258_161.png 已替换为LaTeX, 原图保留备查 -->

The MOs used for CIS/TDHF and TDA-DFT/TDDFT are yielded by HF and DFT calculation for ground state of present system, respectively. The Slater determinant that consisted of the occupied MOs, namely the ground state wavefunction, is known as reference state. If the reference

state is closed-shell, then α and β MOs are exactly matched with each other, and thus β→β orbital transitions have one-to-one correspondence with α→α orbital transitions; in this situation, only one set of orbital transition is recorded, and correspondingly, the configuration coefficients are normalized to 0.5 instead of 1.

3.21.A.3 Input files

Input files of almost all electron excitation analysis functions are basically the same, except for subfunction 3 (Analyzing charge transfer based on density difference grid data). Two kinds of input files are needed:

(1) A file containing basis function and molecular orbital information (orbital


<!-- p.259 -->

wavefunctions of reference state)

mwfn, .fch/.fchk, .molden, and .gms files produced by excited state calculation (e.g. TDDFT) can be directly used. This file should be loaded when Multiwfn boots up. For example, you can use the .fch file converted by formchk from .chk file of TDDFT task of Gaussian, and another example, you can use the .molden.input file converted by orca_2mkl from .gbw file of TDDFT task of ORCA.

(2) A file containing configuration coefficients of excited states. The path of this kind of file should be inputted when you enter corresponding analysis function, Multiwfn will load configuration coefficients from this file. There are several situations, as shown below:

- Gaussian users: Output file (.out or .log) of CIS, TDHF, TDDFT and TDA-DFT tasks can be used. Both single point and optimization tasks are supported; for the latter case, Multiwfn analyzes electron excitation at the final geometry. Since by default Gaussian only outputs the configuration coefficients whose absolute value is larger than 0.1, In order to achieve acceptable accuracy, you must add IOp(9/40=4) keyword in the route section so that all configuration coefficients whose magnitude larger than 0.0001 will be printed (If the calculation in Multiwfn is found to be too expensive, using IOp(9/40=3) instead is also generally acceptable). Implicit solvation model, including external iteration (state specific) treatment of solvent response to transition, is fully compatible.

- ORCA users using CIS or TDA-DFT: Output file of CIS or TDA-DFT tasks can be used. Beware that TPrint keyword should be used in %cis or %tddft, otherwise only very small amount of configuration coefficients will be printed. TPrint x means outputting configurations whose contribution to excited state is larger than x*100%. Typically, I suggest using TPrint 1E-8. Since contribution is calculated as square of configuration coefficient, TPrint 1E-8 simply corresponds to outputting configurations who have absolute value of coefficients larger than 1E-4, the effect is identical to IOp(9/40=4) in Gaussian. Below is an example input:


```text
! PBE0 def2-SVP
%tddft
nroots 8
tprint 1E-8
end
```

Spin-flip TDDFT output file of ORCA is also supported, you just need to add SF TRUE

into %tddft field and set spin multiplicity of reference state ≥ 3. Note that only a few functions, including generating natural orbitals of excited state, hole-electron analysis and related analyses, are formally supported, other functions were not tested. In particular, all analyses directly based on transition density matrix (including NTO analysis) are not supported in this case.

- ORCA users using TDDFT: Because coefficients of excitation and de-excitation configurations are not recorded explicitly in output file, in this case, not only TDDFT output file is needed, but also a json file recording all configuration coefficients is needed. After running a typical TDDFT input file named e.g. TDDFT.inp, you will have TDDFT.gbw in current folder. Then you should create a text file named TDDFT.json.conf with the following content.


```text
{
"CIS": true,
```


<!-- p.260 -->


```text
"CISNRoots": true
}
```

Then run orca_2json TDDFT.gbw, you will have TDDFT.json in current folder. After that, when Multiwfn attempts to load the TDDFT.out you inputted during an analysis, if the file with the same name and folder but with .json suffix (i.e. TDDFT.json), the excitation and de-excitation configurations will be automatically loaded from TDDFT.json instead. If you are still confused, please read my blog article http://sobereva.com/758 (in Chinese), which described how to prepare files and run a typical analysis using Multiwfn in combination with TDDFT calculation of ORCA.

- ORCA users using sTDA or sTDDFT: They are approximations of regular TDA and TDDFT, respectively, and their output file can be used. In ORCA, their calculations are based on DFT MOs; once the single point task of DFT has finished, the excited states will be calculated by sTDA/sTDDFT with negligible cost. To carry out these calculations, use keywords like follows (see ORCA manual for details)


```text
! wB97X-D3 def2-SV(P) def2/J RIJCOSX
%tddft
Mode sTDDFT    //The sTDDFT may also be changed to sTDA
Ethresh 7.0
PThresh 1e-4
PTLimit 30
maxcore 6000
end
```

It is important to note that only the three largest configuration coefficients are printed during the calculation (unfortunately, TPrint does not work for sTDA/sTDDFT calculation), therefore often the normalization condition of configuration coefficients is violated evidently, in this case the analysis result is unreliable or even fully misleading! So, please take care of the "Deviation to expected normalization value" shown on screen after loading selected excited state.

- BDF users: Output file of TDDFT task of BDF program can be used.

- CP2K users: Periodic TDDFT (with/without sTDA kernel) task of CP2K is supported. Currently, only hole-electron analysis, NTO analysis, “Generate natural orbitals of specific excited states “, “Check, modify and export configuration coefficients of an excitation” and “Print major MO transitions in all excited states” are formally supported, other analyses may or may not work (at least I have not tested).

After booting up Multiwfn, the .molden file containing all virtual orbitals and cell information should be loaded. Then, after you enter an analysis module, output file of CP2K should be loaded.

It is noteworthy that using Multiwfn to prepare input file of TDDFT task of CP2K is quite easy. After booting up Multiwfn, load a structure file first (for crystal, often .cif is used, see Section 2.9.3 for detail), then input cp2k and the path of the input file to export. After that, you may first enter option -11 and then suboption 19 to extend the current cell to a supercell if needed. Then return to the interface of creating CP2K input file, choose option 15 to enable TDDFT calculation, then input y to allow CP2K to generate the .molden file containing all orbitals and specify how many virtual orbitals to solve and record in the .molden file. Finally, choose option 0 to yield CP2K input file. Then use CP2K to run the input file, after the calculation is finished, manually insert cell information


<!-- p.261 -->

to .molden file (as mentioned in Section 2.9.2.1). Now the .molden file and output file can be used for electron excitation analyses.

Note that the virtual orbitals recorded in .molden file should cover all virtual orbitals involved in the printed configurations. If you do not know how many virtual orbitals should be calculated, simply set it to a very large value so that all virtual orbitals will be solved and recorded, however in this case the .molden file may be quite large. You can also perform TDDFT once, then check the printed configurations and find the highest virtual orbital, then properly set the number of virtual orbitals to solve in the input file and redo a single point calculation to generate the .molden file.

- General cases: You can also use plain text file as the input file. The format of transition information should be completely identical to Gaussian output, for instance: (the // and all text after it should not appear in your file)


```text
Excited State   1   1   5.7945    // Label, index, multiplicity and excitation energy (eV)
       5 ->  6         0.70642    // MO pairs and configuration coefficients
                                  // Use a blank line to separate each excited state
Excited State   2   1   7.8943
       5 ->  7         0.63860
       5 ->  8         0.30006

Excited State   3   1   7.8943
       5 ->  7        -0.30006
       5 ->  8         0.63860
       4 <-  8         0.01000
```

Example of unrestricted TDDFT calculation is given below. Note that spin multiplicity is set to 0, meaning undefined, since the excited states produced by this kind of calculation are not pure spin states.


```text
Excited State   1      0     2.07774
       600B -> 601B        -0.676085
       598A -> 602A         0.454805
       600A -> 603A         0.416875
...ignored

 Excited State   2      0     2.07792
       599B -> 601B         0.561757
       598A -> 601A         0.496762
       600B -> 603B         0.468381
...ignored
```

Evidently, the above-mentioned two kinds of files must correspond to the same geometry and same calculation level. For example, if the MOs in the .fch were produced at B3LYP/6-31G* level while the Gaussian output file corresponds to the TDDFT task carried out at PBE0/6-31G* level, the analysis results will be completely meaningless.

NOTE 1: For closed-shell reference case, the coefficients in the plain text file should follow convention of Gaussian, namely the sum of square of all coefficients should be 0.5 (rather than normalize to 1.0).

NOTE 2: The MO indices in the plain text file provided to Multiwfn should start from 1. However, in some programs like ORCA, the MO indices start from 0, so their users need to manually add the MO indices in by 1 when preparing the plain text file.


<!-- p.262 -->

- Special case for GAMESS-US and Firefly users: If you are a user of Firefly or GAMESS-US program, you do not need to separately provide two kinds of files as mentioned above for electron excitation analysis. If the input file used for Multiwfn is TDDFT output file with .gms suffix, the Multiwfn will not only load basis function and molecular orbital information from this file when Multiwfn boots up, but also load configuration coefficients of excited states when performing electron excitation analysis. The H2CO_TDDFT_Firefly.gms and H2CO_TDDFT_GAMESS.gms in "examples\excit\" folder are example file of TDDFT output file of Firefly and GAMESS-US, respectively.

For Firefly user, you should decrease the "PRTTOL" parameter in $TDDFT so that more configuration coefficients could be printed.

For GAMESS-US, there is no option used to control the printing threshold of configuration coefficients, therefore some analysis results may not be very accurate because some configurations, which have non-negligible contributions, may be ignored. In addition, CIS task of GAMESS-US is not supported by Multiwfn.

Output files of excited state optimization and frequency tasks of GAMESS-US and Firefly are not supported.


### 3.21.0 Check, modify and export configuration coefficients of an excitation (-1)



This function allows one to check, modify and export configuration coefficients. The input files needed by this function have been detailedly described at the beginning of Section 3.21, namely you should load a file containing basis function information when Multiwfn boots up, then load a file containing configuration coefficients of excited states. The summary of all recognized excited states will be printed on screen, you should select one of them, the configuration coefficients of orbital pairs involved in this electron excitation will be loaded. After that, up to 10 orbital pairs that have largest absolute contribution to the excitation are automatically shown. Then in the newly appeared menu, you can find below options:

1 Set coefficient of an orbital pair: You can use this option to replace the loaded configuration coefficients of an orbital pair with inputted value.

2 Set coefficient for specific range of orbital pairs: This option is used to replace a batch of loaded configuration coefficients with inputted values. You should input index range of the occupied MOs and virtual MOs corresponding to the orbital transitions.

After manually modifying coefficients using above two options, in order to make the modification affect following electron excitation analysis, you should use option -3 to export the modified coefficients as plain text file, and then use this file as the second kind of input file for electron excitation analyses.

-1 Retrieve original coefficient of all orbital pairs: If configuration coefficients have been manually modified by above two options, you can select this option to retrieve the coefficients to the original loaded values.

-2 Print coefficient (and contribution to excitation) of some orbital pairs: You can use this option to print configuration coefficients whose absolute value are larger than specific value, meantime the corresponding contributions to the electron excitation are shown together. Via this


<!-- p.263 -->

option you can easily find out which orbital pair transition has crucial contribution to the electron excitation.

-3 Export current excitation information to a plain text file: Basic information and configuration coefficients of currently selected excited state can be exported to a specific plain text file. This file can then be employed as the second kind of input file for various electron excitation analysis functions of Multiwfn, e.g. hole-electron analysis and NTO analysis, and then the analysis result will correspond to the modified configuration coefficients.

Obviously, if you set coefficient of some orbital pairs to zero, then their contributions to the quantities you studied will be completely ignored; while if you have cleaned all coefficients except for a specific orbital pair, then the resulting quantities will only reveal characters of this orbital transition.

The example given in Section 4.18.10 utilized this function.


### 3.21.1 Analyze and visualize hole&electron distribution, transition density, and transition electric/magnetic dipole moment density (1)



This very powerful module is used to analyze and visualize hole-electron distribution, transition density and transition electric/magnetic dipole moment density. Moreover, hole and electron can be decomposed to orbital pair contributions as well as atom and fragment contributions; furthermore, the atom/fragment contributions can be directly plotted as heat map for visual inspection.

3.21.1.1 Theory

There are many knowledge points involved in this module, they will be described below first.

Theory 1: Real space representation of hole and electron Process of single-electron excitation can be described as "an electron leaves hole and goes to electron", the "hole" and "electron" can be defined in different ways. If an excitation can be perfectly

described as HOMO→LUMO transition, then hole and electron could be simply represented by HOMO and LUMO, respectively. However, in most practical cases, the single orbital pair representation is not suitable, excitations have to be represented as transition of multiple MO pairs with corresponding weighting coefficients.

How to represent hole and electron distributions when there is no single dominant MO pair transition? One way is using natural transition orbital (NTO) analysis, as introduced in Section 3.21.6. Unfortunately, in many cases, even though the MOs have been transformed to NTOs, there is still no single NTO pair that has dominating contribution. The best representation of hole and electron should be the one introduced in this Section, the idea was originally proposed by me and my collaborator Cheng Zhong in 2013. Although the paper detailedly introducing this method has not been published, if this theory is involved in your study, please cite my work: Carbon, 165, 461-467 (2020) DOI: 10.1016/j.carbon.2020.05.023, in which hole-electron analysis is utilized and briefly described.

It can be shown that density distribution of hole and electron can be perfectly defined as


<!-- p.264 -->

$$\rho^{\mathrm{hole}}(\mathbf{r})=\rho_{(\mathrm{loc})}^{\mathrm{hole}}(\mathbf{r})+\rho_{(\mathrm{cross})}^{\mathrm{hole}}(\mathbf{r})=\sum_{i\rightarrow a}(w_{i}^{a})^{2}\varphi_{i}(\mathbf{r})\varphi_{i}(\mathbf{r})+\sum_{i\rightarrow a}\sum_{j\neq i\rightarrow a}w_{i}^{a}w_{j}^{a}\varphi_{i}(\mathbf{r})\varphi_{j}(\mathbf{r})$$

note that the notions used here:

$$\sum_{i\to a}\equiv\sum_{i}^{\mathrm{o c c}}\sum_{a}^{\mathrm{v i r}}\qquad\sum_{i\to a}\sum_{j\neq i\to a}\equiv\sum_{i}^{\mathrm{o c c}}\sum_{j\neq i}^{\mathrm{o c c}}\sum_{a}^{\mathrm{v i r}}$$

where φ denotes MO wavefunction. "loc" and "cross" stand for the contribution of local term and cross term to the hole and electron distribution, respectively. Note that the definition of hole and electron given above is in density form rather than wavefunction form, hence the hole and electron do not have phase (If you really need phase information of hole and electron, you should resort on NTO analysis, see Section 3.21.6).

Due to the orthonormality of MOs and the fact that the sum of square of all configuration coefficients is 1.0, it is clear that


$$\int\rho^{\mathrm{h o l e}}(\mathbf{r})\mathrm{d}\mathbf{r}=1\quad\int\rho^{\mathrm{e l e}}(\mathbf{r})\mathrm{d}\mathbf{r}=1$$

<!-- formula-ocr: formula_p264_162.png 已替换为LaTeX, 原图保留备查 -->

This is an important property that any reasonable definition of hole and electron distribution should satisfy, it indicates that one electron is excited.

The overlap function between hole and electron distribution can be defined as


$$\rho^{\mathrm{excited}}(\mathbf{r})=\rho^{\mathrm{ground}}(\mathbf{r})-\rho^{\mathrm{hole}}(\mathbf{r})+\rho^{\mathrm{ele}}(\mathbf{r})$$

<!-- formula-ocr: formula_p264_163.png 已替换为LaTeX, 原图保留备查 -->

namely taking the minimal value of ρhole and ρele everywhere. Another function for measuring the overlap is


$$S_{\mathrm{m}}(\mathbf{r})=\min[\rho^{\mathrm{hole}}(\mathbf{r}),\rho^{\mathrm{ele}}(\mathbf{r})]$$

<!-- formula-ocr: formula_p264_164.png 已替换为LaTeX, 原图保留备查 -->

It is evident that $S_{r}$ is always equal or larger than Sm. Both the two definitions are reasonable, but I prefer to use Sr, since its graphical effect is better and its mathematical meaning is clearer.

The charge density difference (CDD) between excited state and ground state can be easily evaluated as


$$S_{\mathrm{r}}(\mathbf{r})=\sqrt{\rho^{\mathrm{hole}}(\mathbf{r})\rho^{\mathrm{ele}}(\mathbf{r})}$$

<!-- formula-ocr: formula_p264_165.png 已替换为LaTeX, 原图保留备查 -->

NOTE: Beware that if you are a Gaussian user, the Δρ calculated in this way is obviously different to the Δρ produced via subtracting excited state density by ground state density, unless you specified keyword density=rhoci when generating .wfn/wfx file of excited state. Because by default the excited state density exported to .wfn/wfx file by Gaussian is relaxed density rather than unrelaxed density (which is directly constructed by MOs and excited state configuration coefficients). In other

words, unrelaxed excited state density can be simply written as $\rho^{\mathrm{excited}}(\mathbf{r})=\rho^{\mathrm{ground}}(\mathbf{r})-\rho^{\mathrm{hole}}(\mathbf{r})+\rho^{\mathrm{ele}}(\mathbf{r})$𝜌hole(𝐫) + 𝜌ele(𝐫) , while deriving relaxed excited state density requires employing the very complicated "Z-vector" method.

After generalization, above definitions of hole and electron can also be applied to TDHF and TDDFT cases, where de-excitations must be taken into account. The generalized local terms are


<!-- p.265 -->

$$\rho_{(\mathrm{loc})}^{\mathrm{hole}}=\sum_{i\rightarrow a}(w_{i}^{a})^{2}\rho_{i}-\sum_{i\leftarrow a}(w_{i}^{\prime a})^{2}\rho_{i}$$

where ρi=|φi|2 stands for electron density of orbital i, w' denotes configuration coefficient of de-excitation. The generalized cross terms are

$$\begin{array}{r l}&{\rho_{\mathrm{(c r o s s)}}^{\mathrm{h o l e}}=\displaystyle\sum_{i\to a}\displaystyle\sum_{j\neq i\to a}w_{i}^{a}w_{j}^{a}\varphi_{i}\varphi_{j}-\displaystyle\sum_{i\leftarrow a}\displaystyle\sum_{j\neq i\leftarrow a}w_{i}^{\prime a}w_{j}^{\prime a}\varphi_{i}\varphi_{j}}\end{array}$$

$$\begin{array}{r l}&{\rho_{\mathrm{(c r o s s)}}^{\mathrm{h o l e}}=\displaystyle\sum_{i\to a}\displaystyle\sum_{j\neq i\to a}w_{i}^{a}w_{j}^{a}\varphi_{i}\varphi_{j}-\displaystyle\sum_{i\leftarrow a}\displaystyle\sum_{j\neq i\leftarrow a}w_{i}^{\prime a}w_{j}^{\prime a}\varphi_{i}\varphi_{j}}\end{array}$$

$$\begin{array}{r l}&{\rho_{\mathrm{(c r o s s)}}^{\mathrm{h o l e}}=\displaystyle\sum_{i\to a}\displaystyle\sum_{j\neq i\to a}w_{i}^{a}w_{j}^{a}\varphi_{i}\varphi_{j}-\displaystyle\sum_{i\leftarrow a}\displaystyle\sum_{j\neq i\leftarrow a}w_{i}^{\prime a}w_{j}^{\prime a}\varphi_{i}\varphi_{j}}\end{array}$$

$$\rho_{(\mathrm{c r o s s})}^{\mathrm{e l e}}=\sum_{i\rightarrow a i\rightarrow b\neq a}w_{i}^{a}w_{i}^{b}\varphi_{a}\varphi_{b}-\sum_{i\leftarrow a i\leftarrow b\neq a}w_{i}^{\prime a}w_{i}^{\prime b}\varphi_{a}\varphi_{b}$$

Theory 2: Contribution of MOs, basis functions, atoms and fragments to hole and electron distributions

In order to investigate which MOs have significant contributions to hole and electron, I defined the contribution of occupied MO to hole and contribution of virtual MO to electron as follows

$$\rho_{(\mathrm{loc})}^{\mathrm{hole}}=\sum_{i\rightarrow a}(w_{i}^{a})^{2}\rho_{i}-\sum_{i\leftarrow a}(w_{i}^{\prime a})^{2}\rho_{i}$$

Below normalization conditions are held evidently:


$$\rho_{(\mathrm{loc})}^{\mathrm{hole}}=\sum_{i\rightarrow a}(w_{i}^{a})^{2}\rho_{i}-\sum_{i\leftarrow a}(w_{i}^{\prime a})^{2}\rho_{i}$$

<!-- formula-ocr: formula_p265_166.png 已替换为LaTeX, 原图保留备查 -->

Contribution to hole/electron by an atom can be easily evaluated using real space partition like Hirshfeld, Hirshfeld-I and Becke. For example, contribution to hole by atom A using Hirshfeld partition:

$$\Theta_{A}^{\mathrm{h o l e}}=\int w_{A}^{\mathrm{H i r s h}}(\mathbf{r})\rho^{\mathrm{h o l e}}(\mathbf{r})\mathrm{d}\mathbf{r}$$

Hirsh is weighting function of atom A under Hirshfeld partition, see Section 3.9.1 for its detail. where 𝑤𝐴

Mulliken-like partition is also possible, and the working equation is derived as follows. Considering the normalization condition of the hole (de-excitation part is temporarily ignored for simplicity)


<!-- p.266 -->


$$\int\left(\sum_{i,j\rightarrow a}w_{i}^{a}w_{j}^{a}\sum_{\mu}\sum_{\nu}C_{\mu,i}C_{\nu,j}\chi_{\mu}\chi_{\nu}\right)\mathrm{d}\mathbf{r}=1$$

<!-- formula-ocr: formula_p266_167.png 已替换为LaTeX, 原图保留备查 -->

where χ denotes basis function, S and C are overlap matrix and coefficient matrix, respectively. If

$$\Theta_{A}^{\mathrm{h o l e}}=\sum_{i,j\rightarrow a}w_{i}^{a}w_{j}^{a}\frac{1}{2}\Biggl(\sum_{\mu\in A}\sum_{\nu}C_{\mu,i}C_{\nu,j}S_{\mu,\nu}+\sum_{\mu}\sum_{\nu\in A}C_{\mu,i}C_{\nu,j}S_{\mu,\nu}\Biggr)$$

then we can define contribution of atom A to hole in below form

$$\Theta_{A}^{\mathrm{h o l e}}=\sum_{i,j\rightarrow a}w_{i}^{a}w_{j}^{a}\frac{1}{2}\Biggl(\sum_{\mu\in A}\sum_{\nu}C_{\mu,i}C_{\nu,j}S_{\mu,\nu}+\sum_{\mu}\sum_{\nu\in A}C_{\mu,i}C_{\nu,j}S_{\mu,\nu}\Biggr)$$

Above treatment can be similarly applied to de-excitation part of hole as well as electron. The actual working equations used to evaluate atomic contribution to hole and electron are

$$\Theta_{A}^{\mathrm{h o l e}}=\sum_{i,j\rightarrow a}w_{i}^{a}w_{j}^{a}\frac{1}{2}\Biggl(\sum_{\mu\in A}\sum_{\nu}T_{\mu,\nu}^{i j}+\sum_{\mu}\sum_{\nu\in A}T_{\mu,\nu}^{i j}\Biggr)-\sum_{i,j\leftarrow a}w_{i}^{\prime a}w_{j}^{\prime a}\frac{1}{2}\Biggl(\sum_{\mu\in A}\sum_{\nu}T_{\mu,\nu}^{i j}+\sum_{\mu}\sum_{\nu\in A}T_{\mu,\nu}^{i j}\Biggr)$$

$$\Theta_{A}^{\mathrm{c l e}}=\sum_{i\rightarrow a,b}w_{i}^{a}w_{i}^{b}\frac{1}{2}\Biggl(\sum_{\mu\in A}\sum_{\nu}T_{\mu,\nu}^{a b}+\sum_{\mu}\sum_{\nu\in A}T_{\mu,\nu}^{a b}\Biggr)-\sum_{i\leftarrow a,b}w_{i}^{\prime a}w_{i}^{\prime b}\frac{1}{2}\Biggl(\sum_{\mu\in A}\sum_{\nu}T_{\mu,\nu}^{a b}+\sum_{\mu}\sum_{\nu\in A}T_{\mu,\nu}^{a b}\Biggr)$$

$$\Theta_{A}^{\mathrm{h o l e}}=\sum_{i,j\rightarrow a}w_{i}^{a}w_{j}^{a}\frac{1}{2}\Biggl(\sum_{\mu\in A}\sum_{\nu}C_{\mu,i}C_{\nu,j}S_{\mu,\nu}+\sum_{\mu}\sum_{\nu\in A}C_{\mu,i}C_{\nu,j}S_{\mu,\nu}\Biggr)$$

Contribution of a basis functions μ to hole and electron can be defined as

$$\Theta_{A}^{\mathrm{h o l e}}=\sum_{i,j\rightarrow a}w_{i}^{a}w_{j}^{a}\frac{1}{2}\Biggl(\sum_{\mu\in A}\sum_{\nu}T_{\mu,\nu}^{i j}+\sum_{\mu}\sum_{\nu\in A}T_{\mu,\nu}^{i j}\Biggr)-\sum_{i,j\leftarrow a}w_{i}^{\prime a}w_{j}^{\prime a}\frac{1}{2}\Biggl(\sum_{\mu\in A}\sum_{\nu}T_{\mu,\nu}^{i j}+\sum_{\mu}\sum_{\nu\in A}T_{\mu,\nu}^{i j}\Biggr)$$

$$\Theta_{A}^{\mathrm{c l e}}=\sum_{i\rightarrow a,b}w_{i}^{a}w_{i}^{b}\frac{1}{2}\Biggl(\sum_{\mu\in A}\sum_{\nu}T_{\mu,\nu}^{a b}+\sum_{\mu}\sum_{\nu\in A}T_{\mu,\nu}^{a b}\Biggr)-\sum_{i\leftarrow a,b}w_{i}^{\prime a}w_{i}^{\prime b}\frac{1}{2}\Biggl(\sum_{\mu\in A}\sum_{\nu}T_{\mu,\nu}^{a b}+\sum_{\mu}\sum_{\nu\in A}T_{\mu,\nu}^{a b}\Biggr)$$

In order to significantly save computational time, Multiwfn ignores all terms if magnitude of product of corresponding two configuration coefficients is less than 0.001. The loss of accuracy due to this trick is negligible.

For both Mulliken-like and Hirshfeld partitions, fragment contributions to hole and electron can be simply evaluated by summing up atomic contributions:

$$\Theta_{f r a g}^{\mathrm{h o l e}}=\sum_{A\in f r a g}\Theta_{A}^{\mathrm{h o l e}}\quad\Theta_{f r a g}^{\mathrm{e l e}}=\sum_{A\in f r a g}\Theta_{A}^{\mathrm{e l e}}$$

Furthermore, I defined contribution of atom and fragment to charge density difference (variation of electron population of the atom and fragment) as

$$\Theta_{A}^{\mathrm{C D D}}=\Theta_{A}^{\mathrm{e l e}}-\Theta_{A}^{\mathrm{h o l e}}\quad\Theta_{f r a g}^{\mathrm{C D D}}=\Theta_{f r a g}^{\mathrm{e l e}}-\Theta_{f r a g}^{\mathrm{h o l e}}$$

Overlap between hole and electron in atom and fragment spaces are defined as geometry


<!-- p.267 -->

average of their contributions:


$$\Theta_{A}^{\mathrm{o v l p}}=\sqrt{\Theta_{A}^{\mathrm{e l e}}\Theta_{A}^{\mathrm{h o l e}}}\quad\Theta_{f r a g}^{\mathrm{o v l p}}=\sqrt{\Theta_{f r a g}^{\mathrm{e l e}}\Theta_{f r a g}^{\mathrm{h o l e}}}$$

<!-- formula-ocr: formula_p267_168.png 已替换为LaTeX, 原图保留备查 -->

Notice that the overlap in this form is not additive, namely ABBAΘ≠Θ+Θ. ovlpovlpovlp

Mulliken-like partition works reasonably for most cases, however, it is incompatible with diffuse functions. Another well-known shortcoming of this partition is that some atomic contributions may be small negative values in certain situations, obviously in this case the overlap between hole and electron in corresponding atomic spaces cannot be evaluated, so Multiwfn automatically sets the overlap values to zero. Obviously, when diffuse functions must be employed (e.g. anionic system, Rydberg excited state), or you have observed notable negative atomic contribution to hole or electron, you have to change to Hirshfeld partition, which is more robust but computational cost is higher.

Mulliken-like and Hirshfeld partitions can be directly selected in hole-electron analysis module. Due to the extreme flexibility of Multiwfn, you may also use other ways to determine atomic contributions to hole and electron, such as Becke and Hirshfeld-I partitions. However, you have to manually evaluate them. For example, if you want to employ Becke partition for hole and electron, you should first export cube file of hole or electron, then set "iuserfunc" in `settings.ini` to -1 (in this case the user-defined function will correspond to the interpolated function based on the grid data), then load hole or electron cube file into Multiwfn, use subfunction 1 of main function 15 to integrate "user-defined function" in each Becke's atomic fuzzy space. Note that if in the main function 15, you first select option -4 to define a fragment and then use subfunction 1 to integrate user-defined function, then the sum of results of all atoms will correspond to the fragment contribution.

Theory 3: Quantitative characterization of hole and electron distribution in the whole space

The overall distribution of hole and electron can be quantitatively characterized in following ways, they are quite useful for identifying type of electron excitations.

To characterize overlapping extent of hole and electron, Sm index and Sr index are defined as follows (Sr must be equal or larger than Sm index)

$$S_{\mathrm{m}}\mathrm{index}=\int S_{\mathrm{m}}(\mathbf{r})\mathrm{d}\mathbf{r}\equiv\int\min[\rho^{\mathrm{hole}}(\mathbf{r}),\rho^{\mathrm{ele}}(\mathbf{r})]\mathrm{d}\mathbf{r}$$

Centroid can be calculated to reveal most representative position of hole and electron distribution. For example, X coordinate of centroid of electron is written as


$$S_{\mathrm{m}}\mathrm{index}=\int S_{\mathrm{m}}(\mathbf{r})\mathrm{d}\mathbf{r}\equiv\int\min[\rho^{\mathrm{hole}}(\mathbf{r}),\rho^{\mathrm{ele}}(\mathbf{r})]\mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p267_169.png 已替换为LaTeX, 原图保留备查 -->

where x is X component of position vector r.

The charge transfer (CT) length in X/Y/Z can be measured by distance between centroid of hole and electron in corresponding directions:


<!-- p.268 -->

xeleholeyeleholezeleholeDXXDYYDZZ=−=−=−

The total magnitude of CT length is referred to as D index:


$$D\operatorname{index}=|\mathbf{D}|\equiv\sqrt{(D_{x})^{2}+(D_{y})^{2}+(D_{z})^{2}}$$

<!-- formula-ocr: formula_p268_170.png 已替换为LaTeX, 原图保留备查 -->

It is noteworthy that the variation of dipole moment of excited state (corresponding to unrelaxed density) with respect to ground state in X, Y and Z can be simply calculated as

$$D_{\mathrm{x}}=\left|X_{\mathrm{ele}}-X_{\mathrm{hole}}\right|\quad D_{\mathrm{y}}=\left|Y_{\mathrm{ele}}-Y_{\mathrm{hole}}\right|\quad D_{\mathrm{z}}=\left|Z_{\mathrm{ele}}-Z_{\mathrm{hole}}\right|$$

The RMSD of hole and electron can be used to characterize their extent of spatial distribution. For example, X component of RMSD of hole is expressed as

$$\sigma_{\mathrm{hole,x}}=\sqrt{\int\left(x-X_{\mathrm{hole}}\right)^{2}\rho^{\mathrm{hole}}(\mathbf{r})\mathrm{d}\mathbf{r}}$$

The |σhole| and |σele| are referred to as σhole and σele indices, they measure overall RMSD of hole and electron, respectively.

The difference between RMSD of electron and hole in X/Y/Z direction can be measured via

$$H\operatorname{index}=\left(\left|\pmb{\sigma}_{\mathrm{c l c}}\right|+\left|\pmb{\sigma}_{\mathrm{h o l c}}\right|\right)/2$$

$$\Delta\sigma\ \mathrm{index}=\mid\pmb{\sigma}_{\mathrm{ele}}\mid-\mid\pmb{\sigma}_{\mathrm{hole}}\mid$$

$H_{\lambda}$ measures average degree of spatial extension of hole and electron distribution in X/Y/Z direction, HCT is that in CT direction, and H index is an overall measure

$$D_{\mathrm{x}}=\left|X_{\mathrm{ele}}-X_{\mathrm{hole}}\right|\quad D_{\mathrm{y}}=\left|Y_{\mathrm{ele}}-Y_{\mathrm{hole}}\right|\quad D_{\mathrm{z}}=\left|Z_{\mathrm{ele}}-Z_{\mathrm{hole}}\right|$$

H CTCT ·= || uH

H 2/|)||(|index += σσ holeele

where uCT is unit vector in CT direction and can be straightforwardly derived using centroid of hole and electron.

t index is designed to measure separation degree of hole and electron in CT direction:

CTindexindexHDt−=

If t index<0, it implies that hole and electron are not substantially separated due to CT. Clear separation of hole and electron distributions must correspond to evidently positive t index.

The hole delocalization index (HDI) and electron delocalization index (EDI) are defined as follows


$$\begin{aligned}&HDI=100\times\sqrt{\int[\rho^{hole}(\mathbf{r})]^{2}d\mathbf{r}}\\ &EDI=100\times\sqrt{\int[\rho^{ele}(\mathbf{r})]^{2}d\mathbf{r}}\\ \end{aligned}$$

<!-- formula-ocr: formula_p268_171.png 已替换为LaTeX, 原图保留备查 -->

It is found that the smaller the HDI (EDI), the larger the spatial delocalization of hole (electron); in


<!-- p.269 -->

other words, the more evenly distributed throughout the system. HDI and EDI are pretty useful in

quantifying breadth of spatial distribution (although |$|\boldsymbol{\sigma}_{\mathrm{hole}}|$| can also reveal this point, they are not suitable when hole or electron are concentrated in multiple areas).

There are often many nodes or complicated fluctuations in hole and electron distributions. In order to make visual study of hole and electron easier, Chole and Cele functions are defined as follows. The function behavior of Chole and Cele is similar to Gaussian function, they are highly smooth functions, the value asymptotically approaches zero from centroid of hole/electron.

$$C_{\mathrm{hole}}(\mathbf{r})=A_{\mathrm{hole}}\exp\left(-\frac{(x-X_{\mathrm{hole}})^{2}}{2\sigma_{\mathrm{hole,x}}^{2}}-\frac{(y-Y_{\mathrm{hole}})^{2}}{2\sigma_{\mathrm{hole,y}}^{2}}-\frac{(z-Z_{\mathrm{hole}})^{2}}{2\sigma_{\mathrm{hole,z}}^{2}}\right)$$

The factor A is introduced so that Chole and Cele are normalized.

In fact, the definition of RMSD, Chole, Cele, H and t indices introduced above was motivated by J. Chem. Theory Comput., 7, 2498 (2011), these quantities were originally used to analyze electron excitation based on density difference, but I found all of them work well under the framework of hole-electron analysis. Also note that many details of these indices have been modified when introduced to hole-electron analysis framework.

The above defined quantitative indices could be used for distinguishing type of electron excitation. My empirical rule is summarized as follows, it should be suitable for most cases.

In the table, three kinds of excitations are involved:

- Local excitation (LE): The hole and electron occupy similar spatial region.
- Charge-transfer excitation (CT): The spatial separation of hole and electron is large, leading to evident displacement of charge density. The CT may be single directional or multiple directional (centrosymmetric CT is a special case of the latter).

- Rydberg excitation: Electron mainly consists of very diffuse MOs, therefore the overlap between electron and hole must be small. This type of excitation in general does not lead to prominent long-range displacement of charge density.

Theory 4: Transition density matrix and transition density (One-electron, spinless) transition density matrix between excited state and ground state of an N-electron system in real space representation is defined as follows (real type of wavefunctions is assumed, so complex conjugation sign is omitted)

$$T(\mathbf{r};\mathbf{r}^{\prime})\equiv T(\mathbf{r}_{1};\mathbf{r}_{1}^{\prime})=\int\Phi^{0}(\mathbf{x}_{1},\mathbf{x}_{2},\cdots\mathbf{x}_{N})\Psi^{\mathrm{e x c}}(\mathbf{x}_{1}^{\prime},\mathbf{x}_{2},\cdots\mathbf{x}_{N})\mathrm{d}\sigma_{1}\mathrm{d}\mathbf{x}_{2}\mathrm{d}\mathbf{x}_{3}\cdots\mathrm{d}\mathbf{x}_{N}$$


| Excitation type | Index |  |  |  |
| --- | --- | --- | --- | --- |
|  | D | S<br/>r | t | ∆σ |
| LE | small | medium ~ large | <0 | small |
| Single direction CT | large | ? | ? | ? |
| Centrosymmetric CT | small | ? | <0 | large |
| Rydberg | small | Small | <0 | large |

<!-- p.270 -->

where Φ0 is Slater-determinant of ground state wavefunction. x is spin-space coordinate, σ stands for spin coordinate. The T is referred to as a matrix because it has two continuous indices.

For excited state wavefunction generated by single-reference methods, after expanding $\Psi^{exc}$ and applying Slater-Condon rule, it can be easily shown that T can be explicitly written as


$$T(\mathbf{r};\mathbf{r}^{\prime})=\sum_{i}\sum_{a}w_{i}^{a}\varphi_{i}(\mathbf{r})\varphi_{a}(\mathbf{r}^{\prime})$$

<!-- formula-ocr: formula_p270_172.png 已替换为LaTeX, 原图保留备查 -->

If we only take the diagonal terms of the transition density matrix, then we obtain transition density


$$T(\mathbf{r})=\sum_{i}\sum_{a}w_{i}^{a}\varphi_{i}(\mathbf{r})\varphi_{a}(\mathbf{r})$$

<!-- formula-ocr: formula_p270_173.png 已替换为LaTeX, 原图保留备查 -->

T(r) can be studied as a common real space function, for example, visualized in terms of isosurface

map. Assuming that there is only one dominant orbital transition, for example, HOMO→LUMO, then T(r) is simply φHOMO(r)φLUMO(r). Therefore, it is easy to understand, if a region has large magnitude of transition density, the hole and electron must be strongly coupled in this region; while if a region has small distribution of T(r), then overlap between hole and electron in this area should be insignificant. Clearly, T(r) is a useful function for characterizing underlying nature of electron excitation, and its main distribution characteristics are closely related to the Sr(r) function.

Note that due to the orthonormality of MOs, integral of T(r) over the whole space is exactly zero. If the excited state and ground state correspond to different spin states, due to the orthonormality of spin coordinate, T(r;r') must be a zero matrix, and T(r) is correspondingly zero everywhere. However, notice that only spatial part of T(r) is taken into account when Multiwfn

evaluates it, therefore you are still able to study T(r) for e.g. S0→T1 excitation.

Theory 5: Transition electric/magnetic dipole moment density Note that there are many kinds of transition dipole moment, including transition electric dipole moment, transition magnetic dipole moment, transition velocity dipole moment and so on. The word "transition dipole moment" commonly refers to transition electric dipole moment.

X, Y and Z components of transition electric dipole moment density can be written as negative of product of X, Y and Z coordinate variables and transition density, respectively:

)()()()()()(zyxrrrrrrzTTyTTxTT−=−=−=

Integrating transition electric dipole moment density over the whole space yields transition dipole moment D

$$D_{x}=\int T_{x}(\mathbf{r})\mathrm{d}\mathbf{r}\qquad D_{y}=\int T_{y}(\mathbf{r})\mathrm{d}\mathbf{r}\qquad D_{z}=\int T_{z}(\mathbf{r})\mathrm{d}\mathbf{r}$$

Obviously, one can conveniently study contribution to transition electric dipole moment of various molecular regions by plotting transition electric dipole moment density.

Next, we look at transition magnetic dipole moment. The operator for magnetic dipole moment due to movement of electrons is the angular momentum operator L (see e.g. Theor. Chim. Acta, 6, 341 (1966))

Lrijk xyzˆˆˆˆ() = −×∇=++ iLLL


$$\begin{aligned}&\hat{\mathbf{L}}=-i\left(\mathbf{r}\times\nabla\right)=\hat{\mathbf{i}}L_{\mathrm{x}}+\hat{\mathbf{j}}L_{\mathrm{y}}+\hat{\mathbf{k}}L_{\mathrm{z}}\\&=-i\left[\hat{\mathbf{i}}\left(y\frac{\partial}{\partial z}-z\frac{\partial}{\partial y}\right)+\hat{\mathbf{j}}\left(z\frac{\partial}{\partial x}-x\frac{\partial}{\partial z}\right)+\hat{\mathbf{k}}\left(x\frac{\partial}{\partial y}-y\frac{\partial}{\partial x}\right)\right]\\ \end{aligned}$$

<!-- formula-ocr: formula_p270_174.png 已替换为LaTeX, 原图保留备查 -->


<!-- p.271 -->

where i, j, k are unity vectors in X, Y and Z directions, respectively. Therefore, the X component of transition magnetic dipole moment can be explicitly defined as below. In order to get real value, the imaginary and negative signs are dropped; the symbol "←" denotes de-excitation MO pairs in TDHF/TDDFT formalism.

$$M_{x}=\left\langle\Phi^{0}\Big|y\frac{\partial}{\partial z}-z\frac{\partial}{\partial y}\Big|\Psi^{\mathrm{e x c}}\right\rangle=\sum_{i\rightarrow a}w_{i}^{a}\left\langle\varphi_{i}\Big|y\frac{\partial}{\partial z}-z\frac{\partial}{\partial y}\Big|\varphi_{a}\right\rangle-\sum_{j\leftarrow b}w_{j}^{\prime b}\left\langle\varphi_{j}\Big|y\frac{\partial}{\partial z}-z\frac{\partial}{\partial y}\Big|\varphi_{b}\right\rangle$$

My and Mz can be defined similarly. Notice that to convert the transition magnetic dipole moment

given above (also that outputted by Multiwfn) to the more common definition, 1 2 𝑖⟨𝜓𝑖|𝐫× 𝛁|𝜓𝑗⟩, it

should be manually divided by 2.

We can define transition magnetic dipole moment density component mi(r) by considering the

relationship ( )d, ,iiMmix y z==∫rr , so that distribution of transition magnetic dipole

moment can be visualized in terms of e.g. isosurface map. Explicit expression of $m_{i}(\mathbf{r})$ component is given below, Y and Z components can be defined similarly.

$$m_{\mathrm{x}}(\mathbf{r})=\sum_{i\rightarrow a}w_{i}^{a}\varphi_{i}(\mathbf{r})\Bigg[y\frac{\partial\varphi_{a}}{\partial z}(\mathbf{r})-z\frac{\partial\varphi_{a}}{\partial y}(\mathbf{r})\Bigg]-\sum_{j\leftarrow b}w_{j}^{\prime b}\varphi_{j}(\mathbf{r})\Bigg[y\frac{\partial\varphi_{b}}{\partial z}(\mathbf{r})-z\frac{\partial\varphi_{b}}{\partial y}(\mathbf{r})\Bigg]$$

Theory 6: Coulomb attraction between hole and electron (exciton binding energy) The "electron" of course carries negative charge, while "hole" can be regarded as carrying positive charge, therefore formally there is a Coulomb attractive energy between them, its negative value is known as exciton binding energy, which is a positive value. This term can be calculated via simple Coulomb formula (in atomic unit form):


$$E_{\mathrm{C}}=\iint\frac{\rho^{\mathrm{hole}}(\mathbf{r}_{1})\rho^{\mathrm{ele}}(\mathbf{r}_{2})}{|\mathbf{r}_{1}-\mathbf{r}_{2}|}\mathrm{d}\mathbf{r}_{1}\mathrm{d}\mathbf{r}_{2}$$

Some discussions about the exciton binding energy can be found in e.g. J. Chem. Phys., 143, 244905 (2015) and J. Phys. Chem. C, 121, 17088 (2017).

Note that the exciton binding energy calculated in above form is different to the exciton binding energy defined in another form, namely $E_{\mathrm{C}}=(\mathrm{IP}-\mathrm{EA})-E_{\mathrm{optical~gap}}$=(IP-EA)-Eoptical gap (see Mater. Horiz., 1, 17 (2014) for more details), because electronic correlation and orbital relaxation effects are involved in practical electron ionization and electron affinity processes; moreover, in fact there is an exchange term in EC (though it is negligible when separation of hole and electron is significant). All of these factors are ignored in the evaluation of exciton binding energy in Multiwfn.

In Multiwfn, above integral is directly calculated based on evenly distributed grid data of hole and electron. Notice that although the code has been substantially optimized and parallelized, the computational cost is still high, therefore you need to wait patiently during calculation. The cost is formally proportionally to square of the number of grids; therefore, the cost of medium-quality grid will be higher than low-quality grid by one order of magnitude.

3.21.1.2 Usage and Functions

The input files needed by present module have been detailedly described at the beginning of Section 3.21, namely you should load a file containing basis function information when Multiwfn boots up, and then load a file containing configuration coefficient information of excited states. The summary of recognized excited states will be printed on screen, you should select the excited state


<!-- p.272 -->

that you want to carry out aforementioned analyses. Each time only one state can be analyzed, if you want to analyze another state, you should exit this function, then enter again and select another state.

Present module has many functions, they will be described below in turn.

Function 1: Visualize and analyze hole, electron and transition density and so on After you enter this function, you are requested to set up grid data, then grid data will be calculated for hole distribution, electron distribution, overlap of hole and electron, transition density, transition electric/magnetic dipole moment density, charge density difference and $C_{ele}/C_{hole}$ functions.

After calculation of grid data is finished, various quantities introduced in Section 3.21.1.1 will be evaluated based on the evenly distributed grid data and then shown on screen, their meanings should be very easy to understand. The outputted transition electric/magnetic dipole moment is calculated by integrating grid data of transition dipole moment density, the value should be very close to the one directly outputted by quantum chemistry program. The ideal value of the integral of hole or electron over the whole space is 1.0, while for transition density the ideal value is 0. If the actual outputted values deviate too far from expected values, then the printed t index, H index, D index, Sm index and so on may be unreliable. There are three reasons that may lead to this problem:

(1) The grid quality is too poor. Higher number of grid points should be used (2) The spatial extent of the grid data is too narrow, you should enlarge extension distance so that the grid data could cover broader regions

(3) You forgot to use the IOp(9/40=x) option mentioned at the beginning of Section 3.21, as a result, only very small number of configuration coefficients are loaded

In post-processing menu, grid data of hole, electron, transition density, $S_{m}$ and so on can be directly visualized as isosurface map, or be exported as cube file in current folder by corresponding options. You can also choose corresponding option to calculate Coulomb attractive energy between hole and electron distribution, notice that this calculation is expensive even if you only choose low-quality grid.

By default, the transition magnetic dipole moment density is not evaluated because it is less important than the transition electric dipole moment density. If you want to calculate it, select option -1 before entering this function.

For large systems, if computational cost for grid data is too high and you only need to qualitatively examine isosurface map of hole, electron, transition density and so on, in Gaussian you can safely use IOp(9/40=3) instead of IOp(9/40=4), so that smaller number of configurations will be taken into account.

Function 2: Show molecular orbital contribution to hole and electron distribution You only need to input printing threshold, then contribution of MO to hole and electron distribution will be shown. This function is very useful to identify which MOs have significant contribution to hole and electron. Below is an output example:


```text
 MO     126, Occ:   2.00000    Hole:  0.29664     Electron:  0.00000
 MO     127, Occ:   2.00000    Hole:  0.19783     Electron:  0.00000
 MO     128, Occ:   2.00000    Hole:  0.38666     Electron:  0.00000
 MO     130, Occ:   0.00000    Hole:  0.00000     Electron:  0.08058
```


<!-- p.273 -->


```text
 MO     132, Occ:   0.00000    Hole:  0.00000     Electron:  0.16703
 MO     133, Occ:   0.00000    Hole:  0.00000     Electron:  0.22976
 Sum of hole:  1.00000    Sum of electron:  1.00000
```

Function 3: Show atom or fragment contribution to hole and electron and plot the contributions as heat map

After you enter this function, many quantities mentioned in "Theory 2" of Section 3.21.1.1 will be printed on screen, below is an output example. Mulliken type of partition is used to derive the atomic contributions.


```text
Contribution of each non-hydrogen atom to hole and electron:
    1(C )  Hole:  1.37 %  Electron:  8.96 %  Overlap:  3.50 %  Diff.:   7.59 %
    2(C )  Hole: 11.86 %  Electron:  0.74 %  Overlap:  2.97 %  Diff.: -11.11 %
    3(C )  Hole:  8.96 %  Electron: 11.00 %  Overlap:  9.93 %  Diff.:   2.04 %
...[ignored]
   14(N )  Hole:  0.18 %  Electron: 23.80 %  Overlap:  2.07 %  Diff.:  23.62 %
   15(O )  Hole:  3.07 %  Electron: 17.23 %  Overlap:  7.28 %  Diff.:  14.16 %
   16(O )  Hole:  3.07 %  Electron: 17.23 %  Overlap:  7.28 %  Diff.:  14.16 %
```

In the output, the "Overlap" is simply the geometry average of "Hole" and "Electron", while "Diff." is obtained by subtracting "Hole" from "Electron". Since hydrogens commonly do not participate in electron excitations of interest, by default hydrogens are ignored, but you can choose "Toggle if taking hydrogens into account" option to switch status.

If you need contribution of molecular fragments to above-mentioned quantities, you can select option "-1 Load fragment definition" and then input the number of fragments and atomic index of each fragment in turn. Fragment definition can also be loaded from an external plain text file, in which each fragment occupies a line, for example


```text
1,3,6-10,12
2,4,5
11
13-15
```

This example totally defines four fragments, the first fragment consists of atoms 1,3,6,7,8,9,10,12. Once defining fragments is completed, contribution of the fragments to various quantities will be immediately printed on screen.

Composition of atom/fragment in hole and electron, as well as hole-electron overlaps in various atom/fragment spaces can be plotted as heat map, so that their distribution character can be very vividly exhibited. Below is an example, the color corresponds to function value, while abscissa corresponds to atom index.

From the graph, you can immediately recognize that this is a local excitation, since most part of both hole and electron are distributed on the fragments consisting of atoms 1-14. In particular, atoms 7 and 8 are the atoms that contribute most to this electron excitation. If you load fragment definition before plotting, then the abscissa of the heat map will correspond to fragment index. In the menu,


![](../imgs/p273_043.png)

<!-- p.274 -->

there are also options used to adjust color scale, ratio of the map and interval between labels in X axis.

A very detailed example of this hole-electron module is given in Section 4.18.1. Example of analyzing transition density and transition dipole moment density using this module is given in Section 4.18.2.1. More discussion and examples can be found from my blog article "Using Multiwfn to perform hole-electron analysis to fully investigate electron excitation character" (in Chinese, http://sobereva.com/434).

Information needed: See beginning of Section 3.21.


### 3.21.2 Plot atom/fragment transition matrix of various kinds as heat map (2)



This function is used to plot atom transition matrix (ATM) of various kinds as heat map (color-filled matrix map). The ATM refers to any kind of atom-based matrix that represents electron transition information between two states. For example, it may correspond to the atom-based transition density matrix (see below), the atom-atom charge transfer matrix, the atom transition dipole moment matrix and so on. In this function, the ATM can also be further transformed to fragment transition matrix (FTM) and then plotted as heat map.

Although this function can also plot heat maps for other matrices, the major purpose of developing this function is plotting atom or fragment-based transition density matrix, therefore I will first introduce theories related to transition density matrix.

Theories about transition density matrix (TDM) Below, the word "TDM" refers to the transition density matrix in basis function representation. The TDM between ground state and an excited state can be calculated as (de-excitation transitions have been ignored for simplicity)

$$P_{\mu\nu}^{\mathrm{t r a n}}=\sum_{i}^{\mathrm{o c c}}\sum_{a}^{\mathrm{v i r}}w_{i}^{a}C_{\mu i}C_{v a}$$

ia

where Cμi denotes the expansion coefficient of basis function μ in MO i. It is worth to note in passing that the TDM in real space representation, which is introduced in Section 3.21.1.1, can be

constructed easily via TDM in basis function representation (χ stands for basis function):


$$P_{\mu\nu}^{\mathrm{t r a n}}=\sum_{i}^{\mathrm{o c c}}\sum_{a}^{\mathrm{v i r}}w_{i}^{a}C_{\mu i}C_{v a}$$

<!-- formula-ocr: formula_p274_175.png 已替换为LaTeX, 原图保留备查 -->

The off-diagonal elements of TDM essentially represent the coupling between various basis functions during electron excitation. Assume there are only two basis functions and meantime the

excitation can be perfectly represented as i→a MO transition, then the TDM could be explicitly written as below form (notice that the index of the elements has been rearranged according to convention of TDM heat map)

$$P_{\mu\nu}^{\mathrm{t r a n}}=\sum_{i}^{\mathrm{o c c}}\sum_{a}^{\mathrm{v i r}}w_{i}^{a}C_{\mu i}C_{v a}$$


<!-- p.275 -->

If magnitude of off-diagonal element 𝑃1,2 tran is large, it implies that basis functions 1 and 2

significantly participate in occupied orbital i and virtual orbital a, respectively. More generally, we may say that basis functions 1 and 2 have large contribution to hole and electron, respectively, in this case the two basis functions are strongly coupled during the excitation. The diagonal terms are also meaningful, if element 𝑃μ,μtran has large magnitude, it implies that basis function μ must

simultaneously have large contribution to both hole and electron.

Since TDM in general is not a symmetric matrix, in order to make certain discussions easier, some papers employ below symmetrized form


$$\overline{P}_{\mu\nu}^{\mathrm{tran}}=\frac{P_{\mu\nu}^{\mathrm{tran}}+P_{\nu\mu}^{\mathrm{tran}}}{\sqrt{2}}$$

<!-- formula-ocr: formula_p275_176.png 已替换为LaTeX, 原图保留备查 -->

The TDM can be contracted to atom-based form according to correspondence between basis functions and atoms, it will be symbolized as p. In Multiwfn, below construction ways are available:

$$Way1\colon p_{A B}=\sum_{\mu\in A}\sum_{\nu\in B}(P_{\mu\nu}^{\mathrm{t r a n}})^{2}$$

$$Way1\colon p_{A B}=\sum_{\mu\in A}\sum_{\nu\in B}(P_{\mu\nu}^{\mathrm{t r a n}})^{2}$$

||:3Way Pp ABAB = μν   μν tran

$$Way1\colon p_{A B}=\sum_{\mu\in A}\sum_{\nu\in B}(P_{\mu\nu}^{\mathrm{t r a n}})^{2}$$

where μ and ν denote the basis functions centered at atom A and on B, respectively. Both original form and symmetrized form of TDM could be employed here.

If way 1 is employed, the p will correspond to the matrix of so-called correlated electron-hole probability diagram (CEHPD), its (A,B) element was interpreted as the probability of simultaneously finding a hole in atom A and an electron in atom B (this interpretation is not strictly true in general cases). See J. Chem. Phys., 113, 10002 (2000) and J. Am. Chem. Soc., 129, 14257 (2007) for example, in which the authors used 𝑃̅μνtran obtained at ZINDO level.

If the p is constructed in way 2, 3 or 4, the resulting matrix may be referred to as atom transition density matrix. For example, the way 4 has been employed in Chem. Rev., 102, 3171 (2002). However, according to my experiences, using way 2 or 3 is preferred, since I found that the diagonal terms obtained in way 4 is often too large compared to the off-diagonal terms.

Assume that the TDM used to construct p was not symmetrized, the general structure of the resulting p could be expressed in below form


$$\mathbf{p}\equiv\mathrm{e l e c t r o n}\left[\begin{matrix}{1,N}&{2,N}&{\cdots}&{N,N}\\ {\vdots}&{\vdots}&{\ddots}&{\vdots}\\ {1,2}&{2,2}&{\cdots}&{N,2}\\ {1,1}&{2,1}&{\cdots}&{N,1}\\ \end{matrix}\right]$$

<!-- formula-ocr: formula_p275_177.png 已替换为LaTeX, 原图保留备查 -->

hole

In complete analogy with the discussion about TDM, the physical meaning of the matrix elements of p can be roughly understood as follows, irrespective of the choice of the specific way of


<!-- p.276 -->

constructing the p:

- Diagonal terms: If (A,A) is large, it implies that atom A has large contribution to both hole and

electron, therefore the electron excitation should result in evident charge reorganization within atom A
- Off-diagonal terms: If (A,B) is large, then atom A should have large contribution to hole and

meantime atom B should have large contribution to electron, implying that electron excitation leads to CT from A to B The "hole" and "electron" mentioned above are highly abstract concepts, although they have the same physical meaning as the those defined in the hole-electron analysis (Section 3.21.1), one cannot expect that the pattern of the p defined in any one of above ways is always very close to the atom-atom charge transfer matrix, which is much more strictly defined and more meaningful.

If symmetrized form of TDM was used to build p, then CT directional information will not be reflected by p. In this case, if off-diagonal term (A,B)=(B,A) is large, then we can simply say that coherence between atoms A and B is strong during the electron excitation, in other words, charge transfer occurs between atoms A and B.

The heat map of p is particularly useful for analyzing large-size and highly conjugated molecules. Commonly hydrogens are omitted in the plot to make the map compact, since hydrogens rarely participate in electron excitation of chemical interest.

If fragments are defined, the p (or other kinds of atom transition matrix) can further be contracted to fragment-based form: fragfragRSABAR BSpp = 

This form is very convenient when one wishes to study role of various fragments in electron excitation.

Input files Since there are different types of atom transition matrix, and the matrix can be passed to Multiwfn in different ways, there are several circumstances as shown below, you should use proper input files. The file that should be loaded when Multiwfn boots up is always the file containing basis function information, and it should correspond to another file that needed to be loaded when you enter present function.

(1) Plotting heat map of p in usual way You should load a file containing configuration coefficient information of excited states when you enter this function (see beginning of Section 3.21). Then Multiwfn will automatically generate TDM between ground state and you selected excited state, and at the same time you can choose if symmetrizing the resulting TDM in aforementioned way.

(2) Plotting heat map of p based on the TDM recorded in Gaussian output file You should load Gaussian output file of electron excitation task when you enter this function. The keywords density=transition=x IOp(6/8=3) must be specified in Gaussian input file, so that TDM between ground state and excited state x can be printed in output file by Link 601 of Gaussian. Via this way, not only the TDM of CIS/TDHF/TDA-DFT/TDDFT can be plotted, but also the TDM generated by the EOM-CCSD and semi-empirical ZINDO method can be plotted.

Note 1: The TDM outputted by Gaussian is in aforementioned symmetrized form. Note 2: If your ground state is singlet state while you used such as TD=triplet to request Gaussian to compute triplet excited states, then the outputted TDM will be exactly zero due to spin forbidden, and thus Multiwfn is unable to plot corresponding TDM map. However, it is possible to draw spatial part of the singlet-triplet TDM. To do this, you should let Multiwfn itself to generate TDM, see (1).


<!-- p.277 -->

Note 3: If the basis set you used contains diffuse basis functions, in rare cases, the TDM outputted by Gaussian is incorrect, and thus the resulting heat map will be useless.

In summary, if the method you are using is not ZINDO, do not let Multiwfn to load TDM directly from Gaussian output file.

(3) Plotting heat map of p based on the TDM recorded in a plain text file You should load a file named tdmat.txt when you enter this function, Multiwfn will read TDM from this file. Commonly, the tdmat.txt is generated by subfunction 9 of main function 18 (see Section 3.21.9 for detail), which can not only generate TDM between ground state and an excited state, but can also generate TDM between two excited states. An example file has been provided as examples\excit\tdmat.txt.

For above three cases, you can choose the way used to contract the TDM to the p. (4) Plotting atom transition dipole moment matrix You should load a file named one of AAtrdip.txt, AAtrdipX.txt, AAtrdipY.txt, AAtrdipZ.txt when you enter this function, Multiwfn will read atom transition dipole moment matrix from this file. Commonly, they are generated by subfunction 11 of main function 18 (see Section 3.21.11 for detail). By plotting heat map of these matrices, one can easily recognize which atoms and which interatomic couplings notably affect transition dipole moment.

(5) Plotting atom-atom charge transfer matrix You should load a file named atmCTmat.txt when you enter this function, Multiwfn will read atom-atom charge transfer matrix from this file. Commonly, the atmCTmat.txt is generated by subfunction 8 of main function 18 (see Section 3.21.8 for detail). By plotting heat map of this kind of matrix, charge transfers between various atoms or fragments as well as charge reorganization sites can be intuitively recognized.

Hint: In fact, you can also make the tdmat.txt or AAtrdip.txt/atmCTmat.txt contain other kinds of matrices so that they can be plotted as heat map via present module. For example, you can export bond order matrix as bndmat.txt using corresponding subfunction in main function 9, then rename it as atmCTmat.txt and delete the first line from it, then if you load this file into Multiwfn when entering present module, the plotted heat map will correspond to the bond order matrix.

Usage After loading all needed files and generating all needed data as mentioned above, you will enter the interface for plotting heat map of the atom transition matrix (ATM). Some options are self-explanatory, others are described below:

Option 0: Showing heat map of ATM on screen. By default, labels in abscissa and ordinate of this map correspond to indices of non-hydrogen atoms.

Option 1: The same as option 0, but save the heat map as graphical file in current folder. Option 3: Exporting the ATM as matrix.txt in current folder, so that it can then be conveniently plotted by some third-party tools such as Origin and Sigmaplot.

Option 4: Switching the status if hydrogens will be included in the heat map Option 5: Changing upper and lower limits of color scale. By default, they are automatically set to maximum and minimum matrix elements of ATM, respectively.

Option 6: Changing the number of interpolation steps between grid data. If you want to make the graph look smooth, it should be set to a large value (the default 10 is already quite large); if the value is set to 1, then interpolation will not be performed, in this case each square grid in the map exactly corresponds to a matrix element.

Option 8: Determining if performing normalization. If the status is switched to "Yes", then normalization factor will be applied so that the sum of all elements of ATM is equal to unity.


<!-- p.278 -->

If you select option "-1 Define fragments", fragment definition can be directly inputted or loaded from a plain text file, which should look like below, each fragment occupies a line:


```text
1,3,6-10,12
2,4,5
11
13-15
```

Then Multiwfn will contract the atom transition matrix to fragment transition matrix (FTM). After that, the matrix to be plotted or exported in present module will be FTM instead of ATM

An example of plotting and studying p matrix is given in Section 4.18.2.2; example of analyzing transition dipole moment matrix is given in Section 4.18.2.3; example of plotting atom-atom charge transfer matrix is given in Section 4.18.8.


### 3.21.4 Calculate ∆r index to measure charge-transfer length (4)

Theory

In the paper J. Chem. Theory Comput., 9, 3118 (2013), $\Delta r$ index was proposed to measure CT length during electron excitation. The Δr can be expressed as


$$\Delta r_{i}^{a}=\frac{(K_{i}^{a})^{2}}{\displaystyle\sum_{i,a}(K_{i}^{a})^{2}}\big|\big\langle\varphi_{a}\big|\mathbf{r}\big|\varphi_{a}\big\rangle-\big\langle\varphi_{i}\big|\mathbf{r}\big|\varphi_{i}\big\rangle\big|$$

<!-- formula-ocr: formula_p278_178.png 已替换为LaTeX, 原图保留备查 -->

where ∆𝑟𝑖 𝑎 is contribution of orbital transition between i and a to the $\Delta r$ index:

The index i and a run over all occupied and virtual MOs, respectively. φ is orbital wavefunction. Assume that the method you used to calculate electron excitation is CIS or the TDDFT under Tamm-Dancoff approximation, then $K_i^a$ 𝑎 is simply the configuration coefficient corresponding to excitation

of i→a. While if the method you used is TDHF or TDDFT, then $K_i^a$ 𝑎 and 𝑤′𝑖 𝑎 denote the configuration coefficient corresponding to excitation of i→a and de-excitation of 𝑎= 𝑤𝑖 𝑎+ 𝑤′𝑖 𝑎, where 𝑤𝑖

i←a, respectively.

$\Delta r$ is especially useful for diagnosing when certain classes of DFT functionals are failure for TDDFT purpose. When Δr is large, pure functionals such as BLYP and PBE, and the hybrid functionals with low Hartree-Fock exchange composition such as B3LYP and PBE0, will not work well. In this case, long-range corrected functionals should be employed; for instance, CAM-B3LYP and ωB97XD.

It is worth to mention that if an electron excitation can be perfectly represented by one pair of

MO transition, then the $\Delta r$ index and D index defined in hole-electron analysis framework will be exactly identical in principle:

$$\begin{aligned}&\Delta r=\left|\left\langle\varphi_{a}\left|\mathbf{r}\right|\varphi_{a}\right\rangle-\left\langle\varphi_{i}\left|\mathbf{r}\right|\varphi_{i}\right\rangle\right|\equiv\left|\int\mathbf{r}\left|\varphi_{a}(\mathbf{r})\right|^{2}\mathrm{d}\mathbf{r}-\int\mathbf{r}\left|\varphi_{i}(\mathbf{r})\right|^{2}\mathrm{d}\mathbf{r}\right|\\ &D\ \mathrm{index}=\left|\mathbf{D}\right|=\left|\int\mathbf{r}\rho^{\mathrm{ele}}(\mathbf{r})\mathrm{d}\mathbf{r}-\int\mathbf{r}\rho^{\mathrm{hole}}(\mathbf{r})\mathrm{d}\mathbf{r}\right|=\left|\int\mathbf{r}\left|\varphi_{a}(\mathbf{r})\right|^{2}\mathrm{d}\mathbf{r}-\int\mathbf{r}\left|\varphi_{i}(\mathbf{r})\right|^{2}\mathrm{d}\mathbf{r}\right|\\ \end{aligned}$$

However, their values outputted by Multiwfn should be marginally different, since they are


<!-- p.279 -->

evaluated based on different numerical integration algorithms.

Usage The input files needed by present module have been detailedly described at the beginning of Section 3.21, namely you should load a file containing basis function information when Multiwfn boots up, and then load a file containing configuration coefficient information of excited states.

After entering present function (subfunction 4 of main function 18), you will be prompted to

select the excited states for which the $\Delta r$ will be calculated, then the results will be printed on screen immediately.

If you only selected one state, then Multiwfn will ask you to choose if decomposing the $\Delta r$ into orbital pair contributions. If you input e.g. 0.01, then orbital pairs which have contribution to Δr larger than 0.01 will be printed. From the output, you can easily identify which orbital pairs have significant contribution to charge-transfer of electron excitation.

An example of present function is provided as Section 4.18.4. Information needed: See beginning of Section 3.21.


### 3.21.3 Analyze charge-transfer based on density difference grid data (3)

Theory In the paper J. Chem. Theory Comput., 7, 2498 (2011), the authors proposed a method for analyzing charge-transfer (CT) during electron transition, present function fully implements this analysis method. It is also probable that this method can be used to study CT in other processes, such as formation of molecular complex. In the original paper, the author only discussed the cases when charge-transfer is in one-dimension, while in Multiwfn this scheme has been generalized to three-dimension case. In addition, some quantities introduced below are not proposed in the original paper but proposed by me, definition of some quantities in the original paper have also been modified by me to make the analysis more meaningful.

The electron density variation between excited state (EX) and ground state (GS) is


$$\Delta\rho(\mathbf{r})=\rho_{\mathrm{E X}}(\mathbf{r})-\rho_{\mathrm{G S}}(\mathbf{r})$$

<!-- formula-ocr: formula_p279_179.png 已替换为LaTeX, 原图保留备查 -->

$$\Delta\rho(\mathbf{r})=\rho_{\mathrm{E X}}(\mathbf{r})-\rho_{\mathrm{G S}}(\mathbf{r})$$

$\rho_{+}$ as well as their integrals over the whole space in principle can also be larger than 1.0, this is because excitation of an electron must lead to reorganization of distribution of the rest of electrons,

which also make contribution to Δρ.

The transferred charge $q_{CT}$ is the magnitude of the integral of $\rho_{+}$ over the whole space. It is important to correctly recognize the physical meaning of this quantity. qCT only corresponds to the total amount of charge whose distribution is perturbed during electron excitation, it does not


<!-- p.280 -->

correspond to net charge transfer from one fragment to another fragment (e.g. from donor group to acceptor group)

The barycenter of positive and negative parts of Δρ can be computed as


$$\begin{aligned}\mathbf{R}_{+}=&\int\mathbf{r}\rho_{+}(\mathbf{r})\mathrm{d}\mathbf{r}/\int\rho_{+}(\mathbf{r})\mathrm{d}\mathbf{r}\\mathbf{R}_{-}=&\int\mathbf{r}\rho_{-}(\mathbf{r})\mathrm{d}\mathbf{r}/\int\rho_{-}(\mathbf{r})\mathrm{d}\mathbf{r}\end{aligned}$$

<!-- formula-ocr: formula_p280_180.png 已替换为LaTeX, 原图保留备查 -->

The Cartesian component coordinates of R+ will be referred to as X+, Y+, Z+ below, while that of R− will be referred to as X−, Y−, Z−.

The distance between the two barycenters measures the CT length, its three Cartesian components:


$$\sqrt{(D_x)^2 + (D_y)^2 + (D_z)^2} \equiv |\mathbf{R}_+ - \mathbf{R}_-|$$

<!-- formula-ocr: formula_p280_181.png 已替换为LaTeX, 原图保留备查 -->

$$\begin{aligned}&\Delta\sigma_{\lambda}=\sigma_{+,,\lambda}-\sigma_{-,,\lambda}\qquad\lambda=\{x,y,z\}\\&\Delta\sigma index=|\pmb{\sigma}_{+}|-|\pmb{\sigma}_{-}|\\ \end{aligned}$$

length.

The dipole moment variation caused by electron excitation can be evaluated as

$$\Delta\mu_{_{X}}=(X_{+}-X_{-})q_{\mathrm{CT}}\quad\Delta\mu_{_{Y}}=(Y_{+}-Y_{-})q_{\mathrm{CT}}\quad\Delta\mu_{_{Z}}=(Z_{+}-Z_{-})q_{\mathrm{CT}}$$

The RMSDs of distribution of $\rho_{+}$ in each direction are defined as


$$\sigma_{a,\lambda}=\sqrt{\frac{\int\rho_{a}(\mathbf{r})(\lambda^{\prime}-\lambda_{a})^{2}\mathrm{d}\mathbf{r}}{\int\rho_{a}(\mathbf{r})\mathrm{d}\mathbf{r}}}$$

<!-- formula-ocr: formula_p280_182.png 已替换为LaTeX, 原图保留备查 -->

where a={+,-}, λ’={x,y,z}, λ={X, Y, Z}. x, y and z are Cartesian components of position vector r. For example, σ+,y can be explicitly written as


$$\sigma_{+,y}=\sqrt{\frac{\int\rho_{+}(\mathbf{r})(y-Y_{+})^{2}\mathrm{d}\mathbf{r}}{\int\rho_{+}(\mathbf{r})\mathrm{d}\mathbf{r}}}$$

<!-- formula-ocr: formula_p280_183.png 已替换为LaTeX, 原图保留备查 -->

$$\begin{aligned}&\Delta\sigma_{\lambda}=\sigma_{+,,\lambda}-\sigma_{-,,\lambda}\qquad\lambda=\{x,y,z\}\\&\Delta\sigma index=|\pmb{\sigma}_{+}|-|\pmb{\sigma}_{-}|\\ \end{aligned}$$


$$\begin{aligned}&\Delta\sigma_{\lambda}=\sigma_{+,,\lambda}-\sigma_{-,,\lambda}\qquad\lambda=\{x,y,z\}\\&\Delta\sigma index=|\pmb{\sigma}_{+}|-|\pmb{\sigma}_{-}|\\ \end{aligned}$$

<!-- formula-ocr: formula_p280_184.png 已替换为LaTeX, 原图保留备查 -->

It is noteworthy that D index is zero for exactly centrosymmetric systems, therefore, it is useless for

discussing CT problem of such kind of system. However, Δσ index is often useful to identify this type of excitation, since in this case Δσ index must be large because diffuseness extent of ρ+ is much higher than ρ−.

C+ and C− functions are defined aiming for visualizing CT more intuitively than Δρ. Their structures are similar to Gaussian function, the value asymptotically approaches zero from the centroid of the function.


<!-- p.281 -->

$$C_{+}(\mathbf{r})=A_{+}\exp\left(-\frac{\left(x-X_{+}\right)^{2}}{2\sigma_{+,x}^{2}}-\frac{\left(y-Y_{+}\right)^{2}}{2\sigma_{+,y}^{2}}-\frac{\left(z-Z_{+}\right)^{2}}{2\sigma_{+,z}^{2}}\right)$$

Normalization factor A is introduced so that the integrals of C+ and C− over the whole space are equal to that of $\rho_{+}$, respectively.

Hλ measures average degree of spatial extension of $\rho_{+}$ in X/Y/Z direction, HCT is that in CT direction, and H index is an overall measure:


$$\begin{aligned}&H_{\lambda}=(\sigma_{+,\lambda}+\sigma_{-,\lambda})/2\quad\lambda=\{x,y,z\}\\&H_{\mathrm{CT}}=\mid\mathbf{H}\cdot\mathbf{u}_{\mathrm{CT}}\mid\\&H\operatorname{index}=\left(\mid\pmb{\sigma}_{+}\mid+\mid\pmb{\sigma}_{-}\mid\right)/2\\ \end{aligned}$$

<!-- formula-ocr: formula_p281_185.png 已替换为LaTeX, 原图保留备查 -->

H CTCT ·= || uH

H 2/|)||(|index += σσ −+

where uCT is unit vector in CT direction and can be straightforwardly derived using centroid of $\rho_{+}$.

t index measures separation degree of $\rho_{+}$:

CTindexindexHDt−=

If t index<0, it implies that $\rho_{+}$ are not substantially separated due to CT. Clear separation of ρ− and ρ+ distributions must correspond to evidently positive t index.

I defined another quantity to measure overlapping extent between C+ and C−:


$$S_{+-}=\int\sqrt{C_{+}(\mathbf{r})/A_{+}}\sqrt{C_{-}(\mathbf{r})/A_{-}}\mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p281_186.png 已替换为LaTeX, 原图保留备查 -->

If the value equals 1, that means the two functions are completely superposed, else if the value equals zero, it indicates that their distributions are completely separated. This index is dimensionless.

Usage Because all numerical integrals mentioned above are computed based on evenly distributed

grid data, user needs to generate grid data of Δρ by using custom operation of main function 5, see Section 3.7.1, or load a file (e.g. cube file) containing grid data of density difference when Multiwfn boots up. After that, enter subfunction 3 of main function 18, all aforementioned quantities will be

shown on screen immediately. The "Overlap integral between C+ and C-" term is the S+− introduced above. In the post-processing menu, the user can choose to visualize C+ and C−, or export grid data for the two functions to cube file in current folder.

An example is given in Section 4.18.3. Information needed: Grid data of electron density difference


### 3.21.5 Calculate transition electric/magnetic dipole moments between all states and for each state (5)



This function is used to calculate transition electric/magnetic dipole moment between all states


<!-- p.282 -->

(including both ground state and excited states). This function is also able to print electric dipole moment for each state.

For a transition i → j, the transition electric dipole moment is defined as ⟨𝜓𝑖|−𝐫|𝜓𝑗⟩; when i=j, this quantity corresponds to electric dipole moment of this state contributed by electrons. The

transition magnetic dipole moment is defined as 1 2 𝑖⟨𝜓𝑖|𝐫× 𝛁|𝜓𝑗⟩, but the moment outputted by this

function simply corresponds to ⟨𝜓𝑖|𝐫× 𝛁|𝜓𝑗⟩ , which is the same as the value outputted by electronic excitation calculations in Gaussian.

The input files needed by this function have been detailedly described at the beginning of Section 3.21, namely you should load a file containing basis function information when Multiwfn boots up, and then load a file containing configuration coefficient information of excited states. If you need very accurate transition dipole moments, you should use IOp(9/40=5) keyword of Gaussian or TPrint 1E-10 keyword of ORCA to make the program print as much configuration coefficients as possible.

After you enter present function, summary of all excitations will be printed. "Normalization" should be as close as possible to expected value (0.5 and 1.0 for closed- and open-shell reference states, respectively). If the deviation is large, then the resulting transition dipole moments must have a large error, and you must make your quantum chemistry program output more configuration coefficients.

In the interface you can use option 0 to choose the type of (transition) dipole moments to be calculated, by default they are electric, but you can change to magnetic. You can use options 1 ~ 4 to choose the task to conduct, see below, in which options 3 and 4 are available only if the (transition) dipole moment to be calculated is set to electric.

- Option 1: Output transition electric dipole moments between all states (including both ground state and excited states) to screen

- Option 2: The same as 1, but output to transdipmom.txt in current folder.
- Option 3: Generate input file of SOS module of Multiwfn as SOS.txt in current folder. Then if you use the SOS.txt as input file, you can use SOS module to evaluate (hyper)polarizability, see Section 3.27.2 for detail.

- Option 4: Output electric dipole moment of each excited state to dipmom.txt in current folder. Note that both electronic and nuclear contributions to the value are taken into account (this is clearly different to the values corresponding to i=j cases printed by option 1 and 2, which only considers contribution from electrons).

The calculation process of all the tasks consists of three stages: Stage 1: Calculate dipole moment integrals between all basis functions Stage 2: Calculate dipole moment integrals between all MOs Stage 3: Calculate dipole moment integrals between all excited states. Usually this is the most time-consuming step.

If the output file of quantum chemistry program includes both singlet and triplet excited states, for example, you used TD(50-50) keyword in Gaussian and reference state is closed-shell, only aforementioned tasks (1) and (2) are available, and transition dipole moment of all singlet-singlet pairs (including ground state) and triplet-triplet pairs will be calculated by Multiwfn and outputted


<!-- p.283 -->

separately, while singlet-triplet pairs are ignored because due to spin-forbidden the result must be zero. In addition, excitation energies between S0 and all excited states are printed at the end of output. This function is of great importance if you want to use PySOC code to calculate spin-orbit coupling matrix element, see my blog article "Using Gaussian+PySOC to calculate spin-orbit coupling matrix element under TDDFT" (http://sobereva.com/411, in Chinese) for detail.

There is a parameter "maxloadexc" in `settings.ini`, if this value is not 0 (default) and the actual number of excited states is higher than this value, then only the first "maxloadexc" excited states will be loaded and subjected to transition electric dipole moment calculation.

Calculation of transition dipole moments between excited states is quite time-consuming for large systems. However, if you only need them between ground state and excited states, the data can always be quickly calculated. In this case, before starting calculation, you should select option “-1: Toggle if only calculating between ground and excited states” to change its status to “Yes”, then transition dipole moments between excited states will not be calculated and printed.

Examples of this function are given in Section 4.18.5. Information needed: See beginning of Section 3.21.

Appendix The formulae used to derive transition electric/magnetic dipole moment between electronic states used in the present function are given as follows

(1) Transition electric dipole moment between ground state and an excited state K:

$$\mathbf{D}_{0\rightarrow K}=\left\langle\Psi_{0}\left|-\mathbf{r}\right|\Psi_{K}\right\rangle=\sum_{i}^{\mathrm{o c c}}\sum_{a}^{\mathrm{v i r}}w_{i,a}^{K}\left\langle\varphi_{i}\left|-\mathbf{r}\right|\varphi_{a}\right\rangle+\sum_{i}^{\mathrm{o c c}}\sum_{a}^{\mathrm{v i r}}w_{i,a}^{\prime K}\left\langle\varphi_{i}\left|-\mathbf{r}\right|\varphi_{a}\right\rangle$$

where w and w’ are coefficients of excitation and de-excitation configurations respectively. i and a denote indices of occupied and unoccupied molecular orbitals, respectively.

(2) Transition magnetic dipole moment between ground state and an excited state K:

$$\mathbf{M}_{0\rightarrow K}=\left\langle\psi_{0}\left|\mathbf{r}\times\nabla\right|\psi_{K}\right\rangle=\sum_{i}^{o c c}\sum_{a}^{v i r}w_{i,a}^{K}\left\langle\varphi_{i}\left|\mathbf{r}\times\nabla\right|\varphi_{a}\right\rangle-\sum_{i}^{o c c}\sum_{a}^{v i r}w_{i,a}^{\prime K}\left\langle\varphi_{i}\left|\mathbf{r}\times\nabla\right|\varphi_{a}\right\rangle$$

See Eqs. 22 and 24 in J. Chem. Phys., 66, 3460 (1977) on why the consideration of excitations and de-excitations is different for evaluating electric and magnetic transition dipole moments.

(3) Transition electric/magnetic dipole moment between excited states K and L:

$$\mathbf{T}_{K\rightarrow L}=\left\langle\psi_{K}\left|\hat{\mathbf{v}}\right|\psi_{L}\right\rangle=\sum_{i}^{\mathrm{o c c}}\sum_{a}^{\mathrm{v i r}}\tilde{w}_{i,a}^{K}\sum_{j}^{\mathrm{o c c}}\sum_{b}^{\mathrm{v i r}}\tilde{w}_{j,b}^{L}V^{i a j b}$$

with


<!-- p.284 -->

$$V^{i a j b}=\begin{cases}{\left\langle\varphi_{i}\right\vert\hat{\mathbf{v}}\big\vert\varphi_{a}\big\rangle}&{(i=j,a\neq b)}\\ {-\Big\langle\varphi_{i}\Big\vert\hat{\mathbf{v}}\Big\vert\varphi_{a}\Big\rangle}&{(i\neq j,a=b)}\\ {\mathbf{v}^{0}-\Big\langle\varphi_{i}\Big\vert\hat{\mathbf{v}}\Big\vert\varphi_{i}\Big\rangle+\Big\langle\varphi_{a}\Big\vert\hat{\mathbf{v}}\Big\vert\varphi_{a}\Big\rangle}&{(i=j,a=b)}\\ {0}&{(i\neq j,a\neq b)}\\ \end{cases}$$


$$\mathbf{v}^{0}=\sum_{l}^{\mathrm{o c c}}\eta_{l}\left\langle\varphi_{l}\right|\hat{\mathbf{v}}\left|\varphi_{l}\right\rangle$$

<!-- formula-ocr: formula_p284_187.png 已替换为LaTeX, 原图保留备查 -->

where 𝑤̃ denotes both w and w’. v0 corresponds to ground state property with η being orbital occupancy. The operator 𝐯̂ = −𝐫 is for transition electric dipole moment and 𝐯̂ = 𝐫× ∇ is for transition magnetic dipole moment. For TD case, the V terms between excitation and de-excitation configurations are simply ignored. In addition, when calculating V terms between de-excitation

configurations, it is replaced with −V.


### 3.21.6 Generate natural transition orbitals (NTOs) (6)

Theory This function is used to generate natural transition orbitals (NTOs). NTO was proposed in J. Chem. Phys., 118, 4775 (2003), it has become a very popular and useful way to analyze character electron excitation obtained by single-reference methods.

Transition of electronic state is often not predominated by only one MO pair, in many cases multiple MO pair transitions simultaneously have non-negligible contributions, which can be evaluated as square of corresponding configuration coefficient. This fact brings great hindrance of analyzing electron excitation character by simply visualizing related MOs. The NTO method aims to relieve this difficulty, it separately performs unitary transformation for occupied MOs and virtual MOs, so that only one or very few number of orbital pairs have dominant contributions.

The basic procedure of yielding NTOs is outlined below: (1) Generating transition density matrix in MO basis (T). Assume that the system has $n_{\mathrm{occ}}$ occupied MOs and nvir virtual MOs, then T has dimension of (nocc, nvir), its (i,l) element is simply constructed as

ai liTw= ,

𝑎 stands for configuration coefficient corresponding to i→a orbital transition. Note that for TD formalism, there may be some de-excitations, their configuration coefficients are simply ignored in constructing the T. where i<$n_{\mathrm{occ}}$, l<nvir and a=l+nocc. 𝑤𝑖

(2) Generating temporary matrix for occupied and virtual orbitals, respectively

TToccvir==TTTTT T

Evidently, both Tocc and Tvir are square matrices, their dimensions are $n_{\mathrm{occ}}$ and nvir, respectively.

(3) Diagonalizing Tocc and Tvir to obtain eigenvalues and eigenvectors

11occoccoccoccvirvirvirvir−−==UT UΛU T UΛ

(4) The diagonal terms of Λocc and Λvir are eigenvalues of occupied and virtual NTOs, respectively. For the former, the eigenvalues are commonly sorted from low to high, while for the latter, the eigenvalues are commonly sorted from high to low. A NTO pair consists of a$n_{\mathrm{occ}}$upied


<!-- p.285 -->

NTO and a virtual NTO sharing the same eigenvalue. Eigenvalue of a NTO pair multiplied by 100 is just its percentage contribution to the electron excitation.

For CIS and TDA-DFT, the range of eigenvalue must be 0.0~1.0. However, in the TDHF and TDDFT cases, due to presence of de-excitations, which is not explicitly considered in the NTO analysis, it is possible that a NTO pair has eigenvalue slightly larger than 1.0, in this situation you can simply treat it as 1.0 (However, if the value is much larger than 1.0, the TDDFT result may be unreliable, and I suggest using TDA-DFT instead).

(5) MOs are transformed to NTOs via unitary transformation matrix U

NTOMONTOMOoccoccoccvirvirvir==CCUCCU

where 𝐂occMO and 𝐂vir MO are coefficient matrix of occupied MOs and virtual MOs in original basis functions, respectively; their columns correspond to different MOs. The counterpart matrices with NTO superscript denote coefficient matrix of occupied and virtual NTOs.

Implementation and Usage The input files needed by present function have been detailedly described at the beginning of Section 3.21, namely you should load a file containing basis function information when Multiwfn boots up, and then load a file containing configuration coefficient information of excited states.

After you enter present function, you should input the index of the electron excitation to be studied, then Multiwfn will load corresponding configuration coefficients and generate NTOs according to the equations shown above, and then output eigenvalues of NTO pairs. Next, you can choose if exporting the NTOs to .fch/.molden/.mwfn file. If you choose to export, then you can use Multiwfn to load the newly generated file to visualize the NTOs, analyze NTO orbital composition and so on (note that in this case the data in orbital energy field in fact is NTO eigenvalues).

Present function works for both restricted and unrestricted reference states; for the latter, the result of Alpha part and Beta part are calculated and printed separately, you only need to pay attention to the NTO pairs having largest eigenvalues (e.g. the largest eigenvalue of Alpha part is 0.03, while the largest eigenvalue of Beta part of 0.95, that means this electron excitation is dominated by transition of the Beta NTO pair)

According to my experiences, NTO analysis often works equally well as the hole-electron analysis introduced in Section 3.21.1, namely both of them are able to avoid necessity of inspecting many MOs when discussing electron excitation. An additional advantage of NTO analysis over hole-electron analysis is that the orbital phase information is retained; however, in some cases NTO analysis completely fails, namely even after transformation from MO to NTO representation, there is still no dominant orbital pair transition. Clearly in this case you have to resort to hole-electron analysis.

An example of generating and analyzing NTOs is provided in Section 4.18.6. Information needed: See beginning of Section 3.21


### 3.21.7 Calculate ghost-hunter index (7)

Theory background


<!-- p.286 -->

The ghost states are spurious very low-lying charge transfer (CT) excited states with excitation wavelength usually around 1000 nm or more, they result from evidently incorrect asymptotic behavior of exchange potential of pure DFT functionals or the hybrid functionals having low Hartree-Fock exchange composition in long range electron interaction. Since the ghost states are unreal states, they should be ignored when discussing electron excitations and plotting electronic spectra. When ghost states are identified, then DFT functionals with relatively high global HF exchange composition (e.g. M06-2X and BH&HLYP), or long-range corrected functional (e.g.

ωB97XD), or range-separated functional with high HF exchange composition at long range of electronic interaction (e.g. CAM-B3LYP), should be employed to get rid of them.

The lower bound of TDDFT excitation energy of a CT state can be expressed as

𝜔low = 𝐼𝑃𝐷−𝐸𝐴𝐴−1/𝑅 where IPD is ionization potential of electron donor moiety (energy consumption of leaving an electron), EAA is electron affinity of electron acceptor moiety (its negative is energy lowering due to receiving an electron), and R denotes the electrostatic interaction between the hole and electron

after the CT excitation. According to Koopmans’ theorem, IP≈−εHOMO, EA≈−εLUMO, and we assume that the excitation fully corresponds to HOMO→LUMO transition, where HOMO and LUMO are completely localized in donor and acceptor regions respectively, we have

𝜔low≈−𝜀HOMO + 𝜀LUMO −1/𝑅 In practice, electron excitation is contributed by multiple orbital transitions, so weighted MO energies should be employed instead. In addition, the R may be estimated using $D_{CT}$ index (see later). So, the above equation can be converted to

$$\omega_{\mathrm{low}}=\underbrace{\sum_{i,a}\left[\frac{\left(w_{i}^{a}\right)^{2}}{\sum_{i,a}\left(w_{i}^{a}\right)^{2}}\left(\varepsilon_{a}-\varepsilon_{i}\right)\right]}_{\mathrm{term1}}-\frac{1}{D_{\mathrm{CT}}}_{\mathrm{term2}}$$

term 1

where i and a denote occupied and virtual MOs, respectively. The summation loops all TDDFT

configurations. w is configuration coefficient. ε stands for MO energy.

In J. Comput. Chem., 38, 2151 (2017), the authors proposed ghost-hunter index ($M_{AC}$) to diagnose if an excited state yielded by current TDDFT calculation may be a ghost state. The MAC is

simply the ωlow shown above.

Notice that in the original $M_{AC}$ paper, they erroneously used w rather than w2 in the above

equation, and the sign in front of $\varepsilon_{a}$ is wrong, these problems have been fixed in their later publication J. Chem. Phys., 154, 204102 (2021). This paper and the original $M_{AC}$ paper did not explicitly mention how to deal with de-excitation configurations, in the implementation in Multiwfn, all de-excitation configurations are ignored.

Since the $M_{AC}$ corresponds to the theoretical lower bound of CT excitation energy calculated by TDDFT (ETDDFT), in the paper of ghost-hunter index, it is argued that

$E_{TDDFT}$ →ghost CT state

𝐸TDDFT > $M_{AC}$ →real CT state Ghost-hunter index is undoubtedly useful, however, according to my experience, this criterion is often too stringent. I suggest only regard $E_{TDDFT}$ as a necessary rather than sufficient condition for determining presence of ghost CT state.

Evaluation of ghost-hunter index


<!-- p.287 -->

To calculate the $M_{AC}$, you should perform hole-electron analysis as usual, see introduction in Section 3.21.1 and example in Section 4.18.1. Once calculation of grid data of hole and electron is finished, Multiwfn automatically prints the MAC index as well as its two terms (see above equation for the meaning of the two terms).

Beware that in Multiwfn, the $D_{\mathrm{CT}}$ used in the $M_{AC}$ expression is evaluated as the distance between centroid of electron and hole distributions, this case corresponds to adopting unrelaxed density of excited state. It is more or less different to the DCT evaluated in original paper of MAC (referred to as DCT' below), which is calculated as centroid distance between positive and negative parts of density difference between relaxed excited state density and ground state density. The DCT calculated by hole-electron analysis module of Multiwfn is not only reasonable enough, but also much cheaper than DCT', since evaluating TDDFT relaxed density for large systems is fairly expensive. However, if you really want to calculate MAC index based on DCT', you should obtain the first term of MAC via electron-hole analysis module, and then obtain DCT' via subfunction 3 of main function 18 (see the example given in Section 4.18.3) and manually calculate the second term of MAC (namely -1/DCT'), and finally sum up the two terms to derive MAC.

It is worth to mention that the $M_{AC}$ index is in principle only applicable to one-dimension CT case, if the CT takes place in multiple directions, then this index is incapable of correctly identifying ghost state.

Calculation of $M_{AC}$ is involved in the hole-electron analysis example in Section 4.18.1. Information needed: See beginning of Section 3.21


### 3.21.8 Calculate interfragment charge transfer in electron excitation via IFCT method (8)



Theory Interfragment charge transfer is a very important phenomenon in electron excitation process. I devised an albeit simple but quite useful way of evaluating amount of interfragment charge transfer between any number of fragments, the method is described below (to be published). This method will be referred to as IFCT (InterFragment Charge Transfer).

The IFCT method contains three steps: (1) Calculating atomic contribution to hole and electron (see introduction of the concept of hole and electron in Section 3.21.1.1)

(2) Calculating fragment contributions to hole and electron by summing up atomic contributions

(3) Constructing interfragment charge transfer matrix Q. Its (R,S) element corresponds to the electron transfer from fragment R to fragment S during the excitation:

,,hole,eleR SRSQ= ΘΘ

where ΘR,hole and ΘS,ele denote contribution of fragment R to hole and contribution of fragment S to electron, respectively. Above formula is very easy to comprehend, it essentially assumes that electron transfer from R to S is proportional to both composition of R in hole (where electron leaves)


<!-- p.288 -->

and composition of S in electron (where electron goes).

Then three additional useful quantities could be defined:

·Electron net transferred from fragments S to R: ,,SRS RR SpQQ→=−

$$\begin{aligned}\Delta p_{_{R}}&=\sum_{S\neq R}(Q_{_{S,R}}-Q_{_{R,S}})=\sum_{S\neq R}(\Theta_{_{S,\mathrm{hole}}}\Theta_{_{R,\mathrm{ele}}}-\Theta_{_{R,\mathrm{hole}}}\Theta_{_{S,\mathrm{ele}}})\\&=\Theta_{_{R,\mathrm{ele}}}\sum_{S\neq R}\Theta_{_{S,\mathrm{hole}}}-\Theta_{_{R,\mathrm{hole}}}\sum_{S\neq R}\Theta_{_{S,\mathrm{ele}}}\\&=\Theta_{_{R,\mathrm{ele}}}(1-\Theta_{_{R,\mathrm{hole}}})-\Theta_{_{R,\mathrm{hole}}}(1-\Theta_{_{R,\mathrm{ele}}})\\&=\Theta_{_{R,\mathrm{ele}}}-\Theta_{_{R,\mathrm{hole}}}\\ \end{aligned}$$

·Intrafragment electron redistribution of fragment R: QR,R By the way, it is easy to show that variation of electron population of a fragment evaluated in above way is quite reasonable:

$$\begin{aligned}\Delta p_{_{R}}&=\sum_{S\neq R}(Q_{_{S,R}}-Q_{_{R,S}})=\sum_{S\neq R}(\Theta_{_{S,\mathrm{hole}}}\Theta_{_{R,\mathrm{ele}}}-\Theta_{_{R,\mathrm{hole}}}\Theta_{_{S,\mathrm{ele}}})\\&=\Theta_{_{R,\mathrm{ele}}}\sum_{S\neq R}\Theta_{_{S,\mathrm{hole}}}-\Theta_{_{R,\mathrm{hole}}}\sum_{S\neq R}\Theta_{_{S,\mathrm{ele}}}\\&=\Theta_{_{R,\mathrm{ele}}}(1-\Theta_{_{R,\mathrm{hole}}})-\Theta_{_{R,\mathrm{hole}}}(1-\Theta_{_{R,\mathrm{ele}}})\\&=\Theta_{_{R,\mathrm{ele}}}-\Theta_{_{R,\mathrm{hole}}}\\ \end{aligned}$$

$$\begin{aligned}\Delta p_{_{R}}&=\sum_{S\neq R}(Q_{_{S,R}}-Q_{_{R,S}})=\sum_{S\neq R}(\Theta_{_{S,\mathrm{hole}}}\Theta_{_{R,\mathrm{ele}}}-\Theta_{_{R,\mathrm{hole}}}\Theta_{_{S,\mathrm{ele}}})\\&=\Theta_{_{R,\mathrm{ele}}}\sum_{S\neq R}\Theta_{_{S,\mathrm{hole}}}-\Theta_{_{R,\mathrm{hole}}}\sum_{S\neq R}\Theta_{_{S,\mathrm{ele}}}\\&=\Theta_{_{R,\mathrm{ele}}}(1-\Theta_{_{R,\mathrm{hole}}})-\Theta_{_{R,\mathrm{hole}}}(1-\Theta_{_{R,\mathrm{ele}}})\\&=\Theta_{_{R,\mathrm{ele}}}-\Theta_{_{R,\mathrm{hole}}}\\ \end{aligned}$$

$$\begin{aligned}\Delta p_{_{R}}&=\sum_{S\neq R}(Q_{_{S,R}}-Q_{_{R,S}})=\sum_{S\neq R}(\Theta_{_{S,\mathrm{hole}}}\Theta_{_{R,\mathrm{ele}}}-\Theta_{_{R,\mathrm{hole}}}\Theta_{_{S,\mathrm{ele}}})\\&=\Theta_{_{R,\mathrm{ele}}}\sum_{S\neq R}\Theta_{_{S,\mathrm{hole}}}-\Theta_{_{R,\mathrm{hole}}}\sum_{S\neq R}\Theta_{_{S,\mathrm{ele}}}\\&=\Theta_{_{R,\mathrm{ele}}}(1-\Theta_{_{R,\mathrm{hole}}})-\Theta_{_{R,\mathrm{hole}}}(1-\Theta_{_{R,\mathrm{ele}}})\\&=\Theta_{_{R,\mathrm{ele}}}-\Theta_{_{R,\mathrm{hole}}}\\ \end{aligned}$$


$$\begin{aligned}\Delta p_{_{R}}&=\sum_{S\neq R}(Q_{_{S,R}}-Q_{_{R,S}})=\sum_{S\neq R}(\Theta_{_{S,\mathrm{hole}}}\Theta_{_{R,\mathrm{ele}}}-\Theta_{_{R,\mathrm{hole}}}\Theta_{_{S,\mathrm{ele}}})\\&=\Theta_{_{R,\mathrm{ele}}}\sum_{S\neq R}\Theta_{_{S,\mathrm{hole}}}-\Theta_{_{R,\mathrm{hole}}}\sum_{S\neq R}\Theta_{_{S,\mathrm{ele}}}\\&=\Theta_{_{R,\mathrm{ele}}}(1-\Theta_{_{R,\mathrm{hole}}})-\Theta_{_{R,\mathrm{hole}}}(1-\Theta_{_{R,\mathrm{ele}}})\\&=\Theta_{_{R,\mathrm{ele}}}-\Theta_{_{R,\mathrm{hole}}}\\ \end{aligned}$$

<!-- formula-ocr: formula_p288_188.png 已替换为LaTeX, 原图保留备查 -->

It is easy to comprehend that this is a quite reasonable way of evaluating variation of electron population of fragment R, and thus well demonstrated reasonableness of the interfragment charge analysis formalism introduced above.

In addition, it is worth to note that sum of amount of interfragment transferred electrons and amount of intrafragment redistribution electrons exactly equals unity, reflecting the fact that only one electron is excited:


$$\begin{aligned}&\sum_{R}\sum_{S\neq R}Q_{R,S}+\sum_{S}Q_{S,S}\\&=\sum_{R}\sum_{S}Q_{R,S}\\&=\sum_{R}\sum_{S}\Theta_{R,\mathrm{hole}}\Theta_{S,\mathrm{ele}}\\&=\sum_{R}\Theta_{R,\mathrm{hole}}\sum_{S}\Theta_{S,\mathrm{ele}}\\&=1\end{aligned}$$

<!-- formula-ocr: formula_p288_189.png 已替换为LaTeX, 原图保留备查 -->

RS

RS

RS

On the evaluation of CT% The concepts of charge transfer percentage (CT%) and its complement local excitation percentage (LE%) are frequently involved in electron excitation studies. In the IFCT framework, they can be defined in two different ways, I believe it is useful to explicitly distinguish them.

- Intrinsic CT% and LE%: The former is evaluated as CT% = 100% × ∑∑𝑄𝑅,𝑆𝑆≠𝑅𝑅, and the latter is evaluated as LE% = 100% × ∑𝑄𝑆,𝑆𝑆, clearly they sum up to 100%. This definition works

for any number of fragments.

- Apparent CT% and LE%: This definition only works for two fragment cases. Apparent CT% is simply evaluated as 100%×|ΔpR|, and apparent LE% is defined as 100%−CT%, where R denotes either fragment.

In the case of two fragments (R and S), the intrinsic CT% and apparent CT% must be somewhat


<!-- p.289 -->

different, both of them have their own value. Intrinsic CT% represents the amount of electrons that essentially participate in charge transfer, which does not reflect the cancellation effect between

electron transfers of R→S and S←R. In contrast, the apparent CT% corresponds to the apparent phenomenon of net electron transfer between R and S, namely the cancellation of the bidirectional electron transfer is taken into account. Clearly, intrinsic CT% must be equal or larger than apparent CT%, and they are equal only if the interfragment charge transfer is completely single directional, that is hole and electron fully and respectively localize on the two fragments.

It is worth to emphasize that %CT is directly dependent of the definition of fragments, because it characterizes amount of charge transfer between the fragments. In the limiting case, you define the whole system as a single fragment, then %CT must be exactly zero for all excitations.

Usage The input files needed by the IFCT analysis have been detailedly described at the beginning of Section 3.21, namely you should load a file containing basis function information when Multiwfn boots up, and then load a file containing configuration coefficient information of excited states.

After entering this function, you need to choose the method for calculating fragment distribution to hole and electron, and select the excited state to be studied, then input the total number of fragments, after that you should define each fragment in turn by inputting atomic indices. If you prefer to load fragment definition from a plain text file, you can input 0 when Multiwfn let you set the total number of fragments, then you can input the path of the file containing fragment definition, the file format should look like below, definition of each fragment occupies a line:


```text
1,3,6-10,12
2,4,5
11
13-15
```

If in this step you input -1, Multiwfn will not carry out regular IFCT analysis but export a file named atmCTmat.txt in current folder, this file records atom-atom charge transfer matrix, whose element

is defined as $Q_{A,B} = \Theta_{A,\text{hole}} \Theta_{B,\text{ele}}$. If you input path of this file after entering the function used to plot atom/fragment transition matrix (see Section 3.21.2), this matrix could be plotted as heat map so that you can visually study its matrix elements.

Once definition of fragments is completed, Multiwfn will calculate and print contribution of all defined fragments to hole and electron, as well as amount of electron transfer between fragments. In addition, net electron transfer as well as variation of electron population of each fragment are also printed. Below is an output instance:


```text
 Variation of population number of fragment  1:  -0.25313
 Variation of population number of fragment  2:  -0.23110
 Variation of population number of fragment  3:   0.48423

 Intrafragment electron redistribution of fragment  1:   0.00334
 Intrafragment electron redistribution of fragment  2:   0.31271
 Intrafragment electron redistribution of fragment  3:   0.02419

 Transferred electrons between fragments:
  1 ->  2:   0.11977       1 <-  2:   0.00874     Net  1 ->  2:   0.11103
```


<!-- p.290 -->


```text
  1 ->  3:   0.14299       1 <-  3:   0.00089     Net  1 ->  3:   0.14210
  2 ->  3:   0.36476       2 <-  3:   0.02263     Net  2 ->  3:   0.34213
```

If two fragments are defined, then both intrinsic and apparent CT(%) and LE(%) will then be printed, while if more than two fragments are defined, only intrinsic CT(%) and LE(%) are printed.

Usually Mulliken-like partition is reasonable choice for evaluating fragment contribution to hole and electron, see "Theory 2" of Section 3.21.1.1 for detail of this method. However, diffuse functions must not be employed in this case, otherwise the result may be very misleading. Hirshfeld method is more robust and fully compatible with diffuse functions, but it is evidently more expensive. When diffuse functions do not occur, the IFCT result under Mulliken-like partition and Hirshfeld partition are in good agreement with each other.

An example of IFCT analysis is given in Section 4.18.8. Information needed: See beginning of Section 3.21


### 3.21.9 Generate and export transition density matrix (9)

According to MO expansion coefficients and configuration coefficients, transition density matrix (TDM) in basis function representation can be constructed by this function. Two kinds of TDMs can be generated:

(1) TDM between ground state and a selected excited state K:

$$P_{\mu\nu}^{\mathrm{t r a n}}=\sum_{i}^{\mathrm{o c c}}\sum_{a}^{\mathrm{v i r}}w_{i,a}^{K}C_{\mu i}C_{\nu a}$$

where w corresponds to coefficient of the configurations involved in the excitation, Cμi denotes the expansion coefficient of basis function μ in MO i. Excitation and de-excitation cases are not distinguished in this context (PS: The TDM constructed in this way is suitable for studying transition electric dipole moment, but not suitable for studying transition velocity and magnetic dipole moment, see Eqs. 22, 23 and 24 in J. Chem. Phys., 66, 3460 (1977)).

(2) TDM between two selected excited states K and L:

$$P_{\mu\nu}^{K L}=\sum_{i}^{\mathrm{o c c}}\sum_{a}^{\mathrm{v i r}}w_{i,a}^{K}\sum_{j}^{\mathrm{o c c}}\sum_{b}^{\mathrm{v i r}}w_{j,b}^{L}V_{\mu\nu}^{i a j b}$$

$$P_{\mu\nu}^{K L}=\sum_{i}^{\mathrm{o c c}}\sum_{a}^{\mathrm{v i r}}w_{i,a}^{K}\sum_{j}^{\mathrm{o c c}}\sum_{b}^{\mathrm{v i r}}w_{j,b}^{L}V_{\mu\nu}^{i a j b}$$

where P is density matrix of ground state. For TD case, the V between excitation and de-excitation configurations is simply ignored. In addition, when calculating V between de-excitation

configurations, it is replaced with −V.

Once generation of TDM has been finished, you can choose if symmetrizing the TDM. There are two ways


<!-- p.291 -->

- Way 1: trantrantran() / 2PPPμνμννμ=+

- Way 2: trantrantran() /2PPPμνμννμ=+

The way 1 is reasonable and should be used in common cases. However, it should be noted that the TDM generated by Gaussian program corresponds to the one symmetrized by way 2, therefore you should choose way 2 if you want the resulting TDM follows convention of Gaussian.

The generated matrix will be outputted to tdmat.txt in current folder. You can also choose to output TDM.fch in current folder, whose “Total SCF Density” field will correspond to TDM (this file is useful if you would like to calculate TrEsp type of atomic transition charges by making use of cubegen utility in Gaussian, see Section 4.A.9 for detail).

Note that when ground state and excited state have different spin multiplicities, due to the orthonormality of spin coordinates, although in principle the transition density matrix should be zero, the outputted matrix is not, because Multiwfn only takes spatial part of the MOs into account during constructing the matrix.

The input files needed by present function have been detailedly described at the beginning of Section 3.21, namely you should load a file containing basis function information when Multiwfn boots up, and then load a file containing configuration coefficient information of excited states.

The example in Section 4.18.2.4 and Section 4.18.9 utilized present function. Information needed: See beginning of Section 3.21

Appendix: Derivation of the formula of evaluating TDM between two excited states The TDM between two excited states K and L in real space representation is

$$T^{K L}(\mathbf{r};\mathbf{r}^{\prime})=\int\Psi^{K}(\mathbf{r},\mathbf{r}_{2},...,\mathbf{r}_{N})\Psi^{L}(\mathbf{r}^{\prime},\mathbf{r}_{2},...,\mathbf{r}_{N})\mathrm{d}\mathbf{r}_{2}\ldots\mathrm{d}\mathbf{r}_{N}$$

where the excited state wavefunctions are represented by linear combination of singly excited Slater determinants

$$\begin{array}{r l}{\Psi^{K}=\displaystyle\sum_{i}^{\mathrm{o c c}}\displaystyle\sum_{a}^{\mathrm{v i r}}w_{i,a}^{K}\Phi_{i}^{a}}&{{}\quad\Psi^{L}=\displaystyle\sum_{j}^{\mathrm{o c c}}\displaystyle\sum_{b}^{\mathrm{v i r}}w_{j,b}^{L}\Phi_{j}^{b}}\end{array}$$

We have

$$T^{K L}(\mathbf{r};\mathbf{r}^{\prime})=\sum_{i}^{\mathrm{o c c}}\sum_{a}^{\mathrm{v i r}}w_{i,a}^{K}\sum_{j}^{\mathrm{o c c}}\sum_{b}^{\mathrm{v i r}}w_{j,b}^{L}\int\Phi_{i}^{a}(\mathbf{r},\mathbf{r}_{2},\ldots,\mathbf{r}_{N})\Phi_{j}^{b}(\mathbf{r}^{\prime},\mathbf{r}_{2},\ldots,\mathbf{r}_{N})\mathrm{d}\mathbf{r}_{2}\ldots\mathrm{d}\mathbf{r}_{N}$$

Slater-Condon rule shows that for an single-electron operator ℵ̂ = ∑ℎ𝑖𝑖, integral between two singly excited determinants, namely ⟨Φ𝑖 𝑎|ℵ̂|Φ𝑗 𝑏⟩, satisfies


$$\begin{aligned}&=0\quad\left(i\neq j,a\neq b\right)\\&=\left\langle a\middle|h\middle|b\right\rangle\quad\left(i=j,a\neq b\right)\\&=-\left\langle j\middle|h\middle|i\right\rangle\quad\left(i\neq j,a=b\right)\\&=\sum_{p}^{N}\left\langle p\middle|h\middle|p\right\rangle-\left\langle i\middle|h\middle|i\right\rangle+\left\langle a\middle|h\middle|a\right\rangle\quad\left(i=j,a=b\right)\end{aligned}$$

<!-- formula-ocr: formula_p291_190.png 已替换为LaTeX, 原图保留备查 -->

p


<!-- p.292 -->

Without performing the integral and view the h operator as 1, based on the above relations we have

$$T^{KL}(\mathbf{r};\mathbf{r}^{\prime})=\left\{\begin{aligned}0&\quad(i\neq j,a\neq b)\\ \sum_{i}\sum_{a}\sum_{b}w_{i,a}^{K}w_{i,b}^{L}\varphi_{a}(\mathbf{r})\varphi_{b}(\mathbf{r}^{\prime})&\quad(i=j,a\neq b)\\ -\sum_{i}\sum_{j}\sum_{a}w_{i,a}^{K}w_{j,a}^{L}\varphi_{j}(\mathbf{r})\varphi_{i}(\mathbf{r}^{\prime})&\quad(i\neq j,a=b)\\ \sum_{i}\sum_{a}w_{i,a}^{K}w_{i,a}^{L}\left[\sum_{p}^{N}\varphi_{p}(\mathbf{r})\varphi_{p}(\mathbf{r}^{\prime})-\varphi_{i}(\mathbf{r})\varphi_{i}(\mathbf{r}^{\prime})+\varphi_{a}(\mathbf{r})\varphi_{a}(\mathbf{r}^{\prime})\right]&\quad(i=j,a=b)\end{aligned}\right.$$

Given that


$$\begin{aligned}T^{KL}(\mathbf{r};\mathbf{r}^{\prime})=&\sum_{i}\sum_{a}\sum_{b}w_{i,a}^{K}w_{i,b}^{L}\varphi_{a}(\mathbf{r})\varphi_{b}(\mathbf{r}^{\prime})\\=&\sum_{i}\sum_{a}\sum_{b}w_{i,a}^{K}w_{i,b}^{L}\sum_{\mu}\sum_{\nu}C_{\mu a}C_{\nu b}\chi_{\mu}(\mathbf{r})\chi_{\nu}(\mathbf{r}^{\prime})\\Rightarrow P^{KL}=&\sum_{i}\sum_{a}\sum_{b}w_{i,a}^{K}w_{i,b}^{L}C_{\mu a}C_{\nu b}\end{aligned}$$

<!-- formula-ocr: formula_p292_191.png 已替换为LaTeX, 原图保留备查 -->

where χ is basis function, we can finally reach the formula or evaluating PKL shown earlier in this section. For example, in the case of $i=j$

$$T^{KL}(\mathbf{r};\mathbf{r}^{\prime})=\left\{\begin{aligned}0&\quad(i\neq j,a\neq b)\\ \sum_{i}\sum_{a}\sum_{b}w_{i,a}^{K}w_{i,b}^{L}\varphi_{a}(\mathbf{r})\varphi_{b}(\mathbf{r}^{\prime})&\quad(i=j,a\neq b)\\ -\sum_{i}\sum_{j}\sum_{a}w_{i,a}^{K}w_{j,a}^{L}\varphi_{j}(\mathbf{r})\varphi_{i}(\mathbf{r}^{\prime})&\quad(i\neq j,a=b)\\ \sum_{i}\sum_{a}w_{i,a}^{K}w_{i,a}^{L}\left[\sum_{p}^{N}\varphi_{p}(\mathbf{r})\varphi_{p}(\mathbf{r}^{\prime})-\varphi_{i}(\mathbf{r})\varphi_{i}(\mathbf{r}^{\prime})+\varphi_{a}(\mathbf{r})\varphi_{a}(\mathbf{r}^{\prime})\right]&\quad(i=j,a=b)\end{aligned}\right.$$


$$\mathbf{D}^{\mathrm{t r a n}}=\sum_{i,a}(w_{i,a}+w_{i,a}^{\prime})\langle\varphi_{i}\big|-\mathbf{r}\big|\varphi_{a}\rangle$$

<!-- formula-ocr: formula_p292_192.png 已替换为LaTeX, 原图保留备查 -->


### 3.21.10 Decompose transition electric/magnetic dipole moment as molecular orbital pair contributions (10)



Theoretical chemists often prefer to study electron excitations in terms of molecular orbital transitions, this function helps them in this respect. This function decomposes transition electric or magnetic dipole moment from ground state to an excited state of interest as molecular orbital pair contributions to provide users a deeper insight into electron excitation.

Theory As mentioned in Section 3.13.1, oscillator strength (f) of an electron excitation directly relates to the integral area of the corresponding absorption peak. f has direct relationship with transition electric dipole moment $\mathbf{D}^{\mathrm{tran}}$ (in atomic unit):

tran22||3fE=Δ×D

where ΔE denotes the transition energy between the two electronic states. Clearly, $\mathbf{D}^{\mathrm{tran}}$ is a crucial quantity of electron excitations and largely determines optical absorption. Dtran between ground state and an excited state is calculated as follows


$$\mathbf{D}^{\mathrm{tran}}=\sum_{i,a}(w_{i,a}+w_{i,a}^{\prime})\langle\varphi_{i}|-\mathbf{r}|\varphi_{a}\rangle$$

where i and a loop over all occupied and virtual MOs, respectively. w and w′ are configuration


<!-- p.293 -->

coefficient of excitations and de-excitations, respectively. φ denotes molecular orbital wavefunction. It is clear that the transition dipole moment can be straightforwardly decomposed into contribution of various MO pairs. Via such a decomposition, one can easily study why some excitations have relatively large oscillator strength and thus have strong absorption, and why some excitations only have small oscillator strength and thus they are difficult to observe in electronic spectrum.

Transition magnetic dipole moment $\mathbf{M}^{\mathrm{tran}}$ is also an important quantity of electron excitation, because Mtran and Dtran collectively determine rotatory strength, which determines electronic circular dichroism (ECD) and circularly polarized luminescence (CPL) spectra. Mtran between ground state and an excited state is calculated as follows


$$\mathbf{M}^{\mathrm{t r a n}}=\sum_{i,a}(w_{i,a}-w_{i,a}^{\prime})\left\langle\varphi_{i}\left|\mathbf{r}\times\nabla\right|\varphi_{a}\right\rangle$$

<!-- formula-ocr: formula_p293_194.png 已替换为LaTeX, 原图保留备查 -->

Obviously, $\mathbf{M}^{\mathrm{tran}}$ can also be straightforwardly decomposed into contribution of various MO pairs.

Usage The input files needed by present function have been detailedly described at the beginning of Section 3.21, namely you should load a file containing basis function information when Multiwfn boots up, and then load a file containing configuration coefficient information of excited states when you enter this function.

In this function, you will be asked to select the type of transition dipole moment, and will be prompted to choose the excited state for which the transition dipole moment will be decomposed as MO pairs, then a menu appears. You can select corresponding option to make Multiwfn output contribution of every MO pair to transdip.txt in current folder, or let Multiwfn sort the MO pairs according to their contributions to transition dipole moment and then output the first few or dozens of terms, so that you can immediately identify the most important MO transitions. In addition, you can request Multiwfn to only output MO pairs with contribution larger than a given threshold.

An example of this function is given in Section 4.18.10. Information needed: See beginning of Section 3.21


### 3.21.11 Decompose transition electric/magnetic dipole moment as basis function and atom contributions (11)



This function is used to decompose the transition electric or magnetic dipole moment between ground state and a selected excited state, or between two excited states, into contributions from various basis functions and atoms. The result is exported to trdipcontri.txt. Therefore, from which you can easily examine which part of the system has significant impact on excitation properties such as oscillator strength.

There are many possible ways to realize the decomposition. In this function Mulliken-like partition is employed due to its simplicity. The contribution of basis function μ to transition electric dipole moment vector is evaluated as

$$\mathbf{D}_{\mu}=P_{\mu\mu}^{\mathrm{t r a n}}\left\langle\boldsymbol{\chi}_{\mu}\middle|-\mathbf{r}\middle|\boldsymbol{\chi}_{\mu}\right\rangle+\frac{1}{2}\sum_{\nu\neq\mu}\left(P_{\mu\nu}^{\mathrm{t r a n}}\left\langle\boldsymbol{\chi}_{\mu}\middle|-\mathbf{r}\middle|\boldsymbol{\chi}_{\nu}\right\rangle+P_{\nu\mu}^{\mathrm{t r a n}}\left\langle\boldsymbol{\chi}_{\nu}\middle|-\mathbf{r}\middle|\boldsymbol{\chi}_{\mu}\right\rangle\right)$$


<!-- p.294 -->

and the contribution of basis function μ to transition magnetic dipole moment vector is evaluated as

$$\mathbf{M}_{\mu}=P_{\mu\mu}^{\mathrm{t r a n}}\left\langle\boldsymbol{\chi}_{\mu}\middle|\mathbf{r}\times\nabla\middle|\boldsymbol{\chi}_{\mu}\right\rangle+\frac{1}{2}\sum_{\nu\neq\mu}\left(P_{\mu\nu}^{\mathrm{t r a n}}\left\langle\boldsymbol{\chi}_{\mu}\middle|\mathbf{r}\times\nabla\middle|\boldsymbol{\chi}_{\nu}\right\rangle+P_{\nu\mu}^{\mathrm{t r a n}}\left\langle\boldsymbol{\chi}_{\nu}\middle|\mathbf{r}\times\nabla\middle|\boldsymbol{\chi}_{\mu}\right\rangle\right)$$

where Ptran is transition density matrix from ground state to the excited state of interest. The contribution from an atom is simply the sum of the contribution from the basis functions belonging to it.

Since Mulliken partition is incompatible with diffuse functions, the decomposition result is unreliable if diffuse functions are presented in the basis set you used. In this case, the best way to study contribution from various atoms is visualizing the transition dipole moment density (see Section 3.21.1).

This function also asks you if outputting atom transition dipole moment matrix, if you choose y, then X, Y, Z components of the matrix will be exported to AAtrdipX.txt, AAtrdipY.txt, AAtrdipZ.txt in current folder, respectively, the matrix elements are defined as follows (I take atom-atom contribution matrix of transition electric dipole moment as example, the matrix for transition magnetic dipole moment is defined similarly and thus not explicitly shown here)


$$D_{A,B}^{X}=\sum_{\mu\in A}\sum_{\nu\in B}P_{\mu\nu}^{\mathrm{t r a n}}\left\langle\chi_{\mu}\right|-x\left|\chi_{\mu}\right\rangle$$

<!-- formula-ocr: formula_p294_195.png 已替换为LaTeX, 原图保留备查 -->

For example, the term $D_{A,B}^{X}$ 𝑋 corresponds to joint contribution of A-B atomic pair to X component of

transition dipole moment, the sum of all elements of DX equals X component of transition dipole moment of current system. Total transition dipole moment matrix (sum of square of X, Y, Z) is exported as AAtrdip.txt in current folder. All of these .txt files can be directly plotted as colored matrix map (heat map) by atom transition matrix plotting module (see Section 3.21.2 for detail).

The input files needed by present function have been detailedly described at the beginning of Section 3.21, namely you should load a file containing basis function information when Multiwfn boots up, and then load a file containing configuration coefficient information of excited states when you enter this function.

The example of Section 4.18.11 utilized this function. Information needed: See beginning of Section 3.21


### 3.21.12 Calculate Mulliken atomic transition charges (12)

This function is used to calculate atomic transition charges, which is useful for studying Coulomb coupling between ground state and excited state (exciton coupling) of two molecules, see e.g. J. Phys. Chem. B, 110, 17268 (2006) and Photosynth. Res., 111, 47 (2012).

Transition population of a basis function μ derived by Mulliken method is


$$\Theta_{\mu}^{\mathrm{t r a n}}=P_{\mu\mu}^{\mathrm{t r a n}}+\sum_{\nu\neq\mu}S_{\mu\nu}(P_{\mu\nu}^{\mathrm{t r a n}}+P_{\nu\mu}^{\mathrm{t r a n}})/2$$

<!-- formula-ocr: formula_p294_196.png 已替换为LaTeX, 原图保留备查 -->


<!-- p.295 -->

So, the Mulliken atomic transition charge of atom A should be μμ∈−Θ . Sum of all atomic A tran

transition charges must be zero because the total number of electrons keeps unchanged during electron excitation.

The input files needed by present function have been detailedly described at the beginning of Section 3.21, namely you should load a file containing basis function information when Multiwfn boots up, and then load a file containing configuration coefficient information of excited states when you enter this function. After that, you should choose the excited state for which the Mulliken transition charges will be calculated. Then the result will be outputted to atmtrchg.chg file in current folder, the format of this kind of file has been introduced in Section 2.5, the last column of this file corresponds to the transition charges.

Below is an example of the calculation. Boot up Multiwfn and input examples\excit\N-phenylpyrrole.fch

!!! terminal "Multiwfn session"

    - **18** — Electron excitation analysis
    - **12** — Calculate Mulliken transition charges N-phenylpyrrole.out
    - **3** — Study the transition from ground state to the third excited state Then you will find atmtrchg.chg in current folder. Note that in Multiwfn it is also possible to calculate the TrEsp (transition charge from electrostatic potential) introduced in J. Phys. Chem. B, 110, 17268 (2006), which is derived by ESP fitting method based on transition density. See Section 4.A.9 on how to do this. For studying exciton coupling purpose, TrEsp should work better than Mulliken atomic transition charge, but for large systems, cost of evaluating the former is is significantly higher than the latter.

Information needed: See beginning of Section 3.21


### 3.21.13 Generate natural orbitals of specific excited states (13)

This function is used to generate natural orbitals (NOs) for a batch of selected excited states, and then export the NOs as .mwfn file. After that, if you want to perform wavefunction analysis for an excited state, you can simply load corresponding .mwfn file. Of course, you can also calculate e.g. density difference between two excited states using corresponding two .mwfn files via custom operation feature of main functions 3, 4 and 5.

To use this function, you should load a file containing basis function information, and then load a file containing configuration coefficients when you enter this file, see beginning of Section 3.21 for detail. After that, you will be prompted to input the indices of the excited state for which NOs will be generated. For each selected excited state, the program will do below steps:

(1) Generating density matrix of excited state $\mathbf{P}^{\mathrm{ES}}$ (note that the density matrix constructed in this way corresponds to unrelaxed density):


$$\mathbf{P}^{\mathrm{E S}}=\mathbf{P}^{\mathrm{G S}}+\Delta\mathbf{P}^{\mathrm{l o c a l}}+\Delta\mathbf{P}^{\mathrm{c r o s s}}$$

<!-- formula-ocr: formula_p295_197.png 已替换为LaTeX, 原图保留备查 -->

where PGS is density matrix of ground state, ΔPlocal and ΔPcross are local part and cross part of


<!-- p.296 -->

variation of density matrix of excited state with respect to ground state, respectively.

The local part is calculated as

$$\begin{array}{r}{\Delta\mathbf{P}^{\mathrm{l o c a l}}=\displaystyle\sum_{i\to a}(w_{i}^{a})^{2}(-\mathbf{P}^{i i}+\mathbf{P}^{a a})+\sum_{i\leftarrow a}(w_{i}^{a})^{2}(-\mathbf{P}^{a a}+\mathbf{P}^{i i}).}\end{array}$$

where i and j loop over all occupied MOs, while a and b loop over all virtual MOs. The matrix like Prs is evaluated as follows, where Cr is column vector of expansion coefficients of MO r

rs=PC C Trs

The cross part is calculated as

$$\begin{array}{r}{\Delta\mathbf{P}^{\mathrm{l o c a l}}=\displaystyle\sum_{i\to a}(w_{i}^{a})^{2}(-\mathbf{P}^{i i}+\mathbf{P}^{a a})+\sum_{i\leftarrow a}(w_{i}^{a})^{2}(-\mathbf{P}^{a a}+\mathbf{P}^{i i}).}\end{array}$$

(2) Diagonalizing the PES to yield NOs. Each NO is an eigenvector of PES, the accompanied eigenvalue is occupation number of the NO.

(3) Exporting information of basis function and NOs to .molden file. If the excited state you selected is 2, then they will be exported as NO_0002.mwfn in current folder.

This function supports both closed-shell and open-shell reference states. For the latter case, density matrices of alpha and beta spins are calculated separately, and natural orbitals of alpha and beta spins are generated and exported to the .mwfn file respectively.

The example given in Section 4.18.13 fully utilizes this function. In addition, in http://sobereva.com/wfnbbs/viewtopic.php?pid=2446 I illustrated the full steps of generating natural orbitals for states solved by SF-TDDFT calculation of ORCA program.

Information needed: See beginning of Section 3.21


### 3.21.14 Calculate Λ index to characterize electron excitation (14)

Theory

In the paper J. Chem. Phys., 128, 044118 (2008), Λ index was proposed to distinguish types of electron excitations. The form of the Λ index and the $\Delta r$ index (see Section 3.21.4) is very similar. Λ index can be expressed as


$$\begin{array}{r}{\Delta\mathbf{P}^{\mathrm{l o c a l}}=\displaystyle\sum_{i\to a}(w_{i}^{a})^{2}(-\mathbf{P}^{i i}+\mathbf{P}^{a a})+\sum_{i\leftarrow a}(w_{i}^{a})^{2}(-\mathbf{P}^{a a}+\mathbf{P}^{i i}).}\end{array}$$

<!-- formula-ocr: formula_p296_198.png 已替换为LaTeX, 原图保留备查 -->

where a iΛ is contribution of MO transition between i and a to the Λ index:


$$\Lambda_{i}^{a}=\frac{(K_{i}^{a})^{2}}{\displaystyle\sum_{i,a}(K_{i}^{a})^{2}}\int\bigl|\varphi_{i}(\mathbf{r})\bigr|\bigl|\varphi_{a}(\mathbf{r})\bigr|\mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p296_199.png 已替换为LaTeX, 原图保留备查 -->

All quantities involved in above expression are identical those in $\Delta r$ index. The integral corresponds to overlap extent of the MO i and a, it is calculated numerically via Becke's multicenter grid-based


<!-- p.297 -->

integration approach. The default grid is a good compromise between cost and accuracy; if you want to change it, you can set "iautogrid" in `settings.ini` to 0 and then specify "radpot" and "sphpot" in

`settings.ini` as your expected values. Note that calculation cost of the Λ index is by far higher than $\Delta r$ index, because the above numerical integral step is expensive, especially for large systems.

The theoretical lower and upper limits of the Λ index are 0.0 and 1.0, respectively; the former (latter) corresponds to the case that hole and electron are completely separated (perfectly overlapped).

As $\Delta r$ index, the Λ index is useful for distinguishing type of electron excitations. Notice that their intrinsic characteristics are different, the Δr index is essentially an indicator of configuration weighted orbital separation distance, while Λ index reflects configuration weighted orbital overlapping extent. In some sense, the physical nature of Δr and Λ indices are similar to the D and Sr indices defined in hole-electron analysis framework, respectively (see Section 3.21.1.1), however I believe that the D and Sr indices are more reasonable, since their physical meanings are clearer and couplings between different configurations are fully taken into account. Therefore, without special reasons, using D and Sr indices is more recommended.

It is worth to mention that if an electron excitation can be perfectly represented by one pair of

MO transition, then the Λ index and Sr index defined in hole-electron analysis framework will be exactly identical in principle:

$$\begin{aligned}\Lambda=&\int\left|\varphi_{i}(\mathbf{r})\right|\left|\varphi_{a}(\mathbf{r})\right|\mathrm{d}\mathbf{r}\\S_{\mathrm{r}}=&\int\sqrt{\rho^{\mathrm{hole}}(\mathbf{r})\rho^{\mathrm{ele}}(\mathbf{r})}\mathrm{d}\mathbf{r}=\int\sqrt{\left|\varphi_{i}(\mathbf{r})\right|^{2}\left|\varphi_{a}(\mathbf{r})\right|^{2}}\mathrm{d}\mathbf{r}=\int\left|\varphi_{i}(\mathbf{r})\right|\left|\varphi_{a}(\mathbf{r})\right|\mathrm{d}\mathbf{r}\end{aligned}$$

However, their values outputted by Multiwfn should be marginally different, since they are evaluated based on different numerical integration algorithms.

Usage The input files needed by present module have been detailedly described at the beginning of Section 3.21, namely you should load a file containing basis function information when Multiwfn boots up, and then load a file containing configuration coefficient information of excited states.

After entering present function (subfunction 14 of main function 18), the matrix containing overlap integral between norms of all occupied and unoccupied MOs will be evaluated first, then

you will be prompted to select the excited states for which the Λ will be calculated, then the results will be printed on screen immediately.

If you only selected one state, then Multiwfn will ask you to choose if decomposing the Λ into orbital pair contributions. If you inputted e.g. 0.01, then orbital pairs which have contribution to Λ larger than 0.01 will be printed.

An example of present function is provided as Section 4.18.4. Information needed: See beginning of Section 3.21.


### 3.21.15 Print major MO transitions in all excited states

This is a useful function used to show major MO transitions for all excited states, so that you


<!-- p.298 -->

can quickly recognize basic characteristics of various excited states in terms of MOs.

Below is an example. Boot up Multiwfn and input examples\excit\D-pi-A.out

!!! terminal "Multiwfn session"

    - **Output file of TDDFT task of Gaussian 18** — Electron excitation analysis
    - **15** — The present function You can see the following information immediately, including excitation energy, spin multiplicity, notable MO transitions and their contributions of each excited state.


```text
##   1   3.9069 eV    317.35 nm   f=  0.01880   Spin multiplicity= 1:
   H-4 -> L 81.9%, H-4 -> L+2 12.1%
 #   2   4.0624 eV    305.20 nm   f=  0.63550   Spin multiplicity= 1:
   H -> L 86.0%, H-3 -> L 5.3%
 #   3   4.4166 eV    280.72 nm   f=  0.00010   Spin multiplicity= 1:
   H-6 -> L 85.3%, H-6 -> L+2 11.9%
 #   4   4.7912 eV    258.77 nm   f=  0.01350   Spin multiplicity= 1:
   H-2 -> L 54.5%, H -> L+1 27.6%, H-3 -> L+1 6.4%
 #   5   4.8872 eV    253.69 nm   f=  0.00790   Spin multiplicity= 1:
   H -> L+3 57.3%, H-2 -> L 17.0%, H-1 -> L+2 8.8%, H-1 -> L 8.0%
```

From above output, for example, we can find HOMO-4 → LUMO transition contributes 81.9% to the excitation from ground state to S1 state.

For open-shell cases, orbital spins are explicitly indicated. For example, Ha-4 means

HOMOalpha−4.

By default, only MO transitions with contribution larger than 5% are printed. The printing threshold corresponds to 10 times of "compthres" parameter in `settings.ini`.

You can use output file of ZINDO/CIS/TDHF/TDA-DFT/TDDFT task of Gaussian, ORCA, GAMESS-US/Firefly as input file. Unlike most functions in main function 18, the file containing basis function information is not needed in the present function.


### 3.21.16 Charge-transfer spectrum (CTS) analysis

This function is used to calculate data for plotting the charge-transfer spectrum (CTS). At the meantime, major characters given by IFCT analysis of all excited states are presented.

The idea of CTS was firstly proposed by me in Carbon, 187, 78-85 (2022) DOI: 10.1016/j.carbon.2021.11.005 for studying spectrum nature of C18@Li complex, please cite this paper if this method is employed in your study.

Theory of CTS Please first recall the hole-electron analysis introduced in Section 3.21.1. For every excited state, it is able to calculate hole and electron distributions. Using Mulliken-like partition or Hirshfeld partition, contributions of various fragments to hole and electron can be calculated. Then, according to the IFCT analysis introduced in Section 3.21.8, amount of intrafragment electron redistribution and amount of interfragment electron transfer can be calculated. Sum of all redistribution terms and electron transfer terms of an excited state equals unity.

As introduced in Section 3.13.1, UV-Vis spectrum is obtained via broadening excitation energies (Eexc) and oscillator strength (f) of all excited states by Gaussian function (G).


<!-- p.299 -->

Mathematically, the spectrum curve is expressed as


$$\varepsilon(E)=c\sum_{i}f_{i}G(E-E_{i}^{\mathrm{exc}})$$

<!-- formula-ocr: formula_p299_200.png 已替换为LaTeX, 原图保留备查 -->

where ε(E) is molar absorption coefficient at energy E. i loops over all excited states. c is a constant.

The CTS aims at graphically exhibit contribution of electron transfer component and redistribution component to UV-Vis spectrum. The idea is very simple, and only the f will be modified. Assume there are two fragments, A and B, then the absorption curve of CTS corresponding to electron transfer from A to B is expressed as


$$\mathcal{E}_{A,B}(E)=\sum_{i}f_{i}Q_{i}^{A,B}G(E-E_{i}^{\mathrm{e x c}})$$

<!-- formula-ocr: formula_p299_201.png 已替换为LaTeX, 原图保留备查 -->

𝐴,𝐵 is amount of electron transfer from A to B of excited state i. The absorption curve of CTS corresponding to electron redistribution within fragment A is expressed as where 𝑄𝑖


$$\mathcal{E}_{A,A}(E)=\sum_{i}f_{i}Q_{i}^{A,A}G(E-E_{i}^{\mathrm{e x c}})$$

<!-- formula-ocr: formula_p299_202.png 已替换为LaTeX, 原图保留备查 -->

where 𝑄𝑖 𝐵,𝐴= 1 (see Section 3.21.8 for proof), sum of four types of charge-transfer spectra is exactly the UV-Vis spectrum: 𝐴,𝐴 is amount of electron redistribution within fragment A of excited state i. Because 𝑄𝑖 𝐴,𝐴+ 𝑄𝑖 𝐵,𝐵+ 𝑄𝑖 𝐴,𝐵+ 𝑄𝑖

,,,,( )( )( )( )( )A AB BA BB AEEEEEεεεεε+++=

It is obvious that charge-transfer spectrum is able to make the underlying nature of significant peaks of UV-Vis spectrum very easy to recognize. In order words, the total UV-Vis spectrum is decomposed as different subparts corresponding to different physical natures.

Procedure of plotting CTS (1) Prepare input files for present function. The input file is exactly identical to hole-electron or IFCT analysis, namely a file containing basis function information and a file containing configuration coefficients of excited states. See Section 3.21.A for detail of generation of these files via quantum chemistry programs.

(2) Calculate IFCT data and generate data files used for plotting CTS. Boot up Multiwfn and load the file containing basis function information. Enter present function (subfunction 16 of main function 18). Input the number of fragments (there is no upper limit), input atomic indices for each fragment, then input the path of the file containing configuration coefficients. Finally, choose the method for calculating fragment contributions to hole and electron. After that, contribution to hole and electron of each fragment will be computed for every excited state in turn.

Hint: If there are very large number of atoms and excited states and diffuse functions were not employed, choosing Mulliken method is suggested because it is fairly fast. However, if diffuse functions were employed, you have to choose the more expensive but more robust Hirshfeld method.

After the calculation is complete, you can find IFCTdata.txt in current folder, which contains full IFCT data for all excited states. The IFCTmajor.txt in current folder records major IFCT terms (those with contribution larger than 5%), from which you can easily recognize major characters of all excited states. You also have a batch of files in the newly created "CT_multiple" subfolder of current folder; in which the CT_multiple.txt is the file used in spectrum plotting module of Multiwfn; if you open it by text editor you can see it contains path of many files with labels. Specifically, the total_spectrum.txt is used to plot UV-Vis spectrum, the files with "ET_" prefix is used to plot interfragment electron transfer spectra, the files with "Redis_" prefix is used to plot intrafragment


<!-- p.300 -->

electron redistribution spectra. Note that when the "CT_multiple" subfolder is moved, you should also manually modify the paths of the included files.

(3) Boot up Multiwfn, use the CT_multiple.txt in "CT_multiple" subfolder as input file, then enter main function 11, select "UV-Vis", and choose option 0 to plot the spectrum. You will find the interfragment electron transfer spectrum and intrafragment electron redistribution spectrum together with UV-Vis spectrum are shown. You can also use the rich options in the interface to improve the graph, see Section 3.13.3 for explanation.

An example of calculating IFCT data for a batch of excited states and plotting CTS is given in Section 4.18.16.


### 3.21.17 Electron density polarization analysis based on electron excitations



1. Introduction

An applied external potential, $\delta v$(r), can cause polarization of electron density of a chemical system. Usually, the corresponding variation of electron density, which will be referred to as density

polarization ($\rho_{\mathrm{pol}}$) later, can be obtained by taking difference between the densities obtained with and without $\delta v$. Obviously, this needs two single point calculations to generate wavefunction files of the respective status.

J. Phys. Chem. A, 124, 633 (2020) proposed a novel way of evaluating and analyzing $\rho_{\mathrm{pol}}$ based on electron excitation calculations (e.g. TDDFT). Currently only the $\delta v$ consisting of one or more point charges are explored. There are some practical applications illustrated in this paper, also this method has been employed in J. Comput. Chem., 42, 1118 (2021) to study substitution effect on the performance of Mo-oxo catalyst. This method has two unique advantages:

(1) After a regular electron excitation calculation with a sufficient number of excited states,

one can easily obtain the $\rho_{\mathrm{pol}}$ induced by an arbitrary time-independent $\delta v$. That means one does not need to perform a quantum chemistry calculation for each δv of interest. But note that the ρpol obtained via this method is less accurate than that obtained via the aforementioned traditional method, because this method was derived based on the low-order perturbation theory. This also

implies that the $\delta v$ should not be too strong. For example, it may be a point charge of no more than 0.1 e, while 0.5 e may be too large unless it was placed far from the system.

(2) More importantly, this method is able to provide deep understanding of and chemical

insights into $\rho_{\mathrm{pol}}$ in terms of electron excitations. One can gain information about which excitation(s) contribute significantly to the ρpol, and discuss why the contributions are significant by further analyzing the distribution of the transition density of the excitations. In other words, this method

decomposes $\rho_{\mathrm{pol}}$ to reveal its nature.

2. Theory

According to perturbation theory, the ground state wavefunction perturbed by $\delta v$ can be linearly expanded by the ground (k=0) and excited states (k>0) without the perturbation at the same geometry:


$$|\Psi_{0}\rangle=\sum_{k=0}^{\infty}c_{k}|\psi_{k}^{(0)}\rangle$$

<!-- formula-ocr: formula_p300_203.png 已替换为LaTeX, 原图保留备查 -->


<!-- p.301 -->

where


$$c_{k}=-\frac{\left\langle\Psi_{k}^{(0)}\right|\delta v\left|\Psi_{0}^{(0)}\right\rangle}{E_{k}^{(0)}-E_{0}^{(0)}}=-\frac{\int\rho_{0}^{k}(\mathbf{r})\delta v(\mathbf{r})\mathrm{d}\mathbf{r}}{E_{k}^{(0)}-E_{0}^{(0)}}$$

<!-- formula-ocr: formula_p301_204.png 已替换为LaTeX, 原图保留备查 -->

𝑘 is the transition density between ground state and this excited state. Definition of transition density can be found in Section 3.21.1.1. Clearly, for an excited state, the smaller the excitation energy, and the larger the effective overlap (with care of phase cancellation) between the distribution of transition density and external potential, the larger the magnitude of the coefficient. Note that the magnitude is much more sensitive to the latter. The square of the coefficients of k>0 can be understood as the contributions from the electronic states. The square of the coefficient of ground state (k=0) is always close to 1.0 because in which the denominator is the excitation energy of excited state k, while 𝜌0

of the assumption of weak δv.

2 ≈1, the density polarization, which is the difference between the electron density with and without the perturbation (𝜌pert and 𝜌0), can be evaluated as follows Further, with the condition 𝑐0


$$\rho_{\mathrm{p o l}}(\mathbf{r})=\rho_{\mathrm{p e r t}}(\mathbf{r})-\rho_{0}(\mathbf{r})\approx2\sum_{k=1}^{\infty}c_{k}\rho_{0}^{k}(\mathbf{r})$$

<!-- formula-ocr: formula_p301_205.png 已替换为LaTeX, 原图保留备查 -->

Integral of ρpol over the whole space must be zero since the perturbation does not alter the number of electrons, nonetheless, it is useful to characterize the amount of electrons polarized (δN); to this aim, one can integrate positive or negative part of ρpol, or equivalently, calculate it as 𝛿𝑁=


$$\delta N = \frac{1}{2} \int |\rho_{\mathrm{pol}}(\mathbf{r})| \mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p301_206.png 已替换为LaTeX, 原图保留备查 -->

Finally, according to the second-order perturbation theory, the first-order perturbation correction energy represents the interaction energy between the external potential and permanent electron distribution


$$E^{(1)}=\left\langle\Psi_{0}^{(0)}\right|\delta v\left|\Psi_{0}^{(0)}\right\rangle=\int\rho_{0}(\mathbf{r})\delta v(\mathbf{r})\mathrm{d}\mathbf{r}$$

<!-- formula-ocr: formula_p301_207.png 已替换为LaTeX, 原图保留备查 -->

and the second-order correction energy represents the energetic stabilization experienced by the system by distorting its electron density (caused by mix of ground and excited states) in response to the perturbation


$$E^{(2)}=\sum_{k>0}^{\infty}\frac{\left|\left\langle\Psi_{k}^{(0)}\right|\delta v\left|\Psi_{0}^{(0)}\right\rangle\right|^{2}}{E_{0}^{(0)}-E_{k}^{(0)}}=\sum_{k>0}^{\infty}c_{k}^{2}\left(E_{0}^{(0)}-E_{k}^{(0)}\right)$$

<!-- formula-ocr: formula_p301_208.png 已替换为LaTeX, 原图保留备查 -->

It is seen that $E^{(2)}$ can be exactly decomposed into contributions of different excited states, from which one can recognize the significance of different excited states in the response to the perturbation from an energetic point of view.

3. Practical guidance Arbitrary number of point charges can be taken as the external potential, which is expressed as $\delta\boldsymbol{v}(\mathbf{r}) = -\sum_{i}^{n} q_{i}/|\mathbf{r} - \mathbf{R}_{i}|$⁄𝑛𝑖 , where qi and Ri are value and coordinate vector of point charge i, respectively. The negative sign comes from the fact that electron carries charge of -1 e. The point charge(s) can be placed anywhere as long as you believe it is meaningful. Please check the original paper for illustrative applications. For example, to approximately mimic the effects of an electron-withdrawing (electron-donating) substituent, one can place a point charge of +0.1 e (-0.1 e) at the nuclear position of the atom linking to the substituent, see J. Comput. Chem., 42, 1118 (2021) for


<!-- p.302 -->

instance. For another example, to examine the effect of a Lewis base approaching the system on the electron distribution, a slight negative point charge can be placed at the position of the Lewis base atom in the expected reaction complex.

Theoretically, any methods for calculating excited states may be used in this analysis as long as excited state wavefunction is available. However, in the present implementation, only the methods based on singly excited configurations, are supported, such as CIS and TDDFT. Usually TDDFT with a proper DFT functional is the preferential choice. Generally, I recommend using

ωB97XD or CAM-B3LYP in combination with def-TZVP.

In the expressions given above, infinite number of excited states are involved, clearly this is inaccessible in practical studies. The larger the number of excited states calculated, the higher the computational cost in the quantum chemistry program and Multiwfn, while the lower the risk that important excited states are overlooked. In the original papers and J. Comput. Chem., 42, 1118 (2021), 50 excited states were taken into account, this choice is likely to be a good starting point, but larger number of states may be needed in certain cases.

In Multiwfn, the integral involved in evaluating {$\{c_k\}$} is calculated based on uniform grids. The smaller the grid spacing, the better the accuracy, while the higher the cost. For a small system, I suggest using the very fine grid spacing 0.1 or 0.15 Bohr, while for a large system, considering the high computational cost, a larger grid spacing such as 0.2 or 0.25 Bohr has to be used (to guarantee numerical accuracy, performing a convergence test of grid spacing is suggested).

4. Usage

The present function is able to calculate $\rho_{\mathrm{pol}}$, {$\{c_k\}$}, E(2), δN. The needed input files for this analysis are exactly the same as those described in Section 3.21.A.

The steps of using this function are as follows: (1) Load a file containing basis function information when Multiwfn boots up. For example, the .fchk file resulting from TDDFT calculation of Gaussian

(2) Enter subfunction 17 of main function 18 (3) Input total number of point charges, and then input X, Y, Z coordinates and charge value for each of them

(4) Setting up grid (5) Load a file containing the configuration coefficients from an excited state calculation, such as Gaussian output file of TDDFT task

Then Multiwfn starts to calculate data for each excited state. Once calculation is finished,

excitation energy, $\{c_k\}$ and E(2) of each excited state is shown on screen, and then total E(2) and δN are given. Integral of $\rho_{\mathrm{pol}}$ over the whole space is also shown, the more it is close to 0, indicating that the more the current grid quality is satisfactory.

Later, post-processing menu appears, in which $\rho_{\mathrm{pol}}$, δv, and transition densities of the excited states of interest (for example, the ones with largest |$\{c_k\}$|), and be directly plotted as isosurface maps, or be exported as .cub files.

An example of this function is given in Section 4.18.17.


<!-- p.303 -->


### 3.21.18 Calculate ECD/CPL dissymmetry factor (g) for chiral systems

The function introduced in this section enables one to very easily obtain dissymmetry factor (g) and relevant quantities involved in ECD/CPL of chiral systems based on output file of Gaussian or ORCA, and at the meantime the transition electronic/magnetic dipole moments (𝛍tran and 𝐦tran) can be easily and intuitively visualized in VMD.

Background Theory

(1) Absorption case Chiral systems have different absorptions for left and right circularly polarized lights due to electronic excitations, which is reflected by electronic circular dichroism (ECD). For each excited state, the dissymmetry factor of absorption ($g_{abs}$) is defined as


$$g_{\mathrm{a b s}}=\frac{\varepsilon_{\mathrm{L}}-\varepsilon_{\mathrm{R}}}{\frac{1}{2}(\varepsilon_{\mathrm{L}}+\varepsilon_{\mathrm{R}})}$$

<!-- formula-ocr: formula_p303_209.png 已替换为LaTeX, 原图保留备查 -->

where 𝜀L and 𝜀R are molecular absorption coefficients for left and right circularly polarized lights, respectively.

$g_{abs}$ can be evaluated as based on rotatory strength (R) and dipole strength (D)


$$g_{abs}=4\frac{R}{D}$$

<!-- formula-ocr: formula_p303_210.png 已替换为LaTeX, 原图保留备查 -->

Rotatory strength is calculated as

tran|cos𝜃 where θ is the angle between 𝛍0𝑣 tran) For real wavefunctions, 𝐦𝑣0 tran, so 𝑅= −Im(𝛍0𝑣 tran = −𝐦0𝑣 tran = ⟨Ψ0|−𝐫|Ψ𝑣⟩ and 𝐦0𝑣 tran ∙𝐦0𝑣 𝑅= Im(𝛍0𝑣 tran) = −|𝛍0𝑣 tran ∙𝐦𝑣0 tran||𝐦0𝑣 tran = 1 2𝑖⟨Ψ0|𝐫× 𝛁|Ψ𝑣⟩ , which are

respectively the transition electric dipole moment and transition magnetic dipole moment from ground state (0) to an excited state (v).

Dipole strength is calculated as

tran|2 𝛍tran of 1 a.u. corresponds to 2.541746×10-18 esu·cm, 𝐦tran of 1 a.u. corresponds to 1.85480201566(56)×10-20 erg/Gauss, so R of 1 a.u. corresponds to 2.541746×1.85480201566×10-38 erg·esu·cm/Gauss, where erg·esu·cm/Gauss is cgs unit. Usually, R is reported in the unit of 10-40 cgs. Actually 1 esu·cm = 1 erg/Gauss = 1 g1/2·cm5/2/s, so it is easy to understand why g is dimensionless. 𝐷= |𝛍0𝑣 tran|2 + |𝐦0𝑣

Because magnitude of 𝐦tran is usually significantly smaller than 𝛍tran, at least for organic systems, an approximation is often used in literature:

𝑔≈−4 |𝐦0𝑣 tran|cos𝜃|𝛍0𝑣 tran|

tran outputted by electronic excitation calculation of Gaussian actually corresponds to ⟨Ψ0|𝐫× 𝛁|Ψ𝑣⟩, and that outputted by ORCA corresponds to 1 It should be noticed that the 𝐦0𝑣 2⟨Ψ0|𝐫× 𝛁|Ψ𝑣⟩.

Many papers missed the negative sign, leading to incorrect inverted result.

(2) Emission case Chiral systems also have circularly polarized luminescence (CPL) phenomenon. The dissymmetry factor of luminescence (glum), also known as CPL dissymmetry factor (gCPL), is defined


<!-- p.304 -->

as


$$g_{\mathrm{lum}}=\frac{I_{\mathrm{L}}-I_{\mathrm{R}}}{\frac{1}{2}\left(I_{\mathrm{L}}+I_{\mathrm{R}}\right)}$$

<!-- formula-ocr: formula_p304_211.png 已替换为LaTeX, 原图保留备查 -->

where 𝐼L and 𝐼R are strength of the left and right circularly polarized luminescence, respectively. According to Kasha’s rule, organic systems usually only have one emission state, which corresponds to the lowest singlet excited state (S1). Like gabs, glum is also theoretically calculated as 4𝑅/𝐷, but it should only be calculated for the emission state at optimized minimum structure of this excited state.

It is important to note that at exactly the same geometry (geometry relaxation is fully ignored), according to the property of operator, with the assumption that wavefunctions are real, absorption and emission processes have the same transition electric dipole moment, namely 𝛍𝑣0 tran , while their transition magnetic dipole moments have opposite directions, namely 𝐦𝑣0 tran. However, one should never naively substitute these relationships into the aforementioned formula tran = −𝐦0𝑣 tran = 𝛍0𝑣

to reach the conclusion that $R_{\mathrm{lum}}$ of S1→S0 equals negative value of Rabs of S0→S1. In fact, Rabs = Rlum, and thus gabs = glum, due to the physical definition of the rotatory strength of absorption and emission process (somewhat involved, I will not go into detail here). In practice, due to the geometry relaxation between S0 and S1 minima, it is frequently observed that Rabs and Rlum have different signs.

I found many papers ignored the points mentioned here, making the glum or relevant intermediate data presented in the papers incorrect, especially the sign of $R_{\mathrm{lum}}$ and/or direction of transition magnetic dipole moment of CPL process are incorrectly inverted.

Usage To use this function, input file should be the output file of electronic excitation task (typically TDDFT) of Gaussian or ORCA. For CPL case, output file of geometry optimization task of emission state is also acceptable as Multiwfn automatically loads the data outputted last time (corresponding to minimum structure of emission state). After entering subfunction 18 of main function 18, Multiwfn will load transition electric and magnetic dipole moments from the output file, then

calculate and print $|\mu^{\text{tran}}|, |\mathbf{m}^{\text{tran}}|, \theta, \cos(\theta), R, g$ for all excited states. You need to distinguish the situation for ECD and CPL cases:

·For ECD: Electronic excitation calculation should be performed at minimum structure of ground state, and you should select “1 This study is for ECD” after entering this function.

·For CPL: Electronic excitation calculation should be performed at minimum structure of actual emission state (can usually be determined by Kasha’s rule), and you should select “1 This study is for CPL” after entering this function, which inverts the loaded transition magnetic dipole moment (calculation of rotatory strength is not affected by this treatment due to the aforementioned reason). Evidently, only the printed data corresponding to the actual emission state is meaningful.

In the post-processing menu, you can select option 1 to generate a plotting script of VMD, and if you execute the script in VMD, a customized command emtran will be available. If you run for example emtran 3, then 𝛍tran and 𝐦tran of the 3rd excited state will be drawn in the graphical window as red and cyan arrows, respectively, so that you can intuitively understand their orientations. You can also supplement arguments to this command to control arrow length, radius, and shift of arrow centers, please check comment lines at the top of the script for full description of the usage.
