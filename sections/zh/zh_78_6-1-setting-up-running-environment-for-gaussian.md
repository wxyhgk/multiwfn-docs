# 在Windows下为Gaussian设置运行环境(Setting up running environment for Gaussian in

> Multiwfn manual, p.1152–1154.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.1152 -->




## 6 附录(Appendix)


### 6.1 在Windows下为Gaussian设置运行环境(Setting up running environment for Gaussian in


### Windows)

Multiwfn的某些功能可以直接调用Gaussian（前提是`settings.ini`中的“gaupath”已设为Gaussian可执行文件的实际路径）。为了使Windows版Gaussian在这种情况下能正常运行，你必须定义“GAUSS_EXEDIR”环境变量，否则会出现“No executable for file l1.exe”错误，Gaussian运行将失败，因为Gaussian不知道在哪里找到l1.exe可执行文件。下面是设置该环境变量的步骤。

(1)对于Windows XP用户：进入“控制面板(Control panel)”-“系统属性(System properties)”-“高级(Advanced)”(2)对于Windows 7用户：进入“控制面板(Control panel)”-“系统(System)”-“高级系统设置(Advanced system setting)”-“高级(Advanced)”

(3)对于Windows 10用户：在开始按钮上点击鼠标右键，进入“控制面板(Control panel)”-“系统(System)”-“高级系统设置(Advanced system setting)”-“高级(Advanced)”

之后，点击“环境变量(Environment variables)”按钮，然后点击“新建(New)”按钮（在“用户变量(User variables)”框中），输入GAUSS_EXEDIR作为变量名，输入Gaussian的安装目录作为变量值（例如D:\study\g09w\，假设g09.exe在该文件夹中）。

此外，非常重要的一点是注意，当Multiwfn在Windows环境下调用Gaussian时，Gaussian将在当前文件夹而不是在Gaussian临时路径下搜索Default.Rou。因此，如果Default.Rou中有重要设置，例如默认使用的核心数，你应该将该文件复制到当前文件夹，以使设置在计算过程中生效。


### 6.2 计算实空间函数的例程(The routines for evaluating real space functions)

下面是function.f90文件中的例程。你可以利用它们自己构造新的实空间函数。更多细节请查看相应例程代码中的注释。

实空间函数的计算(Calculation of real space functions)function calcfuncall：在给定点计算任何支持的实空间函数的包装器

function userfunc：用户定义的实空间函数function linintp3d：通过对内存中格点数据的三线性插值得到的函数值function splineintp3D：通过对内存中格点数据的三次B样条插值得到的函数值

function fmo：轨道波函数值


<!-- p.1153 -->



function forbdens：轨道概率密度function fdens：电子密度function fspindens：自旋或Alpha或Beta电子密度function fgrad：密度的梯度（x,y,z分量或其模）或约化密度梯度(RDG)

function flapl：电子密度的Laplacian（xx或yy或zz部分或总量）function Lagkin：Lagrangian动能G(r)或其分量function Hamkin：Hamiltonian动能K(r)或其分量function calcprodens：前分子密度

function signlambda2rho：sign[λ2(r)]ρ(r) subroutine signlambda2rho_RDG：同时计算sign[λ2(r)]ρ(r)和RDG function signlambda2rho_prodens：前分子近似下的sign[λ2(r)]ρ(r) function RDGprodens：前分子近似下的RDG

subroutine signlambda2rho_RDG_prodens：以前分子近似同时计算sign[λ2(r)]ρ(r)和RDG

subroutine IGMprodens：计算通常类型或独立梯度模型(IGM)类型的前分子密度梯度

function ELF_LOL：ELF或LOL或SCI（强共价作用指数）function avglocion：平均局域电离能function loceleaff：局域电子亲和能function edr：电子离域范围EDR(r;d) function edrdmax：轨道重叠距离函数D(r)

function delta_g_IGM：IGM方法中定义的δg(r) function linrespkernel：闭壳层的DFT线性响应核的近似形式function pairfunc：交换相关密度、相关穴和相关因子、同顶对密度

function srcfunc：源函数function infoentro：Shannon信息熵函数或Shannon熵密度function totesp：总ESP function nucesp：来自核或原子电荷的ESP function eleesp：来自电子的ESP function totespskip：不含由iskipnuc参数定义的原子核贡献的ESP subroutine planeesp：计算平面内的ESP subroutine espcub：计算来自电子的ESP格点数据function twoorbnorm：两个轨道模的乘积function beckewei：生成Becke权重函数

function densellip：电子密度的椭率、η指数和刚度function xLSDA：LSDA交换泛函的被积函数function xBecke88：Becke88交换泛函的被积函数function cLYP：LYP相关泛函的被积函数function DFTxcfunc：各种DFT交换相关泛函的被积函数function DFTxcpot：各种DFT交换相关势function weizsacker：Weizsäcker泛函（位阻能）的被积函数function KED：各种电子动能密度

<!-- p.1154 -->



function KEDpot：各种动能泛函的势function stericpot：位阻势，其负值为单电子势function stericcharge：位阻电荷function stericforce：位阻力的大小function paulipot：Pauli势function pauliforce：Pauli力的大小function paulicharge：Pauli电荷function Fisherinfo：Fisher信息密度function calcatmdens：基于内建原子径向密度的Lagrange插值计算的前分子密度

function IRIfunc：相互作用区域指示符(IRI) function PAEM：分子中作用于一个电子的势function SEDD：单指数衰减探测器(SEDD) function DORI：密度重叠区域指示符(DORI) function localcorr：局域电子相关函数function elemomdens：电子线动量密度function magmomdens：磁偶极矩密度function energydens_grdn：能量密度的梯度模function energydens_lapl：能量密度的Laplacian function vdwpotfunc：范德华势及其两个分量function orbwei_Fukui：轨道加权的Fukui函数和对描述符function relShannon：相对Shannon熵密度（信息增益密度）function locHFexc：局域Hartree-Fock交换能function stress_stiffness：应力张量刚度，其逆对应于应力张量极化率

function stress_ellipticity：应力张量椭率subroutine calcGTFval：以数组形式返回所有GTF值subroutine calcbasval：以数组形式返回所有基函数值

实空间函数导数的计算(Calculation of derivatives of real space functions)subroutine gencalchessmat：用于在给定点计算各种实空间函数的值、梯度和Hessian矩阵的通用例程

subroutine orbderv：计算给定点处一系列轨道的波函数值及其导数，直至三阶

subroutine EDFrho：计算EDF对密度及相应导数（直至三阶）的贡献

subroutine calchessmat_dens：计算电子密度及其梯度和Hessian矩阵subroutine rho_tensor：计算电子密度及其梯度、Hessian矩阵和三阶导数张量

subroutine calchessmat_prodens：基于内建原子密度以前分子近似计算电子密度及其梯度和Hessian矩阵

subroutine gendensgradab：同时生成alpha和beta电子的电子密度和梯度模
