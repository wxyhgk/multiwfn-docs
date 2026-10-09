# 2.8 Graphic formats and image size

> Multiwfn manual, p.70–76. Images: `../imgs/`.

---

<!-- p.70 -->


## 2.8 Graphic formats and image size

Multiwfn supports a lot of mainstream graphic formats, including: 1 Postscript (ps) 2 Encapsulated postscript (eps) 3 Portable document format (pdf) 4 Windows metafile format (wmf) 5 Graphics interchange format (gif) 6 TIFF (tiff) 7 Portable network graphics (png) 8 Windows bitmap format (bmp) 9 Scalable vector graphics (svg) The graphic format of the picture exported by Multiwfn is controlled by “graphformat” parameter in `settings.ini`, you can set this parameter to the texts in the parentheses listed above, the default format is “png”.

For curve maps, the height and weight of the image file are controlled by “graph1Dsize” parameter in `settings.ini`. “graph2Dsize” is responsible for two-dimension data plotting (color-filled map, contour map, relief map, etc.). “graph3Dsize“ is responsible for three-dimension data plotting (isosurface graph, molecular structure graph, etc.).

Tip 1: If the graph is mainly composed of lines, e.g. contour line map and curve map, the best formats are pdf and svg. However, if you need to embed the resulting graph to Office, commonly wmf format should be used.

Tip 2: If you want to make background of exported image file transparent, please look this video illustration: https://youtu.be/E7lAGac3aDM.


## 2.9 Analysis of periodic systems

Multiwfn is able to deal with periodic systems, details will be given in this section. To analyze wavefunction for periodic systems, you can use either wavefunction of cluster model produced by quantum chemistry codes, or use periodic wavefunction produced by CP2K program, as will be described in Section 2.9.1 and 2.9.2, respectively. There are many analyses in Multiwfn independent of wavefunction, special attention of applying them to periodic systems will be described in Section 2.9.3.

2.9.1 Wavefunction analysis on wavefunction of cluster model

You can extend primitive cell of the crystal to a large supercell, then extract a cluster from the supercell. Based on this cluster, you can use any quantum chemistry code to carry out optimization or single point task and then analyze the resulting wavefunction as usual in Multiwfn. Of course, to minimize artificial boundary effect due to the finite cluster size, the cluster should be large enough. If you are not sure what the minimum acceptable size is, you can perform a convergence test for the


<!-- p.71 -->

result with respect to cluster size. It is important to recognize that electronic structure of boundary atoms of the cluster should not be included in the discussion since it must be meaningless due to unavoidable boundary effect.

If the crystal structure was determined by X-ray diffraction experiment, you should always perform an optimization for positions of hydrogens, since hydrogens usually cannot be accurately determined by X-ray diffraction.

If the atomic positions were determined experimentally with satisfactory resolution, geometry optimization of heavy atoms (i.e. non-hydrogen atoms) should be ignored. However, if you want to study surface reaction or adsorption, or investigate reaction inside the crystal, you should freeze boundary heavy atoms to mimic bulk circumstance while optimize central region of the cluster to represent the influence on geometry due to the reaction or adsorption.

There are four common kinds of crystals, some comments are given below:

- Molecular crystal: This is the simplest situation. Section 4.12.6 illustrates how to extract a urea cluster from urea crystal, you can follow it to construct other kinds of cluster. A good example of using cluster model to analyze wavefunction of molecular crystal is Fig. 6 of J. Comput. Chem., 33, 580 (2012), in which reduced density gradient analysis was employed for urea cluster based on B3LYP/6-31G** wavefunction. Another example: “Calculate absorption spectrum of a molecule in crystal environment based on background charge” (http://sobereva.com/579).

- Metal crystal: An example of utilizing this model can be found in my blog article: "Calculating adsorption on metal surface by quantum chemistry program based on cluster model" (http://sobereva.com/540). It is not recommended to use cluster model to study d-group and f-group metals, since self-consistent field of the corresponding cluster is very difficult to converge, and it is easy to converge to unstable wavefunction.

- Covalent crystal: Graphene and diamond are typical instances, you should saturate the boundary atoms by hydrogens to avoid dangling bonds, which make electronic structure of the current system highly artificial. Of course, the position of the added hydrogens should be optimized. A good example is Mater. Sci. Eng. B, 273, 115425 (2021) DOI: 10.1016/j.mseb.2021.115425, which studies interaction between cyclo[18]carbon and graphene fragment using Multiwfn.

- Ionic or semi-ionic crystal: NaCl and TiO2 are typical cases. This type of crystal needs special attention to properly account for boundary effect. Usually, the embedded cluster model should be used, as mentioned below. One should first determine a region of suitable size to be treated quantum chemically (known as QM region). The larger the region, often the better the result, but more expensive. Numerous layers of point charges at crystal sites around the QM region should be added as background charges to mimic electrostatic interaction between QM atoms and the environmental atoms. Oxidation states of the environmental atoms may be chosen as the values of the point charges, while there is a better but more complicated way to determine them by means of iteration process, see Inorg. Chem., 58, 9303 (2019). In addition, effective core potentials (ECP, without basis functions) of corresponding elements should be added to a layer of environmental atoms closest to the QM region, they are known as capped ECP (cECP), and this very thin region is recognized as buffer region. Presence of buffer region is needed to avoid electron spill-out from the QM region towards the neighboring positive Coulomb singularities of the point charges, it is of great importance when the QM region is negatively charged. See Inorg. Chem., 58, 9303 (2019) and J. Chem. Theory Comput., 16, 6950 (2020) for details about the aforementioned embedded cluster model, SI in the former paper provides an example ORCA input file. Also see Surface Sci., 471, 21


<!-- p.72 -->

(2001) for another application. Note that another way of avoiding the electron spill-out problem is using Gaussian charge distribution to represent the environmental atoms, this is known as Gaussian expansion of the electrostatic potential (GEEP) and supported by QM/MM treatment of CP2K, see J. Chem. Theory Comput., 1, 1176 (2005).

2.9.2 Wavefunction analysis on periodic wavefunction

To directly use Multiwfn to analyze periodic wavefunctions, you should use the freely available and efficient CP2K code (https://www.cp2k.org) to carry out calculation for periodic systems, details are described as follows. Currently no first-principles code other than CP2K can be supported by Multiwfn. The .fch/fchk file produced by periodic calculation of Gaussian program is also fully supported, however it lacks practical use because the periodic calculation in Gaussian is extremely slow.

2.9.2.1 Generating .molden wavefunction file

Note: For more information and discussion about this topic, see “On the using CP2K to generate wavefunction files in molden format for Multiwfn” (http://sobereva.com/651, in Chinese)

The .molden file exported by CP2K can be used as input file of Multiwfn. In order to generate it, you should add the following content in the $DFT field of input file


```text
    &PRINT
      &MO_MOLDEN
        NDIGITS 9
      &END MO_MOLDEN
    &END PRINT
```

After calculation, you will obtain a .molden file in current folder.

·For users of CP2K ≥ 2026.2 If the system is periodic, also insert WRITE_CELL T into the &MO_MOLDEN field to ask CP2K to write cell information into the .molden file as [Cell] field.

If pseudopotential is used, also insert WRITE_PSEUDO T into the &MO_MOLDEN field to ask CP2K to write actual number of valence electrons of every atom into the .molden file as [Pseudo] field.

·For users of CP2K < 2026.2 You should edit the file to manually add cell information at the beginning of the file, for example


```text
[Molden Format]
[Cell]
7.13358000    0.00000000    0.00000000
0.00000000    7.13358000    0.00000000
0.00000000    0.00000000    7.13358000
 [Atoms] AU
 C        1       4       0.000000       0.000000       0.000000
 C        2       4       1.685064       1.685064       1.685064
 C        3       4       0.000000       3.370128       3.370128
```


<!-- p.73 -->


```text
...ignored
```

The three highlighted rows respectively correspond to the three translation vectors of the cell (also known as cell vectors) in Å. Any type of cell is supported, the cell is not necessarily to be orthogonal.

For convenience, you can also specify the cell information in terms of cell lengths (a, b, c) and

cell angles (α, β, γ). For example, the following content defines a = 15 Å, b = 13 Å, c = 18.5 Å, α = 90°, β = 90°, γ = 121.3°.


```text
[Cell]
15 13 18.5 90 90 121.3
```

In addition, if you do not hope to modify .molden file, you can also provide the cell information (three lines for three cell vectors, or one line for six cell parameters) in a text file named [Cell].txt and put it in current folder. When [Cell] cannot be found from .molden file while [Cell].txt is detected in current folder, Multiwfn will ask you if loading cell information from it.

If you employed pseudopotential, it is suggested to modify the element index of the atoms to actual number of valence electrons, so that appropriate electron density function (EDF) can be automatically employed to represent electron density of inner core electrons when you studying electron density and its derivatives (see Appendix 4 for detail), and Multiwfn can correctly calculate atomic charges, this is why the second term after "C" in the example above has been changed to 4 from the element index (6). If you find it is too troublesome to modify the file for every atom one by one, you can use the [Nval] field to manually specify number of valence electrons for specific elements, for example


```text
...ignored
0.00000000    7.13358000    0.00000000
0.00000000    0.00000000    7.13358000
[Nval]
C 4
O 6
 [Atoms] AU
...ignored
```

An example CP2K input file of generating .molden file for 2×2 supercell of diamond has been provided as examples\PBC\CP2K_diamond_2x2_DZVP-MOLOPT.inp.

2.9.2.2 Functions available for analyzing periodic wavefunction

Currently limited functions in Multiwfn formally support periodic wavefunctions, the following ones have been tested and they are found to work well for periodic systems, other functions may or may not work normally. More functions will formally support periodic wavefunctions in the future.

- Viewing orbitals (main function 0)
- Calculate properties at a point (main function 1)
- Topology analysis (main function 2)
- Plotting curve map for real space functions (main function 3), including promolecular and deformation properties

- Plotting plane map for real space functions (main function 4), including promolecular and


<!-- p.74 -->

deformation properties

- Calculating grid data and plotting isosurface maps for real space functions (main function 5), including promolecular and deformation properties. Note that in the case of nonorthogonal cell, isosurface map cannot be correctly plotted in Multiwfn, however you can export the grid data as cube file and then visualize it in VMD and VESTA

- Atomic charge and population analysis: Hirshfeld, Hirshfeld-I, MBIS, CM5, 1.2*CM5, Mulliken population, Löwdin population, various modified Mulliken populations, PEOE (Gasteiger), EEM, and AIM (via basin analysis module)

- Orbital composition analysis by Mulliken, Stout-Politzer, SCPA and Hirshfeld methods, including showing fragment contributions (subfunctions 1-6 in main function 8)

- LOBA/mLOBA method for calculating oxidation states
- Bond order analysis: Mayer bond order, Wiberg bond order, Mulliken bond order and its decomposition analysis, orbital occupancy-perturbed Mayer bond order, fuzzy bond order

- Electron delocalization and aromaticity analyses: Multi-center bond order, HOMA, HOMAc, HOMER, Bird, AV1245

- Plotting TDOS, PDOS, OPDOS, LDOS, MO-PDOS and COHP (main function 10)
- Charge decomposition analysis (CDA)
- Orbital localization by Pipek-Mezey method with Mulliken or Löwdin population (main function 19)

- Visualization analyses of weak interactions (IGMH, mIGM, amIGM, aIGM, IGM, IRI, NCI, aNCI, DORI).

- Electron excitation analyses: Electron-hole analysis (hole and electron distributions, transition density and transition dipole moment density, various indices that irrelevant to centroids including ghost-hunter index), IFCT analysis, NTO analysis, generate and export transition density matrix, calculate Mulliken atomic transition charges, generate natural orbitals of excited states, "Check, modify and export configuration coefficients of an excitation", print major MO transitions in all excited states, CTS analysis

- Fuzzy atomic space analysis: Performing integration in fuzzy atomic spaces for a real space function, calculating AOM, calculating LI, DI, fragment LI, IFDI, PDI, FLU, FLU-π, CLRK, PLR. Hirshfeld, Hirshfeld-I and MBIS partitions are supported.

- Others: Integrate a function in whole space; biorthogonalization; NAdO and BOD Analysis of electrostatic potential (ESP) has not been supported yet! Because Multiwfn is unable to directly calculate ESP based on wavefunction information.

2.9.2.3 Related parameters for analyzing periodic wavefunctions

There are some parameters in `settings.ini` that related to analysis of periodic wavefunctions and structures, as shown below. Notice that for non-orthogonal cells, the X, Y, Z mentioned above in fact refer to the first, second, third dimensions, respectively.

- ifdoPBCxyz: Its three values control if considering periodicity in X, Y and Z respectively when cell information is provided in input file. For example, if "ifdoPBCxyz" is set to be 1,1,0, then periodicity in Z will be fully ignored.

- PBCnxnynz: Its three values control how many neighbouring mirrors are considered in X, Y and Z respectively. For example, if "PBCnxnynz" is set to be 1,1,1, then the +1 and -1 neighbouring mirror cells in all directions with respect to the current cell will be considered during calculation. The "current cell" denotes the cell in which the position or atom to be considered resides. The default


<!-- p.75 -->

1,1,1 is commonly suitable and should not be changed without special reason. In principle, increasing the values will make the result more accurate but significantly increase costs.

- expcutoff_PBC: In order to reduce cost of evaluation of exponential term during calculating real space functions, if x of exp(x) is found to be smaller than this parameter, evaluation will be skipped. The default value is a good balance between speed and accuracy. Clearly, increasing this parameter will worsen the result but decrease cost.

Note on studying one- and two- dimension systems: If you want to study a two-dimension system which is parallel to XY plane, it is highly suggested to set the "ifdoPBCxyz" to 1,1,0, then periodicity in Z direction will not be taken into account, the computational cost will also be reduced. Similarly, for a one-dimension system with periodicity of Z direction, it is suggested to set "ifdoPBCxyz" to 0,0,1.

Very important note on CP2K calculation k-point sampling is not considered by Multiwfn, that means only gamma point should be involved in CP2K calculation. So, the size of the cell should be sufficiently large to avoid the need to consider k-point sampling.

If the cell is very small, for example, conventional cell of diamond, whose size is about 3.5 Å, it is best to set the aforementioned "PBCnxnynz" parameter to 2,2,2, otherwise the result will be slightly inaccurate.

If the analysis method you want to employ is incompatible with diffuse functions, such as Mayer bond order and Mulliken population analysis, you should never use a basis set containing basis functions showing strong diffuse character, otherwise the result will be unphysical. According to my test, DZVP-GTH is usually inacceptable, while MOLOPT-SR-GTH series of basis set is a good choice.

2.9.3 Other kinds of analyses on periodic systems

Some functions in Multiwfn are independent of wavefunction, only atom information or grid data is needed, such as independent gradient model (IGM) analysis, reduced density gradient (RDG) analysis under promolecular approximation, Hirshfeld surface analysis, calculation of coordination number. In this case, you can use any first-principles code such as CP2K, Quantum ESPREESO, Abinit and VASP to optimize the crystal or surface, then convert the resulting geometry to any file format supported by Multiwfn (e.g. .xyz, .pdb, .mol2) and then use it as input file.

Currently, only a few of these functions explicitly support taking periodic boundary condition (PBC) into account, as shown below (in other words, other functions will simply treat the current system as an isolated system):

- Visualizing geometry and grid data (main function 0)
- Processing grid data (main function 13), including plotting (local) integral curve
- RDG/NCI analysis based on promolecular density, independent gradient model (IGM), modified IGM (mIGM), averaged IGM (aIGM), averaged mIGM (amIGM)

- van der Waals potential analysis (subfunction 6 of main function 20)
- Analysis of atomic contributions to dispersion energy and dispersion density (Section 3.24.4)
- Evaluate interatomic connectivity and atomic coordination number (subfunction 9 of main


<!-- p.76 -->

function 100)

- Calculating cavity diameter (described in Section 3.100.21)
- Visualizing free regions and calculating free volume for a porous system (subfunction 1 of main function 300)

- Plot molecular surface distance projection map (subfunction 8 of main function 300)
- Domain analysis (subfunction 14 of main function 200)
- Calculating bond length/order alternation (BLA/BOA) (subfunction 9 of main function 200) Note that the "ifdoPBCxyz" parameter mentioned in the last section also affects result of geometry analysis of periodic systems.

2.9.4 Files that can provide cell information to Multiwfn

In order to explicitly consider PBC in the above functions, cell information is needed. The following files can provide cell information to Multiwfn

- .cif file
- .molden file produced by CP2K and modified according to Section 2.9.2
- .mwfn file containing "Ndim" field and Ndim>0
- .pdb and .pqr file containing "CRYST1" field
- .gro file of GROMACS/GROMOS code
- .mol2 file containing "@<TRIPOS>CRYSIN" field
- Gaussian input file containing "Tv" (translation vector) information
- .fch/fchk file produced by Gaussian PBC calculation
- CP2K input file or restart file
- POSCAR, CHGCAR, CHG, ELFCAR, LOCPOT file of VASP program
- .xyz file. The original format does not have a field to record cell information, however you can manually add cell information in the second line of this file to provide cell information to Multiwfn. For example, the following content in second line defines three translation vectors as (7.426 0.0 0.0), (-3.66 6.40 0.0) and (0.0 0.0 10.0) Å:


```text
Tv_1: 7.426 0.0 0.0 Tv_2: -3.66 6.40 0.0 Tv_3: 0.0 0.0 10.0
```

Alternatively, in the second line you can use the same way as extended xyz format (“Lattice” label) to record cell information, for example


```text
Lattice="7.426 0.0 0.0 -3.66 6.40 0.0 0.0 0.0 10.0"
```

- .wfn file. The original format does not have a field to record cell information, however you can manually add cell information like the following one at the end of the file. The field contains three cell vectors and has the same format as the [Cell] field in CP2K file as mentioned above, the unit is Å.


```text
[Cell]
 9.901    0.0     0.0
-4.879   8.534   0.0
 0.0    0.0    10.0
```

If cell information is available, these files exported by subfunction 2 of main function 100 will also carry cell information: .mwfn, .molden, .pdb, .pqr, .xyz, .fch, .gjf, .wfn, CP2K input file.
