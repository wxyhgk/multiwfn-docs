# 内建原子密度的细节(Detail of built-in atomic densities)

> Multiwfn manual, p.1155–1155.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.1155 -->



subroutine gendens_gradvec_lapl_ab：同时生成alpha和beta电子的电子密度、梯度矢量和Laplacian

subroutine calchessmat_lapl：计算电子密度Laplacian及其梯度和Hessian矩阵（目前Hessian不可用）

subroutine calchessmat_ELF_LOL：计算ELF/LOL及其梯度和Hessian矩阵（目前Hessian不可用）

subroutine calchessmat_orb：计算轨道波函数的梯度和Hessian矩阵subroutine calchessmat_rhograd：计算电子密度梯度模的梯度和Hessian矩阵

subroutine calchessmat_IRI_RDG：计算IRI和RDG的梯度和Hessian矩阵subroutine calchessmat_vdWpot：计算范德华势的梯度和Hessian矩阵

subroutine calchessmat_Shannon：计算局域信息熵（功能11）或Shannon熵密度（用户定义函数50）及其梯度和Hessian矩阵

subroutine calchessmat_Fisherinfo：计算Fisher信息密度（用户定义函数51）及其梯度和Hessian矩阵

subroutine calchessmat_second_Fisherinfo：计算第二Fisher信息密度（用户定义函数52）及其梯度和（半数值）Hessian矩阵

subroutine calchessmat_relShannon：计算相对Shannon熵密度（用户定义函数49，也称为信息增益密度）及其梯度和Hessian矩阵

subroutine stericderv：计算位阻势的一阶导数subroutine proatmgrad：使用内建密度计算自由状态下原子的电子密度和梯度


### 6.3 内建原子密度的细节(Detail of built-in atomic densities)

一些分析，如Hirshfeld/ADCH布居分析和Hirshfeld轨道成分分析，需要原子密度。如第3.7.3节(Section 3.7.3)所示，虽然原子密度可以基于原子的.wfn文件求得，但过程稍显复杂，即必须先准备所需的元素.wfn文件并进行球平均。为了简化这些分析任务，Multiwfn提供了一套内建原子密度（从H到Lr均可用），可直接选择使用。

这些内建原子密度是在原子基态下以高精度计算水平求得的，并已进行球平均（许多原子基态的密度分布并非球对称）。序号<=18的主族元素在B3LYP/cc-pVQZ水平下计算，序号>18的在B3LYP/ANO-RCC水平下计算（Ca除外，使用UGBS，因为EMSL网站上的Ca的ANO-RCC是错的，至少在我构建密度时是如此）。过渡金属在HF/UGBS水平下计算。镧系和锕系在B3LYP/SARC-DKH水平下计算（U和Np除外，对它们使用ROHF代替B3LYP，因为DFT无法重现它们正确的基态构型）。对于所有比Ar重的元素，均采用DKH2方法考虑标量相对论效应。除非另有说明，开壳层体系均采用非限制开壳层形式处理。

原子密度在atmraddens.f90中记录为径向点，第二类Gauss-
