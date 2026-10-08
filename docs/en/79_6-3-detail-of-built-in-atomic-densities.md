# 6.3 Detail of built-in atomic densities

> Multiwfn manual, p.1155–1155. Images: `../imgs/`.

---

<!-- p.1155 -->

subroutine gendens_gradvec_lapl_ab: Generate electron density, gradient vector and Laplacian for alpha and beta electrons at the same time

subroutine calchessmat_lapl: Calculate Laplacian of electron density, its gradient and Hessian matrix (Hessian is currently not available)

subroutine calchessmat_ELF_LOL: Calculate ELF/LOL, its gradient and Hessian matrix (Hessian is currently not available)

subroutine calchessmat_orb: Calculate gradient and Hessian matrix for an orbital wavefunction subroutine calchessmat_rhograd: Calculate gradient and Hessian matrix for gradient norm of electron density

subroutine calchessmat_IRI_RDG: Calculate gradient and Hessian matrix for IRI and RDG subroutine calchessmat_vdWpot: Calculate gradient and Hessian matrix for van der Waals potential

subroutine calchessmat_Shannon: Calculate local information entropy (function 11) or Shannon entropy density (user-defined function 50), its gradient and Hessian matrix

subroutine calchessmat_Fisherinfo: Calculate Fisher information density (user-defined function 51), its gradient and Hessian matrix

subroutine calchessmat_second_Fisherinfo: Calculate second Fisher information density (user-defined function 52), its gradient and (semi-numerical) Hessian matrix

subroutine calchessmat_relShannon: Calculate relative Shannon entropy density (user-defined function 49, also known as information gain density), its gradient and Hessian matrix

subroutine stericderv: Calculate the first-order derivative of steric potential subroutine proatmgrad: Calculate electron density and gradient of an atom in free state using built-in density


### 6.3 Detail of built-in atomic densities

Some analyses, such as Hirshfeld/ADCH population analyses and Hirshfeld orbital composition analysis request atomic densities. Though, as shown in Section 3.7.3, the atomic densities can be evaluated based on atomic .wfn files, the process is slightly complicated, namely the element .wfn files needed must be prepared and sphericalized first. In order to simplify these analysis tasks, a set of built-in atomic densities (available from H to Lr) was provided in Multiwfn and one can directly choose to use it.

These built-in atomic densities were evaluated at highly accurate computational level at atom ground-states, and have been sphericalized (density distribution of many atoms in their ground states are not spherically symmetric). Main group elements with index <=18 were calculated at B3LYP/cc-pVQZ level, those >18 were calculated at B3LYP/ANO-RCC level (except for Ca, UGBS is used since the ANO-RCC of Ca in EMSL website is wrong, at least when I constructed the densities). Transition metals were calculated at HF/UGBS level. Lanthanides and Actinides were calculated at B3LYP/SARC-DKH level (except for U and Np, for which ROHF was used instead of B3LYP because DFT cannot reproduce their correct ground state configurations). For all elements heavier than Ar, DKH2 method was employed to take scalar relativistic effect into account. Unless otherwise specified, open-shell systems were treated by unrestricted open-shell formalism.

The atomic densities are recorded as radial points in atmraddens.f90, the second kind of Gauss-
