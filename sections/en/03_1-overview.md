# 1 Overview

> Multiwfn manual, p.22–30. Images: `../imgs/`.

---

<!-- p.22 -->


## 1  Overview

Multiwfn is a powerful wavefunction analysis program, it supports almost all of the most important wavefunction analysis methods. Multiwfn is free, open-source, high-efficient, very user-friendly and flexible. Multiwfn can be downloaded at Multiwfn official website http://sobereva.com/multiwfn. This code is developed by Tian Lu at Beijing Kein Research Center for Natural Sciences (http://www.keinsci.com).

Input files supported by Multiwfn Multiwfn accepts many kinds of files for loading wavefunction information: .mwfn (Multiwfn wavefunction file), .wfn/.wfx (Conventional / Extended PROAIM wavefunction file), .fch (Gaussian formatted check file), .molden (Molden input file), .31~.40 (NBO plot files) and .gms (GAMESS-US and Firefly output file). Other types such as Gaussian input and output files, .cub, .grd, .pdb, .xyz and .mol files can be used for specific functions.

Briefly speaking, Multiwfn can perform wavefunction analyses based on outputted file of almost all well-known quantum chemistry programs, such as Gaussian, ORCA, GAMESS-US, Molpro, NWChem, Dalton, xtb, PSI4, Molcas, Q-Chem, MRCC, deMon2k, Firefly, CFOUR, Turbomole... Since .molden file exported by CP2K is also supported, Multiwfn is not only able to deal with molecular systems but can also analyze periodic systems (though limited functions can be used, see Section 2.9 of manual for detail).

Special points of Multiwfn (1) Very comprehensive functions. Almost all of the most important wavefunction analysis methods have been well supported by Multiwfn.

(2) Extremely user-friendly. Multiwfn is designed as an interactive program (but can also run silently and be embedded into shell script), prompts shown on screen in each step clearly tell users what should input next. Multiwfn also never prints obscure messages, therefore there is no any barrier even for beginners. In addition, all wavefunction analysis theories are very detailedly documented, and there are more than one hundred well-written examples in the manual; furthermore, there is a "quick start" document that guides new users to master common analyses immediately. Moreover, the developer always very timely and patiently replies all users' questions in Multiwfn official forum.

(3) High flexibility. The design of the overall framework, functions and user interface of Multiwfn is rather flexible, but this does not sacrifice ease of use. Different modules of Multiwfn are organically integrated together to make numerous analyses that single module cannot realize feasible

(4) High efficiency. The code of Multiwfn is substantially optimized. Most parts are parallelized by OpenMP technology. For computationally intensive tasks, the efficiency of Multiwfn exceeds analogous programs significantly.

(5) Results can be visualized directly. A high-level graphical library DISLIN is invoked internally and automatically by Multiwfn for visualizing results, most plotting parameters are controllable in interactive interface. This remarkably simplified wavefunction analysis, especially


<!-- p.23 -->

for studying distribution of real space functions.

Major functions of Multiwfn PS: Despite that there are so many functions in Multiwfn and the manual is quite thick, you can easily learn how to realize the functions listed below by checking the "Multiwfn quick start" document in Multiwfn binary package.

- Showing molecular structure and viewing orbitals (MO, NBO, natural orbital, NTO, LMO, etc.). Speed of generating orbital graph is extremely fast, and the use is very convenient.
- Outputting all supported real space functions as well as gradient and Hessian at a point. Value can be decomposed to orbital contributions.
- Calculating real space function along a line and plot curve map.
- Calculating real space function in a plane and plot plane map. Supported graph types include filled-color map, contour map, relief map (with/without projection), gradient map and vector field map.
- Calculating real space function in a spatial scope, data can be exported to Gaussian-type cube grid file (.cub) and can be visualized as isosurface.
- For the calculation of real space functions in one-, two- and three-dimensions, users can define the operations between the data generated from multiple wavefunction files. Therefore one can calculate and plot such as Fukui function, dual descriptor and density difference very easily. Meanwhile promolecule and deformation properties for all real space functions can be calculated directly.
- Topology analysis for any real space function, such as electron density (AIM analysis), Laplacian, ELF, LOL, electrostatic potential and so on. Critical points (CPs) can be located, topology paths and interbasin surfaces can be generated, and then they can be directly visualized in a 3D GUI window or be plotted in plane map. Value of various real space functions can be calculated at critical points or along topology paths. CP properties can be decomposed as orbital contributions.
- Checking and modifying wavefunction. For example, print orbital and basis function information, manually set orbital occupation number and type, translate and duplicate system, discard wavefunction information from specified atoms.
- Population analysis. Supported methods: ADCH (Atomic dipole moment corrected Hirshfeld), Hirshfeld, Hirshfeld-I, MBIS, cMBIS, EMBIS, AEMBIS, VDD, Mulliken, Löwdin, Modified Mulliken (including three methods: SCPA, Stout & Politzer, Bickelhaupt), Becke, CM5, 1.2*CM5, CHELPG, Merz-Kollmann, RESP, RESP2, AIM (Atoms-in-Molecules) and EEM (Electronegativity Equalization Method). Electrostatic interaction energy of two given fragments can be calculated based on atomic charges.
- Orbital composition analysis. Mulliken, Stout & Politzer, SCPA, Hirshfeld, Hirshfeld-I, Becke, natural atomic orbital (NAO) and AIM methods are supported to obtain orbital composition. Orbital delocalization index (ODI) or spatial delocalization index (SDI) can be calculated to quantify extent of spatial delocalization of orbitals.
- Bond order/strength analysis. Mayer bond order; multi-center bond order (MCBO) and multi-center index (MCI) in AO or natural atomic orbital (NAO) basis (arbitrary number of centers); Wiberg bond order in Löwdin orthogonalized basis; Mulliken bond order; AV1245 index; intrinsic bond strength index (IBSI). Mayer and Mulliken bond order can


<!-- p.24 -->

be decomposed to orbital contributions. Wiberg bond order can be decomposed to contribution from various NAO pair interactions.
- Plotting total, partial, overlap population density-of-states (TDOS, PDOS, OPDOS) and MO-PDOS. Up to 10 fragments can be very flexibly and conveniently defined. Local DOS (LDOS) can also be plotted for a point as curve map or for a line as color-filled map. Furthermore, plotting photoelectron spectrum (PES) based on (generalized) Koopmans' theorem is fully supported, d-band and p-band centers can be calculated. Crystal overlap Hamilton populations (COHP) can also be plotted.
- Plotting various kinds of spectra: IR (infrared), regular/pre-resonance Raman, UV-Vis, directional UV-Vis, ECD (electronic circular dichroism), VCD (vibrational circular dichroism), Raman optical activity (ROA) and NMR. For vibrational spectra, not only harmonic spectrum, but also anharmonic fundamental, overtone and combination bands can be plotted. Spin-orbit coupling effect could be incorporated for electronic spectra. Abundant parameters (broadening function, FWHM, scale factor, etc.) can be customized by users. Maxima and minima of the spectra can be printed and directly labelled on the map. Spikes can be added to bottom of the graph to clearly indicate position and degeneracy of transition levels. Total spectrum can be decomposed to individual contribution of each transition. Spectrum of multiple systems can be conveniently plotted together. Conformational weighted spectrum can be easily plotted. In addition, for vibrational type of spectra, partial vibrational spectrum (PVS) can be plotted to intuitively understand how different atoms or internal coordinates participate in the spectra, and overlap partial vibration spectrum (OPVS) can be plotted to visualize coupling of various terms. Partial vibrational density-of-states (PVDOS) can also be plotted. Color displayed by a chemical substance can be exactly predicted based on its theoretically simulated and experimentally determined UV-Vis spectrum.
- Quantitative analysis of molecular surface. Surface properties such as (total/positive/negative/polar/nonpolar) surface area, enclosed volume, average value and std. of mapped functions can be computed for overall molecular surface or local surfaces; Various kinds of GIPF descriptors and molecular polarity index (MPI) can be evaluated; minima and maxima of mapped functions on the surface can be located; area of

characteristic region corresponding to e.g. σ/π-hole and lone pair can be calculated based on ESP; Basin-like analysis on molecular surface for arbitrary mapped function can be realized.
- Processing grid data (can be loaded from .cub/.grd/.vti/.dx/CHGCAR... or directly generated by Multiwfn). Users can perform very rich mathematical operations on grid data, set value in certain range, extract data in specified plane, plot (local) integral and plane-averaged curve, perform translation, etc.
- Adaptive natural density partitioning (AdNDP) analysis. The interface is interactive and the AdNDP orbitals can be visualized directly. Energy and orbital composition of AdNDP orbitals can be obtained.
- Fuzzy atomic space analysis. Becke, Hirshfeld, Hirshfeld-I, and MBIS atomic space partition methods are supported, the following quantities can be computed: Integral of real space functions in atomic spaces or in overlap region between atomic spaces, dipole and multipole moments of atom/fragment/molecule, atomic multipole moments, atomic


<!-- p.25 -->

overlap matrix (AOM), fragment overlap matrix (FOM), localization and delocalization indices (LI, DI), interfragment DI (IFDI) and fragment LI (FLI), condensed linear response kernel, multi-center DI, as well as five aromaticity indices, namely FLU, FLU-p, PDI, PLR and information-theoretic aromaticity index. Atomic effective volume, free volume, polarizability, and C6 dispersion coefficient can also be calculated according to Tkatchenko-Scheffler method.
- Charge decomposition analysis (CDA) and extended CDA analysis. Orbital interaction diagrams can be plotted. Infinite number of fragments can be defined.
- Basin analysis. Attractors can be located for any real space function, corresponding basins can be generated and visualized at the same time. All real space functions can be integrated in the generated basins. Electric multipole moments, basin/atomic overlap matrix (BOM/AOM), localization index (LI) and delocalization index (DI) can be calculated for the basins. Atomic contribution to basin population can be obtained. Labels of ELF basins can be automatically assigned. High ELF localization domain population and volume (HELP and HELV) can be evaluated.
- Electron excitation analyses: Visualizing and analyzing hole-electron distribution, transition density, transition electric/magnetic dipole moment and charge density difference; Calculating Coulomb attractive energy between hole and electron (exciton binding energy); Calculating Mulliken atomic transition charges and TrEsp (transition charge from electrostatic potential); Decomposing transition electric/magnetic dipole moment to MO pair contribution or basis function/atom contribution; Analyzing charge-transfer by the method proposed in JCTC, 7, 2498; Plotting atom/fragment transition density matrix, transition dipole moment matrix and charge transfer matrix as heat maps;

Calculating Δr index (JCTC, 9, 3118) and Λ index (JCP, 128, 044118) to reveal electron excitation character; Calculating transition electric/magnetic dipole moments between excited states; Generating natural transition orbitals (NTOs); Calculating ghost-hunter index (JCC, 38, 2151); Calculating amount of interfragment charge transfer via IFCT; method; Generating natural orbitals for a batch of excited states; Quickly examining major MO transitions in all excited states; Plotting charge-transfer spectrum (Carbon, 187, 78); Electron density polarization analysis based on electron excitations (JPCA, 124, 633); Calculating ECD/CPL dissymmetry factor (g) for chiral systems.
- Orbital localization analysis: Pipek-Mezey (based on Mulliken, Löwdin or Becke population) and Foster-Boys localization methods are supported. Composition, energy and dipole moment of the resulting LMOs can be derived, shape and center of the LMOs can be easily visualized. Furthermore, based on the LMOs, oxidation states can be evaluated via LOBA method (PCCP, 11, 11297) or modified LOBA method.

- Visual study of weak interactions: Interaction region indicator (IRI and IRI-π, Chem.-Methods, 1, 231); RDG/NCI method (JACS, 132, 6498); aNCI method (noncovalent interaction analysis in fluctuating environments, JCTC, 9, 2226); DORI method (JCTC, 10, 3745); independent gradient model (IGM) method (PCCP, 19, 17928); IGM based on Hirshfeld partition of molecular density (IGMH) (JCC, 43, 539); modified IGM (mIGM, Struct. Bond., 190, 297); averaged IGM and averaged mIGM (mIGM and amIGM, Struct. Bond., 190, 297). Individual regions enclosed by isosurface of these real space functions can be integrated for quantitative analysis. Becke and Hirshfeld surface analyses, as well


<!-- p.26 -->

as fingerprint analysis are also supported. van der Waals potential (J. Mol. Model., 26, 315) can be visualized and extrema can be located.
- Conceptual density functional theory (CDFT) analysis: Fukui function and dual descriptor, as well as their condensed form and orbital-weighted variants; Fukui potential and dual descriptor potential; Mulliken electronegativity; hardness; electrophilicity and nucleophilicity indices; electrophilic descriptor; softness; condensed local softness; relative electrophilicity and nucleophilicity; electrophilic and nucleophilic superdelocalizabilities; bond dual descriptor; dual delocalization descriptor, and so on. A specific model is supported to properly treat the situation with (quasi-)degenerate HOMO and LUMO.
- Extended Transition State - Natural Orbitals for Chemical Valence (ETS-NOCV): Arbitrary number of fragments can be defined, both closed-shell and open-shell cases are supported. NOCV eigenvalues, energies and compositions can be obtained, many related functions can be easily visualized as isosurfaces, including NOCV orbital wavefunctions, NOCV pair densities, frozen state orbitals, Pauli deformation density, orbital deformation density and total density difference.
- Energy decomposition analysis: sobEDA and sobEDAw (J. Phys. Chem. A, 127, 7023 (2023)), EDA based on UFF/AMBER/GAFF molecular force fields (EDA-FF); Shubin Liu's energy decomposition (EDA-SBL); Analysis of atomic contribution to dispersion energy and evaluation of dispersion density.
- Electron delocalization and aromaticity analyses: Multi-center bond order (MCBO), AV1245 and AVmin; Iso-chemical shielding surface (ICSS); NICS_ZZ for non-planar or

tilted system; ELF-π and ELF-σ; harmonic oscillator measure of aromaticity (HOMA) and Bird indices; reparameterized HOMA (HOMAc and HOMER indices); Shannon aromaticity index; para-delocalization index (PDI); aromatic fluctuation index (FLU) and

FLU-π; para linear response index (PLR); information-theoretic (ITA) aromaticity index; properties of ring critical point; NICS-1D scan curve map; integral NICS (INICS) and FiPC-NICS indices; NICS-2D scan plane map, and so on.
- (Hyper)polarizability study: Parsing Gaussian output file of "polar" task and calculating many data related to (hyper)polarizability; Calculating quantities related to Hyper-Rayleigh scattering (HRS); plotting (hyper)polarizability density; obtaining atomic contribution to (hyper)polarizability; calculating (hyper)polarizability by means of sum-over-states (SOS) method; two-level and three-level model analyses; unit sphere and vector representation of (hyper)polarizability tensor; calculating atomic polarizabilities in molecules
- Structure and geometry related analyses: Molecular van der Waals (vdW) volume; area of vdW surface of whole system or individual fragments; molecular length/height/weight, vdW diameter and kinetic diameter; cavity volume and diameter; interatomic connectivity and atomic coordination number; average bond length of atomic cluster; bond length alternation (BLA), bond order alternation (BOA) as well as bond angle and dihedral alternations; molecular planarity parameter (MPP) and span of deviation from plane (SDP); visualizing free regions (pores) in a cell and evaluating their volumes; very rich geometry operations; plotting surface distance projection map; minimum/maximum and geometry/mass center distances between two fragments; area and perimeter of a specific


<!-- p.27 -->

ring
- Other functions (incomplete list): Integrating a real space function over the whole space by Becke's multi-center method; evaluating overlap integral between alpha and beta orbitals; evaluating overlap and centroid distance between two orbitals; generating new wavefunction by combining fragment wavefunctions; calculating LOLIPOP index; calculating intermolecular orbital overlap; Yoshizawa's electron transport route analysis; calculating atomic and bond dipole moment in Hilbert space; plotting radial distribution function for real space functions; calculating overlap integral between orbitals in two different wavefunctions; outputting various kinds of integrals between orbitals; evaluating the first and second moments and radius of gyration for a real space function; exporting loaded structure/wavefunction to many popular formats such as .wfn, .wfx, .molden, .fch, NBO .47, .pdb, .xyz and yield input file for a lot of known quantum chemistry codes; calculating bond polarity index (BPI); domain analysis (obtaining properties within isosurfaces defined by a real space function); calculating electron correlation indices;

detecting π orbitals and evaluating orbital π composition; perform biorthogonalization between alpha and beta orbitals to maximally pair them; evaluating core-valence bifurcation (CVB) index; evaluating orbital contributions to density difference (e.g. Fukui function) or other kind of grid data; bond order density (BOD) and natural adaptive orbital (NAdO) analyses; fitting atomic radial density as STOs or GTFs; simulating scanning tunneling microscope (STM) image; evaluating electric dipole/quadrupole/octopole/hexadecapole moments and electronic spatial extent, etc. Real space functions supported by Multiwfn Real space function analysis is one of the most powerful features of Multiwfn, more than 100 real space functions are supported and listed below, detailed descriptions can be found in Section 2.6 and 2.7 of the manual:

- Electron density
- Gradient norm of electron density
- Laplacian of electron density
- Wavefunction value and probability density of an orbital
- Electron spin density
- Hamiltonian kinetic energy density K(r)
- Lagrangian kinetic energy density G(r)
- Electron localization function (ELF) defined by Becke and the one defined by Tsirelson
- Localized orbital locator (LOL) defined by Becke and the one defined by Tsirelson

- Interaction region indicator (IRI) and IRI-π
- δg function defined in Independent Gradient Model (IGM) and IGM based on Hirshfeld partition (IGMH)

- Local information entropy
- Electrostatic potential (ESP), and that from nuclear / electronic / atomic charges
- van der Waals potential
- Reduced density gradient (RDG) with/without promolecular approximation

- sign(λ2)ρ (product of the sign of the second largest eigenvalue of electron density Hessian matrix and electron density) with/without promolecular approximation


<!-- p.28 -->

- Exchange-correlation density, correlation hole and correlation factor
- Average local ionization energy (ALIE) and local electron attachment energy (LEAE)
- Source function
- Electron delocalization range function EDR(r;d) and orbital overlap distance function D(r)
- Others (incomplete list): Potential energy density, electron energy density, orbital-weighted Fukui function and dual descriptor, strong covalent interaction index (SCI), ultrastrong interaction (USI), bonding and noncovalent interaction (BNI), local electron affinity/electronegativity/hardness, ellipticity and stiffness of electron density, eta index, on-top pair density, numerous forms of DFT exchange-correlation potential, numerous forms of DFT kinetic energy density, Weizsäcker potential, Fisher information entropy, Ghosh/Shannon entropy density, integrand of Rényi entropy, shape function, local temperature, bond metallicity, linear response kernel, steric energy/potential/charge, Pauli potential/force/charge, quantum potential/force/charge, PAEM, density overlap regions indicator (DORI), region of slow electrons (RoSE), PS-FID, single exponential decay detector (SEDD), electron linear momentum density, electric/magnetic dipole moment density, local electron correlation function, magnitude of electric field, stress tensor stiffness, stress tensor polarizability, fractional occupation number weighted electron density (FOD), and so on.

Implementing a new real space function into Multiwfn is extremely easy, as illustrated in Section 2.7 of the manual.

Things that Multiwfn can do The analyses that Multiwfn support for different topics are briefly listed below, you can easily find related manual sections by searching "Multiwfn quick start.pdf" document. Do not forget to ask questions in Multiwfn official forum when you are confused!

- Visualizing various kinds of orbitals generated by various programs in various forms
- Characterizing chemical bonds: Various form of AIM analyses; studying real space functions

(ELF, LOL, 2ρ, kinetic/potential energy density, IRI and IRI-π, valence electron density, fragment density difference, deformation density, source function, bond ellipticity, bond degree, eta index, V(r)/G(r), SCI, PAEM, IGM...); various kinds of bond orders analysis (Mayer, Laplacian, Mulliken, Wiberg, Fuzzy and multi-center bond orders, as well as decomposition analysis for Mayer, Mulliken and Wiberg bond orders); intrinsic bond strength index (IBSI); localization/delocalization index; orbital localization analysis; bond order density (BOD) and natural adaptive orbital (NAdO) analyses; various methods of measuring bond polarity and bond dipole moment; charge decomposition analysis (CDA); Extended Transition State - Natural Orbitals for Chemical Valence (ETS-NOCV); overlap population density-of-states (OPDOS); energy decomposition analysis and so on. See Section 4.A.11 of manual for an overview. Variation of various properties of chemical bonds during scan and IRC processes can also be easily studied via shell scripts, see Section 4.A.1 of manual.

- Characterizing electron distribution and variation: Atomic charges (AIM, Mulliken, SCPA, Hirshfeld, Hirshfeld-I, Voronoi, Löwdin, ADCH, CM5, MBIS, EEM, CHELPG, MK, RESP, RESP2...); total and spin population analyses for basis functions/shells/atoms/fragments; atomic electric dipole and multipole moment analysis (can also be visualized in VMD program via a plotting script provided in Multiwfn); plotting / basin analysis / domain analysis for density difference; charge displacement curve


<!-- p.29 -->

- Aromaticity and electron delocalization analyses: See Section 4.A.3 of manual for an overview

- Characterizing intramolecular and intermolecular weak interactions: AIM analysis (bond path visualization and analysis of various properties at bond critical point); visual analyses of weak

interactions (NCI, IGM, IGMH, aIGM, IRI, DORI); atom and atomic pair δg indices based on IGM or IGMH; quantitative molecular surface analysis for electrostatic potential (ESP); plotting ESP in various form; plotting van der Waals potential; energy decomposition analysis based on forcefield (EDA-FF); Hirshfeld/Becke surface analysis; LOLIPOP; mutual penetration distance and penetration volume analysis; atomic charge and multipole moment analysis; charge transfer analysis (density difference map, CDA, variation of population ...); ELF and core-valence bifurcation (CVB) index and so on. See Section 4.A.5 of manual for an overview

- Electron excitation analysis: Analysis of hole and electron (distribution, atom/fragment/orbital contribution, centroid position, displacement and overlap, exciton binding energy); charge transfer analysis (IFCT, density difference...); NTO; overlap and centroid distance between crucial MOs; plotting atom/fragment transition density matrix and charge transfer matrix; ∆r index; decomposition of transition dipole moment to basis function/atom/fragment/MO pair contributions; transition dipole moment between various excited states; transition atomic charge; ghost-hunter index; revealing variation of electronic structure (bonding and population) during excitation; printing major MO transitions in all excited states; plotting charge-transfer spectrum to graphically reveal nature of UV-Vis spectrum, and so on. See Section 4.A.12 of manual for an overview

- Prediction of reactive sites and reactivity analysis: ESP and ALIE analyses on molecular surface; atomic charges; orbital composition analysis for frontier molecular orbitals; population of

π electron; orbital overlap distance function analysis; automatically calculating all quantities defined in the framework of conceptual density functional theory; evaluating contribution of orbitals (MO, NBO, NAO, etc.) to Fukui function. See Section 4.A.4 of manual for an overview

- Prediction properties of molecular condensed phase: Using ESP distribution on vdW surface to empirically predict heat of vaporization, heat of sublimation, density of molecular crystal, boiling point, heat of fusion, surface tension, pKb and so on. Molecular polarity can be quantified. See Section 3.15.1 of manual

- Plotting spectra: IR, Raman, UV-Vis, ECD, VCD, ROA, NMR and photoelectron spectra. In the case of UV-Vis, displayed color can be exactly predicted

- Characterizing geometric structure
- (Hyper)polarizability study
- Electric conduction analysis: TDOS and PDOS; orbital overlap analysis between neighbouring monomers; Yoshizawa's transport route analysis; bond length/order alternation (BLA/BOA)

- Many others: Teaching structure chemistry; simulating scanning tunneling microscope (STM) image; converting file formats containing geometry or wavefunction information; studying electron correlation effect; realizing ELF-tuning and LOL-tuning for DFT functionals; evaluating oxidation state by LOBA or modified LOBA method; studying distribution of real space functions (in terms of radial distribution function, centroid, first and second moments, integral over whole space and

local region...); evaluating σ or π component in molecular orbitals, geometry transformation, and so on


<!-- p.30 -->

Citing Multiwfn If Multiwfn is used in your research, at least the following papers must be cited in the main text, which are original papers of Multiwfn program:

Tian Lu, Feiwu Chen, Multiwfn: A Multifunctional Wavefunction Analyzer, J. Comput. Chem. 33, 580-592 (2012) DOI: 10.1002/jcc.22885 Tian Lu, A comprehensive electron wavefunction analysis toolbox for chemists, Multiwfn, J. Chem. Phys., 161, 082503 (2024) DOI: 10.1063/5.0216272

My other papers should be cited depending on the method and function employed in your work. Please carefully check How to cite Multiwfn.pdf document in the Multiwfn binary package.

Whenever possible, please mention and cite Multiwfn in main text rather than in supplemental information, otherwise not only Multiwfn will be difficult for readers to notice, but also the paper will not be included in citation statistics.

Discussion zones There are two Multiwfn official forums, with different languages. You can discuss anything about Multiwfn and wavefunction analysis in either one. If you encountered problems in using Multiwfn, please do not hesitate to post topic on these forums!

Multiwfn English forum: http://sobereva.com/wfnbbs Multiwfn Chinese forum: http://bbs.keinsci.com/wfn BTW: Multiwfn Youtube channel contains some valuable illustration videos of Multiwfn, it is highly recommended to look at them and subscribe to this channel.
