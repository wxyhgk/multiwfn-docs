# 3.10 Orbital composition analysis (8)

> Multiwfn manual, p.134–140. Images: `../imgs/`.

---

<!-- p.134 -->


### 3.9.19 Constrained MBIS (cMBIS), elliptical MBIS (EMBIS), asymmetric elliptical MBIS (AEMBIS) (21, 22, 23)



The codes of constrained MBIS (cMBIS), elliptical MBIS (EMBIS), asymmetric elliptical MBIS (AEMBIS) correspond to subfunctions 21, 22 and 23 in main function 7, respectively. They were contributed by Prof. Frank Jensen (frj@chem.au.dk), please contact him for any details about these functions.

cMBIS is described in: J. E. S. Mikkelsen, F. Jensen "Minimal Basis Iterative Stockholder Decomposition with Multipole Constraints", J. Chem. Theory Comput., 21, 1179-1193 (2025)

EMBIS is described in: A. M. H. Nielsen, F. Jensen "Minimal Basis Iterative Stockholder Decomposition with Ellipsoidal Atoms", J. Chem. Theory Comput., 21, 8753-8761 (2025)

The AEMBIS is not published (yet) but corresponds to adding a beta*R term to the sqrt(Rt*alpha*R) in the EMBIS and also optimize the three beta parameters. This can be considered as adding a dipole-like term to the ellipsoidal basin and thus makes the ellipsoid non-centrosymmetric. A possible citation could be: B. L. Wessel, A. M. H. Nielsen, F. Jensen, (unpublished).

The cMBIS and EMBIS codes have the capacity of employing multipole constraint. EMBIS with the constraint is referred to as cEMBIS in the original paper. The constraint code in AEMBIS is just a straight copy of the EMBIS, and thus produces EMBIS results.

In addition to the information loss value, the atomic volumes and the bond-order matrix are also calculated.

In cMBIS code, there is a possibility to calculate Vne and Vee atomic contributions by numerical and double numerical, respectively. Integration of the Vee is numerically (very) intensive. The Vee is only the Coulomb interaction, but it allows an IQA decomposition into atom-atom energy interactions using the MBIS atom definition to give at least a semi-quantitative measure of interaction

There is also an option of plotting the density along directions in these functions. When entering these functions, you will be asked to choose integration grids. 1 (fine) and 2 (ultrafine) are required to get ~10-4 accuracy for the non-spherical decompositions and high-rank multipoles.

Information needed: GTFs, atom coordinates


## 3.10 Orbital composition analysis (8)

Notice that the word “orbital” here is not restricted to molecular orbital, for example, if the input file carries natural bond orbitals (NBO), then what will be analyzed is NBOs. There is an excellent paper comparing various orbital composition analysis approaches, see Acta Chim. Sinica, 69, 2393 (2011) (in Chinese, http://sioc-journal.cn/Jwk_hxxb/CN/abstract/abstract340458.shtml).

No matter which orbital composition analysis method you choose, if you request Multiwfn to


<!-- p.135 -->

print composition of various atoms in an orbital, in the output you can find a value "Orbital delocalization index" (ODI). The lower the value, the stronger the orbital delocalization. When you intend to quantitatively compare extent of spatial delocalization of various orbitals, you will find this index quite useful. This ODI is detailedly described and illustrated in Section 4.8.5.


### 3.10.1 Output basis function, shell and atom composition in a specific orbital by Mulliken, Stout-Politzer and SCPA approaches (1, 2, 3)



Mulliken, SCPA and Stout-Politzer methods support decomposing orbital to basis function, shell and atom compositions. Actually, I have introduced the theories in Sections 3.9.5, 3.9.6 and

3.9.7, Θi,a×100% is just the composition of basis function a in orbital i, if we sum up all the compositions of basis functions that within a shell we will get shell composition, and if we sum up all the compositions of shells that attributed to the same atom, we will get atom composition.

These approaches rely on basis expansion, in current Multiwfn version you must use .mwfn, .fch, .molden or .gms as input file.

When you entered “Orbital composition analysis” submenu from main menu, select which method you want to use for decomposition, and then input the index of orbital, the result will be printed on screen immediately, you can also input -1 to print basic information of all orbitals to find which one you are interested in. By default, only those terms with composition larger than 0.5% will be printed, this threshold can be adjusted by “compthres” in `settings.ini`.

If the basis functions stored in .mwfn/.fch/.molden file are spherical harmonic type, then the label of basis functions printed will look like D+1, F-3 rather than XX, XYY. The labels of spherical harmonic basis functions used in Multiwfn are completely identical to Gaussian program, the conversion relationship is:


```text
D 0=-0.5*XX-0.5*YY+ZZ  Note: This corresponds to dz2
D+1=XZ
D-1=YZ
D+2=√3/2*(XX-YY)  Note: This corresponds to d(x2-y2)
D-2=XY

F 0=-3/2/√5*(XXZ+YYZ)+ZZZ
```

F+1=-√(3/8)*XXX-√(3/40)*XYY+√(6/5)*XZZ

F-1=-√(3/40)*XXY-√(3/8)*YYY+√(6/5)*YZZ


```text
F+2=√3/2*(XXZ-YYZ)
F-2=XYZ
```

F+3=√(5/8)*XXX-3/√8*XYY

F-3=3/√8*XXY-√(5/8)*YYY


```text
G 0=ZZZZ+3/8*(XXXX+YYYY)-3*√(3/35)*(XXZZ+YYZZ-1/4*XXYY)
```

G+1=2*√(5/14)*XZZZ-3/2*√(5/14)*XXXZ-3/2/√14*XYYZ

G-1=2*√(5/14)*YZZZ-3/2*√(5/14)*YYYZ-3/2/√14*XXYZ

G+2=3*√(3/28)*(XXZZ-YYZZ)-√5/4*(XXXX-YYYY)

G-2=3/√7*XYZZ-√(5/28)*(XXXY+XYYY)

G+3=√(5/8)*XXXZ-3/√8*XYYZ


<!-- p.136 -->

G-3=-√(5/8)*YYYZ+3/√8*XXYZ

G+4=√35/8*(XXXX+YYYY)-3/4*√3*XXYY


```text
G-4=√5/2*(XXXY-XYYY)
```

H 0=ZZZZZ-5/√21*(XXZZZ+YYZZZ)+5/8*(XXXXZ+YYYYZ)+√(15/7)/4*XXYYZ

H+1=√(5/3)*XZZZZ-3*√(5/28)*XXXZZ-3/√28*XYYZZ+√15/8*XXXXX+√(5/3)/8*XYYYY+√


```text
(5/7)/4*XXXYY
```

H-1=√(5/3)*YZZZZ-3*√(5/28)*YYYZZ-3/√28*XXYZZ+√15/8*YYYYY+√(5/3)/8*XXXXY+√


```text
(5/7)/4*XXYYY
```

H+2=√5/2*(XXZZZ-YYZZZ)-√(35/3)/4*(XXXXZ-YYYYZ)

H-2=√(5/3)*XYZZZ-√(5/12)*(XXXYZ+XYYYZ)

H+3=√(5/6)*XXXZZ-√(3/2)*XYYZZ-√(35/2)/8*(XXXXX-XYYYY)+√(5/6)/4*XXXYY

H-3=-√(5/6)*YYYZZ+√(3/2)*XXYZZ-√(35/2)/8*(XXXXY-YYYYY)-√(5/6)/4*XXYYY

H+4=√35/8*(XXXXZ+YYYYZ)-3/4*√3*XXYYZ


```text
H-4=√5/2*(XXXYZ-XYYYZ)
```

H+5=3/8*√(7/2)*XXXXX+5/8*√(7/2)*XYYYY-5/4*√(3/2)*XXXYY

H-5=3/8*√(7/2)*YYYYY+5/8*√(7/2)*XXXXY-5/4*√(3/2)*XXYYY

An example is given in Section 4.8.1. Information needed: Basis functions


### 3.10.2 Define fragments 1 and 2 (-1, -2)

Before doing composition analysis for fragments by Mulliken, Stout-Politzer and SCPA approaches, you have to define fragments in advance. If what you are interested in is only composition of one fragment rather than the composition between two fragments (cross term composition), you only need to define fragment 1. The content of the fragment can be chosen to basis functions, shells, atoms or mixture of them, whatever you choose, only the indices of corresponding basis functions are recorded eventually. Notice that the "fragment" I referred to here has no relationship with the "fragment" involved in Section 3.1, the fragment defined here does not disturb wavefunction at all.

All supported commands in the interface of defining fragment are self-explanatory, so I will not reiterate them but only give an examples, that is define fragment as all P-shells of atom 3: First, type command all, information of all basis functions is listed, find out the shells that attributed to center 3 and contain X, Y and Z type of basis functions (viz. PX, PY and PZ). Assume that the indices of such shells are 3, 6 and 7, then input s 3,6,7 to add them into fragment. If you want to verify your operation, input all again and check if asterisks have appeared in the leftmost of corresponding rows, the marked basis functions are those that have been included in the fragment. Finally, input the letter q to save current fragment and return to last menu, the indices of basis functions in the fragment will be printed at the same time.

By default, fragments do not have any content. Each time you enter the fragment definition interface, the status of fragment is identical to that when you leave the interface last time. So, if you have defined the fragment earlier and you want to completely redefine it, do not forget to use “clean”


<!-- p.137 -->

command to empty the fragment first.


### 3.10.3 Output composition of fragment 1 and inter-fragment composition by Mulliken, Stout-Politzer and SCPA approaches (4, 5, 6)



After you define fragment 1, the fragment composition analysis based on Mulliken, Stout-Politzer and SCPA approaches is available. The fragment composition is the sum of all basis function compositions within the fragment, in this function the fragment compositions of all orbitals are printed on screen at the same time. If the analysis method you chose is Mulliken (subfunction 4) or Stout-Politzer (subfunction 5), below component terms are outputted together with total composition:

c^2 term: The sum of square of coefficients of basis functions within fragment 1, namely


$$\sum_{a\in frag1} C_{a,i}^2 \times 100\%$$

<!-- formula-ocr: formula_p137_075.png 已替换为LaTeX, 原图保留备查 -->

Int.cross: The sum of internal cross terms in fragment 1, namely

$$\sum_{a\in frag1} \sum_{b\notin frag1} w_{a,b} 2C_{a,i} C_{b,i} S_{a,b} \times 100\%$$

Ext.cross: Fragment 1 part of the total cross term between fragment 1 and all other atoms,

$$\sum_{a\in frag1} \sum_{b\notin frag1} w_{a,b} 2C_{a,i} C_{b,i} S_{a,b} \times 100\%$$

It is clear that total composition of fragment 1 equals c^2 term + Int.cross + Ext.cross. If fragment 2 is also defined (you must have already defined fragment 1), in subfunction 5 (Mulliken) or subfunction 5 (Stout-Politzer) the cross term between fragment 1 and fragment 2 in

each orbital, namely $\sum_{a\in\mathrm{frag1}}\sum_{b\in\mathrm{frag2}}2C_{a,i}C_{b,i}S_{a,b}\times100\%$ will be outputted too. “Frag1 part” and C C S

“Frag2 part” correspond to the components of cross term attributed to fragment 1 and fragment 2 respectively, for Mulliken analysis the two terms are of course exactly equal due to the “equal partition”.


### 3.10.4 Orbital composition analysis by natural atomic orbital approach (7)



This function is used to calculate orbital composition based on natural atomic orbitals (NAOs). This idea was proposed in my paper Acta Chim. Sinica, 69, 2393 (2011) http://sioc-journal.cn/Jwk_hxxb/CN/abstract/abstract340458.shtml.

Theory The first step of the famous natural bond orbital (NBO) analysis is converting original basis functions to NAOs based on density matrix. Resulting NAOs can be classified into three categories:

- Core-type NAOs, describing inner core densities, their occupation numbers are almost equal to integer

- Valence-type NAOs, describing valence densities, generally they have high occupation


<!-- p.138 -->

numbers

- Rydberg-type NAOs, mainly displaying characteristics of polarization and delocalization of electrons, the occupation numbers of them are very low

Core and valence NAOs are collectively called as minimal set, they have strong physical meaning and have one-to-one correspondence with "actual" atomic orbitals, so they are what we should be most concerned about. Occupied MOs are almost exclusively contributed by minimal set NAOs. Rydberg NAOs do not have clear physical interpretation, their contributions can be ignored in occupied MOs, however they often have great contribution to virtual orbitals.

Since NAOs is an orthonormal set, if we have MO coefficient matrix in NAO basis, we can get contribution from a NAO to specific MO by simply squaring corresponding expansion coefficient and then multiplying it by 100%. Composition of an atom can be calculated as sum of composition of minimal set NAOs in this center.

This orbital composition calculation method based on NAOs has great basis set stability as Hirshfeld approach, it is especially suitable for analyzing composition of occupied orbitals. However, for virtual orbitals, since contribution from Rydberg NAOs is often large, this method no longer works well.

Input file The MO coefficient matrix in NAO basis cannot be generated by Multiwfn itself, you need to provide an output file of NBO program containing this matrix as Multiwfn input file. By default, NBO program does not output this matrix, so you need to manually add NAOMO keyword between \$NBO ... \$END field in NBO input file. The NBO program we referred to here may be stand-alone NBO program (also known as GENNBO), or NBO module embedded in quantum chemistry software, such as L607 in Gaussian.

Options After loading proper input file and entering present function, you will find following options in the interface:

-1 Define fragment: This option is used to define a fragment, which is needed by fragment contribution analysis (option 1). All commands are self-explanatory.

0 Show composition of an orbital: Print contribution from NAOs, shells and atoms to a specific MO. At the meantime, contributions from core, valence and Rydberg type of NAOs are reported respectively.

1 Show fragment contribution to a batch of orbitals: Print contribution from the fragment defined by option -1 to specific orbitals.

2 Select output mode: This option controls which set of terms will be printed by option 0, there are four modes:

(0) Show all terms (1) Show non-Rydberg terms (2) Show the terms whose contributions are larger than specific criterion (3) Show non-Rydberg terms whose contributions are larger than specific criterion (default) 3 Switch spin type: You can find this option if the current system is open shell. You can select the spin of the MOs to be analyzed.

An example is given in Section 4.8.2.


<!-- p.139 -->

Information needed: MO coefficients in NAO basis


### 3.10.5 Calculate atom and fragment contributions by Hirshfeld or Hirshfeld-I method (8,10)



Hirshfeld and Hirshfeld-I weighting function (see Sections 3.9.1 and 3.9.13, respectively) can also be used for decomposing orbital to atom and fragment compositions, the composition of atom

$$\int \varphi_i^2(\mathbf{r}) w_A(\mathbf{r}) \mathrm{d}\mathbf{r} \times 100\%$$

the compositions of the atoms that belong to the fragment. These methods have great basis set stability and are always more reliable and reasonable than Mulliken and MMPA. In fact, the Hirshfeld partition is already good enough, the more sophisticated and computationally demanding Hirshfeld-I partition is not necessary.

If you choose to use Hirshfeld partition, you will be prompted to select the way to generate atomic densities for constructing Hirshfeld weighting function, I strongly suggest using the built-in atomic densities rather than using atomic .wfn files, since the former is much more convenient. If you choose to use Hirshfeld-I partition, regular HI iterations will be performed first to yield converged atomic weighting functions (if you are confused by the operations, please consult the example of computing HI charges in Section 4.7.4 and the implementation details of Hirshfeld-I introduced in Section 3.9.13).

Before calculating orbital composition, data initialization is automatically carried out. Once it is finished, you can input the orbital index that you are interested in. Because numerical quadrature always introduces some errors, so the sum of all atom compositions is not exactly equal to 100%, the deviation might be relatively significant in rare cases, so Multiwfn normalizes results automatically and prints them under the title “After normalization”.

If you want to view composition of an atom in specific range of orbitals at the same time, choose option -2, then input the atom index and the index range of orbitals.

If you wish to study contribution of a fragment to orbitals, use -9 to define a fragment first, then when you input an orbital index, the contribution of the fragment will be outputted along with the contributions of all atoms. Also, you can choose -3 to calculate the contribution from the fragment you defined to a range of orbitals.

If selecting option -4, program will calculate composition of every atom in every orbital and then export all of them to orbcomp.txt in current folder.

An example is given in Section 4.8.3. Information needed: Atom coordinates and GTFs


### 3.10.6 Calculate atom and fragment contributions by Becke method (9)

This function is very similar to the function introduced in Section 3.10.5, the only difference is that Becke partition is used instead of Hirshfeld partition. For most cases, their results are in qualitative agreement with each other. Using Becke partition instead of Hirshfeld partition has a prominent advantage, namely the atomic wavefunction files are not needed, since the Becke atomic


<!-- p.140 -->

space can be simply constructed based on atomic radius. For more details about Becke partition, see Section 3.18.0. An example is given in Section 4.8.3.

Information needed: Atom coordinates and GTFs


### 3.10.7 Calculate atom and fragment contributions by AIM method (11)

Multiwfn is also able to compute orbital composition based on atoms-in-molecules (AIM) partition of molecular space. In this partition method, each atomic basin corresponds to space of an atom, see Section 3.20 on detail about the concept of basin and AIM partition. To calculate orbital composition under AIM partition, you should use subfunction 11 of basin analysis module (main function 17), see Section 4.8.6 for example.

Usually, I do not recommend calculating orbital composition in this way, because the cost is significantly higher than other ways while the result is not better.

Information needed: Atom coordinates and GTFs


### 3.10.100 Evaluate oxidation state by LOBA and mLOBA method (100)

This function is an implementation of the localized orbital bonding analysis (LOBA) method proposed in Phys. Chem. Chem. Phys., 11, 11297 (2009), and the modified LOBA (mLOBA) proposed by me (to be published).

Theory LOBA is a method used to evaluate atomic oxidation state based on orbital composition of localized MOs (LMOs). The idea is very simple: if an atom has nuclear charge of Z, and its compositions in N occupied LMOs are larger than a given threshold (e.g. 50%. In this case the electrons in these LMOs can be approximately viewed as completely attributed to the atom. If a LMO is doubly occupied, it should be counted twice), then the oxidation state of the atom will be

Z−N.

The idea of LOBA can also be extended to define oxidation state of a fragment, namely if the sum of nuclear charge in a fragment is Z, and the fragment contribution to N LMOs are larger than

a certain threshold, then the fragment oxidation state will be Z−N.

mLOBA employs a different way of determining attribution of electrons of LMOs. In this method, electrons in each LMO are assigned to the atom with maximal contribution to it. This not only removes the arbitrariness of the choice of the threshold, but also guarantees that sum of oxidation states exactly equal to net charge of present system. In addition, oxidation state of a fragment in mLOBA is simply the sum of oxidation states of all its constituent atoms. I strongly suggest using mLOBA instead of LOBA!

The only shortcoming of mLOBA is that when there is (local) geometric symmetry, the result may be unbalanced. For example, in ethane there is an LMO corresponding to the C-C bond, the two carbon atoms contribute equally to it. In mLOBA, the two electrons in LOBA may be assigned to either one of the two carbons, and finally, one carbon has oxidation state of -4 and another one has oxidation state of -2. The best way of circumventing this issue is defining the two carbons as a
