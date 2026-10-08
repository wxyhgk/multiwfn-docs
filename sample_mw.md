# Multiwfn 样张（10页）


<!-- p.22 -->

**（原书 p.22）**

# 1  Overview
Multiwfn is a powerful wavefunction analysis program, it supports almost all of the most important wavefunction analysis methods. Multiwfn is free, open-source, high-efficient, very userfriendly and flexible. Multiwfn can be downloaded at Multiwfn official website http://sobereva.com/multiwfn. This code is developed by Tian Lu at Beijing Kein Research Center for Natural Sciences (http://www.keinsci.com).
Input files supported by Multiwfn Multiwfn accepts many kinds of files for loading wavefunction information: .mwfn (Multiwfn wavefunction file), .wfn/.wfx (Conventional / Extended PROAIM wavefunction file), .fch (Gaussian formatted check file), .molden (Molden input file), .31~.40 (NBO plot files) and .gms (GAMESS-US and Firefly output file). Other types such as Gaussian input and output files, .cub, .grd, .pdb, .xyz and .mol files can be used for specific functions.
Briefly speaking, Multiwfn can perform wavefunction analyses based on outputted file of almost all well-known quantum chemistry programs, such as Gaussian, ORCA, GAMESS-US, Molpro, NWChem, Dalton, xtb, PSI4, Molcas, Q-Chem, MRCC, deMon2k, Firefly, CFOUR, Turbomole... Since .molden file exported by CP2K is also supported, Multiwfn is not only able to deal with molecular systems but can also analyze periodic systems (though limited functions can be used, see Section 2.9 of manual for detail).
Special points of Multiwfn (1) Very comprehensive functions. Almost all of the most important wavefunction analysis methods have been well supported by Multiwfn.
(2) Extremely user-friendly. Multiwfn is designed as an interactive program (but can also run silently and be embedded into shell script), prompts shown on screen in each step clearly tell users what should input next. Multiwfn also never prints obscure messages, therefore there is no any barrier even for beginners. In addition, all wavefunction analysis theories are very detailedly documented, and there are more than one hundred well-written examples in the manual; furthermore, there is a "quick start" document that guides new users to master common analyses immediately. Moreover, the developer always very timely and patiently replies all users' questions in Multiwfn official forum.
(3) High flexibility. The design of the overall framework, functions and user interface of Multiwfn is rather flexible, but this does not sacrifice ease of use. Different modules of Multiwfn are organically integrated together to make numerous analyses that single module cannot realize feasible
(4) High efficiency. The code of Multiwfn is substantially optimized. Most parts are parallelized by OpenMP technology. For computationally intensive tasks, the efficiency of Multiwfn exceeds analogous programs significantly.
(5) Results can be visualized directly. A high-level graphical library DISLIN is invoked internally and automatically by Multiwfn for visualizing results, most plotting parameters are controllable in interactive interface. This remarkably simplified wavefunction analysis, especially

<!-- p.31 -->

**（原书 p.31）**

# 2  General information

## 2.1 Install

### 2.1.1 Windows version
What you need to do is just uncompressing the program package, then you can start to use by double-clicking the icon.
A few functions in Multiwfn rely on Gaussian, if you need to carry out these analyses, you need to setup environment variables for Gaussian manually, see Appendix 1.
It is strongly suggested to set "nthreads" in `settings.ini` to actual number of CPU physical cores of your machine, so that all computing power of your CPU could be utilized during calculation. See Section 2.4 for more detail.
If you want to make Multiwfn able to directly open .chk file produced by Gaussian, set "formchkpath" in `settings.ini` to actual path of formchk executable file in Gaussian package.

### 2.1.2 Linux version
Note: Chinese version of this section is my blog article “Chinese instructions for installing Multiwfn under Linux” (http://sobereva.com/688).
- Uncompress the Multiwfn binary package
- Make sure that you have installed motif package, which provides libXm.so.4, full version of
Multiwfn cannot boot up without this file. The motif is freely available at https://motif.ics.com/motif/downloads. If you are a CentOS or Red Hat Linux user and have not installed motif, you can directly run yum install motif to install it; alternatively, you can download corresponding rpm package (e.g. motif-2.3.4-1.x86_64.rpm) and manually install it; If you are an Ubuntu user, run sudo apt-get install libxm4 libgl1 to install it, or download deb package (e.g. libmotif4_2.3.4-1_amd64.deb) and manually install it.
- Add below lines to ~/.bashrc file (using e.g. vi ~/.bashrc command)

```text
export OMP_STACKSIZE=1000M
ulimit -s unlimited
```
These lines remove limitation on stacksize memory, and define stacksize of 1000MB for each OpenMP thread during parallel calculations, see Section 2.4 for detail.
Note: If ulimit -s unlimited does not work properly on your system, try to use ulimit -Sn unlimited instead.
- Run cat /proc/sys/kernel/shmmax to check if the size of SysV shared memory segments is
large enough (unit is in bytes); if the value is too small, Multiwfn may crash when analyzing big wavefunction. To enlarge the size, for example you can add kernel.shmmax = 5000000000 to /etc/sysctl.conf and reboot system, then the upper limit will be enlarged to about 5GB.
- Assume that you are using Bash shell, and you have decompressed the Multiwfn package as
“/sob/Multiwfn_3.6_bin_Linux” folder, you should add below lines into ~/.bashrc file:

```text
export Multiwfnpath=/sob/Multiwfn_3.6_bin_Linux
export PATH=$PATH:/sob/Multiwfn_3.6_bin_Linux
```

<!-- p.32 -->

**（原书 p.32）**
- Run below command to add executable permission to Multiwfn executable file:

```text
chmod +x /sob/Multiwfn_3.6_bin_Linux/Multiwfn
```
- Configure the settings.ini file in Multiwfn folder in the same way as described in last Section
After re-entering the terminal, you can boot up Multiwfn anywhere by simply running Multiwfn command.
If you use Multiwfn via remote connection to a server with text-only mode, and you find Multiwfn get stuck by about two seconds after loading input file, please add export DISPLAY=":0" to your ~/.bashrc file.
Linux version of Multiwfn works well on CentOS 6/7/8, Rocky Linux 9 and Ubuntu 12/14/16/22. I cannot guarantee that the program is completely compatible with all other Linux distributions. If system prompts you that some dynamical link libraries (.so files) are missing when booting up Multiwfn, please try to find and install the packages which contain the corresponding .so files.
If you encounter difficulty when running/compiling Multiwfn due to missing or incompatibility of some graphics related library files, and meantime you do not need any visualization function of Multiwfn, you can run/compile Multiwfn without GUI supported, all functions irrelevant to GUI and map plotting will still work normally. Please check “COMPLIATION_METHOD.txt” in source code package on how to compile this special version, the pre-compiled executable file of this version can also be downloaded from Multiwfn website (termed as "noGUI" version).

### 2.1.3 Mac OS version
As I am not a MacOS user, there is no MacOS release of Multiwfn. If you want to compile Multiwfn on MacOS, please check https://github.com/digital-chemistry-laboratory/multiwfn-macbuild. If you can read Chinese, see http://bbs.keinsci.com/thread-46059-1-1.html.
After compilation of Multiwfn, you should do following steps (but I cannot guarantee that the first two steps below still work for latest version of MacOS):
(1) Add the following line to your .profile file (e.g. /Users/sob/.profile) to make them take effect automatically, then reboot your terminal. If the .profile is nonexistent, you should create it manually.

```text
export OMP_STACKSIZE=64000000
```
OMP_STACKSIZE defines stacksize (in bytes) for each thread in parallel implementation, see Section 2.4 for detail.
(2) Run sysctl -a|grep shmmax to check if the size of SysV shared memory segments is large enough (unit is in bytes), if the value is too small, Multiwfn may crashes when analyzing big wavefunction. In order to enlarge the size, you should edit or create the file /etc/sysctl.conf, and add kern.sysv.shmmax = 512000000 to it and reboot system, then the upper limit will be enlarged to about 512MB.
(3) Set Multiwfnpath environment variable if needed, see point 5 of Section 2.1.2. (4) Configure the `settings.ini` file in the same way as described in Section 2.1.1. An alternative method of running Multiwfn on MacOS was provided by a Multiwfn user Maciej Spiegel:
First of all, a user should download the newest version of Unofficial Wineskin (https://github.com/Gcenx/WineskinServer/releases/tag/V1.8.4). After that, run it, update the wrapper version and download one of the most recent engines. These are WS11WineCX64Bit19.0.1-1 (for 64bit system) or WS11WineCX19.0.1-1 (for 32bit system). Finally, one should create new wrapper and use Windows GUI installer.

<!-- p.41 -->

**（原书 p.41）**
ELF for  and  electrons separately.
- LOCPOT: This file records external potential felt by one electron generated by VASP. For
spin polarization case, it records the potential for  and  electrons separately. If LVHAR=.TRUE., the potential corresponds to negative of electrostatic potential; while if LVHAR=.FALSE., it corresponds to “potential acting on one electron in a molecule” (PAEM, described in Section 2.7).
Plain text file: This file type is only used for special functions, such as plotting DOS graph, plotting spectrum, generating Gaussian input file with initial guess. See explanations in corresponding sections.

## 2.6 Real space functions
The "Real space functions" in this manual are referred to as the functions whose variables are coordinate of the three-dimension space of present system. Real space function analysis is one of the most important functions of Multiwfn, the supported real space functions are listed below. All wavefunctions are assumed to be real type, all units are in atomic unit (a.u.).
Notice that for speeding up calculation, especially for big system, when evaluating a exponential function (except for some real space functions, such as 12, 14 and 16), if the exponent is more negative than -40, then this evaluation will be skipped. The default cutoff value is safe enough and cannot cause detectable loss of precision even in quantitative analysis, you can also disable this treatment or adjust cutoff, see “expcutoff” in `settings.ini`.
1 Electron density
2 2

![](../sample_imgs/formula_p41_01.png)

<!-- formula-raw p.41: C==rrr -->
, ( ) ( ) ( ) i i i i i i
where i is occupation number of orbital i,  is orbital wavefunction,  is basis function. C is coefficient matrix, the element of the ith row jth column corresponds to the expansion coefficient of orbital j respect to basis function i. Atomic unit for electron density can be explicitly written as 1/Bohr3 (which corresponds to 6.74833/Å3, since 1 Bohr = 0.529177Å).
When input file does not contain GTF information, this function will be calculated as promolecular density, which is approximate molecular electron density simply constructed by superposing built-in spherically averaged free-state atomic density of all atoms in the system. See Appendix 3 on how the built-in atomic densities were derived.
It is worth to note that distribution character of valence electron density is much more informative than electron density, this point was thoroughly discussed in my work Acta Phys. -Chim. Sin., 34, 503 (2018) DOI: 10.3866/pku.Whxb201709252.
2 Gradient norm of electron density
2 2 2 ) ( ) ( ) ( ) (      

![](../sample_imgs/formula_p41_02.png)

<!-- formula-raw p.41:  ⏎  ⏎ =zyx ⏎ rrrr ⏎ + ⏎ + -->

<!-- p.51 -->

**（原书 p.51）**
Since we already have explicit expression to calculate ГXC term, other quantities introduced earlier can be easily computed according to the relationships between them and ГXC. Recall that

![](../sample_imgs/formula_p51_03.png)

<!-- formula-raw p.51: =rr. ⏎  ⏎  -->
2 ( ) ( ) i i i
Postscript: One can show that XC,approx
α,tot (𝐫1, 𝐫2) also exactly holds the requirement that
integration of r2 over the whole space is equal to −𝜌(𝐫1). However, in common, integrating r2 over the whole space for X,approx

![](../sample_imgs/formula_p51_04.png)

<!-- formula-raw p.51: α,tot(𝐫1, 𝐫2)  deviate from −𝜌(𝐫1)  and zero, ⏎ α,tot(𝐫1,𝐫2)  and C,approx ⏎ α,tot. ⏎ α,tot and C -->
respectively, which are basic properties of exact form of X

> **Usage** — In Multiwfn, r1 is seen as reference point and r2 is seen as variable, to define the coordinate of reference point, just modifying “refxyz” in `settings.ini` before booting up.
“paircorrtype” parameter in `settings.ini` controls which type of correlation effect will be taken into consideration in calculation of Г. Since correlation hole and correlation factor are calculated based on Г, this setting also affects them. For single-determinant wavefunction, =1 and =3 are equivalent and =2 is meaningless, because Coulomb correlation is completely omitted.
=1: Only consider exchange correlation =2: Only consider Coulomb correlation =3: Consider both exchange and Coulomb correlation “pairfunctype” parameter in `settings.ini` controls which function and which spin will be calculated by real space function 17, see below, those enclosed by parentheses are for single-
determinant wavefunction cases. Of course, for closed-shell system, the results for  spin are exactly identical to those for β spin. Note that correlation factor for post-HF wavefunction case is undefined.
=1: h,tot (h,) =2: h,tot (h,) =4: Undefined (f ,) =5: Undefined (f ,) =7: ,tot (,) =8: ,tot (,) =10: , when paircorrtype =1 (,) =11: , when paircorrtype =1 (,) =12: any,any (any,any) For example, if paircorrtype=1 and pairfunctype=2, for post-HF wavefunction, what will be
calculated is ,tot X 1 2 ( , ) h r r , which is equivalent to X 1 2 ( , ) hr r since β electron pairs have no
exchange correlation. This quantity can be interpreted as Fermi hole at r2 caused by an  electron present at r1.
18 Average local ionization energy Average local ionization energy is written as (Can. J. Chem., 68, 1440 (1990))

![](../sample_imgs/formula_p51_05.png)

<!-- formula-raw p.51: =i ⏎ rr -->
| |) ( ) ( r
i i I
) (
where i(r) and i are the electron density function and orbital energy of the ith molecular orbital, respectively. Hartree-Fock and typical DFT functionals such as B3LYP are both suitable for computing 𝐼̅. Lower value of 𝐼̅ indicates that the electrons at this point are more weakly bounded. 𝐼̅ has widespread uses, for example revealing atomic shell structures, measuring electronegativity, predicting pKa, quantifying local polarizability and hardness, but the most important one may be

<!-- p.54 -->

**（原书 p.54）**
24 Interaction region indicator (IRI) IRI was proposed by me in Chemistry—Methods, 1, 231 (2021), which is extremely useful in revealing all kinds of interaction regions of chemical system. See Section 3.23.8 for detailed information. IRI is defined as

![](../sample_imgs/formula_p54_06.png)

<!-- formula-raw p.54: aIRI=rr -->
| ( )| ( )
[ ( )]
r
where a corresponds to "uservar" in `settings.ini`. When it is set to 0, then the recommended value 1.1 is employed. See Section 3.23.8 for detailed introduction of IRI. Note that IRI is set to an
arbitrarily large value (5.0) if  is equal or smaller than “IRI_rhocut” in `settings.ini`, so that IRI isosurfaces in uninterested extremely low  regions will not occur. If “IRI_rhocut” is set to 0 then this treatment is not applied. For basin analysis and topology analysis for IRI or IRI-, it should be set to 0 to avoid occurrence of artificial extrema due to this treatment (this is automatically done by Multiwfn).
25 van der Waals potential Van der Waals (vdW) potential is very important for studying intermolecular interactions dominated by vdW effect, it has comparable role of electrostatic potential for intermolecular interactions dominated by electrostatic effect. See Section 3.23.7 for introduction of this function. The unit of this function is in kcal/mol, the probe atom can be set by "ivdwprobe" in `settings.ini`.

## 2.7 User-defined real space function
In real space function selection menu, you can find a term named "User-defined real space function". In order to avoid lengthy list of real space functions, numerous uncommonly used real space functions are not explicitly presented in the list. However, if you want to use them, you can set "iuserfunc" parameter in `settings.ini` to one of the indices (see below), then the user-defined function will be pinned to corresponding function. For example, before running Multiwfn, if you set "iuserfunc" to 2, then the user-defined real space function will be equivalent to density of beta electrons. An alternative way of setting user-defined function is inputting iu in the main menu, you can input the index of the user-defined function.
In fact, the user-defined function corresponds to “userfunc” function in source file function.f90. By filling in proper code yourself, the functions supported by Multiwfn can be easily extended. For example, after filling the code "userfunc=fgrad(x,y,z,'t')**2/8/fdens(x,y,z)" into proper place of “function userfunc” in function.f90 and recompile Multiwfn, the integrand of Weizsäcker kinetic
2 W[ ] ( ) /[8 ( )]d     =   r r r , will be ready for use. When you
energy functional, namely
write your own code you can refer to existing codes, a list of built-in functions is given in Appendix 2 of this manual.
Prebuilt user-defined functions

<!-- p.70 -->

**（原书 p.70）**

## 2.8 Graphic formats and image size
Multiwfn supports a lot of mainstream graphic formats, including: 1 Postscript (ps) 2 Encapsulated postscript (eps) 3 Portable document format (pdf) 4 Windows metafile format (wmf) 5 Graphics interchange format (gif) 6 TIFF (tiff) 7 Portable network graphics (png) 8 Windows bitmap format (bmp) 9 Scalable vector graphics (svg) The graphic format of the picture exported by Multiwfn is controlled by “graphformat” parameter in `settings.ini`, you can set this parameter to the texts in the parentheses listed above, the default format is “png”.
For curve maps, the height and weight of the image file are controlled by “graph1Dsize” parameter in `settings.ini`. “graph2Dsize” is responsible for two-dimension data plotting (color-filled map, contour map, relief map, etc.). “graph3Dsize“ is responsible for three-dimension data plotting (isosurface graph, molecular structure graph, etc.).
Tip 1: If the graph is mainly composed of lines, e.g. contour line map and curve map, the best formats are pdf and svg. However, if you need to embed the resulting graph to Office, commonly wmf format should be used.
Tip 2: If you want to make background of exported image file transparent, please look this video illustration: https://youtu.be/E7lAGac3aDM.

## 2.9 Analysis of periodic systems
Multiwfn is able to deal with periodic systems, details will be given in this section. To analyze wavefunction for periodic systems, you can use either wavefunction of cluster model produced by quantum chemistry codes, or use periodic wavefunction produced by CP2K program, as will be described in Section 2.9.1 and 2.9.2, respectively. There are many analyses in Multiwfn independent of wavefunction, special attention of applying them to periodic systems will be described in Section 2.9.3.
2.9.1 Wavefunction analysis on wavefunction of cluster model
You can extend primitive cell of the crystal to a large supercell, then extract a cluster from the supercell. Based on this cluster, you can use any quantum chemistry code to carry out optimization or single point task and then analyze the resulting wavefunction as usual in Multiwfn. Of course, to minimize artificial boundary effect due to the finite cluster size, the cluster should be large enough. If you are not sure what the minimum acceptable size is, you can perform a convergence test for the

<!-- p.601 -->

**（原书 p.601）**

### 4.8.1 Analyze acetamide by Mulliken method
In this example we employ Mulliken method to first analyze the composition of the 6th molecular orbital of acetamide, and then analyze which orbitals have main contribution to the bonding between formamide part and methyl group. Beware that Mulliken method is incompatible with diffuse functions, if they are involved, you should either choose other orbital composition methods (e.g. NAO, Hirshfeld...) or remove them from your basis set.
Boot up Multiwfn and input following commands examples\CH3CONH2.fch // You have to use .mwfn/.fch/.molden/.gms file as input for this type of analysis
8 // Orbital composition analysis 1 // Use Mulliken partition 6 // The orbital index is 6 (Note that as shown in the prompt on the screen, you can also input orbital label here, for example h-3 corresponds to HOMO-3, l+1 corresponds to LUMO+1, etc.)
The composition of basis functions, shells and atoms are printed immediately, see below.

```text
Threshold of absolute value:  >   0.50000 %    // Only the basis functions with composition
larger than 0.5% will be printed, you can change the threshold by “compthres” parameter
in settings.ini.
Orbital:     6  Energy(a.u.):     -0.905290  Occ:  2.000000  Type: Alpha&Beta
 Basis Type    Atom    Shell      Local       Cross term        Total
   23   S        5(C )   14      0.44902 %      0.67507 %      1.12409 %
   24   X        5(C )   15      0.31240 %      0.50522 %      0.81762 %
   25   Y        5(C )   15      4.25271 %      5.88221 %     10.13493 %
   29   Y        5(C )   17      0.00777 %     -0.61063 %     -0.60286 %
   38   S        6(O )   20      3.50037 %      2.65507 %      6.15544 %
   42   S        6(O )   22      3.29488 %      1.71316 %      5.00803 %
   53   S        7(N )   26     15.20411 %     15.32688 %     30.53098 %
   57   S        7(N )   28     16.89006 %     17.40040 %     34.29046 %
   61   XX       7(N )   30      0.00774 %      0.58279 %      0.59053 %
   63   ZZ       7(N )   30      0.02793 %     -0.98090 %     -0.95297 %
   67   S        8(H )   31      1.27855 %      3.03091 %      4.30946 %
   69   S        9(H )   33      1.52931 %      3.60949 %      5.13880 %
Sum up those listed above:      46.75484 %     49.78967 %     96.54451 %
Sum up all basis functions:     51.95605 %     48.04395 %    100.00000 %
Composition of each shell, threshold of absolute value:  >    0.500000 %
Shell    14 Type: S    in atom    5(C ) :     1.12409 %
Shell    15 Type: P    in atom    5(C ) :    10.95268 %
Shell    17 Type: P    in atom    5(C ) :    -0.97156 %
Shell    20 Type: S    in atom    6(O ) :     6.15544 %
Shell    22 Type: S    in atom    6(O ) :     5.00803 %
Shell    26 Type: S    in atom    7(N ) :    30.53098 %
Shell    28 Type: S    in atom    7(N ) :    34.29046 %
Shell    31 Type: S    in atom    8(H ) :     4.30946 %
```

<!-- p.602 -->

**（原书 p.602）**

```text
Shell    33 Type: S    in atom    9(H ) :     5.13880 %
Composition of different types of shells (%):
s:  88.193  p:  11.391  d:   0.416  f:   0.000  g:   0.000  h:   0.000
Composition of each atom:
Atom     1(C ) :     1.17249 %
Atom     2(H ) :     0.05445 %
Atom     3(H ) :     0.03212 %
Atom     4(H ) :     0.00817 %
Atom     5(C ) :    11.81245 %
Atom     6(O ) :    11.63274 %
Atom     7(N ) :    65.50085 %
Atom     8(H ) :     4.47022 %
Atom     9(H ) :     5.31651 %
Orbital delocalization index:   46.15
```
The result indicates that nitrogen has primary contribution (65.5%) to orbital 6, and the contribution consists of two S-shells (30.5% and 34.3%). P-shells of neighbouring carbon and Sshells of oxygen have slight contribution too (both are about 12%). We can check if the result is reasonable by viewing isosurface (isovalue is set to 0.1 here):
From the graph, the region where the value of orbital wavefunction is large is mainly localized around nitrogen, and there is no nodal plane, so the orbital wavefunction in this region should be constructed from s-type orbitals. The isosurface also somewhat intrudes into the region of atom C5 and O6, so they should have small contribution to MO 6, moreover, because there is a nodal plane in C5, the atomic orbitals of C5 used to form MO 6 should be p-type. Obviously, these conclusions are in fairly agreement with composition analysis. The advantage of composition analysis is that the result can be quantified, while by visual study we can only draw qualitative conclusion, for some complex system we cannot draw even qualitative conclusion.
The " Orbital delocalization index" printed at the end of the output has close relationship with extent of spatial delocalization of the orbital, this point will be described in Section 4.8.5 in detail.
Now let us find which molecular orbitals have main contribution to the bonding between

![](../sample_imgs/p602_001.png)

<!-- p.801 -->

**（原书 p.801）**
structure
17 // Basin analysis 1 // Generate basins 1 // Electron density 2 // Medium-quality grid 7 // Integrate real space functions in AIM basins with mixed type of grids 2 // Exact refinement of basin boundary 6 // Hamiltonian kinetic energy K(r) The result is

```text
    Atom       Basin       Integral(a.u.)   Vol(Bohr^3)   Vol(rho>0.001)
     1 (C )       2         36.98331415       243.914        67.166
     2 (H )       4          0.59352399       554.936        49.848
     3 (O )       1         75.30251602       887.039       127.096
     4 (H )       3          0.59369956       567.076        49.832
Sum of above integrals:           113.47305372
Sum of basin volumes (rho>0.001):     293.942 Bohr^3
```
The electronic energy yielded by quantum chemistry calculation can be manually found at the end of the H2CO.wfn, namely -114.50047 a.u., which is also printed by Multiwfn after loading this file. Note that the T is 113.47305 a.u., hence the atomic energy of O3 can be calculated as 75.30252*-114.50047/113.47305 = -75.98433 a.u., similarly for other atoms. You can also then manually sum up atomic energy for some atoms to derive fragment energy.
It is noteworthy that the actual virial ratio of H2CO.wfn is 2.009, which can be found at the end of this file and also printed after Multiwfn loading this file. Since its deviation to exact virial
ratio 2.0 is insignificant, our scaling treatment of E is reasonable and acceptable.
An evidently more convenient and better way of deriving atomic contribution to energy is choosing user-defined function -11 as the integrand, it is scaled electron energy density involving virial ratio, whose integral over the whole space exactly equals the electronic energy given by quantum chemistry code, see corresponding part of Section 2.7 for its definition. Now we redo the example above. Open `settings.ini` and set “iuserfunc” to -11, then boot up Multiwfn and input
examples\H2CO.wfn 17 // Basin analysis 1 // Generate basins 1 // Electron density 2 // Medium-quality grid 7 // Integrate real space functions in AIM basins with mixed type of grids 2 // Exact refinement of basin boundary 100 //User-defined function, which now corresponds to the scaled electron energy density The result is

```text
    Atom       Basin       Integral(a.u.)   Vol(Bohr^3)   Vol(rho>0.001)
     1 (C )       2        -37.32041642       244.279        67.166
     2 (H )       4         -0.60162114       554.745        49.848
     3 (O )       1        -75.97660985       887.040       127.096
     4 (H )       3         -0.60179889       566.901        49.832
```
