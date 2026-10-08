# 3.24 Energy decomposition analysis (21)

> Multiwfn manual, p.333–340. Images: `../imgs/`.

---

<!-- p.333 -->

for trajectory frames.

To perform amIGM analysis, you should provide a multiple frame .xyz file recording the molecular dynamics trajectory as input file, then enter subfunction -12 of main function 20, then define fragments for amIGM analysis like the standard mIGM/IGM analysis, then choose the range of frames to be considered, and finally define a proper box for calculating grid data. After that, various grid data will be calculated, and post-processing menu appears. In this menu, you can export

cube files of 𝛿𝑔̅inter and averaged sign(λ2)ρ as avgdg_inter.cub and avgsl2r.cub, respectively. There is an option (-1) to a plot scatter map between the two functions, which may be useful in the amIGM analysis. You can can also export the averaged RDG (a byproduct of amIGM analysis) and thermal fluctuation index (TFI) mentioned Section 3.23.3 as cube files.

To plot 𝛿𝑔̅inter isosurface map colored by averaged sign(λ2)ρ, you should put the exported avgdg_inter.cub and avgsl2r.cub as well as examples\aIGM.vmd to VMD folder, then boot up VMD and input source aIGM.vmd command in VMD console window to execute the plotting script, you will immediately see the amIGM map.

In the post-processing menu, you can also choose option 8 to generate grid data of standard

deviation of 𝛿𝑔inter and thermal fluctuation index of amIGM (TFIamIGM), which are defined as follows

$$\mathrm{TFI}^{\mathrm{amIGM}}(\mathbf{r})=\frac{s t d(\delta g^{\mathrm{inter}})(\mathbf{r})}{\delta g^{-\mathrm{inter}}(\mathbf{r})}$$

$$\mathrm{TFI}^{\mathrm{amIGM}}(\mathbf{r})=\frac{s t d(\delta g^{\mathrm{inter}})(\mathbf{r})}{\delta g^{-\mathrm{inter}}(\mathbf{r})}$$

where 𝛿𝑔𝑖 inter denotes 𝛿𝑔inter of frame i, and N denotes number of considered frames. By mapping TFIamIGM or 𝑠𝑡𝑑(𝛿𝑔inter) onto isosurface of 𝛿𝑔̅inter with a properly chosen color range, stability of interactions at different areas can be distinguished.

An example of amIGM analysis is given in Section 4.20.13.

Information needed: Multiple frames of atom coordinates


## 3.24 Energy decomposition analysis (21)


### 3.24.1 Energy decomposition analysis based on molecular forcefield (EDA-FF)



Energy decomposition analysis (EDA) is an important method to reveal the nature of interaction. Most EDA analysis methods are based on wavefunction, they are accurate, rigorous and the results are meaningful, unfortunately they are often too expensive for large systems. Present module is designed for analyzing intramolecular and intermolecular weak interactions based on classical molecular force field (FF), this method could be referred to as EDA-FF, the computational


<!-- p.334 -->

cost is negligible for systems consisting of hundreds of atoms, and it can even be applied to systems with more than ten thousand atoms. Due to the limitation of FF, this module evidently cannot be used to discuss nature of chemical bond interactions. The word "weak interaction" in this section refers to the interatomic interaction separated by more than three bonds.

If EDA-FF analysis is utilized in your work, please cite this article, in which I briefly described EDA-FF and employed it in studying interaction between cyclo[18]carbon and graphene: Mat. Sci. Eng. B, 273, 115425 (2021) DOI: 10.1016/j.mseb.2021.115425.

Theory There are many popular FFs for molecular systems. The major ingredients of weak interactions are van der Waals (vdW) interaction and electrostatic interaction, most FFs represent them by mean of pairwise potential, as shown below.

·Electrostatic interaction energy between atoms A and B (atomic unit is used):


$$E_{_{AB}}^{ele}=\frac{q_{_{A}}q_{_{B}}}{r_{_{AB}}}$$

<!-- formula-ocr: formula_p334_225.png 已替换为LaTeX, 原图保留备查 -->

where q is atomic charge and rAB is distance between A and B.

·vdW interaction energy between atoms A and B:

EEE ABABAB disprepvdW +=

$$E_{_{AB}}^{\mathrm{vdW}}=E_{_{AB}}^{\mathrm{rep}}+E_{_{AB}}^{\mathrm{disp}}$$

where Erep represents repulsive interaction due to Pauli repulsion effect (also known as exchange-

repulsion), while Edisp is attractive dispersion interaction. The εAB is well depth of interatomic vdW interaction potential, while R0AB is vdW nonbond distance. When rAB=RAB0, the interaction energy just corresponds to well depth.

The parameters ε and R0 are provided by FFs, and the values are commonly defined for each atom type. The interatomic parameters used in practical calculation are commonly evaluated as geometric average or arithmetic average of atomic parameters. For example, in UFF forcefield, the following mixing rule is used


$$E_{_{AB}}^{\mathrm{vdW}}=E_{_{AB}}^{\mathrm{rep}}+E_{_{AB}}^{\mathrm{disp}}$$

<!-- formula-ocr: formula_p334_226.png 已替换为LaTeX, 原图保留备查 -->

While for some other FFs such as AMBER and GAFF, atomic ε and R* are defined, the employed mixing rule is


$$E_{AB}^{\mathrm{rep}}=\varepsilon_{AB}\left(\frac{R_{AB}^{0}}{r_{AB}}\right)^{12}\quad E_{AB}^{\mathrm{disp}}=-2\varepsilon_{AB}\left(\frac{R_{AB}^{0}}{r_{AB}}\right)^{6}$$

<!-- formula-ocr: formula_p334_227.png 已替换为LaTeX, 原图保留备查 -->

where R* is known as atomic nonbond radius or atomic vdW radius.

Given the interatomic interaction terms, evaluating various physical components of interfragment interaction energy is straightforward:


$$E_{IJ}^{\mathrm{ele}}=\sum_{A\in I}\sum_{B\in J}E_{AB}^{\mathrm{ele}}\qquad E_{IJ}^{\mathrm{rep}}=\sum_{A\in I}\sum_{B\in J}E_{AB}^{\mathrm{rep}}\qquad E_{IJ}^{\mathrm{disp}}=\sum_{A\in I}\sum_{B\in J}E_{AB}^{\mathrm{disp}}$$

<!-- formula-ocr: formula_p334_228.png 已替换为LaTeX, 原图保留备查 -->

The present module is mainly used to evaluate above three terms between two or more user-defined fragments, many useful quantities can be obtained at the meantime.

Usage The basic steps of using this module are:


<!-- p.335 -->

(1) Prepare a "molecule list" file, which contains paths of "molecule type" files. Detailed description is given later.

(2) Load a file containing geometry information of the whole system. Evidently, many formats supported by Multiwfn could be used, for example, .xyz, .mol, .pdb, .fch and so on.

(3) Enter subfunction 1 of main function 21. (4) Use option 3 to load molecule list file. This step is used to assign an atomic charge and type for each atom.

(5) Use option 2 to define fragments. Infinite number of fragments may be defined, any atom should not simultaneously appear in two or more fragments. If you want to study interaction between two fragments in the same molecule, any atomic pair between the two fragments should be separated by at least three bonds (otherwise the interaction will no longer belong to the scope of weak interaction). Note that the order of the steps (4) and (5) could be exchanged.

(6) Choose option 1 to start analysis, then interaction energy components between each fragment pair, as well as atomic contributions will be printed. Before the analysis, if you want to check whether the charges and types have been properly assigned, you can choose option 4.

There are other options you can select before calculation: ·Option -1: This is used to choose the FF employed in the calculation. Currently, AMBER99 & GAFF (default) and UFF are supports, their difference is that the built-in atomic vdW parameters and the mixing rule used in the calculation are different.

·Option -2: This option can choose the operator in calculating electrostatic interactions. By default 1/r operator is employed, while using this option you can change it to 1/r2. Obviously, the attenuation of Eele calculated based on 1/r2 with respect to interaction distance r is much faster than the default case, this is why some studies employ this simple strategy to effectively exhibit water environment, since it is well-known that polar solvents such as water can significantly shield electrostatic interaction strength due to its large dielectric constant.

·Option -3: If you choose this option once to switch the status to "Yes", then after calculation, all interatomic interaction energy terms including their physical components will be exported to interatm.txt in current folder.

·Option -4: In the standard .pqr format, the last two columns are specific for storing atomic vdW radii and atomic charges. If you choose this option once to switch the status to "Yes", then during calculation, atmint_tot.pqr, atmint_ele.pqr, atmint_rep.pqr, atmint_disp.pqr and atmint_vdW.pqr will be outputted in current folder, their last columns record atomic contribution to total, electrostatic, repulsion, dispersion and vdW (i.e. repulsion + dispersion) interaction energies, respectively. In the popular VMD visualization program, you can load one of these .pqr file and color the atoms according to "atomic charges" data, then the atom colors will vividly exhibit contribution of each atom to corresponding kind of interaction energy.

Next, I introduce the rule of writing the molecular list file. The content of the file should look like this:


```text
C:\mol1\phenol.txt 1
C:\mol2\H2O.txt 4
C:\HCl.txt 2
```

This example file implies that, in the geometry information provided by the file loaded when


<!-- p.336 -->

Multiwfn boots up, the recording sequence is: one phenol molecule, four H2O molecules and two HCl molecules. The three .txt files contain atom types (case sensitive) and charges of respective molecule. For example, below is the content of the C:\mol2\H2O.txt, which records information of the atoms in H2O molecule, the OW and HW are atom types of AMBER force field.


```text
OW -0.728713
HW  0.364427
HW  0.364286
```

The first column is atom type corresponding to the FF you currently choose, the second column corresponds to atomic charge. Notice that the atom sequence in this file must be exactly identical to the geometry information loaded when Multiwfn boots up. If the forcefield employed in analysis is UFF, then this file should only contain atomic charge, thus there should be only one column (because for each element, all relevant atom types share the same UFF vdW parameters, therefore users do not need to define atom types).

·About atom types: Detailed description of atom types can be found in original paper of corresponding forcefields. For AMBER, see Table 1 of J. Am. Chem. Soc., 117, 5179 (1995). For GAFF, see Table 1 of J. Comput. Chem., 25, 1157 (2004); you can also consult the AMBER99.txt and GAFF.txt in "examples\EDA\EDA_FF" folder for description of atom types. In general, you can manually find appropriate atom type for each atom in current system according to its actual chemical environment. However, if you feel this process is troublesome, you can use third-part programs to help you identify atom types and construct the molecular files. For example, GaussView can automatically assign AMBER atom types (enter "Atom List", click the icon with large organge "M" symbol, double click head of "AMBER Type" column, select "File"-"Export Data", then extract the data corresponding to "AMBER Type" column), while Antechamber utility in AmberTools package is able to assign GAFF atom types. Note that AMBER and GAFF atom types can be mixed together in the same molecule file, since these two forcefields are completely compatible with each other, the AMBER and GAFF atom types use upper and lower case, respectively.

Note: The atom types assigned by GaussView are always in upper case, however, some atom types of AMBER99 are lower case, e.g. Br. Clearly, you should manually make modification before loading the file into Multiwfn. If you are confused, take a look at examples\EDA\EDA_FF\AMBER99.txt.

·On the choice of forcefield: For organic type of systems, commonly I suggest using AMBER/GAFF forcefield to conduct the analysis, the result should be reasonable and chemically meaningful. In fact, since vdW parameters of GAFF are directly inherited from AMBER, commonly there should be no difference between using GAFF and AMBER atom types. Evidently, the geometry used in the analysis should be firstly optimized under reasonable level. Using UFF is generally deprecated, since I found that when UFF is employed, the total interfragment interaction energy is usually positive due to overestimation of Erep, even if the geometry has already been substantially optimized with appropriate quantum chemistry method. A way to solve this problem is using the geometry optimized by UFF itself (many programs can do this, such as Gaussian and OpenBabel), however the resulting geometry for weakly interacting molecular dimer or multimer is often not quite good. The unique advantage of UFF is that it covers almost entire periodic table. Considering this, I designed a trick in Multiwfn: If you are using AMBER/GAFF, when atom type is written as UF, then UFF vdW parameter will be employed. This treatment greatly extends the application scope of AMBER and GAFF.


<!-- p.337 -->

·On the choice of atomic charges: The atomic charges used for energy decomposition analysis should be able to reproduce electrostatic potential (ESP) around molecular vdW surface well. Commonly I suggest using CHELPG atomic charge, which is obtained via ESP fitting process and can be directly calculated via Multiwfn, see Section 3.9.10 for introduction and Section 4.7.1 for example. Note that if a type of molecule appears more than once in current system with significantly different conformations, given that ESP fitting charges of each monomer may be very different to others, it is suggested to treat these replicas as different types of molecules, so that atomic charges can be individually assigned. If some monomers of the system are too large to calculate their ESP fitting atomic charges, you may change to EEM atomic charges using the parameters fitted for reproducing ESP fitting charges, see Section 3.9.15 for introduction. The computational cost of EEM charges is negligible for a system composed of hundreds of atoms, since the calculation is purely based on molecular geometry information and empirical parameters.

Examples of this module are provided in Section 4.21.1. Information needed: Atom coordinates and special files containing atomic charges/types


### 3.24.2 Shubin Liu's energy decomposition

Theory In J. Chem. Phys., 126, 244103 (2007), the author Shubin Liu proposed an idea of energy decomposition, which will be referred to as EDA-SBL below. In this method, the total molecular energy is decomposed as

stericelectrostaticquantumEEEE=++

The steric term is simply the energy derived by Weizsäcker kinetic functional, which corresponds to the exact kinetic energy under assumption that the electrons in present system are non-interacting bosons:


$$E_{\mathrm{s t e r i c}}=T_{\mathrm{W}}=\left|\nabla\rho(\mathbf{r})\right|^{2}/\left[8\rho(\mathbf{r})\right]$$

<!-- formula-ocr: formula_p337_229.png 已替换为LaTeX, 原图保留备查 -->

The electrostatic term is the sum of all classical Coulomb interactions of the particles in the system:

$$E_{\mathrm{e l e c t r o s t a t i c}}=E_{\mathrm{J}}+E_{\mathrm{N-E}}+E_{\mathrm{N-N}}=\iint\frac{\rho(\mathbf{r}_{1})\rho(\mathbf{r}_{2})}{r_{12}}\mathrm{d}\mathbf{r}_{1}\mathrm{d}\mathbf{r}_{2}-\int\rho(\mathbf{r})\sum_{A}\frac{Z_{A}}{|\mathbf{r}-\mathbf{R}_{A}|}\mathrm{d}\mathbf{r}+\sum_{A>B}\frac{Z_{A}Z_{B}}{R_{AB}}$$

Finally, the quantum term is the energy purely caused by quantum effect:

quantumPauliXCEEE=+

where the EXC is exchange-correlation energy, the EPauli=TS-TW is Pauli kinetic energy, in which the TS stands for total kinetic energy of non-interacting electron model and can be computed as the sum of kinetic energy of all occupied molecular orbitals. The Equantum essentially exhibits electronic correlation effect as well as influence of Pauli exclusion principle on electronic kinetic energy under non-interacting particle assumption.


<!-- p.338 -->

The EDA-SBL method has been employed in many research papers, such as the ones shown below, which are suggested to read to if you want to understand how this method can be used to study practical chemical problems: J. Phys. Chem. A, 117, 962 (2013), J. Chem. Phys., 133, 114110 (2010), Phys. Chem. Chem. Phys., 17, 27052 (2015), J. Phys. Chem. A, 119, 8216 (2015), Chem. Phys. Lett., 687, 131 (2017).

Usage Multiwfn itself is unable to evaluate all terms in the EDA-SBL method, Multiwfn needs to read relevant information from Gaussian output file. The way of using Gaussian to perform EDA-SBL analysis is summarized as follows:

(1) Manually create a special Gaussian input file of single point task based on optimized geometry

(2) Run the input file by Gaussian and get output file as well as fch/fchk file (3) Boot up Multiwfn and load the fch/fchk file, then enter subfunction 2 of main function 21 (4) Input the path of the Gaussian output file Then Multiwfn calculates the Esteric term, and prints all three energy components defined by the EDA-SBL method. Other intermediate terms involved in the EDA-SBL terms are also simultaneously given, such as Pauli kinetic energy, nuclear-electronic Coulomb attraction energy and so on.

The special Gaussian input file should be coincident with following format, the geometry has been optimized using appropriate level.


```text
%chk=H2O.chk
## B3LYP/6-31G* ExtraLinks=L608

Optimized water

0 1
O 0.00000000     0.00000000     0.11930801
H 0.00000000     0.75895306    -0.47723204
H 0.00000000    -0.75895306    -0.47723204

-5
```

The DFT functional and basis set can be arbitrarily chosen, the "ExtraLinks=L608" must be specified so that Gaussian can break total energy into various components and print them to output file. After calculation, the resulting H2O.chk should be converted to fch/fchk file using formchk utility. As you can see, there is a value "-5" at the end of the input file, this value should be specified according to the DFT functional you actually used, you can find corresponding value by consulting IOp(3/74) in Gaussian IOp reference. The values for commonly employed hybrid functionals are:

-73 (MN15) -58 (ωB97XD), -55 (M06-2X), -54 (M06), -53 (M06L), -40 (CAM-B3LYP), -35 (TPSSh), -13 (PBE0), -5 (B3LYP), -6 (B3PW91), -3 (BHandHLYP), 402 (BLYP), 1009 (PBE), 2523 (TPSS).

An alternative way of finding the corresponding value of IOp(3/74) for present DFT functional is carrying out a simple calculation and check the value of IOp(3/74) automatically shown at the beginning of the output file, for example, the output file using B3LYP/6-31G* level will contain a line "3/5=1,6=6,7=1,11=2,16=1,25=1,30=1,


<!-- p.339 -->

74=-5/1,2,3;", showing that the IOp(3/74) is -5. More explanation of ExtraLinks=L608 can be found in http://gaussian.com/faq1/.

IMPORTANT NOTE for Gaussian with version ≤ G16 C.01: According to response from Gaussian support, at least for G16 C.01 or older, range-separated functionals such as ωB97XD and CAM-B3LYP are not compatible with ExtraLinks=L608. In addition, for consistency reason, if you are using G16, you should also add value "5" after the functional index to request Gaussian to use “ultrafine” grid for the ExtraLinks=L608, because “ultrafine” is the default DFT grid since G16. For example, if you need to use M06-2X, you should write -55 5 rather than simply 55.

A practical example of EDA-SBL analysis is given in Section 4.21.2.


### 3.24.3 SobEDA and sobEDAw energy decomposition analyses

The sobEDA and sobEDAw energy decomposition analyses defined based on dispersion-corrected density functional theory are very robust, efficient, universal, and easy-to-use, and thus highly recommended to use! They can be easily performed using sobEDA.sh shell script based on Gaussian and Multiwfn. Please check the original paper J. Phys. Chem. A, 127, 7023 (2023) for introduction about the theory background and illustrative applications, a very detailed tutorial is available at http://sobereva.com/soft/sobEDA_tutorial.zip. My blog article “Using sobEDA and sobEDAw methods to perform very accurate, fast, convenient and universal energy decomposition analysis” (http://sobereva.com/685, in Chinese) contains additional discussions.


### 3.24.4 Analysis of atomic contribution to dispersion energy

Theory For a DFT functional such as B3LYP whose ability to describe dispersion interaction is zero, the well-known DFT-D3 dispersion correction energy can be approximately regarded as the dispersion energy. This point has been proposed in J. Phys. Chem. A, 127, 7023 (2023), and further confirmed in J. Chem. Theory Comput., 20, 1923 (2024) by comparing with the dispersion energy calculated by DLPNO-CCSD(T). Without considering the three-body coupling term, the total dispersion correction energy of DFT-D3 is the sum of the dispersion interaction energy between each pair of atoms. Therefore, the contribution of atom A to dispersion energy of a system can be

calculated as 𝜀𝐴= (1/2) ∑𝜀𝐴,𝐵𝐵≠𝐴, where 𝜀𝐴,𝐵 is DFT-D3 dispersion correction energy between atoms A and B. Contribution of a fragment to dispersion energy is simply the sum of contributions of its atoms. The dispersion interaction energy between two fragments is equal to the sum of the dispersion interaction energy between each pair of atoms between them.

Furthermore, J. Chem. Theory Comput., 20, 1923 (2024) proposed the idea of dispersion energy, which is defined as


$$\rho_{\mathrm{d i s p}}(\mathbf{r})=\left(\frac{\pi}{\alpha}\right)^{-3/2}\sum_{A}\varepsilon_{A}e^{-\alpha(\mathbf{r}-\mathbf{R}_{A})^{2}}$$

<!-- formula-ocr: formula_p339_230.png 已替换为LaTeX, 原图保留备查 -->

where α usually takes 0.5, RA is coordinate of atom A. Essentially, the 𝜌disp broadens atomic

contributions to dispersion energy into Gaussian functions to obtain a real space function, which can be exhibited graphically.

The difference in dispersion energy contributed by a certain atom A shared by different chemical environments (such as structures m and n) is denoted as ∆𝜀𝐴. Replacing 𝜀𝐴 in the above formula with ∆𝜀𝐴 results in the ∆𝜌disp function. If the nuclear coordinates used to calculate ∆𝜌disp correspond to the structure m, then ∆𝜌disp can be used to color the atoms of structure m, or drawn


<!-- p.340 -->

as isosurfaces and appended to a structure map, to highlight the region contribute most to variation of dispersion energy.

The aforementioned information is also true for other types of dispersion correction schemes, such as DFT-D4, however Multiwfn currently only supports performing the analysis based on DFT-D3.

Functions All data in this module are calculated based on DFT-D3(BJ) dispersion correction energy with parameters fitted for B3LYP. Periodic system is supported.

The functions of the present module are as follows
- Calculate atomic contributions to dispersion energy for current system: The value of each atom is shown on screen, and a file named atomdisp.pqr can be exported, in which the “charge” property (third to last column in the file) corresponds to the atomic contributions to dispersion energy. If you load the file into VMD program, you can color atoms according to the “charge” property to intuitively exhibit the atomic contributions.
- Calculate dispersion density for current system: You will be asked to define grid setting, then grid data of dispersion density will be calculated, and then can be exported as dispdens.cub in current folder. After that, you can use such as VMD and VESTA to load it and plot isosurface of dispersion density.
- Calculate difference of atomic contributions to dispersion energy between current and another system: You will be asked to define a fragment for present system (fragment i for system A), and then be asked to input file path of another system and define a fragment for it (fragment j for system B). The two systems do not necessarily correspond to the same system, but the two fragments must have the same number of atoms and same atomic order. After that, Multiwfn will print total dispersion energy for system B and then for system A in turn. Then difference between contributions of atoms in fragment i to dispersion energy of system A and contributions of atoms in fragment j to dispersion energy of system B will be printed, and diffatomdisp.pqr can be exported, whose “charge” property corresponds to the difference.
- Calculate dispersion density difference between current and another system. Similar to the last function, but grid data of ∆𝜌disp is calculated and exported as dispdensdiff.cub in

current folder.
- Calculate contribution of a fragment to dispersion energy
- Calculate dispersion interaction energy between two fragments

Usage This module corresponds to subfunction 4 of main function 21. The input file must contain atom information, such as xyz, pdb, mol2, gjf, fch, mwfn, see Section 2.5 for comprehensive introduction. If the input file contains cell information, then the calculation will be considered as periodic.

This function needs Grimme’s dftd3 code modified by Tian Lu, which can be downloaded at http://sobereva.com/soft/dftd3_TLmod.zip, and contains modified source code, precompiled Windows version of executable file (dftd3.exe), precompiled Linux version of executable file (dftd3). You should set “dftd3path” in `settings.ini` to actual path of the dftd3 executable file before booting up Multiwfn, so that Multiwfn can invoke dftd3. In the case of Linux environment, do not forget to use “chmod” to add executable permission for the dftd3.
