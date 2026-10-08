# 2.3 Files of Multiwfn

> Multiwfn manual, p.34–40. Images: `../imgs/`.

---

<!-- p.34 -->


## 2.3 Files of Multiwfn

You will find following files after uncompressing Multiwfn package, only the bolded files are indispensable for running Multiwfn:

- Multiwfn.exe (Windows) or Multiwfn (Linux/Mac OS) : The executable file of Multiwfn.
- libiomp5md.dll (Windows) : Intel OpenMP Runtime library.
- `settings.ini` : All detail parameters for running Multiwfn are recorded here, most of them do not need to be frequently modified. When booting up, Multiwfn will try to find and use this file in current folder, if it is not presented in current folder, the file in the path defined by "Multiwfnpath" environment variable will be used; if the file still cannot be found, default settings will be used instead. If you run Multiwfn via command line, you can also directly specify position of this file via "-set" argument, for example: Multiwfn test.wfn -set /sob/3.7/settings.ini.

The meanings of all parameters in `settings.ini` are not documented in this manual systematically, since they have already been commented in detail, only those important will be mentioned in this manual. I suggest you read through the `settings.ini` and find out the ones useful for you.

- “examples” folder : Some useful files, scripts and the files involved in the examples of Chapter 4.

- LICENSE.txt : The terms that all users must follow.
- Multiwfn quick start.pdf : A short document lets new users immediately understand how to use Multiwfn to carry out very common tasks.

- How to cite Multiwfn.pdf : Please properly cite Multiwfn according to this document.


## 2.4 Parallel implementation

Most time-consuming codes of Multiwfn have been parallelized by OpenMP technique. If your CPU has multiple cores, you can greatly benefit from parallelization. To enable parallelization, just modify “nthreads” parameter in `settings.ini` to a proper number. For example, your computer has a CPU with 12-cores physical cores, then commonly you should change “nthreads” to 12.

If Multiwfn crashes during parallel calculation for a very large system, try to enlarge “ompstacksize” in `settings.ini` (for Windows version) or enlarge the value of the environment variable OMP_STACKSIZE (for Linux or Mac OS version).


## 2.5 Input files and wavefunction types

Wavefunction types supported by Multiwfn include restricted/unrestricted single-determinant wavefunction, restricted open-shell wavefunction and post-HF wavefunction (in natural orbital formalism).

Cartesian or spherical harmonic Gaussian functions with angular moments up to h are supported.

There is no upper limit of the number of atoms / basis functions / GTFs / orbitals in Multiwfn, the actual upper limit is only decided by available memory in your computer.


<!-- p.35 -->

Multiwfn determines the input file type by file extension. Notice that different functions need different types of information, you should choose proper type of input file, see the table below. For example, the wavefunction represented by GTFs is enough for Hirshfeld population, so you can use .mwfn/.fch/.molden/.gms/.31~.40/.wfn/.wfx file as input, but .pdb, .xyz, .mol, etc. do not carry any wavefunction information hence cannot be used; in contrast, generating grid data of RDG function with promolecular approximation only requires atom coordinates, so all supported file formats can be used (except for plain text file). The requirement on information types by each function is commonly described at the end of corresponding section in Chapter 3 by red text.

About ghost atom: In any wavefunction format described below, ghost atoms (the points with basis functions but without nuclear charges) are allowed to occur. Their element indices should be 0, and if the file format records element names, the ghost atom should have element name of Bq. Their nuclear charges are loaded by Multiwfn in common way from the file, but of course, in principle they should be zero since they are ghost atoms.

Multiwfn wavefunction file (.mwfn): This format is defined and supported since Multiwfn 3.7. This is the most ideal format for wavefunction storage and exchange purposes. This file records all information for wavefunction analysis in a strict, concise, compact and extensible format. The introduction and definition of this format have been carefully described in my paper: ChemRxiv (2020) DOI: 10.26434/chemrxiv.11872524.

AIM wavefunction file (.wfn): This format was first introduced by Bader’s AIMPAC program, and currently supported by a lot of mainstream quantum chemistry softwares, such as Gaussian, ORCA, GAMESS-US/UK, Firefly, Q-Chem and NWChem. The information in .wfn file include atomic coordinates, elements, orbital energies, occupation numbers, expansion coefficients of Cartesian Gaussian type functions (GTF). Supported angular momentum of GTF is up to f. The wfn


| File Format | Provided information types<br/>Basis Atom Grid Atomic<br/>GTFs<br/>functions coordinates data charges |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| .fch/.fchk/.chk | √ | √ | √ | × | × |
| .mwfn, .molden, .gbw, .gms | √ | √ | √ | × | × |
| NBOplot file (.31 to .40) | × | √ | √ | × | × |
| .wfn and .wfx | × | √ | √ | × | × |
| .pdb, .xyz, .mol/sdf, .mol2, .gro, .cif, .mop,<br/>Gaussian/ORCA input/output file,<br/>CP2K input/restart file, POSCAR,<br/>Quantum ESPRESSO input file<br/>Turbomole coordination file | × | × | √ | × | × |
| .chg and .pqr | × | × | √ | × | √ |
| .cub/.cube<br/>CHGCAR/CHG/ELFCAR/LOCPOT | × | × | √ | √ | × |
| .vti, .grd, .dx | × | × | × | √ | × |
| Others (plain text file) | × | × | × | × | × |

<!-- p.36 -->

file does not contain any virtual orbital. The generation method of .wfn file is documented at the beginning of Chapter 4.

Note: Although GTFs with angular moment of g and h are not formally supported by original .wfn format, if g and h-type GTFs are recorded in following manner, then Multiwfn is able to recognize them: 21~35 in "TYPE ASSIGNMENT" correspond to YZZZ, XYYY, XXYY, XYZZ, YZZZ, XYYZ, XXXX, XXXY, XZZZ, XXYZ, XXXZ, XXZZ, YYYY, YYYZ, ZZZZ, respectively. 36~56 correspond to ZZZZZ, YZZZZ, YYZZZ, YYYZZ, YYYYZ, YYYYY, XZZZZ, XYZZZ, XYYZZ, XYYYZ, XYYYY, XXZZZ, XXYZZ, XXYYZ, XXYYY, XXXZZ, XXXYZ, XXXYY, XXXXZ, XXXXY, XXXXX, respectively. The sequence shown here in fact is also the sequence used in the .wfn outputted by Molden2AIM and Gaussian09 since B.01.

AIM extended wavefunction files (.wfx) : This is a format introduced as an extension of .wfn, and it was supported by Gaussian 09 since B.01 revision. Relative to .wfn format, .wfx supports higher data record precision and infinitely high GTF angular moment. The most special point of this format is the newly added electron density function (EDF) field, that is using multiple GTFs to represent inner core electron density of the wavefunction in which effective core potential (ECP) is used. Due to this, the result of electron density analysis for the wavefunction using ECP is nearly identical to that for full electron wavefunction. Currently the real space functions supported EDFs in Multiwfn include: electron density, its gradient and Laplacian, local information entropy, reduced density gradient as well as Sign(λ2(r)). Meanwhile topology analyses of electron density and its Laplacian also take into account EDFs. Notice that EDF information has neither effect on ESP nor the real space functions that relied on wavefunction (e.g. kinetic energy density, ELF). If you you want to analyze these properties for heavy elements, you should use full-electrons basis sets, at lease small-core ECP. Currently the only supported GTF type in EDF field is S-type (actually S-type is enough for fitting inner density, since which is nearly spherical symmetry). Like .wfn, Multiwfn does not allow virtual orbitals presented in .wfx file.

Multiwfn has a powerful built-in EDF library, taken from Molden2aim program developed by Wenli Zou. As long as the input file contains GTF information (e.g. .fch, .wfn, .molden, .gms...), Multiwfn always automatically loads EDF information from this library for the atoms using ECP. Only when you use .wfx file as input and the .wfx itself already contains EDF field, the EDF information will be loaded from the .wfx file rather than from EDF library. See Appendix 4 for more details.

Note that although some programs other than Gaussian can also generate .wfx file (e.g. ORCA), these .wfx files are unable to provide EDF field.

Notice: For certain version of Gaussian (e.g. G09 B.01), I found that the EDF field recorded in .wfx for rare cases is problematic, namely the number of electrons represented by EDF field is unequal to the actual number of core electrons exhibited by ECP. In order to verify if the EDF field is correct, you can use subfunction 4 in main function 100 to obtain the integral of total electron density over the whole space, if the result is approximately equal to the total number of electrons (core+valence electrons), that means the EDF field is correct.

Gaussian formatted checkpoint file (.fch/.fchk): Checkpoint file of Gaussian program (.chk) can be converted to formatted checkpoint file (.fch/.fchk) via formchk utility in Gaussian package. There is no difference between .fch and .fchk. "fch" ("fchk") is the default extension generated by Windows (Linux) version of formchk.

If you want to make Multiwfn able to directly load .chk file, you must set "formchkpath" in `settings.ini` to actual path of formchk executable file in Gaussian package. In this case Multiwfn will automatically invoke formchk to convert .chk file to .fch/fchk file, and if conversion is successful, the .fch/fchk will be loaded and then be automatically deleted once loading is finished.

.fch/.fchk contains richer information than .wfn/.wfx files, virtual orbital wavefunctions are


<!-- p.37 -->

also recorded, and meanwhile it provides basis function information for Multiwfn. If you want to use .fch/.fchk file as carrier for post-HF wavefunction, read the beginning of Chapter 4 carefully!

The .fchk file generated by Q-Chem and PSI4 can also be used as input file of Multiwfn. (If the .fchk file was generated by relatively old version of Q-Chem, you must set “ifchprog” in `settings.ini` to 2. You do not need to do this if your Q-Chem version is equal or newer than 5.0).

Molden input file (.molden or .molden.input or molden.inp): Currently, a wide variety of quantum chemistry packages, such as Molpro, Molcas, ORCA, Q-Chem, CFour, Turbomole, PSI4, MRCC and NWChem, as well as a first-principles code CP2K, are able to produce input file of Molden visualization program. This type of file records atomic coordinates, basis set definition, information of all occupied and virtual orbitals (including expansion coefficient of basis functions, occupation number, spin, energy and symmetry), meanwhile there is no information only specific for Molden. So in fact, Molden input file can be regarded as a standard and general file format for exchanging wavefunction information. For Multiwfn, this type of file can provide atomic coordinate, basis function information and GTF information.

Beware that the Molden input files produced by a lot of programs are quite non-standard! Currently Multiwfn only formally supports the Molden input file generated by Molpro, ORCA, xtb, Dalton, NWChem (only for spherical harmonic functions and meantime symmetry is disabled), MRCC (only for spherical harmonic functions), deMon2k, BDF, CP2K (only for spherical harmonic functions). If the Molden input file you used is generated by other programs, the analysis result may or may not be correct, you should first use the methods described in Appendix 5 to check if the wavefunction has been correctly loaded.

Hint: Multiwfn fully supports the Molden input file standardized by molden2aim utility (see Section 5.1 for detail), which is able to properly recognize Molden input files generated by many other quantum chemistry codes, such as CFOUR and Molcas.

.molden file only formally supports basis functions up to g angular moment. However, subfunction 2 of main function 100 can generate .molden file containing h functions, and Multiwfn can then normally load it. Multiwfn can also normally load .molden file generated by ORCA and Dalton even if h functions are presented.

Although Molden input file also supports Slater type orbital (STO), Multiwfn can only utilize the Molden input file recording Gaussian type basis functions.

One severe drawback of Molden format is that it does not explicitly record nuclear charges as other formats such as wfn and fch, therefore the results relying on nuclear charges (e.g. electrostatic potential and atomic charge) will be problematic when ECP is used. To address this issue, Multiwfn loads atomic indices in the file (i.e. the third column in [Atoms] field) as nuclear charges, thus if you manually change the atomic index to the number of atomic valence electrons (equivalent to effective nuclear charge) that explicitly represented in the quantum chemistry calculation, then the result will be correct. If you are confused about this point, please check this post: http://sobereva.com/wfnbbs/viewtopic.php?pid=721. Alternatively, you can manually insert [Nval] field at the beginning of this file to explicitly specify number of valence electrons for specific elements; for example, the following lines ask Multiwfn to set number of valence electrons of Na and Cl to 9 and 7, respectively, while that of other elements remain unchanged.


```text
[Nval]
Na 9
Cl 7
```


<!-- p.38 -->

It is noteworthy that if you are using ORCA >=6.0, you do not need to perform the aforementioned modification on the molden file, because the molden file exported by ORCA contains [Pseudo] field, which provides correct nuclear charge for the atoms with ECP and Multiwfn automatically loads it (in this case the title line of the molden file must contain orca word so that Multiwfn is able to recognize that it was generated by ORCA).

Another evident disadvantage of using Molden input file as wavefunction carrier is that this format is not as compact as .mwfn and .fch. Due to this reason, for the same wavefunction, loading speed of .molden file is much slower than .mwfn and .fch. Therefore, if you need to frequently analyze a .molden file, I suggest you use subfunction 2 of main function 100 to convert it to .mwfn format.

The way of generating Molden input file by some quantum chemistry programs is described at the beginning of Chapter 4. If you are an ORCA user and you do not want to manually convert the .gbw file to Molden input file via the orca_2mkl utility in ORCA, you can set "orca_2mklpath" in `settings.ini` to actual path of orca_2mkl executable file in ORCA folder, then Multiwfn will be able to directly load .gbw file.

PS: Detailed description about .molden format can be found on Molden official site: https://www3.cmbi.umcn.nl/molden/molden_format.html.

GAMESS-US or Firefly output file (.gms): If you want to use GAMESS-US or Firefly (originally known as PC-GAMESS) output file as input file, you can change its extension as .gms, then Multiwfn will properly recognize it. Currently, I can only guarantee that output file of HF/DFT/TDDFT calculation with default NPRINT option can be normally loaded by Multiwfn. If the point group is not C1, Multiwfn will be unable to deal with the output file.

The role of .gms is similar as .molden and .fch file, i.e. all of them provide atomic coordinates, GTF and basis function information.

Since I am not an experienced Firefly user, I cannot guarantee that the compatibility with Firefly output files is as good as GAMESS-US output files. For the former I only tested DFT single point task and TDDFT task.

Plot files of NBO program (.31~.40): The main purpose of supporting these file types is for visualizing PNAO/NAO/PNHO/NHO/PNBO/NBO/PNLMO/NLMO/MO (their orbital coefficients are recorded in .32~.40 respectively), .31 recorded basis function information. After booting up Multiwfn, you should input the path of .31 file first, and then input the path of one of .32~.40 files (for simplicity, you can only input the suffix when the filenames are identical).

Notice that among all types of orbitals generated by NBO program, only using NBO or NLMO to calculate real space functions is meaningful!

Protein data bank format (.pdb), .xyz, MDL Molfile (.mol/sdf), .mol2: These are the most widely used formats for recording atom coordinates. They do not carry any wavefunction information, but for the functions which only require atom coordinates, using these kinds of files as input is adequate. An advantage of .mol and .mol2 with respect to .pdb and .xyz is that they contain atomic connectivity table, which is need by a few functions of Multiwfn, e.g. Calculation of EEM atomic charges. If .xyz file contains multiple frames, only the first frame will be loaded.

Notice that the .mol file supported by Multiwfn is V2000 version, both the maximum number of atoms and bonds that can be recorded are 999. More descriptions about .mol format can be found in https://en.wikipedia.org/wiki/Chemical_table_file. .sdf file is simply a wrapper of .mol file with additional information.


<!-- p.39 -->

In a standard .xyz file, the name of each atom is element name. However, the .xyz file exported by VMD based on trajectory of some molecular dynamics programs is atom name used in the simulation, in this case Multiwfn is unable to always correctly recognize actual elements from the atom names, so there is special rule in Multiwfn to circumvent this issue: If there is a .pdb file with identical name in the same folder as the inputted .xyz file, element name in the .pdb file will be used instead (however, if for an atom the element name is missing in the .pdb file, the Multiwfn will still guess element from atom name in the .xyz file).

.pqr file: This format is very similar to .pdb format, but with different content. Behind the columns corresponding to atomic X/Y/Z coordinate, there are two columns recording atomic charges and atomic radii, respectively (the number of decimals of the two columns is not important, the fields must be delimited by white-space). This kind of file can provide atom information as well as atomic charge information to Multiwfn. Below is an example .pqr file of water. The REMARK field could exist to record comments, they will be skipped during loading the file.


```text
REMARK From file m1charges.out
REMARK ESP charges
ATOM      1 O    O 1     1       0.000   0.123   0.000 -0.680698  2.9000
ATOM      2 H    O 1     1       0.757  -0.490   0.000  0.340338  2.6000
ATOM      3 H    O 1     1      -0.757  -0.490   0.000  0.340361  2.6000
```

Charge files (.chg): This type of plain text file can be generated by some functions of Multiwfn (e.g. population analysis functions), it contains element names (less than or equal to two characters), atom coordinates (first three columns, in Å) and charges (the fourth column), users can modify them manually. This file is free-formatted, all fields must be delimited by white-space. This file can provide atomic charge information, the main use of which is to visualize electrostatic potential and analyze it on molecular surface based on atomic charges, the electrostatic interaction energy based on atomic charges can also be evaluated by subfunction -2 of main function 7 using .chg as input file. When .chg file is loaded, the sum of all atomic charges as well as electric dipole moment calculated using the atomic charges will be shown on screen.

An example of .chg file of water molecule is given below:


```text
  O     0.000000    0.000000    0.119308   -0.301956
  H     0.000000    0.758953   -0.477232    0.150977
  H     0.000000   -0.758953   -0.477232    0.150977
```

.gro file: GROMOS structure format. This kind of file is most frequently employed in GROMACS molecular dynamics program. .gro file can only provide atomic information for Multiwfn. Note that since this file records atom name rather than element, Multiwfn automatically guesses the actual element based on atom names and residue names during loading. However, sometime the guessed element may be incorrect, therefore it is recommended to examine the printed molecular formula after loading the file.

.cif file: This is the standard format for recording crystal structure. Symmetry operations must be explicitly given in this file, otherwise positions of equivalent atoms cannot be generated.

Gaussian-type cube file (.cub or .cube): This is the most popular volumetric data format, it can be generated by vast computational chemistry softwares and can be recognized by the majority of molecular graphics programs. Atom coordinates, a set of grid data of real space function or multiple sets of grid data of molecular orbitals could be recorded in this file. After a cube file is


<!-- p.40 -->

loaded into Multiwfn, one can choose main function 0 to visualize isosurfaces, or use main function 13 to process the grid data.

.vti, .dx and DMol3 grid file (.grd) .vti is "ParaView VTK Image Data" format, which can record scalar field and vector field. This kind of file can be generated by e.g. GIMIC 2.0 and ParaView programs. Only .vti file containing scalar data of ASCII type is supported. Briefly speaking, this file is very similar to .cub file, but no atom information is presented.

.dx is volumetric data format that can be exported by e.g. Volmap plugin of VMD program. .grd file is the volumetric data format mainly used by DMol3 program. No atom information is recorded in .grd.

Gaussian input file (.gjf), ORCA input file and MOPAC input file (.mop): These files can

provide atom coordinate information as well as the number of α and β electrons information to Multiwfn. Note that the atoms must be recorded as Cartesian coordinate. .gjf can also provide cell information to Multiwfn via “Tv” field.

Gaussian and ORCA output files Gaussian and ORCA output files may provide atom information for Multiwfn.

- Gaussian output file: When "iloadGaugeom" in `settings.ini` is set to 1 (default, load input orientation) or 2 (load standard orientation), Multiwfn will load (final) geometry and number of electrons from this file.

- ORCA output file: When "iloadORCAgeom" in `settings.ini` is set to 1 (default), Multiwfn will load (final) geometry from this file.

CP2K input and restart file (.inp and .restart): These files can provide atom coordinate information and cell information to Multiwfn. Note that the atoms must be recorded as Cartesian coordinate in Å.

Quantum ESPRESSO input (.inp or .in): It can provide atom coordinate information and cell information to Multiwfn. Only ibrav=0 is supported.

Turbomole coordination file: If the first line of a plain text file is &coord, then it will be loaded as Turbomole coordination file. $coord field provides atomic information. If $periodic and $lattice are available, they will also provide cell information.

VASP related files The following files are related to VASP code. Multiwfn is able to load them, the file name must contain corresponding string and there is no .in or .inp extension. For example, to load a file as POSCAR, the file name could be such as POSCAR_Si8 and MOF.POSCAR.

- POSCAR: This is one of input files of VASP, records cell and atom information.
- CHGCAR or CHG: This file records electron density generated by VASP. For spin polarization case, it also records spin density at the same time

- ELFCAR: This file records ELF generated by VASP. For spin polarization case, it records
