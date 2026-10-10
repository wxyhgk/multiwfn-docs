# 3.17 Adaptive natural density partitioning (AdNDP) analysis (14)

> Multiwfn manual, p.217–221. Images: `../imgs/`.

---

<!-- p.217 -->

Information needed: Grid data (both orthogonal and nonorthogonal grids are supported)


### 3.16.16 Duplicate grid data periodically (20)

This function is used to duplicate grid data along the 1st/2nd/3rd box vector by specific times, and you can also let Multiwfn to duplicate atoms at the same time. If the box information of the present grid data is exactly coincident with cell information of a crystal, then you can obtain grid data and structure corresponding to supercell via this function. See “Using Multiwfn to rapidly generate grid data of supercell” (http://sobereva.com/770) for illustrative application of this function.

Information needed: Grid data (both orthogonal and nonorthogonal grids are supported)


## 3.17 Adaptive natural density partitioning (AdNDP) analysis (14)




### 3.17.1 Theory

Famous NBO analysis developed by Weinhold and coworkers is able to recover up to 3-centers 2-electrons (3c-2e) orbitals from density matrix (e.g. by using "3cbond" keyword in NBO program). Adaptive natural density partitioning (AdNDP), which was proposed by Boldyrev et al. (Phys. Chem. Chem. Phys., 10, 5207 (2008)), may be viewed as a natural extension of NBO analysis aiming for locating N>3 centers orbitals. AdNDP has been extensively used to study electronic structure characteristic of a widespread cluster systems, by googling "AdNDP" you can find much related literature.

Canonical molecular orbitals (CMOs) are generally highly delocalized, often lacking chemical significances; While 2c or 3c NBOs are substantially localized, for highly conjugated system resonant description is often needed (otherwise large non-Lewis composition will occur, that means current system is inappropriate to be portrayed by single set of NBOs), this somewhat conflicts with modern quantum chemistry concepts and obscures delocalization natural of electrons in conjugated system. AdNDP orbitals seamlessly bridged CMOs and NBOs, AdNDP bonding patterns avoid resonant description and are always consistent with the point symmetry of the molecule.

The basic idea of AdNDP to generate multi-center orbitals is very similar to NBO analysis, that is constructing proper sub-block of density matrix in natural atomic orbital (NAO) basis and then diagonalize it, the eigenvalues and eigenvectors correspond to occupation number and orbital wavefunction respectively. For example, we want to generate all possible 4-centers orbitals for atom A,B,C,D, we first pick out corresponding sub-blocks and then combine them altogether:


<!-- p.218 -->

$$P^{(\boldsymbol{A},\boldsymbol{B},\boldsymbol{C},\boldsymbol{D})}=\left[\begin{matrix}{P_{\boldsymbol{A},\boldsymbol{A}}}&{P_{\boldsymbol{A},\boldsymbol{B}}}&{P_{\boldsymbol{A},\boldsymbol{C}}}&{P_{\boldsymbol{A},\boldsymbol{D}}}\\ {P_{\boldsymbol{B},\boldsymbol{A}}}&{P_{\boldsymbol{B},\boldsymbol{B}}}&{P_{\boldsymbol{B},\boldsymbol{C}}}&{P_{\boldsymbol{B},\boldsymbol{D}}}\\ {P_{\boldsymbol{C},\boldsymbol{A}}}&{P_{\boldsymbol{C},\boldsymbol{B}}}&{P_{\boldsymbol{C},\boldsymbol{C}}}&{P_{\boldsymbol{C},\boldsymbol{D}}}\\ {P_{\boldsymbol{D},\boldsymbol{A}}}&{P_{\boldsymbol{D},\boldsymbol{B}}}&{P_{\boldsymbol{D},\boldsymbol{C}}}&{P_{\boldsymbol{D},\boldsymbol{D}}}\\ \end{matrix}\right]$$

After diagonalization of $P^{(A,B,C,D)}$, if one or more eigenvalues exceeded the predefined threshold, which is commonly set to close to 2.0 (e.g. 1.7), then corresponding orbitals will be regarded as candidate 4c-2e bonds. Completely identical strategy can be used to generate orbitals with higher number of centers.

Indeed, the orbital generating process of AdNDP is quite easy once atom combination is determined, however the searching process of final Nc-2e orbitals in entire system is complicated, manual inspections and operations are necessary. AdNDP approach has large ambiguity, it is possible that the searching process carried out by different peoples finally results in different AdNDP pattern, I think this is the most serious limitation of current AdNDP approach. So, AdNDP is never a black box, before using it users must have preliminary understanding of the searching process of the AdNDP implemented in Multiwfn.

Before the search, densities from core-type NAOs are automatically eliminated from the density matrix, since they have no contribution to bonding. After that, 1-center orbitals (lone pair), 2-centers orbitals, 3-centers orbitals, 4-centers orbitals ... will be searched in turn, until residual density (trace of density matrix) is close to zero. The search could be exhaustive, that means when searching N-centers orbitals, Multiwfn will construct and diagonalize M!/(M-N)!/N! sub-blocks of density matrix, where M is the total number of atoms. All of the orbitals whose occupation numbers are larger than the threshold will be added to candidate orbital list. For large system, the searching process may be very time-consuming or even forbidden, for example, exhaustive search of 10-centers orbitals in the system with 30 atoms needs to construct and diagonalize 30045015 sub-blocks of density matrix! This is very difficult to finish in personal computer, for such case, user-directed searching is necessary. In Multiwfn you can define a search list, then the exhaustive search will only apply to the atoms in the search list, so that the amount of computation would be greatly reduced. You can also directly let Multiwfn construct and diagonalize sub-block of density matrix for specified atom combination. Note that user-directed searching has relatively high requirements of skill and experience on users.

Once the search of N-centers orbitals is finished, we will get a list containing candidate N-centers orbitals. We need to pick some of them out as final N-centers AdNDP orbitals. Commonly, one or more orbitals with the highest occupation numbers will be picked out. Notice that, since some densities are simultaneously shared by multiple candidate orbitals, if we directly pick out several candidate orbitals with the largest occupation at one time, the electrons may be overcounted. To avoid this problem, assume that K orbitals with the highest occupation numbers obviously overlap with some other candidate orbitals meanwhile there is no evident overlapping between the K orbitals, we should first pick out K orbitals as final AdNDP orbitals, then Multiwfn will automatically deplete their density from the density matrix and then reconstruct and diagonalize the corresponding sub-blocks of density matrix for remained candidate orbitals to update their shapes and occupation numbers. If there are still some candidate orbitals with occupation numbers close to 2.0, you may consider picking them out, then remained orbitals will be updated again. Such process may be repeated several times until there is no orbital that has a high occupation number. After that, you can


<!-- p.219 -->

start to search N+1 centers orbitals.

The general requirements of AdNDP analysis are that: The final residual density (corresponds to non-Lewis composition in NBO analysis) should as low as possible; the occupation numbers of each AdNDP orbital should as close to 2.0 as possible; the number of centers of AdNDP orbitals should as less as possible; the resulting orbitals must be consistent with molecular symmetry.

However, there is no unique rule on how to search orbitals and pick out candidate orbitals as AdNDP orbitals. For example, one can first search 5-centers orbitals before completing search of 3-centers orbitals, and one can also directly search 6-centers orbitals after the search of 2-centers orbitals has finished. The sequence of picking out candidate orbitals is also not necessarily always in accordance with magnitude of occupation numbers. The final AdNDP pattern obtained by different operations may be different, how to do AdNDP analysis is largely dependent on users themselves. Actually, some molecules may have two or even more equally reasonable AdNDP patterns, sometimes it is difficult to discriminate which pattern is the best. I have confidence to say that some AdNDP patterns presented in published papers are not the optimal ones. The experience of using AdNDP approach can be gradually enriched in practices and during reading related papers.

AdNDP is very insensitive to basis set quality as NBO analysis, 6-31G* is enough to produce accurate results for main group elements in the first few rows. Over enhancing basis set quality will not improve AdNDP analysis results but only lead to increase of the computational burden in diagonalization step, since the size of sub-block of density matrix is directly determined by size of basis set.

Multiwfn offers capacity for evaluating AdNDP orbital energies. You need to provide a file containing Fock (or Kohn-Sham) matrix in original basis functions. The Fock matrix can be obtained from output of Gaussian or other programs. The energy of AdNDP orbital is corresponding diagonal term of Fock matrix in AdNDP orbital representation. Specifically, Multiwfn performs below representation transform:

TAdNDPAOAONAO==FC FCCXc

where FAO is the Fock matrix in original basis function that loaded from user-provided file, C(r,i) corresponds to coefficient of basis function r in AdNDP orbital i. c(s,i) corresponds to coefficient of NAO s in AdNDP orbital $X_{AONAO}$ is transformation matrix between original basis function and NAO, i.e. X(t,s) is coefficient of basis function t in NAO s. Energy of AdNDP orbital j is simply FAdNDP(j,j), which is expectation value of Fock operator of AdNDP orbital wavefunction.


### 3.17.2 Input file

The output file of NBO program containing density matrix in NAO basis (DMNAO) can be used as input file for AdNDP analysis. If you also need to visualize AdNDP orbitals or export orbitals as cube files, .fch file must be provided, meanwhile transformation matrix between NAO and original basis functions (AONAO) must be presented in the NBO output file.

Assume that you are a Gaussian user, in order to obtain a Gaussian output file containing all information needed by Multiwfn to perform the AdNDP analysis and visualization, you should write a Gaussian input file of single point task with pop=nboread keyword in route section, and write \$NBO AONAO DMNAO \$END after molecular geometry section with a blank line as separator. Then run the input file by Gaussian and then convert .chk file to .fch format by formchk utility.

The Gaussian output file (not .fch file) should be used as the initial input file when Multiwfn


<!-- p.220 -->

boots up. Once you entered AdNDP module, Multiwfn will load NAO information and DMNAO matrix from this file. If then you choose corresponding options to visualize or export orbitals, AONAO matrix will be loaded and the program will prompt you to input the path of the .fch file (if .fch is in the same folder and has identical name as the Gaussian output file, then the .fch will be automatically loaded).

Multiwfn is also compatible with the output files of stand-alone NBO program (GENNBO), of course you have to add DMNAO keywords in $NBO section in .47 file. In this case it is impossible to visualize AdNDP orbitals.

Formally, AdNDP approach is also applicable to open-shell systems; of course, the occupation threshold should be divided by 2. When you enter AdNDP module, Multiwfn will ask you which density matrix should be used, the so-called total density matrix is the sum of alpha and beta density matrix.

Notice that if after you entered AdNDP module Multiwfn suddenly crashes, and the basis set you used contains diffuse functions, you can try to use another basis set without diffuse functions. This problem is caused by the bug in NBO 3.1 module, namely in rare cases the DMNAO output may be slightly problematic if diffuse functions present. Since AdNDP analysis is quite insensitive to diffuse functions, they can be safely removed without any loss of accuracy.

If you want to obtain AdNDP orbital energies, Fock matrix corresponding to present system at the same calculation level must be provided in lower-triangular sequence in a plain text file, namely: F(1,1) F(2,1) F(2,2) F(3,1) F(3,2) F(3,3) ... F(nbasis,nbasis), where nbasis is the total number of basis functions. The format is free. If you are a Gaussian user, you can add archive file=XXX keyword between \$NBO ... \$END, then in the resulting XXX.47 file, search \$FOCK and copy all data between \$FOCK ... \$END to a plain text file, then this file can be directly used to provide Fock matrix to Multiwfn (In fact, Multiwfn is also able to automatically locate and read the \$FOCK field when the file name has .47 suffix).


### 3.17.3 Options

All of the options involved in AdNDP module are introduced below, some options are invisible in certain cases. If current candidate orbital list is not empty, then all candidate orbitals will always be printed on screen in front of the menu (except when you select option 5 or 13), the candidate orbital indices are determined according to occupation numbers. The number of residual valence electrons of all atoms in the search list is always printed at the upper of the menu, this value decreases with gradually picking out candidate orbitals as final AdNDP orbitals. If this value is very low (e.g. lower than 1.4), it is suggested that new Nc-2e AdNDP orbitals will be impossible to be found between the atoms in the search list.

-10 Return to main menu: Once you choose this option, you will return to main menu, meantime all results of AdNDP analysis will be lost. Hence the status of AdNDP module can be reset by choosing this option and then re-entering the module.

-2 Various other settings and functions: This option has several unimportant subfunctions and settings. The option "Set maximum number of candidate orbitals to be printed" is worth to mention, it is used to set how many candidate orbitals will be printed on screen, proper choice of the threshold can avoid excessive output when very large number of candidates are found.

-1 Define exhaustive search list: In this option, one can define a search list, exhaustive search (option 2) will only apply to the atoms in the search list. All commands in this defining interface are


<!-- p.221 -->

self-explanatory. Notice that default search list includes all atoms of the molecule.

0 Pick out some candidate orbitals and update occupations of others: This is used to pick out orbitals from candidate list to actual AdNDP orbital list. As shown by prompt on screen, the user can input indices of the orbitals to pick out. For convenience, if user only inputs one number, e.g. 5, then 5 candidate orbitals with largest occupation numbers will be picked out. After that, the eigenvectors (orbital shape) and eigenvalues (occupation numbers) of remaining candidate orbitals will be updated as mentioned earlier.

1 Perform orbitals search for a specific atom combination: Users need to input indices of some atoms, e.g. 3,4,5,8,9, then sub-block of density matrix for atom 3,4,5,8,9 will be constructed and diagonalized, all resultant eigenvectors will be added to candidate orbitals list, meantime all previous candidate orbitals will be removed. There is no limit on the number of inputted atoms.

2 Perform exhaustive search of N-centers orbitals within the search list: N atoms will be selected out from the search list in an exhaustive manner, assume that the search list contains M atoms, then totally M!/(M-N)!/N! atom combinations will be formed. For each combination, corresponding sub-block of density matrix will be constructed and diagonalized, all eigenvectors with eigenvalues larger than user-defined threshold will be added to candidate orbital list. Old candidate orbital list will be cleaned.

3 Set the number of centers in the next exhaustive search: Namely set the value N in option 2. Once exhaustive search of N-centers orbitals is finished, N will be automatically increased by one.

4 Set occupation threshold in the next exhaustive search: Namely set the threshold used in option 2.

5 Show information of AdNDP orbitals: Print occupation numbers and involved atoms of all saved AdNDP orbitals.

6 Delete some AdNDP orbitals: Input two numbers, e.g. i, j, then saved AdNDP orbitals from i to j will be removed.

7 Visualize AdNDP orbitals and molecular geometry: The path of corresponding .fch file will be prompted to be inputted, after loading some necessary information from the file, a GUI window will pop up and molecular geometry will be shown. Isosurfaces of AdNDP orbitals can be plotted by clicking corresponding numbers in the right-bottom list

8 Visualize candidate orbitals and molecular geometry: Analogous to option 7, but used to visualize isosurfaces of candidate orbitals. It is useful to visualize the isosurfaces before picking out some candidate orbitals as final AdNDP orbitals.

9 Export some AdNDP orbitals to Gaussian-type cube files: User need to choose grid setting and then input index range, e.g. 2-4, then wavefunction value of AdNDP orbitals 2, 3, 4 will be calculated and exported to AdNDPorb0002.cub, AdNDPorb0003.cub and AdNDPorb0004.cub in current folder, respectively. They are Gaussian-type cube files and can be visualized by many softwares such as VMD.

10 Export some candidate orbitals to Gaussian-type cube files: Analogous to option 9, but used to export cube files for candidate orbitals.

11/12 Save/Load current density matrix and AdNDP orbital list: Option 11 is used to save current density matrix and AdNDP orbital list in memory temporarily, when density matrix and AdNDP orbital list is changed, you can choose option 12 to recover previous state.

13 Show residual density distributions on the atoms in the search list: After choosing this option, population number of each atom in the search list will be calculated according to present
