# 6.1 Setting up running environment for Gaussian in Windows

> Multiwfn manual, p.1152–1154. Images: `../imgs/`.

---

<!-- p.1152 -->


## 6 Appendix


### 6.1 Setting up running environment for Gaussian in Windows



Some functions of Multiwfn can directly invoke Gaussian (the precondition is that "gaupath" in `settings.ini` has been set to actual path of Gaussian executable file). In order to make Windows version of Gaussian run normally in this case, you must define "GAUSS_EXEDIR" environment variable, otherwise error “No executable for file l1.exe” will occur and Gaussian running will fail, because Gaussian does not know where to find the l1.exe executable file. Below are steps for setting up this environment variable.

(1) For Windows XP users: Enter “Control panel”-“System properties”-“Advanced” (2) For Windows 7 users: Enter “Control panel”-“System”-“Advanced system setting”-“Advanced”

(3) For Windows 10 users: Click right mouse button on the start button, enter “Control panel”-“System”-“Advanced system setting”-“Advanced”

After that, click “Environment variables” button, then click “New” button (in “User variables” frame), input GAUSS_EXEDIR as variable name, input installation directory of Gaussian as variable value (e.g. D:\study\g09w\, assuming that g09.exe is in this folder).

In addition, it is very important to note that when Multiwfn invoke Gaussian in Windows environment, Gaussian will search for Default.Rou in current folder rather than in Gaussian scratch path. Therefore, if there are important settings in Default.Rou, such as the default number of cores to be utilized, you should copy this file to current folder to make the settings take effect during calculations.


### 6.2 The routines for evaluating real space functions

Below are the routines in function.f90 file. You can make use of them to construct new real space functions yourself. For more details, please check the comments in the code of corresponding routine.

Calculation of real space functions function calcfuncall: A wrapper for calculating any supported real space function at a given point

function userfunc: User-defined real space function function linintp3d: Function value obtained by trilinear interpolation from grid data in memory function splineintp3D: Function value obtained by cubic B-spline interpolation from grid data in memory

function fmo: Orbital wavefunction value


<!-- p.1153 -->

function forbdens: Orbital probability density function fdens: Electron density function fspindens: Spin or Alpha or Beta electron density function fgrad: Gradient (x,y,z components or its norm) of density, or reduced density gradient (RDG)

function flapl: Laplacian of electron density (xx or yy or zz part or total) function Lagkin: Lagrangian kinetic G(r), or its components function Hamkin: Hamiltonian kinetic K(r), or its components function calcprodens: Promolecular density

function signlambda2rho: sign[λ2(r)]ρ(r) subroutine signlambda2rho_RDG: Calculate sign[λ2(r)]ρ(r) and RDG at the same time function signlambda2rho_prodens: sign[λ2(r)]ρ(r) with promolecular approximation function RDGprodens: RDG with promolecular approximation

subroutine signlambda2rho_RDG_prodens: Calculate sign[λ2(r)]ρ(r) and RDG at the same time with promolecular approximation

subroutine IGMprodens: Calculate promolecular density gradient of usual type or Independent Gradient Model (IGM) type

function ELF_LOL: ELF or LOL or SCI (strong covalent interaction index) function avglocion: Average local ionization energy function loceleaff: Local electron affinity function edr: Electron delocalization range EDR(r;d) function edrdmax: Orbital overlap distance function D(r)

function delta_g_IGM: δg(r) defined in IGM method function linrespkernel: Approximate form of DFT linear response kernel for closed-shell function pairfunc: Exchange-correlation density, correlation hole and correlation factor, on-top pair density

function srcfunc: Source function function infoentro: Shannon information entropy function or Shannon entropy density function totesp: Total ESP function nucesp: ESP from nuclear or atomic charges function eleesp: ESP from electrons function totespskip: ESP without contribution of nucleus defined by iskipnuc parameter subroutine planeesp: Calculate ESP in a plane subroutine espcub: Calculate grid data of ESP from electrons function twoorbnorm: Product of norm of two orbitals function beckewei: Generate Becke weighting function

function densellip: Ellipticity of electron density, η index, and stiffness function xLSDA: Integrand of LSDA exchange functional function xBecke88: Integrand of Becke88 exchange functional function cLYP: Integrand of LYP correlation functional function DFTxcfunc: Various kinds of integrand of DFT exchange-correlation functionals function DFTxcpot: Various kinds of DFT exchange-correlation potentials function weizsacker: Integrand of Weizsäcker functional (steric energy) function KED: Various kinds of kinetic energy density of electrons


<!-- p.1154 -->

function KEDpot: Potential of various kinds of kinetic energy functionals function stericpot: Steric potential, which negative value is one-electron potential function stericcharge: Steric charge function stericforce: Magnitude of steric force function paulipot: Pauli potential function pauliforce: Magnitude of Pauli force function paulicharge: Pauli charge function Fisherinfo: Fisher information density function calcatmdens: Promolecular density calculated based on Lagrange interpolation of built-in atomic radial density

function IRIfunc: Interaction region indicator (IRI) function PAEM: Potential acting on one electron in a molecule function SEDD: Single exponential decay detector (SEDD) function DORI: Density Overlap Regions Indicator (DORI) function localcorr: Local electron correlation function function elemomdens: Electron linear momentum density function magmomdens: Magnetic dipole moment density function energydens_grdn: Gradient norm of energy density function energydens_lapl: Laplacian of energy density function vdwpotfunc: Van der Waals potential and its two components function orbwei_Fukui: Orbital-weighted Fukui function and dual descriptor function relShannon: Relative Shannon entropy density (information gain density) function locHFexc: Local Hartree-Fock exchange energy function stress_stiffness: Stress tensor stiffness, its inversion corresponds to stress tensor polarizability

function stress_ellipticity: Stress tensor ellipticity subroutine calcGTFval: Return all GTF values as an array subroutine calcbasval: Return all basis function values as an array

Calculation of derivatives of real space functions subroutine gencalchessmat: A general routine used to calculate value, gradient and Hessian matrix at a given point for various real space functions

subroutine orbderv: Calculate wavefunction value of a range of orbitals and their derivatives at given point, up to third-order

subroutine EDFrho: Calculate contribution from EDFs to density and corresponding derivatives (up to third-order)

subroutine calchessmat_dens: Calculate electron density, its gradient and Hessian matrix subroutine rho_tensor: Calculate electron density, its gradient, Hessian matrix and 3rd derivative tensor

subroutine calchessmat_prodens: Calculate electron density, its gradient and Hessian matrix with promolecular approximation based on built-in atomic densities

subroutine gendensgradab: Generate electron density and gradient norm for alpha and beta electrons at the same time
