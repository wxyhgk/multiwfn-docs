# 1 总览

> Multiwfn manual, p.22–30.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.22 -->



## 1 总览（Overview）

Multiwfn 是一款强大的波函数分析程序，支持几乎所有最重要的波函数分析方法。Multiwfn 免费、开源、高效、非常易用且灵活。Multiwfn 可在其官方网站 http://sobereva.com/multiwfn 下载。本程序由 Beijing Kein Research Center for Natural Sciences（http://www.keinsci.com）的 Tian Lu 开发。

Multiwfn 支持的输入文件 Multiwfn 接受多种文件以载入波函数信息：.mwfn（Multiwfn 波函数文件）、.wfn/.wfx（传统/扩展 PROAIM 波函数文件）、.fch（Gaussian 格式化检查点文件）、.molden（Molden 输入文件）、.31~.40（NBO 绘图文件）和 .gms（GAMESS-US 和 Firefly 输出文件）。其他类型如 Gaussian 输入和输出文件、.cub、.grd、.pdb、.xyz 和 .mol 文件可用于特定功能。

简而言之，Multiwfn 可以基于几乎所有著名量子化学程序输出的文件进行波函数分析，如 Gaussian、ORCA、GAMESS-US、Molpro、NWChem、Dalton、xtb、PSI4、Molcas、Q-Chem、MRCC、deMon2k、Firefly、CFOUR、Turbomole……由于还支持 CP2K 导出的 .molden 文件，Multiwfn 不仅能处理分子体系，也能分析周期性体系（尽管可用功能有限，详见手册2.9节）。

Multiwfn 的特点 (1) 功能非常全面。几乎所有最重要的波函数分析方法都已在 Multiwfn 中得到良好支持。

(2) 极其易用。Multiwfn 被设计为交互式程序（但也可以静默运行并嵌入 shell 脚本），每一步屏幕上显示的提示都清楚地告诉用户下一步该输入什么。Multiwfn 也从不输出晦涩难懂的信息，因此即使是初学者也没有任何障碍。此外，所有波函数分析理论都有非常详细的文档，手册中有上百个写得很好的例子；还有一份“quick start”文档指导新用户迅速掌握常用分析。另外，开发者在 Multiwfn 官方论坛上总是非常及时、耐心地回复所有用户的问题。

(3) 高度灵活。Multiwfn 的总体框架、功能和用户界面的设计相当灵活，但这并不牺牲易用性。Multiwfn 的不同模块有机地结合在一起，使单个模块无法实现的大量分析成为可能

(4) 高效。Multiwfn 的代码经过了大幅优化。大部分用 OpenMP 技术并行。对于计算密集型任务，Multiwfn 的效率明显超过同类程序。

(5) 结果可直接可视化。Multiwfn 内部自动调用高级图形库 DISLIN 来可视化结果，大多数绘图参数都可在交互界面中控制。这极大地简化了波函数分析，特别


<!-- p.23 -->


是对于研究实空间函数的分布。

Multiwfn 的主要功能 注：尽管 Multiwfn 功能众多、手册很厚，但只要查看 Multiwfn 程序包中的“Multiwfn quick start”文档，就能很容易学会如何实现下面列出的功能。

- 显示分子结构并查看轨道（MO、NBO、自然轨道、NTO、定域轨道等）。生成轨道图的速度极快，使用非常方便。
- 输出某一点处所有支持的实空间函数以及梯度和 Hessian。数值可分解为轨道贡献。
- 计算沿一条线的实空间函数并绘制曲线图。
- 计算一个平面内的实空间函数并绘制平面图。支持的图形类型包括填充色图、等值线图、浮雕图（带/不带投影）、梯度图和矢量场图。
- 计算空间范围内的实空间函数，数据可导出为 Gaussian 型 cube 网格文件（.cub），并可视化为等值面。
- 对于一维、二维和三维实空间函数的计算，用户可以定义多个波函数文件产生的数据之间的运算。因此可以非常容易地计算和绘制如 Fukui 函数、dual descriptor 和密度差等。同时所有实空间函数的 promolecule 和变形性质可直接计算。
- 对任意实空间函数做拓扑分析，如电子密度（AIM 分析）、Laplacian、ELF、LOL、静电势等。可以定位临界点（CPs），生成拓扑路径和盆间界面，然后在三维图形界面窗口中直接可视化，或绘制在平面图上。可计算临界点处或沿拓扑路径的各种实空间函数数值。临界点性质可分解为轨道贡献。
- 检查和修改波函数。例如，输出轨道和基函数信息，手动设置轨道占据数和类型，平移和复制体系，丢弃指定原子的波函数信息。
- 布居分析。支持的方法：ADCH（Atomic dipole moment corrected Hirshfeld）、Hirshfeld、Hirshfeld-I、MBIS、cMBIS、EMBIS、AEMBIS、VDD、Mulliken、Löwdin、Modified Mulliken（包括三种方法：SCPA、Stout & Politzer、Bickelhaupt）、Becke、CM5、1.2*CM5、CHELPG、Merz-Kollmann、RESP、RESP2、AIM（Atoms-in-Molecules）和 EEM（Electronegativity Equalization Method）。可基于原子电荷计算两个给定片段间的静电相互作用能。
- 轨道成分分析。支持 Mulliken、Stout & Politzer、SCPA、Hirshfeld、Hirshfeld-I、Becke、自然原子轨道（NAO）和 AIM 方法来获得轨道成分。可计算轨道离域指数（ODI）或空间离域指数（SDI），以定量衡量轨道的空间离域程度。
- 键级/键强度分析。Mayer 键级；AO 或自然原子轨道（NAO）基下的多中心键级（MCBO）和多中心指数（MCI）（任意中心数）；Löwdin 正交化基下的 Wiberg 键级；Mulliken 键级；AV1245 指数；本征键强度指数（IBSI）。Mayer 和 Mulliken 键级可


<!-- p.24 -->


分解为轨道贡献。Wiberg 键级可分解为各种 NAO 对相互作用的贡献。
- 绘制总态密度、偏态密度、重叠布居态密度（TDOS、PDOS、OPDOS）和 MO-PDOS。最多可非常灵活方便地定义10个片段。也可绘制某一点的局域态密度（LDOS）曲线图，或一条线上的色填图。此外，完全支持基于（广义）Koopmans 定理绘制光电子能谱（PES），可计算 d-band 和 p-band 中心。也可绘制晶体轨道 Hamilton 布居（COHP）。
- 绘制各种光谱：IR（红外）、常规/预共振 Raman、UV-Vis、方向 UV-Vis、ECD（电子圆二色）、VCD（振动圆二色）、Raman 光学活性（ROA）和 NMR。对于振动光谱，不仅可绘制谐振光谱，还可绘制非谐基频、泛频和合频谱带。电子光谱可计入自旋-轨道耦合效应。用户可自定义丰富的参数（展宽函数、半峰宽、校正因子等）。可在图上输出并直接标注光谱的极大和极小。可在图底部加钉状线以清楚指示跃迁能级的位置和简并度。总光谱可分解为各个跃迁的单独贡献。可方便地把多个体系的光谱画在一起。可容易地绘制构象加权光谱。此外，对于振动类光谱，可绘制偏振动光谱（PVS），以直观理解不同原子或内坐标如何参与光谱，还可绘制重叠偏振动光谱（OPVS）以可视化各项的耦合。也可绘制偏振动态密度（PVDOS）。可基于理论模拟和实验测定的 UV-Vis 光谱精确预测化学物质显示的颜色。
- 分子表面的定量分析。可计算整个分子表面或局域表面的表面性质，如（总/正/负/极性/非极性）表面积、包围体积、映射函数的平均值和标准差；可计算各种 GIPF 描述符和分子极性指数（MPI）；可定位表面上映射函数的极小和极大；可基于 ESP 计算如 σ/π-hole 和孤对电子对应的特征区域面积；可对任意映射函数实现分子表面上的类盆分析。
- 处理网格数据（可从 .cub/.grd/.vti/.dx/CHGCAR... 载入，或由 Multiwfn 直接产生）。用户可对网格数据进行非常丰富的数学运算、设置特定范围内的数值、提取指定平面内的数据、绘制（局域）积分和平面平均曲线、进行平移等。
- 自适应自然密度划分（AdNDP）分析。界面是交互式的，AdNDP 轨道可直接可视化。可获得 AdNDP 轨道的能量和轨道成分。
- 模糊原子空间分析。支持 Becke、Hirshfeld、Hirshfeld-I 和 MBIS 原子空间划分方法，可计算以下量：在原子空间内或原子空间重叠区域内实空间函数的积分、原子/片段/分子的偶极和多极矩、原子多极矩、原子


<!-- p.25 -->


重叠矩阵（AOM）、片段重叠矩阵（FOM）、定域和离域指数（LI、DI）、片段间 DI（IFDI）和片段 LI（FLI）、凝聚线性响应核、多中心 DI，以及五个芳香性指数，即 FLU、FLU-π、PDI、PLR 和信息论芳香性指数。也可按 Tkatchenko-Scheffler 方法计算原子有效体积、自由体积、极化率和 C6 色散系数。
- 电荷分解分析（CDA）和扩展 CDA 分析。可绘制轨道相互作用图。可定义无限多个片段。
- 盆分析。对任意实空间函数可定位吸引子，可同时产生相应盆并可视化。所有实空间函数都可在产生的盆内积分。可计算盆的电多极矩、盆/原子重叠矩阵（BOM/AOM）、定域指数（LI）和离域指数（DI）。可获得原子对盆布居的贡献。ELF 盆的标记可自动指定。可计算高 ELF 定域域布居和体积（HELP 和 HELV）。
- 电子激发分析：可视化和分析空穴-电子分布、跃迁密度、跃迁电/磁偶极矩和电荷密度差；计算空穴与电子间的库仑吸引能（激子结合能）；计算 Mulliken 原子跃迁电荷和 TrEsp（基于静电势拟合的跃迁电荷，transition charge from electrostatic potential）；把跃迁电/磁偶极矩分解为 MO 对贡献或基函数/原子贡献；用 JCTC, 7, 2498 提出的方法分析电荷转移；把原子/片段跃迁密度矩阵、跃迁偶极矩矩阵和电荷转移矩阵绘制为热图；

计算 Δr 指数（JCTC, 9, 3118）和 Λ 指数（JCP, 128, 044118）以揭示电子激发特征；计算激发态之间的跃迁电/磁偶极矩；产生自然跃迁轨道（NTOs）；计算 ghost-hunter 指数（JCC, 38, 2151）；通过 IFCT 方法计算片段间电荷转移量；为一批激发态产生自然轨道；快速查看所有激发态中的主要 MO 跃迁；绘制电荷转移光谱（Carbon, 187, 78）以揭示激发特征；基于电子激发的电子密度极化分析（JPCA, 124, 633）；为手性体系计算 ECD/CPL 不对称因子（g）。
- 轨道定域化分析：支持 Pipek-Mezey（基于 Mulliken、Löwdin 或 Becke 布居）和 Foster-Boys 定域化方法。可得到所得定域轨道（LMOs）的成分、能量和偶极矩，定域轨道的形状和中心可容易地可视化。此外，基于定域轨道，可通过 LOBA 方法（PCCP, 11, 11297）或改进 LOBA 方法计算氧化态。

- 弱相互作用的可视化研究：相互作用区域指示符（IRI 和 IRI-π, Chem.-Methods, 1, 231）；RDG/NCI 方法（JACS, 132, 6498）；aNCI 方法（涨落环境中的非共价相互作用分析，JCTC, 9, 2226）；DORI 方法（JCTC, 10, 3745）；独立梯度模型（IGM）方法（PCCP, 19, 17928）；基于分子密度 Hirshfeld 划分的 IGM（IGMH）（JCC, 43, 539）；改进 IGM（mIGM, Struct. Bond., 190, 297）；平均 IGM 和平均 mIGM（mIGM 和 amIGM, Struct. Bond., 190, 297）。这些实空间函数等值面包围的单个区域可积分以做定量分析。也支持 Becke 和 Hirshfeld 表面分析以及


<!-- p.26 -->


指纹图分析。也可可视化范德华势（J. Mol. Model., 26, 315）并定位极值。
- 概念密度泛函理论（CDFT）分析：Fukui 函数和 dual descriptor，及其凝聚形式和轨道加权变体；Fukui 势和 dual descriptor 势；Mulliken 电负性；硬度；亲电性和亲核性指数；亲电描述符；软度；凝聚局域软度；相对亲电性和亲核性；亲电和亲核超离域性；键 dual descriptor；dual 离域描述符，等等。支持特定模型以妥善处理（准）简并 HOMO 和 LUMO 的情形。
- 扩展跃迁态-化学价自然轨道（ETS-NOCV）：可定义任意多个片段，同时支持闭壳层和开壳层情形。可获得 NOCV 本征值、能量和成分，许多相关函数可容易地可视化为等值面，包括 NOCV 轨道波函数、NOCV 对密度、冻结态轨道（frozen state orbitals）、Pauli 变形密度、轨道变形密度和总密度差。
- 能量分解分析：sobEDA 和 sobEDAw（J. Phys. Chem. A, 127, 7023 (2023)）、基于 UFF/AMBER/GAFF 分子力场的 EDA（EDA-FF）；Shubin Liu 能量分解（EDA-SBL）；原子对色散能贡献的分析和色散密度的计算。
- 电子离域和芳香性分析：多中心键级（MCBO）、AV1245 和 AVmin；等化学屏蔽表面（ICSS）；用于非平面或倾斜体系的 NICS_ZZ；ELF-π 和 ELF-σ；芳香性谐振子模型（HOMA）和 Bird 指数；重参数化 HOMA（HOMAc 和 HOMER 指数）；Shannon 芳香性指数；对位离域指数（PDI）；芳香涨落指数（FLU）和

FLU-π；对位线性响应指数（PLR）；信息论（ITA）芳香性指数；环临界点性质；NICS-1D 扫描曲线图；积分 NICS（INICS）和 FiPC-NICS 指数；NICS-2D 扫描平面图，等等。
- （超）极化率研究：解析 Gaussian 的“polar”任务输出文件并计算许多与（超）极化率相关的数据；计算与超 Rayleigh 散射（HRS）相关的量；绘制（超）极化率密度；获得原子对（超）极化率的贡献；用态求和（SOS）方法计算（超）极化率；二能级和三能级模型分析；（超）极化率张量的单位球和矢量表示；计算分子中原子极化率
- 结构和几何相关分析：分子范德华（vdW）体积；整个体系或单个片段的 vdW 表面积；分子长度/高度/重量、vdW 直径和动力学直径；空腔体积和直径；原子间连接性和原子配位数；原子簇的平均键长；键长交替（BLA）、键级交替（BOA）以及键角和二面角交替；分子平面性参数（MPP）和偏离平面跨度（SDP）；可视化晶胞中的自由区域（孔）并计算其体积；非常丰富的几何操作；绘制表面距离投影图；两个片段间的最小/最大以及几何/质量中心距离；特定


<!-- p.27 -->


环的面积和周长
- 其他功能（不完全列表）：用 Becke 多中心方法在全空间积分实空间函数；计算 alpha 和 beta 轨道间的重叠积分；计算两个轨道间的重叠和质心距离；通过组合片段波函数产生新波函数；计算 LOLIPOP 指数；计算分子间轨道重叠；Yoshizawa 电子传输路径分析；计算 Hilbert 空间中的原子和键偶极矩；绘制实空间函数的径向分布函数；计算两个不同波函数中轨道间的重叠积分；输出轨道间的各种积分；计算实空间函数的一阶和二阶矩以及回转半径；把载入的结构/波函数导出为许多流行格式，如 .wfn、.wfx、.molden、.fch、NBO .47、.pdb、.xyz，以及为许多已知量子化学程序产生输入文件；计算键极性指数（BPI）；域分析（获得由实空间函数定义的等值面内的性质）；计算电子相关指数；

探测 π 轨道并计算轨道 π 成分；在 alpha 和 beta 轨道间做双正交化以最大配对；计算核-价分岔（CVB）指数；计算轨道对密度差（如 Fukui 函数）或其他网格数据的贡献；键级密度（BOD）和自然自适应轨道（NAdO）分析；把原子径向密度拟合为 STOs 或 GTFs；模拟扫描隧道显微镜（STM）图像；计算电偶极/四极/八极/十六极矩和电子空间范围，等等。 Multiwfn 支持的实空间函数 实空间函数分析是 Multiwfn 最强大的功能之一，支持100多种实空间函数，列举如下，详细描述见手册2.6节和2.7节：

- 电子密度
- 电子密度梯度模
- 电子密度 Laplacian
- 某轨道的波函数值和概率密度
- 电子自旋密度
- Hamilton 动能密度 K(r)
- Lagrangian 动能密度 G(r)
- Becke 定义的电子定域函数（ELF）和 Tsirelson 定义的 ELF
- Becke 定义的定域轨道指示符（LOL）和 Tsirelson 定义的 LOL

- 相互作用区域指示符（IRI）和 IRI-π
- 独立梯度模型（IGM）中定义的 δg 函数和基于 Hirshfeld 划分的 IGM（IGMH）中定义的 δg 函数

- 局域信息熵
- 静电势（ESP），以及来自核/电子/原子电荷的静电势
- 范德华势
- 约化密度梯度（RDG），含/不含 promolecular 近似

- sign(λ2)ρ（电子密度 Hessian 矩阵第二大本征值的符号与电子密度的乘积），含/不含 promolecular 近似


<!-- p.28 -->


- 交换-相关密度、相关穴和相关因子
- 平均局域电离能（ALIE）和局域电子亲和能（LEAE）
- source 函数
- 电子离域范围函数 EDR(r;d)和轨道重叠距离函数 D(r)
- 其他（不完全列表）：势能密度、电子能量密度、轨道加权 Fukui 函数和 dual descriptor、强共价作用指数（SCI）、超强相互作用（USI）、成键和非共价相互作用（BNI）、局域电子亲和/电负性/硬度、电子密度的椭率和刚度、eta 指数、on-top 对密度、多种形式的 DFT 交换-相关势、多种形式的 DFT 动能密度、Weizsäcker 势、Fisher 信息熵、Ghosh/Shannon 熵密度、Rényi 熵的被积函数、shape 函数、局域温度、键金属性、线性响应核、位阻能/势/电荷、Pauli 势/力/电荷、量子势/力/电荷、PAEM、密度重叠区域指示符（DORI）、慢电子区域（RoSE）、PS-FID、单指数衰减探测器（SEDD）、电子线动量密度、电/磁偶极矩密度、局域电子相关函数、电场强度、应力张量刚度、应力张量极化率、分数占据数加权电子密度（FOD），等等。

在 Multiwfn 中实现新的实空间函数极其容易，如手册2.7节所示。

Multiwfn 能做的事 下面简要列出 Multiwfn 针对不同主题支持的分析，查阅“Multiwfn quick start.pdf”文档可很容易找到相关手册章节。当你感到困惑时，别忘了在 Multiwfn 官方论坛提问！

- 可视化各种程序产生的各种轨道（多种形式）
- 表征化学键：各种形式的 AIM 分析；研究实空间函数

（ELF、LOL、∇2ρ、动能/势能密度、IRI 和 IRI-π、价电子密度、片段密度差、变形密度、source 函数、键椭率、键度、eta 指数、V(r)/G(r)、SCI、PAEM、IGM……）；各种键级分析（Mayer、Laplacian、Mulliken、Wiberg、Fuzzy 和多中心键级，以及 Mayer、Mulliken 和 Wiberg 键级的分解分析）；本征键强度指数（IBSI）；定域/离域指数；轨道定域化分析；键级密度（BOD）和自然自适应轨道（NAdO）分析；用多种方法衡量键极性和键偶极矩；电荷分解分析（CDA）；扩展跃迁态-化学价自然轨道（ETS-NOCV）；重叠布居态密度（OPDOS）；能量分解分析，等等。综述见手册4.A.11节。在扫描和 IRC 过程中各种化学键性质的变化也可通过 shell 脚本很容易研究，见手册4.A.1节。

- 表征电子分布及其变化：原子电荷（AIM、Mulliken、SCPA、Hirshfeld、Hirshfeld-I、Voronoi、Löwdin、ADCH、CM5、MBIS、EEM、CHELPG、MK、RESP、RESP2……）；基函数/壳层/原子/片段的总和自旋布居分析；原子电偶极和多极矩分析（还可通过 Multiwfn 提供的绘图脚本在 VMD 程序中可视化）；对密度差的绘制/盆分析/域分析；电荷位移曲线


<!-- p.29 -->


- 芳香性和电子离域分析：综述见手册4.A.3节

- 表征分子内和分子间弱相互作用：AIM 分析（键路径可视化和键临界点处各种性质的分析）；弱相互作用的可视化分析

（NCI、IGM、IGMH、aIGM、IRI、DORI）；基于 IGM 或 IGMH 的原子和原子对 δg 指数；对静电势（ESP）的定量分子表面分析；多种形式的 ESP 绘制；范德华势的绘制；基于力场的能量分解分析（EDA-FF）；Hirshfeld/Becke 表面分析；LOLIPOP；相互穿透距离和穿透体积分析；原子电荷和多极矩分析；电荷转移分析（密度差图、CDA、布居变化……）；ELF 和核-价分岔（CVB）指数，等等。综述见手册4.A.5节

- 电子激发分析：空穴和电子的分析（分布、原子/片段/轨道贡献、质心位置、位移和重叠、激子结合能）；电荷转移分析（IFCT、密度差……）；NTO；关键 MO 间的重叠和质心距离；原子/片段跃迁密度矩阵和电荷转移矩阵的绘制；∆r 指数；跃迁偶极矩向基函数/原子/片段/MO 对贡献的分解；各激发态之间的跃迁偶极矩；跃迁原子电荷；ghost-hunter 指数；揭示激发过程中电子结构（成键和布居）的变化；输出所有激发态中的主要 MO 跃迁；绘制电荷转移光谱以图形化揭示 UV-Vis 光谱本质，等等。综述见手册4.A.12节

- 反应位点预测和反应性分析：分子表面上的 ESP 和 ALIE 分析；原子电荷；前线分子轨道的轨道成分分析；π 电子布居；轨道重叠距离函数分析；自动计算概念密度泛函理论框架下定义的所有量；计算轨道（MO、NBO、NAO 等）对 Fukui 函数的贡献。综述见手册4.A.4节

- 预测分子凝聚相性质：利用 vdW 表面上的 ESP 分布经验预测汽化热、升华热、分子晶体密度、沸点、熔化热、表面张力、pKb 等。可定量分子极性。见手册3.15.1节

- 绘制光谱：IR、Raman、UV-Vis、ECD、VCD、ROA、NMR 和光电子能谱。在 UV-Vis 情形下，可精确预测显示的颜色

- 表征几何结构
- （超）极化率研究
- 导电分析：TDOS 和 PDOS；相邻单体间的轨道重叠分析；Yoshizawa 传输路径分析；键长/键级交替（BLA/BOA）

- 其他：讲授结构化学；模拟扫描隧道显微镜（STM）图像；转换含几何或波函数信息的文件格式；研究电子相关效应；为 DFT 泛函实现 ELF-tuning 和 LOL-tuning；用 LOBA 或改进 LOBA 方法计算氧化态；研究实空间函数的分布（径向分布函数、质心、一阶和二阶矩、全空间和局域积分……）；计算分子轨道中的 σ 或 π 成分、几何变换，等等


<!-- p.30 -->


引用 Multiwfn 若在研究中使用了 Multiwfn，至少必须在正文中引用以下 Multiwfn 原始文献：

Tian Lu, Feiwu Chen, Multiwfn: A Multifunctional Wavefunction Analyzer, J. Comput. Chem. 33, 580-592 (2012) DOI: 10.1002/jcc.22885 Tian Lu, A comprehensive electron wavefunction analysis toolbox for chemists, Multiwfn, J. Chem. Phys., 161, 082503 (2024) DOI: 10.1063/5.0216272

应根据所用方法和功能引用我的其他论文。请认真查看 Multiwfn 程序包中的 How to cite Multiwfn.pdf 文档。

请尽量在正文而不是补充信息中提及和引用 Multiwfn，否则读者不仅很难注意到 Multiwfn，该论文也不会被计入引用统计。

讨论区 有两个 Multiwfn 官方论坛，使用不同语言。你可以在其中任一个讨论任何关于 Multiwfn 和波函数分析的内容。若在使用 Multiwfn 时遇到问题，请毫不犹豫在这些论坛上发帖！

Multiwfn 英文论坛：http://sobereva.com/wfnbbs Multiwfn 中文论坛：http://bbs.keinsci.com/wfn 另外：Multiwfn Youtube 频道有一些有价值的 Multiwfn 演示视频，强烈建议观看并订阅该频道。

## Multiwfn

> 第2章：安装、使用、输入文件、实空间函数、用户自定义函数、图形格式、周期体系

> 原文件：`../multiwfn_full.md`（全量单文件存档）｜图片目录：`../mw_imgs/`

---
