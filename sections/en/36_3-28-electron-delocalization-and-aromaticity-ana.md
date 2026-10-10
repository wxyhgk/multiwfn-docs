# 3.28 Electron delocalization and aromaticity analyses (25)

> Multiwfn manual, p.377–383. Images: `../imgs/`.

---

<!-- p.377 -->

Example of using this function to study practical molecules are given in Section 4.24.5.


## 3.28 Electron delocalization and aromaticity analyses (25)

Some aromaticity analysis methods are introduced in following sections, while most electron delocalization and aromaticity analyses in Multiwfn are introduced in other sections, see Section 4.A.3 for an overview.


### 3.28.3 Generate iso-chemical shielding surfaces (ICSS) and related quantities



Theory Nuclear independent chemical shielding (NICS) is commonly studied at some special points (e.g. ring center), and in some papers NICS is investigated by scanning its value in a line (1D) or in a plane (2D). The so-called iso-chemical shielding surface (ICSS) actually is the isosurface of negative of NICS, which clearly exhibits the distribution of NICS in 3D space, and thus presents a very intuitive picture on aromaticity.

Present function is used to generate grid data and visualize isotropic ICSS, anisotropic ICSS, ICSSXX, ICSSYY and ICSSZZ, they essentially correspond to the isosurface of negative of NICS, NICSani, NICSXX, NICSYY and NICSZZ, respectively. By the way, at a given point, NICSani is defined

as ε3 - (ε1 + ε2)/2, where ε denotes the eigenvalue of magnetic shielding tensor ranked from small to large (viz. ε3 is the largest one).

The original paper of ICSS is J. Chem. Soc. Perkin Trans. 2, 2001, 1893. While ICSSani, ICSSXX, ICSSYY and ICSSZZ were proposed by me. If they are utilized in your work, please cite Carbon, 165, 468 (2020), which is one of my works employing ICSSZZ. I believe for planar systems, the component form of ICSS must be more meaningful and useful than ICSS, just like NICSZZ has conspicuous advantage over NICS. ICSSani is useful to reveal the anisotropic character of NICS in different regions.

Usage Multiwfn itself is incapable of calculating magnetic shielding tensors and thus requires Gaussian to do that. The general steps of performing ICSS analysis are shown below

(1) Prepare a Gaussian input file for the system under study, %chk have to be explicitly specified. The geometry should have been optimized. The keywords in this file will be used for preparing Gaussian input file of NMR task. For example, see examples\ICSS\anthracene.gjf.

(2) After booting up Multiwfn, load the .gjf file, then enter subfunction 3 of main function 25. (3) Set up grid by following the prompt. Beware that even using medium-quality grid may be fairly time-consuming. Hence low-quality grid is in general recommended for medium-size systems.

(4) Input n, namely do not skip steps 5. (5) Many input files of Gaussian NMR task are generated in current folder, they are named as NICS0001.gjf, NICS0002.gjf... It is recommended to manually check one of them to ensure the format and keywords are correct.

In these files, each Bq atom corresponds to a grid point. In the NMR task Gaussian will output magnetic


<!-- p.378 -->

shielding tensor at each Bq along with that at each nucleus. By default 8000 atoms (the real ones + Bq) are presented in each input file, but this can be altered via "NICSnptlim" parameter in `settings.ini`. The reason why separate files rather than a single file are generated is because Gaussian cannot run properly if the number of Bq atoms is too large due to over-consume of memory, also there is upper limit on the total number of atoms in each Gaussian run. You can try to set "NICSnptlim" to a larger value if you have large physical memory, this may reduce overall cost of ICSS analysis (however "NICSnptlim" should also not be too large, for example, the total computational cost of "NICSnptlim=10000" is even higher than "NICSnptlim=1000"!).

Note that for G09 D.01 and E.01, due to a bug in memory allocation when using the default Harris initial guess, you should always add "guess=huckel" to route section of template .gjf file, otherwise the NICSnptlim has to be set to a very small value (e.g. 1000) to make Gaussian work; in this case the overall cost of ICSS calculations is often quite high. For other Gaussian versions, this keyword should not be added. If error occurs in Link 401 module when "guess=huckel" is specified, try to use "guess=core" instead. For G16, the guess keyword is not needed.

(6) Run all of the Gaussian input files generated at last step to yield output files. The NICS0001.gjf must be run prior to any other ones. It is best to keep Multiwfn running (If you have terminated it, reboot Multiwfn and repeat steps 2 and 3 with exactly the same setting and input y at step 4).

Hint: You can make use of the script examples\runall.sh (for Linux) or examples\runall.bat (for Windows), which invokes Gaussian to run all .gjf files in current folder to yield output files with the same name but with .out suffix.

(7) Input the path of the folder containing Gaussian output files yielded in the last step. Then Multiwfn will load the magnetic shielding tensors from the NICS0001.out, NICS0002.out ... in this folder.

(8) Select the property you are interested in. (9) Visualize isosurface or export the grid data to cube file by corresponding option. For example, in step 8 you selected "$\mathrm{NICS}(0)_{\mathrm{ZZ}}$ component", then the isosurface and the grid data will correspond to ICSSZZ. You can also select "-1 Load another ICSS form" to study other forms.

Notice that if this is not the first time you analyze your system and you already have Gaussian output files of NMR task of present system in hand, you can start from step 2 and input y in step 4 to bypass steps 5 and 6. In this case, the grid setting selected in step 3 must exactly accord with the that originally used in generating the Gaussian output files of NMR task.

An example is given in Section 4.25.3.

3.28.4 Obtain NICS$\mathrm{NICS}(0)_{\mathrm{ZZ}}$ value for non-planar or tilted system

Introduction Nucleus-independent chemical shift (NICS) is a very popular index used to measure aromaticity. In many papers, such as Org. Lett., 8, 863 (2006), It was shown that NICS(0)$\mathrm{NICS}(0)_{\mathrm{ZZ}}$ or $\mathrm{NICS}(1)_{\mathrm{ZZ}}$ is a better index than the original definition of NICS, which is currently known as NICS(0).

For exactly planar systems, if the system plane is parallel to XY plane, then NICS(0)$\mathrm{NICS}(0)_{\mathrm{ZZ}}$ means the ZZ component of magnetic shielding tensor at ring center. The only difference from $\mathrm{NICS}(1)_{\mathrm{ZZ}}$ to NICS(0)ZZ is that the calculated point is not ring center, but the point above (or below) 1 Å of the plane from ring center. Note that the definition of ring center is highly arbitrary, the original definition uses geometry center, while some people use center of mass, and some researchers recommend using ring critical point (RCP) of AIM theory as ring center, for example WIREs Comput. Mol. Sci., 3, 105 (2013). (Personally, I think using RCP is the best choice)

If the ring of interest is skewed, not exactly planar or tilted, calculation of NICS$\mathrm{NICS}(0)_{\mathrm{ZZ}}$ is difficult,


<!-- p.379 -->

because one cannot directly acquire the component of magnetic shielding tensor perpendicular to the plane from output file of quantum chemistry programs. Moreover, for NICS(1)ZZ, it is difficult to properly set the position to be calculated. Present function is designed to solve these difficulties.

In this function, the component of magnetic shielding tensor perpendicular to a given ring is

calculated as σ⊥=$\sigma_{\perp} = \mathbf{u}^{\mathrm{T}} \boldsymbol{\sigma} \mathbf{u}$σu, where σ is magnetic shielding tensor, u is column unit vector perpendicular to the ring, and uT is transpose of u.

Steps for obtaining NICS(1)ZZ If you want to calculate NICS(1)ZZ for a non-planar system, you should follow below steps: (1) Use Multiwfn to open a file containing atomic coordinates of your system (e.g. .xyz/.pdb/.mol/.wfn/.mwfn/.fch/.molden...)

(2) Determine ring center. You can use topology analysis module (main function 2) to locate RCP, or use subfunction 21 in main function 100 to obtain geometry center or center of mass.

(3) Enter subfunction 4 of main function 25 (namely the present function), input the ring center you just obtained, and input index of a series of atoms to fit the ring plane. Commonly the inputted atoms should be all atoms in the ring of interest. Then the coordinate of the points above and below 1 Å of the ring plane from the ring center will be outputted.

Hint 1: The unit normal vector perpendicular to the ring plane is also outputted by Multiwfn, by which you can easily derive the position used to calculate such as NICS(2), NICS(3.5)...

Hint 2: Step (2) can be skipped if you simply want to use geometry center and all atoms in the ring are selected to fit the plane, because as mentioned in the prompts on screen, if you directly press ENTER button when Multiwfn asks you to input the ring center, then it will be automatically determined as the geometry center of the atoms you selected for fitting the ring plane.

(4) Use any of the two points obtained in last step to calculate magnetic shielding tensor at corresponding position by quantum chemistry program

(5) Input all components of the magnetic shielding tensor in Multiwfn according to the output of your quantum chemistry program. Then the negative value of "The shielding value normal to the plane" outputted by Multiwfn is just NICS(1)ZZ.

Note that if the system is not symmetric with respect to the plane, in fact the NICS(1)ZZ and NICS(-1)ZZ are different. To obtain the NICS(1)ZZ in common sense, you can take their average when appropriate.

Steps for obtaining NICS(0)ZZ For calculating NICS(0)ZZ, the process is simpler: (1) Identical to the step 1 shown above (2) Identical to the step 2 shown above (3) Use the ring center you obtained in step (2) to calculate the magnetic shielding tensor at this position by quantum chemistry program.

(4) Enter subfunction 4 of main function 25, input ring center, and input index of a series of atoms to fit the ring plane. Then input all components of the magnetic shielding tensor according to the output of your quantum chemistry program. Then the negative value of "The shielding value normal to the plane" outputted by Multiwfn is just NICS(0)ZZ.

There is a blog article illustrating this function: “Using Multiwfn to calculate NICS_ZZ of tilted and twisted rings” http://sobereva.com/261 (in Chinese).

Information needed: Atom coordinates


<!-- p.380 -->


### 3.28.6 Calculate HOMA and Bird aromaticity index

HOMA index Harmonic oscillator measure of aromaticity (HOMA) is the most popular geometry-based index for measuring aromaticity. This quantity was originally proposed in Tetrahedron Lett., 13, 3839 (1972), and then the generalized form was given in J. Chem. Inf. Comput. Sci., 33, 70 (1993). The generalized HOMA can be written as (notice that the HOMA formula has been incorrectly cited by numerous papers)

,2ref,HOMA1()i j α= −− i ji RRN

where N is the total number of the atoms considered, j denotes the atom next to atom i, α and RRef are pre-calculated constants given in original paper for each type of atomic pair. If HOMA equals 1, that means length of each bond is identical to optimal value $R_{\mathrm{ref}}$ and thus the ring is fully aromatic. While if HOMA is equal to 0, that means the ring is completely nonaromatic. If HOMA is a significantly negative value, then the ring shows anti-aromaticity characteristic.

The inventor of HOMA develops the HOMA parameters in the following way, see Chem. Inf. Comput. Sci., 33, 70 (1993) for detail


$$\begin{aligned}&R_{ref}=(R_{s}+wR_{d})/(1+w)\\ &\alpha=\frac{2}{(R_{s}-R_{ref})^{2}+(R_{d}-R_{ref})^{2}}\\ \end{aligned}$$

<!-- formula-ocr: formula_p380_284.png 已替换为LaTeX, 原图保留备查 -->

where Rs and Rd are experimental bond lengths of single bond and double bond, respectively. w=kd/ks, where ks and kd are force constants of single and double bonds, respectively. Usually, w is assumed

to be 2.0 (special case also exists, such as w=4.2 for BN bond). For example, the $R_{\mathrm{ref}}$ and α parameters for CO bond were derived based on the experimental lengths of C-O and C=O bonds in formic acid with assumption of w=2.0.

HOMA can be calculated by subfunction 6 in main function 25. When you choose option 0, Multiwfn will prompt you to input the indices of the atoms in the local system, for example, 2,3,4,5,6,7 (assume that there are six atoms in the ring. The input order must be consistent with atom connectivity), then HOMA value and contributions from each atomic pair will be immediately outputted on the screen. For example, thiophene optimized under MP2/6-311+G**, the output is


```text
        Atom pair         Contribution  Bond length(Angstrom)
   1(C )  --    2(C ):      -0.001852        1.382006
   2(C )  --    3(C ):      -0.056708        1.421170
   3(C )  --    4(C ):      -0.001852        1.382006
   4(C )  --    5(S ):      -0.023886        1.712627
   5(S )  --    1(C ):      -0.023886        1.712627
HOMA value is    0.891817
```

Since 0.891817 is close to 1, the HOMA analysis suggests that thiophene has prominent aromaticity.

The source of built-in α and RRef parameters are shown below:
- CC, CN, CO, CP, CS, NN, NO: Chem. Inf. Comput. Sci., 33, 70 (1993)
- BN: Tetrahedron, 54, 14913 (1998)
- BC: Struct. Chem., 23, 595 (2012)


<!-- p.381 -->

The built-in parameters can be modified or supplemented by user via option 1.

Bird index Bird index (Tetrahedron, 41, 1409 (1985)) is another geometry-based quantity aimed at measuring aromaticity, and can be calculated by option 2 of subfunction 6 in main function 25. The formula is

K100[1(/)]IV V=−

where


$$V=\frac{100}{\overline{N}}\sqrt{\frac{\sum_{i}(N_{i.j}-\overline{N})^{2}}{n}}\quad N_{i.j}=\frac{a}{R_{i,j}}-b$$

<!-- formula-ocr: formula_p381_285.png 已替换为LaTeX, 原图保留备查 -->

In the formula, i cycles all of the bonds in the ring, j denotes the atom next to atom i. n is the total number of the bonds considered. N denotes Gordy bond order, $\overline{N}$ is the average value of the N values. Ri,j is bond length. a and b are predefined parameters respectively for each type of bonds. VK is pre-determined reference V, for five and six-membered rings the value is 35 and 33.2, respectively. The more the Bird index close to 100, the stronger the aromaticity is.

Available a and b parameters include C-C, C-N, C-O, C-S, N-O and N-N, they are taken from Tetrahedron, 57, 5715 (2001), the B-N parameter was obtained from Tetrahedron, 54, 14913 (1998). For other type of bonds user should provide corresponding parameter by option 3. By option 4 user can adjust or add VK parameter.

Corresponding example of this function is provided in Section 4.25.6. Information needed: Atom coordinates


### 3.28.7 HOMAc and HOMER

HOMER and HOMAc were proposed in Phys. Chem. Chem. Phys., 25, 16763 (2023) and J.

Org. Chem., 90, 1297 (2025), respectively. They reparameterized $R_{ref}$ and α parameters, and can be used for a ring containing CC, CN, CO, NN bonds.

HOMER is abbreviation of Harmonic Oscillator Model of Excited-state aRomaticity. HOMER aims at characterizing aromaticity at T1 state simply based on optimized geometry, it is found that it has a reasonable correlation with NICS(1)zz index calculated for T1 state; in contrast, HOMA has negligible correlation with NICS(1)zz. Of course, HOMER is unable to characterize T1 aromaticity at Franck-Condon point, because the geometry is the same as S0.

HOMAc aims at improving the ability of HOMA in determining aromaticity for S0 ground state. Indeed, comparisons in original paper showed that it performs better than HOMA. So, using HOMAc instead of HOMA is recommended.

It is noted that HOMAc and HOMER derived the $R_{ref}$ parameters in the way that they are exactly 1.0 for prototypical S0 and T1 aromaticity molecules at corresponding minima, respectively,

while the α parameters of HOMAc and HOMER were further determined in the way that they are very close to -1 for prototypical S0 and T1 antiaromaticity molecules at corresponding minima,


<!-- p.382 -->

respectively. The parameters in HOMAc and HOMER were derived from geometries optimized at the very expensive CASPT2/cc-pVQZ level, however, these indices also work reasonably for DFT optimized structures.

HOMAc and HOMER can be calculated via subfunctions 6a and 6b in main function 25, respectively. The use is completely the same as HOMA.

Information needed: Atom coordinates


### 3.28.13 NICS-1D scan curve map, integral NICS (INICS) and FiPC- NICS



Background It is well known that nucleus-independent chemical shift (NICS) is a very useful quantity to measure aromaticity. Commonly NICS is calculated at ring center or above/below 1 Å of ring center. If NICS is scanned perpendicular to the ring and starts from ring center, evidently much richer information about aromaticity can be obtained.

As proposed in J. Phys. Chem. A, 123, 3922 (2019), integrating the NICS curve is a more reliable way than only studying NICS at specific points in determining aromaticity, this integral is known as INICS index.

The FiPC-NICS aromaticity index was proposed in Inorg. Chem., 53, 3579 (2014). NICS at any point can be regarded as sum of in-plane component NICSin=(NICSXX+NICSYY)/3 and out-of-plane component NICSout=NICSZZ/3. The NICSout value in the aforementioned scanning path where NICSin equals 0 is defined as free of in-plane component NICS (FiPC-NICS). Because NICSin is

contributed heavily by localized electrons corresponding to σ-bond and lone pairs, the FiPC-NICS value, which is the NICS fully free of contamination from in-plane component, is believed to be a more rigorous index than NICS(1)ZZ in characterizing aromaticity. In fact, the popular NICS(1)ZZ is an acceptable approximation of FiPC-NICS, because in this paper it was found that the distance for calculating FiPC-NICS from ring center is not far away from 1 Å. In addition, this paper showed that the characteristics of the curve map of scanning data with NICSin and NICSout as X-axis and Y-axis respectively is also useful in assigning aromaticity and anti-aromaticity.

Usage This function corresponds to subfunction 13 of main function 25. In this function, you can very easily plot a NICS curve map along a specific line and obtain INICS and FiPC-NICS. The following steps are needed:

(1) Boot up Multiwfn and then load a file containing structure information of the system to be

studied (2) Enter subfunction 13 of main function 25 (3) Define a line and number of scanning points distributed evenly on the line (4) Select option 1 to generate input file of Gaussian program. You need to input path of a

Gaussian template file, which should correspond to a standard NMR task, but coordinate part should be replaced with [geometry], see examples\NICS_scan\template_NMR.gjf for example. Then NICS_1D.gjf will be generated in current folder, you can properly modify


<!-- p.383 -->

keywords according to practical situation (5) Run the .gjf file by Gaussian manually (6) Select option 2 and input the path of the output file of Gaussian to load it (7) Select the component of interest. By default, the NICS data extracted by Multiwfn is the

negative value of the component of magnetic shielding tensor projected on the scanning line. You can also choose to extract isotropy, anisotropy, XX/YY/ZZ component, or the component in the direction of a specific vector. (8) In the new interface, you can plot NICS curve map, or save it as an image file, or export

curve data as .txt file. You can also calculate INICS or FiPC-NICS index using corresponding option in this interface (note that FiPC-NICS calculation if available only if the scanning path is parallel to a Cartesian axis). In step (3), The line can be specified via two ways:

- Manually specify coordinate of the two end points.
- Input indices of some atoms, a plane will be fitted for them. Then respectively specify the distance above and below the plane with respect to the geometric center of the atoms. It is noteworthy that if properly set the Gaussian template file, Multiwfn is able to plot NICS

curve contributed by specific molecular orbitals, such as plotting NICSσ,zz and NICSπ,zz curve.

Examples are given in Section 4.25.13.


### 3.28.14 NICS-2D scan plane map

Multiwfn is able to easily plot very nice NICS plane map, the following steps are needed: (1) Boot up Multiwfn and then load a file containing structure information of the system to be

studied (2) Enter subfunction 14 of main function 25 (3) Define plotting plane, the settings are exactly the same as that of main function 4 (4) Select option 1 to generate input file of Gaussian program. You need to input path of a

Gaussian template file, which should correspond to a standard NMR task, but coordinate part should be replaced with [geometry], see examples\NICS_scan\template_NMR.gjf for example. Then NICS_2D.gjf will be generated in current folder, you can properly modify keywords according to practical situation (5) Run the .gjf file by Gaussian manually (6) Select option 2 and input the path of the output file of Gaussian to load it (7) Select the component of NICS of interest (8) The NICS map shows on screen automatically. After closing it, you can adjust plotting

settings in the post-processing menu and the replot. Examples are given in Section 4.25.14.
