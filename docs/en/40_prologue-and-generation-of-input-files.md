# Prologue and generation of input files

> Multiwfn manual, p.458–460. Images: `../imgs/`.

---

<!-- p.458 -->


## 4  Tutorials and Examples


## Prologue and generation of input files

Welcome to use Multiwfn! If you have not read "ALL USERS MUST READ" on page 2 of this manual, please read it first. If you encounter any problem in using Multiwfn, please free feel to post topic on Multiwfn forum.

Before getting started, I first show you how to generate various kinds of input files. Notice that different functions in Multiwfn require different types of input file, see Section 2.5 for explanation. Briefly speaking, for any analysis that is solely based on real space function, you can use .wfn or .wfx as input file. However, many functions require basis function information, in these cases you have to use .mwfn, .fch/fchk, .molden or .gms file as input file. Since these files contain richer information than .wfn/wfx file (i.e. basis functions and virtual orbitals), in principle for any function that requires .wfn/wfx file as input file, you can also use .mwfn/fch/molden/gms instead. A few functions in Multiwfn (e.g. AdNDP and ICSS analysis) rely on some special files, requirements on the input files for these situations are clearly indicated in corresponding section in Chapter 3.

Generating .wfn and .wfx files

- Gaussian: Write out=wfn in route section, leave a blank line after molecular coordinate section and write the destination path of .wfn file, e.g. C:\otoboku\H2O.wfn (you can consult H2O.gjf in “examples” folder), then run this file. If the task terminates normally, H2O.wfn will appear in "C:\otoboku" folder.

If you would like to generate .wfx file in Gaussian (supported since G09 B.01), simply write out=wfx instead of out=wfn in route section.

If you use MCSCF in Gaussian, in order to generate and export natural orbitals to .wfn, you should also use pop=no keyword. If you are using Gaussian older than G09 C.01, please carefully read the information below:

If the theoretical method is post-HF type, you have to also add “density” keyword in route section to use current density, otherwise what outputted to .wfn file will still be HF orbitals. If you are using TDDFT or CIS and you want to export natural orbitals corresponding to excited state wavefunction, you also need to specify "density" keyword.

For CCD/CCSD, QCISD or MP2/3, MP4SDQ tasks based on unrestricted HF reference state, only when “pop=NOAB” keyword is also specified then natural spin orbitals rather than spatial natural orbitals will be saved to the .wfn file. TD, CI and MCSCF tasks of Gaussian cannot produce natural spin orbitals.

If the Gaussian you are using is older than G09 B.01, be aware that there is a serious bug, if your task is restricted open-shell (ROHF and RODFT), the occupation numbers of singly occupied orbitals in .wfn file will erroneously be 2.0, you have to open the file by text editor, locate the last entry "OCC NO =", and then manually change the value behind it to 1. 0000000.

- GAMESS-US: Add AIMPAC=.TRUE. in $CONTRL section. After the task is finished, the generated .dat file in the folder defined by $SCR environment variable (see rungms script) will contain wavefunction information with the same format as .wfn file, extract the content between "----- TOP OF INPUT FILE FOR BADER'S AIMPAC PROGRAM -----" and "----- END OF INPUT FILE FOR BADER'S AIMPAC PROGRAM -----" and save them to a new file with “.wfn” suffix.

- ORCA: .wfn and .wfx files can be generated simply using aim keyword in the input file, or using the command orca_2aim XXX to convert XXX.gbw to XXX.wfn and XXX.wfx. At least for


<!-- p.459 -->

ORCA 4.1, .wfn and .wfx files cannot be generated when ECP is used. Using .molden file as input file of Multiwfn is always more recommended.

As regards the method of outputting .wfn files in other quantum chemistry packages, please consult corresponding manuals.

Generating .fch file

- Gaussian: First run a Gaussian task with e.g. "%chk=test.chk" to yield binary checkpoint file test.chk file, then run command formchk test.chk to convert test.chk to test.fch.

Note: There is no difference between .fch and .fchk formats. The former and the latter are the default extensions of formatted checkpoint file of Windows and Linux version of Gaussian, respectively. You can use either of them as input file of Multiwfn.

When post-HF task is performed, the orbitals and occupations recorded in Gaussian .fch file by default are the HF ones, hence the Multiwfn analysis results are identical to HF. Similarly, under default case, analysis results based on .fch file produced by TDDFT task are identical to ground state DFT wavefunction. To analyze wavefunction for post-HF wavefunction or TDDFT excited state wavefunction, analysis should be done using natural orbitals (NOs) at corresponding level, there are two ways to yield them:

(1) Make Multiwfn generate natural orbitals (or spin natural orbitals, natural spin orbitals) by using subfunction 16 of main function 200. See Section 3.200.16 for details. This way is recommended since it is very convenient.

(2) Make Gaussian write natural orbitals into .fch file. You should first perform post-HF or TDDFT task with “density” keyword, and then rerun the task only with "guess (save,only,naturalorbitals) chkbasis" in route section. Note that Gaussian fills orbital occupation numbers into orbital energy field in .fch file, hence you should write “saveNO” in the first line of .fch file to let Multiwfn know this behavior. Beware that if what you performed is open-shell post-HF calculation, even above process is unable to correctly store natural spin orbitals into .fch file. Generally, I strongly recommend using .wfn/.wfx file to view natural orbitals and analyze real space functions for post-HF wavefunctions.

For MCSCF calculation, you should load the resulting .fch file and use subfunction 16 of main function 200 to generate .molden file containing NOs at MCSCF level, and then use this .molden file as input file. Since for MCSCF the alpha and beta orbitals cannot be generated separately, for systems with spin multiplicity larger than 1, you must manually open the .fch file, set "Number of beta electrons" to the same value as "Number of alpha electrons" to make Multiwfn recognize that there is only one set of orbitals in the input file.

- Q-Chem: Write GUI 2 in $rem field, after task has finished, you will find the resulting .fchk file in current folder. Beware that if you are using quite old version (maybe ≤5.0) of Q-Chem, before loading the .fchk files into Multiwfn, you must set “ifchprog” in `settings.ini` to 2.

- PSI4: The .fchk file produced by currently latest version (not older versions) of PSI4 is compatible with Multiwfn. The examples\psi4_fch.inp is an example file of generating .fchk file at B3LYP/6-31G** level. In Section 4.A.8, I also show how to analyze post-HF wavefunction based on .fchk file of PSI4.

Generating .molden file
- ORCA: Using the command orca_2mkl XX -molden to convert XX.gbw to Molden input file

XX.molden.input. You do not need to then manually change the suffix from .molden.input to .molden, since the former can also be recognized by Multiwfn. You can also set "orca_2mklpath" in `settings.ini` to actual path of orca_2mkl executable file in ORCA folder,


<!-- p.460 -->

then Multiwfn will be able to directly load .gbw file.
- Molpro: Adding such as put,molden,ltwd.molden at the last line of your input file, the Molden

input file ltwd.molden will be produced after finishing the calculation.
- Dalton: The program automatically outputs .molden file when calculation is finished. The file

is molden.inp in .tar.gz package. This file can be directly loaded without changing suffix.
- NWChem: An example input file is provided as examples\NWChem_molden.nw. After running

it, the .molden file will be generated in current folder. Notice that spherical harmonic basis functions must be employed (i.e. the "spherical" keyword) and "noautosym" keyword must be employed when the system has symmetry of point group.
- MRCC: Once the calculation is normally finished, a file named MOLDEN will be generated in

current folder. Then rename it to make it have .molden suffix. An example is given in Section 4.A.8.
- xtb: Run xtb with "--molden" option, then molden.input will be generated in current folder.
- Other programs: Please consult corresponding manuals.

When pseudopotential is used and you need to do some analyses relating to nuclear charges, do not forget to manually change atomic indices in the .molden file as nuclear charges, see Section 2.5 for details.

Note: Currently, only the Molden input file generated by Molpro, ORCA, xtb, Dalton, NWChem, MRCC, deMon2k, BDF programs are formally supported. If the file is generated by other programs, the result may or may not be correct, because the files produced by numerous programs are non-standard or problematic. Fortunately, molden2aim utility is able to deal with the Molden input files produced by wider scope of programs and can output standardized Molden input files, which is then able to be used as Multiwfn input file. See Section 5.1 for detail.

Generating .gms file GAMESS-US and Firefly (old name is PC-GAMESS) output file can also be used as Multiwfn input file, you need to change its suffix as .gms so that Multiwfn can recognize it. Currently, I can only guarantee that output file of HF/DFT calculation with default NPRINT option can be normally loaded by Multiwfn. A sample of input and output files of GAMESS-US are provided as GAMESS_US.inp and UKS_cc-pVDZ.gms in examples folder, respectively.

Now let us start! Note that the examples in 4.x section are relevant to main function x, therefore you can quickly find the examples that you need. Section 4.A includes special topics and advanced tutorials, in which more than one functions and some advanced skills may be involved, such as studying aromaticity and weak interactions. You can find almost all of the files involved in these examples in “examples” folder. All the texts behind // are comments and should not be inputted as command. Tutorials in this chapter only cover basic applications of Multiwfn, if you want to learn the usage of more functions and more options, please read corresponding sections in Chapter 3 and play with the options that are not mentioned in the examples.

For most examples, I take .fch or .wfn as format of input file, however it never means these functions can only accept these two formats! If you have read Section 2.5, you must know how to properly choose format of input file for different functions.

PS1: If you would like to analyze wavefunction higher than CCSD level, reading Section 4.A.8 is suggested, you will need ORCA, PSI4 or MRCC program.

PS2: In chapter 4, many my blog articles written in Chinese are involved, they often contain extended discussion and more examples. If you cannot read Chinese, you can try to use Google translator (For example, you can install Mozilla Firefox add-on called "Google translator for Firefox". After a successful installation, you will find an icon "T" in the Firefox toolbar. Now open
