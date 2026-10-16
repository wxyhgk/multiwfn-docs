# Multiwfn 避坑表（FAQ）

> 做错会浪费时间/算错的实质项：注意、警告、常见报错与解法。

## 安装与通用
| 注意/问题 | 出处 | 说明与解法 |
|---|---|---|
| 发论文用了 Multiwfn 却只在补充信息里引用，或漏引原文 | [sec-1-overview.md](sec-1-overview.md) | 正文中至少必须引用 Tian Lu 原始两篇论文（J. Comput. Chem. 33, 580-592 (2012)；J. Chem. Phys. 161, 082503 (2024），再按二进制包中 How to cite Multiwfn.pdf 补引所用方法论文；尽量写在正文而非补充信息，否则读者难注意到且不计入引用统计。 |
| Windows 下只解压不配 settings.ini，并行跑不满、多核浪费 | [sec-2-1-install.md](sec-2-1-install.md) | 把 settings.ini 中 nthreads 设为 CPU 物理核心数；想直接打开 .chk 还须设 formchkpath 为 Gaussian 的 formchk 实际路径。 |
| Linux 启动报缺 libXm.so.4，或大体系分析崩溃 | [sec-2-1-install.md](sec-2-1-install.md) | 先装 motif（CentOS 系 yum install motif；Ubuntu 系 sudo apt-get install libxm4 libgl1）；~/.bashrc 加 export OMP_STACKSIZE=1000M 与 ulimit -s unlimited（不好用改 ulimit -Sn unlimited）；cat /proc/sys/kernel/shmmax 太小则在 /etc/sysctl.conf 加 kernel.shmmax=5000000000 并重启；缺 .so 就装提供它的包；只缺图形库又不用可视化就改用 noGUI 版。 |
| 远程纯文本模式载入文件后卡约 2 秒 | [sec-2-1-install.md](sec-2-1-install.md) | 在 ~/.bashrc 加 export DISPLAY=":0" 后重进终端。 |
| 在 MacOS 上找不到官方安装包 | [sec-2-1-install.md](sec-2-1-install.md) | 官方无 MacOS 版，须自编译（见 multiwfn-mac-build 仓库或中文论坛帖）并设 OMP_STACKSIZE 与 shmmax（kern.sysv.shmmax），或用 Unofficial Wineskin 跑 Windows 版。 |
| 用主菜单 r 换文件后结果异常 | [sec-2-2-using-multiwfn.md](sec-2-2-using-multiwfn.md) | r 会重载 settings.ini 但不如重启干净，最稳妥是重启 Multiwfn 或开新实例；上次文件可用字母 o 快载，同目录文件可用 ? 代替路径。 |
| 改了 settings.ini 却没生效 | [sec-2-3-files-of-multiwfn.md](sec-2-3-files-of-multiwfn.md) | 查找顺序为当前文件夹、Multiwfnpath 环境变量路径、默认设置；确认改的是实际被加载的那一份，并通读 settings.ini 注释找相关参数。 |
| 大体系并行计算崩溃 | [sec-2-4-parallel-implementation.md](sec-2-4-parallel-implementation.md) | 增大 settings.ini 的 ompstacksize（Windows）或环境变量 OMP_STACKSIZE（Linux/MacOS）；nthreads 一般设为物理核心数。 |
| 功能报错多半是输入文件类型不对 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) | Multiwfn 按扩展名判类型，不同功能要不同信息：Hirshfeld 等布居分析需 GTF 波函数（.mwfn/.fch/.molden/.gms/.31~.40/.wfn/.wfx），.pdb/.xyz/.mol 等无波函数不能用；promolecular 近似 RDG 只需坐标，几乎所有格式都可用。 |
| 含幽灵原子的文件读入电荷不对 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) | 幽灵原子元素序号应为 0、元素名应为 Bq，Multiwfn 按常规读核电荷但其核电荷原则上应为零，建文件时就要写对。 |
| .wfn 不含虚轨道、g/h 函数读不出 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) | .wfn 本来就不记录虚轨道，需要虚轨道改用 .fch/.mwfn/.molden；g/h 角动量须按手册 TYPE ASSIGNMENT 21~35/36~56 的特定顺序记录才被识别。 |
| 对 ECP 体系的 ESP、动能密度、ELF 算出离谱值却以为是 EDF 的锅 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) | EDF 只修正电子密度及其梯度/Laplacian、局域信息熵、RDG、sign(λ2)ρ 及相应拓扑分析，既不影响 ESP 也不影响依赖波函数的量（如动能密度、ELF）；要分析重元素后者须用全电子基组、至少小核 ECP。 |
| 非 Gaussian 产生的 .wfx 做 ECP 密度分析仍缺芯电子 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) | ORCA 等产生的 .wfx 无 EDF 段；但只要输入含 GTF 信息 Multiwfn 会自动从内置 EDF 库加载，只有自带 EDF 段的 .wfx 才用文件内 EDF；G09 B.01 等极少数 .wfx 的 EDF 电子数不对，须用主功能 100 子功能 4 积分全空间密度验证是否约等于总电子数。 |
| .chk 直接加载失败；post-HF 用 .fch 结果不对 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) | 直读 .chk 须先设 settings.ini 的 formchkpath，Multiwfn 自动调 formchk 转 .fch/.fchk 并事后删除；用 .fch/.fchk 作 post-HF 载体前必须先读第 4 章开头，老版本 Q-Chem 的 .fchk 还须设 ifchprog=2（Q-Chem≥5.0 不用）。 |
| 任意程序的 molden 都拿来用，结果错了还不知道 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) | 只正式支持 Molpro、ORCA、xtb、Dalton、NWChem（仅球谐且关对称）、MRCC（仅球谐）、deMon2k、BDF、CP2K（仅球谐）的 molden，其它先按附录 5 检查波函数是否正确加载，或先经 molden2aim 标准化；molden 只认 GTF 不认 STO，h 函数仅有限支持；大 .molden 反复分析先用主功能 100 子功能 2 转 .mwfn 提速。 |
| ECP 体系用 molden 算 ESP/原子电荷全错 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) | molden 不显式记核电荷，Multiwfn 把 [Atoms] 段第三列原子序号当核电荷，ECP 体系须手动改为价电子数或在文件头加 [Nval] 段（如 Na 9、Cl 7）；ORCA≥6.0 导出且标题行含 orca 字样的 [Pseudo] 段可自动处理，不用手改；ORCA .gbw 免手工转换可设 orca_2mklpath。 |
| .gms 非 C1 对称或 Firefly 文件读入失败 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) | .gms 只保证默认 NPRINT 的 HF/DFT/TDDFT 输出，非 C1 点群无法处理；Firefly 兼容性差（仅测过 DFT 单点与 TDDFT），改 C1 重算或换 molden/fch。 |
| NBO 轨道画出来不对，或加载顺序错 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) | .31 记基函数须先载，再载 .32~.40 之一（同名可只输后缀）；各类轨道中只有 NBO/NLMO 算实空间函数才有意义。 |
| .xyz/.mol 结构读错元素、多帧只读到第一帧 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) | .pdb/.xyz/.mol 等本来就无波函数；.xyz 多帧只加载第一帧；.mol 仅支持 V2000（原子/键上限各 999）；VMD 导出的 .xyz 用原子名而非元素名易误判，同目录有同名 .pdb 则借用其元素名，仍要核对。 |
| .gro 元素识别错；.cif 对称原子生成不出来 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) | .gro 只记原子名，Multiwfn 按原子名/残基名猜元素，加载后必须检查分子式；.cif 必须显式给出对称操作否则无法生成等效原子。 |
| .gjf/.mop/CP2K/QE 输入文件加载坐标失败或无晶胞 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) | .gjf/.mop 与 CP2K .inp/.restart 原子必须用 Å 笛卡尔坐标记录（.gjf 另用 Tv 字段给晶胞）；Quantum ESPRESSO 输入只支持 ibrav=0；Gaussian/ORCA 输出文件的几何还受 settings.ini 的 iloadGaugeom/iloadORCAgeom 控制。 |
| VASP 文件放在目录里却识别不出来 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) | POSCAR/CHGCAR/CHG/ELFCAR/LOCPOT 靠文件名含相应字符串识别，且不能带 .in/.inp 扩展名（如 MOF.POSCAR 可，POSCAR.in 不行）。 |
| Laplacian 数值与 AIMAll 对不上；大体系实空间函数耗时异常 | [sec-2-6-real-space-functions.md](sec-2-6-real-space-functions.md) | AIMAll/AIM2000 的 Laplacian 定义与 Multiwfn 差 -1/4 因子，对比前先换算，laplfac 非 1.0 也会缩放结果；指数小于 -40 跳过求值由 expcutoff 控制，默认精度安全，勿乱关。 |
| 核处函数值溢出/发散导致后续分析崩 | [sec-2-6-real-space-functions.md](sec-2-6-real-space-functions.md) | 核处发散的函数在程序内恒返回 1000 而非无穷大，属刻意数值保护，作图/积分遇到 1000 平台即为核点。 |
| 多组态波函数 ELF 用错定义还与文献硬比 | [sec-2-6-real-space-functions.md](sec-2-6-real-space-functions.md) | Becke 原始 ELF 与 MP2/CASSCF/CCSD 等多组态不兼容，Multiwfn 对多组态仅基于自然轨道算 ELF（Savin 动能观点），属合理实现而非错误；Tsirelson 近似版（ELFLOL_type=1）因动能项近似而不如 Becke 版，只保定性，可免波函数分析 X 射线密度。 |
| NCI 图被共价区淹没；重元素 promolecular RDG 算不出 | [sec-2-6-real-space-functions.md](sec-2-6-real-space-functions.md) | RDG_maxrho 默认 0.05，把高密度处 RDG 置 100 以屏蔽非弱相互作用区，设 0 取消；promolecular 原子密度 H~Ar 取 NCI 原文数据，其余按附录 3 求得，重于 Lr 无数据。 |
| post-HF 交换-相关密度当成精确值发表 | [sec-2-6-real-space-functions.md](sec-2-6-real-space-functions.md) | 含 Gaussian 在内主流程序不输出 2PDM，Multiwfn 对 post-HF 用 Müller 自然轨道近似且形式不唯一，整数占据时才退化为单行列式形式；αβ/αα 相关无法从总量中分离，解释时须声明近似。 |
| IGM 的 δg 选错编号导致要波函数却只给了坐标 | [sec-2-6-real-space-functions.md](sec-2-6-real-space-functions.md) | 函数 22 是 promolecular δg 只需几何，函数 23 是 Hirshfeld 划分 δg 必须提供波函数；研究特定片段间弱相互作用用 IGM 而非只看总数。 |
| 格点插值函数 -3 算出来在核处有毛刺、越界得零 | [sec-2-7-user-defined-real-space-function.md](sec-2-7-user-defined-real-space-function.md) | 三次 B 样条 -3 虽比三线性 -1 光滑，但在核 cusp、陡变或格点稀疏处可能更差甚至振荡；不考虑周期时越界返回 0；周期格点须先经隐藏主功能 1000 选项 18 设盒子信息，或在 .cub 首行加 box2cell。 |
| 局域亲和/电负性/硬度函数算出无意义值 | [sec-2-7-user-defined-real-space-function.md](sec-2-7-user-defined-real-space-function.md) | EA_L/E_att/χ_L/η_L 要求输入同时含单行列式占据+虚轨道且不支持限制性开壳层（用 .mwfn/.fch/.molden/.gms）；EA_L（含 χ_L/η_L）与弥散基组不兼容，E_att 可用任何基组但要求 LUMO 能量为负（B3LYP/6-31+G(d,p) 常可用）。 |
| 超大体系 PAEM 算到天荒地老 | [sec-2-7-user-defined-real-space-function.md](sec-2-7-user-defined-real-space-function.md) | 自定义 33 是精确 PAEM，34 是 DFT 交换-相关势版只支持闭壳层但快得多，超大体系只能选 34（经 iDFTxcsel 选泛函）；V(r)/G(r) 在 BCP 处 <1 闭壳层、>2 共价、1~2 中间型。 |
| 信息增益密度 i_G 全零/报错；g3 等函数找不到变形图 | [sec-2-7-user-defined-real-space-function.md](sec-2-7-user-defined-real-space-function.md) | 自定义 49（i_G）分析前必须先经隐藏主功能 1000 子功能 17 构建 promolecular 波函数；自定义 57/58/59 只能在主功能 3/4/5 作图，deformation/promolecular 图不可用。 |
| 线条图锯齿严重、投 Office 模糊 | [sec-2-8-graphic-formats-and-image-size.md](sec-2-8-graphic-formats-and-image-size.md) | graphformat 设导出格式，线条为主（曲线/等值线）用 pdf/svg，嵌 Office 用 wmf；graph1Dsize/2Dsize/3Dsize 分管曲线/二维/三维尺寸；透明背景看指定视频教程。 |
| 团簇边界电子结构当结论、d/f 金属团簇 SCF 反复不收敛 | [sec-2-9-analysis-of-periodic-systems.md](sec-2-9-analysis-of-periodic-systems.md) | 团簇要足够大并做尺寸收敛测试，边界原子电子结构必无意义不讨论；X 射线结构恒优化 H、重原子一般不优化，表面/吸附固定边界只优化中心；共价晶体 H 饱和边界并优化 H；d/f 金属不推荐团簇模型；离子晶体用嵌入团簇（QM 区+多层点电荷+最内层 cECP 缓冲防电子溢出）。 |
| 拿其它周期程序的波函数硬塞 Multiwfn | [sec-2-9-analysis-of-periodic-systems.md](sec-2-9-analysis-of-periodic-systems.md) | 周期波函数只支持 CP2K（Gaussian 周期 .fch 虽支持但太慢无实用价值）；CP2K 的 DFT 段须加 &PRINT/&MO_MOLDEN（NDIGITS 9），≥2026.2 再加 WRITE_CELL T/WRITE_PSEUDO T，老版手动补 [Cell]/[Nval] 或同目录 [Cell].txt，赝势体系把序号改为价电子数以自动用 EDF 并算对电荷。 |
| 非正交原胞等值面画歪、周期 ESP 当能算 | [sec-2-9-analysis-of-periodic-systems.md](sec-2-9-analysis-of-periodic-systems.md) | 非正交原胞等值面在 Multiwfn 内画不准，导出 cube 用 VMD/VESTA 看；ESP 分析尚不支持（无法基于波函数信息直接算 ESP）。 |
| 周期计算又慢又不准、一维/二维还按三维算 | [sec-2-9-analysis-of-periodic-systems.md](sec-2-9-analysis-of-periodic-systems.md) | PBCnxnynz 默认 1,1,1 无理由不改，小原胞（如 3.5 Å 金刚石）改 2,2,2；二维（XY 平面）设 ifdoPBCxyz=1,1,0，一维（沿 Z）设 0,0,1；expcutoff_PBC 调大变快但变差，默认已平衡。 |
| CP2K 用了 k 点/弥散基组做 Mayer/Mulliken 分析 | [sec-2-9-analysis-of-periodic-systems.md](sec-2-9-analysis-of-periodic-systems.md) | Multiwfn 不考虑 k 点，CP2K 只能用 gamma 点且原胞要足够大；Mayer 键级/Mulliken 布居等与弥散函数不兼容，绝不用强弥散基组，DZVP-GTH 常不可接受，推荐 MOLOPT-SR-GTH。 |
| 手头只有 .xyz/.wfn 却想做周期几何分析 | [sec-2-9-analysis-of-periodic-systems.md](sec-2-9-analysis-of-periodic-systems.md) | .xyz 第二行加 Tv_1/Tv_2/Tv_3 或 Lattice="..."，.wfn 末尾加 [Cell] 三行原胞矢量（Å），即可提供原胞信息；ifdoPBCxyz 同样影响几何分析；仅部分几何功能明确支持 PBC，其余当孤立体系处理。 |

## 布居键级与基础功能
| 注意/问题 | 出处 | 说明与解法 |
|---|---|---|
| Linux 下主功能 0 的鼠标拖拽无反应 | [sec-3-2-showing-molecular-structure.md](sec-3-2-showing-molecular-structure.md) | 须先单击一次绘图区域使光标变为手形，之后左键旋转、Ctrl+拖拽旋转/缩放、Shift+拖拽平移才生效 |
| 调大 Isosur. quality 后原来的轨道等值面消失了 | [sec-3-2-showing-molecular-structure.md](sec-3-2-showing-molecular-structure.md) | 这是预期行为，调整该数值会删除当前等值面，需重新选轨道计算；默认格点较粗糙，可改 settings.ini 中 nprevorbgrid 提高默认质量 |
| 想只把一个等值面设为透明面却做不到 | [sec-3-2-showing-molecular-structure.md](sec-3-2-showing-molecular-structure.md) | Multiwfn 不支持只把单个等值面绘制为透明面，透明风格须同时应用于等值面 #1 和 #2 |
| 非限制性波函数选错自旋轨道（如把 beta 当 alpha 看） | [sec-3-2-showing-molecular-structure.md](sec-3-2-showing-molecular-structure.md) | 列表前 Na 个为 alpha、后 Nb 个为 beta；输入框中负编号对应 beta（如 -9 为第 9 个 beta 轨道），输入前先确认自旋 |
| Rydberg 等弥散轨道等值面被截断或显示不全 | [sec-3-2-showing-molecular-structure.md](sec-3-2-showing-molecular-structure.md) | 默认 Aug3D 外延盒子对弥散轨道太小，用 Other settings-Set extension distance 增大本次外延，或改 settings.ini 中 Aug3D |
| GUIsettings.ini 保存/载入位置与预期不符 | [sec-3-2-showing-molecular-structure.md](sec-3-2-showing-molecular-structure.md) | 若定义了 Multiwfnpath 环境变量，该文件写到其指向目录并优先从那里载入，找不到时先检查该环境变量 |
| 主功能 0 显示的成键关系与经验预期不符 | [sec-3-2-showing-molecular-structure.md](sec-3-2-showing-molecular-structure.md) | .mol/.mol2 自带连接信息时直接按文件成键显示；其余情况按 CSD 共价半径和 1.15 倍判据判定，可拖 Bonding threshold 滑块调整 |
| 把某点实空间函数的轨道分解贡献加和后与总值对不上 | [sec-3-3-outputting-all-properties-at-a-point.md](sec-3-3-outputting-all-properties-at-a-point.md) | 多数实空间函数（如 ELF）含非线性算符，各轨道贡献之和一般不等于全轨道结果，不要用加和校验正确性 |
| 只想看某点电子密度等，ESP 计算拖慢全过程 | [sec-3-3-outputting-all-properties-at-a-point.md](sec-3-3-outputting-all-properties-at-a-point.md) | ESP 是代价最高的实空间函数，不需要时把 settings.ini 中 ishowptESP 设为 0 跳过 |
| 用 .pdb 等纯坐标文件在某点只能算很少函数 | [sec-3-3-outputting-all-properties-at-a-point.md](sec-3-3-outputting-all-properties-at-a-point.md) | 纯坐标输入只能给出基于 promolecular 密度的有限函数，这是输入信息不足所致，需换含 GTF 的波函数文件 |
| 线图上找的驻点和 Y=指定值位置不准 | [sec-3-4-outputting-and-plotting-specific-property-in-a-line.md](sec-3-4-outputting-and-plotting-specific-property-in-a-line.md) | 寻点基于已算数据点，点越密 X 越准；可增大 settings.ini 中 num1Dpoints（默认 3000）重算 |
| 线图上 ESP 曲线分辨率明显低于其它函数 | [sec-3-4-outputting-and-plotting-specific-property-in-a-line.md](sec-3-4-outputting-and-plotting-specific-property-in-a-line.md) | ESP 计算点数会自动降为六分之一以省时间，属预期行为，如需精细 ESP 剖面应分段或改用其它方式加密 |
| 平面梯度线图/矢量场图计算作图特别慢 | [sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) | 这两类需算函数梯度且图形库生成梯度线耗时，明显贵于其它图类；梯度线积分默认 RK2 已兼顾精度速度，RK4 更稳但更慢，非必要不换 |
| 平面图格点数拍脑袋设，浮雕图挤成一团或 ESP 算不动 | [sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) | Relief 类推荐 100,100（再密线条拥挤），其它图类推荐 200,200；总 ESP 非常耗时，预览先用较少格点 |
| 模式 6 定义平面得到歪斜或错误图形 | [sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) | 该专家模式要求两平移矢量正交，不正交则作图区域定义错误，输入前先正交化两矢量 |
| 模式 4/5 画出的平面图方向与预期镜像或转置 | [sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) | 三个原子/点的输入顺序直接决定作图区域 X、Y 轴取向，调换输入顺序即可校正方向 |
| 浮雕图顶部被削平 | [sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) | 数值太大在图中被截断，用后处理 Multiply data by a factor 缩放数据后再画 |
| 平面图上不显示临界点、键路径或盆间路径 | [sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) | 须先在主功能 2 中搜到 CP 并生成路径再回来画平面图；且 CP/路径点距平面超过阈值（CP 默认 0.5 Bohr，盆间路径用 disshowlabel）的不显示，可调阈值或换平面 |
| 盆间路径太短/太长或显示残缺 | [sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) | 路径最大长度=步长×最大迭代数，用 Set stepsize and maximal iteration 调整；距平面超 disshowlabel 的点不绘制 |
| 模式 1/2/3 的低/中/高质量名不副实 | [sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md](sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md) | 三档对应固定格点总数（约 12.5/51.2/172.8 万），只相对中等体系而言；大体系模式 3 也只算中等，微小体系模式 1 已足够细 |
| 等值面粗糙就无脑加密格点，计算时间爆炸 | [sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md](sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md) | 计算时间随格点数近似线性增长，先用模式 1 预览，确认实空间函数和等值无误后再提高质量 |
| 等值面边界被截断 | [sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md](sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md) | 盒子由包围分子的盒子外延得到，外延不合适时用 -10 Set extension distance 或改 settings.ini 中 Aug3D |
| 外部点文件（选项 100）载入失败或数值怪异 | [sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md](sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md) | 坐标必须用 Bohr 单位；首行为点数；每行 X Y Z 自由格式，第四列之后被忽略 |
| 自定义操作与主功能 -4、-3、6 联用得荒谬结果 | [sec-3-7-custom-operation-promolecular-and-deformation-properties.md](sec-3-7-custom-operation-promolecular-and-deformation-properties.md) | 避免这种联用；自定义操作只在主功能 3、4、5 内对多个波函数做加减乘除 |
| 前分子/变形性质算到一半报 Gaussian 相关错误 | [sec-3-7-custom-operation-promolecular-and-deformation-properties.md](sec-3-7-custom-operation-promolecular-and-deformation-properties.md) | atomwfn 缺元素 .wfn 时自动调 Gaussian 生成，要求 settings.ini 中 gaupath 正确；基组建议与分子波函数一致；出错先查 wfntmp 下 Gaussian 输入输出文件 |
| Gaussian 报 .wfn 路径截断或写文件失败 | [sec-3-7-custom-operation-promolecular-and-deformation-properties.md](sec-3-7-custom-operation-promolecular-and-deformation-properties.md) | Gaussian 只允许 .wfn 路径最长 60 字符，不要把 Multiwfn 放在路径太深的目录中 |
| 体系含超 Kr 重元素时前分子/变形性质做不出 | [sec-3-7-custom-operation-promolecular-and-deformation-properties.md](sec-3-7-custom-operation-promolecular-and-deformation-properties.md) | 自动生成+球化只支持到 Kr，更重元素须手动计算并球化原子波函数后放入 atomwfn 目录 |
| 指定原子波函数理论方法时加了 RO/U 前缀导致失败 | [sec-3-7-custom-operation-promolecular-and-deformation-properties.md](sec-3-7-custom-operation-promolecular-and-deformation-properties.md) | 用斜杠同时给方法和基组（如 BLYP/6-311G*），不要加 RO/U 前缀，程序会自动添加 |
| 原子密度球化后前分子性质仍有取向依赖或明显不对 | [sec-3-7-custom-operation-promolecular-and-deformation-properties.md](sec-3-7-custom-operation-promolecular-and-deformation-properties.md) | 球化方案与波函数类型绑定：主族用非限制、过渡金属用限制性开壳都会失效；过渡金属用 HF 也失效（4s 高于 3d 顺序错）；不需球化可把 settings.ini 中 ispheratm 设 0 |
| 每次算前分子性质都重新跑 Gaussian 生成原子波函数 | [sec-3-7-custom-operation-promolecular-and-deformation-properties.md](sec-3-7-custom-operation-promolecular-and-deformation-properties.md) | 把 wfntmp 中不带数字后缀的 .wfn（如 C .wfn）移到 atomwfn 目录（缺则自建），下次直接复用；examples/atomwfn 有前四周期 6-31G* 球化好的文件可直接复制 |
| 主功能 6 删掉片段 GTF 后后续分析全错且无法撤销 | [sec-3-8-checking-and-modifying-wavefunction.md](sec-3-8-checking-and-modifying-wavefunction.md) | 子功能 -3/-4 不可逆，GTF 丢弃后只能重启重载恢复；只可与主功能 1~6 安全联用，其它任务不懂原理不要用 |
| 子功能 0 存出 new.wfn 后轨道/原子数变少 | [sec-3-8-checking-and-modifying-wavefunction.md](sec-3-8-checking-and-modifying-wavefunction.md) | 保存时自动丢弃零占据轨道和无 GTF 原子，属预期行为；要其它格式先回主菜单进主功能 100 子功能 2 另存 |
| 照子功能 4 打印系数组装波函数结果不对 | [sec-3-8-checking-and-modifying-wavefunction.md](sec-3-8-checking-and-modifying-wavefunction.md) | 该处系数包含 GTF 归一化常数，不是纯基函数系数，基函数系数看子功能 5（需输入文件含基函数信息） |
| 用子功能 32 扩展的超胞波函数能带/轨道行为异常 | [sec-3-8-checking-and-modifying-wavefunction.md](sec-3-8-checking-and-modifying-wavefunction.md) | 平移复制只是近似，完全忽略相邻原胞轨道混合，只能省时间，不能替代真正的超胞计算 |
| 子功能 35 看不到 IRREP 或 discard 后行为异常 | [sec-3-8-checking-and-modifying-wavefunction.md](sec-3-8-checking-and-modifying-wavefunction.md) | 仅 .mwfn/.molden/.gms 记录 IRREP 且仅限 R/U SCF 波函数；很多程序写的 .molden 中 IRREP 缺失或错误，先检查文件 |
| 子功能 38 整数化占据后电子组态明显错乱 | [sec-3-8-checking-and-modifying-wavefunction.md](sec-3-8-checking-and-modifying-wavefunction.md) | 该功能假设轨道已按能量升序排列，乱序文件先确认/调整轨道顺序再用 |
| 算完布居发现没有片段电荷输出 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | 任何子功能想得片段电荷都须先选 -1 Define fragment 定义片段，否则只打印原子电荷 |
| Hirshfeld 电荷之和明显偏离整数 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | 说明数值积分不准，结果不可靠；增大 settings.ini 中 radpot/sphpot（默认 75/434，可试 100/590）重算 |
| VDD 电荷之和明显偏离分子净电荷 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | 同为积分精度问题，优先增大 sphpot（比 radpot 影响显著），作者另建议直接用 Hirshfeld 代替 VDD |
| Mulliken/SCPA/Stout-Politzer 电荷随基组乱飘或出现负布居 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | Mulliken 类方法基组依赖极强，一定不能带弥散函数；偶发负布居无意义；其中 Stout-Politzer 还有显著转动依赖性（旋转分子结果变），应少用，SCPA 至少保证布居非负 |
| Becke 电荷在离子体系中明显不合理 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | 默认 modified CSD 半径只对典型有机体系合理，离子体系不合适，需换半径或换电荷模型 |
| CHELPG/MK 拟合含重元素时程序追问半径或电荷异常 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | CHELPG 默认半径只定义到前三行，其它元素需手动输入（回车则用 UFF/1.2）；MK 默认第一二行及 P/S/Cl 沿用 Gaussian，Na-Si 用 1.57/1.65/1.65/1.80 Å；半径影响拟合点分布从而影响电荷 |
| 用选项 -1 读外部拟合点时 ESP 列被忽略/用错 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | 只有首行 numdata 为负值时才读第四列预计算 ESP，否则 Multiwfn 自己算 ESP |
| 用选项 -3 检验给定 .chg 的复现性时报错或 RMSE 异常 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | 若用选项 -2 加过额外拟合中心，.chg 中电荷数须与拟合中心总数一致；只看某碎片复现性用选项 4 限定原子 |
| Hirshfeld-I 算不动：缺 .rad、Gaussian 失败或 Windows 调不起 Gaussian | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | 最省事把 examples/atmrad 复制到当前目录直接用内置 .rad；自动生成缺 .rad 时镧系锕系无能为力须手动做；Gaussian 失败多为 SCF 不收敛，调关键词；Windows 先按附录 1 配 Gaussian 环境变量 |
| Hirshfeld-I 大体系巨慢或内存爆炸 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | 默认快速算法内存约 7×n_atm×n_atm×n_rad×n_ang，大体系换低内存算法；距离截断（选项 -3，默认开，截断 2.0）出问题可关闭或调大 |
| 手动准备 .rad 文件后 HI 仍去跑 Gaussian | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | 各族所需带电态须配齐（IA/VIIIA 配 -1/0/1，IIA 配 -1/0/1/2，IIIA~VIA 配 -2~2，VIIA 配 -1/0/1/2，过渡金属配 -1/0/1/2，镧系锕系建议 -1/0/1/2），缺了会自动补算；如算水需 O-2~O+2 和 H-1~H+1 共 8 个 |
| EEM 进去就报错或电荷明显不对 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | EEM 必须用 .mol/.mol2 输入（唯一带连接信息）；.mol 原子数上限 999，大体系用 .mol2；离子体系先用选项 2 设净电荷；芳香环须单双键交替表示（不能用 ar/4 号键型），建议 OpenBabel 由 xyz 转 .mol2 自动处理 |
| EEM 对共轭/金属等复杂体系复现很差 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | 内置参数只拟合典型有机体系（Mulliken/MK/NPA 目标），电子结构复杂体系不要指望 EEM 成立 |
| 用差水平算的 ADCH 电荷去复现实验偶极矩失败 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | ADCH 精确复现的是当前计算水平的偶极矩，HF/6-31G 等差水平的 ADCH 本来就无用；想在低水平也得合理偶极矩用 CM5 |
| 拿 CM5 电荷跑 uESE 溶剂化能结果差 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | uESE 在气相 B3LYP/def2-TZVP 下参数化，CM5 计算与几何优化都应在该水平做，并把 settings.ini 中 uESEinp 设 1 生成输入文件 |
| RESP 等价/电荷约束文件载入后结果无意义或报错 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | 同一原子不能出现在两条等价约束中；任一电荷约束条目与等价约束条目不能有交集；电荷约束之间允许相交 |
| 对称等价原子 ESP 电荷有轻微差异 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | 拟合点分布不严格服从点群对称所致；用选项 5 载入等价约束（含子功能 11 自动按点群生成 eqvcons_PG.txt）强制相等，优于单纯加密 CHELPG 格点 |
| RESP 成键判定错导致甲基等价约束/拟合原子划分错 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | 默认按 CSD 共价半径和 1.15 倍判连通，不符预期时在主功能 0 调成键阈值到显示正确，或用选项 7 读入 .mol 的连通性 |
| PEOE 电荷全零/不支持或含氮体系杂化明显错 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) | PEOE 只支持 H/C/N/P/O/S/F/Cl/Br/I 且不支持带电体系；连通性靠键长猜，三配位 N 杂化由几何定，务必先用至少定性正确的优化几何 |
| Mulliken/SCPA/Stout-Politzer 做轨道成分时报错要基函数 | [sec-3-10-orbital-composition-analysis.md](sec-3-10-orbital-composition-analysis.md) | 这三类方法依赖基组展开，当前版本必须用 .mwfn/.fch/.molden/.gms 作输入文件 |
| 片段成分分析结果对应 yesterday 的片段 | [sec-3-10-orbital-composition-analysis.md](sec-3-10-orbital-composition-analysis.md) | 片段定义界面状态会保留，做交叉项须先定义片段 1 再定义片段 2；彻底重定义前先用 clean 清空旧片段 |
| NAO 轨道成分模块进去无数据或虚轨道成分怪异 | [sec-3-10-orbital-composition-analysis.md](sec-3-10-orbital-composition-analysis.md) | NAO 基 MO 系数矩阵 Multiwfn 自己产不出，须在 NBO 输入 $NBO...$END 间加 NAOMO 关键词后提供输出文件；且该方法只适合占据轨道，虚轨道 Rydberg 贡献大不好用 |
| Hirshfeld/Hirshfeld-I 轨道成分又慢成分和又偏离 100% | [sec-3-10-orbital-composition-analysis.md](sec-3-10-orbital-composition-analysis.md) | 权重原子密度选内建原子密度而非原子 .wfn 文件（方便得多）；Hirshfeld 已足够好，无需更贵的 Hirshfeld-I；数值积分致总和偏离时程序自动归一化，看 After normalization 行 |
| 用 AIM 盆算轨道成分等半天结果还一般 | [sec-3-10-orbital-composition-analysis.md](sec-3-10-orbital-composition-analysis.md) | 作者明确不推荐，耗时远高于其它划分而结果并不更好，改用 Hirshfeld/Becke 划分 |
| LOBA 氧化态随阈值漂移、加和不等于净电荷 | [sec-3-10-orbital-composition-analysis.md](sec-3-10-orbital-composition-analysis.md) | 强烈建议改用 mLOBA（输 m）：电子判给贡献最大原子，无阈值任意性且氧化态之和严格等于净电荷；需 LMO/NBO 输入（Multiwfn 定域化产物或 Gaussian pop=saveNBO/saveNLMO 的 .fch） |
| 乙烷等对称体系 mLOBA 给出 -4/-2 不对称氧化态 | [sec-3-10-orbital-composition-analysis.md](sec-3-10-orbital-composition-analysis.md) | mLOBA 在（局域）对称下可能不平衡，把对称原子并为一片段求片段氧化态再平均（如两碳作一片段得 -6，每碳 -3） |
| Mayer/MCBO 键级随基组乱变 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) | 与 Mulliken 布居一样对基组敏感，不要用带弥散函数的基组，否则不可靠；要抗弥散用 NAO 基的选项 -2（需带 DMNAO 的 NBO 输出作输入，不要用 .fch） |
| 不同环大小的 MCBO 数值直接比出反直觉结论 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) | 不同中心数 MCBO 量级不同不可比，跨环比较用归一化 MCBO^(1/n)；开壳层只看 α+β 之和项 |
| MCBO 正反输结果不同，芳香性格点顺序拿不准 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) | 原始 MCBO 依赖输入方向与排列：环原子按顺/逆时针连序输入，或把 settings.ini 中 iMCBOtype 设 1 取双向平均，设 2 得全排列平均的 MCI；NAO 基/-3 结果与方向无关 |
| MCBO 算出微小负值或三中心明显负值不知咋解释 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) | 无弥散或 NAO 基下的微小负值直接视零；三中心明显负值意味着 3c-4e 作用（如 CO2） |
| NBO 算的 Wiberg 键级与主功能 9 选项 3 对不上 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) | 两者必然不同：NBO 在 NAO 基（OWSO 正交化）下算，选项 3 在 Löwdin 正交化基下算；要在 Multiwfn 得 NBO 一致值用 3.11.8 节 NAO 基分解（选项 -2 输两原子即 NAO 下 Wiberg，等价 NBO bndidx） |
| 拿 Mulliken 键级定量比较键强被质疑 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) | Mulliken 键级与经验键级一致性差，只宜定性看成键（正）/反键（负），定量比较用 Mayer；Wiberg(Löwdin)又倾向高估极性键，无特殊原因也优先 Mayer |
| 各轨道占据微扰 Mayer 贡献加和不等于 Mayer 键级 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) | Mayer 键级非密度矩阵线性函数，各轨道 I* 之和一般不等于总键级；只看 I* 与总键级之差（越负越成键）的相对排序 |
| LBO 在离子键或重原子间成键给出过小值 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) | 当前 LBO 实现只适合有机共价体系，不适合离子键和重于 Ar 的重原子间成键（模糊重叠区电荷集中不显著），应换键级定义 |
| 按 IBSI 原文复现 IBSI 数值对不上 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) | Multiwfn 不支持原文的 IGM-GB，只支持 IGM-pro/IGMH/mIGM且结果差异大，其中 IGM-pro 最接近原文；IGMH 贵得多，IGMH/mIGM 至少 high-quality，IGM-pro medium 即可；换水平用 IGMH 时参考值要重算（默认 H2 0.74144 Å，载 H2 波函数设参考 1.0 反推） |
| 大体系 IBSI 算不动或输出淹没在无数原子对中 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) | 只关心局域时用选项 3 限定片段以降低开销；默认只打印间距 <3.5 Å 原子对（可选项 5 调阈值），更大间距 IBSI 可忽略 |
| 直接算的 AV1245 比文献值系统性偏小 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) | 文献基于 AIM 盆+SOM，Multiwfn 按常规密度+重叠矩阵算，结果偏小属预期；3.8 起 MCBO 已线性可算大环，AV1245 优势减弱 |
| AV1245 算出无意义值或大环原子序号输不完 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) | 原始基函数下勿带弥散函数（NAO 基除外）；环原子按连接顺序输，先输 d 回车可自动按连接排序，但环原子与环外多连或 NAO 基时 d 模式不可用 |
| 片段间总键级对某些选项无输出 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) | 选项 -1 定义的片段间总键级对 MCBO、占据微扰 Mayer、Wiberg 分解不可用，换 Mayer/FBO 等双中心键级 |

## 谱学与表面
| 注意/问题 | 出处 | 说明与解法 |
|---|---|---|
| 用 Gaussian 输出文件做 DOS 输入，必须加 `pop=full` | [sec-3-12-plotting-density-of-states-pes-and-cohp.md](sec-3-12-plotting-density-of-states-pes-and-cohp.md) | 否则文件中没有绘制所需的轨道成分信息；纯文本输入只能画 TDOS |
| 画 PDOS/OPDOS 必须用含基函数信息的文件（`.mwfn` / `.fch` / `.molden` / `.gms`） | [sec-3-12-plotting-density-of-states-pes-and-cohp.md](sec-3-12-plotting-density-of-states-pes-and-cohp.md) | 纯文本输入没有基函数信息，界面中选项 -1 和 7 不出现，只能画总态密度 |
| 基组含弥散函数时，用 Mulliken/SCPA 算的 PDOS 毫无意义 | [sec-3-12-plotting-density-of-states-pes-and-cohp.md](sec-3-12-plotting-density-of-states-pes-and-cohp.md) | 不能删弥散函数时必须换 Hirshfeld 或 Becke 方法（代价是更耗时且只能把片段定义为原子集、画不了 OPDOS）；孤立体系默认 Mulliken，周期体系默认 SCPA（后者不需重叠矩阵） |
| DOS/PES 曲线绝对高度无意义，只看不同能量区相对高度 | [sec-3-12-plotting-density-of-states-pes-and-cohp.md](sec-3-12-plotting-density-of-states-pes-and-cohp.md) | 定稿时可在后处理菜单用选项 13 关掉 Y 轴标签和刻度；OPDOS 量级远小于 TDOS/PDOS，程序用双轴显示并提供右轴缩放因子 |
| 孤立体系 DOS 图上的 HOMO 虚线不是费米能级 | [sec-3-12-plotting-density-of-states-pes-and-cohp.md](sec-3-12-plotting-density-of-states-pes-and-cohp.md) | 对孤立体系“费米能量”是定义不清的概念，任何 ≥ E(HOMO) 且 < E(LUMO) 的能量都可算；不要在文章里把它标成 Fermi energy |
| Koopmans 定理做 PES 只是近似，多数 DFT 泛函 MO 能量负值偏离真实 VIP 很大 | [sec-3-12-plotting-density-of-states-pes-and-cohp.md](sec-3-12-plotting-density-of-states-pes-and-cohp.md) | 它完全忽略电子相关与轨道弛豫（QTP17 等特殊泛函除外）；用广义 Koopmans 定理对结合能做整体位移后再与实验比；PES 界面只能用 eV 单位和高斯展宽 |
| Raman 活性不等于 Raman 强度，直接展宽活性画出的不是实验谱 | [sec-3-13-plotting-spectra.md](sec-3-13-plotting-spectra.md) | 强度依赖入射光波数 ν0 与温度，须按手册换算式把 Si 换算为 Ii 后再画，Raman/ROA 配 PVS-NC 曲线时也要先换算 |
| 荧光只取 S1、磷光只取 T1，且几何必须用对应激发态优化结构 | [sec-3-13-plotting-spectra.md](sec-3-13-plotting-spectra.md) | 违背 Kasha 规则的体系除外；磷光必须考虑自旋-轨道耦合，否则振子强度 f 为零，画出来是空谱 |
| ORCA 做 TDDFT 默认用 TDA，振子强度和旋光强度明显差于标准 TDDFT | [sec-3-13-plotting-spectra.md](sec-3-13-plotting-spectra.md) | 画 UV-Vis/ECD 前在输入里加 `TDA false` 关掉 TDA；ORCA 的 ECD 旋光强度用的是长度表象 |
| xtb 算的 IR 强度质量不好 | [sec-3-13-plotting-spectra.md](sec-3-13-plotting-spectra.md) | 频率尚可，强度不可信；要发表的 IR 对比用 DFT 级别重算强度 |
| NMR 化学位移的参比与样品必须在完全相同计算设置下得到 | [sec-3-13-plotting-spectra.md](sec-3-13-plotting-spectra.md) | 方法、基组、溶剂模型任一不同，δ = σ(ref) − σ 就无意义；多体系叠加画 NMR 还要求所有体系原子数相同 |
| 多体系加权画图的图例若全由数字组成会被当成权重 | [sec-3-13-plotting-spectra.md](sec-3-13-plotting-spectra.md) | 数字图例前加 `$`（如 `$50` 显示为 50）；Linux 下 `multiple.txt` 里含 `/` 或空格的路径须加双引号 |
| Poincaré-Hopf 关系不满足必定漏了临界点，但满足也不保证找全 | [sec-3-14-topology-analysis.md](sec-3-14-topology-analysis.md) | 缺点就换不同起始点继续搜；ELF/LOL/拉普拉斯等比电子密度复杂得多，务必用球内随机模式（选项 -1 逐原子）反复搜多次 |
| 模式 6 搜到的临界点序号每次运行都可能不同 | [sec-3-14-topology-analysis.md](sec-3-14-topology-analysis.md) | 起始点随机；写脚本或记录时不要硬编码 CP 序号，每次重搜后先可视化确认索引 |
| 拓扑功能 7 默认计算所有临界点处的 ESP，耗时极大 | [sec-3-14-topology-analysis.md](sec-3-14-topology-analysis.md) | 不关心 ESP 时把 `settings.ini` 里 `ishowptESP` 设为 0 跳过；从外部导入临界点时文件格式必须与子选项 4 导出的 `CPs.txt` 完全相同 |
| 周期体系临界点搜索模式 3 与模式 4/5 循环的原子范围不同 | [sec-3-14-topology-analysis.md](sec-3-14-topology-analysis.md) | 模式 3 同时循环实际原子和镜像原子，模式 4/5 只循环实际原子；周期体系选错模式会漏（或重搜）镜像区临界点 |
| 分子表面 ESP 拟合关系式的系数依赖计算级别，不可跨级别套用 | [sec-3-15-quantitative-analysis-of-molecular-surface.md](sec-3-15-quantitative-analysis-of-molecular-surface.md) | 如升华热拟合用 B3LYP/6-31G* 优化 + B3LYP/6-311++G(2df,2p) 算 ESP，换级别须重拟合；晶体密度公式仅适用于 C/H/N/O 小有机物，其它体系误差极大 |
| 球形度不适用于有空腔的体系 | [sec-3-15-quantitative-analysis-of-molecular-surface.md](sec-3-15-quantitative-analysis-of-molecular-surface.md) | 如 C60 球心有空腔（等值面），算出的球形度无意义；分子表面原子局域划分本身也不唯一，按手册权重规则理解即可 |
| 大体系 ESP 直接算太慢可用原子电荷近似，但电荷必须同水平产生；格点间距太大漏极值点 | [sec-3-15-quantitative-analysis-of-molecular-surface.md](sec-3-15-quantitative-analysis-of-molecular-surface.md) | 选 Electrostatic potential from atomic charges 并提供同水平算的 `.chg`；默认间距一般可靠，丢极值点时先调小间距；FPA 的三个波函数文件几何必须完全相同；重复分析同一体系先用后处理选项 7 导出 `vtx.txt` 复用 |
| 格点数据之间做运算，要求原点、平移矢量、各维度格点数完全一致 | [sec-3-16-processing-grid-data.md](sec-3-16-processing-grid-data.md) | 不一致先重采样到同一格点设置再运算；把另一 cube 值映射到等值面的功能精度不如主功能 12，后者优先 |
| AdNDP 不是黑箱，搜索与挑选任意性大；选 -10 回主菜单则全部结果丢失 | [sec-3-17-adaptive-natural-density-partitioning-analysis.md](sec-3-17-adaptive-natural-density-partitioning-analysis.md) | 最终剩余密度尽量低、占据数尽量接近 2.0、中心数尽量少、轨道须符合分子对称性；中途退出等于重置，挑选完先导出/存盘 |
| Gaussian 做 AdNDP 输入要求严格：`pop=nboread` 加 `$NBO AONAO DMNAO $END`，再 `formchk` 转 `.fch` | [sec-3-17-adaptive-natural-density-partitioning-analysis.md](sec-3-17-adaptive-natural-density-partitioning-analysis.md) | 缺 AONAO 则不能可视化/导出 cube；独立 GENNBO 须在 `.47` 的 `$NBO` 段加 `DMNAO`，且同样不可视化；要轨道能量须另供下三角 Fock 矩阵文本 |
| 进 AdNDP 模块就崩溃且基组含弥散函数，换无弥散基组重算 | [sec-3-17-adaptive-natural-density-partitioning-analysis.md](sec-3-17-adaptive-natural-density-partitioning-analysis.md) | 这是 NBO 3.1 在极少数情况下对弥散函数的 DMNAO 输出 bug；AdNDP 对弥散函数不敏感，去掉不损失精度 |
| PDI/PLR/FLU 只适用于闭壳层，环原子须按连接顺序输入；平面体系分 α/π 须先清零另一类 MO | [sec-3-18-fuzzy-atomic-space-analysis.md](sec-3-18-fuzzy-atomic-space-analysis.md) | 顺序错则环不闭合结果错；用主功能 6 选项 26（或主功能 100 选项 22）把非 π（非 α）MO 占据数置零后再算 PDI-π/PLR-π；FLU-π 需先看轨道等值面确认 π 轨道序号 |
| 算 CLRK/LRK 必须用含虚轨道信息的文件（`.mwfn` / `.fch` / `.molden` / `.gms`），且只适用于 HF/DFT 闭壳层 | [sec-3-18-fuzzy-atomic-space-analysis.md](sec-3-18-fuzzy-atomic-space-analysis.md) | 默认最高虚轨道不参与（`settings.ini` 里 `ispecial`=3 才计入全部）；原子极化率/C6 的 ρ 与 ρ(free) 须同一水平计算，Hirshfeld 权重用的球化原子密度与算 V(free) 的那套无关 |
| CDA 四条输入铁律：方法基组相同、坐标完全一致、原子顺序可拼接、尽量不用弥散函数 | [sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md) | 片段必须从优化好的复合物几何截取做单点，绝不能各自优化；混合基组下片段与复合物对应部分基组一一相同；有弥散函数时 CDA 常不合理甚至无意义 |
| Gaussian 做 CDA 必须 `nosymm`，输出文件做 CDA 必须 `nosymm pop=full`（复合物另加 `IOp(3/33=1)`，笛卡尔坐标） | [sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md) | 默认标准取向会转掉坐标导致要求 (2) 破坏；混合基组（尤其 Pople 基）片段计算加 `5d`；基函数数≠轨道数加 `IOp(3/32=2)`；post-HF 闭/开壳分别用 `density pop=NO` / `density pop=NOAB` 输出自然轨道 |
| 限制性开壳层文件做 CDA 数据完全错误；ECDA 禁 post-HF、多于两片段、SCPA 组成 | [sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md) | ROHF 会被按闭壳层处理，只有轨道相互作用图可用，须先转成等价非限制开壳层；开壳层片段须翻转其中一片自旋使 α/β 总数与复合物一致；Mulliken 组成偶发小负值或略超 100% 直接视为 0/100%，高能虚轨道的 SCPA 组成也可能不合理 |
| basin 积分用的格点设置必须与生成 basin 的格点严格一致；格点排布与对称性不对易，对称性要求高须用精细格点 | [sec-3-20-basin-analysis.md](sec-3-20-basin-analysis.md) | 全体系定性用中等格点、高精度积分用高质量格点；“未归属/travelled to boundary”格点多在远离原子的不重要区域，可忽略 |
| 核附近剧变函数禁只用均匀格点直接积 AIM basin；BOM 用电子密度定 basin 时选混合格点 | [sec-3-20-basin-analysis.md](sec-3-20-basin-analysis.md) | 拉普拉斯、动能密度、source function 在核区涨落剧烈，用选项 7 的原子中心+均匀混合格点；选项 3/4/5/7/8 若输入无 GTF（如 `.cub`）须另供含 GTF 的文件 |
| 用了 ECP 又没让程序补 EDF（`isupplyEDF`）时价区冒出大量假吸引子；赝势元素定不了 ELF basin 标签 | [sec-3-20-basin-analysis.md](sec-3-20-basin-analysis.md) | 进选项 7/8 前先用选项 -6 子选项 3 把假吸引子手动聚为一个；赝势体系须可视化吸引子/空间范围手动定标签；basin 模块吸引子精度受格点限制且只找 (3,-3)，要全类型 CP 精确坐标用主功能 2 |
| Gaussian 做激发分析必须加 `IOp(9/40=4)`，ORCA CIS/TDA 必须加 `TPrint 1E-8` | [sec-3-21-electron-excitation-analysis.md](sec-3-21-electron-excitation-analysis.md) | 默认只打印系数 >0.1（ORCA 只印极少量），精度不够；嫌贵可用 `IOp(9/40=3)`；Firefly 调小 `$TDDFT` 的 `PRTTOL`；GAMESS-US 无阈值选项、结果可能不准且不支持 CIS；优化+频率输出不支持 |
| ORCA 标准 TDDFT 系数不在 `.out` 里，须配同名 `.json`；CP2K 的 `.molden` 虚轨道须覆盖组态涉及的虚轨道 | [sec-3-21-electron-excitation-analysis.md](sec-3-21-electron-excitation-analysis.md) | 先建 `TDDFT.json.conf` 写 CIS/CISNRoots 再跑 `orca_2json` 得 `TDDFT.json` 放同目录；虚轨道数未知就一次设足够大（文件大）或先跑一次看最高虚轨道再重算；两份输入文件几何与水平不一致则结果无意义 |
| ORCA sTDA/sTDDFT 只打印三个最大系数，归一化常被破坏 | [sec-3-21-electron-excitation-analysis.md](sec-3-21-electron-excitation-analysis.md) | `TPrint` 对此无效；务必看载入激发态后屏幕的 Deviation to expected normalization value，偏大则分析不可靠甚至误导；自旋翻转 TDDFT 只有空穴-电子等少数功能正式支持，基于跃迁密度矩阵的分析（含 NTO）不支持 |
| 空穴-电子 Mulliken 划分与弥散函数不兼容；Gaussian 默认激发态密度是弛豫密度 | [sec-3-21-electron-excitation-analysis.md](sec-3-21-electron-excitation-analysis.md) | 阴离子/Rydberg 激发或出现明显原子负贡献时换 Hirshfeld 划分（小负贡献置零）；要与 Gaussian 激发态减基态的 Δρ 对上，须加 `density=rhoci` 用未弛豫密度；手写纯文本输入闭壳系数平方和按 Gaussian 惯例为 0.5，ORCA 系 MO 编号从 0 起须手动加 1 |

## 高级功能
| 注意/问题 | 出处 | 说明与解法 |
|---|---|---|
| 含弥散函数时 PM-Mulliken / PM-Löwdin 可能失效 | manual_md_zh/sec-3-22-orbital-localization-analysis.md | 弥散函数破坏 Mulliken / Löwdin 布居意义；电子结构不需要弥散时去掉弥散，或改用更稳健但贵得多的 PM-Becke；FB 也兼容弥散但双键变香蕉键且不保持 σ-π 分离 |
| 无特殊原因只定域化占据轨道 | manual_md_zh/sec-3-22-orbital-localization-analysis.md | 非占据轨道收敛更难、数量多得多，耗时剧增；只有占据轨道携带电子结构有用信息；选项 1 只定域化占据 MO |
| PM-Becke 绝不要用于大体系 | manual_md_zh/sec-3-22-orbital-localization-analysis.md | PM-Becke 在 6-31G* 下对 C60 已极其昂贵；代价排序 PM-Becke >> FB（正比 N_orb²N_bas²）> PM-Mulliken/Löwdin（正比 N_orb²N_bas）；2-zeta 加极化基组已完全足够，更大基组无可察觉改善 |
| 生成 LMO 中心后不要再做波函数分析 | manual_md_zh/sec-3-22-orbital-localization-analysis.md | LMO 中心以 Bq 幽灵原子加入体系且无基函数，此时再做波函数分析会导致崩溃或完全无意义的结果 |
| 不要把 LMO 偶极矩 d 直接加和当体系偶极矩，也不要用 D_i 度量 LMO 极性 | manual_md_zh/sec-3-22-orbital-localization-analysis.md | 所有 d 之和一般不等于体系偶极矩；D_i 含参考点贡献，须用相对于恰当 r_c 的 d_i 讨论极性（单中心取最大贡献原子位置，双中心取共价半径加权成键区中心） |
| NCI 用于大体系（约 300 原子以上）直接算波函数不可行 | manual_md_zh/sec-3-23-visual-study-of-weak-interaction.md | 改用前分子近似 NCI、IGM / mIGM，或用 xtb 半经验算出 .molden 再做 NCI，结果好于前分子近似 |
| NCI 波函数不需要大基组和高精度方法 | manual_md_zh/sec-3-23-visual-study-of-weak-interaction.md | def2-SVP / 6-31G** 加 B3LYP / M06-2X 已完全足够；post-HF 密度提升在 NCI 图中几乎察觉不到，B3LYP 算不准相互作用能不代表密度不够用 |
| NCI 图被不感兴趣区域的多余等值面污染 | manual_md_zh/sec-3-23-visual-study-of-weak-interaction.md | 用筛除局域等值面方法屏蔽，或改用 IGM 并恰当定义片段，可完全避免该问题 |
| 大体系即使 high-quality 格点图形仍有锯齿空洞 | manual_md_zh/sec-3-23-visual-study-of-weak-interaction.md | low/medium/high-quality 格点是相对中小体系而言的；大盒子下改用手动输入格点数或格点间距，保证间距足够小并让盒子刚好包住感兴趣区域 |
| RDG 格点数据经选项 -2 修改后无法恢复 | manual_md_zh/sec-3-23-visual-study-of-weak-interaction.md | 把指定 sign(λ2)ρ 范围的 RDG 设大值屏蔽前先导出 cube 备份，否则改错只能重算 |
| 一般不要用 aNCI，用 amIGM 代替 | manual_md_zh/sec-3-23-visual-study-of-weak-interaction.md | amIGM 可定义片段、等值面更光滑，有时 aNCI 完全失败而 amIGM 仍合理；aNCI 强制前分子近似、一般至少 500 帧，且轨迹中感兴趣分子坐标须固定并远离盒子边界 |
| 不要用 DORI，用 IRI | manual_md_zh/sec-3-23-visual-study-of-weak-interaction.md | IRI 只需密度梯度（DORI 还需 Hessian），更便宜且图形效果显著更好 |
| IGM / IGMH / mIGM 选型错误或几何未优化 | manual_md_zh/sec-3-23-visual-study-of-weak-interaction.md | 几何必须先合理优化否则结果误导；负担得起永远用 IGMH 代替 IGM；无波函数或太贵时用 mIGM 代替 IGM；aIGM 无用，永远用 amIGM 代替 |
| EDA-FF 片段与分子列表文件定义错误 | manual_md_zh/sec-3-24-energy-decomposition-analysis.md | 任一原子不得同时属于两个片段；分子内两片段间须相隔至少三个化学键；分子列表文件中原子顺序须与载入几何完全一致，否则电荷类型指派全错 |
| EDA-FF 力场与电荷选错 | manual_md_zh/sec-3-24-energy-decomposition-analysis.md | 有机体系用 AMBER/GAFF，一般不用 UFF（高估排斥，总相互作用能常为正）；缺参数元素把原子类型写作 UF 以借用 UFF 参数；电荷须用复现 ESP 的 CHELPG（太大体系用 EEM），不要用 Mulliken 类电荷 |
| 色散能分析误用 DFT-D4 或官方 dftd3 | manual_md_zh/sec-3-24-energy-decomposition-analysis.md | Multiwfn 目前仅支持基于 B3LYP 拟合参数的 DFT-D3(BJ)；须用 Tian Lu 修改版 dftd3 并在 settings.ini 设 dftd3path，Linux 下记得 chmod 加可执行权限 |
| CDFT 的 N / N+1 / N-1 文件几何或级别不一致 | manual_md_zh/sec-3-25-conceptual-density-functional-theory-analysis.md | 三个态几何必须相同且均为 N 态优化几何、计算级别相同，否则电离势、亲和势、Fukui 函数全错 |
| 换级别后直接沿用默认亲核性指数 | manual_md_zh/sec-3-25-conceptual-density-functional-theory-analysis.md | 默认 TCE 的 HOMO 能量是 B3LYP/6-31G* 下的 -0.335198 Hartree；非该级别须自己重算 TCE 再手动修正亲核性指数及其局域版本 |
| 涉及虚轨道的 CDFT 量用了弥散函数 | manual_md_zh/sec-3-25-conceptual-density-functional-theory-analysis.md | 轨道加权 Fukui / 对偶描述符、超离域性 D_N 与 D_N0 利用虚轨道，弥散函数会严重损害虚轨道化学意义，此时不应使用弥散函数 |
| 凝聚轨道加权 Fukui 求和明显偏离 1.0 | manual_md_zh/sec-3-25-conceptual-density-functional-theory-analysis.md | 默认积分格点不够密；把 settings.ini 的 iautointgrid 设 0 再增大 radpot 与 sphpot |
| 简并体系仍用默认 p=q=1 或自旋多重度设错 | manual_md_zh/sec-3-25-conceptual-density-functional-theory-analysis.md | 先用选项 -3 按 MO 能量定 p、q；N+p / N-q 态多重度通常设 p+1 / q+1；基于密度的 f_Q 与 Δf_Q 仅对闭壳层定义 |
| 算不出 ω_cubic 与 ε | manual_md_zh/sec-3-25-conceptual-density-functional-theory-analysis.md | 二者依赖 N-2 态，默认不算；须先选项 -1 切 Yes 再准备 N、N+1、N-1、N-2 四个 .wfn 文件 |
| Fukui 势格点（选项 9）算得极慢 | manual_md_zh/sec-3-25-conceptual-density-functional-theory-analysis.md | 每个带电态都要算 ESP 格点，开销大，格点设置应保守，避免过于耗时 |
| DDD 的 AOM 只含占据轨道 | manual_md_zh/sec-3-25-conceptual-density-functional-theory-analysis.md | 用模糊或盆模块导出全 MO 的 AOM 前，先把 settings.ini 的 ispecial 设 3，否则 AOM 只涉及占据轨道 |
| ETS-NOCV 用了不支持的波函数或文件 | manual_md_zh/sec-3-26-ets-nocv-analysis.md | 仅 HF / KS-DFT，不支持耦合簇、CASSCF、双杂化与多组态；仅限制闭壳与非限制开壳，不支持限制开壳；文件须含基函数（.fch / .mwfn / .molden），.wfn / .wfx 不能用 |
| ETS-NOCV 片段与复合物设置不一致 | manual_md_zh/sec-3-26-ets-nocv-analysis.md | 片段计算水平须与复合物完全相同；片段原子顺序与复合物一致且每个片段原子连续出现；Gaussian 片段单点加 nosymm 防重定向；无特殊理由不用弥散（SCPA 组成与弥散不兼容）；避免隐式溶剂 |
| 把 Multiwfn 的 NOCV 能量当严格 ETS-NOCV 能量 | manual_md_zh/sec-3-26-ets-nocv-analysis.md | 程序内拿不到 F^TS，只能用实际 Fock 矩阵近似（载入或 F=SCEC^-1 生成），全部 NOCV 能量之和不严格等于 ΔE_orb，只能定性判断主导 NOCV 对 |
| 对称体系 NOCV 配对不符合预期 | manual_md_zh/sec-3-26-ets-nocv-analysis.md | 简并 NOCV 本征值排序任意导致自动配对错误（如直线型 Ne...BeO），用选项 -6 手工重定义配对与轨道对应关系 |
| Gaussian polar 输出 Multiwfn 解析失败或只拿到静态量 | manual_md_zh/sec-3-27-hyperpolarizability-analysis.md | 路线部分必须写 #P；要 β(-2ω;ω,ω) 必须用 polar=DCSHG；解析频域量前先用选项 -1 切换，再选频率 |
| 自行处理 Gaussian 超极化率分量符号错误 | manual_md_zh/sec-3-27-hyperpolarizability-analysis.md | Gaussian 输出的超极化率分量符号众所周知是反的（须乘 -1），Multiwfn 已自动处理，绕开 Multiwfn 直接引用时记得翻转 |
| SOS 输入文件类型与目标量不匹配 | manual_md_zh/sec-3-27-hyperpolarizability-analysis.md | Gaussian 激发输出文件只能算 α（缺全部跃迁偶极矩）；算 β / γ / δ 必须用含激发能与跃迁偶极矩的纯文本文件；实际用最低 60-120 个态通常已够，大体系 ab initio 求大量激发态很贵，导数法可行时不用 SOS |
| （超）极化率密度有限差分场强随意取值 | manual_md_zh/sec-3-27-hyperpolarizability-analysis.md | 场强太大太小都引入显著数值误差，经验好选择是 0.003 a.u.；真正感兴趣常是偶极方向分量，计算前先把偶极矩重取向到某笛卡尔轴（如 Z） |
| HRS 退偏比 DR 低于 1.5 误判为算错 | manual_md_zh/sec-3-27-hyperpolarizability-analysis.md | 入射光半波长接近同水平 TDDFT 吸收带时会发生 SHG 共振导致 DR 偏低；Td 点群正常值恰为 1.5，对照时须排除共振 |
| ICSS 的 Gaussian 任务设置或复用旧数据出错 | manual_md_zh/sec-3-28-electron-delocalization-and-aromaticity-analyses.md | 模板 .gjf 必须显式写 %chk；NICS0001.gjf 必须先运行；复用已有 NMR 输出时格点设置须与当初完全一致；G09 D.01 / E.01 模板加 guess=huckel（Link 401 报错改 guess=core），其他版本与 G16 不加 |
| HOMA 原子顺序错误或公式引用错误 | manual_md_zh/sec-3-28-electron-delocalization-and-aromaticity-analyses.md | 输入环原子序号必须按连接顺序；HOMA 公式被众多论文误引，以手册为准；判断 S0 芳香性推荐用 HOMAc 代替 HOMA |
| FiPC-NICS 算不出来 | manual_md_zh/sec-3-28-electron-delocalization-and-aromaticity-analyses.md | 仅扫描路径平行于笛卡尔轴时才能计算 FiPC-NICS；非对称体系 NICS(1)zz 与 NICS(-1)zz 不同，通常意义值取二者平均 |
| 散点图几乎看不到点 | manual_md_zh/sec-3-100-other-functions-part-1.md | Multiwfn 按最值自动定坐标轴范围，有时须用选项 4 / 5 手工重置范围；选项 -2 / -3 修改格点数据后无法恢复，先备份 |
| 组合碎片波函数做初猜的 gjf 必定失败 | manual_md_zh/sec-3-100-other-functions-part-1.md | 把轨道系数写入输入文件时，必须手工指定与原波函数相同的基组；碎片计算须加 nosymm 与 pop=full |
| SCF 收敛监控无数据或能量分解用了老方法 | manual_md_zh/sec-3-100-other-functions-part-1.md | 监控 SCF 须 Gaussian 路线写 #P 才会记录中间信息；不要再用 3.100.7 老能量分解，改用 sobEDA / sobEDAw |
| π 轨道识别结果无意义或联用失败 | manual_md_zh/sec-3-100-other-functions-part-1.md | 识别 π 组成默认 Mulliken+SCPA 时绝不能用弥散函数；Foster-Boys 的 LMO 混成香蕉键不能联用，必须用 Pipek-Mezey 定域的 LMO |
|  counterpoise / Fock 矩阵相关计算结果错误 | manual_md_zh/sec-3-100-other-functions-part-1.md | 二聚体与单体三次计算基组须相同、坐标与原子顺序一致，且先载体 A 再载 B；Gaussian 输出做输入不推荐（精度低），须 IOp(3/33=1) nosymm guess=only；F=SCEC^-1 的 Fock 精度低于原程序；线性依赖删基后该功能不可用 |
| CVB 指数与文献对不上，π 氢键算不出 | manual_md_zh/sec-3-200-other-functions-part-2.md | ELF(C-V) 定义含糊、文献规则不一，跨文献对比无意义；受体非单原子（如乙烯 π 区）的 π 氢键必须手动计算 CVB |
| 轨道重叠展开积分不可靠或巨耗时 | manual_md_zh/sec-3-200-other-functions-part-2.md | 两波函数原子分布范围差别大则积分精度必然低；代价正比于轨道数，轨道很多时不要一次全选；提高精度把 settings.ini 的 iautointgrid 设 0 再增大 radpot / sphpot / radcut |
| 轨道对 Δρ 贡献分解爆内存或结论随意 | manual_md_zh/sec-3-200-other-functions-part-2.md | 轨道范围选择高度任意且明显影响结果；轨道多加格点密时基于内存模式易爆内存，改用基于 cube 文件模式；自动算的轨道密度格点与载入 Δρ 格点严格相同 |
| SNO 载入后看错轨道，BLA / BOA 全错 | manual_md_zh/sec-3-200-other-functions-part-2.md | 含 SNO 的 .mwfn 载入后体系视为开壳，只有 alpha 轨道对应 SNO，beta 无意义须忽略；Mayer 键级与弥散函数不兼容，BLA / BOA 波函数不能带弥散 |
| STM 图像算不出或误读 | manual_md_zh/sec-3-300-other-functions-part-3.md | .wfn 无虚轨道不能模拟 V>0；只支持 HF / KS-DFT（双杂化与多组态不支持）；恒流模式比恒高耗时多；针尖被简化为点，图像只有相对差异有意义，不能与实验严格比较 |
| 原子密度拟合不收敛或自由体积结果失真 | manual_md_zh/sec-3-300-other-functions-part-3.md | 拟合函数超过约 20 个时不要同时拟合指数与系数；自由体积考虑周期边界更真但贵得多；分子表面距离投影的体系取向是用户责任 |

## 基础实例
| 注意/问题 | 出处 | 说明与解法 |
|---|---|---|
| 需要基函数信息的功能误用 .wfn/.wfx 作输入 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) | 仅基于实空间函数的分析可用 .wfn/.wfx；需要基函数信息时必须用 .mwfn、.fch/.fchk、.molden 或 .gms，少数特殊功能（AdNDP、ICSS 等）按第 3 章要求准备特殊文件 |
| Gaussian 做 post-HF 导出 .wfn 未加 density，得到的是 HF 轨道 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) | post-HF 方法必须在 route section 加 `density` 关键词才使用当前密度，否则 .wfn 里仍是 HF 轨道 |
| TDDFT/CIS 想导出激发态自然轨道到 .wfn 却得到基态轨道 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) | 同样需指定 `density` 关键词，才能导出与激发态波函数对应的自然轨道 |
| 非限制性参考的 CCD/CCSD、QCISD、MP2/3、MP4SDQ 导出的 .wfn 不是自然自旋轨道 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) | 必须同时指定 `pop=NOAB`，存入 .wfn 的才是自然自旋轨道而非空间自然轨道；Gaussian 的 TD、CI、MCSCF 任务给不出自然自旋轨道 |
| 老版本 Gaussian 的 ROHF/RODFT 的 .wfn 单占据轨道占据数被写成 2.0 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) | 早于 G09 B.01 有此严重 bug，用文本编辑器打开 .wfn，找到最后一处 `OCC NO =`，手动把其后的值改为 `1.0000000` |
| Gaussian 做 MCSCF 导出 .wfn 未得到自然轨道 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) | 须再加 `pop=no` 关键词才能把自然轨道生成并导出到 .wfn |
| ORCA 用 ECP 时生成不了 .wfn/.wfx | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) | 至少 ORCA 4.1 在 ECP 下无法生成 .wfn/.wfx，改用 `orca_2mkl XX -molden` 生成 .molden 作输入，总体也更推荐 .molden |
| post-HF 或 TDDFT 的 .fch 默认记录的是 HF 或基态 DFT 轨道，分析结果与 HF/基态相同 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) | 用主功能 200 子功能 16 由 Multiwfn 生成自然轨道（推荐），或带 `density` 算完再以 `guess (save,only,naturalorbitals) chkbasis` 重跑让 Gaussian 写自然轨道，并在 .fch 第一行写 `saveNO`；开壳层 post-HF 即使如此也存不进正确的自然自旋轨道，此时改用 .wfn/.wfx 看自然轨道和分析实空间函数 |
| MCSCF 的 .fch 在多重度大于 1 时载入后轨道套数不对 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) | 先载入 .fch 用主功能 200 子功能 16 生成含 MCSCF 自然轨道的 .molden 再作输入；因 MCSCF 给不出分开的 alpha/beta 轨道，须手动把 .fch 中 `Number of beta electrons` 改为与 `Number of alpha electrons` 相同 |
| 老版本 Q-Chem 的 .fchk 载入 Multiwfn 失败或读错 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) | 版本相当老（可能 ≤5.0）时先把 `settings.ini` 中 `ifchprog` 设为 2 再载入；新版 PSI4 的 .fchk 才与 Multiwfn 兼容 |
| NWChem 生成的 .molden 载入后出错或结果不对 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) | 必须用球谐基函数（`spherical` 关键词），且体系有对称性时必须用 `noautosym` 关键词 |
| 用赝势的 .molden 做与核电荷有关的分析结果不对 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) | 手动把 .molden 文件中的原子序号改为核电荷，细节见 2.5 节 |
| 非官方支持程序生成的 Molden 文件分析结果时对时错 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) | 正式支持的只有 Molpro、ORCA、xtb、Dalton、NWChem、MRCC、deMon2k、BDF；其它程序先用 molden2aim 工具标准化后再载入 |
| GAMESS-US/Firefly 输出改后缀 .gms 后载入失败 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) | 只保证默认 NPRINT 下 HF/DFT 计算的输出可正常载入，其它情形不保证 |
| Linux 版主功能 0 里鼠标拖不动体系 | [sec-4-0-view-orbitals-and-structure.md](sec-4-0-view-orbitals-and-structure.md) | 先在绘图区单击一次使图标变为手形，再按住左键旋转、Ctrl+左键旋转/缩放、Shift+左键平移 |
| 开壳层体系在主功能 0 选不到 beta 轨道 | [sec-4-0-view-orbitals-and-structure.md](sec-4-0-view-orbitals-and-structure.md) | beta 轨道输负序号，如 `-5` 对应第 5 个 beta 轨道；R/U/RO 波函数也可用 `h`、`l+2`、`la`、`hb-3` 等标记选轨道 |
| Rydberg 轨道等值面被截断、显示不全 | [sec-4-0-view-orbitals-and-structure.md](sec-4-0-view-orbitals-and-structure.md) | Rydberg 轨道很弥散，先在 Other settings 用 Set extension distance 输入较大值（如 `12` Bohr，默认由 `settings.ini` 的 `Aug3D` 控制）再可视化 |
| 非限制性计算的 NBO plot 结果 странный（.32/.33 载入异常） | [sec-4-0-view-orbitals-and-structure.md](sec-4-0-view-orbitals-and-structure.md) | Gaussian 内 NBO 3.1 输出的 .32 和 .33 文件头缺失，参照 .34 等其它 plot 文件手动修复标题部分即可 |
| .fch 存的 NBO 序号与 NBO 模块输出对不上 | [sec-4-0-view-orbitals-and-structure.md](sec-4-0-view-orbitals-and-structure.md) | Gaussian 存 checkpoint 时会自动重排 NBO，以输出文件 `Reordering of NBOs for storage:` 一行为准对照 |
| .fch 作 NBO 载体时能量/占据数显示不对 | [sec-4-0-view-orbitals-and-structure.md](sec-4-0-view-orbitals-and-structure.md) | HF/DFT 任务在 .fch 第一行加 `saveNBOene`，post-HF 加 `density` 的任务加 `saveNBOocc`；若只在主功能 0 看图可忽略此步 |
| VMD 联用脚本对大体系格点不够、Rydberg 图被截断 | [sec-4-0-view-orbitals-and-structure.md](sec-4-0-view-orbitals-and-structure.md) | 大体系（约一百原子以上）把 `showorb.txt` 第四行设为 `3` 切 high-quality grid；Rydberg 在第三、四行之间加 `-10`、`12` 两行把延伸距离提到 12 Bohr；高质量渲染请用 VMD 1.9.3 |
| 旧版 G09 做 post-HF 的 .wfn 密度仍是 HF 密度 | [sec-4-1-calculate-properties-at-a-point.md](sec-4-1-calculate-properties-at-a-point.md) | 必须加 `density` 关键词；且 G09/G16 在 MP4 级别产不出密度，改用 `MP4(SDQ)` 关键词 |
| 照搬文献拟合式由核处 ESP 预测相互作用能，换级别后偏差大 | [sec-4-1-calculate-properties-at-a-point.md](sec-4-1-calculate-properties-at-a-point.md) | 该式在特定级别下拟合（MP4(SDQ)/aug-cc-pVTZ//MP2/6-311++G**），换级别须重拟合；省时间可用 MP2/aug-cc-pVDZ，其 ΔΔVn 与高级别值接近 |
| 用 V(r_BCP)/2 估算 X-H…O 氢键键能 | [sec-4-2-topology-analysis.md](sec-4-2-topology-analysis.md) | 该流行式误差明显更大，不推荐；用 J. Comput. Chem. (2019) 论文严格验证的预测方程 |
| 预期存在的临界点搜不到 | [sec-4-2-topology-analysis.md](sec-4-2-topology-analysis.md) | 先用选项 2~5，若仍缺用选项 6 的子选项 -1（每原子周围默认撒 1000 起始点），可重复几次；再找不到多半是搜索参数不合适而非起点问题 |
| 远离体系处出现零星临界点 | [sec-4-2-topology-analysis.md](sec-4-2-topology-analysis.md) | 属数值噪声伪 CP，进选项 -1 子选项 8 把判据增大几个数量级（如 `1E-15`）再按常规搜索 |
| 赝势体系找不到核处 (3,-3)、键径连不到核、核周围冒出大量怪 CP | [sec-4-2-topology-analysis.md](sec-4-2-topology-analysis.md) | 须提供 EDF（内核电子密度）信息：Gaussian 的 .wfx 默认载入 EDF 场，其它格式 Multiwfn 从内置库自动载入；此时全部 CP 正常，大核赝势可用但小核精度更好；若关掉 EDF（`settings.ini` 的 `readEDF`/`isupplyEDF`）则忽略核区伪 CP 只看真正感兴趣的 BCP；全电子方案用 DKH2 加 DK 优化基组（如 `cc-pVDZ-DK`，Gaussian 加 `int=DKH2`） |
| LOL/ELF 的临界点搜不全就反复重算 | [sec-4-2-topology-analysis.md](sec-4-2-topology-analysis.md) | LOL 分布复杂难找全，找到感兴趣的 CP 即可中止；选项 6 是随机撒点，每次 CP 编号都不同属正常；找 ELF/LOL 极大可用最速上升法专搜 (3,-3) |
| 关联空穴曲线 reference 位置对不上、开壳层自旋搞混 | [sec-4-3-output-and-plot-various-properties-in-a-line.md](sec-4-3-output-and-plot-various-properties-in-a-line.md) | 参考电子位置由 `settings.ini` 的 `refxyz` 决定，画前先改；`paircorrtype` 取 1/2/3 分别对应 Fermi/Coulomb/总关联空穴，开壳层用 `pairfunctype` 选自旋（闭壳层 alpha/beta 相同）；后 HF 近似空穴经 Müller 近似由自然轨道构造，至少定性正确 |
| 把 PAEM-MO 当通用成键判据 | [sec-4-3-output-and-plot-various-properties-in-a-line.md](sec-4-3-output-and-plot-various-properties-in-a-line.md) | PAEM-MO 误判水二聚体氢键为共价、多原子因占据轨道太多太复杂难用、原子太近恒判共价；HF 下 XC 势近似一般够用（`iuserfunc=33` 基于 Γ，`34` 用 DFT XC 势更快），但结论须谨慎 |
| 等值线图存成默认 png 后线条发虚、放大模糊 | [sec-4-4-output-and-plot-various-properties-in-a-plane.md](sec-4-4-output-and-plot-various-properties-in-a-plane.md) | 线条为主的图把 `settings.ini` 的 `graphformat` 改为 `pdf`，矢量格式无损缩放 |
| 平面图上部分原子标签/成键显示不出来 | [sec-4-4-output-and-plot-various-properties-in-a-plane.md](sec-4-4-output-and-plot-various-properties-in-a-plane.md) | 原子到平面垂直距离超过 `settings.ini` 的 `disshowlabel` 就不显示，用后处理选项 17 把阈值放大（如 `10` Bohr）并选 `y` 超阈值仍以细字显示 |
| 画变形密度/相对密度图时反复调用 Gaussian 现算原子波函数 | [sec-4-4-output-and-plot-various-properties-in-a-plane.md](sec-4-4-output-and-plot-various-properties-in-a-plane.md) | 把 `wfntmp` 中无数字后缀的原子 .wfn（如 `C .wfn`）拷到 `atomwfn` 文件夹复用；比 Kr 重的元素必须手动算好原子 .wfn 放入 `atomwfn` |
| 配合物相对单体的密度差值图出现莫名信号 | [sec-4-4-output-and-plot-various-properties-in-a-plane.md](sec-4-4-output-and-plot-various-properties-in-a-plane.md) | 只有片段坐标与复合物坐标完全一致时差值图才有意义，单体须直接取复合物坐标且全部加 `nosymm` 防 Gaussian 标准取向重定向 |
| 平面矢量图上电场箭头方向与直觉相反 | [sec-4-4-output-and-plot-various-properties-in-a-plane.md](sec-4-4-output-and-plot-various-properties-in-a-plane.md) | 电场是 ESP 的负梯度，箭头实际应反向读图 |
| 日常研究照 4.5.4 手工流程算 Fukui/对偶描述符，步骤繁琐 | [sec-4-5-generate-grid-data-and-view-isosurface-map.md](sec-4-5-generate-grid-data-and-view-isosurface-map.md) | 直接用主功能 22 自动算 Fukui 函数和对偶描述符，还附带一批 CDFT 量 |
| 算 Fukui 函数前优化了 N+1/N-1 态几何 | [sec-4-5-generate-grid-data-and-view-isosurface-map.md](sec-4-5-generate-grid-data-and-view-isosurface-map.md) | Fukui 定义偏导数要求核坐标（外势 ν）恒定，N±1 态必须用中性态几何做单点，绝不能重优化；B3LYP/6-31G* 是有意义结果的最低可接受水平 |
| 密度差值格点图符号/位置错乱 | [sec-4-5-generate-grid-data-and-view-isosurface-map.md](sec-4-5-generate-grid-data-and-view-isosurface-map.md) | Gaussian 默认把体系转到标准取向，片段与复合物取向不一致差值即错；多片段差值推广见 4.4.8 节做法 |
| 把 ELF/LOL 当各轨道贡献之和来分解 | [sec-4-6-modify-and-check-wavefunction.md](sec-4-6-modify-and-check-wavefunction.md) | ELF、LOL 相对轨道非线性，不可分解求和；电子密度、动能密度才可线性分解为轨道贡献；价层密度分析即把内层轨道占据数置零，闭壳层如 HCN 置零 MO 1、2，乙烷直接用主功能 6 选项 34 |
| 价层电子密度图中心白圈误读为 1s 电子 | [sec-4-6-modify-and-check-wavefunction.md](sec-4-6-modify-and-check-wavefunction.md) | 白圈是价层原子轨道向芯区穿透所致，不是内层电子 |
| 用主功能 6-32 平移复制原胞得到“周期”轨道/性质就当真 | [sec-4-6-modify-and-check-wavefunction.md](sec-4-6-modify-and-check-wavefunction.md) | 该超胞只是忽略相邻原胞轨道混合的粗糙近似，轨道波函数不忠实，仅中心区实空间函数有正确周期特征，边界仍错，需继续扩大；真做周期体系用 Multiwfn 联用 CP2K；PBC 未加 `nosymm` 时平移矢量以 .fch 的 `Translation vectors` 或输出文件的 `PBC vector` 为准 |
| Mulliken 布居/轨道成分用了弥散基函数还直接发表 | [sec-4-7-population-analysis-and-atomic-charge-calculation.md](sec-4-7-population-analysis-and-atomic-charge-calculation.md) | Mulliken 与弥散函数不兼容，结果毫无意义，须换 NAO、Hirshfeld 等方法或删弥散函数；轨道成分的 Mulliken 同理，且 Mulliken 对基组敏感 |
| 发表时用了未归一化的原子电荷，总和不等于净电荷 | [sec-4-7-population-analysis-and-atomic-charge-calculation.md](sec-4-7-population-analysis-and-atomic-charge-calculation.md) | 空间积分数值误差使总和偏离净电荷，研究和写文章一律用 `Final atomic charges`（归一化到实际电子数后）标签下的数据 |
| Hirshfeld-I 算不出或结果随手头文件漂移 | [sec-4-7-population-analysis-and-atomic-charge-calculation.md](sec-4-7-population-analysis-and-atomic-charge-calculation.md) | HI 需各元素不同带电态原子径向密度 .rad；最省事直接把 examples 下 `atmrad` 文件夹拷到当前目录用内建 .rad；要同水平自制 .rad 须先在 `settings.ini` 设好 `gaupath` 并删掉旧 `atmrad`，否则 Multiwfn 直接复用旧 .rad 不重算 |
| EEM 电荷载入 .fch/.wfn 失败，或共轭体系报键级 4 错误 | [sec-4-7-population-analysis-and-atomic-charge-calculation.md](sec-4-7-population-analysis-and-atomic-charge-calculation.md) | EEM 目前必须用提供连接信息的 .mol/.mol2 作输入；π 共轭须写成 Lewis 结构；GaussView 存 .mol 会把共轭键写成 4 重键，用 `obabel old.mol -O new.mol` 转换修复后再算 |
| 柔性分子只用单个构象拟合 RESP 就拿去做 MD | [sec-4-7-population-analysis-and-atomic-charge-calculation.md](sec-4-7-population-analysis-and-atomic-charge-calculation.md) | 多构象拟合时写 `conf.txt`（每行 `文件名 权重`，权重和须约等于 1）；只看权重 1.0 的构象会使其它构象 RMSE/RRMSE 恶化；只用单构象至少选自由能最低者；化学等价原子（如磷酸二甲酯两甲氧基）须写 `eqvcons.txt` 施加等价约束 |
| NAO 轨道成分分析用 .fch 作输入，或边优化边算 | [sec-4-8-molecular-orbital-composition-analysis.md](sec-4-8-molecular-orbital-composition-analysis.md) | NAO 矩阵 Multiwfn 自己产不出，必须用 NBO 输出（如 Gaussian `pop=nboread` 加 `$NBO NAOMO $END` 的 .out）作输入，绝不用 .fch；Gaussian 任务须为单点，不可同时做优化 |
| 用 NAO 方法分析虚轨道并发表原子贡献百分比 | [sec-4-8-molecular-orbital-composition-analysis.md](sec-4-8-molecular-orbital-composition-analysis.md) | Rydberg NAO 对虚轨道贡献显著且物理意义难解释，Rydberg 占比大（如 >10%）时重归一化也破坏意义；虚轨道改用 Hirshfeld/Becke 方法；占据轨道非 Rydberg 和不足 100% 时才可重归一化 |
| 指望 Hirshfeld/Becke 轨道成分给出 s/p/d 组成 | [sec-4-8-molecular-orbital-composition-analysis.md](sec-4-8-molecular-orbital-composition-analysis.md) | Hirshfeld/Becke 只能给原子或片段组成，给不出原子轨道组成；且 .wfn/.wfx 无虚轨道信息，做轨道成分优先用 .fch 等含虚轨道的文件 |
| Mayer/多中心键级用 .wfn 作输入算不出 | [sec-4-9-bond-order-analysis.md](sec-4-9-bond-order-analysis.md) | Mayer、多中心键级需要基函数信息，必须用 .mwfn/.fch/.molden/.gms；模糊键级和 LBO 不依赖基函数，可用 .wfn/.wfx；模糊键级更贵但基组敏感性低、有弥散也不变差 |
| 各轨道微扰贡献加和不等于 Mayer 键级，以为算错了 | [sec-4-9-bond-order-analysis.md](sec-4-9-bond-order-analysis.md) | Mayer 键级不是密度矩阵的线性函数，加和不等属正常，无需担心 |
| 阴离子/含弥散基组的多中心键级、AV1245/AVmin 结果离谱 | [sec-4-9-bond-order-analysis.md](sec-4-9-bond-order-analysis.md) | 此时必须转到 NAO 基（Gaussian 向 NBO 传 `DMNAO` 关键词，用其 .out 作输入）计算，否则结果完全无用或误导；无弥散时两种基结果一致 |
| 原子数不同的环直接比多中心键级/AV1245 原始值 | [sec-4-9-bond-order-analysis.md](sec-4-9-bond-order-analysis.md) | 原子数不同比归一化多中心键级；萘这类有原子同时连三个环原子的体系不可用 `d` 模式直接输 `1-10` 算全局 AV1245/AVmin，Multiwfn 无法自动定环顺序 |
| 纯几何文件算出的 IBSI 当高精度键强用 | [sec-4-9-bond-order-analysis.md](sec-4-9-bond-order-analysis.md) | .pdb/.xyz 等只有几何的输入默认得 IBSI^IGM；严格 IBSI 参考值应在与当前体系相同水平下计算，内置数据只是近似 |

## 光谱表面实例
| 注意/问题 | 出处 | 说明与解法 |
|---|---|---|
| 画 PDOS/OPDOS 误用 .wfn/.wfx 导致无数据 | sec-4-10-plot-density-of-states-dos-maps.md | PDOS/OPDOS 需要基函数与虚轨道信息，只能用 .fch/.mwfn/.molden/.gms 做输入；仅画 TDOS 时才可用记录 MO 能级的纯文本文件或带 pop=full 的 Gaussian 输出文件。 |
| 默认 Mulliken/SCPA 画 PDOS 时用了弥散函数，结果不可靠 | sec-4-10-plot-density-of-states-dos-maps.md | 弥散函数会严重损害 Mulliken/SCPA 轨道组成，非占据区尤其明显；改用 Hirshfeld 或 Becke 方法求轨道组成才可带弥散，但此时无法画 OPDOS。 |
| d 带中心随 X 轴能量范围变化，甚至出现非物理正值 | sec-4-10-plot-density-of-states-dos-maps.md | 只有当前 X 轴范围内的 PDOS 参与中心计算，能量范围必须完整包住 d 密度；扩展基组（如 Lanl2DZ）高能区（如 15~40 eV）的大 PDOS 是与价 d 正交的轨道所致，应排除，只取价 d 区（如 -13~0 eV）。 |
| 开壳层 DOS 只看一条自旋曲线就下结论 | sec-4-10-plot-density-of-states-dos-maps.md | 非限制开壳层须分别计算 alpha 与 beta，默认只考虑 alpha；要看 beta 时用选项 6 Choose orbital spin 切换后再画再导出。 |
| 谐振子频率直接与实验峰位对比，对不上 | sec-4-11-plot-various-kinds-of-spectra.md | 谐振近似频率系统性偏高，须用基频比例因子校正（如 B3LYP/6-31G* 取 0.9614），入口为选项 14 Set scale factor；可分批对不同模式设不同因子，选 n 保留已设效果再设下一批。 |
| multiple.txt 图例写纯数字，或 Linux 路径含 / 与空格导致读入失败 | sec-4-11-plot-various-kinds-of-spectra.md | 纯数字图例会被解释为构象权重，图例必须含非数字字符；Linux 下路径含 / 或空格时须在路径两端加双引号。 |
| 甲基三个 H 的 NMR 各自成峰，与实验不符 | sec-4-11-plot-various-kinds-of-spectra.md | 甲基旋转快，三个 H 只有一个峰，须用选项 10 Average shielding values of specific atoms 把甲基 H 屏蔽值平均后再定化学位移。 |
| Cs 对称分子的表面极值点 X/Y 坐标不对称，误以为算错 | sec-4-12-quantitative-analysis-of-molecular-surface.md | 表面散点本身不具有分子对称性，数值上无法精确对称，不是错误；用选项 3 Spacing of grid data 减小格点间距可改善，代价是计算量上升。 |
| 表面 ESP 极小值为正（或极大值为负），误以为程序 bug | sec-4-12-quantitative-analysis-of-molecular-surface.md | 极小/极大只是相对周围的高低，不要求为负/为正，中性体系中此类符号“反常”的极值化学上不重要，可用后处理选项 3/4 输入 d 删去；阳离子/阴离子因净电荷主导，极值通常全正/全负。 |
| 局域表面 ESP 平均出现 NaN，误以为程序出错 | sec-4-12-quantitative-analysis-of-molecular-surface.md | 某原子局域表面上全为负（或全为正）ESP 时，正（或负）部分的平均无法定义，NaN 是正常输出，可直接忽略。 |
| 用 ESP 全局最小点判断亲电位点、用 ALIE 判断亲核位点 | sec-4-12-quantitative-analysis-of-molecular-surface.md | 苯酚全局 ESP 最小点在 O 孤对附近，但 O 不是亲电位点，这是 ESP 方法的内在局限；ALIE 只对亲电/自由基进攻有指示意义，对亲核进攻完全无用，亲核位点应看 ESP 或局域表面平均。 |
| 用 density.cub + ESP.cub 做表面 ESP 分析结果不准 | sec-4-12-quantitative-analysis-of-molecular-surface.md | 两个 cube 的网格设置必须完全相同，且网格间距不大于 0.25 Bohr，否则插值与分析结果不可靠。 |
| 提取的平面数据稀疏、倾斜平面尤其严重 | sec-4-13-process-grid-data.md | 提取平面数据时 Multiwfn 不做插值，格点间距大则平面点稀疏；倾斜平面（用三原子定义）对此更敏感，须先提高格点质量。 |
| 两 cube 相减结果错位或报错 | sec-4-13-process-grid-data.md | 做 A-B 类格点运算时，第二个 cube 的网格设置必须与内存中第一套格点完全一致，否则差值无意义。 |
| 单体密度格点与二聚体格点对不上，交叠积分不对 | sec-4-13-process-grid-data.md | 给单体算 Gaussian 波函数时必须加 nosymm，否则 Gaussian 自动重定向/平移几何，单体格点与二聚体全空间格点不再对应。 |
| AdNDP 计算加弥散函数后数值异常甚至载入崩溃 | sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md | AdNDP 强烈不建议用弥散函数，常引起数值问题且对结果从无改善；直接去掉弥散函数重算。 |
| AdNDP 输入文件缺 NBO 数据导致无法分析 | sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md | Gaussian 路线部分必须指定 pop=nboread，文件末尾必须加 $NBO AONAO DMNAO $END，再转 .fch；求 AdNDP 轨道能量还需另备含 Fock 矩阵的 .47 文件。 |
| 一次取出全部高占据候选轨道，电子被重复计数 | sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md | 相邻候选轨道可能共享密度（如都含原子 3），应分批取出，每取出一批后密度矩阵扣除、剩余候选占据自动更新；高阶搜索前可用选项 11 存档、选项 12 恢复；剩余价电子远小于 2.0（如 1.34）即应停止，占据仅 1.4~1.8 的候选不应取出。 |
| 模糊空间 LI/DI/PDI/FLU 精度差却不知原因 | sec-4-15-fuzzy-atomic-space-analysis.md | 先看屏幕输出的 AOM 误差，超过约 0.001 即不可忽略；把 settings.ini 中 iautointgrid 设为 0 并增大 radpot/sphpot（默认 iautointgrid=1 对应 (40,230) 格点），AOM 精度直接决定 LI/DI/PDI/FLU 精度。 |
| 用 .wfn 算 PLR 得到无意义结果 | sec-4-15-fuzzy-atomic-space-analysis.md | PLR 基于线性响应核，依赖虚轨道，.wfn 只含占据轨道，必须用 .mwfn/.fch/.molden/.gms 做输入；另注意 PDI 输入环原子顺序须与连接顺序一致。 |
| 片段偶极矩数值随原点漂移，误以为算错 | sec-4-15-fuzzy-atomic-space-analysis.md | 片段净电荷不为零时片段偶极矩本来就依赖原点；苯酚二聚体单体因轻微电荷转移带小净电荷，当前原点取在二聚体核电荷中心时结果可用，不宜过度解读。 |
| 算原子有效体积/极化率/C6 时孤立原子与分子水平不一致 | sec-4-15-fuzzy-atomic-space-analysis.md | 每个元素的孤立原子波函数须按与分子计算完全相同的理论水平另行产生，否则 Veff/Vfree 与 alpha eff(0)/C6 无意义；原子文件可以是 Multiwfn 支持的任意格式，不必限于 .wfn。 |
| 共价结合片段做 CDA 时 alpha/beta 电子数对不上 | sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md | CH3+NH2（或两甲基）两片段 alpha/beta 总数与配合物不符时，必须翻转其中一个片段的自旋再分析；且开壳层相互作用下 d-b 不可靠，净转移量以 ECDA 的 CT(1->2)-CT(2->1) 为准。 |
| RO 波函数直接做 CDA 结果不对 | sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md | RO 只给出一套轨道，须先经主功能 6 选项 37 Split spatial orbitals 把每个片段的 RO 轨道拆成占据不同的 alpha/beta 轨道（存为 *_UKS.fch），再按开壳层流程做 CDA 并翻转一片段自旋。 |
| 混合基组 CDA 中配合物与片段基组不一致 | sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md | Gaussian 对 Pople 基组默认用笛卡尔型函数，易导致配合物与片段基组不一致，所有 Gaussian 输入文件都应加 5d；同时片段顺序必须与配合物中原子顺序对应，ECDA 只适用于两片段，r 项相对原始 CDA 定义已加倍，对比文献时注意。 |
| AIM 电荷用功能 2 积分，总电子数明显偏离 | sec-4-17-basin-analysis.md | AIM 流域积分不要用功能 2（纯均匀格点），要用功能 7（原子中心+均匀混合格点）；可靠 AIM 电荷的常规流程是 1（生成流域）→7 选项 2（积分同时细化边界）→选电子密度，必要时把格点提到 High 甚至 Lunatic；多极矩对应地用功能 8 而非功能 3，LI/DI 用功能 4 选项 2 的混合格点。 |
| Li6 积分中途报无法判断吸引子归属而卡住 | sec-4-17-basin-analysis.md | 提示 Warning: Unable to determine the attractor ... belongs to which atom 时，真 NNA 直接按回车继续；用赝势且该吸引子是某原子价电子极大簇时输入该原子序号；否则输入 q 返回并用更密格点重生流域。注意存在 NNA 时 AIM 原子电荷之和不再等于体系净电荷，属 AIM 本身局限。 |
| 电子密度差流域出现不对称的孤立吸引子 | sec-4-17-basin-analysis.md | 电子密度差变化复杂，必须用 High-quality grid；格点不够密时对称平面另一侧的对应吸引子会丢失（如吸引子 8），提高格点质量后重做。 |
| 空穴/电子积分明显偏离 1.0，D/Sr/t 等指标不可信 | sec-4-18-electron-excitation-analysis.md | 三种可能：Gaussian TDDFT 没加 IOp(9/40=3 or 4)；格点质量太低；延展距离太小没包住空穴/电子（Rydberg 激发务必增大延展距离）。应核对 hole/electron 积分约 1.0、跃迁密度积分约 0，并把 Multiwfn 跃迁偶极矩与 Gaussian 输出值对照。 |
| 含弥散函数时片段空穴/电子贡献出现非物理负值 | sec-4-18-electron-excitation-analysis.md | 空穴/电子成分与跃迁偶极矩分解默认用类 Mulliken 划分，与弥散函数不兼容；阴离子或必须带弥散时改用 Hirshfeld 划分（慢但稳健），或去掉弥散重算。 |
| 大量弥散函数下 LMO 形状反常 | sec-4-19-orbital-localization-analysis.md | 默认 PM-Mulliken 定域在大量弥散函数下可能误导，须改用 PM-Becke 或 Foster-Boys；另注意 Foster-Boys 的双键常表现为两个“香蕉”轨道而不分 sigma/pi，PM 则给出分离的 sigma 与 pi，这是方法特征不是错误。 |

## 高级实例与专题
| 注意/问题 | 出处 | 说明与解法 |
|---|---|---|
| VMD 导出的 .xyz 记录的是原子名而非元素名，直接载入可能认错元素 | [sec-4-20-visual-study-of-weak-interactions.md](sec-4-20-visual-study-of-weak-interactions.md) | 载入后检查屏幕提示的 Formula（如 `H1022 O511`）；若出现不期望的元素，须把 .xyz 中的原子名（如 OW、HW1、HW2）手动替换为实际元素名 |
| aNCI 的 MD 冻结中心水必须用 NVT 系综，不可用 NPT | [sec-4-20-visual-study-of-weak-interactions.md](sec-4-20-visual-study-of-weak-interactions.md) | NPT 会缩放原子坐标，破坏 `freezegrps` 冻结效果；冻结关键词示例为 `freezegrps = r_101` |
| IRI 等值面默认值 1.0 不一定适合所有体系 | [sec-4-20-visual-study-of-weak-interactions.md](sec-4-20-visual-study-of-weak-interactions.md) | 在 .vmd 脚本中修改 `mol representation Isosurface` 后面的值，或在 VMD 的 Graphics-Representations 面板中手动调节 |
| 能拿到波函数文件时强烈建议用 IGMH 而非 IGM；拿不到时用 mIGM 而非 IGM | [sec-4-20-visual-study-of-weak-interactions.md](sec-4-20-visual-study-of-weak-interactions.md) | IGM 的等值面过于臃肿，即使仔细调节等值也难以避免，图形与定量效果明显差于 IGMH |
| H-H 区域的 NCI 散点图尖峰没有触及底部不是计算错误 | [sec-4-20-visual-study-of-weak-interactions.md](sec-4-20-visual-study-of-weak-interactions.md) | 该区域不存在电子密度梯度为零的位置，故没有对应临界点和键径；这正是 NCI 相对 AIM 的优势：无键临界点处也能揭示相互作用 |
| EDA-FF 要求每种分子类型内的原子序号必须连续，否则无法设置电荷与类型 | [sec-4-21-energy-decomposition-analysis.md](sec-4-21-energy-decomposition-analysis.md) | 用 GaussView 的 Edit-Reorder-All Atoms (Except the First) by Bonding 按连接关系重排后再保存，使每个单体原子序号连续 |
| mollist.txt 中文件路径顺序必须与 .pdb 中的分子顺序严格一致 | [sec-4-21-energy-decomposition-analysis.md](sec-4-21-energy-decomposition-analysis.md) | 顺序错乱会导致电荷/类型赋给错误的原子，示例格式为 `C:\C.txt 1` 每行一个分子类型文件加分子数目 |
| 不可用 EDA-FF 把单个氢键的供受体划为两个片段来定单个氢键结合能 | [sec-4-21-energy-decomposition-analysis.md](sec-4-21-energy-decomposition-analysis.md) | 静电是长程效应（1/r），忽略其余原子会得不合理的正结合能；相距很近的多个氢键耦合强，无法合理分解，定单个氢键结合能最好用 AIM 方法 |
| 一般不推荐基于 UFF 做 EDA-FF | [sec-4-21-energy-decomposition-analysis.md](sec-4-21-energy-decomposition-analysis.md) | UFF 会系统性严重高估交换-排斥成分（如 G-C 相互作用能被算成很大的正值）；EDA-FF 之前用 UFF 优化几何可部分缓解 |
| EDA-FF 强烈推荐使用 ESP 拟合电荷（MK 或 CHELPG），不要轻易用 EEM 电荷代替 | [sec-4-21-energy-decomposition-analysis.md](sec-4-21-energy-decomposition-analysis.md) | EEM 电荷会使静电项产生显著误差（本例中 -74.26 对 -120.98 kJ/mol）；ESP 拟合电荷对静电精度至关重要 |
| EDA-SBL 的 Gaussian 输入须加 ExtraLinks=L608 且文件末尾加 -5 行指定泛函 | [sec-4-21-energy-decomposition-analysis.md](sec-4-21-energy-decomposition-analysis.md) | 缺少该关键词 Multiwfn 无法从输出载入 steric 项所需信息；本例 -5 表示 B3LYP |
| 涉及 N+1 态的 CDFT 量（垂直电子亲和能、Mulliken 电负性）用小基组不准 | [sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md) | 阴离子能量需要弥散函数；用 Multiwfn 准备输入文件时建议至少选 6-311+G* 水平 |
| 轨道加权 Fukui 函数等值面用默认值可能完全不可见 | [sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md) | 须把等值面值改为合适的值（如 C60 例用 0.0003 a.u.），否则会误以为计算失败 |
| B3LYP 加弥散基组算 f+ 和对偶描述符会弥散失真且破缺对称性 | [sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md) | 系泛函自相互作用误差致 N+2 态电子过度弥散；推荐长程校正泛函（如 ωB97XD）配合不含弥散函数的 3-zeta 基组（如 6-311G*） |
| HOMO/LUMO（准）简并体系必须设简并度或用轨道加权形式，否则 f-/Δf 违背对称性 | [sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md) | 用选项 -3 设简并度（Multiwfn 按与 LUMO 能量差小于 0.01 eV 自动判断），再分别产生 N、N+p、N-q 态波函数；否则会对反应位点得出误导结论 |
| ETS-NOCV 无特殊原因请勿使用弥散函数 | [sec-4-23-examples-of-ets-nocv-analysis.md](sec-4-23-examples-of-ets-nocv-analysis.md) | 弥散函数可能导致无法直接生成 Fock/Kohn-Sham 矩阵（须改从外部文件提供，见附录 7），且 SCPA 方法算的轨道组成可能高度不合理 |
| ETS-NOCV 片段输入须加 nosymm 且不得做几何优化 | [sec-4-23-examples-of-ets-nocv-analysis.md](sec-4-23-examples-of-ets-nocv-analysis.md) | Gaussian 会自动重取向几何，片段坐标须与配合物中完全一致；优化后坐标不一致则分析无效 |
| 片段波函数文件的载入顺序必须与片段在配合物中的出现顺序一致 | [sec-4-23-examples-of-ets-nocv-analysis.md](sec-4-23-examples-of-ets-nocv-analysis.md) | 顺序错乱会导致片段轨道归属错误，NOCV 对应关系全错 |
| 开壳层 ETS-NOCV 必须正确翻转其中一片段的自旋 | [sec-4-23-examples-of-ets-nocv-analysis.md](sec-4-23-examples-of-ets-nocv-analysis.md) | 须保证两片段 α（β）电子数之和与整个体系相同（如两 ⋅CH3 各 5α4β，须翻转其一，否则合并为 10α8β而乙烷是 9α9β） |
| Multiwfn 打印的 Sum of pair energies 不是严格的轨道相互作用能 | [sec-4-23-examples-of-ets-nocv-analysis.md](sec-4-23-examples-of-ets-nocv-analysis.md) | 因 Fock/KS 矩阵基于实际配合物波函数而非过渡态波函数构建，NOCV 能量也不是标准 ETS-NOCV 的确切量；但一般差异很小，不影响结论 |
| 片段与体系混用不同基组（如 genecp）时强烈建议所有输入都加 5d | [sec-4-23-examples-of-ets-nocv-analysis.md](sec-4-23-examples-of-ets-nocv-analysis.md) | 不熟悉 Gaussian 对 Cartesian 与球谐基函数默认适配规则时，不加 5d 会导致片段与体系基函数总数不同 |
| (CO)5Cr=CH2 的 CH2 片段单点必须用单重态而非基态三重态 | [sec-4-23-examples-of-ets-nocv-analysis.md](sec-4-23-examples-of-ets-nocv-analysis.md) | 单重态 CH2 更接近配位物中 CH2 的实际电子结构（孤对与 Cr 空 3d 形成配位键）；参考态选错则 NOCV 图像无意义 |
| NOCV 本征值与 NOCV 对能量之间没有必然的正相关 | [sec-4-23-examples-of-ets-nocv-analysis.md](sec-4-23-examples-of-ets-nocv-analysis.md) | 如 π 反馈的密度变化（本征值）大于 σ 给体，但能量贡献反而更小；两者须分别考察 |
| (超)极化率计算中弥散函数绝对不可少 | [sec-4-24-examples-of-hyperpolarizability-analyses.md](sec-4-24-examples-of-hyperpolarizability-analyses.md) | 例用 aug-cc-pVTZ；无弥散函数则结果定量不可靠，γ 的准确计算甚至需要 d-aug-cc-pVTZ |
| Gaussian 的 polar 任务必须用 #P，否则 Multiwfn 无法解析 | [sec-4-24-examples-of-hyperpolarizability-analyses.md](sec-4-24-examples-of-hyperpolarizability-analyses.md) | 如 `#P HF/6-311++g(d,p) polar=DCSHG CPHF=rdfreq`；不用 #P 则输出信息不足 |
| 解析 gamma(0;0,0,0) 之前不要选选项 -1 | [sec-4-24-examples-of-hyperpolarizability-analyses.md](sec-4-24-examples-of-hyperpolarizability-analyses.md) | 选项 -1 针对动态（频率相关）情形，静态 gamma 解析前选它会出错 |
| 解析的 γ 张量对应输入取向而 α/β 对应标准取向，VMD 结构须配套 | [sec-4-24-examples-of-hyperpolarizability-analyses.md](sec-4-24-examples-of-hyperpolarizability-analyses.md) | 把 settings.ini 中 iloadGaugeom 改为 1 再从输出文件导出 .pdb，否则单位球表示图会误导 |
| SOS 计算必须检验 (超)极化率随计入态数目的收敛性 | [sec-4-24-examples-of-hyperpolarizability-analyses.md](sec-4-24-examples-of-hyperpolarizability-analyses.md) | 用选项 5/6/7 把 α/β/γ 对态数作图；一般 100 个态足够、70 个定性可用；本例用 150 个态以避免截断误差 |
| CIS/TDDFT 做 SOS 准备时须加 IOp(9/40=5) | [sec-4-24-examples-of-hyperpolarizability-analyses.md](sec-4-24-examples-of-hyperpolarizability-analyses.md) | 默认 Gaussian 只输出绝对值大于 0.1 的跃迁系数，该 IOp 把阈值降到 0.00001，否则 Multiwfn 算出的跃迁偶极矩不准 |
| 二/三能级分析仅在两个条件同时满足时有用 | [sec-4-24-examples-of-hyperpolarizability-analyses.md](sec-4-24-examples-of-hyperpolarizability-analyses.md) | β 只有一个分量（βXXX 或 βYYY 或 βZZZ）主导，且一个（两）个激发态贡献远大于其余态；给体-π-受体体系通常满足 |
| Excel 生成频率列表存 .txt 时不要选 Unicode text | [sec-4-24-examples-of-hyperpolarizability-analyses.md](sec-4-24-examples-of-hyperpolarizability-analyses.md) | 选 Text (tab delimited) 等普通文本格式，否则 SOS 模块读入失败 |
| SOS 模块中用的单位全是原子单位 | [sec-4-24-examples-of-hyperpolarizability-analyses.md](sec-4-24-examples-of-hyperpolarizability-analyses.md) | 输入频率、解读结果时注意单位换算，不要按 eV 或 nm 直接输入 |
| (超)极化率密度分析必须先明确分子取向 | [sec-4-24-examples-of-hyperpolarizability-analyses.md](sec-4-24-examples-of-hyperpolarizability-analyses.md) | 如 H2CO 例 C=O 键平行 Z 轴后才研究 ρzzz(3) 与 -zρzzz(3) 对 γZZZZ 的贡献；取向不明则分量无意义 |
| NICS0001.gjf 必须第一个运行 | [sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md) | 后续任务依赖它，顺序错则整批 ICSS 任务失败 |
| 直接加载已有 ICSS 输出时格点设置必须与生成时完全一致 | [sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md) | 设置不同则文件加载必定失败；选 y 跳过生成输入文件后须保证设置相同 |
| 只需 NICS 平面图/曲线图时不要算三维 ICSS 格点 | [sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md) | 直接用主功能 25 的子功能 14（平面图）或 13（曲线图），方便得多且耗时低得多 |
| 基于 ICSSZZ 插值画曲线/平面图时空间范围不可超出格点有效范围 | [sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md) | 默认延伸距离仅 12 Bohr，超出范围的点插值值为 0（如不能画 (0,0,0) 到 (0,0,20) 的曲线） |
| HOMA 输入原子序号的顺序必须与原子连接顺序一致 | [sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md) | 如中间环输入 3,4,8,9,10,7；顺序错则键长贡献全错 |
| 简单能量分解（碎片波函数组合初猜）现在强烈不建议使用 | [sec-4-100-other-functions-part-1.md](sec-4-100-other-functions-part-1.md) | 改用 sobEDA 或 sobEDAw（基于 Multiwfn 和 Gaussian），项更完整且易用得多 |
| new.gjf 须含 nosymm、# 改为 #P、可删 pop=full | [sec-4-100-other-functions-part-1.md](sec-4-100-other-functions-part-1.md) | nosymm 防几何重取向；#P 保证每次迭代都输出 SCF 能量以拿到 ESCF,1st；pop=full 无用可删 |
| 弱相互作用结合的配合物做简单能量分解时必须单独评估色散组分 | [sec-4-100-other-functions-part-1.md](sec-4-100-other-functions-part-1.md) | 强相互作用体系可忽略色散，弱相互作用体系忽略则总相互作用能定性错误 |
| LOLIPOP 与非平面 π 分析须先做轨道定域化，输入文件必须含基函数信息 | [sec-4-100-other-functions-part-1.md](sec-4-100-other-functions-part-1.md) | 无基函数信息（如纯 .cub/.xyz）无法定域化，也就无法自动识别 π 型 LMO |
| 非平面体系探测 π 轨道最好去掉弥散函数；坚持用则须换定域与组成方法 | [sec-4-100-other-functions-part-1.md](sec-4-100-other-functions-part-1.md) | 用 -6 选 Pipek-Mezey based on Becke population 定域（默认 Pipek-Mezey 与弥散函数不兼容但更耗时），轨道组成用 Hirshfeld 或 Becke（默认 Mulliken+SCPA 在弥散函数下不能正常工作） |
| 分子间轨道重叠的单体坐标须直接取自二聚体且所有文件都用 nosymm | [sec-4-100-other-functions-part-1.md](sec-4-100-other-functions-part-1.md) | 保证单体 .fchk 坐标与二聚体 .fchk 完全相同；且单体 1 的原子在前、单体 2 在后 |
| 观察 Rydberg 轨道须先设大扩展距离（如 12）并用小等值面值（如 0.01） | [sec-4-200-other-functions-part-2.md](sec-4-200-other-functions-part-2.md) | 否则弥散的等值面会被截断；须用 aug-cc-pVTZ 这类带大量弥散函数的基组才能忠实描述 |
| 域分析算 RDG 格点时扩展距离不能为零，也不宜过大 | [sec-4-200-other-functions-part-2.md](sec-4-200-other-functions-part-2.md) | 为零则等值面被盒子边界截断，域积分模块无法工作（本例 3 Bohr 合适）；过大则格点数过高非常耗时 |
| 域积分精度直接由格点质量决定 | [sec-4-200-other-functions-part-2.md](sec-4-200-other-functions-part-2.md) | 若某域仅由很少格点组成且轮廓粗糙，其积分精度必然很低，须提高格点质量重算 |
| 研究 BOA 输入文件必须含基函数信息；二面角值域为 0～180° | [sec-4-200-other-functions-part-2.md](sec-4-200-other-functions-part-2.md) | .xyz/.pdb/.mol 只能算 BLA，BOA 须 .mwfn/.fch/.molden/.gms；D 在 90～180° 时偏离平面为 180-D |
| 轨道对密度差贡献的结果依赖所选轨道范围 | [sec-4-200-other-functions-part-2.md](sec-4-200-other-functions-part-2.md) | 如选 MO 1～15 与只选 MO 10～15 时 MO 10～15 的贡献不同；比较前须固定范围 |
| NBO 对 f- 的贡献只考虑 Lewis 型 NBO | [sec-4-200-other-functions-part-2.md](sec-4-200-other-functions-part-2.md) | Rydberg 型 NBO 占据数近零，对 N 态密度无显著贡献，纳入只添噪声 |
| 域分析模块只适合单个分子的内部空腔，不能用于大晶胞所有孔洞 | [sec-4-300-other-functions-part-3.md](sec-4-300-other-functions-part-3.md) | 大晶胞/COF 自由体积用 4.300.1 的方法，域分析模块对此无能为力 |
| STM 模拟前分子必须平行于 XY 平面 | [sec-4-300-other-functions-part-3.md](sec-4-300-other-functions-part-3.md) | 如 phenanthrene.fch 中分子平行 YZ 平面，须先用 Multiwfn 直接旋转波函数和几何；重做单点虽也可行但更麻烦 |
| STM 的偏压 V 定义正确至关重要 | [sec-4-300-other-functions-part-3.md](sec-4-300-other-functions-part-3.md) | V 为负时电子从样品流向针尖，V 越负参与贡献的分子轨道越多；默认 V 设为 HOMO 能量与费米能级之差此时仅 HOMO 贡献 |
| 大量弥散函数致量子化学程序删掉线性相关基函数时 Multiwfn 无法直接产生 Kohn-Sham 矩阵 | [sec-4-300-other-functions-part-3.md](sec-4-300-other-functions-part-3.md) | 须改用其它方式提供矩阵，如 Gaussian 直接产生 .47 文件（几何、泛函、基组须与原任务完全相同） |
| 沿 IRC 算 Mayer 键级/ELF 时单点须去掉弥散函数并加 nosymm | [sec-4-A-special-topics-and-advanced-tutorials.md](sec-4-A-special-topics-and-advanced-tutorials.md) | 有弥散函数时 Mayer 键级效果不佳（忽略弥散不改变 ELF 等值面）；不加 nosymm 则 Gaussian 自动重取向致 ELF 动画出现跳帧 |
| 基组含弥散函数时不要用 Mulliken/Löwdin/SCPA 类自旋布居 | [sec-4-A-special-topics-and-advanced-tutorials.md](sec-4-A-special-topics-and-advanced-tutorials.md) | 结果可能可靠也可能不可靠；此时改用模糊原子空间积分自旋密度 |
| TDDFT 激发态没有自旋密度，OED 是表征未成对电子分布的唯一途径 | [sec-4-A-special-topics-and-advanced-tutorials.md](sec-4-A-special-topics-and-advanced-tutorials.md) | 不要试图用自旋密度画 TDDFT 激发态的自由基分布，直接算 OED |

## 运行环境与附录
| 注意/问题 | 出处 | 说明与解法 |
|---|---|---|
| 非官方支持程序生成的 .molden 直接分析可能结果错误 | [sec-5-1-make-multiwfn-support-more-quantum-chemistry-programs.md](sec-5-1-make-multiwfn-support-more-quantum-chemistry-programs.md) | 先用 Wenli Zou 的 Molden2AIM（<https://github.com/zorkzou/Molden2AIM>）把 .molden 标准化（按 m2a.ini 配置后运行，得到 ltwd_new.molden 及 .wfn/.wfx），再载入 Multiwfn 分析。 |
| 用 ECP 时 Molden2AIM 输出的 .wfn 算静电势结果错误 | [sec-5-1-make-multiwfn-support-more-quantum-chemistry-programs.md](sec-5-1-make-multiwfn-support-more-quantum-chemistry-programs.md) | Molden2AIM 输出的 .wfn 中 charge 字段是元素周期表序号而非有效核电荷（与 Gaussian 的 ECP .wfn 不一致，如 Lanl2DZ 下 Au 应为 19.0）；用 ECP 并计算静电势前，须手动把该字段改为有效核电荷。 |
| 静默/批处理运行时图形窗口弹窗卡住流程 | [sec-5-2-running-multiwfn-in-silent-mode.md](sec-5-2-running-multiwfn-in-silent-mode.md) | 把 settings.ini 中 isilent 由 0 改为 1，或在命令行加 -silent 参数，禁止运行中自动显示图形/GUI；输入流文件每行即交互模式下的一次输入，输入文件名作为命令行参数给出，不写入流文件。 |
| 任务完成后出现 forrtl: severe (24): end-of-file during read 报错 | [sec-5-2-running-multiwfn-in-silent-mode.md](sec-5-2-running-multiwfn-in-silent-mode.md) | 不是真正的报错，可安全忽略；若想优雅退出，应恰当编写输入流文件，使最后一步在主功能菜单输入 q 退出。 |
| Windows PowerShell 下 Multiwfn … < xxx.in 重定向无效 | [sec-5-2-running-multiwfn-in-silent-mode.md](sec-5-2-running-multiwfn-in-silent-mode.md) | PowerShell 不支持 < 重定向符，改用管道：Get-Content orbana_1_3.in \| ./Multiwfn.exe COCl2.fch > orbana_1_3.txt。 |
| 大波函数密度矩阵等长输出在命令行窗口只剩最后一部分 | [sec-5-5-make-command-line-window-capable-of-recording-more-outputs.md](sec-5-5-make-command-line-window-capable-of-recording-more-outputs.md) | 右键窗口标题栏进 Properties（属性）-Layout（布局），把缓冲区由默认 300 改大（如 9999），设置永久保存；Linux/MacOS 在终端找类似的缓冲区设置。 |
| 非 .fch/.fchk/.chk 输入无法调用 cubegen 加速 ESP 计算 | [sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md](sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md) | 先把 settings.ini 中 cubegenpath 设为 cubegen 可执行文件实际路径；只有 .fch/.fchk/.chk 输入会被自动调用。.mwfn/.molden/.gms 先经主功能 100 子功能 2 转为 .fch；ORCA 的 .gbw 可用 examples/scripts/gbw2fch.sh 批量转 .fch。注意只需算极少数格点 ESP 的功能不支持 cubegen 调用。 |
| 用 cubegen 算的 ESP 与预期的电子态不一致（如 MP2） | [sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md](sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md) | cubegen 用的是 .fch/.fchk 中的密度矩阵，默认 SCF 密度；文件中若有多种密度（如 # MP2/cc-pVTZ density 同时含 SCF 与 MP2 密度），须把 settings.ini 中 cubegendenstype 由默认 SCF 改为 MP2。 |
| 大体系下 Multiwfn 调用 cubegen 失败或崩溃 | [sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md](sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md) | 常见原因是 cubegen 需分配内存超默认上限，分析前先在终端运行 export GAUSS_MEMDEF=4GB；另两类原因是 .fch/.fchk 有问题（无波函数信息如 ONIOM 力场低层文件、缺少所选类型的密度矩阵、文件损坏/传输不完整）或 cubegen 太旧与文件不兼容。cubegen 输出转存于当前文件夹 nouseout 文件，可查看排查。 |
| G09 的 cubegen 只用单核，并行加速无效 | [sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md](sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md) | G09 cubegen 并行实现有 bug 只用一个 CPU 核心，G16 才按 settings.ini 中 nthreads 分配核心；Multiwfn 靠 cubegenpath 中是否含 g16/G16 字符串判断版本，路径命名须保留该标识。 |
| 修改占据数等改动波函数后 cubegen 算出的 ESP 仍是旧结果 | [sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md](sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md) | cubegen 用的是输入文件中的原始密度矩阵，不受内存中修改（如主功能 6 子功能 26 改占据数）影响；须先用主功能 100 子功能 2 导出 .fch（其中 SCF 密度矩阵对应当前波函数），再以该 .fch 为输入做 ESP 分析。 |
| 截图/默认导出导致论文图质量差、有锯齿 | [sec-5-8-some-tips-on-achieving-ideal-drawing-quality.md](sec-5-8-some-tips-on-achieving-ideal-drawing-quality.md) | 不截屏，用 save picture / export graphical file 选项生成图像（Linux 屏显质量差但存图与平台无关）；纯文本线条图把 settings.ini 中 graphformat 改为 .pdf/.svg 等矢量格式再转像素，含渐变色（等值面/颜色填充图）用默认 .png，先存大尺寸再用图像软件缩小以等效抗锯齿。 |
| 等值面图粗糙、光照不满意 | [sec-5-8-some-tips-on-achieving-ideal-drawing-quality.md](sec-5-8-some-tips-on-achieving-ideal-drawing-quality.md) | 用高质量格点（小间距/多格点数）生成格点数据，显示前先缩放使体系充满绘图区域；光照不满意在等值面 GUI 菜单 Other settings - Set lighting 中调；效果要求高时用 VMD 绘图脚本渲染（见 4.A.14 节做法）。 |
| Multiwfn 调用 Gaussian 失败并报 No executable for file l1.exe | [sec-6-1-setting-up-running-environment-for-gaussian-in-windows.md](sec-6-1-setting-up-running-environment-for-gaussian-in-windows.md) | 须定义 GAUSS_EXEDIR 环境变量（值为 Gaussian 安装目录，如 D:\study\g16w\，即 g16.exe 所在文件夹），否则 Gaussian 找不到 l1.exe 等可执行文件。 |
| Multiwfn 调用的 Gaussian 没用上预设的核数等默认设置 | [sec-6-1-setting-up-running-environment-for-gaussian-in-windows.md](sec-6-1-setting-up-running-environment-for-gaussian-in-windows.md) | Windows 下被调用的 Gaussian 在当前文件夹而非 Gaussian 临时文件夹找 Default.Rou；若其中有重要设置（如默认 CPU 核心数），须把该文件复制到当前文件夹。 |
| 赝势体系电子密度全空间积分远小于总电子数 | [sec-6-4-details-about-supplying-inner-core-electron-density.md](sec-6-4-details-about-supplying-inner-core-electron-density.md) | 缺内层电子密度所致（如 Pt(NH3)2Cl2 不载 EDF 积分为 52.00 价电子数，正确应为 132.00）；保持 settings.ini 中 isupplyEDF 为 1 让 Multiwfn 从内置 EDF 库自动补充，之后用主功能 100 子功能 4 全空间积分电子密度验证是否为总电子数。 |
| 想用高质量内置 EDF 库却实际读了 Gaussian .wfx 自带 EDF | [sec-6-4-details-about-supplying-inner-core-electron-density.md](sec-6-4-details-about-supplying-inner-core-electron-density.md) | Gaussian 产生的赝势 .wfx 自带 EDF 字段时默认优先读取（readEDF 为 1），而内置 EDF 库质量更优；想用内置库把 settings.ini 中 readEDF 由 1 改为 0；完全不想自动补充则把 isupplyEDF 设为 0。 |
| 从原子 .wfx 借用 EDF 后内层密度仍不对 | [sec-6-4-details-about-supplying-inner-core-electron-density.md](sec-6-4-details-about-supplying-inner-core-electron-density.md) | 先把 settings.ini 中 isupplyEDF 设为 1，再按元素逐个指定原子 .wfx；每次选择的原子（如直接输序号 4,8-10,11）必须对应相同元素和相同赝势；原子 .wfx 须用户自己准备，且事后务必做全空间积分验证。 |
| 载入 .molden 等第三方输入后不知波函数是否被正确读取 | [sec-6-5-check-sanity-of-wavefunction.md](sec-6-5-check-sanity-of-wavefunction.md) | 做两项合理性检查：(1) 进主功能 100 子功能 4 对电子密度全空间积分，结果应非常接近实际电子数；(2) 进隐藏的主功能 1000 子功能 100 检查轨道归一化，若与 1 和与整数的最大偏差都明显大于零则输入文件必有严重问题，任一接近零则与 Multiwfn 兼容。 |
| 归一化检查时不知该选 GTF 还是基函数轨道系数 | [sec-6-5-check-sanity-of-wavefunction.md](sec-6-5-check-sanity-of-wavefunction.md) | 若输入文件同时含 GTF 和基函数信息，主功能 1000 子功能 100 会要求二选一检查，两种系数都应满足归一化条件，建议两种都检查。 |
| 碎片-轨道核吸引能（主功能 1000 子功能 90）结果与预期差一个占据数因子 | [sec-6-6-special-functions.md](sec-6-6-special-functions.md) | 该功能计算不考虑轨道占据数，公式即 <φi\|ΣZ_A/\|r-R_A\|\|φi\> 的 Becke 多中心积分；比较不同轨道贡献时须自行乘占据数。 |
| Becke 积分精度不够或想复现/导出积分格点 | [sec-6-6-special-functions.md](sec-6-6-special-functions.md) | Hirshfeld/ADCH 电荷、模糊原子空间分析、核吸引能等用的 Becke 多中心积分精度由 settings.ini 中 radpot 和 sphpot 控制；用主功能 1000 隐藏子功能 93 可把积分点导出到当前目录 intpt.txt（进入后选 y 一并输出权重），角向 Lebedev、径向第二类 Gauss-Chebyshev。 |
| 前分子波函数性质与实际体系对不上 | [sec-6-6-special-functions.md](sec-6-6-special-functions.md) | 主功能 1000 子功能 17 生成前分子波函数时，原子 .wfn 文件所用基组必须与当前体系实际波函数基组完全一致，否则前分子性质无意义；成功生成后选 y 即切换内存波函数为前分子波函数。 |
| 轨道定域化/ETS-NOCV/COHP 等功能缺 Fock/KS 矩阵导致新轨道无能量 | [sec-6-7-about-providing-fock-ks-matrix-to-multiwfn.md](sec-6-7-about-providing-fock-ks-matrix-to-multiwfn.md) | 纯文本文件以下三角形式记录矩阵元（闭壳层 F(1,1) F(2,1) F(2,2) … F(nbasis,nbasis)；开壳层先写完整 alpha 套再写完整 beta 套），数据格式自由、个数正确最重要；.mwfn 自带该矩阵可直接载入；任一含分子轨道的波函数文件都可经主功能 100 子功能 17 按轨道能量和系数生成并导出此文件。 |
| 不知如何从量子化学程序拿到 Fock/KS 矩阵 | [sec-6-7-about-providing-fock-ks-matrix-to-multiwfn.md](sec-6-7-about-providing-fock-ks-matrix-to-multiwfn.md) | Gaussian 计算加 IOp(5/33=3)、GAMESS-US 加 NPRINT=5 打印每轮 SCF 矩阵后转格式；ORCA 输入加 %output Print[P_Iter_F] 1，Multiwfn 取最后一次（收敛）矩阵；CP2K 在 &FORCE_EVAL/&DFT 下加 &PRINT/&KS_CSR_WRITE（REAL_SPACE T、UPPER_TRIANGULAR T、THRESHOLD 0）导出 .csr；或 Gaussian 用 # … pop=nboread 加 $NBO archive file=C:\MY_FILE $END 生成 .47 文件，Multiwfn 从其 $FOCK 域读取。 |
| 选错输入文件类型导致功能不可用或白算 | [README.md](README.md) | Multiwfn 不同功能需要不同输入文件类型，动手前认真阅读 2.5 节关于输入文件与波函数类型的说明；且 Multiwfn 多数功能本地无需安装 Gaussian。 |
| 找不到 Multiwfn 输出文件/输出位置与预期不符 | [README.md](README.md) | 手册所说当前文件夹指调用 Multiwfn 时所在路径（Windows 双击图标启动即 Multiwfn 可执行文件所在文件夹）；找输出文件、放 Default.Rou、看 cubegen 的 nouseout 都以此为准。 |
| Linux/Mac 下等值面透明效果异常或某些功能失灵 | [README.md](README.md) | Linux/Mac 图形窗口中透明风格等值面不生效是已知限制，保存为图像文件后透明渲染正常；不建议用 MacOS 版（某些功能可能无法正常工作），新手强烈建议用 Windows 版（最稳定、图形显示最好、免配置）。 |
