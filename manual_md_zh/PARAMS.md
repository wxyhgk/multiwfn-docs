# Multiwfn 参数关键词表

> settings.ini 参数、量子化学关键词、环境变量与文件格式要点。

## settings.ini 参数
| 参数/关键词 | 含义与取值 | 出处 |
|---|---|---|
| `nthreads` | 并行线程数，设为 CPU 物理核心实际数目；G16 的 cubegen 所用核心数与之相同 | [sec-2-1](sec-2-1-install.md) |
| `ompstacksize` | Windows 版大体系并行崩溃时增大此栈大小（Linux/MacOS 对应环境变量 `OMP_STACKSIZE`） | [sec-2-4](sec-2-4-parallel-implementation.md) |
| `formchkpath` | Gaussian 包中 `formchk` 可执行文件的实际路径，设好后可直接加载 `.chk`（自动转 `.fch`/`.fchk` 后删除） | [sec-2-5](sec-2-5-input-files-and-wavefunction-types.md) |
| `orca_2mklpath` | ORCA 文件夹中 `orca_2mkl` 可执行文件的实际路径，设好后可直接加载 `.gbw` | [sec-2-5](sec-2-5-input-files-and-wavefunction-types.md) |
| `gaupath` | Gaussian 可执行文件的实际路径，供 promolecular 原子波函数、Hirshfeld-I 的 `.rad`、CM5、CDFT 等自动调用 Gaussian | [sec-3-7](sec-3-7-custom-operation-promolecular-and-deformation-properties.md) |
| `orcapath` | ORCA 可执行文件的实际路径，设好后 CDFT 模块可直接调用 ORCA 算 N/N+1/N-1 态 | [sec-3-25](sec-3-25-conceptual-density-functional-theory-analysis.md) |
| `cubegenpath` | Gaussian 的 `cubegen` 可执行文件的实际路径，设好后 `.fch`/`.fchk` 输入时自动调用算 ESP | [sec-5-7](sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md) |
| `cubegendenstype` | cubegen 所用密度矩阵类型，默认 `SCF`；如 `.fch` 由 `# MP2/cc-pVTZ density` 产生且想算 MP2 的 ESP 则改为 `MP2` | [sec-5-7](sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md) |
| `dftd3path` | 经 Tian Lu 修改的 `dftd3` 可执行文件的实际路径（Linux 下 `chmod +x`），供原子对色散能分析调用 | [sec-3-24](sec-3-24-energy-decomposition-analysis.md) |
| `lastfile` | 上次成功读取的输入文件路径；主菜单输 `o` 即重载该文件，`?` 可代指其所在目录 | [sec-5-6](sec-5-6-rapidly-load-a-file-into-multiwfn.md) |
| `radpot` | Becke 数值积分径向点数，默认 75（Hirshfeld 电荷不准时可改为 100；模糊键级默认 40） | [sec-3-9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| `sphpot` | Becke 数值积分角向点数，默认 434（可改为 590；模糊键级默认 230）；VDD 电荷偏离时优先增大此项 | [sec-3-9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| `radcut` | Becke 积分径向截断，默认 15；与上两项配合提高精度时须先设 `iautointgrid=0` | [sec-3-200](sec-3-200-other-functions-part-2.md) |
| `iautointgrid` | 设为 0 才手动用 `radpot`/`sphpot`/`radcut` 控制格点；为 1 时 AOM 用 (40,230) 自动格点 | [sec-4-15](sec-4-15-fuzzy-atomic-space-analysis.md) |
| `iautogrid` | Λ 指数的 Becke 格点开关；设为 0 后再在 `radpot`/`sphpot` 中指定期望值 | [sec-3-21](sec-3-21-electron-excitation-analysis.md) |
| `outmedinfo` | 设为 1 则全空间积分时导出 `integrate.txt`（序号、坐标、函数值、Lebedev 权重、原子权重），PEOE 下可监视每轮电荷/电负性 | [sec-3-100](sec-3-100-other-functions-part-1.md) |
| `expcutoff` | 指数求值截断：指数小于 -40 跳过（实空间函数 12、14、16 除外）；设 0 可关闭该处理 | [sec-2-6](sec-2-6-real-space-functions.md) |
| `expcutoff_PBC` | 上条的 PBC 版本：`exp(x)` 的 `x` 小于此值跳过求值，增大省时但变差 | [sec-2-9](sec-2-9-analysis-of-periodic-systems.md) |
| `laplfac` | 电子密度拉普拉斯乘子，默认 1.0；设为其它值则 `∇²ρ` 整体乘以该值 | [sec-2-6](sec-2-6-real-space-functions.md) |
| `ipolarpara` | 设为 1 时自旋密度函数返回自旋极化参数函数而非自旋密度 | [sec-2-6](sec-2-6-real-space-functions.md) |
| `ELF_addminimal` | 改为 0 则关闭给 `D(r)` 加极小值 1e-5 的处理（该处理抑制分子边界外 ELF 恒为 1 的缺陷） | [sec-2-6](sec-2-6-real-space-functions.md) |
| `ELFLOL_type` | 0 为 Becke 定义的 ELF/LOL；改为 1 用 Tsirelson 定义的 ELF；改为 2 用另一形式 `LOL(r)=1/(1+[1/τ(r)]²)` | [sec-2-6](sec-2-6-real-space-functions.md) |
| `iESPcode` | ESP 计算代码：1 为旧慢代码，2（默认）为基于 LIBRETA 的新快代码 | [sec-2-6](sec-2-6-real-space-functions.md) |
| `atomdenscut` | 设为 0 关闭小贡献跳过；默认 H/C/N/O 对某点贡献小于 0.00001 时不计算 | [sec-2-6](sec-2-6-real-space-functions.md) |
| `RDG_maxrho` | 默认 0.05：电子密度大于此值处 RDG 置 100.0 以屏蔽成键区；设为 0 取消该处理 | [sec-3-23](sec-3-23-visual-study-of-weak-interaction.md) |
| `RDGprodens_maxrho` | 上条在 promolecular 近似下的对应物，默认阈值 0.1 | [sec-3-23](sec-3-23-visual-study-of-weak-interaction.md) |
| `refxyz` | 参考点坐标（Bohr），如 `0.0,0.0,-0.3`；影响关联空穴、`srcfuncmode=1` 的源函数、模糊空间参考点 | [sec-2-6](sec-2-6-real-space-functions.md) |
| `paircorrtype` | 对密度 Γ 考虑的相关：1 为 Fermi（交换）空穴，2 为 Coulomb 空穴，3 为总关联空穴；单行列式下 1 与 3 等价、2 无意义 | [sec-4-3](sec-4-3-output-and-plot-various-properties-in-a-line.md) |
| `pairfunctype` | 实空间函数 17（关联空穴/交换-关联密度/关联因子）算哪个函数和哪个自旋；闭壳层 α/β 相同 | [sec-4-3](sec-4-3-output-and-plot-various-properties-in-a-line.md) |
| `iALIEdecomp` | 设为 1 时主功能 1 除输出平均局域电离能外还输出每个占据 MO 的贡献 | [sec-2-6](sec-2-6-real-space-functions.md) |
| `srcfuncmode` | 源函数模式：1（默认）以 `refxyz` 为固定参考点、`r'` 为变量；2 反之 | [sec-2-6](sec-2-6-real-space-functions.md) |
| `uservar` | 通用数值变量：IRI 参数 `a`（0 即推荐值 1.1）；局域温度分母密度阈值；910~914 原子权重函数的指定原子；KED 附加 `∇²ρ/uservar` 项 | [sec-2-7](sec-2-7-user-defined-real-space-function.md) |
| `IRI_rhocut` | 默认 0.00005 a.u.：ρ 小于等于此值处 IRI 置大值 5.0；设为 0 取消（做 basin/拓扑分析时应设 0） | [sec-3-23](sec-3-23-visual-study-of-weak-interaction.md) |
| `ivdwprobe` | vdW 势探针原子的元素序号，默认 6（碳）；设为 0 则进入功能时手动输入元素名 | [sec-3-23](sec-3-23-visual-study-of-weak-interaction.md) |
| `iuserfunc` | 自定义实空间函数序号：12 为核吸引势能密度，3 为 r² 期望密度，33/34 为 PAEM 的波函数/DFT 版 XC 势，92/93/94 为 vdW/排斥/色散势，98 为 Δf_w，-1 为载入 cube 的插值函数，-3 为 B 样条插值，10000+i 指向第 i 个主实空间函数 | [sec-2-7](sec-2-7-user-defined-real-space-function.md) |
| `steric_addminimal` | 空间位阻势分母中的小量 δ；设为 0 则恢复原始表达式 | [sec-2-7](sec-2-7-user-defined-real-space-function.md) |
| `ispecial` | 多功能模式开关：决定 Pauli 势算法（0 为能量分解式，1 为原始定义）；为 1 时输出原子四极矩、偶极前平移使核贡献为零、用自定义函数代密度；模糊/CDFT 的 AOM 含全部轨道须设为 3 | [sec-2-7](sec-2-7-user-defined-real-space-function.md) |
| `iDFTxcsel` | XC 泛函选择：0-29 为只 X 部分，30-69 为只 C 部分，70-99 为整个 XC（如 32 对应 LYP 相关） | [sec-2-7](sec-2-7-user-defined-real-space-function.md) |
| `iKEDsel` | 动能密度形式选择（自定义函数 1200/1210、Pauli 相关量用；原始定义 Pauli 势目前只支持 3、5、7） | [sec-2-7](sec-2-7-user-defined-real-space-function.md) |
| `graphformat` | 导出图片格式，默认 `png`；线条为主的图建议 `pdf`/`svg`，嵌入 Office 常用 `wmf` | [sec-2-8](sec-2-8-graphic-formats-and-image-size.md) |
| `graph1Dsize` / `graph2Dsize` / `graph3Dsize` | 曲线图 / 二维图（填充、等值线、浮雕等）/ 三维图（等值面、结构）的图像高宽 | [sec-2-8](sec-2-8-graphic-formats-and-image-size.md) |
| `symbolsize` | 主功能 100 双函数散点图中点的大小 | [sec-3-100](sec-3-100-other-functions-part-1.md) |
| `aug1D` | 沿线绘图模式 1 两侧延长距离，默认 1.5 Bohr（也可用选项 0 临时改） | [sec-3-4](sec-3-4-outputting-and-plotting-specific-property-in-a-line.md) |
| `num1Dpoints` | 线上取点数，默认 3000（ESP 自动降为六分之一）；光谱曲线的实际点数亦由此控制 | [sec-3-4](sec-3-4-outputting-and-plotting-specific-property-in-a-line.md) |
| `Aug2D` | 平面图作图区外延默认值，默认 4.5 Bohr（也可用选项 0 临时改） | [sec-3-5](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) |
| `Aug3D` | 格点盒子与轨道等值面盒子的外延默认值；Rydberg 等弥散轨道经 Other settings 临时增大（如 12 Bohr） | [sec-3-2](sec-3-2-showing-molecular-structure.md) |
| `pleatmlabsize` / `iatmlabtype` | 平面图原子标签的大小 / 形式（原子序号还是元素名） | [sec-3-5](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) |
| `disshowlabel` | 距平面距离阈值：小于此值才显示原子标签（选项 17 可临时改），盆间路径距平面超此值部分不显示 | [sec-3-5](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) |
| `iatom_on_plane_far` | 与远离作图平面的原子的显示控制相关（手册中英文原文在此处均截断，确切行为见 `settings.ini` 注释） | [sec-3-5](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) |
| `nprevorbgrid` | 主功能 0 轨道等值面默认格点数（Isosur. quality 可临时调高，注意当前等值面会被删除） | [sec-3-2](sec-3-2-showing-molecular-structure.md) |
| `isoRGB_same` / `isoRGB_oppo` | 等值面正值部分 / 负值部分的默认 RGB（如 `1.0,0.0,0.0` 为纯红） | [sec-3-2](sec-3-2-showing-molecular-structure.md) |
| `bondRGB` / `atmlabRGB` / `atmcolorfile` | 键连线 / 原子标签颜色与原子球颜色文件，改后重启生效 | [sec-3-2](sec-3-2-showing-molecular-structure.md) |
| `CP_RGB_2D` | 平面图上各类临界点的颜色设置 | [sec-4-4](sec-4-4-output-and-plot-various-properties-in-a-plane.md) |
| `iplaneextdata` | 设为 1 时平面格点数据不内部计算，改从外部纯文本文件载入（各点坐标自动输出，可用 cubegen 等第三方工具算值） | [sec-3-5](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) |
| `isurfstyle` | 盆间表面描绘方式：1 为路径束，2（默认）为实心面，3 少用 | [sec-3-14](sec-3-14-topology-analysis.md) |
| `MCvolmethod` | vdW 体积区域定义：(1) 原子 vdW 球叠加（快、无需波函数）；(2) 电子密度等值面包围区（0.001 孤立体系，0.002 凝聚相） | [sec-3-100](sec-3-100-other-functions-part-1.md) |
| `bndordthres` | 键级打印阈值，默认 0.05；DA 加成早期弱键须设为 0.0 才输出 | [sec-3-11](sec-3-11-bond-order-analysis.md) |
| `compthres` | 轨道成分打印阈值，默认只打印大于 0.5% 的项；激发态 MO 跃迁打印阈值为其 10 倍（即 5%） | [sec-3-10](sec-3-10-orbital-composition-analysis.md) |
| `compthresCDA` | CDA 片段轨道贡献显示阈值，默认只显示贡献 ≥1% 的片段轨道 | [sec-3-19](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md) |
| `iCDAcomp` | 改为 2 则用 SCPA 代替 Mulliken 算片段轨道组成（组成恒正且不超过 100%） | [sec-3-19](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md) |
| `iMCBOtype` | 设为 1 直接打印正反向平均的多中心键级；设为 2 直接打印多中心指数 MCI | [sec-3-11](sec-3-11-bond-order-analysis.md) |
| `ishowptESP` | 设为 0 则主功能 1 与拓扑分析的临界点性质中跳过最耗时的 ESP 计算 | [sec-3-3](sec-3-3-outputting-all-properties-at-a-point.md) |
| `ibasinlocmin` | 设为 1 则 basin 分析定位极小值（排斥子）而非极大值，用于找 RDG/IRI 极小 | [sec-3-20](sec-3-20-basin-analysis.md) |
| `ispheratm` | 设为 0 则跳过 promolecular 计算前的原子电子密度球化步骤 | [sec-3-7](sec-3-7-custom-operation-promolecular-and-deformation-properties.md) |
| `SpherIVgroup` | 设为 1 则 IV A 族原子也用复制旋转单占据轨道法球化，而非默认的 sp³ 组态 | [sec-3-7](sec-3-7-custom-operation-promolecular-and-deformation-properties.md) |
| `iloadGaugeom` | 从 Gaussian 输出文件加载几何：1（默认）为输入取向，2 为标准取向 | [sec-2-5](sec-2-5-input-files-and-wavefunction-types.md) |
| `iloadORCAgeom` | 设为 1（默认）则从 ORCA 输出文件加载最终几何 | [sec-2-5](sec-2-5-input-files-and-wavefunction-types.md) |
| `ifchprog` | 较老版本（约 ≤5.0）Q-Chem 产生的 `.fchk` 载入前须设为 2 | [sec-2-5](sec-2-5-input-files-and-wavefunction-types.md) |
| `ishowchgtrans` | 设为 1 则 ADCH/CM5 计算中输出原子间电荷转移细节 | [sec-3-9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| `uESEinp` | 设为 1 则 CM5 计算后生成 uESE/xESE 溶剂化模型输入（须在气相 B3LYP/def2-TZVP 下算 CM5） | [sec-3-9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| `maxloadexc` | 非零且激发态数超限时只载入前该数目个态（如 5），加速跃迁偶极矩与 SOS 计算 | [sec-3-21](sec-3-21-electron-excitation-analysis.md) |
| `NICSnptlim` | 每个 Gaussian NMR 输入文件的原子数（真实+Bq）上限，默认 8000；G09 老版本须配 `guess=huckel` 否则须设很小（如 1000） | [sec-3-28](sec-3-28-electron-delocalization-and-aromaticity-analyses.md) |
| `iprintLMOorder` | 设为 1 则定域轨道成分按原子/原子对顺序打印，便于找目标键的 LMO | [sec-4-19](sec-4-19-orbital-localization-analysis.md) |
| `IGMvdwscl` | IGMH/mIGM/IGM 加速：只算落在两以上片段缩放 vdW 球重叠区内的格点（如设 2.0，此时只能画 δg_inter） | [sec-4-20](sec-4-20-visual-study-of-weak-interactions.md) |
| `amIGMvdwscl` | aIGM/amIGM 加速的片段 1 缩放 vdW 半径因子，默认 2；设为 0 关闭加速 | [sec-4-20](sec-4-20-visual-study-of-weak-interactions.md) |
| `readEDF` / `isupplyEDF` | `readEDF` 从 1 改为 0 则含赝势的 `.wfx` 不从其 EDF 字段读内 Post Hollis 数据而用内置库；`isupplyEDF` 设为 0 关闭从内置 EDF 库自动补充，设为 1 则从原子 `.wfx` 借用 EDF | [sec-6-4](sec-6-4-details-about-supplying-inner-core-electron-density.md) |
| `ESPrhoiso` | 设为大于 0 的值（如 0.001）则只对该电子密度等值面附近格点算 ESP，其余置 0，大幅降 ESP 着色 vdW 面代价 | [sec-4-A](sec-4-A-special-topics-and-advanced-tutorials.md) |
| `imolsurparmode` | 局域分子表面分析的划分模式，直接影响结果（教程例用 `imolsurparmode=1`） | [sec-4-12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| `isilent` | 由 0 改为 1（等价于命令行 `-silent`）则运行中禁止自动显示任何图形/GUI | [sec-5-2](sec-5-2-running-multiwfn-in-silent-mode.md) |
| `ifdoPBCxyz` | X/Y/Z 三方向是否考虑周期性，如 `1,1,0` 忽略 Z 方向（二维平行 XY 体系推荐，沿 Z 一维链推荐 `0,0,1`） | [sec-2-9](sec-2-9-analysis-of-periodic-systems.md) |
| `PBCnxnynz` | X/Y/Z 三方向各考虑多少邻镜像，默认 `1,1,1`；原胞很小（如金刚石 3.5 Å）建议 `2,2,2` | [sec-2-9](sec-2-9-analysis-of-periodic-systems.md) |

## 程序关键词
| 参数/关键词 | 含义与取值 | 出处 |
|---|---|---|
| `nosymm` | 禁止 Gaussian 自动重定向/标准取向；凡是要求片段与复合物坐标严格一致的任务都必须加，包括碎片组合初猜、分子间轨道重叠、ETS-NOCV 片段单点、密度差/差值平面图与等值面、CDA 片段计算、超胞 PBC 平移矢量核对 | [sec-3-100-other-functions-part-1.md](sec-3-100-other-functions-part-1.md) |
| `pop=full` | Gaussian 路线关键词，使输出文件中打印全部轨道信息；碎片组合初猜要求每个碎片计算都指定 `nosymm` 和 `pop=full`；单体轨道重叠要求两单体输出指定 `nosymm pop=full`；仅画 TDOS 时可用带 `pop=full` 的 Gaussian 单点输出代替波函数文件 | [sec-3-100-other-functions-part-1.md](sec-3-100-other-functions-part-1.md) |
| `pop=nboread` | 告诉 Gaussian 把 `$NBO ... $END` 段转交给内嵌 NBO 模块；是使用 NAO 基分析（NAO 轨道组成、NAO 基多中心键级与 Wiberg 分解、AdNDP、Yoshizawa 输运路径、NBO plot 文件）的前提路线关键词 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) |
| `$NBO DMNAO $END` | 写在 Gaussian 输入文件几何之后、空行隔开的 NBO 输入段，使 NBO 打印 NAO 基下的密度矩阵；选项 -2（NAO 基多中心键级）、选项 9（NAO 基 Wiberg 分解）、AV1245/AVmin NAO 版、AdNDP 都要求此关键词，且此时不可用 `.fch` 作输入 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) |
| `#p PBE1PBE/6-311G** pop=nboread` + `$NBO DMNAO $END` | NAO 基多中心键级/Wiberg 分解的标准 Gaussian 输入写法示例：路线行指定 `pop=nboread`，几何后空行写 `$NBO DMNAO $END`；输出 `.out`（不是 `.fch`）作为 Multiwfn 输入 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) |
| `NAOMO`（`$NBO NAOMO $END`） | NBO 输入关键词，使 NBO 输出 NAO 基下的 MO 系数矩阵；默认 NBO 不输出此矩阵，必须在 `$NBO ... $END` 间手动添加；对应 Gaussian 输入示例为 `#P b3lyp/6-31g* pop=nboread` 路线加尾行 `$NBO NAOMO $END`，且任务须为单点任务 | [sec-3-10-orbital-composition-analysis.md](sec-3-10-orbital-composition-analysis.md) |
| `AONAO`（`$NBO AONAO DMNAO $END`） | NBO 输入关键词，输出原始基函数到 NAO 的变换矩阵；AdNDP 要求 Gaussian 路线加 `pop=nboread`、几何后加 `$NBO AONAO DMNAO $END`，启动 Multiwfn 时载入 `.out` 而非 `.fch`，可视化 AdNDP 轨道另需同名 `.fch` | [sec-3-17-adaptive-natural-density-partitioning-analysis.md](sec-3-17-adaptive-natural-density-partitioning-analysis.md) |
| `$NBO archive file=C:\Li5+ $END` | NBO 输入关键词写法示例（`.gjf` 末行改写），使 Gaussian 运行后产生 `.47` 文件（含 Fock 矩阵）；AdNDP 界面选项 16 输入该 `.47` 路径即可打印各已取 AdNDP 轨道能量 | [sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md](sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md) |
| `$NBO plot file=C:\NH2COH $END` | NBO 输入关键词写法示例，与 `pop=nboread` 联用产生 `.31`~`.41` plot 文件；载入 `.31`（基函数信息）+ `.37`（NBO 信息）后可在主功能 0 查看 NBO/NAO/NHO（`.32`~`.40` 依次对应 PNAO/NAO/PNHO/NHO/PNBO/NBO/PNLMO/NLMO/MO） | [sec-3-2-showing-molecular-structure.md](sec-3-2-showing-molecular-structure.md) |
| `pop=saveNBO` / `pop=saveNLMO` | Gaussian 路线关键词，把 NBO/NLMO 存入 checkpoint，对应 `.fch` 可直接载入主功能 0 查看 NBO，或作为 LOBA/mLOBA 分析输入；HF/DFT 首行加 `saveNBOene`，post-HF 加 `density` 时首行加 `saveNBOocc` | [sec-3-2-showing-molecular-structure.md](sec-3-2-showing-molecular-structure.md) |
| `bndidx` | NBO 程序关键词，打印 NAO 基 Wiberg 键级；Multiwfn 键级选项 -2 只输两个原子序号时的结果与 `bndidx` 打印值完全一致 | [sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md) |
| GENNBO / `.47` 文件 | 独立 NBO 程序（又称 GENNBO）及其输入/输出文件；可在 `.47` 的 `$NBO...$END` 域中加入 `NAOMO` 后载入做 Yoshizawa 分析；AdNDP 轨道能量也可由 `.47` 的 `$FOCK` 提供；主功能 100 子功能 2 可导出 GENNBO 输入（`.47`） | [sec-3-10-orbital-composition-analysis.md](sec-3-10-orbital-composition-analysis.md) |
| `$FOCK`（`.47`） | `.47` 文件中的 Fock 矩阵段；AdNDP 选项 16 算轨道能量时，能量可由 Fock 矩阵文本或 `.47` 的 `$FOCK` 提供 | [sec-3-17-adaptive-natural-density-partitioning-analysis.md](sec-3-17-adaptive-natural-density-partitioning-analysis.md) |
| `#P` | Gaussian 路线必须以 `#P` 开头才能在输出中记录 SCF 每步中间信息（监控 SCF 收敛、碎片组合 `new.gjf` 跑完取首末迭代能量都依赖它）；只写 `#` 则无中间信息 | [sec-3-100-other-functions-part-1.md](sec-3-100-other-functions-part-1.md) |
| `SCF=QC` / `SCF=XQC`（不兼容 `SCF=DM`） | SCF 收敛监控功能兼容的 Gaussian SCF 算法关键词；`SCF=DM` 不兼容 | [sec-3-100-other-functions-part-1.md](sec-3-100-other-functions-part-1.md) |
| `IOp(3/33=1)`（`IOp(3/33=1) nosymm guess=only`） | 分子间轨道重叠积分的二聚体 Gaussian 输出路线要求；Multiwfn 从该文件读取重叠矩阵，MO 本身不用（`guess=only` 只存初猜） | [sec-3-100-other-functions-part-1.md](sec-3-100-other-functions-part-1.md) |
| `guess=only` / `guess(save,only)` / `guess=read` | 二聚体轨道重叠计算中二聚体用 `guess(save,only)` 只存初猜；碎片组合初猜输出的 `new.gjf` 靠读入碎片轨道作初猜；二聚体中单体顺序与载入顺序须一致 | [sec-4-100-other-functions-part-1.md](sec-4-100-other-functions-part-1.md) |
| `IOp(3/32=2)` | 用 Gaussian 跑弥散函数体系的 `new.gjf` 时若在 Link401 出错，加上此关键词再试 | [sec-3-100-other-functions-part-1.md](sec-3-100-other-functions-part-1.md) |
| `IOp(9/40=4)` / `IOp(9/40=5)` | Gaussian 激发计算输出组态系数的 IOp：主功能 18 空穴–电子分析要求加 `IOp(9/40=4)`（否则只载入极少组态，空穴/电子积分偏离 1.0）；子功能 5 跃迁偶极矩/SOS 若 Normalization 偏离期望则改用 `IOp(9/40=5)` 输出更多组态 | [sec-3-21-electron-excitation-analysis.md](sec-3-21-electron-excitation-analysis.md) |
| `TPrint 1E-8` / `TPrint 1E-10` | ORCA 端对应 `IOp(9/40)` 的组态输出阈值：空穴–电子分析用 `TPrint 1E-8`，跃迁偶极矩 Normalization 不对时改用 `TPrint 1E-10` | [sec-3-21-electron-excitation-analysis.md](sec-3-21-electron-excitation-analysis.md) |
| `freq` / `freq=raman` / `freq=VCD` / `freq=ROA` / `freq=anharm` / `freq=intmodes` | 主功能 11 光谱输入的 Gaussian 频率任务关键词：`freq` 画 IR，`freq=raman` 画 Raman，`freq=VCD`/`freq=ROA` 画 VCD/ROA，`freq=anharm` 为非谐（Multiwfn 会提示选非谐数据），`freq=intmodes` 输出内坐标振动模式供 PVS/PVDOS-RIC 用 | [sec-3-13-plotting-spectra.md](sec-3-13-plotting-spectra.md) |
| `CPHF=rdfreq`（几何后空行写入射光频率） | 预共振 Raman 的 Gaussian 任务关键词：`freq=raman` 另加 `CPHF=rdfreq`，并在几何后空行写入射光频率如 `300nm 400nm 500nm`；ROA 任务同样在几何后空行指定入射频率 | [sec-3-13-plotting-spectra.md](sec-3-13-plotting-spectra.md) |
| `polar` + `CPHF=RdFreq` / `DCSHG`（几何后给频率，输入须用 `#P`） | Gaussian（超）极化率任务关键词：跑 `polar` 任务输入须用 `#P`；频率相关计算需在几何后给频率并用 `CPHF=RdFreq`/`DCSHG`，再进主功能 24 子功能 1 解析 | [sec-3-27-hyperpolarizability-analysis.md](sec-3-27-hyperpolarizability-analysis.md) |
| `ExtraLinks=L608` | Shubin Liu 能量分解（主功能 21 子功能 2）要求的 Gaussian 输出：输入为 `.fch/.fchk` 加含 `ExtraLinks=L608` 分解量的 Gaussian 输出；输入文件末尾需按泛函写 `IOp(3/74)` 值 | [sec-3-24-energy-decomposition-analysis.md](sec-3-24-energy-decomposition-analysis.md) |
| `pop=MK` / `pop=CHELPG` + `IOp(6/33=2)`，`IOp(6/42=x)` | RESP 拟合直接从 Gaussian 输出载入拟合点+ESP 的任务关键词组合；`IOp(6/42=x)` 设 MK 点密度，建议 `x=6` 对应 Multiwfn 默认 | [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| ORCA 激发/光谱输入：`%tddft nroots 20 TDA false end`，`dosoc true`；`%elprop Polar 1 end` + `numfreq`；`%freq doVCD true end` | 主功能 11 UV-Vis/ECD 要求 ORCA TDDFT 输出（`TDA false` 关掉默认 TDA，SOC 用 `dosoc true`，sTDA/sTD-DFT 亦支持）；Raman 需 `%elprop Polar 1 end` + `numfreq`，VCD 需 `%freq doVCD true end`；ORCA SOC-TDDFT 输出可选载入 SOC 修正数据 | [sec-3-13-plotting-spectra.md](sec-3-13-plotting-spectra.md) |
| ORCA NMR 输入：`! B3LYP/G 6-31G* NMR cpcm(chloroform) RIJK autoaux` | ORCA NMR 光谱输入关键词示例；Gaussian NMR 示例为 `# B972/def2tzvp scrf=solvent=chloroform NMR`；CP2K NMR 用 `.data` 文件 | [sec-3-13-plotting-spectra.md](sec-3-13-plotting-spectra.md) |
| sTDA 的 `tda.dat`；xtb 输出；BDF 输出；CP2K TDDFPT 输出 | 主功能 11 UV-Vis/ECD 除 Gaussian/ORCA 外还支持的激发计算输出：sTDA 的 `tda.dat`、xtb 输出、BDF TDDFT 输出、CP2K TDDFPT 输出；注意勿用 `.fch/.molden/.wfn` 作光谱输入 | [sec-3-13-plotting-spectra.md](sec-3-13-plotting-spectra.md) |
| `5d`（混合基组）/ `TV`（PBC 平移矢量） | CDA/ETS-NOCV 混合基组计算须加 `5d`（与片段计算一致）；Gaussian PBC 输入用 `TV` 给平移矢量（路线如 `#P PBEPBE/3-21g/Auto SCF=Tight`，再 `formchk` 得 `graphene.fch`）；若 PBC 未加 `nosymm` 则以 `.fch` 的 Translation vectors 为准 | [sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md) |
| `$coord` / `$periodic` / `$lattice`（Turbomole coordination 文件） | 纯文本文件第一行为 `&coord` 即被当作 Turbomole coordination 文件加载；`$coord` 段提供原子信息，若有 `$periodic` 和 `$lattice` 还提供晶胞信息 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.gms`（GAMESS-US/Firefly 输出改扩展名） | 把 GAMESS-US 或 Firefly 输出文件扩展名改为 `.gms`，Multiwfn 才能识别；点群不是 C1 时无法处理；作用类似于 `.molden` 和 `.fch`（提供坐标、GTF 和基函数信息） | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `formchk` / `.fch`与`.fchk`无区别 | Gaussian 的 checkpoint（`.chk`）须经 `formchk` 转为格式化文件；`.fch` 与 `.fchk` 内容无区别，只是 Windows/Linux 版 `formchk` 默认扩展名不同；想让 Multiwfn 直接打开 `.chk` 须在 `settings.ini` 设 `formchkpath` | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `field=z+300`（外电场单点） | 电荷位移曲线 CDC 实例中施加外电场的 Gaussian 关键词写法：`field=z+300` 施加电场，分别算有场/无场两套 `.wfn` 再积分得 CDC | [sec-4-13-process-grid-data.md](sec-4-13-process-grid-data.md) |
| 基组写法 `6-31G*` / `6-311G**` / `def2-TZVP` / `aug-cc-pVTZ` / `/Auto` | 手册实例高频基组与 PBC 基组写法：AdNDP 对基组不敏感（HF/STO-3G 已够）；ETS-NOCV/CDA 通常 def2-TZVP 这类 3-zeta 足够、勿用弥散与隐式溶剂；PBC 路线示例含 `/Auto`（如 `#P PBEPBE/3-21g/Auto SCF=Tight`） | [sec-3-26-ets-nocv-analysis.md](sec-3-26-ets-nocv-analysis.md) |
| `multiple.txt`（光谱加权/同图，NMR 文件名须含 `multiple`） | 主功能 11 多体系同图与构象加权光谱的输入文件名（其它文件名不被识别），每行“文件路径 权重或图例”；NMR 加权文件名须含 `multiple`（如 `valine_multiple.txt`），且各体系原子数相同 | [sec-3-13-plotting-spectra.md](sec-3-13-plotting-spectra.md) |

## 环境变量与文件格式
| 参数/关键词 | 含义与取值 | 出处 |
|---|---|---|
| `Multiwfnpath` | Multiwfn 安装目录。`settings.ini` 查找顺序：当前文件夹 → `Multiwfnpath` 所指路径 → 默认设置；`GUIsettings.ini` 的写入/优先载入位置也受其影响。Linux 下在 `~/.bashrc` 中如 `export Multiwfnpath=/sob/Multiwfn_3.6_bin_Linux`。 | [sec-2-3-files-of-multiwfn.md](sec-2-3-files-of-multiwfn.md) |
| `PATH`（Linux，含 Multiwfn 目录） | 把 Multiwfn 目录加入 `PATH` 后可在任意位置用 `Multiwfn` 命令启动，如 `export PATH=$PATH:/sob/Multiwfn_3.6_bin_Linux`；之后需 `chmod +x /sob/Multiwfn_3.6_bin_Linux/Multiwfn` 加可执行权限。 | [sec-2-1-install.md](sec-2-1-install.md) |
| `PATH`（Windows，含 Gaussian 目录） | 配置 IRC 等需调用 Gaussian 的教程前，除新建 `GAUSS_EXEDIR` 外还要把 Gaussian 安装目录加入 `PATH` 环境变量，否则 Windows 下无法正常调用 Gaussian。 | [sec-4-A-special-topics-and-advanced-tutorials.md](sec-4-A-special-topics-and-advanced-tutorials.md) |
| `OMP_STACKSIZE` | 每个 OpenMP 线程的栈大小。Linux 在 `~/.bashrc` 中设 `export OMP_STACKSIZE=1000M` 并配 `ulimit -s unlimited`（无效则改用 `ulimit -Sn unlimited`）；MacOS 在 `.profile` 中设 `export OMP_STACKSIZE=64000000`（单位字节）；大体系并行崩溃时应增大它（Windows 版则增大 `settings.ini` 的 `ompstacksize`）。 | [sec-2-1-install.md](sec-2-1-install.md) |
| `DISPLAY` | 纯文本远程连接服务器用 Multiwfn 时若载入文件后卡住约两秒，在 `~/.bashrc` 中加入 `export DISPLAY=":0"`。 | [sec-2-1-install.md](sec-2-1-install.md) |
| `GAUSS_EXEDIR` | Windows 下 Multiwfn 调用 Gaussian 的必需变量，值为 Gaussian 安装目录（如 `D:\study\g16w\`，假设 `g16.exe` 在其中），否则报 `No executable for file l1.exe`。前置条件是 `settings.ini` 的 `gaupath` 已设为 Gaussian 可执行文件实际路径。 | [sec-6-1-setting-up-running-environment-for-gaussian-in-windows.md](sec-6-1-setting-up-running-environment-for-gaussian-in-windows.md) |
| `GAUSS_MEMDEF` | cubegen 可分配内存上限。大 `.fch`/`.fchk` 经 Multiwfn 调 cubegen 失败常因超过默认上限，分析前执行如 `export GAUSS_MEMDEF=4GB` 即可；它是 cubegen 崩溃三原因之二（另两项见 `nouseout` 行）。 | [sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md](sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md) |
| `$SCR`（GAMESS-US） | GAMESS-US 跑完后含 `.wfn` 格式波函数信息的 `.dat` 位于 `$SCR` 定义的目录（见 `rungms` 脚本），截取 `----- TOP OF INPUT FILE FOR BADER'S AIMPAC PROGRAM -----` 与 `----- END OF INPUT FILE FOR BADER'S AIMPAC PROGRAM -----` 之间内容存为 `.wfn`。 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) |
| `.mwfn` | Multiwfn 自 3.7 定义的最理想波函数存储交换格式，严格、简洁、紧凑、可扩展；`.molden` 用得多时建议经主功能 100 子功能 2 转为 `.mwfn` 以加快加载。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.fch` / `.fchk` / `.chk` | Gaussian `formchk test.chk` 由 `%chk=test.chk` 生成；两者无区别（分别为 Windows/Linux 版 `formchk` 默认扩展名）。含虚轨道与基函数信息，比 `.wfn`/`.wfx` 丰富；`settings.ini` 设 `formchkpath` 后可直接载入 `.chk`（自动转后删除）；post-HF/TDDFT 默认仍是 HF/基态轨道，做相关分析须用主功能 200 子功能 16 生成自然轨道或带 `density` 重跑加 `guess (save,only,naturalorbitals) chkbasis` 并在首行写 `saveNO`；老 Q-Chem（≤5.0）的 `.fchk` 须设 `ifchprog=2`。 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) |
| `.wfn` | AIM 波函数文件：原子坐标、元素、轨道能量、占据数、笛卡尔 GTF 展开系数，角动量至多 `f`（`g`/`h` 按给定 21~56 编号记录时可识别），不含虚轨道。Gaussian 用 `out=wfn`（坐标后空一行写目标路径如 `C:\otoboku\H2O.wfn`）生成；MCSCF 另加 `pop=no`；post-HF 须加 `density` 否则存的仍是 HF 轨道；早于 G09 B.01 的 ROHF/RODFT 任务单占据数误写 2.0，须手动把末处 `OCC NO =` 后改为 `1.0000000`。ORCA 用 `aim` 关键词或 `orca_2aim XXX` 由 `XXX.gbw` 生成（≥4.1 用 ECP 时生不成，更推荐 `.molden`）。 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) |
| `.wfx` | `.wfn` 扩展：更高精度、无限高 GTF 角动量，独有 EDF 段（S 型 GTF 拟合 ECP 内层密度）。Gaussian 用 `out=wfx`（G09 B.01 起）生成；仅电子密度及其梯度/Laplacian、局域信息熵、RDG、`Sign(λ₂)` 及密度/Laplacian 拓扑考虑 EDF，ESP 与动能密度、ELF 等不受 EDF 影响，重元素分析这些性质须用全电子或小核 ECP；非 Gaussian 程序的 `.wfx` 无 EDF 段。EDF 正确性校验：主功能 100 子功能 4 全空间积分密度应约等于总电子数。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.molden` / `.molden.input` / `molden.inp` / `MOLDEN` | 通用波函数交换格式（含全部占/虚轨道系数、占据数、自旋、能量、对称性）。正式支持仅 Molpro、ORCA、xtb、Dalton、NWChem（球谐且 `noautosym`）、MRCC（球谐）、deMon2k、BDF、CP2K（球谐）；NWChem 必须球谐（`spherical`）且对称体系加 `noautosym`；ORCA 用 `orca_2mkl XX -molden` 由 `XX.gbw` 生成（或设 `orca_2mklpath` 直接载入 `.gbw`）；xtb 加 `--molden` 得 `molden.input`；MRCC 算完把 `MOLDEN` 改后缀；他程序文件先用附录 5 方法验波函数或经 `molden2aim`（`m2a.ini`）标准化。 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) |
| `.molden` 的 ECP 核电荷处理 | Molden 不显式记录核电荷，Multiwfn 把 `[Atoms]` 段第三列原子序号当核电荷；用赝势时须手动改为价电子数（有效核电荷），或在文件头加 `[Nval]` 段（如 `Na 9` / `Cl 7`）；ORCA ≥6.0 的文件含 `[Pseudo]` 段且标题行有 `orca` 字样时自动正确。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.gbw` | ORCA 二进制波函数文件本身不是 Multiwfn 输入格式；把 `settings.ini` 的 `orca_2mklpath` 设为 ORCA 的 `orca_2mkl` 实际路径后可直接载入（另有 `examples/scripts/gbw2fch.sh` 批量转 `.fch` 供 cubegen 用）。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.gms` | GAMESS-US/Firefly 输出文件改后缀即得，提供坐标、GTF 与基函数信息；仅保证默认 NPRINT 的 HF/DFT/TDDFT 且点群 C1 能正常载入；示例输入/输出见 `GAMESS_US.inp` 与 `UKS_cc-pVDZ.gms`。 | [sec-4-prologue-and-generation-of-input-files.md](sec-4-prologue-and-generation-of-input-files.md) |
| NBO 绘图文件 `.31`~`.40` | `.31` 记基函数信息，`.32`~`.40` 记 PNAO/NAO/PNHO/NHO/PNBO/NBO/PNLMO/NLMO/MO 系数；先输 `.31` 路径再输其一（同名可只输后缀）；只有 NBO/NLMO 轨道算实空间函数才有意义。Gaussian 端用 `pop=nboread` 加 `$NBO plot file=... $END` 或 `pop=saveNBO`（HF/DFT 首行另加 `saveNBOene`，post-HF 加 `density` 时加 `saveNBOocc`）产生。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.pdb` / `.xyz` | 只提供原子坐标。`.xyz` 多帧只读第一帧；VMD 由 MD 轨迹导出的 `.xyz` 用模拟原子名时若同目录有同名 `.pdb` 则借用其元素名；`.mol`/`.mol2` 另有连接表，EEM 电荷计算需要它。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.mol` / `.sdf` | V2000 版，原子数与键数上限各 999；`.sdf` 为带附加信息的 `.mol` 外包装。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.mol2` | 含连接表；EEM 电荷（主功能 7 选项 17）要求此类输入，离子体系先用选项 2 设净电荷。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.gro` | GROMOS/GROMACS 结构格式，只提供原子信息；按原子名加残基名猜元素，可能猜错，载入后须核对分子式。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.cif` | 记录晶体结构的标准格式；必须显式给出对称操作，否则无法生成等效原子。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.chg` | 自由格式纯文本：元素名（≤2 字符）、XYZ（Å，前三列）、电荷（第四列），空白分隔；载入显示总电荷与偶极矩；用途为在分子表面可视化原子电荷 ESP，或经主功能 7 子功能 `-2` 算库仑作用能。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.pqr` | 类 `.pdb`，坐标列之后另有电荷列与半径列（小数位不限，空白分隔）；`REMARK` 段为注释，加载跳过。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.cub` / `.cube` | Gaussian 型 cube：记原子坐标加一套实空间函数或多套轨道格点数据；载入后主功能 0 看等值面、主功能 13 处理格点；主功能 5 后处理选项 2 导出。VMD、GaussView、VESTA 均支持。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.vti` | ParaView VTK Image Data，只支持 ASCII 标量数据；与 `.cub` 相似但不含原子信息。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.dx` | 体积数据格式，如由 VMD Volmap 插件导出。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.grd` | DMol3 体积数据格式，不记录原子信息。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `.gjf`（Gaussian 输入） | 提供原子坐标、α/β 电子数（须笛卡尔坐标）；`Tv` 字段另提供晶胞信息。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| Gaussian / ORCA 输出文件 | 只提供原子信息。Gaussian 输出由 `iloadGaugeom=1`（默认，输入取向）/`2`（标准取向）控制载入最终几何与电子数；ORCA 输出由 `iloadORCAgeom=1`（默认）控制。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| CP2K `.inp` / `.restart` | 提供原子坐标与晶胞信息；原子须用 Å 笛卡尔坐标记录。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| Quantum ESPRESSO `.inp` / `.in` | 提供原子坐标与晶胞信息；只支持 `ibrav=0`。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| Turbomole coordination 文件 | 首行为 `&coord` 的纯文本；`$coord` 段给原子信息，另有 `$periodic` 与 `$lattice` 时给晶胞信息。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| VASP：`POSCAR` / `CHGCAR` / `CHG` / `ELFCAR` / `LOCPOT` | 文件名须含相应字符串且无 `.in`/`.inp` 扩展名（如 `POSCAR_Si8`）。`POSCAR` 给晶胞与原子；`CHGCAR`/`CHG` 给电子密度（自旋极化兼记自旋密度）；`ELFCAR` 给 ELF；`LOCPOT` 给单电子外势（`LVHAR=.TRUE.` 为 ESP 负值，`.FALSE.` 为 PAEM）。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| 纯文本文件 | 仅用于特殊功能，如 DOS/光谱绘制、带初猜 Gaussian 输入文件生成；文件名含 `multiple` 的加权文件、`MPP_SDP.txt` 等按各章节格式要求准备。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| 幽灵原子（`Bq` / 元素序号 0） | 任何波函数格式均允许：带基函数、无核电荷，元素序号记 0、元素名记 `Bq`，核电荷按零处理。 | [sec-2-5-input-files-and-wavefunction-types.md](sec-2-5-input-files-and-wavefunction-types.md) |
| `molden2aim` 输出 `.wfn` 的 `charge` 字段 | 该工具输出的 `charge` 是周期表序号而非有效核电荷（即使 用 ECP），与 Gaussian（ECP 下记有效核电荷，如 Lanl2DZ 下 Au 记 19.0）不一致；用 ECP 且算 ESP 时须手动改为有效核电荷；其 `g` 型 GTF 可被 Multiwfn 识别。 | [sec-5-1-make-multiwfn-support-more-quantum-chemistry-programs.md](sec-5-1-make-multiwfn-support-more-quantum-chemistry-programs.md) |
| `Default.Rou`（Windows + Gaussian） | Multiwfn 调 Gaussian 时在当前文件夹（而非 Gaussian 临时文件夹）找 `Default.Rou`；其中有重要设置（如默认 CPU 核心数）时须复制到当前文件夹才生效。 | [sec-6-1-setting-up-running-environment-for-gaussian-in-windows.md](sec-6-1-setting-up-running-environment-for-gaussian-in-windows.md) |
| `nouseout`（cubegen 日志） | cubegen 输出转存于当前文件夹 `nouseout`；调用 cubegen 后崩溃先查它。另两类常见原因：`.fch` 无波函数/缺预期密度矩阵/已损坏，或 cubegen 太旧与文件不兼容。 | [sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md](sec-5-7-make-use-of-cubegen-utility-in-gaussian-package.md) |
