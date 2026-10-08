# 3.8 Checking & modifying wavefunction (6)

> Multiwfn manual, p.100–102. Images: `../imgs/`.

---

<!-- p.100 -->

For elements in IV A group, Multiwfn uses sp3 configuration to replace s2p2 ground state by default. This treatment is reasonable, since in most molecules these atoms are in sp3 hybridization. For VI A, VII A and Fe, Co, Ni, Multiwfn equalizes the occupation number of orbitals within the same shell; for example, oxygen has two singly occupied 2p orbitals and one doubly occupied 2p orbitals in ground state, the number of electrons in this shell is 4, so Multiwfn sets the occupation number of all the three orbitals to 4/3. This method works because the shapes of occupied orbitals are always nearly identical, regardless of the original occupation number is one or two. However, the difference between virtual orbital and occupied orbital is remarkable, thus Multiwfn uses another method to sphericalize electron density of elements in III A group, as well as Sc, Ti and V. In this method, the singly occupied orbitals are duplicated and rotated. Taking boron as example, assume that the singly occupied 2p orbital is directing along Z-axis, Multiwfn replicates this orbital twice and turn them toward X-axis and Y-axis respectively, finally the occupation numbers of the three orbitals are set to 1/3. (Users needn’t to check the orientation of singly occupied orbital by themselves). If you hope that Multiwfn sphericalizes atoms in IV A group in such manner instead of using sp3 configuration, set “SpherIVgroup” in `settings.ini` to 1.

Notice that the sphericalization methods used in Multiwfn are closely related to wavefunction type, the methods fail if unrestricted wavefunction is used for main group elements or restricted open-shell wavefunction is used for transition metals. These methods also fail if Hartree-Fock method is used for transition metals, because orbital order produced by HF is different from most DFT cases (the HF’s order is wrong, 4s is higher than 3d).


## 3.8 Checking & modifying wavefunction (6)

This function provides a lot of subfunctions for checking and modifying loaded wavefunction, all subfunctions take effect immediately, so after modification(s) you can print related information via proper subfunction to check if your previous operations are correct. After returning to main menu, all subsequent analyses which make use of wavefunction information will be affected. The title in this interface shows the number of GTFs, orbitals, atoms and alpha/beta/total electrons of present wavefunction.

Once you finish all modifications of wavefunction, you can save current wavefunction to new.wfn in current folder via subfunction 0. If you want to save to other wavefunction format, you should return to main menu first, and then enter subfunction 2 of main function 100, then choose corresponding option to save to an expected format.

Below I briefly introduce each subfunction in this main function. Subfunction -3 and -4: Defining molecular fragment. In -3 you directly define a fragment by inputting atomic indices; while in -4 you should input the indices of the atoms to be excluded, the remaining atoms will constitute the fragment. The GTFs whose centers do not belong to this fragment will be discarded (can be imagined as corresponding GTF coefficients in all orbitals are set to zero). This function affects all the following analyses which make use of GTF information, in particular, the calculations involving real space functions.

When use these two subfunctions? For large molecules, what you are interested in may be only a small region, by discarding atoms in other regions, the calculation speed of time-consuming task


<!-- p.101 -->

such as generating grid data can be increased evidently. Besides, sometimes you only want to obtain real space function contributed by certain atoms, these two functions can fulfill your purpose.

This function can be safely used together with main functions 1~6. For other tasks, DO NOT use this function if you do not understand what you are exactly doing, otherwise you may obtain wrong or meaningless results. Notice that this function is irreversible, the discarded GTFs cannot be recovered, unless you reboot the program and reload the wavefunction file.

Subfunction 0: Save current wavefunction to new.wfn file in current directory. Notice that the orbitals with zero occupation number and the atoms do not have GTFs will be automatically discarded during saving.

Subfunction 1: Print information of all GTFs, including the centers they belong to, GTF types and exponents.

Subfunction 2: Print information of all basis functions, including the shells/centers they attributed to, types, and corresponding GTF index ranges.

Subfunction 3: Print basic information of all orbitals, including energies, occupation numbers, orbital types (Alpha, beta or alpha+beta).

Subfunction 4: Print detail information of an orbital, including the expansion coefficients with respect to GTFs (along with GTF information), note that the coefficients include GTF normalization constants.

Subfunction 5: Print coefficient matrix in basis functions (not the coefficients with respect to GTFs), only available when the input file contains basis function information.

Subfunction 6: Print one-particle density matrix in basis functions, only available when the input file contains basis function information.

Subfunction 7: Print various kinds of integral matrix between basis functions, including overlap integrals, electric/magnetic dipole moment integrals, kinetic energy integrals, velocity integrals, electric quadrupole and octopole integrals. For overlap matrix, eigenvalues are printed together, which are useful for checking linear dependency. Only available when the input file contains basis function information.

Subfunction 11: Exchange centers or types or exponents or orbital expansion coefficients of two GTFs, or exchange all information of two GTFs at once (equivalent to exchanging recording order of two GTFs, thus does not affect any analysis result)

Subfunction 21 to 24: Set center, type, exponent and expansion coefficient of a specific GTF in an orbital, respectively.

Subfunction 25: Set expansion coefficients of some GTFs in some orbitals to a specific value. The GTFs simultaneously satisfying the three inputted conditions will be selected: Index range of GTFs, index range of the atoms that GTFs centered at, GTF types (input specific type, such as YZ, XXZ, etc., or input angular moment, such as S, P, D, etc.).

If the input file also contains basis function information, by this option you can also set expansion coefficients of basis functions.

Subfunction 26: Set occupation number of some orbitals. You can directly set them to a specific value, or add, minus, multiply, divide them by a given value. This function is very useful for shielding the contributions from certain orbitals to real space functions, namely setting their occupation numbers to zero before calculating real space functions.

Subfunction 27: Set orbital type of some orbitals, then wavefunction type will be automatically updated, please check the prompts shown on the screen.


<!-- p.102 -->

Subfunction 28: Set energy of some orbitals. You can directly set them to a specific value, or add, minus, multiply, divide them by a given value. This function is useful when you want to rectify the orbital energies using a given relationship (e.g. J. Am. Chem. Soc., 121, 3414 (1999)) before plotting density-of-states (DOS) map.

Subfunction 29: Input indices of two orbitals, then all of their information (energy, occupation, coefficients) will be exchanged

Subfunction 30: Exchange energies and occupation numbers for all orbitals. This is particularly useful in obtaining EDDB grid data based on EDDB code of D. W. Szczepanik. After loading the .fchk file exported by EDDB code, entering this function, and selecting option 1 (exchange orbital energies in eV with occupation numbers), then occupation numbers will correspond to eigenvalues of Natural Orbital for Bond Delocalization (NOBD). Then if you use main function 5 to calculate grid data of electron density as usual, the resulting grid data will directly correspond to EDDB.

Subfunction 31: Translate the whole wavefunction and all atom coordinates of current system by inputting translation vectors and their units.

Subfunction 32: Translate and duplicate the whole wavefunction and all atom coordinates of current system, users need to input translation vectors, their units and how many times the system will be translated and duplicated according to the translation vectors. This function is useful for extending the primitive cell wavefunction outputted by Gaussian PBC function to supercell wavefunction, of course you can calculate supercell wavefunction directly by Gaussian, but much more computational time will be consumed. Notice that constructing wavefunction of a supercell by this way is only an approximation, because the mix between orbitals of neighbouring primitive cells to new supercell orbitals is completely ignored.

Subfunction 33: Rotate wavefunction, namely X→Y, Y→Z, Z→X Subfunction 34: Set occupation number of all inner molecular orbitals in present system to zero, namely only contribution from valence orbitals will be reserved for subsequent studies. The number of inner MOs is automatically determined, however, the atoms using pseudopotential are not taken into account.

Subfunction 35: This function is very useful if you want to discard contribution of orbitals with certain irreducible representation (IRREP) in all kinds of analyses. After you enter this subfunction, IRREP of all occupied orbitals will be shown, the "N_orb" denotes the number of occupied orbitals belonging to the corresponding IRREP. If you want to discard contribution of some IRREPs in the succeeding analyses, you can select option 1 and input the index of the IRREPs, then the occupation number of corresponding orbitals will be set to zero and thus their contributions are eliminated, and you will also see their status are changed from "Normal" to "discarded". Then you can choose option 0 to save wavefunction and quit. You can also choose option 2 to recover the original occupation number of all orbitals, or choose 3 to reverse the status of every IRREP between "Normal" and "Discarded". Note that this subfunction only works for .mwfn, .molden and .gms files, because only these files record orbital IRREPs (beware that the IRREPs in the .molden file produced by many quantum chemistry programs are missing or incorrect). Besides, only restricted and unrestricted SCF wavefunctions are supported.

Subfunction 36: Invert phase of some orbitals (i.e. replacing expansion coefficients of basis functions and GTFs of these orbitals with their negative values).

Subfunction 37: This option converts restricted (R) or restricted open-shell (RO)
