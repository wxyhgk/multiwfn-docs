# **1. 概述 (Overview)**

Multiwfn 是一个强大的波函数分析 (wavefunction analysis) 程序，支持几乎所有最重要的波函数分析方法。Multiwfn 免费、开源、高效、非常用户友好且灵活。Multiwfn 可在 Multiwfn 官方网站 <http://sobereva.com/multiwfn> 下载。本程序由北京 Kein 自然科学研究中心 (Beijing Kein Research Center for Natural Sciences) (<http://www.keinsci.com>) 的 [Tian Lu](http://sobereva.com/Tian_Lu.html) 开发。

## **Multiwfn 支持的输入文件 (Input files supported by Multiwfn)**

Multiwfn 接受多种文件来载入波函数信息：[.mwfn](https://doi.org/10.26434/chemrxiv.11872524)（Multiwfn 波函数文件）、.wfn/.wfx（传统/扩展 PROAIM 波函数文件）、.fch（Gaussian 格式化检查文件）、.molden（Molden 输入文件）、.31\~.40（NBO 绘图文件）和 .gms（GAMESS-US 与 Firefly 输出文件）。其它类型如 Gaussian 输入与输出文件、.cub、.grd、.pdb、.xyz 和 .mol 文件可用于特定功能。

简而言之，Multiwfn 可以基于几乎所有著名量子化学程序的输出文件做波函数分析，如 Gaussian、ORCA、GAMESS-US、Molpro、NWChem、Dalton、xtb、PSI4、Molcas、Q-Chem、MRCC、deMon2k、Firefly、CFOUR、Turbomole……由于也支持 CP2K 导出的 .molden 文件，Multiwfn 不仅能处理分子体系，也能分析周期性体系（尽管可用功能有限，细节见手册第 [2.9](sec-2-9-analysis-of-periodic-systems.md) 节）。

## **Multiwfn 的特点 (Special points of Multiwfn)**

- (1) 功能非常全面。几乎所有最重要的波函数分析方法都已被 Multiwfn 很好地支持。

- (2) 极其用户友好。Multiwfn 被设计为交互式程序（但也可以静默运行并嵌入 shell 脚本），每一步屏幕上显示的提示都清楚地告诉用户接下来该输入什么。Multiwfn 也从不打印晦涩难懂的信息，因此即使初学者也没有任何障碍。此外，所有波函数分析理论都有非常详细的文档，手册中有上百个写得很好的例子；还有一份"快速入门 (quick start)"文档指导新用户立刻掌握常用分析。另外，开发者总是在 Multiwfn 官方论坛上非常及时、耐心地回复用户的所有问题。

- (3) 高度灵活。Multiwfn 的整体框架、功能与用户界面的设计相当灵活，但这并不牺牲易用性。Multiwfn 的不同模块有机地整合在一起，使得单个模块无法实现的大量分析成为可能

- (4) 高效。Multiwfn 的代码经过了实质性优化，大部分使用 OpenMP 技术并行化。对于计算密集型任务，Multiwfn 的效率显著超过同类程序。

- (5) 结果可以直接可视化。高级图形库 DISLIN 被 Multiwfn 在内部自动调用以可视化结果，大多数绘图参数都可以在交互界面中控制。这极大地简化了波函数分析，特别是研究实空间函数分布时。

## **Multiwfn 的主要功能 (Major functions of Multiwfn)**

注：尽管 Multiwfn 有如此多的功能且手册很厚，你只需查看 Multiwfn 二进制包中的 "Multiwfn quick start" 文档，就能轻松学会如何实现下面列出的功能。

- 显示分子结构并查看轨道（MO、NBO、自然轨道、NTO、LMO 等）。生成轨道图的速度极快，使用非常方便。

- 输出某一点处所有支持的实空间函数以及梯度和 Hessian。数值可以分解为轨道贡献。

- 计算沿一条线的实空间函数并绘制曲线图。

- 计算一个平面内的实空间函数并绘制平面图。支持的图形类型包括填充色图、等值线图、浮雕图（带/不带投影）、梯度图和矢量场图。

- 计算空间范围内的实空间函数，数据可以导出为 Gaussian 型立方格点文件 (.cub)，并可视化为等值面。

- 对于一维、二维和三维实空间函数的计算，用户可以定义多个波函数文件产生的数据之间的运算。因此可以非常容易地计算并绘制如 Fukui 函数、dual descriptor 和密度差等。同时所有实空间函数的前分子 (promolecule) 与变形 (deformation) 性质都可以直接计算。

- 对任意实空间函数做拓扑分析 (topology analysis)，如电子密度（AIM 分析）、Laplacian、ELF、LOL、静电势等。可以定位临界点 (critical point, CP)，生成拓扑路径和盆间表面，然后在三维图形界面窗口中直接可视化，或绘制在平面图上。可以在临界点处或沿拓扑路径计算各种实空间函数的值。临界点性质可以分解为轨道贡献。

- 检查并修改波函数。例如打印轨道与基函数信息，手动设置轨道占据数与类型，平移并复制体系，丢弃指定原子的波函数信息。

- 布居分析 (population analysis)。支持的方法：ADCH（原子偶极矩校正的 Hirshfeld）、Hirshfeld、Hirshfeld-I、MBIS、cMBIS、EMBIS、AEMBIS、VDD、Mulliken、Löwdin、修正 Mulliken（包括三种方法：SCPA、Stout & Politzer、Bickelhaupt）、Becke、CM5、1.2\*CM5、CHELPG、Merz-Kollmann、RESP、RESP2、AIM（分子中的原子）与 EEM（电负性均衡方法）。可以基于原子电荷计算两个给定片段之间的静电相互作用能。

- 轨道组成分析。支持 Mulliken、Stout & Politzer、SCPA、Hirshfeld、Hirshfeld-I、Becke、自然原子轨道 (natural atomic orbital, NAO) 与 AIM 方法来获得轨道组成。可以计算轨道离域指数 (orbital delocalization index, ODI) 或空间离域指数 (spatial delocalization index, SDI) 以定量表征轨道的空间离域程度。

- 键级/键强分析。Mayer 键级；AO 或自然原子轨道 (NAO) 基下的多中心键级 (multi-center bond order, MCBO) 与多中心指数 (multi-center index, MCI)（任意中心数）；Löwdin 正交化基下的 Wiberg 键级；Mulliken 键级；AV1245 指数；内禀键强指数 (intrinsic bond strength index, IBSI)。Mayer 与 Mulliken 键级可以分解为轨道贡献。Wiberg 键级可以分解为各种 NAO 对相互作用的贡献。

- 绘制总、部分、重叠布居态密度（TDOS、PDOS、OPDOS）与 MO-PDOS。可以非常灵活方便地定义多达 10 个片段。还可以绘制某一点处的局域态密度 (local DOS, LDOS) 曲线图，或一条线上的色填图。此外，完全支持基于（广义）Koopmans 定理绘制光电子能谱 (photoelectron spectrum, PES)，可以计算 *d* 带与 *p* 带中心。还可以绘制晶体重叠 Hamilton 布居 (crystal overlap Hamilton population, COHP)。

- 绘制各种光谱：红外 (IR)、常规/预共振拉曼、紫外-可见 (UV-Vis)、方向紫外-可见、电子圆二色 (ECD)、振动圆二色 (VCD)、拉曼光学活性 (ROA) 与核磁 (NMR)。对于振动光谱，不仅可以绘制谐性光谱，还可以绘制非谐基频、泛频与合频谱带。电子光谱可以纳入自旋-轨道耦合效应。丰富的参数（展宽函数、半峰宽、校正因子等）可由用户自定义。光谱的极大与极小可以打印并直接标注在图上。可以在图底部加上钉状线以清楚指示跃迁能级的位置与简并度。总光谱可以分解为每个跃迁各自的贡献。多个体系的光谱可以方便地画在一起。构象加权光谱可以轻松绘制。此外，对于振动类光谱，可以绘制部分振动光谱 (partial vibrational spectrum, PVS) 以直观理解不同原子或内坐标如何参与光谱，还可以绘制重叠部分振动光谱 (overlap partial vibration spectrum, OPVS) 以可视化各项的耦合。还可以绘制部分振动仍密度 (partial vibrational density-of-states, PVDOS)。化学物质显示的颜色可以根据其理论模拟与实验测定的紫外-可见光谱被精确预测。

- 分子表面的定量分析。整体分子表面或局域表面的表面性质如（总/正/负/极性/非极性）表面积、包围体积、映射函数的平均值与标准差等可以计算；可以评估各种 GIPF 描述符与分子极性指数 (molecular polarity index, MPI)；可以定位表面上映射函数的极小与极大；可以基于静电势 (ESP) 计算如 σ/π 空穴与孤对电子对应的特征区域面积；可以对任意映射函数实现分子表面上的类盆分析。

- 处理格点数据（可从 .cub/.grd/.vti/.dx/CHGCAR……载入，或由 Multiwfn 直接生成）。用户可以对格点数据做非常丰富的数学运算、设定特定范围内的值、提取指定平面内的数据、绘制（局域）积分与平面平均曲线、做平移等。

- 自适应自然密度划分 (adaptive natural density partitioning, AdNDP) 分析。界面是交互式的，AdNDP 轨道可以直接可视化。可以获得 AdNDP 轨道的能量与轨道组成。

- 模糊原子空间分析。支持 Becke、Hirshfeld、Hirshfeld-I 与 MBIS 原子空间划分方法，可以计算以下量：原子空间内或原子空间重叠区域内实空间函数的积分、原子/片段/分子的偶极与多极矩、原子多极矩、原子重叠矩阵 (atomic overlap matrix, AOM)、片段重叠矩阵 (fragment overlap matrix, FOM)、定域与离域指数 (localization and delocalization indices, LI, DI)、片段间离域指数 (interfragment DI, IFDI) 与片段定域指数 (fragment LI, FLI)、凝聚线性响应核、多中心离域指数，以及五个芳香性指数，即 FLU、FLU-π、PDI、PLR 与信息论芳香性指数。还可以根据 Tkatchenko-Scheffler 方法计算原子有效体积、自由体积、极化率与 C6 色散系数。

- 电荷分解分析 (charge decomposition analysis, CDA) 与扩展 CDA 分析。可以绘制轨道相互作用图。可以定义无限多个片段。

- 盆分析。可以对任意实空间函数定位吸引子，同时生成并可视化相应的盆。所有实空间函数都可以在生成的盆内积分。可以计算盆的电多极矩、盆/原子重叠矩阵 (BOM/AOM)、定域指数 (LI) 与离域指数 (DI)。可以获得原子对盆布居的贡献。ELF 盆的标记可以自动指定。可以评估高 ELF 定域域布居与体积 (HELP 与 HELV)。

- 电子激发分析：可视化并分析空穴-电子分布、跃迁密度、跃迁电/磁偶极矩与电荷密度差；计算空穴与电子之间的库仑吸引能（激子结合能）；计算 Mulliken 原子跃迁电荷与 TrEsp（源于静电势拟合的跃迁电荷）；把跃迁电/磁偶极矩分解为分子轨道对贡献或基函数/原子贡献；用 *JCTC* **7**, 2498 提出的方法分析电荷转移；把原子/片段跃迁密度矩阵、跃迁偶极矩矩阵与电荷转移矩阵绘制为热图；计算 Δ*r* 指数 (*JCTC*, **9**, 3118) 与 Λ 指数 (*JCP*, **128**, 044118) 以揭示电子激发特征；计算激发态之间的跃迁电/磁偶极矩；生成自然跃迁轨道 (natural transition orbital, NTO)；计算 ghost-hunter 指数 (*JCC*, **38**, 2151)；用片段间电荷转移 (IFCT) 方法计算片段间电荷转移量；为一批激发态生成自然轨道；快速查看所有激发态中的主要分子轨道跃迁；绘制电荷转移光谱 (*Carbon*, **187**, 78)；基于电子激发的电子密度极化分析 (*JPCA*, **124**, 633)；计算手性体系的 ECD/CPL 不对称因子 (*g*)。

- 轨道定域化分析：支持 Pipek-Mezey（基于 Mulliken、Löwdin 或 Becke 布居）与 Foster-Boys 定域化方法。可以得到所得定域分子轨道 (LMO) 的组成、能量与偶极矩，定域轨道的形状与中心可以轻松可视化。此外，基于定域轨道可以用 LOBA 方法 (*PCCP*, **11**, 11297) 或修正 LOBA 方法评估氧化态。

- 弱相互作用的可视化研究：相互作用区域指示符（IRI 与 IRI-π，*Chem.-Methods*, **1**, 231）；RDG/NCI 方法 (*JACS*, **132**, 6498)；aNCI 方法（涨落环境中的非共价相互作用分析，*JCTC*, **9**, 2226）；DORI 方法 (*JCTC*, **10**, 3745)；独立梯度模型 (independent gradient model, IGM) 方法 (*PCCP*, **19**, 17928)；基于分子密度的 Hirshfeld 划分的 IGM (IGMH) (*JCC*, **43**, 539)；修正 IGM (mIGM, *Struct. Bond.*, **190**, 297)；平均 IGM 与平均 mIGM (mIGM 与 amIGM, *Struct. Bond.*, **190**, 297)。这些实空间函数的等值面包围的各个区域可以积分以做定量分析。还支持 Becke 与 Hirshfeld 表面分析以及指纹分析。范德华势 (*J. Mol. Model.*, **26**, 315) 可以可视化并定位极值点。

- 概念密度泛函理论 (conceptual density functional theory, CDFT) 分析：Fukui 函数与 dual descriptor 及其凝聚形式与轨道加权变体；Fukui 势与 dual descriptor 势；Mulliken 电负性；硬度；亲电性与亲核性指数；亲电描述符；软度；凝聚局域软度；相对亲电性与亲核性；亲电与亲核超离域性；键 dual descriptor；dual 离域描述符，等等。支持特定模型以恰当处理 HOMO 与 LUMO（准）简并的情形。

- 扩展过渡态-化学价自然轨道 (Extended Transition State - Natural Orbitals for Chemical Valence, ETS-NOCV)：可以定义任意多个片段，闭壳层与开壳层情形都支持。可以获得 NOCV 本征值、能量与组成，许多相关函数可以轻松可视化为等值面，包括 NOCV 轨道波函数、NOCV 对密度、冻结态轨道、Pauli 变形密度、轨道变形密度与总密度差。

- 能量分解分析：sobEDA 与 sobEDAw (*J. Phys. Chem. A*, **127**, 7023 (2023))、基于 UFF/AMBER/GAFF 分子力场的能量分解 (EDA-FF)；Shubin Liu 的能量分解 (EDA-SBL)；原子对色散能贡献的分析与色散密度的评估。

- 电子离域与芳香性分析：多中心键级 (MCBO)、AV1245 与 AVmin；等化学屏蔽表面 (iso-chemical shielding surface, ICSS)；用于非平面或倾斜体系的 NICS_ZZ；ELF-π 与 ELF-σ；芳香性谐振子度量 (harmonic oscillator measure of aromaticity, HOMA) 与 Bird 指数；重参数化 HOMA (HOMAc 与 HOMER 指数)；Shannon 芳香性指数；对位离域指数 (para-delocalization index, PDI)；芳香涨落指数 (aromatic fluctuation index, FLU) 与 FLU-π；对位线性响应指数 (para linear response index, PLR)；信息论 (ITA) 芳香性指数；环临界点的性质；NICS-1D 扫描曲线图；积分 NICS (INICS) 与 FiPC-NICS 指数；NICS-2D 扫描平面图，等等。

- (超)极化率研究：解析 Gaussian "polar" 任务的输出文件并计算许多与(超)极化率相关的数据；计算与超 Rayleigh 散射 (Hyper-Rayleigh scattering, HRS) 相关的量；绘制(超)极化率密度；获得(超)极化率的原子贡献；用态求和 (sum-over-states, SOS) 方法计算(超)极化率；二能级与三能级模型分析；(超)极化率张量的单位球与矢量表示；计算分子中原子的极化率

- 结构与几何相关分析：分子范德华 (vdW) 体积；整个体系或各个片段的范德华表面积；分子长度/高度/重量、范德华直径与动力学直径；空腔体积与直径；原子间连接性与原子配位数；原子团簇的平均键长；键长交替 (bond length alternation, BLA)、键级交替 (bond order alternation, BOA) 以及键角与二面角交替；分子平面性参数 (molecular planarity parameter, MPP) 与偏离平面的跨度 (span of deviation from plane, SDP)；可视化晶胞中的自由区域（孔）并评估其体积；非常丰富的几何操作；绘制表面距离投影图；两个片段之间的最小/最大以及几何/质量中心距离；特定环的面积与周长

- 其它功能（不完全列表）：用 Becke 多中心方法在全空间积分实空间函数；计算 alpha 与 beta 轨道之间的重叠积分；计算两个轨道之间的重叠与质心距离；通过组合片段波函数生成新波函数；计算 LOLIPOP 指数；计算分子间轨道重叠；Yoshizawa 电子传输路径分析；计算 Hilbert 空间中的原子与键偶极矩；为实空间函数绘制径向分布函数；计算两个不同波函数中轨道之间的重叠积分；输出轨道之间各种积分；计算实空间函数的一阶与二阶矩以及回转半径；把载入的结构/波函数导出为许多流行格式如 .wfn、.wfx、.molden、.fch、NBO .47、.pdb、.xyz，并为许多已知量子化学程序生成输入文件；计算键极性指数 (bond polarity index, BPI)；域分析（获得实空间函数定义的等值面内的性质）；计算电子相关指数；识别 π 轨道并评估轨道 π 组成；在 alpha 与 beta 轨道之间做双正交化以最大配对；评估核-价分岔 (core-valence bifurcation, CVB) 指数；评估轨道对密度差（如 Fukui 函数）或其它格点数据的贡献；键级密度 (bond order density, BOD) 与自然自适应轨道 (natural adaptive orbital, NAdO) 分析；把原子径向密度拟合为 STO 或 GTF；模拟扫描隧道显微镜 (STM) 图像；计算电偶极/四极/八极/十六极矩与电子空间范围，等等。

## **Multiwfn 支持的实空间函数 (Real space functions supported by Multiwfn)**

实空间函数分析是 Multiwfn 最强大的功能之一，支持 100 多种实空间函数，下面列出，详细描述见手册第 [2.6](sec-2-6-real-space-functions.md) 和 [2.7](sec-2-7-user-defined-real-space-function.md) 节：

- 电子密度

- 电子密度的梯度模

- 电子密度的 Laplacian

- 轨道的波函数值与概率密度

- 电子自旋密度

- Hamilton 动能密度 *K*(**r**)

- Lagrange 动能密度 *G*(**r**)

- Becke 定义的电子定域化函数 (electron localization function, ELF) 与 Tsirelson 定义的版本

- Becke 定义的定域轨道指示符 (localized orbital locator, LOL) 与 Tsirelson 定义的版本

- 相互作用区域指示符 (interaction region indicator, IRI) 与 IRI-π

- 独立梯度模型 (IGM) 中定义的 *δg* 函数与基于 Hirshfeld 划分的 IGM (IGMH) 中定义的版本

- 局域信息熵

- 静电势 (electrostatic potential, ESP)，以及源于核/电子/原子电荷的版本

- 范德华势

- 约化密度梯度 (reduced density gradient, RDG)，带/不带前分子近似

- *sign*(*λ*₂)*ρ*（电子密度 Hessian 矩阵第二大本征值的符号与电子密度的乘积），带/不带前分子近似

- 交换相关密度、相关穴与相关因子

- 平均局域电离能 (average local ionization energy, ALIE) 与局域电子亲和能 (local electron attachment energy, LEAE)

- 源函数

- 电子离域范围函数 EDR(**r**;d) 与轨道重叠距离函数 *D*(**r**)

- 其它（不完全列表）：势能密度、电子能量密度、轨道加权 Fukui 函数与 dual descriptor、强共价相互作用指数 (SCI)、超强相互作用 (USI)、成键与非共价相互作用 (BNI)、局域电子亲和/电负性/硬度、电子密度的椭率与刚度、eta 指数、on-top 对密度、多种形式的 DFT 交换相关势、多种形式的 DFT 动能密度、Weizsäcker 势、Fisher 信息熵、Ghosh/Shannon 熵密度、Rényi 熵的被积函数、形状函数、局域温度、键金属性、线性响应核、空间位阻能/势/电荷、Pauli 势/力/电荷、量子势/力/电荷、PAEM、密度重叠区域指示符 (DORI)、慢电子区域 (RoSE)、PS-FID、单指数衰减探测器 (SEDD)、电子线动量密度、电/磁偶极矩密度、局域电子相关函数、电场强度、应力张量刚度、应力张量极化率、分数占据数加权电子密度 (FOD)，等等。

在 Multiwfn 中实现新的实空间函数极其容易，如手册第 [2.7](sec-2-7-user-defined-real-space-function.md) 节所示。

## **Multiwfn 能做的事 (Things that Multiwfn can do)**

下面简要列出 Multiwfn 针对不同主题支持的分析，你可以通过搜索 "Multiwfn quick start.pdf" 文档轻松找到相关的手册章节。当你困惑时别忘了在 Multiwfn 官方论坛提问！

- 可视化各种程序产生的各种轨道，形式多样

- 表征化学键：各种形式的 AIM 分析；研究实空间函数（ELF、LOL、∇²*ρ*、动能/势能密度、IRI 与 IRI-π、价电子密度、片段密度差、变形密度、源函数、键椭率、键度、eta 指数、*V***(r**)/*G*(**r**)、SCI、PAEM、IGM……）；各种键级分析（Mayer、Laplacian、Mulliken、Wiberg、Fuzzy 与多中心键级，以及 Mayer、Mulliken 与 Wiberg 键级的分解分析）；内禀键强指数 (IBSI)；定域/离域指数；轨道定域化分析；键级密度 (BOD) 与自然自适应轨道 (NAdO) 分析；测量键极性与键偶极矩的各种方法；电荷分解分析 (CDA)；扩展过渡态-化学价自然轨道 (ETS-NOCV)；重叠布居态密度 (OPDOS)；能量分解分析，等等。概述见手册第 [4.A.11](sec-4-A-special-topics-and-advanced-tutorials.md#4a11-研究化学键的方法概述) 节。用 shell 脚本也可以轻松研究扫描与 IRC 过程中化学键各种性质的变化，见手册第 [4.A.1](sec-4-A-special-topics-and-advanced-tutorials.md#4a1-沿irc路径研究电子结构的变化) 节。

- 表征电子分布与变化：原子电荷（AIM、Mulliken、SCPA、Hirshfeld、Hirshfeld-I、Voronoi、Löwdin、ADCH、CM5、MBIS、EEM、CHELPG、MK、RESP、RESP2……）；基函数/壳层/原子/片段的总与自旋布居分析；原子电偶极与多极矩分析（也可以通过 Multiwfn 提供的绘图脚本在 VMD 程序中可视化）；密度差的绘制/盆分析/域分析；电荷位移曲线

- 芳香性与电子离域分析：概述见手册第 [4.A.3](sec-4-A-special-topics-and-advanced-tutorials.md#4a3-芳香性研究方法概述) 节

- 表征分子内与分子间弱相互作用：AIM 分析（键路径可视化与键临界点处各种性质的分析）；弱相互作用的可视化分析（NCI、IGM、IGMH、aIGM、IRI、DORI）；基于 IGM 或 IGMH 的原子与原子对 *δg* 指数；静电势 (ESP) 的定量分子表面分析；各种形式的 ESP 绘制；范德华势的绘制；基于力场的能量分解分析 (EDA-FF)；Hirshfeld/Becke 表面分析；LOLIPOP；相互穿透距离与穿透体积分析；原子电荷与多极矩分析；电荷转移分析（密度差图、CDA、布居变化……）；ELF 与核-价分岔 (CVB) 指数，等等。概述见手册第 [4.A.5](sec-4-A-special-topics-and-advanced-tutorials.md#4a5-弱相互作用研究方法概述) 节

- 电子激发分析：空穴与电子的分析（分布、原子/片段/轨道贡献、质心位置、位移与重叠、激子结合能）；电荷转移分析（IFCT、密度差……）；NTO；关键分子轨道之间的重叠与质心距离；原子/片段跃迁密度矩阵与电荷转移矩阵的绘制；∆*r* 指数；跃迁偶极矩向基函数/原子/片段/分子轨道对贡献的分解；不同激发态之间的跃迁偶极矩；跃迁原子电荷；ghost-hunter 指数；揭示激发过程中电子结构（成键与布居）的变化；打印所有激发态中的主要分子轨道跃迁；绘制电荷转移光谱以图形化揭示紫外-可见光谱的本质，等等。概述见手册第 [4.A.12](sec-4-A-special-topics-and-advanced-tutorials.md#4a12-电子激发分析方法概述) 节

- 反应位点预测与反应性分析：分子表面上的 ESP 与 ALIE 分析；原子电荷；前线分子轨道的轨道组成分析；π 电子布居；轨道重叠距离函数分析；自动计算概念密度泛函理论框架下定义的所有量；评估轨道（MO、NBO、NAO 等）对 Fukui 函数的贡献。概述见手册第 [4.A.4](sec-4-A-special-topics-and-advanced-tutorials.md#4a4-反应位点预测方法概述) 节

- 分子凝聚相性质的预测：利用范德华表面上的静电势分布经验性预测汽化热、升华热、分子晶体密度、沸点、熔化热、表面张力、p $K_{b}$ 等。分子极性可以定量化。见手册第 [3.15.1](sec-3-15-quantitative-analysis-of-molecular-surface.md#3151-理论) 节

- 绘制光谱：红外、拉曼、紫外-可见、ECD、VCD、ROA、核磁与光电子能谱。对于紫外-可见情形，显示的颜色可以被精确预测

- 表征几何结构

- (超)极化率研究

- 导电分析：TDOS 与 PDOS；相邻单体之间的轨道重叠分析；Yoshizawa 传输路径分析；键长/键级交替 (BLA/BOA)

- 许多其它：讲授结构化学；模拟扫描隧道显微镜 (STM) 图像；转换含几何或波函数信息的文件格式；研究电子相关效应；对 DFT 泛函实现 ELF 调节与 LOL 调节；用 LOBA 或修正 LOBA 方法评估氧化态；研究实空间函数的分布（径向分布函数、质心、一阶与二阶矩、全空间与局域积分……）；评估分子轨道中的 σ 或 π 成分、几何变换，等等

## **引用 Multiwfn (Citing Multiwfn)**

如果你的研究中使用了 Multiwfn，正文中**至少**必须引用以下 Multiwfn 程序的原始论文：

Tian Lu, Feiwu Chen, Multiwfn: A Multifunctional Wavefunction Analyzer, *J. Comput. Chem.* **33**, 580-592 (2012) DOI: [10.1002/jcc.22885](https://doi.org/10.1002/jcc.22885)

Tian Lu, A comprehensive electron wavefunction analysis toolbox for chemists, Multiwfn, *J. Chem. Phys.*, **161**, 082503 (2024) DOI: [10.1063/5.0216272](https://doi.org/10.1063/5.0216272)

根据工作中使用的方法与功能，还应引用我的其它论文。请认真查看 Multiwfn 二进制包中的 *How to cite Multiwfn.pdf* 文档。

请尽可能在正文而不是补充信息中提及并引用 Multiwfn，否则不仅读者难以注意到 Multiwfn，论文也不会被纳入引用统计。

## **讨论区 (Discussion zones)**

有两个 Multiwfn 官方论坛，使用不同语言。你可以在其中任何一个讨论关于 Multiwfn 与波函数分析的一切。如果使用 Multiwfn 时遇到问题，请毫不犹豫地在这些论坛上发帖！

- Multiwfn 英文论坛：<http://sobereva.com/wfnbbs>

- Multiwfn 中文论坛：<http://bbs.keinsci.com/wfn>

顺便说一句：[Multiwfn Youtube 频道](https://www.youtube.com/playlist?list=PLGZRmytlfpyPMknda9_tdJh8HPHjSECsW)中有一些很有价值的 Multiwfn 演示视频，强烈建议观看并订阅该频道。
