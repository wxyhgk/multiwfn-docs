# Multiwfn 菜单操作路径索引

> 按主功能编号组织：功能 | 菜单路径 | 输入 | 关键选项与产出 | 来源。

## 分功能详表

| 主功能 | 详表 | 主功能 | 详表 |
|---|---|---|---|
| 0 显示分子结构与查看轨道/等值面 | [func-00](menu/func-00.md) | 14 自适应自然密度划分 | [func-14](menu/func-14.md) |
| 1 在某一点输出所有性质 | [func-01](menu/func-01.md) | 15 模糊原子空间分析 | [func-15](menu/func-15.md) |
| 2 拓扑分析 | [func-02](menu/func-02.md) | 16 电荷分解分析与轨道相互作用图 | [func-16](menu/func-16.md) |
| 3 在一条线上输出并绘制特定性质 | [func-03](menu/func-03.md) | 17 盆分析 | [func-17](menu/func-17.md) |
| 4 在平面内输出并绘制特定性质 | [func-04](menu/func-04.md) | 18 电子激发分析 | [func-18](menu/func-18.md) |
| 5 在空间区域内输出并绘制特定性质 | [func-05](menu/func-05.md) | 19 轨道定域化分析 | [func-19](menu/func-19.md) |
| 6 检查和修改波函数 | [func-06](menu/func-06.md) | 20 弱相互作用可视化 | [func-20](menu/func-20.md) |
| 7 布居分析与原子电荷计算 | [func-07](menu/func-07.md) | 21 能量分解分析 | [func-21](menu/func-21.md) |
| 8 轨道成分分析 | [func-08](menu/func-08.md) | 22 概念密度泛函理论分析 | [func-22](menu/func-22.md) |
| 9 键级分析 | [func-09](menu/func-09.md) | 23 ETS-NOCV 分析 | [func-23](menu/func-23.md) |
| 10 态密度与光电子能谱 | [func-10](menu/func-10.md) | 24 （超）极化率分析 | [func-24](menu/func-24.md) |
| 11 光谱绘制 | [func-11](menu/func-11.md) | 25 电子离域与芳香性分析 | [func-25](menu/func-25.md) |
| 12 分子表面定量分析 | [func-12](menu/func-12.md) | 100 其他功能1 | [func-100](menu/func-100.md) |
| 13 处理格点数据 | [func-13](menu/func-13.md) | 200 其他功能2 | [func-200](menu/func-200.md) |

## 主功能 0–6（结构/点线面体/波函数检查）
| 功能 | 菜单路径 | 输入 | 关键选项与产出 | 来源 |
|---|---|---|---|---|
| 显示分子结构、查看轨道/格点等值面 | 主功能0（显示分子结构与查看轨道/等值面） | 原子坐标；看轨道需含 GTFs/轨道信息的 .fch/.wfn/.molden 等，看等值面需 .cub/.grd | Isosur. quality 调格点精度，Show+Sel. Isosur#2 双轨道叠加显示 | [3.2](sec-3-2-showing-molecular-structure.md) |
| 测量键长、键角、二面角 | 主功能0 → Tools → Measure geometry | 原子坐标 | 输入两个/三个/四个原子序号，返回键长/键角/二面角 | [3.2](sec-3-2-showing-molecular-structure.md) |
| 批量绘制轨道图 | 主功能0 → Tools → Batch plotting orbitals | 含轨道信息的波函数文件 | 将大量选定轨道分别保存为图像文件 | [3.2](sec-3-2-showing-molecular-structure.md) |
| 片段识别、元素原子序号查询、坐标/内坐标导出 | 主功能0 → Tools → Select fragment / Get atom indices of a given element / Print XYZ coordinates / Export all internal coordinates（无 GUI 版输入 geomparm） | 原子坐标（.mol/.mol2 直接用自带连接信息） | 高亮片段并返回原子编号，或导出 int_coord.txt | [3.2](sec-3-2-showing-molecular-structure.md) |
| 在某一点输出所有实空间函数值 | 主功能1（在某一点输出所有性质） | GTFs（依所选函数而定）+ 原子坐标；仅坐标文件（如 .pdb）只输出基于 promolecular 密度的有限函数 | f? 选函数、o? 选轨道、d 分解轨道贡献；附梯度/Hessian，电子密度另给应力张量 | [3.3](sec-3-3-outputting-all-properties-at-a-point.md) |
| 沿一条线绘制特定性质曲线 | 主功能3（在一条线上输出并绘制特定性质） | GTFs（核电荷 ESP 与 RDG 等 promolecular 近似除外）+ 原子坐标 | 两种定线方式（两个原子序号自动延长 / 两个端点坐标），数据导出 line.txt，可定位极大极小值 | [3.4](sec-3-4-outputting-and-plotting-specific-property-in-a-line.md) |
| 在平面内绘制特定性质（填充色图/等值线图/浮雕图/梯度线图/矢量场图） | 主功能4（在平面内输出并绘制特定性质）→ 选实空间函数 → 选图类别 → 设格点 → 选平面定义模式1-8 | GTFs（依所选函数而定）+ 原子坐标 | 8 种平面定义模式（XY/XZ/YZ/三原子/三点/原点+矢量/切键平面/局域平面），后处理调色标等值线、导出 plane.txt | [3.5](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) |
| 绘制 Becke/Hirshfeld 权重平面图 | 主功能4 → 隐藏选项111（Becke 权重/交叠权重）/ 112（Hirshfeld 权重） | 原子坐标 | 绘制指定原子的 Becke 权重或原子/片段 Hirshfeld 权重 | [3.5](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) |
| 在平面图上叠加临界点、拓扑路径与盆间路径 | 先主功能2（拓扑分析）搜索临界点并生成路径 → 主功能4 按常规绘平面图 → 后处理选项 4 / Generate interbasin paths | GTFs + 原子坐标 | 选项 4 设 CP 类别与标记/路径颜色，选项设距离阈值与盆间路径步长×迭代数 | [3.5](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) |
| 生成空间格点数据/cube 文件并查看等值面 | 主功能5（在空间区域内输出并绘制特定性质）→ 格点模式1-11 → 后处理 -1 看等值面 / 2 导出 .cub / 3 导出 output.txt | 原子坐标 + GTFs（依所选函数而定） | 模式1-3快/中/高精度、模式4-7自定义格点、模式8套用已有 cube 格点、模式10 GUI 设盒子、模式11片段扩展盒子 | [3.6](sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md) |
| 计算 Becke/Hirshfeld 权重的空间格点 | 主功能5 → 隐藏选项111（Becke 权重）/ 112（Hirshfeld 权重） | 原子坐标 | 输出指定原子 Becke 权重或原子/片段 Hirshfeld 权重的格点数据 | [3.6](sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md) |
| 计算任意分布点集的函数值 | 主功能5 → 100 Load a set of points from external file | 点坐标文本文件（首行点数，Bohr 单位）+ GTFs | 载入点坐标批量计算函数值，输出坐标+函数值文本文件 | [3.6](sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md) |
| 只显示特定片段的等值面 | 主功能5 后处理 → 9（片段 Hirshfeld 加权） | 原子坐标 + 格点数据 | 输入片段原子序号，格点数据乘 Hirshfeld 权重后远离片段处归零 | [3.6](sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md) |
| 多个波函数的自定义运算 | 主功能3/4/5 → 自定义操作子功能 | 多个波函数文件（如 a.wfn、b.wfn、c.wfn） | 支持＋−*/任意多个波函数组合，如密度差、福井函数、电子密度差 | [3.7](sec-3-7-custom-operation-promolecular-and-deformation-properties.md) |
| 计算前分子性质与变形性质 | 主功能3/4/5 → 子功能 -1（前分子性质）/ -2（变形性质） | 分子波函数 + atomwfn 目录原子 .wfn（缺失时自动调 Gaussian 生成并球化） | 变形性质＝分子实际性质 − 前分子性质，如变形密度揭示电荷转移与成键 | [3.7](sec-3-7-custom-operation-promolecular-and-deformation-properties.md) |
| 检查波函数内容 | 主功能6（检查和修改波函数）→ 子功能1（GTF 信息）/ 2（基函数）/ 3（轨道基本信息）/ 4（轨道详细系数）/ 5（系数矩阵）/ 6（密度矩阵）/ 7（积分矩阵与重叠矩阵本征值） | 波函数文件；子功能2/5/6/7 需含基函数信息 | 打印 GTF、基函数、轨道、矩阵信息，检查线性依赖与波函数正确性 | [3.8](sec-3-8-checking-and-modifying-wavefunction.md) |
| 定义分子片段丢弃无关 GTF | 主功能6 → 子功能 -3（按原子序号定义片段）/ -4（按排除原子定义片段） | 波函数文件（GTFs + 原子坐标） | 丢弃中心不在片段内的 GTF，加速格点计算或只取片段贡献；不可逆 | [3.8](sec-3-8-checking-and-modifying-wavefunction.md) |
| 修改 GTF 与轨道系数/占据数/能量 | 主功能6 → 子功能11（交换 GTF）/ 21-25（改 GTF 中心/类型/指数/系数）/ 26（设占据数）/ 28（设轨道能量）/ 29-30（交换轨道信息）/ 36（反转轨道相位） | 波函数文件 | 置零占据数以屏蔽轨道贡献，修正轨道能量以绘制 DOS，交换/设定系数与能量 | [3.8](sec-3-8-checking-and-modifying-wavefunction.md) |
| 平移/复制/旋转波函数与坐标 | 主功能6 → 子功能31（平移）/ 32（平移复制超胞）/ 33（旋转 X→Y→Z） | 波函数文件（GTFs + 原子坐标） | 输入平移矢量及单位（32 另输复制次数），近似由原胞波函数构建超胞波函数 | [3.8](sec-3-8-checking-and-modifying-wavefunction.md) |
| 按轨道类别丢弃贡献（核轨道/IRREP/整数占据/R转U） | 主功能6 → 子功能34（核轨道占据置零）/ 35（IRREP 丢弃）/ 37（R/RO 转 U）/ 38（整数占据 Aufbau 化） | 波函数文件；35 仅 .mwfn/.molden/.gms 且限 SCF 波函数 | 丢弃核轨道或指定 IRREP 贡献，ROKS 转 U 以做 CDA，整数化占据并修正波函数类型 | [3.8](sec-3-8-checking-and-modifying-wavefunction.md) |
| 保存修改后的波函数 | 主功能6 → 子功能0（存 new.wfn），或回主菜单 → 主功能100 → 子功能2 存其它格式 | 当前内存中的波函数 | 保存为 new.wfn（自动丢弃零占据轨道与无 GTF 原子），其它格式经主功能100转存 | [3.8](sec-3-8-checking-and-modifying-wavefunction.md) |

## 主功能 7–12（布居/轨道组成/键级/DOS/光谱/拓扑/表面）
| 功能 | 菜单路径 | 输入 | 关键选项与产出 | 来源 |
|---|---|---|---|---|
| Mulliken 布居与原子电荷 | 主功能7（布居分析与原子电荷）→ 5 → 子功能1 | 含基函数信息的波函数文件（.fch/.molden/.mwfn/.wfn 等） | 子功能1打印基函数/壳层/角动量布居与原子电荷；-1 可把大体系输出重定向到文本文件 | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| Mulliken 总原子布居矩阵分解 | 主功能7（布居分析与原子电荷）→ 5 → 子功能2 | 含基函数信息的波函数文件 | 输出总原子布居矩阵，对角元为局域项、非对角元×2 为原子对交叉项 | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| Mulliken 总基函数布居矩阵分解 | 主功能7（布居分析与原子电荷）→ 5 → 子功能3 | 含基函数信息的波函数文件 | 输出总基函数布居矩阵，可选把各占据轨道贡献导出到 grobasdcp.txt（文件巨大慎用） | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| 占据轨道对原子布居的贡献 | 主功能7（布居分析与原子电荷）→ 5 → 子功能4 | 含基函数信息的波函数文件 | 把各占据轨道对原子布居的贡献输出到 atmpopdcp.txt | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| Löwdin 布居分析 | 主功能7（布居分析与原子电荷）→ 6 | 含基函数信息的波函数文件 | 先做 Löwdin 正交化再做 Mulliken 型划分；基组稳定性略好但物理意义不更优 | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| SCPA 修正 Mulliken 布居（Ros & Schuit） | 主功能7（布居分析与原子电荷）→ 7 | 含基函数信息的波函数文件 | 用 Ros-Schuit 交叉项划分改进 Mulliken；输出同 Mulliken | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| Stout-Politzer 修正 Mulliken 布居 | 主功能7（布居分析与原子电荷）→ 8 | 含基函数信息的波函数文件 | 用 Stout-Politzer 交叉项划分；输出同 Mulliken | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| Bickelhaupt 修正 Mulliken 布居 | 主功能7（布居分析与原子电荷）→ 9 | 含基函数信息的波函数文件 | 用 Bickelhaupt 定义的基函数布居；输出同 Mulliken | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| Hirshfeld 原子电荷 | 主功能7（布居分析与原子电荷）→ 1 | GTF + 原子坐标（.fch/.molden/.mwfn 等） | 基于变形密度实空间积分；电荷总和应接近整数否则调大 settings.ini 的 radpot/sphpot；可选输出 .chg | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| VDD 原子布居 | 主功能7（布居分析与原子电荷）→ 2 | GTF + 原子坐标 | 权重函数换成类 Voronoi 胞划分，其余同 Hirshfeld；一般建议直接用 Hirshfeld | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| Becke 原子电荷（含原子偶极矩校正） | 主功能7（布居分析与原子电荷）→ 10 | GTF + 原子坐标 | 用 Becke 权重做原子空间划分，无需原子波函数文件 | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| ADCH 原子电荷 | 主功能7（布居分析与原子电荷）→ 11 | GTF + 原子坐标 | Hirshfeld 电荷 + 原子偶极矩校正电荷，能精确复现当前水平的偶极矩 | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| CHELPG ESP 拟合电荷 | 主功能7（布居分析与原子电荷）→ 12 → 选项1开始拟合 | GTF + 原子坐标 | 选项2~4设格点、选项5选ESP类型（含跃迁ESP即TrEsp）、选项8偶极约束、选项10选半径、选项-1/-2/-3支持外部拟合点/额外拟合中心/检验给定电荷；输出拟合电荷与 RMSE/RRMSE | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| MK ESP 拟合电荷 | 主功能7（布居分析与原子电荷）→ 13 | GTF + 原子坐标 | 与 CHELPG 唯一区别是拟合点分布在各原子 vdW 半径 1.4/1.6/1.8/2.0 倍层上；选项2设点密度、选项3设层数 | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| AIM（Bader）原子电荷 | 主功能7（布居分析与原子电荷）→ 14 | GTF + 原子坐标 | 选格点质量后自动用原子中心+均匀格点做盆积分并修正盆边界，直接打印 AIM 电荷（比盆模块更方便） | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| Hirshfeld-I 原子电荷 | 主功能7（布居分析与原子电荷）→ 15 → 选项0开始迭代 | GTF + 原子坐标；另需各元素带电态 .rad 文件（examples/atmrad 自带，缺失时可调 Gaussian 自动生成） | 迭代优化原子空间；选项-3 控制距离截断加速；收敛后打印归一化 HI 电荷，可输出 .chg | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| CM5 / 1.2×CM5 电荷 | 主功能7（布居分析与原子电荷）→ 16 / -16 | GTF + 原子坐标 | 先算 Hirshfeld 再加经验键级校正；1.2×CM5 适合 OPLS-AA 联用的分子动力学；设 uESEinp=1 可生成 uESE 溶剂化模型输入 | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| EEM 原子电荷 | 主功能7（布居分析与原子电荷）→ 17 → 选项0计算 | 含连接信息的 .mol/.mol2 文件（离子体系先用选项2设净电荷） | 选项1选内置参数集（Mulliken/MK/NPA 拟合三套）或从外部文件载入；极快，适合大体系粗估 | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| RESP 电荷 / 带约束的 ESP 拟合 | 主功能7（布居分析与原子电荷）→ 18 → 选项1两步标准RESP / 选项2一步拟合 | 含 GTF 的波函数文件；多构象拟合时用选项-1提供“文件路径+权重”列表 | 选项3选MK/CHELPG格点、选项4设惩罚函数、选项5设等价约束、选项6设电荷约束、选项7处理连通性；支持多构象加权与 TrEsp | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| PEOE（Gasteiger）电荷 | 主功能7（布居分析与原子电荷）→ 19 | 仅原子坐标（建议用优化过的几何以正确判断连通性；.mol/.mol2 可直接提供连通性） | 进入即打印电荷；仅支持 H/C/N/P/O/S/F/Cl/Br/I，不支持带电体系；可用 PEOEinit.txt 自定义初始电荷 | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| MBIS 电荷 | 主功能7（布居分析与原子电荷）→ 20 → 选项1开始迭代 | GTF + 原子坐标 | 迭代优化类 Slater 壳层布居与宽度；选项-2 可打印收敛的壳层布居 N 与宽度 σ；支持到 Rn | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| cMBIS / EMBIS / AEMBIS 电荷 | 主功能7（布居分析与原子电荷）→ 21 / 22 / 23 | GTF + 原子坐标 | Jensen 组贡献的带多极矩约束/椭球原子变体；进入后先选积分格点（高阶多极建议 fine/ultrafine）；额外输出原子体积与键级矩阵 | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| 碎片电荷求和与碎片间静电作用能 | 主功能7（布居分析与原子电荷）→ -1 定义碎片；→ -2 算碎片间库仑作用能 | 任意已算出电荷的任务（-2 需载入 .chg/.pqr 文件） | -1 定义碎片后原子电荷打印时附带碎片电荷；-2 用经典库仑公式算两碎片静电相互作用能（可用于激子耦合分析） | [3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) |
| 特定轨道的基函数/壳层/原子成分 | 主功能8（轨道成分分析）→ 1 / 2 / 3（Mulliken / Stout-Politzer / SCPA） | 含基函数信息的波函数文件（NBO 则分析 NBO） | 输入轨道序号即打印该轨道的基函数、壳层、原子成分 | [3.10](sec-3-10-orbital-composition-analysis.md) |
| 片段对轨道的成分与片段间成分 | 主功能8（轨道成分分析）→ -1 / -2 定义片段1/2 → 4 / 5 / 6 | 含基函数信息的波函数文件 | -1/-2 用基函数/壳层/原子混合定义片段；4/5/6 一次打印所有轨道的片段成分（Mulliken 与 Stout-Politzer 还给出 c² 项、内外交叉项及片段间交叉项） | [3.10](sec-3-10-orbital-composition-analysis.md) |
| NAO 轨道成分分析 | 主功能8（轨道成分分析）→ 7 | 含 NAO 基 MO 系数矩阵的 NBO 输出文件（NBO 输入须加 NAOMO 关键词） | 选项0看单轨道成分、选项1看片段对一批轨道的贡献、选项2选输出模式（默认只显示大于阈值的非 Rydberg 项） | [3.10](sec-3-10-orbital-composition-analysis.md) |
| Hirshfeld / Hirshfeld-I 轨道成分 | 主功能8（轨道成分分析）→ 8 / 10 | 原子坐标 + GTF | 实空间积分配方，基组稳定性好；-9 定义片段、-2 看某原子在一批轨道中的成分、-4 导出全矩阵到 orbcomp.txt；Hirshfeld-I 版更贵而无必要 | [3.10](sec-3-10-orbital-composition-analysis.md) |
| Becke 轨道成分 | 主功能8（轨道成分分析）→ 9 | 原子坐标 + GTF | 与 Hirshfeld 版相同用法，但无需原子波函数文件 | [3.10](sec-3-10-orbital-composition-analysis.md) |
| AIM 盆贡献的轨道成分 | 主功能17（盆分析）→ 11 | 原子坐标 + GTF | 在 AIM 划分下算轨道成分；耗时远高于其它方法一般不推荐 | [3.10](sec-3-10-orbital-composition-analysis.md) |
| LOBA / mLOBA 氧化态评估 | 主功能8（轨道成分分析）→ 100 | 含定域轨道的 .mwfn/.fch/.molden（或 Gaussian pop=saveNBO/saveNLMO 的 .fch） | 输入阈值（如 50）得 LOBA 氧化态，输入 m 得无阈值 mLOBA 氧化态（推荐）；-1 可定义片段并输出片段氧化态 | [3.10](sec-3-10-orbital-composition-analysis.md) |
| Mayer 键级 | 主功能9（键级分析）→ 1 | 含基函数信息的波函数文件 | 输入原子序号对即输出 Mayer 键级；-1 可预定义两片段并同时输出片段间总键级 | [3.11](sec-3-11-bond-order-analysis.md) |
| 多中心键级 MCBO | 主功能9（键级分析）→ 2（标准）/ -2（NAO 基）/ -3（Löwdin 基，隐藏选项） | 选项2/-3 需基函数；选项-2 需带 DMNAO 关键词的 NBO 输出文件（不可用 .fch） | 按顺序输入环原子序号；有弥散函数时必须用 -2；settings.ini 的 iMCBOtype=2 可直接打印多中心指数 | [3.11](sec-3-11-bond-order-analysis.md) |
| Löwdin 基 Wiberg 键级 | 主功能9（键级分析）→ 3 | 含基函数信息的波函数文件 | Löwdin 正交化基下的 Wiberg 键级，对基组依赖小于 Mayer | [3.11](sec-3-11-bond-order-analysis.md) |
| Mulliken 键级与分解 | 主功能9（键级分析）→ 4 计算 / 5 分解 | 含基函数信息的波函数文件 | 最早的键级定义；选项5 可做分解分析 | [3.11](sec-3-11-bond-order-analysis.md) |
| 轨道占据微扰 Mayer 键级 | 主功能9（键级分析）→ 6 | 含基函数信息的波函数文件 | 给出特定轨道对 Mayer 键级的贡献，用于指认成键/反键轨道作用 | [3.11](sec-3-11-bond-order-analysis.md) |
| 模糊键级 FBO | 主功能9（键级分析）→ 7 | GTF + 原子坐标 | 基于模糊重叠空间的 Mayer 型键级，对弥散函数稳健 | [3.11](sec-3-11-bond-order-analysis.md) |
| 拉普拉斯键级 LBO | 主功能9（键级分析）→ 8 | GTF + 原子坐标 | 基于模糊重叠空间中电子密度拉普拉斯的共价键级定义 | [3.11](sec-3-11-bond-order-analysis.md) |
| NAO 基 Wiberg 键级的原子轨道对分解 | 主功能9（键级分析）→ 9 | 含 NAO 信息的 NBO 相关输入 | 输入两个原子序号即打印不可忽略的 NAO 对/壳对贡献与总 Wiberg 键级 | [3.11](sec-3-11-bond-order-analysis.md) |
| 本征键强度指数 IBSI | 主功能9（键级分析）→ 10 → 选项0开始计算 | 仅坐标即可（IGM-pro/mIGM）；IGMH 版需 GTF | 选项2选 IGM 形式（默认 IGM-pro 最接近原文）、选项3限定局域区域、选项4设 H2 参考值、选项5设打印距离阈值（默认 3.5 Å） | [3.11](sec-3-11-bond-order-analysis.md) |
| AV1245 / AVmin 大环芳香性指数 | 主功能200（其它功能）→ 19 | 原子坐标 + 基函数；NAO 版需带 DMNAO 的 NBO 输出 | 按成环顺序输入原子序号（d 模式可自动推测连接顺序）；输出 AV1245、各 4c-ESI 与 AVmin；有弥散函数时用 NAO 版 | [3.11](sec-3-11-bond-order-analysis.md) |
| AIM 盆间离域指数 DI | 主功能9（键级分析）→ 12 | 原子坐标 + 基函数 | 选网格质量后用原子中心+均匀格点算 AIM 盆间离域指数，可视为键级的度量（极性键会偏低） | [3.11](sec-3-11-bond-order-analysis.md) |
| TDOS / PDOS / OPDOS 态密度图 | 主功能10（DOS/PES/COHP）→ -1 定义片段 → 0 绘图 | 画 PDOS/OPDOS 需 .mwfn/.fch/.molden/.gms；仅 TDOS 可用 Gaussian 单点输出（pop=full）或纯文本轨道文件 | 选项1选展宽函数、选项2设能量范围、选项3设 FWHM、选项7选 Mulliken/SCPA/Hirshfeld/Becke 成分法（有弥散函数必须用后两者）、选项8切换 eV；-6 可把 HOMO 移到零点 | [3.12](sec-3-12-plotting-density-of-states-pes-and-cohp.md) |
| 最近邻原子 OPDOS / MO-PDOS | 主功能10（DOS/PES/COHP）→ 00（最近邻 OPDOS，无需定义片段）；→ -2 定义 MO 片段后用 0 绘图 | .mwfn/.fch/.molden/.gms（含基函数信息） | 00 直接画 TDOS + 最近邻原子重叠布居态密度；-2 按分子轨道集合分组画 MO-PDOS；选项9 可用线高显示简并度 | [3.12](sec-3-12-plotting-density-of-states-pes-and-cohp.md) |
| 局域态密度 LDOS（点 / 沿线） | 主功能10（DOS/PES/COHP）→ 10 画一点的 LDOS；→ 11 画沿线的 LDOS 颜色填充图 | 同 DOS 输入（片段定义不影响 LDOS；要分解角动量贡献先用主功能6子功能25清零不需要的 GTF 系数） | 10 输入点坐标，11 输入直线起终点与点数；FWHM/能量单位/范围/缩放比选项同样生效 | [3.12](sec-3-12-plotting-density-of-states-pes-and-cohp.md) |
| 光电子能谱 PES | 主功能10（DOS/PES/COHP）→ 12 → 选项1绘图（Koopmans）/ 选项3设偏移量（广义 Koopmans） | 同 DOS 输入（.mwfn/.fch/.molden/.gms、pop=full 的 Gaussian 输出或纯文本文件） | 只能用 eV + 高斯展宽；选项6设 FWHM（默认 0.2 eV）、选项11调曲线/分立线相对高度、-3 导出 PESinfo.txt 微调各轨道强度与宽度 | [3.12](sec-3-12-plotting-density-of-states-pes-and-cohp.md) |
| COHP 分析 | 主功能10（DOS/PES/COHP）→ -7 切换到 COHP 模式 → 提供 Kohn-Sham 矩阵 → -1 定义片段（如需）→ 0 绘图 | 含基函数信息的 .mwfn/.fch/.molden + Kohn-Sham 矩阵（可由 Multiwfn 生成或从外部文件载入） | 不定义片段时画最近邻原子间 COHP，定义两片段后画片段间 COHP；后处理选项-2 打印各轨道 COHP 原始数据与 ICOHP 求和 | [3.12](sec-3-12-plotting-density-of-states-pes-and-cohp.md) |
| IR / Raman / VCD 光谱 | 主功能11（光谱绘制）→ 选 IR / Raman / VCD 类型 → 选项0绘图 | Gaussian/ORCA/CP2K 频率任务输出（Gaussian 非谐用 freq=anharm，Multiwfn 会提示选非谐数据）；Raman 活性转强度用选项19 | 选项6选展宽函数、选项8设 FWHM、选项14缩放频率（含幂律缩放）、选项15输出各跃迁贡献、选项9开关分立谱线；s/l 可存取绘制设置 | [3.13](sec-3-13-plotting-spectra.md) |
| UV-Vis / ECD 光谱 | 主功能11（光谱绘制）→ 选 UV-Vis / ECD 类型 → 选项0绘图 | Gaussian/ORCA TDDFT 输出、sTDA 的 tda.dat、xtb 输出、BDF 输出或纯文本跃迁文件（勿用 .fch/.molden/.wfn） | 选项10切换 eV/nm/1000cm⁻¹；选项20可清零除 S1 外振子强度以画荧光光谱；ORCA SOC-TDDFT 输出可选载入 SOC 修正数据 | [3.13](sec-3-13-plotting-spectra.md) |
| 预共振 Raman / ROA 光谱 | 主功能11（光谱绘制）→ 选预共振 Raman / ROA 类型并输入入射光频率 → 选项0绘图 | Gaussian freq=raman + CPHF=rdfreq（含入射光频率）输出；ROA 用 Gaussian ROA 任务输出 | 先用选项19 把活性换算为强度（需输入射频率与温度）；ROA 支持 SCP(180/90)、DCP 等形式选择 | [3.13](sec-3-13-plotting-spectra.md) |
| NMR 光谱 | 主功能11（光谱绘制）→ 选 NMR → 选项0绘图 | Gaussian/ORCA/BDF 的 NMR 任务输出，CP2K 的 .data 文件；多构象加权用文件名含 multiple 的纯文本权重文件 | 用参考屏蔽换算化学位移；选项0显示谱图，选项1存图（推荐 pdf 矢量格式）；支持构象加权与多体系同图 | [3.13](sec-3-13-plotting-spectra.md) |
| 多体系同图与构象加权光谱 | 以 multiple.txt 为输入进入主功能11 → 照常绘图；选项18切换加权显示 | 名为 multiple.txt 的纯文本文件，每行“文件路径 权重或图例” | 加权谱 = 各构象谱按权重求和（粗红曲线）；第二列非数字则为图例只同图不加权；选项21控制加权曲线与各体系曲线的显示 | [3.13](sec-3-13-plotting-spectra.md) |
| 部分振动光谱 PVS / 部分振动态密度 PVDOS | 主功能11（光谱绘制）→ 选振动光谱类型 → 选项24 定义碎片并选谱类型（t）→ q 离开 → 选项0绘图 | PVS-NC/PVDOS-NC(atom)：Gaussian/ORCA/CP2K（xtb 需另给 g98.out）频率输出；RIC 版需 Gaussian freq=intmodes；PVS-I 另需同任务的 .fch/.fchk | 支持 PVS-NC(atom/RIC)、PVS-I(atom，仅 IR)、PVDOS-NC(atom/RIC)；PVS-I 基于偶极导数分解 IR 强度，组成可略为负或超 100% 属正常 | [3.13](sec-3-13-plotting-spectra.md) |
| 由 UV-Vis 光谱预测颜色 | 主功能11（光谱绘制）→ 25（由当前可见光谱预测）；或载入两列纯文本谱直接选 0 预测 | 情形1同 UV-Vis 输入；情形2为“波长(nm) 吸光度”两列纯文本（如 examples\spectra\Allura_red_UV-Vis.txt） | 显示吸收色及其互补色（右下角大致为实际观感色）；荧光色预测先清零除 S1 外振子强度；柔性分子用 multiple.txt 加权谱预测 | [3.13](sec-3-13-plotting-spectra.md) |
| 临界点搜索 | 主功能2（拓扑分析）→ 2 从核位置 / 3 从原子对中点 / 4 从三原子三角中心 / 5 从四原子锥体中心 / 6 从球内批点 / 1 从给定起点 | 含电子密度等实空间函数的波函数文件；-11 可切换被分析函数（电子密度/ELF/LOL/拉普拉斯/ESP 等） | 模式2找 (3,-3)、模式3找 (3,-1)、模式4找 (3,+1)、模式5找 (3,+3)；ELF/LOL/拉普拉斯强烈建议用模式6的子选项-1（每原子球内撒点）多搜几次；-1 设搜索参数（步长/收敛判据/算法） | [3.14](sec-3-14-topology-analysis.md) |
| 拓扑路径与盆间表面生成 | 主功能2（拓扑分析）→ 8/9 生成键径等拓扑路径；→ 10 生成盆间表面 | 需先完成临界点搜索且至少有一个 (3,-1) 点 | -2 设路径生成参数、-3 设盆间表面参数；输入 (3,-1) 序号生成对应表面，输入 0 生成全部，负号删除 | [3.14](sec-3-14-topology-analysis.md) |
| 拓扑结果可视化 / 性质 / 管理 | 主功能2（拓扑分析）→ 0 可视化；→ 7 查临界点处函数值；→ -9 测几何；→ -4 管理临界点；→ -5 管理路径 | 同上（ESP 性质开销大，不需要时可设 settings.ini 的 ishowptESP=0 跳过） | 0 弹窗显示 CP/路径/表面并校验 Poincaré-Hopf 关系；7 给出各 CP 处全部实空间函数值与梯度/Hessian；-4 可按类型/序号/距片段距离/密度删点并导出 CPs.txt/.pdb；-5 可导出 paths.txt/.pdb、画沿路径曲线、子选项8 仅保留两片段间键径 | [3.14](sec-3-14-topology-analysis.md) |
| 基于电子密度拓扑的芳香性指数 | 主功能2（拓扑分析，实空间函数须为电子密度）→ 20 Shannon 指数；→ 21 RCP 垂直曲率 | 需已搜出环 BCP/RCP 的电子密度拓扑结果 | 20 输入环 BCP 个数与序号，SA 越小芳香性越强（0.003~0.005 为芳香/反芳香分界）；21 输入 RCP 序号并选平面拟合模式，曲率越负芳香性越强 | [3.14](sec-3-14-topology-analysis.md) |
| 分子表面定量分析（常规） | 主功能12（分子表面定量分析）→ 选项1选等值面（默认 0.001 即 vdW 面）→ 选项2选映射函数（ESP/ALIE 等）→ 0 启动分析（6 为跳过映射函数的快速版） | 至少原子坐标；ESP 等映射函数需 GTF（大体系可用原子电荷版 ESP 加速，或选项5从外部文件/cube 载入映射函数值） | 输出表面积/体积、ESP 极值点、整体/正负区平均值与方差 Π、σ² 等描述符及球形度；选项3设格点间距、选项4 等为 ESP 精度选项 | [3.15](sec-3-15-quantitative-analysis-of-molecular-surface.md) |
| 局域分子表面分析 | 主功能12（分子表面定量分析）→ 在分析设置中选局域模式：按原子分解 / 表面极值点周围区域 / 类盆分割 | 同上 | 按原子局域表面可得原子表面性质；极值点周围区域用于定量 σ-hole/π-hole 面积；类盆分割联用 ESP 可得化学上有用的表面盆 | [3.15](sec-3-15-quantitative-analysis-of-molecular-surface.md) |
| 表面分析后处理与导出 | 分析完成后后处理菜单 → 0 查看极值点；→ 6/7/8 导出表面顶点（vtx.pdb/vtx.txt/vtx.pqr）与极值点；→ 9 按映射函数值区间统计面积；→ 14 算极值点周围区域面积与平均值 | 同上 | vtx.pdb 的 B 因子记录映射函数值便于 VMD 着色；值太小的函数（如 Fukui）用 pqr 导出保证精度；-2 可导出 surf.cub 供 VMD 画彩色等值面 | [3.15](sec-3-15-quantitative-analysis-of-molecular-surface.md) |
| Hirshfeld / Becke 表面分析与指纹图 | 主功能12（分子表面定量分析）→ 选项1选 Hirshfeld/Becke 表面并输入片段原子序号 → 选项2选映射函数 → 0 启动 → 后处理 20 指纹图与局域接触分析 | 至少原子坐标（无波函数时用前分子密度）；晶体/配合物体系 | 选项0 对全表面做指纹图（di vs de），选项1/2 定义 inside/outside 原子做局域接触；选项3 统计元素对接触面积；选项4/5 导出局域接触面与全表面顶点 | [3.15](sec-3-15-quantitative-analysis-of-molecular-surface.md) |

## 主功能 13–19（格点/AdNDP/模糊空间/CDA/盆/激发/定域化）
| 功能 | 菜单路径 | 输入 | 关键选项与产出 | 来源 |
|---|---|---|---|---|
| 可视化当前格点等值面 | 主功能13（处理格点数据）→ 选项-2 | 内存格点数据或 .cub/.grd/CHGCAR | 图形窗口检查等值面，验证运算后格点有效性 | [3.16](sec-3-16-processing-grid-data.md) |
| 导出当前格点为 cube | 主功能13 → 选项0 | 内存格点数据 | 连同原子信息写出 cube 文件 | [3.16](sec-3-16-processing-grid-data.md) |
| 输出全部格点数据点 | 主功能13 → 选项1 | 内存格点数据 | 全量 X/Y/Z（Å）与数值写 output.txt | [3.16](sec-3-16-processing-grid-data.md) |
| 输出 XY/YZ/XZ 平面数据 | 主功能13 → 选项2/3/4 | 内存格点数据 | 取最接近输入 Z/X/Y 的平面输出，可做平面图 | [3.16](sec-3-16-processing-grid-data.md) |
| 输出坐标范围内平面平均数据 | 主功能13 → 选项5/6/7 | 内存格点数据 | 对 Z/X/Y 范围内多平面平均后输出 X/Y/Z/数值 | [3.16](sec-3-16-processing-grid-data.md) |
| 输出任意平面内数据点 | 主功能13 → 选项8/9 | 内存格点数据 | 输入三原子或三点定义平面+容差，可投影到 XY 平面 | [3.16](sec-3-16-processing-grid-data.md) |
| 输出指定数值范围内数据点 | 主功能13 → 选项10 | 内存格点数据 | 只输出值落在 [下限,上限] 的点；上下限相等时取 ±3% 窄带 | [3.16](sec-3-16-processing-grid-data.md) |
| 格点数据运算 | 主功能13 → 选项11 | 内存格点 + 可选第二格点文件（格点设置须一致） | 22 种运算（加减乘除、乘方、log/exp、min、加权等），就地更新格点 | [3.16](sec-3-16-processing-grid-data.md) |
| 映射另一 cube 值到等值面 | 主功能13 → 选项12 | 电子密度格点 + 同格点设置的 ESP cube | 按等值±百分比偏差取面点，输出其坐标与另一文件中数值（如 vdW 面 ESP） | [3.16](sec-3-16-processing-grid-data.md) |
| 屏蔽片段内外区域 | 主功能13 → 选项13 | 内存格点数据 | 输入 vdW 缩放因子与期望值，片段 vdW 球外（缩放为负则为内）格点置为该值 | [3.16](sec-3-16-processing-grid-data.md) |
| 屏蔽两片段重叠区之外 | 主功能13 → 选项14 | 内存格点数据 | 仅保留两片段缩放 vdW 区叠加区，其余置指定值，便于看片段间等值面 | [3.16](sec-3-16-processing-grid-data.md) |
| 按数值范围替换格点值 | 主功能13 → 选项15 | 内存格点数据 | 落在 [下限,上限] 的值统一设为期望值 | [3.16](sec-3-16-processing-grid-data.md) |
| 线性缩放数据范围 | 主功能13 → 选项16 | 内存格点数据 | 超界截断后线性映射旧区间到新区间 | [3.16](sec-3-16-processing-grid-data.md) |
| 格点统计 | 主功能13 → 选项17 | 内存格点数据 | 输出限制区内最小/最大/均值/RMS/体积/积分与正负总重心 | [3.16](sec-3-16-processing-grid-data.md) |
| 积分/局域积分/平面平均曲线 | 主功能13 → 选项18 | 内存格点数据（研究方向须满足正交条件） | 选 X/Y/Z 方向与范围，绘制导出曲线；电子密度差即电荷位移曲线 | [3.16](sec-3-16-processing-grid-data.md) |
| 盒内平移格点数据 | 主功能13 → 选项19 | 内存格点数据（正交/非正交均可，周期体系常用） | 按三轴分数平移，超盒绕回，可选把原子一并绕回 | [3.16](sec-3-16-processing-grid-data.md) |
| 周期性复制格点数据 | 主功能13 → 选项20 | 内存格点数据（盒子与单胞重合） | 沿盒矢量复制 N 次，可同时复制原子，得超胞格点与结构 | [3.16](sec-3-16-processing-grid-data.md) |
| 指定原子组合搜索轨道 | 主功能14（AdNDP）→ 选项1 | NBO 输出（含 DMNAO；可视化另需 .fch+AONAO） | 构造给定原子密度子块并对角化，结果入候选列表（清空旧列表） | [3.17](sec-3-17-adaptive-natural-density-partitioning-analysis.md) |
| 穷举 N 中心轨道搜索 | 主功能14 → 选项2（配合选项3设中心数、选项4设占据阈值） | NBO 输出（含 DMNAO） | 遍历搜索列表全部 C(M,N) 组合，占据数超阈值者入候选；N 自动加一 | [3.17](sec-3-17-adaptive-natural-density-partitioning-analysis.md) |
| 从候选挑选 AdNDP 轨道 | 主功能14 → 选项0 | NBO 输出（含 DMNAO） | 按序号或取前 K 个挑入最终轨道并耗竭密度更新其余候选 | [3.17](sec-3-17-adaptive-natural-density-partitioning-analysis.md) |
| 可视化 AdNDP/候选轨道 | 主功能14 → 选项7/8 | NBO 输出 + 同名 .fch（AONAO） | GUI 按编号绘制轨道等值面，挑前先看候选形状 | [3.17](sec-3-17-adaptive-natural-density-partitioning-analysis.md) |
| 导出轨道 cube 文件 | 主功能14 → 选项9/10 | NBO 输出 + .fch | 选序号范围输出 AdNDPorbXXXX.cub，可用 VMD 显示 | [3.17](sec-3-17-adaptive-natural-density-partitioning-analysis.md) |
| 导出 .mwfn / 算成分 / 算能量 | 主功能14 → 选项14/15/16 | NBO 输出（能量另需 Fock 矩阵文本或 .47 的 $FOCK） | AdNDP.mwfn 供后续分析；NAO 法成分；Fock 期望值即轨道能量 | [3.17](sec-3-17-adaptive-natural-density-partitioning-analysis.md) |
| 模糊原子空间积分 | 主功能15（模糊原子空间分析）→ 选项1 | 波函数文件（.fch/.wfn/.molden/.mwfn 等，选项-1 选 Hirshfeld/Becke/HI/MBIS） | 对实空间函数做原子加权积分，如电子布居；选项-5 限原子，-10/-11 设参考点 | [3.18](sec-3-18-fuzzy-atomic-space-analysis.md) |
| 交叠空间积分 | 主功能15 → 选项8 | 波函数文件（仅 Becke 划分） | 计算原子对交叠区积分，正负部分开输出 | [3.18](sec-3-18-fuzzy-atomic-space-analysis.md) |
| 原子与分子多极矩及 <r²> | 主功能15 → 选项2 | 波函数文件 | 输出单极/偶极/四极/八极矩（Cartesian+球谐）与原子电子空间范围，可写 multipole.txt/atom_moment.txt | [3.18](sec-3-18-fuzzy-atomic-space-analysis.md) |
| 原子交叠矩阵 AOM/片段交叠矩阵 FOM | 主功能15 → 选项3/33 | 波函数文件 | AOM 写 AOM.txt，FOM 写 FOM.txt；SUM 偏离单位阵为精度指标 | [3.18](sec-3-18-fuzzy-atomic-space-analysis.md) |
| 定域化/离域化指数 LI/DI（模糊键级） | 主功能15 → 选项4/44 | 波函数文件 | 先算 AOM 再得 LI/DI（DI 即模糊键级），开壳层分自旋输出 | [3.18](sec-3-18-fuzzy-atomic-space-analysis.md) |
| 对位离域化指数 PDI | 主功能15 → 选项5 | 波函数文件 | 对位 DI 平均，衡量六元环芳香性 | [3.18](sec-3-18-fuzzy-atomic-space-analysis.md) |
| 芳香涨落指数 FLU/FLU-π | 主功能15 → 选项6/7 | 波函数文件 | 基于 DI 偏离参考的芳香性指数，适用任意元环 | [3.18](sec-3-18-fuzzy-atomic-space-analysis.md) |
| 凝聚线性响应核 CLRK | 主功能15 → 选项9 | 波函数文件 | 输出原子间线性响应核矩阵 | [3.18](sec-3-18-fuzzy-atomic-space-analysis.md) |
| 对位线性响应指数 PLR | 主功能15 → 选项10 | 波函数文件 | 以 CLRK 代 DI 的 PDI 型芳香性指数 | [3.18](sec-3-18-fuzzy-atomic-space-analysis.md) |
| 多中心离域化指数 | 主功能15 → 选项11 | 波函数文件 | 计算 n 中心 DI | [3.18](sec-3-18-fuzzy-atomic-space-analysis.md) |
| 信息论芳香性指数 | 主功能15 → 选项12 | 波函数文件 | 环原子信息论量（Shannon 熵等三选一）的平均值 | [3.18](sec-3-18-fuzzy-atomic-space-analysis.md) |
| 原子有效体积/极化率/C6 | 主功能15 → 选项13 | 体系波函数 + 各元素原子波函数文件 | 输出 Veff/Vfree/αeff/C6AA 与分子间 C6 | [3.18](sec-3-18-fuzzy-atomic-space-analysis.md) |
| 打印 CDA/ECDA 结果 | 主功能16（电荷分解分析）→ 选项0/1（-3 设阈值，-2 切输出到 CDA.txt） | 复合物文件 + 各片段文件（.mwfn/.fch/.molden/.gms 或 Gaussian 输出；方法基组坐标原子顺序须一致，避免弥散函数） | 输出 d/b/r 与 ECDA 净转移电子数；选项1 显示全部自然轨道 | [3.19](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md) |
| 查看复合物轨道的片段轨道组成 | 主功能16 → 选项2 | 同上 | Mulliken（或 SCPA）组成，定位关键片段轨道贡献 | [3.19](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md) |
| 导出片段轨道系数/重叠矩阵 | 主功能16 → 选项3/4 | 同上 | 写 coFO.txt（复合物轨道在 FO 基下系数）与 ovlpint.txt（FO 间重叠） | [3.19](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md) |
| 分解复合物轨道的 CDA 贡献 | 主功能16 → 选项6 | 同上 | 按 FO 对阈值过滤，揭示 d/b/r 的轨道对来源 | [3.19](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md) |
| 绘制轨道相互作用图 | 主功能16 → 选项5 | 同上（post-HF 无轨道能量时不可用） | 按能量画线、超组成判据连红线，可调标签/能量范围/平移与连接规则 | [3.19](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md) |
| 生成 basin 并定位吸引子 | 主功能17（Basin 分析）→ 选项1（选项-1 选算法/极值，-6 调聚类） | 波函数文件或 .cub/.grd 格点（或主功能5/13 预算格点） | 选实空间函数与格点（定性用中等、定量用高质量），near-grid+边界精修默认 | [3.20](sec-3-20-basin-analysis.md) |
| 可视化吸引子与 basin | 主功能17 → 选项0 | 已生成 basin | GUI 显示吸引子球与 basin，可只看 rho>0.001 区或内部 | [3.20](sec-3-20-basin-analysis.md) |
| basin 内积分实空间函数 | 主功能17 → 选项2（AIM 高精度改用选项7） | GTF 波函数或同格点设置的 .cub/.grd/内存格点 | 输出各 basin 积分与体积；选项7 用原子中心+均匀混合格点，可做边界精修 | [3.20](sec-3-20-basin-analysis.md) |
| basin 电多极矩与 <r²> | 主功能17 → 选项3（AIM 高精度改用选项8） | GTF 波函数 | 以吸引子为原点算到四极矩；选项8 用混合格点并可写 multipole.txt/atom_moment.txt | [3.20](sec-3-20-basin-analysis.md) |
| basin 定域化/离域化指数 | 主功能17 → 选项4 | GTF 波函数 | 与模糊空间 LI/DI 同理，积分域换为 basin | [3.20](sec-3-20-basin-analysis.md) |
| 输出 basin/原子重叠矩阵 | 主功能17 → 选项5/6（仅电子密度定 basin 时见6） | GTF 波函数 | BOM 写 BOM.txt，AOM 写 AOM.txt（跳非核吸引子 basin） | [3.20](sec-3-20-basin-analysis.md) |
| 导出 basin 与吸引子 | 主功能17 → 选项-5/-4/-45/-3/-2 | 已生成 basin | basinXXXX.cub/basin.cub/basinsel.cub；吸引子 pdb/pqr/txt/gjf；basinana 复用存档 | [3.20](sec-3-20-basin-analysis.md) |
| ELF 专项与外部 basin 分析 | 主功能17 → 选项12/10/9/11 | ELF basin（12/10）或外部 basin.cub（9） | 自动标 ELF 芯/价标签；HELP/HELV 孤对表征；外部 basin 的 AIM 原子贡献；basin 对轨道组成贡献 | [3.20](sec-3-20-basin-analysis.md) |
| 检查修改导出组态系数 | 主功能18（电子激发分析）→ 子功能-1 | 参考轨道文件（.fch/.molden/.gms/.mwfn）+ 组态系数文件（Gaussian/ORCA/BDF/CP2K 输出或同格式文本） | 改系数后经 -3 导出文本再做后续分析；-2 按阈值打印关键轨道对 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| 空穴-电子/跃迁密度/偶极矩密度分析 | 主功能18 → 子功能1 | 同上（两种文件） | 输出空穴电子分布、Sr/Sm 重叠、CDD、MO/原子/片段贡献与热图，可视化等值面 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| 原子/片段跃迁矩阵热图 | 主功能18 → 子功能2 | 参考轨道文件 + TDM/电荷转移等矩阵来源 | 把 ATM 转 FTM 并绘制热图，直观定位跃迁局域性 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| 基于密度差格点分析电荷转移 | 主功能18 → 子功能3 | 密度差格点（主功能5 自定义操作或外部 cube） | 直接积分 Δρ 得 CT 量（唯一不需组态系数文件的子功能） | [3.21](sec-3-21-electron-excitation-analysis.md) |
| Δr 电荷转移长度指数 | 主功能18 → 子功能4 | 参考轨道文件 + 组态系数文件 | 输出 Δr，大值指示长程 CT 激发 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| 态间跃迁电/磁偶极矩与态偶极矩 | 主功能18 → 子功能5 | 参考轨道文件 + 组态系数文件 | 输出全部态间跃迁偶极矩及各态电偶极矩 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| 自然跃迁轨道 NTO | 主功能18 → 子功能6 | 参考轨道文件 + 组态系数文件 | 对 TDM 做 SVD 得空穴/电子 NTO 对，导出可视化 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| ghost-hunter 指数 | 主功能18 → 子功能7 | 参考轨道文件 + 组态系数文件（先做空穴-电子分析得格点） | 输出 MAC 指数判别虚假长程 CT（ghost）态 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| IFCT 片段间电荷转移 | 主功能18 → 子功能8 | 参考轨道文件 + 组态系数文件 | 定义片段后输出片段间转移矩阵、CT%/LE% | [3.21](sec-3-21-electron-excitation-analysis.md) |
| 导出跃迁密度矩阵 TDM | 主功能18 → 子功能9 | 参考轨道文件 + 组态系数文件 | 构建基函数表象 TDM 并导出 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| 跃迁偶极矩的 MO 对分解 | 主功能18 → 子功能10 | 参考轨道文件 + 组态系数文件 | 量化各轨道跃迁对振子强度的贡献 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| 跃迁偶极矩的基函数/原子分解 | 主功能18 → 子功能11 | 参考轨道文件 + 组态系数文件 | 结果写 trdipcontri.txt，定位关键原子区 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| Mulliken 原子跃迁电荷 | 主功能18 → 子功能12 | 参考轨道文件 + 组态系数文件 | 输出原子跃迁电荷，用于激子耦合 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| 特定激发态自然轨道 | 主功能18 → 子功能13 | 参考轨道文件 + 组态系数文件 | 导出选中态 NO 到 .mwfn 供波函数分析 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| Λ 指数表征激发 | 主功能18 → 子功能14 | 参考轨道文件 + 组态系数文件 | 输出 Λ，小值指示长程 CT 特征 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| 打印全部态主要 MO 跃迁 | 主功能18 → 打印主要 MO 跃迁功能 | 参考轨道文件 + 组态系数文件 | 一览各态主导轨道对，快速定性 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| 电荷转移光谱 CTS | 主功能18 → CTS 功能 | 参考轨道文件 + 组态系数文件 | 基于 IFCT 输出各态重排/转移并绘制 CTS | [3.21](sec-3-21-electron-excitation-analysis.md) |
| 电子密度极化分析 | 主功能18 → 密度极化功能 | 参考轨道文件 + 组态系数文件 + 点电荷外势定义 | 输出 ρpol、展开系数与二阶能量 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| ECD/CPL 不对称因子 g | 主功能18 → 子功能18 | Gaussian/ORCA 激发输出（含跃迁电/磁偶极矩） | 输出 \|μ\|、\|m\|、夹角、旋光强度与 g 因子，可在 VMD 画偶极矢量 | [3.21](sec-3-21-electron-excitation-analysis.md) |
| 定域化占据轨道 | 主功能19（轨道定域化）→ 选项1（-6 选 PM-Mulliken/Löwdin/Becke/FB） | 含基函数文件（.mwfn/.fch/.molden/.gms，仅限 HF/DFT） | Jacob sweep 定域化，结果写 new.fch 并自动载入，附 Hirshfeld 轨道组成 | [3.22](sec-3-22-orbital-localization-analysis.md) |
| 同时定域化占据与虚轨道 | 主功能19 → 选项2 | 同上 | 占/虚分组分别定域化（互不混合）；虚轨道收敛更难耗时更长 | [3.22](sec-3-22-orbital-localization-analysis.md) |
| 定域化指定 MO 子集 | 主功能19 → 选项3 | 同上 | 仅允许所选 MO 混合，得局域区半定域轨道 | [3.22](sec-3-22-orbital-localization-analysis.md) |
| LMO 能量/中心/偶极矩 | 主功能19 → 选项-4/-8（专题1–3） | 同上（能量另需 Fock 矩阵或由 MO 重构） | 输出 LMO 能量；LMO 中心写 LMOcen.txt 并加 Bq 可视化；占据 LMO 偶极写 LMOdip.txt | [3.22](sec-3-22-orbital-localization-analysis.md) |

## 主功能 20–25（弱相互作用/能量分解/CDFT/ETS-NOCV/极化率/离域芳香性）
| 功能 | 菜单路径 | 输入 | 关键选项与产出 | 来源 |
|---|---|---|---|---|
| NCI（RDG）分析 | 主功能20（弱相互作用可视化）→ 子功能1 | 含 GTF 的波函数文件（.wfn/.wfx/.mwfn/.fch/.molden 等） | 散点图定位尖峰，导出 sign(λ₂)ρ 与 RDG 的 cube，用 RDGfill.vmd 在 VMD 中绘制颜色填充等值面图 | [3.23](sec-3-23-visual-study-of-weak-interaction.md) |
| 基于前分子密度的 NCI 分析 | 主功能20 → 子功能2 | 仅原子坐标（如 .pdb/.xyz） | 操作同常规 NCI，免波函数、适用于大体系；绘图脚本为 RDGfill_pro.vmd | [3.23](sec-3-23-visual-study-of-weak-interaction.md) |
| 平均 NCI（aNCI）分析 | 主功能20 → 子功能3 | 多帧 .xyz 轨迹（感兴趣分子位置固定） | 对多帧平均密度求 aRDG，导出平均 sign(λ₂)ρ 与热涨落指数 TFI 的 cube；一般建议改用 amIGM | [3.23](sec-3-23-visual-study-of-weak-interaction.md) |
| DORI 分析 | 主功能20 → 子功能5 | 原子坐标＋GTF | 同 NCI 流程，用 DORIfill.vmd 绘制 sign(λ₂)ρ 着色的 DORI 等值面，可同时显示共价与非共价区；作者更推荐 IRI | [3.23](sec-3-23-visual-study-of-weak-interaction.md) |
| IGM 分析 | 主功能20 → 子功能10 | 仅原子坐标（.xyz/.pdb/.mol 或波函数文件） | 定义片段后计算 δg/δg_inter/δg_intra 格点与散点图，用 IGM_inter/intra.vmd 绘图；选项6 给出原子对定量指标 δG 与 IBSIW（atmdg.txt/IBSIW.txt） | [3.23](sec-3-23-visual-study-of-weak-interaction.md) |
| IGMH 分析 | 主功能20 → 子功能11 | 含 GTF 的波函数文件（需实际电子密度做 Hirshfeld 分区） | 用法与选项同 IGM，等值面更薄、着色更合理；δg_inter 亦为第 91 号自定义函数 | [3.23](sec-3-23-visual-study-of-weak-interaction.md) |
| 范德华势可视化 | 主功能20 → 子功能6 | 仅原子坐标 | 基于 UFF 参数（探针原子由 ivdwprobe 指定，默认碳）计算 VvdW/Vrepul/Vdisp 格点，可视化等值面或导出 cube；对应自定义函数 92/93/94 | [3.23](sec-3-23-visual-study-of-weak-interaction.md) |
| IRI 与 IRI-π 分析 | 主功能20 → 子功能4 | 原子坐标＋GTF | IRI 等值面（推荐 1.0）经 IRIfill.vmd 绘制 sign(λ₂)ρ 着色图，同时揭示化学键与弱相互作用；IRI-π 需先将非 π 轨道占据数置零 | [3.23](sec-3-23-visual-study-of-weak-interaction.md) |
| 平均 IGM（aIGM）分析 | 主功能20 → 子功能12 | 多帧原子坐标 | 用法同 amIGM，但图形效果差得多，作者明确建议一律改用 amIGM | [3.23](sec-3-23-visual-study-of-weak-interaction.md) |
| 修正 IGM（mIGM）分析 | 主功能20 → 子功能-10 | 仅原子坐标 | 用法与 IGM 完全相同，以前分子密度代替实际密度，效果接近 IGMH 而成本与 IGM 相当 | [3.23](sec-3-23-visual-study-of-weak-interaction.md) |
| 平均修正 IGM（amIGM）分析 | 主功能20 → 子功能-12 | 多帧 .xyz 轨迹 | 定义片段与帧范围后计算平均 δg_inter 与平均 sign(λ₂)ρ（avgdg_inter.cub/avgsl2r.cub），用 aIGM.vmd 绘图；选项8 给出标准差与 TFI_amIGM | [3.23](sec-3-23-visual-study-of-weak-interaction.md) |
| EDA-FF 能量分解 | 主功能21（能量分解）→ 子功能1 | 体系几何文件（.xyz/.pdb/.fch 等）＋分子列表文件（含原子电荷/类型） | 定义片段后给出每对片段的静电/排斥/色散分量与原子贡献，可导出 interatm.txt 与按能量贡献着色的 .pqr 文件 | [3.24](sec-3-24-energy-decomposition-analysis.md) |
| Shubin Liu 能量分解 | 主功能21 → 子功能2 | .fch/.fchk ＋ 含 ExtraLinks=L608 分解量的 Gaussian 输出 | Multiwfn 计算空间位阻项并打印静电/量子三分量及 Pauli 动能等中间量；输入文件末尾需按泛函写 IOp(3/74) 值 | [3.24](sec-3-24-energy-decomposition-analysis.md) |
| sobEDA / sobEDAw 能量分解 | sobEDA.sh 脚本（主功能21之外，需 Gaussian＋Multiwfn 配合） | Gaussian 计算的复合物与片段能量文件（见 sobEDA 教程） | 稳健高效通用的 DFT 能量分解，作者强烈推荐；按 sobEDA_tutorial 流程运行脚本 | [3.24](sec-3-24-energy-decomposition-analysis.md) |
| 原子对色散能贡献分析 | 主功能21 → 子功能4 | 原子信息文件（.xyz/.pdb/.mol2/.gjf/.fch/.mwfn，支持周期体系）＋修改版 dftd3 程序（settings.ini 设 dftd3path） | 基于 DFT-D3(BJ) 给出原子/片段对色散能贡献（atomdisp.pqr）、色散密度（dispdens.cub）及两体系差值与片段间色散作用能 | [3.24](sec-3-24-energy-decomposition-analysis.md) |
| CDFT 整体与原子指数 | 主功能22（CDFT）→ 选项2 | N/N+1/N−1（算 ωcubic/ε 时再加 N−2）态 .wfn/.wfx/.fch/.mwfn，几何相同 | 自动算 Hirshfeld 电荷并输出电离势/亲和势/硬度/亲电性/凝聚 Fukui 等到 CDFT.txt | [3.25](sec-3-25-conceptual-density-functional-theory-analysis.md) |
| Fukui 函数与对偶描述符格点 | 主功能22 → 选项3 | 同上（N/N+1/N−1 态波函数文件） | 计算 f⁺/f⁻/f⁰ 与对偶描述符格点，可视化等值面或导出 cube；乘整体软度即得局域软度 | [3.25](sec-3-25-conceptual-density-functional-theory-analysis.md) |
| Fukui 势与对偶描述符势 | 主功能22 → 选项9 | 同上（各带电态波函数文件） | 用法同选项3但计算各态 ESP 差，得到 Vf⁺/Vf⁻ 与 DDP 格点；ESP 格点开销大、宜用稀疏格点 | [3.25](sec-3-25-conceptual-density-functional-theory-analysis.md) |
| 键对偶描述符 BDD | 主功能22 → 选项10 | 各电子态 .wfn 文件 | 依次载入各态算模糊键级并有限差分，打印每根键的 BDD（负为亲核、正为亲电） | [3.25](sec-3-25-conceptual-density-functional-theory-analysis.md) |
| CDFT 输入文件生成 | 主功能22 → 选项1（ORCA 版先经选项-2 切换） | 任意含目标体系原子信息的文件 | 输入单点关键词与各态电荷/多重度，生成 N/N+1/N−1（可选 N−2）的 Gaussian .gjf 或 ORCA .inp，可直接调用程序计算 | [3.25](sec-3-25-conceptual-density-functional-theory-analysis.md) |
| 轨道加权 Fukui 函数与对偶描述符 | 主功能22 → 选项4（设Δ）→ 选项5（查权重）→ 选项6（凝聚值）/选项7（格点） | 闭壳层单行列式文件（.mwfn/.fch/.molden/.gms，算虚轨道参与量时不用弥散函数） | 按高斯权重混合近简并前线轨道，输出 Hirshfeld 凝聚值与等值面/cube；Δ 初猜 0.1 Hartree | [3.25](sec-3-25-conceptual-density-functional-theory-analysis.md) |
| 基于电子密度的（准）简并 Fukui 函数 | 主功能22 → 选项-3（设 FMO 简并度 p/q）→ 选项1（生成输入）→ 选项2/3 | N、N+p、N−q（及 N±1 求电离势/亲和势）态波函数文件 | 考虑弛豫的密度型 fQ/ΔfQ 及相应局域性质；p/q 按前线轨道能量差判定，态多重度通常取 p+1/q+1 | [3.25](sec-3-25-conceptual-density-functional-theory-analysis.md) |
| 开壳层 Fukui 函数与对偶描述符 | 主功能22 → 子功能12 → 选项1（设简并度）→ 选项2（生成输入）→ 选项3（格点） | 含基函数与全部轨道的波函数文件 | 按自旋数变化类型分别计算 f⁺/f⁻/对偶描述符格点并可视化或导出 .cub | [3.25](sec-3-25-conceptual-density-functional-theory-analysis.md) |
| 亲核/亲电超离域性 | 主功能22 → 选项8 | 闭壳层单行列式文件（.mwfn/.fch/.molden/.gms，算 DN 时不用弥散函数） | 直接打印各原子的 DN/DE/DN0/DE0（基于 Hirshfeld 轨道组成，与弥散函数兼容） | [3.25](sec-3-25-conceptual-density-functional-theory-analysis.md) |
| 对偶离域描述符 DDD | 主功能22 → 子功能11 → 选项1（AIM 划分）/选项2（Hirshfeld 划分）/选项3（载入已有 AOM） | 闭壳层含基函数波函数文件（.fch/.molden 等） | 输入化学键即得 f⁺/f⁻/f⁽¹⁾/g⁺/g⁻/f⁽²⁾，表征离域指数对得失电子响应的不对称性 | [3.25](sec-3-25-conceptual-density-functional-theory-analysis.md) |
| ETS-NOCV 分析 | 主功能23 → 输入片段数 → 依次载入各片段波函数文件 → 后处理菜单选项-1/-2（求 NOCV 能量）、1/2（NOCV 轨道/对密度等值面）、3–5（各类变形密度）、6–10（导出 cube）、11–13（各态轨道）、14（SCPA 组成） | 复合物波函数文件＋各片段波函数文件（.fch/.mwfn/.molden 等含基函数文件，不可用 .wfn/.wfx；另需 Fock 矩阵文件或由轨道能量生成，见附录7） | 计算 NOCV 本征值/能量与对 ΔEorb 的贡献，可视化 NOCV 轨道、对密度与 Pauli/轨道/总变形密度，等值面均可导出 cube | [3.26](sec-3-26-ets-nocv-analysis.md) |
| 解析 Gaussian（超）极化率输出 | 主功能24（超极化率）→ 子功能1 → 按方法选选项1–7（选项-1 切换解析频率相关结果，选项-3 选单位，选项-4 导出张量 txt） | Gaussian polar 任务输出（输入须用 #P；频率相关计算需在几何后给频率并用 CPHF=RdFreq/DCSHG） | 以易读格式打印 μ/α/β/γ 各分量与各向同性值、各向异性、βtot、HRS/退偏比等；SHG 型 β 还可扫描 I(ΨV) 输出 HRS_angle.txt | [3.27](sec-3-27-hyperpolarizability-analysis.md) |
| SOS 方法计算（超）极化率 | 主功能24 → 子功能2 → 选项1–4（定频算 α/β/γ/δ）、选项5–7（随态数收敛）、选项15–17（随频率扫描）、选项19（β 双频扫描） | 激发能＋跃迁偶极矩纯文本文件（可由 3.21.5 功能生成）或 Gaussian CIS/TDDFT 输出（仅算极化率） | 输出各阶（超）极化率张量及相关量，扫描结果存纯文本供 Origin 等作图 | [3.27](sec-3-27-hyperpolarizability-analysis.md) |
| 两能级/三能级模型分析 | 主功能24 → 子功能2 → 选项20（输入一个态序号做两能级，两个做三能级，或范围逐个分析） | 同 SOS 计算的输入文件 | 给出关键态的跃迁偶极矩、偶极矩差、振子强度与激发能分解，便于比较不同体系 β 差异来源 | [3.27](sec-3-27-hyperpolarizability-analysis.md) |
| （超）极化率密度 | 主功能24 → 子功能3 → 选量与方向 → 选项1（生成各电场下 Gaussian 输入）→ 选项2（载入 .wfx） | 原子信息文件（.xyz/.pdb/.mwfn/.fch 等）＋不同外电场下的 .wfx 文件 | 有限差分得 ρ⁽¹⁾/ρ⁽²⁾/ρ⁽³⁾ 及其空间贡献的平面图/等值面/cube，可进一步做原子/片段贡献分析；研究前宜用 300→7→7 功能使偶极矩平行于 Z 轴 | [3.27](sec-3-27-hyperpolarizability-analysis.md) |
| 单位球与矢量表示 | 主功能24 → 子功能5 → 选项1/2/3（分别载入 α/β/γ 张量并生成 VMD 脚本） | 原子信息文件（定球半径）＋ alpha/beta/gamma.txt（由子功能1 选项-4 导出或手动按 Fortran 顺序准备） | 生成 alpha/beta/gamma.tcl（单位球）与 alpha/beta/gamma_vec.tcl（矢量表示），在 VMD 中运行即得图形 | [3.27](sec-3-27-hyperpolarizability-analysis.md) |
| 生成 ICSS 及相关量 | 主功能25（电子离域与芳香性）→ 子功能3 → 设格点 → 生成 NICS*.gjf → Gaussian 算 NMR → 载入输出选性质 → 可视化/导出 cube | Gaussian 输入模板（.gjf，须显式指定 %chk，坐标处由 Multiwfn 填充）＋运行所得 NMR 输出 | 生成各向同性/各向异性/XX/YY/ZZ 的 ICSS 格点，等值面可视化或导出 cube；settings.ini 中 NICSnptlim 控制每个输入文件的 Bq 数 | [3.28](sec-3-28-electron-delocalization-and-aromaticity-analyses.md) |
| 非平面/倾斜体系 NICS_ZZ | 主功能25 → 子功能4 → 输入环中心 → 输入拟合平面原子序号 → 输入磁屏蔽张量分量 | 含原子坐标的文件（.xyz/.pdb/.mol/.wfn/.mwfn/.fch/.molden 等；环中心可由主功能2 的 RCP 或主功能100 子功能21 得到） | 输出环平面法向量与 1 Å 上下方点坐标，法向屏蔽值的负值即 NICS(1)ZZ 或 NICS(0)ZZ | [3.28](sec-3-28-electron-delocalization-and-aromaticity-analyses.md) |
| HOMA 芳香性指数 | 主功能25 → 子功能6 → 选项0（选项1 修改/补充参数） | 仅原子坐标 | 按连接顺序输入环原子序号，输出 HOMA 值与每对原子的贡献 | [3.28](sec-3-28-electron-delocalization-and-aromaticity-analyses.md) |
| Bird 芳香性指数 | 主功能25 → 子功能6 → 选项2（选项3/4 提供键参数/调整 VK） | 仅原子坐标 | 按连接顺序输入环原子序号，输出 Bird 指数（越接近 100 芳香性越强） | [3.28](sec-3-28-electron-delocalization-and-aromaticity-analyses.md) |
| HOMAc / HOMER 指数 | 主功能25 → 子功能6a（HOMAc）/6b（HOMER） | 仅原子坐标 | 用法与 HOMA 完全相同，分别针对基态 S₀ 与 T₁ 态重新参数化，推荐用 HOMAc 代替 HOMA | [3.28](sec-3-28-electron-delocalization-and-aromaticity-analyses.md) |
| NICS-1D 扫描、INICS 与 FiPC-NICS | 主功能25 → 子功能13 → 定义扫描线 → 选项1（生成 NICS_1D.gjf）→ Gaussian 运行 → 选项2（载入输出）→ 选分量 → 绘图/算指数 | 含结构信息的文件＋Gaussian NMR 模板（含 [geometry] 占位，见 examples/NICS_scan/template_NMR.gjf） | 绘制 NICS 曲线（可导出 .txt/图像），直接算积分 INICS 与 FiPC-NICS（后者要求扫描线平行于笛卡尔轴） | [3.28](sec-3-28-electron-delocalization-and-aromaticity-analyses.md) |
| NICS-2D 扫描平面图 | 主功能25 → 子功能14 → 定义作图平面 → 选项1（生成 NICS_2D.gjf）→ Gaussian 运行 → 选项2（载入输出）→ 选分量 | 同上（结构文件＋Gaussian NMR 模板） | 自动显示 NICS 平面图，关闭后可在后处理菜单调设置重绘 | [3.28](sec-3-28-electron-delocalization-and-aromaticity-analyses.md) |

## 主功能 100/200/300（其他功能 1–3）
| 功能 | 菜单路径 | 输入 | 关键选项与产出 | 来源 |
|---|---|---|---|---|
| 双函数散点图与 cube 生成 | 主功能100（其他功能第1部分）→ 子功能1 | 任意波函数文件，或两个网格相同的 .cub（选 0,0 再载入第二文件） | 选两个实空间函数共网格计算，输出 Pearson 相关系数，可绘散点图、导出 output.txt 与 cube | [3.100](sec-3-100-other-functions-part-1.md) |
| 导出各类结构/波函数文件与量子化学程序输入文件 | 主功能100（其他功能第1部分）→ 子功能2 | 当前结构；导出 .wfn/.wfx 需 GTF，导出 .mwfn/.fch/.molden/.47 需基函数，导出 cub/vti/VASP 网格需内存网格数据 | 格式转换（.pdb/.xyz/.gro/.cif/.cml/.gjf 等）与 Gaussian/ORCA/CP2K 等输入文件生成，选项35/36/37 导出网格数据 | [3.100](sec-3-100-other-functions-part-1.md) |
| 分子范德华体积（蒙特卡罗） | 主功能100（其他功能第1部分）→ 子功能3 | 仅原子坐标（定义1：vdW 球叠加）；定义2（电子密度等值面）需 GTF | 选 vdW 区域定义与采样指数 i（N=100×2^i），输出 vdW 体积 | [3.100](sec-3-100-other-functions-part-1.md) |
| 全空间函数积分（含动能/核吸引势能、球平均 ELF/LOL） | 主功能100（其他功能第1部分）→ 子功能4（隐藏 -4/-5 比较两文件函数差异） | 原子坐标、GTFs；比较两文件时另需第二个波函数文件 | 选内置被积函数（动能密度 K、ELF/LOL 等）或自定义 userfunc，Becke 数值积分输出积分值 | [3.100.4](sec-3-100-other-functions-part-1.md#31004-在全空间对函数积分integrate-a-function-over-the-whole-space) |
| Alpha 与 Beta 轨道重叠积分（含 <S²>） | 主功能100（其他功能第1部分）→ 子功能5 | GTFs（非限制波函数） | 选项1 输出完整重叠矩阵与最大配对并给出 <S²>，选项2 只输出对角元 | [3.100](sec-3-100-other-functions-part-1.md) |
| 监控 Gaussian SCF 收敛过程 | 主功能100（其他功能第1部分）→ 子功能6 | Gaussian 输出文件（路线须含 #P；兼容 SCF=QC/XQC） | 打印各步 RMSDP/MaxDP/DE 收敛表并绘制能量与密度矩阵变化曲线 | [3.100](sec-3-100-other-functions-part-1.md) |
| 碎片波函数组合为 Gaussian 初猜（含能量分解、反铁磁耦合建模） | 主功能100（其他功能第1部分）→ 子功能8 | 各碎片的 Gaussian 输出文件（需 nosymm、pop=full） | 输入碎片总数并依次载入，可选翻转碎片自旋，输出 new.gjf；首末 SCF 迭代能量差即轨道相互作用能 | [3.100.8](sec-3-100-other-functions-part-1.md#31008-生成以碎片波函数组合为初猜的gaussian输入文件generate-gaussian-input-file-with-initial-guess-combined-from-fragment-wavefunctions) |
| 原子间连接性与配位数（DFT-D3 定义） | 主功能100（其他功能第1部分）→ 子功能9 | 原子坐标 | 输出每对原子连接性指数 I、连接性之和（粗略配位数）与整数连接性之和，可导出 connmat.txt | [3.100](sec-3-100-other-functions-part-1.md) |
| 两轨道重叠与质心距离（电荷转移分析） | 主功能100（其他功能第1部分）→ 子功能11 | GTFs、原子坐标 | 输入两轨道序号，数值积分输出质心距离与两类重叠量，可增设质心为虚拟原子 | [3.100](sec-3-100-other-functions-part-1.md) |
| Alpha/Beta 轨道双正交化 | 主功能100（其他功能第1部分）→ 子功能12 | 含基函数的 UHF/UKS 文件（.mwfn/.fch/.molden/.gms） | 可选仅占据/全部轨道、是否算轨道能量与按能量排序，输出 biortho.txt 与 biortho.fch | [3.100.12](sec-3-100-other-functions-part-1.md#310012-alpha与beta轨道之间的双正交化biorthogonalization-between-alpha-and-beta-orbitals) |
| LOLIPOP 指数（π 堆积能力） | 主功能100（其他功能第1部分）→ 子功能14 | GTFs、原子坐标（非平面体系需先定域化出 π LMO） | 选 π 轨道并输入成环原子序号，输出 LOLIPOP 值（越小 π 堆积越强），可导出积分点 pt.xyz | [3.100.14](sec-3-100-other-functions-part-1.md#310014-计算lolipopcalculate-lolipop-lol-integrated-pi-over-plane) |
| 分子间轨道重叠积分 | 主功能100（其他功能第1部分）→ 子功能15 | 二聚体与两个单体的含基函数文件（坐标一致、基组相同、原子顺序一致） | 依次载入二聚体与两单体文件，输出单体轨道间重叠积分（如 HOMO-HOMO、LUMO-LUMO） | [3.100.15](sec-3-100-other-functions-part-1.md#310015-计算分子间轨道重叠calculate-intermolecular-orbital-overlap) |
| 基于轨道能量与系数生成 Fock/KS 矩阵 | 主功能100（其他功能第1部分）→ 子功能17 | 含基函数与全部轨道的文件（.fch/.molden/.mwfn/.gms，需无线性依赖删除） | 按 F=SCEC⁻¹ 生成矩阵并以下三角形式导出文本文件（非限制情形分别输出 Fa/Fb） | [3.100](sec-3-100-other-functions-part-1.md) |
| Yoshizawa 电子输运路径分析 | 主功能100（其他功能第1部分）→ 子功能18 | 含基函数文件，另需 NBO 的 NAOMO 信息（Gaussian 加 pop=nboread 与 $NBO NAOMO $END，或载入 .47/NAOMO 文件） | 计算原子间输运概率，输出有利电子传输路径 | [3.100.18](sec-3-100-other-functions-part-1.md#310018-yoshizawa电子输运路径分析yoshizawas-electron-transport-route-analysis) |
| 组合碎片波函数生成新波函数 | 主功能100（其他功能第1部分）→ 子功能19 | 各碎片波函数文件（导出 .mwfn/.fch 需碎片含基函数信息） | 选导出格式并依次载入碎片，输出叠加态组合波函数（.wfn/.fch/.mwfn） | [3.100.19](sec-3-100-other-functions-part-1.md#310019-通过组合碎片波函数生成新波函数generate-new-wavefunction-by-combining-fragment-wavefunctions) |
| Hellmann-Feynman 力 | 主功能100（其他功能第1部分）→ 子功能20 | GTFs、原子坐标 | 解析/数值计算各原子所受 H-F 力并输出 | [3.100](sec-3-100-other-functions-part-1.md) |
| 基于几何的结构性质（直径、平面性、空腔等） | 主功能100（其他功能第1部分）→ 子功能21 | 原子坐标（轨迹分析用多帧 .xyz） | 按选项计算分子直径/长宽高、平面性、空腔直径等并可视化相关区域 | [3.100.21](sec-3-100-other-functions-part-1.md#310021-基于几何信息计算特定原子的性质calculate-properties-based-on-geometry-information-for-specific-atoms) |
| π 轨道检测、占据数设置与 π 组成 | 主功能100（其他功能第1部分）→ 子功能22（自动识别 π 轨道） | 离域情形需 GTFs，定域情形需基函数，另需原子坐标 | 自动识别 π 轨道/LMO，可改占据数并计算任意轨道的 π 组成 | [3.100](sec-3-100-other-functions-part-1.md) |
| 函数分布拟合到原子值 | 主功能100（其他功能第1部分）→ 子功能23 | 原子坐标（被拟合函数如 ESP/ALIE/Fukui 由 GTFs 算得） | 将分子表面实空间函数最小二乘拟合为原子值输出 | [3.100](sec-3-100-other-functions-part-1.md) |
| CVB 指数及相关量（氢键强度） | 主功能200（其他功能第2部分）→ 子功能1 | 原子坐标、GTFs | 输入给体/氢/受体原子序号，自动输出 ELF(C-V,D)、ELF(DH-A) 与 CVB 指数 | [3.200](sec-3-200-other-functions-part-2.md) |
| Hilbert 空间原子与键偶极矩 | 主功能200（其他功能第2部分）→ 子功能2 | 含基函数文件（.mwfn/.fch/.molden/.gms） | 选项1/2/3 分别输出单原子、原子对、Mulliken 划分的原子总偶极矩，选项10 导出电子偶极矩矩阵 | [3.200](sec-3-200-other-functions-part-2.md) |
| 多轨道 cube 文件生成 | 主功能200（其他功能第2部分）→ 子功能3 | 原子坐标、GTFs（支持 h-3/l+2 相对 HOMO/LUMO 选轨） | 选轨道范围与网格，输出单轨道多个 cube 或多轨道合一的 orbital.cub | [3.200](sec-3-200-other-functions-part-2.md) |
| 实空间函数径向分布函数（RDF） | 主功能200（其他功能第2部分）→ 子功能5 | 原子坐标、GTFs | 设球心与径向上下限，输出 RDF 曲线、积分曲线与球平均函数 | [3.200.5](sec-3-200-other-functions-part-2.md#32005-对实空间函数绘制径向分布函数) |
| 两波函数轨道对应关系 | 主功能200（其他功能第2部分）→ 子功能6 | 当前波函数与第二个波函数文件（方法/基组/几何可不同） | 输入双方轨道范围，输出每个轨道的前五大贡献与展开系数，-1 输出全部重叠积分到 convmat.txt | [3.200.6](sec-3-200-other-functions-part-2.md#32006-分析两个波函数中轨道的对应关系) |
| 平均键长与平均配位数（团簇） | 主功能200（其他功能第2部分）→ 子功能9 | 原子坐标（如 Ge12Au.pdb） | 输入两类元素，输出平均键长与平均配位数 | [3.200](sec-3-200-other-functions-part-2.md) |
| 轨道间各类积分（偶极/速度/动能/重叠） | 主功能200（其他功能第2部分）→ 子功能10 | 原子坐标、GTFs | 输入一对或一批轨道，屏幕打印或导出 orbint.txt | [3.200](sec-3-200-other-functions-part-2.md) |
| 函数中心、一二阶矩、回转半径与 <r²> | 主功能200（其他功能第2部分）→ 子功能11 | 原子坐标、GTFs | 选实空间函数，输出分布中心、各阶矩与回转半径 | [3.200](sec-3-200-other-functions-part-2.md) |
| 能量指数 EI 与键极性指数 BPI | 主功能200（其他功能第2部分）→ 子功能12 | 原子坐标、基函数（禁弥散基，因用 Mulliken 划分） | 输入原子序号得 EI，结合参考分子 EI 算 BPI；自由基 -EI 即基团电负性 | [3.200.12](sec-3-200-other-functions-part-2.md#320012-计算能量指数-ei-或键极性指数-bpi) |
| 轨道对密度差（或其他格点数据）贡献 | 主功能200（其他功能第2部分）→ 子功能13 | 含感兴趣轨道的文件与 Δρ 的 cube 文件 | 设约束 P 并选轨道范围，最小二乘输出各轨道贡献 p，可视化拟合密度与残差等值面 | [3.200.13](sec-3-200-other-functions-part-2.md#320013-计算轨道对密度差或其它格点数据的贡献) |
| 域分析（等值面内函数积分） | 主功能200（其他功能第2部分）→ 子功能14 | 原子坐标、GTFs（实空间函数由波函数算得） | 选项2/3 定义域（如 RDG<0.5），输出各域体积与函数积分，支持按 sign(λ₂)ρ 取子域积分 | [3.200.14](sec-3-200-other-functions-part-2.md#320014-域分析求函数等值面内的性质) |
| 电子相关指数（总/动态/非动态） | 主功能200（其他功能第2部分）→ 子功能15 | 含自然轨道占据数的文件（.mwfn/.wfn/.wfx/.molden） | 直接输出三个电子相关指数，另有局域版本可用 | [3.200](sec-3-200-other-functions-part-2.md) |
| 由 .fch 密度矩阵生成自然轨道/NSO/SNO | 主功能200（其他功能第2部分）→ 子功能16 | .fch/.fchk 文件（含各类密度矩阵记录） | 选密度矩阵类型生成 NO/NSO/SNO，可导出 new.mwfn 继续分析 | [3.200](sec-3-200-other-functions-part-2.md) |
| 两轨道 Coulomb 与交换积分 | 主功能200（其他功能第2部分）→ 子功能17 | 含轨道波函数的文件，或两个轨道 cube 文件 | 输入两轨道编号（与网格设置），输出 J 与 K 积分 | [3.200](sec-3-200-other-functions-part-2.md) |
| 键长/键级交替与键角/二面角交替 | 主功能200（其他功能第2部分）→ 子功能18 | 原子坐标（基函数可选，用于同时输出键级；禁弥散基） | 定义路径原子序列，输出 BLA/BOA 及键角二面角变化曲线 | [3.200](sec-3-200-other-functions-part-2.md) |
| 轨道或函数空间离域指数 SDI | 主功能200（其他功能第2部分）→ 子功能19 | 轨道波函数文件，或载入格点数据文件（.cub）走内存格点模式 | 输入轨道编号或直接用内存格点，输出各轨道/函数的 SDI | [3.200](sec-3-200-other-functions-part-2.md) |
| 键级密度 BOD 与自然适应轨道 NAdO | 主功能200（其他功能第2部分）→ 子功能20 | 原子坐标、基函数 | 生成 NAdO 并输出键级密度分析结果，用于化学键表征 | [3.200](sec-3-200-other-functions-part-2.md) |
| 占据轨道 Löwdin 正交化 | 主功能200（其他功能第2部分）→ 子功能21 | 原子坐标、基函数（适用于组合波函数等非正交占据轨道） | 一键正交化占据轨道并更新内存系数与密度矩阵 | [3.200](sec-3-200-other-functions-part-2.md) |
| 胞内自由区域可视化与自由体积 | 主功能300（其他功能第3部分）→ 子功能1 | 含胞信息文件（.cif/.gro/带 CRYST1 的 .pdb）；无胞信息则假设正交盒 | 设格点原点/边长/间距与平滑函数，输出自由体积与占比，等值面可视化或导出 cube | [3.300](sec-3-300-other-functions-part-3.md) |
| 原子径向密度拟合为 STO/GTF 组合 | 主功能300（其他功能第3部分）→ 子功能2 | 单原子波函数文件（GTF，原子须在原点） | 选项3 设初猜后选项1 拟合（LM 算法），输出系数指数、RMSE 与 r²，支持可视化检验与导出 | [3.300.2](sec-3-300-other-functions-part-3.md#33002-将原子径向密度拟合为多个-sto-或-gtf-的线性组合) |
| STM 图像模拟（恒高/恒流） | 主功能300（其他功能第3部分）→ 子功能4 | 含基函数文件（HF/KS-DFT，禁双杂化与多组态；分子须平行 XY 平面） | 设费米能级、偏压与扫描范围，选项0 计算 LDOS 电流并绘制 STM 图 | [3.300.4](sec-3-300-other-functions-part-3.md#33004-模拟扫描隧道显微镜-stm-图像) |
| 电偶极/多极矩与电子空间范围 | 主功能300（其他功能第3部分）→ 子功能5 | 原子坐标，加 GTF/基函数或原子电荷之一 | 解析积分输出偶极、四极、八极、十六极矩与 <r²> | [3.300.5](sec-3-300-other-functions-part-3.md#33005-计算电偶极多极矩和电子空间范围) |
| 输入 Fock 矩阵求当前轨道能量 | 主功能300（其他功能第3部分）→ 子功能6 | 含基函数文件与 Fock/KS 矩阵纯文本文件 | 载入矩阵后输出内存轨道能量（可用于 NTO 等任意轨道） | [3.300.6](sec-3-300-other-functions-part-3.md#33006-通过输入-fock-矩阵计算当前轨道能量) |
| 体系几何相关操作（平移/旋转/缩放/超胞等） | 主功能300（其他功能第3部分）→ 子功能7 | 原子坐标（含胞体系同时操作胞矢量） | 选项覆盖平移旋转、坐标缩放、超胞构建、原子重排、轴变换、包回胞内等 28 类操作 | [3.300](sec-3-300-other-functions-part-3.md) |
| 表面距离投影图 | 主功能300（其他功能第3部分）→ 子功能8 | 原子坐标（promolecular/vdW 表面）；波函数电子密度表面需 GTFs | 选表面定义与 XYZ 扫描范围，选项0 计算并绘制填充色图加等值线 | [3.300](sec-3-300-other-functions-part-3.md) |
| Fermi 能级确定 | 主功能300（其他功能第3部分）→ 子功能9 | 含占据与非占据轨道文件（.mwfn/.fch/.molden；或手写轨道能量纯文本） | 输入温度，二分迭代输出 Fermi 能级 | [3.300](sec-3-300-other-functions-part-3.md) |
| 实例：光气动能与核吸引势能数值积分 | 主功能100（其他功能第1部分）→ 子功能4（同上） | examples\COCl2.wfn（HF/6-31G*）；核吸引项经 userfunc（iuserfunc=12）免重编译 | 选动能密度 K 积分得总动能 1031.1092 a.u.，与 Gaussian 值吻合 | [4.100.4](sec-4-100-other-functions-part-1.md#41004-通过数值积分-numerical-integration计算光气-phosgene的动能-kinetic-energy和核吸引势能-nuclear-attraction-potential-energy) |
| 实例：NH₃BH₃ 简单能量分解 | 主功能100（其他功能第1部分）→ 子功能8（同上） | NH3.out、BH3.out 碎片 Gaussian 输出；复合物 new.gjf 跑出 new.out | 首末 SCF 迭代能量差得轨道作用能 -230.37 kJ/mol，总作用能 -190.44 kJ/mol | [4.100.8](sec-4-100-other-functions-part-1.md#41008-使用组合的碎片波函数-fragment-wavefunction进行简单的能量分解-energy-decomposition) |
| 实例：三重态乙醇双正交化 | 主功能100（其他功能第1部分）→ 子功能12（同上） | examples\ethanol_triplet.fch | 全部轨道双正交化并可选算能量排序，输出 biortho.txt/.fch，奇异值≈1 即配对良好 | [4.100.12](sec-4-100-other-functions-part-1.md#410012-非限制性开壳层波函数-unrestricted-open-shell-wavefunction轨道的双正交化-biorthogonalization分析) |
| 实例：菲与联苯 LOLIPOP | 主功能100（其他功能第1部分）→ 子功能14（联苯先经主功能19 定域化并用子功能22 识别 π 轨道） | examples/phenanthrene.wfn、examples\biphenyl.fch | 菲中央环 6.39、边缘环 8.23，联苯环 8.82；选项5 可只计环单侧，选项6 导出 pt.xyz | [4.100](sec-4-100-other-functions-part-1.md) |
| 实例：DB-TTF 二聚体分子间轨道重叠 | 主功能100（其他功能第1部分）→ 子功能15（同上） | 二聚体 .fchk（guess=only）与两单体 .fchk（坐标与基组一致，nosymm） | 输出单体间 HOMO-HOMO 与 LUMO-LUMO 重叠积分 | [4.100.15](sec-4-100-other-functions-part-1.md#410015-计算-db-ttf-的分子间轨道重叠积分-intermolecular-orbital-overlap-integral) |
| 实例：菲 Yoshizawa 输运路径 | 主功能100（其他功能第1部分）→ 子功能18（同上） | 菲的含基函数文件与 NAOMO 信息 | 输出菲各原子间输运概率，指认有利电子传输路径 | [4.100](sec-4-100-other-functions-part-1.md) |
| 实例：组合波函数整体 ELF 分析 | 主功能100（其他功能第1部分）→ 子功能19（同上） | 各碎片波函数文件 | 先组合生成整体波函数文件，再做 ELF 分析揭示未极化叠加态电子定域特征 | [4.100.19](sec-4-100-other-functions-part-1.md#410019-对由片段波函数组合而成的整体波函数的elf分析) |
| 实例：几何结构表征（直径/平面性/空腔/轨迹） | 主功能100（其他功能第1部分）→ 子功能21（同上） | 结构文件（alpha-cyclodextrin.pdb、[14]annulene、C18_MD_500.xyz 轨迹等，仅需坐标） | 输出分子直径与长宽高、平面性定量指标、空腔直径与区域，支持轨迹逐帧演化分析 | [4.100](sec-4-100-other-functions-part-1.md) |
| 实例：环庚三烯非平面 π 电子特征 | 主功能100（其他功能第1部分）→ 子功能22（先经主功能19 定域化） | 环庚三烯含基函数文件 | 探测 π 型 LMO，置零其余轨道占据后分析 π 电子密度/LOL，占/空轨道 π 组成定量评估 | [4.100](sec-4-100-other-functions-part-1.md) |
| 实例：C₆₀ 与 Rydberg 轨道 RDF | 主功能200（其他功能第2部分）→ 子功能5（同上；Rydberg 轨道先经主功能6 子功能26 设占据） | C60.wfn、H2CO_aVTZ.fch | C₆₀ RDF 峰≈3.5 Å；MO11 RDF 主峰≈4.6 Å 证实 Rydberg 弥散特征 | [4.200.5](sec-4-200-other-functions-part-2.md#42005-绘制电子密度的径向分布函数) |
| 实例：HF/MP2 轨道对应与氮孤对贡献 | 主功能200（其他功能第2部分）→ 子功能6（定域 LMO 经主功能19 产生） | CH3NH2_HF/MP2.wfn、D-pi-A.fchk 与 new.fch（LMO） | 输出 NO 的 MO 展开贡献（如 NO5=0.7408·MO6-0.6412·MO7…）；N24 孤对 LMO44 对 MO49 贡献 33.29% | [4.200](sec-4-200-other-functions-part-2.md) |
| 实例：CH₃NH₂/CH₃F 的 EI 与 BPI | 主功能200（其他功能第2部分）→ 子功能12（同上） | examples\EI_BPI 下 ethane/N2H4/CH3NH2/CH3F/CH3/F 的 .fch（HF/6-31G*，无弥散） | 乙烷 C 的 EI -0.667639 a.u. 为参考；BPI(CN)=-0.046、BPI(CF)=-0.189，C-F 极性更强 | [4.200.12](sec-4-200-other-functions-part-2.md#420012-计算能量指数ei与键极性指数bpi) |
| 实例：苯酚 Fukui 函数 f⁻ 的轨道贡献 | 主功能200（其他功能第2部分）→ 子功能13（f⁻ cube 先经主功能5 自定义操作生成） | phenol.wfn、phenol_N-1.wfn 与 density.cub | HOMO（轨道25）贡献 0.766 主导 f⁻，拟合误差仅 0.0038 | [4.200.13](sec-4-200-other-functions-part-2.md#420013-研究轨道对密度差的贡献) |
| 实例：RDG 域积分定量弱相互作用 | 主功能200（其他功能第2部分）→ 子功能14（同上） | 苯酚二聚体、PP 体系波函数文件 | 苯酚二聚体各 RDG 域积分表征弱相互作用强度；PP 体系用 q_int 指数判断氢键 | [4.200.14](sec-4-200-other-functions-part-2.md#420014-域分析例子) |
| 实例：域分析可视化分子空腔并求体积 | 主功能200（其他功能第2部分）→ 子功能14（同上） | 含空腔分子波函数文件 | 识别空腔域并积分得空腔体积，等值面可视化空腔形状 | [4.200.14.2](sec-4-200-other-functions-part-2.md#4200142-用域分析模块可视化分子空腔并计算其体积) |
| 实例：EDD 等值面内积分 EDD | 主功能200（其他功能第2部分）→ 子功能14（同上） | 苯的形变密度相关文件 | 苯 EDD 域内积分 EDD，同法适用于 Fukui 函数与对偶描述符 | [4.200](sec-4-200-other-functions-part-2.md) |
| 实例：特定路径 BLA/BOA 与键角二面角变化 | 主功能200（其他功能第2部分）→ 子功能18（同上） | 含坐标（键级另需基函数、无弥散）的文件 | 沿指定路径输出键长/键级交替与键角二面角演化 | [4.200](sec-4-200-other-functions-part-2.md) |
| 实例：轨道密度 SDI 表征离域程度 | 主功能200（其他功能第2部分）→ 子功能19（同上） | 含波函数信息文件（或自旋密度 cube） | 输出各轨道密度 SDI，定量比较轨道空间离域程度 | [4.200](sec-4-200-other-functions-part-2.md) |
| 实例：BOD 与 NAdO 研究化学键 | 主功能200（其他功能第2部分）→ 子功能20（同上） | 原子坐标、基函数 | 生成 NAdO 并由键级密度揭示化学键特征 | [4.200](sec-4-200-other-functions-part-2.md) |
| 实例：煤与 COF 晶胞自由区域 | 主功能300（其他功能第3部分）→ 子功能1（同上） | examples\coal.pdb（含 CRYST1）、examples\COF_12000N2.cif | 煤自由体积占比 49.21%、COF 占比 65.19%；非正交胞导出 free_smooth.cub 用 VMD/VESTA 渲染 | [4.300.1](sec-4-300-other-functions-part-3.md#43001-可视化晶胞中的自由区域并计算自由体积的例子) |
| 实例：Si/STO 粗拟合与 Br/GTF 精拟合 | 主功能300（其他功能第3部分）→ 子功能2（同上） | examples\atomwfn\Si.wfn、Br.wfn（ROHF/6-31G*，原子在原点） | Si 用 4 STO 得 r²=0.9907；Br 用 10 GTF 得 r²=0.9994，指数相近者可合并重拟合 | [4.300.2](sec-4-300-other-functions-part-3.md#43002-将原子径向密度拟合为-sto-或-gtf-的例子) |
| 实例：菲恒高/恒流 STM 图像 | 主功能300（其他功能第3部分）→ 子功能4（波函数先经主功能6 子功能33 两次旋转至 XY 平面并经主功能100 子功能2 存 mol.mwfn） | mol.mwfn（菲，B3LYP/6-31G*，位于 Z=0 平面） | V=-5.0 V、Z=1.2 Å 下算恒高 STM；切恒流模式输电流值得 z_c(x,y) 图 | [4.300.4](sec-4-300-other-functions-part-3.md#43004-模拟扫描隧道显微镜stm图像的例子) |
| 实例：尿嘧啶多极矩与电子空间范围 | 主功能300（其他功能第3部分）→ 子功能5（同上） | 尿嘧啶波函数文件 | 输出偶极/四极/八极/十六极矩与 <r²> 解析值 | [4.300](sec-4-300-other-functions-part-3.md) |
| 实例：给体-π-受体 S0→S1 的 NTO 能量 | 主功能300（其他功能第3部分）→ 子功能6（同上） | NTO 轨道文件与相应 Fock/KS 矩阵文本文件 | 输出 NTO 轨道能量，用于激发分析 | [4.300](sec-4-300-other-functions-part-3.md) |
| 实例：[Ru(bpy)₃]²⁺ 表面距离投影图 | 主功能300（其他功能第3部分）→ 子功能8（同上） | [Ru(bpy)₃]²⁺ 结构/波函数文件 | 绘制配位体表面距离投影填充色图，直观揭示位阻与表面起伏 | [4.300.8](sec-4-300-other-functions-part-3.md#43008-为rubpy₃²-配位体绘制表面距离投影图) |

## 实例 4.0–4.7
| 功能 | 菜单路径 | 输入 | 关键选项与产出 | 来源 |
|---|---|---|---|---|
| 查看分子轨道等值面 | 主功能0（查看轨道与结构） | .fch/.wfn等波函数文件 | 右下角选轨道序号或标记（如h、l+2），拖动设等值面值 | [4.0](sec-4-0-view-orbitals-and-structure.md) |
| 同时绘制两个轨道 | 主功能0（查看轨道与结构）→ Show+Sel. isosur#2 | .fch/.wfn等波函数文件 | 先后选两个轨道序号，用网格/透明风格观察重叠 | [4.0](sec-4-0-view-orbitals-and-structure.md) |
| 查看NBO/NHO/NAO（plot文件方式） | 主功能0（查看轨道与结构，载入.31+.37） | NBO plot文件（.31~.41，Gaussian用pop=nboread+plot产生） | 从列表选NBO序号，可同时显示两个NBO看给体—受体重叠 | [4.0](sec-4-0-view-orbitals-and-structure.md) |
| 查看NBO（fch载体方式） | 主功能0（查看轨道与结构，载入.fch） | 含saveNBO的.fch（HF/DFT首行加saveNBOene，post-HF加saveNBOocc） | 直接查看NBO，注意Gaussian存盘时可能重排NBO顺序 | [4.0](sec-4-0-view-orbitals-and-structure.md) |
| 批量绘制轨道图片 | 主功能0（查看轨道与结构）→ Tools → Batch plotting orbitals | 波函数文件 | 一次把大量选定轨道分别存为图片文件 | [4.0](sec-4-0-view-orbitals-and-structure.md) |
| Multiwfn+VMD高质量轨道等值面图 | 主功能5（产生格点数据）→ VMD脚本orb/orbiso/orbclean | .fch/.fchk + VMD | showorb.bat/txt批量导出cube，VMD载入渲染，Tachyon输出出版级图片 | [4.0](sec-4-0-view-orbitals-and-structure.md) |
| 单点处全部实空间性质 | 主功能1（单点处计算性质） | .wfn等波函数文件 | 输入XYZ坐标（Bohr/Å），一次输出密度、ELF、LOL、ESP、梯度、Hessian本征值等；oN选轨道、fN选函数、aN直接取核位置 | [4.1](sec-4-1-calculate-properties-at-a-point.md) |
| 核位置ESP评估相互作用强度 | 主功能1（单点处计算性质）→ aN（取原子核位置） | 复合物+各单体.wfn（MP2/aug-cc-pVDZ以上，post-HF加density） | 读“扣除自身核贡献的ESP”，按ΔΔVn公式预测静电主导相互作用能 | [4.1](sec-4-1-calculate-properties-at-a-point.md) |
| AIM拓扑分析（找CP与键径） | 主功能2（拓扑分析）→ 2（核位置初猜）→ 3（原子对中点初猜）→ 0（可视化）→ 8（生成拓扑路径） | .wfn/.fch | 用Poincaré-Hopf关系校验CP找全，选项7看BCP处性质，-9量距离夹角 | [4.2](sec-4-2-topology-analysis.md) |
| 基于BCP性质预测氢键结合能 | 主功能2（拓扑分析）→ 7（显示CP处性质） | .wfn/.fch | 取BCP处ρ或能量密度V(r)，代入BE拟合方程估算氢键结合能 | [4.2](sec-4-2-topology-analysis.md) |
| 基于CP性质评估芳香性 | 主功能2（拓扑分析）→ 20（Shannon芳香性指数）/ 21（沿指定方向梯度与曲率） | .wfn/.fch | 输入环BCP编号求SA指数，或输入RCP编号+环平面原子求垂直曲率，越小/越负越芳香 | [4.2](sec-4-2-topology-analysis.md) |
| 生成流域间面 | 主功能2（拓扑分析）→ 10（生成流域间面）→ 0（可视化） | .wfn/.fch | 输入(3,-1)CP编号生成IBS，切分相邻原子流域 | [4.2](sec-4-2-topology-analysis.md) |
| LOL/ELF/ESP等其它函数的拓扑分析 | 主功能2（拓扑分析）→ -11（选实空间函数，10为LOL、9为ELF、12为ESP）→ 6（球内随机撒点）/ 2（核位置）→ 8（生成拓扑路径） | .wfn/.fch | 复杂函数多重复几次撒点搜索；找ELF/LOL极大改用-1→12→3最速上升算法 | [4.2](sec-4-2-topology-analysis.md) |
| 沿键径绘制实空间函数 | 主功能2（拓扑分析）→ -5（路径操作）→ 7（沿路径计算性质） | .fch + settings.ini中iuserfunc（如30为密度椭率） | 输入路径编号与函数编号，输出沿键径曲线与数据点，虚线标BCP位置 | [4.2](sec-4-2-topology-analysis.md) |
| CP处性质的轨道贡献分解 | 主功能2（拓扑分析）→ 7 → 编号+d（分解该CP）/ 主功能1 → d（分解给定点） | .fch | 选实空间函数后输出各轨道贡献百分比；可先经主功能19轨道定域化再分解到定域轨道 | [4.2](sec-4-2-topology-analysis.md) |
| VMD高质量AIM拓扑图 | 主功能2（拓扑分析，静默批处理AIM.txt）→ 导出CPs.pdb/paths.pdb/CPprop.txt → VMD中aim/labcp | .wfn + VMD | AIM.bat/txt自动找CP、生成键径并导出，VMD中aim一键渲染、labcp标注CP编号 | [4.2](sec-4-2-topology-analysis.md) |
| 局域/片段间限定AIM分析 | 主功能2（拓扑分析）→ -1（设搜索参数：9限密度范围、10限原子/区域）→ 2/3/4 → 8；-5 → 8（只保留两片段间键径）；-4 → 2（删除CP） | 大体系.wfn（如GCGC碱基对） | 只在弱作用区、低密度区或指定片段内/片段间搜CP，大幅降成本并简化图形 | [4.2](sec-4-2-topology-analysis.md) |
| 流域吸引子精修CP（自旋密度等） | 主功能17（盆分析）→ 1（产生盆并定位吸引子）→ -4 → 3（导出attractors.txt）→ 主功能2 → -11（选函数）→ 1 → 4（从txt读起点） | .wfn/.fch | 先用盆分析保证找到全部极大极小，再用拓扑模块精修坐标，适合自旋密度等复杂函数 | [4.2](sec-4-2-topology-analysis.md) |
| 变形密度的拓扑分析 | 主功能5 → -2（变形性质）→ 主功能17（盆分析找极大极小并导出）→ 主功能2 → -11 → 100（自定义B样条插值函数）→ 1 → 4 / 6 → 8 | .fch + atomwfn原子波函数文件夹 | 格点存内存后转插值函数再搜CP，(3,-1)/(3,+1)可用球内撒点补找 | [4.2](sec-4-2-topology-analysis.md) |
| ESP拓扑分析（找ESP极小） | 主功能2（拓扑分析）→ -11 → 12（ESP）→ 6（Newton找各类CP）/ vmin（最速下降专找极小）/ 联用主功能17盆分析定位后精修 | .wfn/.mwfn | 狭窄谷区极小用“盆分析+拓扑精修”联用法；选项7查看极小处ESP值 | [4.2](sec-4-2-topology-analysis.md) |
| vdW势拓扑分析（找vdW极小） | 主功能2（拓扑分析）→ -11 → 25（vdW势）→ 6（球内撒点）→ -1 | .xyz等几何文件 | 进入即自动切换最速下降法，选项7查看极小处vdW势，可叠等值面验证 | [4.2](sec-4-2-topology-analysis.md) |
| IRI/RDG拓扑分析（找相互作用区极小） | 主功能2（拓扑分析）→ -11 → 24（IRI）→ 6（球内撒点）→ -1 | .mwfn/.wfn | 自动切换最速下降法（Newton难收敛），选项7表征相互作用，可转主功能4画IRI平面图对照 | [4.2](sec-4-2-topology-analysis.md) |
| 沿线绘制实空间函数曲线 | 主功能3（沿线绘制性质）→ 选函数（如5自旋密度）→ 1（两原子定线） | .wfn等波函数文件 | 输入两原子序号定线，选项6定位极值，可导出XY数据用Origin重绘 | [4.3](sec-4-3-output-and-plot-various-properties-in-a-line.md) |
| Fermi/Coulomb/总关联空穴曲线 | 主功能3（沿线绘制性质）→ 17（关联空穴）→ 1（两原子定线） | CCSD等post-HF .wfn + settings.ini设refxyz参考点、paircorrtype | paircorrtype取1/2/3分别画Fermi、Coulomb、总关联空穴 | [4.3](sec-4-3-output-and-plot-various-properties-in-a-line.md) |
| PAEM-MO原子间相互作用分析 | 主功能3（沿线绘制性质）→ 100（自定义函数，iuserfunc=33基于Γ或34基于DFT势）→ 0/1（设延伸与定线） | HF .fch | 沿键轴画PAEM曲线找势垒，与占据MO能量比较判断共价/非共价 | [4.3](sec-4-3-output-and-plot-various-properties-in-a-line.md) |
| 平面填充色图与等值线图 | 主功能4（平面内绘制性质）→ 选函数（如1电子密度）→ 1（填充色）/ 2（等值线） | .wfn等波函数文件 | 选平面（1为XY、2为XZ、3为YZ、4为三原子定面），后处理调色标、原子标签、键与等值线 | [4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md) |
| LOL平面图 | 主功能4（平面内绘制性质）→ 10（LOL）→ 1（填充色）→ 4（三原子定面） | .wfn | 选项17放大标签显示阈值，19换颜色过渡，2叠加等值线增强表达 | [4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md) |
| ELF阴影浮雕投影图 | 主功能4（平面内绘制性质）→ 9（ELF）→ 5（带投影的阴影浮雕图）→ 4（三原子定面） | .wfn | 手动设稍大延伸距离防边界截断，选项0保存图片 | [4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md) |
| 去原子贡献的平面图 | 主功能6 → -3/-4（删除部分原子GTF）→ 主功能4；或主功能4后处理 → -9（只画指定原子Hirshfeld加权贡献） | .wfn | 前者修改波函数并省后续计算量，后者只影响当前图、可一键恢复原数据 | [4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md) |
| ESP等值线图叠范德华表面 | 主功能4（平面内绘制性质）→ 12（总ESP）→ 2（等值线）→ 后处理15（显示vdW表面）；或载入.chg选8（原子电荷ESP） | .wfn/.chg | 叠ρ=0.001的vdW线，实/虚线区分ESP正负，判断亲核亲电区域 | [4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md) |
| 双轨道波函数等值线图 | 主功能4（平面内绘制性质）→ 4（轨道波函数）→ 输入两轨道序号 → 7（平行指定键且垂直三原子面定面） | NBO plot文件（.31+.37） | 选项3删除小值等值线去噪，15设出版风格红实蓝虚线 | [4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md) |
| 梯度线/矢量场图叠CP键径与盆间路径 | 先主功能2 → 2/3（搜CP）→ 8（生成键径）→ -10返回，再主功能4 → 1/3/12 → 6（梯度线）/7（矢量场）；后处理4设CP路径显示，“Generate and show interbasin paths”画盆间路径 | .fch/.wfn | 选项11~14调梯度线效果，选项7设盆间路径步长与迭代数 | [4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md) |
| 电子密度变形平面图 | 主功能4（平面内绘制性质）→ -2（变形图，自动备原子波函数）→ 选函数 → 2（等值线） | .wfn + atomwfn文件夹或Gaussian现算原子波函数 | 自动调Gaussian算原子波函数存wfntmp文件夹，可复用免重算 | [4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md) |
| 复合物相对单体的差值平面图 | 主功能4（平面内绘制性质）→ 0（自定义操作，-减去各单体文件）→ 1（电子密度）/9（ELF）→ 2/1 | complex.wfn+各单体.wfn（同坐标，必须nosymm防重定向） | 红实/蓝虚线示密度增减，选项3设等值线、17设标签阈值 | [4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md) |
| LOL-π平面图揭示离域路径 | 主功能100 → 22（识别π轨道并清零其它占据）→ 主功能4 → 10（LOL）→ 1（填充色）/2（等值线间填色） | 平面体系.fch | 在分子平面上1.2 Bohr处作图，高LOL-π区即优势离域路径，pdf矢量导出更清晰 | [4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md) |
| ESP梯度线/矢量场图揭示电场 | 主功能4（平面内绘制性质）→ 12（ESP）→ 6（梯度线）/7（矢量场） | .wfn | 选项15示vdW线、10加箭头，矢量场用13反转箭头使之指向电场方向并按强度着色 | [4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md) |
| 原子轨道平面图 | 主功能4（平面内绘制性质）→ 4（轨道波函数）→ 输入轨道序号 → 2（等值线）→ 后处理9（等值线间填色）+3（内置轨道波函数等值线档） | atomwfn原子.wfn | 设pdf矢量格式导出，得到出版级清晰轨道图 | [4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md) |
| 等值线上函数极值点 | 主功能4（平面内绘制性质）→ 1（电子密度）→ 2（等值线）→ 后处理19（等值线上极值） | .wfn | 输入等值面值（如0.001）与待求函数（如12为ESP），红/蓝球标极大极小并输出坐标与数值 | [4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md) |
| 格点数据与等值面图 | 主功能5（产生格点数据看等值面）→ 9（ELF）/3（密度Laplacian）→ 2/3（中/高质量格点）→ -1（看图）/2（导出cube） | .wfn/.fch | 调等值面值观察孤对/成键区，导出cube用VMD/ChimeraX高质量渲染 | [4.5](sec-4-5-generate-grid-data-and-view-isosurface-map.md) |
| ELF-σ/ELF-π芳香性指标 | 主功能0（看轨道定π轨道）→ 主功能6 → 26（清零σ或π占据；或主功能100 → 22自动识别π）→ 主功能5（ELF等值面找分岔值）→ 主功能2 → -11 → 9 → 6（搜CP）→ 7（读(3,-1)处ELF精确值） | benzene.wfn | 分岔点ELF值即指标，>0.70判有相应芳香性，σ/π均值判全局芳香 | [4.5](sec-4-5-generate-grid-data-and-view-isosurface-map.md) |
| Fukui函数与对偶描述符等值面 | 主功能5（产生格点数据）→ 0（自定义操作：1个或3个文件加减）→ 1（电子密度）/5（自旋密度）→ 2 → -1 | N/N+1/N-1三态.wfn/.fch（同一几何） | f⁻=ρN−ρN−1、f⁰=(ρN+1−ρN−1)/2，对偶描述符用三态精确式或两态自旋近似式 | [4.5](sec-4-5-generate-grid-data-and-view-isosurface-map.md) |
| 电子密度差值等值面与等值线 | 主功能5 → 0（减去各片段文件）→ 1 → 3 → -1（等值面）；再主功能4 → 0（同样操作）→ 2（等值线） | 复合物+片段.wfn（nosymm保证坐标一致） | 等值面取±0.001左右看电荷转移极化，导出cube用VMD双色渲染 | [4.5](sec-4-5-generate-grid-data-and-view-isosurface-map.md) |
| 电子离域范围函数EDR | 主功能5（产生格点数据）→ 20（EDR）→ 输入长度尺度d → 2 → -1 | 阴离子体系.wfn | 取合适等值面（如0.74）显示溶剂化电子离域位置 | [4.5](sec-4-5-generate-grid-data-and-view-isosurface-map.md) |
| 轨道重叠距离函数D(r)映射 | 主功能5 → 21（D(r)，设指数格点）→ 2（导出EDRDmax.cub）→ 主功能5 → 1（导出density.cub）→ 外部程序映射 | ThioformicAcid.wfn | 两次格点设置须一致，D(r)映射到ρ=0.001面区分硬软孤对 | [4.5](sec-4-5-generate-grid-data-and-view-isosurface-map.md) |
| 删除特定高斯函数 | 主功能6（修改波函数）→ 25（按条件设GTF系数）→ 0（存new.wfn） | .wfn | 按GTF序号范围、归属原子、类型筛选后置零，选项4查看系数验证 | [4.6](sec-4-6-modify-and-check-wavefunction.md) |
| 价层电子密度分析 | 主功能6（修改波函数）→ 26（设占据数，清零内层MO）/34（内层轨道占据数一键置零）→ 主功能4/5/2/17分析 | .wfn | 选项3检查占据数；同法分离ELF-σ/ELF-π | [4.6](sec-4-6-modify-and-check-wavefunction.md) |
| 平移复制原胞波函数建超胞 | 主功能6（修改波函数）→ 32（平移复制原胞波函数） | PBC原胞.fch | 依次输入平移矢量、单位与复制次数；粗糙近似，周期体系分析推荐Multiwfn联用CP2K | [4.6](sec-4-6-modify-and-check-wavefunction.md) |
| Mulliken布居分析 | 主功能7（布居分析与原子电荷）→ 5 → 1 | .fch（忌用弥散基组；开壳层另给α/β/自旋布居） | 输出基函数/壳层/角动量/原子四级布居与电荷，-1可改输出到文件 | [4.7](sec-4-7-population-analysis-and-atomic-charge-calculation.md) |
| Hirshfeld电荷与片段电荷 | 主功能7（布居分析与原子电荷）→ -1（定片段）→ 1 → 1（内置自由原子密度） | .wfn | 采用归一化后电荷（和为净电荷），可导出.chg供静电势分析用 | [4.7](sec-4-7-population-analysis-and-atomic-charge-calculation.md) |
| CHELPG电荷 | 主功能7（布居分析与原子电荷）→ 12 → 1（开始计算） | .wfn | ESP网格拟合电荷，大体系较耗时；先-1定片段可同时得片段电荷 | [4.7](sec-4-7-population-analysis-and-atomic-charge-calculation.md) |
| ADCH电荷 | 主功能7（布居分析与原子电荷）→ 11 → 1（内置自由原子密度） | .fch | Hirshfeld电荷经原子偶极校正，严格重现分子偶极矩，绝对值更合理 | [4.7](sec-4-7-population-analysis-and-atomic-charge-calculation.md) |
| 凝聚Fukui函数与凝聚对偶描述符 | 理论（无直接菜单）：主功能7 → 1分算N/N+1/N-1三态Hirshfeld电荷再代入公式；日常直接用主功能22自动计算 | 苯酚N/N+1/N-1三态.wfn | f⁺=qN−qN+1、f⁻=qN−1−qN、Δf=2qN−qN+1−qN−1定量判定反应位点 | [4.7](sec-4-7-population-analysis-and-atomic-charge-calculation.md) |
| Hirshfeld-I电荷 | 主功能7（布居分析与原子电荷）→ 15 → 1（默认设置，可用内置.rad或让Multiwfn调Gaussian现算） | .wfn | 迭代至电荷最大变化<0.0002收敛，给出自洽原子电荷 | [4.7](sec-4-7-population-analysis-and-atomic-charge-calculation.md) |
| EEM电荷（大体系） | 主功能7（布居分析与原子电荷）→ 17 → 0（开始计算） | .mol/.mol2（含键连信息，π共轭须写成正确Lewis结构） | 无需波函数、秒算数百原子，键连或共轭写法错误会报错 | [4.7](sec-4-7-population-analysis-and-atomic-charge-calculation.md) |
| 基函数与原子轨道对应关系 | 主功能7（布居分析与原子电荷）→ 5 → 1 | 单原子.fch | 看壳层布居确定各基函数归属，供主功能8/10按原子轨道分析用 | [4.7](sec-4-7-population-analysis-and-atomic-charge-calculation.md) |
| RESP与常规ESP拟合电荷 | 主功能7 → 18（RESP模块）→ 1（标准两阶段RESP）/2（单阶段拟合）/8（从Gaussian输出载入拟合点）/-1（载入多构象列表）/5（等价约束）/6（电荷约束）/9（额外拟合中心）/11（点群对称生成等价约束）/4（罚函数参数） | .fch/.xyz/.pdb（提供几何定连接）+ Gaussian MK输出 | 支持多构象加权、等价/电荷约束、非原子点拟合、RESP2，附calcRESP2.sh/RESP.sh脚本一键流程 | [4.7](sec-4-7-population-analysis-and-atomic-charge-calculation.md) |
| 原子电荷ESP再现性检验与可视化 | 主功能7 → MK/CHELPG模块 → -3（从.chg载入待检电荷）→ 1（开始计算）；选项6导出ESPfitpt.pqr/ESPerr.pqr → VMD | .fch + 待检.chg | 输出RMSE/RRMSE，可限特定原子/片段比较，误差文件用VMD按电荷着色可视化 | [4.7](sec-4-7-population-analysis-and-atomic-charge-calculation.md) |
| PEOE电荷 | 主功能7（布居分析与原子电荷）→ 19 | .xyz/.pdb/.mol（仅需几何） | 纯经验迭代、秒出结果，适合大有机体系快速电荷 | [4.7](sec-4-7-population-analysis-and-atomic-charge-calculation.md) |
| CM5与1.2×CM5电荷 | 主功能7（布居分析与原子电荷）→ 16 → 1（CM5）/ -16（1.2×CM5） | 真空下DFT小基组波函数（如B3LYP/def2-SVP的.fchk） | 1.2×CM5供OPLS-AA力场，有1.2CM5.sh脚本全自动算优化+拟合+输出chg | [4.7](sec-4-7-population-analysis-and-atomic-charge-calculation.md) |
| AIM电荷 | 主功能7（布居分析与原子电荷）→ 14 → 2（中质量格点） | .wfn | 盆积分求原子电荷，提高格点质量可改善积分精度但成本上升 | [4.7](sec-4-7-population-analysis-and-atomic-charge-calculation.md) |

## 实例 4.8–4.15
| 功能 | 菜单路径 | 输入 | 关键选项与产出 | 来源 |
|---|---|---|---|---|
| Mulliken 轨道组成分析（乙酰胺 MO6 的基函数/壳层/原子组成） | 主功能8（轨道组成分析）→ 1（Mulliken 划分）→ 输入轨道序号 | .fch/.mwfn/.molden/.gms（禁弥散函数） | 打印各基函数 Local/Cross/Total 组成与原子组成，末尾给出轨道离域指数 | [4.8](sec-4-8-molecular-orbital-composition-analysis.md) |
| 片段间成键的轨道贡献（甲基–甲酰胺交叉项） | 主功能8 → -1/-2（定义片段1/2）→ 4（Mulliken 片段组成与交叉项） | .fch 等含基函数文件 | 交叉项×占据数即该轨道贡献的片段间 Mayer 键级，正大者成键、负大者反键 | [4.8](sec-4-8-molecular-orbital-composition-analysis.md) |
| NAO 轨道组成分析（水 MO4 的原子轨道组成） | 主功能8 → 7（NAO 分析）→ 0（指定轨道） | 含 NAOMO 矩阵的 Gaussian 输出 .out（pop=nboread＋$NBO NAOMO，不用 .fch） | 输出核/价/Rydberg 三类 NAO 组成并凝聚到壳层与原子；虚轨道 Rydberg 占比大时不宜用 | [4.8](sec-4-8-molecular-orbital-composition-analysis.md) |
| 片段 NAO 对一批 MO 的贡献 | 主功能8 → 7 → -1（定义片段，a 选原子）→ 1（指定轨道范围） | 同上（含 NAOMO 的 .out） | 按 Core/Valence/Rydberg/Total 列出片段对每个 MO 的贡献百分比 | [4.8](sec-4-8-molecular-orbital-composition-analysis.md) |
| Hirshfeld/Becke 轨道组成分析（乙酰胺 MO6） | 主功能8 → 8（Hirshfeld 划分）→ 选内置原子密度 → 输入轨道序号 | .fch/.wfn/.wfx 等（兼容弥散函数，只能给原子/片段组成） | 数值积分后自动归一化输出各原子百分比；Hirshfeld-I 开销大且改进有限，一般不用 | [4.8](sec-4-8-molecular-orbital-composition-analysis.md) |
| 某原子对一批轨道的组成与布居 | 主功能8 → 8 → -2（指定原子与轨道范围） | 同上 | 输出组成％与布居数并加和；全占据轨道范围加和即 Hirshfeld 原子布居，可得原子电荷 | [4.8](sec-4-8-molecular-orbital-composition-analysis.md) |
| LOBA/mLOBA 氧化态计算 | 主功能19（轨道定域）→ 1（只定域占据轨道）→ 主功能8 → 100 → 输入阈值（或 m 选 mLOBA） | .fch（需先做常规 Gaussian 计算） | 输出各原子及指定片段氧化态，加和等于体系净电荷；mLOBA 无需选阈值，优先使用 | [4.8](sec-4-8-molecular-orbital-composition-analysis.md) |
| 轨道离域指数 ODI 定量轨道空间离域 | 主功能8 → 1/8（任选组成方法）→ 分析指定轨道 | .fch/.fchk 等 | 输出附带的 ODI 值越小轨道越离域；任意实空间函数的离域另用主功能 300 系的 SDI | [4.8](sec-4-8-molecular-orbital-composition-analysis.md) |
| AIM/ELF 等盆贡献的轨道组成（CH3COCl） | 主功能17（盆分析）→ 1（产生盆并找吸引子，选电子密度/AIM 或 ELF 等）→ 11（计算各盆的轨道组成） | 含 GTF 信息的 .wfn/.wfx/.fch/.molden/.mwfn | 输入轨道序号即得各盆百分比；-9 可定义原子组输出片段贡献，-4 导出全部至 orbcomp.txt | [4.8](sec-4-8-molecular-orbital-composition-analysis.md) |
| Mayer 键级与原子总价/自由价（乙酰胺） | 主功能9（键级分析）→ 1（Mayer 键级） | .mwfn/.fch/.molden/.gms（必须含基函数） | 输出大于阈值（settings.ini 的 bndordthres）的键级与总价；选 y 导出完整键级矩阵 bndmat.txt | [4.9](sec-4-9-bond-order-analysis.md) |
| 轨道占据数微扰 Mayer 键级（找成键主要贡献轨道） | 主功能9 → 6 → 输入两个原子序号 | 同上 | 输出逐个移除占据后键级变化量 Variance，负得越多该轨道成键贡献越大 | [4.9](sec-4-9-bond-order-analysis.md) |
| 模糊键级 Fuzzy bond order | 主功能9 → 7 | .wfn/.wfx 等亦可（不依赖基函数，兼容弥散函数） | 输出与 Mayer 相近的键级表；强极性键两者可能明显偏离 | [4.9](sec-4-9-bond-order-analysis.md) |
| 用 GaussView 显示键级（技巧） | 主功能9 → 1 → y（导出 bndmat.txt）→ 0 → 主功能1000（隐藏功能）→ 13（转含键级 .gjf） | .fch＋GaussView≥6.0 | 生成 gau.gjf（含连接与键级），在 GaussView 中 Results→Bond Properties 着色/标注显示 | [4.9](sec-4-9-bond-order-analysis.md) |
| 多中心键级（Li6 三中心键、菲六中心共轭） | 主功能9 → 2 → 按连接顺序输入原子序号 | .mwfn/.fch/.molden/.gms | 输出多中心键级与归一化值；相同原子数直接比前者，不同原子数比归一化值 | [4.9](sec-4-9-bond-order-analysis.md) |
| NAO 基多中心键级（含弥散体系） | 主功能9 → -2（NAO 基多中心键级）→ 输入原子序号 | 含 DMNAO 关键词的 NBO/Gaussian 输出 .out | 无弥散时与常规选项 2 结果一致；有弥散时仍稳健，须用此路径 | [4.9](sec-4-9-bond-order-analysis.md) |
| Laplacian 键级 LBO（乙烷/乙烯/乙炔 C–C，H2O O–H） | 主功能9 → 8 | .wfn/.fch 等 | 输出各键 LBO，只反映共价成分，与键离解能线性相关好，可比 C–H 强弱顺序 | [4.9](sec-4-9-bond-order-analysis.md) |
| NAO 基 Wiberg 键级分解为原子轨道对贡献（甲醛） | 主功能9 → 9 | 含 DMNAO 的 Gaussian 输出 .out | 输出原子轨道对/壳层对对 Wiberg 键级的贡献分解 | [4.9](sec-4-9-bond-order-analysis.md) |
| Mulliken 键级分解为轨道贡献（CH3CONH2 C–C） | 主功能9 → 5 → 输入两个原子序号 | .fch（需基函数） | 逐轨道输出贡献值，正为成键、负为反键；结合等值面/占据数微扰 Mayer 交叉验证 | [4.9](sec-4-9-bond-order-analysis.md) |
| 本征键强度指数 IBSI（乙炔 IGM/IGMH） | 主功能9 → 10 → 1（开始计算，选积分格点质量）；选项 2 切换 IGM/IGMH/mIGM 型 | .wfn（含波函数算 IBSI-IGMH；纯坐标 .pdb/.xyz 只能算 IBSI-IGM） | 输出原子对距离、积分项与 IBSI 值；IGMH 型与 BDE 线性相关好，IGM 型较差 | [4.9](sec-4-9-bond-order-analysis.md) |
| AV1245/AVmin 芳香性指数（菲局域环、卟啉大环路径） | 主功能9 → 11 → 按连接顺序输入环原子 | .fch | 输出各四中心电子共享指数与 AVmin（×1000），定量比较局域/全局芳香性 | [4.9](sec-4-9-bond-order-analysis.md) |
| 总态密度 TDOS（N-phenylpyrrole） | 主功能10（DOS 作图）→ 0（绘制，不定义片段即只画 TDOS） | .fch/.mwfn/.molden/.gms（只画 TDOS 也可用 MO 能级文本或 pop=full 的 Gaussian 输出） | 曲线为展宽 TDOS，竖线为 MO 能级、虚线标 HOMO；选项 8 切 eV、选项 2 设能量范围、选项 9 以线高表简并度 | [4.10](sec-4-10-plot-density-of-states-dos-maps.md) |
| 片段 PDOS 与片段间 OPDOS | 主功能10 → -1（定义至多 10 个片段，OPDOS 只画片段 1–2 间）→ 0 | .fch 等含基函数文件（Mulliken 组成时禁弥散；Hirshfeld/Becke 组成兼容弥散但无 OPDOS） | 左轴 TDOS/PDOS、右轴 OPDOS（选项 14 缩放）；选项 7 切换组成方法，选项 4/16 调坐标轴与图例 | [4.10](sec-4-10-plot-density-of-states-dos-maps.md) |
| 特定原子轨道的 PDOS（如 N 的 px、s/p/d 分类、π-MO 筛选） | 主功能10 → -1 → cond 条件选基函数（原子范围＋序号＋类型 X/S/P/D）→ 0 | .fch（分子取向已知，如 YZ 平面内 px 即 π） | 只含所选基函数的 PDOS 曲线；l s / l p / l d 可一次选定某角动量全部基函数 | [4.10](sec-4-10-plot-density-of-states-dos-maps.md) |
| MO-PDOS 图（cyclo[18]carbon σ/面内π/面外π） | 主功能10 → -2（定义 MO 片段）→ 输入各组 MO 序号 → 0 | .fch/.fchk（含占据与虚轨道） | 三组 MO 的 PDOS 曲线高度之和等于 TDOS；s 可存状态文件（.dat），l 可载入重绘 | [4.10](sec-4-10-plot-density-of-states-dos-maps.md) |
| 单点局域态密度 LDOS（丁二烯端碳上方） | 主功能10 → 10（单点 LDOS）→ 输入坐标；或先主功能 0 查坐标 | .fch | 输出该空间点的态密度曲线，可与 TDOS 对比，用于解释 STM 数据 | [4.10](sec-4-10-plot-density-of-states-dos-maps.md) |
| 沿直线的一组点 LDOS 颜色填充图 | 主功能10 → 11 → 输入直线两端点 → 取点数（如 200） | .fch | X 轴能量、Y 轴线上位置的颜色图；选项 4 调整纵横比 | [4.10](sec-4-10-plot-density-of-states-dos-maps.md) |
| 开壳体系 α/β 自旋 DOS（Na3O@Si12C12） | 主功能10 → -1（定义片段）→ 0；选项 6 切换 α/β/双自旋；后处理选项 3 导出曲线数据 | 非限制 .fchk | 默认只画 α；导出 alpha.txt/beta.txt 后在 Origin 中取负值可拼上下对称的 α/β 对比图 | [4.10](sec-4-10-plot-density-of-states-dos-maps.md) |
| 光电子谱 PES（Cr3Si12−，广义 Koopmans 定理） | 主功能10 → 12（PES 界面）→ 3（设位移＝VIP＋HOMO 能量）→ 4（设 X 轴）→ 1（绘制） | .fchk（体系第一垂直电离能 VIP 需另行算好） | Y 轴绝对值无意义（选项 13 可隐藏 Y 轴）；峰位与实验 PES 对照验证 | [4.10](sec-4-10-plot-density-of-states-dos-maps.md) |
| 过渡金属 d 带中心（Cu13） | 主功能10 → -1 → cond 选 D 型基函数为片段 → 8（切 eV）→ 2（设 X 轴包住 d 带）→ 0 | .fchk（含过渡金属 D 基函数） | 命令行直接打印 TDOS/PDOS 中心，减去 HOMO（费米能级惯例）即 d 带中心；X 轴上限一般取 0 | [4.10](sec-4-10-plot-density-of-states-dos-maps.md) |
| 晶体轨道哈密顿布居 COHP（C60 近邻原子、N-phenylpyrrole 片段间） | 主功能10 → -7（切 COHP 模式）→ 1（由波函数生成 Kohn-Sham 矩阵）→（片段间则 -1 定义片段）→ 0 | .fch | 左轴展宽曲线、右轴尖峰高度，画的是 −COHP：正为成键态、负为反键态 | [4.10](sec-4-10-plot-density-of-states-dos-maps.md) |
| 红外 IR 光谱（NH3BF3） | 主功能11（绘制光谱）→ 1（IR）→ 0（绘制） | Gaussian/ORCA 振动分析输出（含 freq 频率与强度） | 直接打印吸收峰极值位置与高度；选项 14 按模式设频率比例因子校正谐振误差 | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| 紫外-可见光谱及单个跃迁贡献（乙酸） | 主功能11 → 3（UV-Vis）→ 15（输出指定跃迁贡献，设振子强度阈值）→ 0 | Gaussian TDDFT 输出（或按 3.13.2 格式手写的纯文本） | 生成 spectrum_curve.txt（含各跃迁列）与 spectrum_line.txt，可算某峰处各跃迁百分比贡献 | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| ECD 光谱及极值标注（天冬酰胺） | 主功能11 → 4（ECD）→ 2（速度表象旋光强度）→ 0；选项 16 设极大/极小标签内容与格式 | Gaussian TDDFT 输出（含 30 个低激发态） | 标注波长或 Y 值于峰上；s 保存绘图设置（.dat），l 载入快速重绘 | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| 构象加权 UV-Vis 光谱（plumericin） | 写 multiple.txt（每行：构象输出路径＋Boltzmann 权重）→ 主功能11 → 3 → 0 | 多个构象的 TDDFT 输出＋权重文件 | 粗红线为加权谱，余线为各构象谱；选项 18 切换各构象谱是否乘权重（即看贡献分解） | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| 构象加权 ECD 光谱（plumericin） | 同上，唯类型选 4（ECD）→ 2（速度表象）→ 0 | 同上 | 同上；可识别仅某构象有信号的波段（如约 180 nm 处构象 c 的贡献） | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| Raman 光谱与预共振 Raman（2-methyloxirane） | 主功能11 → 2（Raman）→ 0；预共振：载入预共振 Raman 输出后先选入射频率再进界面 | Gaussian Raman/预共振 Raman 输出 | 绘制前先把拉曼活性转为与激发波长、温度相关的拉曼强度；选项 14 做频率比例校正 | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| 多体系同图对比（含 SOC 与否，Ir 配合物） | 写 multiple.txt（多体系输出路径，SOC 数据在前）→ 主功能11 → 3 → 按提示选每套数据用 SOC 与否 | 多套 TDDFT/SOC-TDDFT 输出 | 一图对比不同构象/构型/分子/计算条件；SOC 使三重态分裂，态数大增，图例自动标注 | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| VCD 光谱（S-methyloxirane 手性分子） | 主功能11 → 5（VCD）→ 14（频率比例因子）→ 0 | Gaussian VCD 输出 | 与 IR 流程相同，唯光谱类型选 VCD；仅手性分子有信号 | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| ROA 光谱（S-methyloxirane） | 主功能11 → 6（ROA）→ 选入射光频率 → 选散射类型（如 SCP(180)背散射）→ 14（比例因子）→ 0 | Gaussian ROA 输出 | 六种数据类型中常用背散射圆偏振 ROA；余同 VCD | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| shell 脚本批量绘制一批文件的光谱（技巧） | 理论（无直接菜单）：shell 循环逐个调用 Multiwfn 主功能 11 | 一批光谱输入文件＋脚本 | 一次跑完一批体系的光谱图片/数据，视频教程见节内链接 | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| 用尖峰标示跃迁能级位置（技巧，NH3BF3 B–N/N–H 振动） | 主功能11 → 1 → 23（设尖峰显示状态）→ 选尖峰组、模式与颜色 → 0 | Gaussian freq 输出（模式序号可查 GaussView） | 光谱底部以不同颜色尖峰标出指定振动模式位置 | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| NMR 谱（乙醛 13C、吡啶定标、缬氨酸构象加权） | 主功能11 → 7（NMR）→ 选项 6 选元素 → 选项 7 定化学位移（TMS 参考/斜率截距定标法）→ 0 | Gaussian NMR 输出；加权谱用 multiple.txt（构象输出＋权重） | X 轴由绝对屏蔽转为化学位移；可指定只显示某元素或隐藏特定核 | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| 荧光光谱（BODIPY） | 主功能11 → 3（UV-Vis）→ 清零 S2 及以上激发态振子强度 → 绘制 | S1 优化几何下的激发态 Gaussian 输出 | 仅保留 S1→S0 相关跃迁即得荧光谱；与吸收谱流程仅此一处不同 | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| 部分振动谱 PVS/部分振动能态密度 PVDOS/重叠 OPVS（C18-B9N9） | 主功能11 → 1（IR）→ 24（设 PVS 片段：定义片段 1/2、片段间 OPVS）→ q →（v 切换为振动 DOS）→ 0 | Gaussian freq 输出 | 总 IR 谱分解为各片段 PVS 曲线与片段间 OPVS；v 切换后 PVS/PVDOS、OPVS/OPVDOS 对应 | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| 定向 UV-Vis 光谱（碳纳米管片段 XY/Z 方向） | 主功能11 → -3（定向 UV-Vis）→ 选方向（如 4 为 XY 方向）→ 0 | Gaussian TDDFT 输出（含跃迁偶极矩） | 分方向曲线相加即常规总谱；判定某吸收峰的跃迁偶极矩主方向、各向异性来源 | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| 颜色预测（靛蓝理论谱、诱惑红实验谱） | 理论谱：主功能11 → 3 → 25（按可见区光谱评价颜色）；实验谱文本：主功能11 → 0 | TDDFT 输出，或实验 UV-Vis X–Y 纯文本 | 显示原色与互补色（含最大亮度版）及 CIE XYZ/RGB 参数；互补色即溶液实际呈现颜色 | [4.11](sec-4-11-plot-various-kinds-of-spectra.md) |
| 分子表面 ESP 定量分析（苯酚 vdW 表面） | 主功能12（分子表面定量分析）→ 0（默认 ESP 默认面下开始） | .wfn/.wfx 等（B3PW91/6-31G** 可用，更准用 def-TZVP/def2-TZVP） | 输出表面极值位置数值、表面积/体积、平均值/方差/nu/Pi/MPI 等；后处理选项 0 可视化极值点 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| 表面 ESP 区间统计分布直方图 | 上述分析后处理界面 → 9 → 原子范围 → ESP 范围 → 区间数 → 单位 | 同上 | 输出每段 ESP 区间面积与占比，可导入作图软件画直方图；也可只统计指定原子局域表面 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| AIM 非键半径与互穿距离 | 上述分析后处理界面 → 10 → 输入原子序号 | 同上 | 输出原子核到 ρ=0.001 面最短距离；两原子非键半径之和减键长即互穿距离，衡量氢键强度 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| 重用已算映射函数数据（技巧，N-phenylpyrrole） | 算完后后处理选项 7 导出 vtx.txt；下次主功能12 → 5（外部加载映射函数）→ 1（纯文本加载全部顶点）→ 0 | 同体系波函数＋vtx.txt | 跳过耗时的 ESP 等计算直接得相同分析结果；仅 cube 输入时可改选由外部 cube 插值 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| 仅用 cube 文件做表面 ESP 分析（无波函数程序） | 先载入 density.cub → 主功能12 → 1（改表面定义）→ 11（内存格点等值面）→ 0.001 → 2（选映射函数）→ 1（ESP）→ 5（外部加载）→ 3（由 cube 插值）→ 0 → 输入 ESP.cub | density.cub＋ESP.cub（网格设置完全相同，间距≤0.25 Bohr） | 与常规表面 ESP 分析等价；CPU 核少时 ESP 计算可改 cubegen/orca_vpot 路径加速 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| 平均局域电离能 ALIE 表面分析（苯酚） | 主功能12 → 2（重选映射函数）→ 2（ALIE）→ 0 | .wfn（B3PW91/6-31G**） | 输出极值、体积面积与 ALIE 均值方差；表面 ALIE 最小处为亲电/自由基进攻有利位点 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| 原子局域表面分析解释位点选择性（丙烯醛亲核位点） | 主功能12 → 0（全表面 ESP）→ 后处理选项 11（输出每个原子局域表面性质，可导出 locsurf.pqr 在 VMD 按 ResID 查看划分） | .wfn | 比较各原子局域表面 ESP 平均值：羰基碳最正即硬亲核试剂最有利位点 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| 分子表面 Fukui 函数 f− 定量分析（苯酚） | 主功能12 → 2（选映射函数）→ 0（由外部文件加载 Fukui）→ 1（改表面定义）→ 1（电子密度等值面）→ 0.01（等值放大以利分析）→ 0 | 中性/阳离子/阴离子三套波函数（或 Fukui cube） | 输出 f− 极值位置数值、各原子局域表面平均值，并可绘制带极值点的 f− 着色表面 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| Becke 表面分析（GC 碱基对单体间弱相互作用） | 主功能12 → 1（改表面定义）→ 6（Becke 面，5 为 Hirshfeld 面）→ 感兴趣原子范围 → 0 | .wfn | 输出表面极值与统计；后处理选项 -3 可视化表面，选项 8 导出 vtx.pqr 到 VMD 画映射点图 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| Hirshfeld 表面与指纹图分析（尿素晶体团簇） | 先主功能300 → 7（几何操作）→ 25（由 .cif 提分子团簇）；载入团簇 → 主功能12 → 1 → 5（Hirshfeld 面）→ 中心分子原子 → 0 → 后处理 20（指纹图）→ 定义内外原子 → 0/1 | .cif（或团簇 .pdb） | 输出 d_norm 映射表面与指纹图 pdf（含局域接触面积）；VMD 可画 Hirshfeld/Becke 着色等值面 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| 基于表面 ESP 预测分子晶体密度（FOX-7） | 主功能12 → 0（默认 ESP 分析） | B3PW91/6-31G** 下 .wfn（公式参数只适配此水平） | 取输出 M/V 与 νσ² 代入 ρ=0.9183(M/V)＋0.0028(νσ²)＋0.0443；同法还可预测汽化热/沸点/溶剂化自由能 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| 轨道重叠距离函数 D(r) 表面分析（硫代甲酸） | 主功能12 → 2 → 6（D(r)，选 EDR 指数方案）→ 0 | .wfn | 输出表面极小/极大位置数值；孤对紧缩处为极小、弥散处为极大 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| 整体与片段 vdW 表面积（多巴胺氨基占比；无波函数用前分子密度） | 主功能12 → 1 → 1（电子密度等值面，气相 0.001/凝聚相 0.002）→ 6（无映射函数直接分析）；片段：后处理选项 12 → 原子序号；无波函数：表面函数选 1（前分子密度） | .wfn（或仅 .xyz，此时用前分子密度近似） | 输出整体面积；片段面积除以整体即占比；可导出 locsurf.pqr 在 VMD 按 ResID 显示局域划分 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| σ-hole/π-hole 面积定量化（ClPO2） | 主功能12 → 0（常规 ESP 分析）→ 后处理选项 14（极值周围区域面积与均值）→ 选极大/极小与编号 → 设判据（如 π 洞 0.04、σ 洞 0.03 a.u.） | .fch（PBE0/def2-TZVP） | 输出选中区域顶点数、面积、平均值与乘积，导出 selsurf.pqr 在 VMD 按 charge 显示定界；判据通常取极大值约 60% 或低 10 kcal/mol | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| ESP 分子表面类盆分析（ClPO2 表面盆地） | 主功能12 → 0 → 后处理选项 15（类盆划分并算面积） | .fch | 输出每个表面极值点对应盆的顶点数、面积与平均 ESP，并导出 surfbasin.pdb（Beta 值为盆编号）在 VMD 按 Beta 着色查看 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| 小分子动力学直径估计（CO） | 主功能0 确认分子轴取向 → 主功能12 → 1 → 1 → 0.0015（等值面）→ 6 | PBE0/def2-TZVP 下 .fch | 输出全部表面顶点 Min/Max-X/Y/Z，垂直分子轴方向跨度除以拟合斜率 1.025 即直径；复杂分子以后处理选项 6 导出 vtx.pdb 在 VMD 量两顶点距 | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| 局域电子亲和能 LEA/局域电子附着能 Eatt 揭示亲电区（CH3Cl） | 脚本流程（examples\\scripts\\local_EA 下 .bat＋.vmd，调用 Multiwfn 生成 density.cub/userfunc.cub/surfanalysis.pdb 后 VMD 着色） | 含虚轨道的 .fchk/.fch（LEA 禁弥散；Eatt 要求至少 LUMO 能量为负，常需加弥散如 6-31+G(d,p)） | 等值面（LEA 取 ρ=0.01、Eatt 取 ρ=0.004）按能量着色，青球为表面极值；越负 Eatt/越正 LEA 处亲电性越强（如甲基端与 Cl σ-hole） | [4.12](sec-4-12-quantitative-analysis-of-molecular-surface.md) |
| 提取平面内数据点（XY 平均面、任意三原子斜面） | 载入 .cub（或主功能 5 算好格点后 0 返回）→ 主功能13（处理格点数据）→ 5（平均平面，输 Z 范围）或 8（三原子定面，选容差与是否投影到 XY） | .cub/.grd/.vti 或内存格点 | 导出 output.txt（坐标＋数值）供 Sigmalpot 等画平面图；不做插值，格点稀疏时斜面数据点稀 | [4.13](sec-4-13-process-grid-data.md) |
| 格点数据数学运算（cube 相减、双轨道密度加和） | 主功能13 → 11（格点计算）→ 4（A 减 B）或 10（A²＋B²＝C）→ 输入另一 cube → 0（导出新 cube） | 两个网格设置完全相同的 .cub | 内存格点更新为运算结果并可导出；电子密度差、双轨道总密度等均由此得到 | [4.13](sec-4-13-process-grid-data.md) |
| 缩放格点数值范围（ELF 0–1 转 0–65535） | 主功能13 → 16（缩放范围）→ 原范围 → 目标范围 | 内存格点（如主功能 5 算的 ELF） | 按 3.16.12 算法线性缩放全部格点值，可导出 cube 或继续提取平面数据 | [4.13](sec-4-13-process-grid-data.md) |
| 筛除局域区域等值面（只留右单体；只留片段交叠区） | 单片段：主功能13 → 13（按距原子远近设值）→ 选内外模式 → 设值 → 选原子；交叠区：主功能13 → 14 → 缩放 vdW 倍数 → 设填充大值 → 给两片段原子表 | .wfn 算出的格点或 RDG.cub＋原子序号文件 | 不关心区域格点被置 0（或交叠区外置大值），选项 -2 预览等值面确认；NCI 分子间区可视化常用 | [4.13](sec-4-13-process-grid-data.md) |
| 分子轨道重心（苯酚 MO10 正负部分与绝对值总重心） | 主功能5 算好轨道格点后 0 返回 → 主功能13 → 17（统计数据）→ 1（全部点）；绝对值重心先 11 → 13（取绝对值）再 17 | .wfn＋主功能 5 的轨道格点 | 输出正/负/总重心坐标、积分、体积与最值；总积分为零的轨道应看绝对值重心以定位轨道分布 | [4.13](sec-4-13-process-grid-data.md) |
| 电荷位移曲线 CDC（外电场下聚炔电荷转移） | 主功能5 自定义操作算密度差格点 → 0 → 主功能13 → 18（积分曲线）→ 选方向（如 Z）→ 范围 → 选项 2 看局域积分曲线 → 选项 1 看 CDC | field 与无 field 两套 .wfn（Gaussian field=z+300 施加电场） | 局域积分曲线峰正负对应密度增减区；沿轴积分即 CDC，中点最小值即半分子得失电子数 | [4.13](sec-4-13-process-grid-data.md) |
| 电子密度交叠 min(ρ1,ρ2)（甲烷二聚体） | 分别以同一网格算两单体密度 cube → 主功能13 → 11 → 21（取两套数据逐点最小值）→ 0（导出 overlap.cub，补原子坐标头） | dimer.pdb 定网格的 userfunc.cub＋两单体 .wfn（Gaussian 用 nosymm 防重定向） | 交叠格点可视化单体密度明显交叠区；静默模式可大幅减少操作步骤 | [4.13](sec-4-13-process-grid-data.md) |
| 圆柱区域内积分电子密度（乙炔 C–C 键） | 主功能5 算好电子密度后 0 返回 → 主功能13 → 17 → 2（特定空间数值范围）→ 2（圆柱）→ 两端点坐标 → 半径 | .wfn | 输出区域内最值、体积、正负积分、重心坐标；选 y 导出参与格点 grid.xyz 在 VMD 核对区域 | [4.13](sec-4-13-process-grid-data.md) |
| AdNDP 穷举搜索多中心键（Li5+ 两个 4c-2e） | 载入含 AONAO/DMNAO 的 NBO 输出 → 主功能14（AdNDP）→ 选项 2 逐级搜 1c→nc（选项 3 预设中心数）→ 选项 0 取出高占据候选 → 选项 5 看已取列表 | Gaussian 输出 .out（路线 pop=nboread，尾加 $NBO AONAO DMNAO $END）＋同名 .fch（禁弥散函数） | 占据数≈2 即理想 nc-2e 键；剩余价电子≈0 时停止；选项 11/12 存取当前状态防取错 | [4.14](sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md) |
| 查看与导出 AdNDP 轨道（等值面/cube） | AdNDP 界面 → 选项 7（图形界面查看，需 .fch 提供基组）→ 选项 9（导出 cube，选质量与序号范围） | 同上 | 得 AdNDPorbXXXX.cub，可用 VMD/Molekel 绘制；B11− 例一次导出 1–17 号轨道 | [4.14](sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md) |
| AdNDP 轨道能量 | 由 .gjf 改写 $NBO archive 得 .47 文件（含 Fock 矩阵）→ AdNDP 界面选项 16 → 输入 .47 路径 | .47 文件（如 examples\\AdNDP\\Li5+.47） | 直接打印各已取 AdNDP 轨道能量（a.u./eV）；等价轨道能量简并 | [4.14](sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md) |
| B11− 分步取轨避免重复计数（9 个 2c＋5 个 3c＋2 个 5c＋1 个 7c） | 主功能14 → 选项 2 搜 2c → 选项 0 分批取出（先取无共享原子的，再取其余）→ 选项 8 检查候选 → 选项 2 逐级搜 3c/5c/7c（占据过低如 <1.9 不取） | B11-.out＋B11-.fch（HF/STO-3G 已够，AdNDP 对基组不敏感） | 剩余价电子 1.34（<2）时结束；选项 5 打印全部轨道占据与原子归属，残余电子即非 Lewis 电子 | [4.14](sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md) |
| VMD 脚本同时绘制一批 AdNDP 轨道 | 理论（无直接菜单）：选项 9 导出全部 cube 后编辑 plotAdNDP.vmd（路径、起止编号、等值与颜色）粘入 VMD | 全部 AdNDPorb cube＋体系 .xyz | VMD 主窗口每条目一轨道，双击 D 显隐；叠加 CPK 结构得 2c/3c/5c/7c 分组图 | [4.14](sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md) |
| 菲的用户导向搜索（两侧 6c-2e 芳香环） | 主功能14 → 选项 2 取 C–H/C–C σ 与中央 π 后 → 选项 13（看各原子剩余布居定搜索范围）→ 选项 1（在指定片段如 1–6 号原子上搜索）→ 取出高占据轨道 | phenanthrene.out（＋.47 供能量分析） | 每侧得 3 个占据≈2 的 6c-2e π 轨道，等值面如苯 π 轨道；也可用 -1 定搜索列表＋选项 3 定中心数达到同样效果 | [4.14](sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md) |
| Au20 大团簇 AdNDP（100 个 1c＋10 个 4c） | 主功能14 → 2（搜 1c，100 个全取）→ 0 取 100 → 2 搜 2c/3c（无）→ 2 搜 4c → 0 取前 4 → 0 取后 6 → 选项 9 → 质量 → 101–110（导出 4c 轨道 cube） | Au20.out（B3PW91/Lanl2DZ，可下载） | 1c 全为孤对，4c 占据 1.84/1.76 仍值得取出；VMD 脚本批量绘制十个 4c 轨道 | [4.14](sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md) |
| AdNDP 轨道组成分析 | AdNDP 界面选项 15（NAO 法，直接指定轨道号）或选项 14（导出 AdNDP.mwfn 后按 4.8 做常规组成分析） | 同 AdNDP 输入（NAO 法需 NBO 信息） | 如菲 6c-2e 轨道纯由 px 价 NAO 组成且集中于特定原子，验证 π 离域图像 | [4.14](sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md) |
| 模糊空间离域/定域指数 DI/LI（苯 C–C/C–H 键级） | 主功能15（模糊原子空间分析）→ 4（算 LI/DI） | .wfn（B3LYP/6-31G*；格点不足致 AOM 误差大时关 iautointgrid 并加大 radpot/sphpot） | DI 矩阵即模糊键级：苯 C–C 1.467（σ＋半个 π）、C–H 0.877；σ/π 成分明显时结果需谨慎解读 | [4.15](sec-4-15-fuzzy-atomic-space-analysis.md) |
| DI-σ/DI-π 分解（苯对位 π 离域大于间位） | 主功能6（修改波函数）→ 26（改占据数，全置 0 后只留 π 轨道占 2）→ -1 → 主功能15 → 4 | 同上（需事先看等值面定 π 轨道号） | 余下 DI 即 DI-π；对位/间位/邻位对比揭示 π 离域拓扑 | [4.15](sec-4-15-fuzzy-atomic-space-analysis.md) |
| PDI 芳香性指数（菲中间环 vs 边缘环） | 主功能15 → 5 → 按连接顺序输入环原子 | .wfn（Becke 默认划分；大体系 AOM 计算耗时） | 输出对位三对 DI 均值；边缘环 PDI 大→芳香性强；AOM 只算一次，后续 FLU 直接复用 | [4.15](sec-4-15-fuzzy-atomic-space-analysis.md) |
| FLU/FLU-π 芳香涨落指数（菲） | 主功能15 → 6（FLU）→ 输入环原子；FLU-π 用选项 7（先输入 π 轨道号） | .wfn | 值越小越像苯（越芳香）；FLU-π 同样给出边缘环更芳香，与 PDI 一致 | [4.15](sec-4-15-fuzzy-atomic-space-analysis.md) |
| PLR 对位线性响应指数（菲） | 主功能15 → 10 | .mwfn/.fch/.molden/.gms（需虚轨道，.wfn 不行） | 输出 CLRK 矩阵后给环的 PLR；边缘环显著大于中间环；PDI/PLR 均可再分 σ/π 成分 | [4.15](sec-4-15-fuzzy-atomic-space-analysis.md) |
| 片段偶极矩展示局域极性（苯酚二聚体两单体） | 主功能15 → -1 → 3（Hirshfeld 内置原子密度）→ 2（原子与分子多极矩）→ 1（屏幕输出）→ -5（指定原子算片段）→ 2 → 1 | .wfn | 输出片段偶极/四极/八极矩与净电荷；主功能 100 → 2 导出 .xyz 后用 drawarrow.tcl 在 VMD 画矢量对比 | [4.15](sec-4-15-fuzzy-atomic-space-analysis.md) |
| 原子有效/自由体积、极化率与 C6 系数（环氧乙烷、SiH4） | 主功能15 → 13 → 依次输入各元素孤立原子波函数；SiH4 例先 -1 → 5（MBIS 划分）→ 1（建空间）再 13 | 分子 .fchk/.fch＋各元素原子 .wfn（与分子同水平；SiH4 用 B3LYP/6-311+G(2df,p)＋MBIS 效果最好） | 输出 Veff/Vfree/比值、TS 法原子极化率及占比、原子 C6 与同分子 C6；划分敏感时看“Contribution”占比而非绝对值 | [4.15](sec-4-15-fuzzy-atomic-space-analysis.md) |
| 原子偶极矩/四极矩可视化（H2O2 箭头、C6H5Br 椭球） | 主功能15 → 2 → 2（输出 multiple.txt＋atom_moment.txt）；AIM 划分改用主功能 17 子功能 8 | .fch/.mwfn＋VMD＋atomdip.tcl/atomquad.tcl 脚本 | VMD 中 source 后运行 atomdip/atomquad：箭头由负电中心指正电中心，椭球短轴对应电子伸展方向（如 Br σ-hole） | [4.15](sec-4-15-fuzzy-atomic-space-analysis.md) |

## 实例 4.16–4.25
| 功能 | 菜单路径 | 输入 | 关键选项与产出 | 来源 |
|---|---|---|---|---|
| 闭壳层体系 CDA/ECDA 分析（CO→BH₃ 施舍-反馈） | 主功能16（电荷分解分析）→ 选项2（定义两片段） | 配合物与两片段的 .fch（如 COBH₃/CO/BH₃） | 选项2输出配合物轨道组成；选项5绘轨道相互作用图；选项6分解 d/b/r 到片段轨道对贡献 | [4.16](sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md) |
| 开壳层（共价结合）体系 CDA 分析（CH₃–NH₂） | 主功能16（电荷分解分析）→ 选项2（定义两片段）→ 翻转其中一片段自旋 | 配合物 .fch＋两开壳层片段 .fch | 须翻转一片段自旋使 α/β 电子数守恒；ECDA 的净转移比 d−b 更可靠 | [4.16](sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md) |
| 多片段 CDA 分析（顺铂 Pt²⁺/(Cl₂)²⁻/(NH₃)₂） | 主功能16（电荷分解分析）→ 选项3（定义三片段）→ 选项0选片段对 | 配合物与三片段的 .fch（原子顺序须与配合物一致） | 两两片段对分别给出 d/b/d−b/r；ECDA 仅适用于两片段 | [4.16](sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md) |
| 基于 RO 波函数的 CDA 分析（乙烷） | 主功能6（修改波函数）→ 选项37（拆分 RO 轨道为 α/β）→ 主功能100 → 选项2 → 7（导出 .fch）→ 主功能16 → 选项2 | RO 波函数 .fch（先转为 UKS 形式） | 先把两 RO 片段转为 UKS 再做常规两片段 CDA（其中一片段翻转自旋） | [4.16](sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md) |
| 绘制轨道相互作用图 | 主功能16（电荷分解分析）→ 选项5（绘制轨道相互作用图）→ 选项3设能量范围 → 选项1绘图 | CDA 已载入的配合物＋片段波函数 | 选项5可切换 α/β 自旋；红线连接组成＞10% 的片段轨道与配合物轨道 | [4.16](sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md) |
| AIM（电子密度）流域生成、吸引子定位与可视化（HCN） | 主功能17（流域分析）→ 选项1（生成流域并找吸引子）→ 选项1（电子密度）→ 选项0可视化 | .wfn/.fch 波函数文件 | 选项0可视化流域与吸引子；可选仅显示 ρ＞0.001 区域 | [4.17](sec-4-17-basin-analysis.md) |
| AIM 流域高精度积分与 AIM 电荷/体积 | 主功能17（流域分析）→ 选项7（原子中心＋均匀格点积分）→ 选项2（积分同时细化边界）→ 选项1（电子密度） | 已生成 AIM 流域 | 比纯均匀格点（选项2）准得多；同时输出 AIM 电荷、体积与归一化因子 | [4.17](sec-4-17-basin-analysis.md) |
| 流域电多极矩计算 | 主功能17（流域分析）→ 选项8（混合格点算电多极矩） | 已生成 AIM 流域 | 输出单极（电荷）、偶极、四极矩及电子空间范围 ⟨r²⟩ | [4.17](sec-4-17-basin-analysis.md) |
| 流域定域化/离域化指数（LI/DI） | 主功能17（流域分析）→ 选项4 → 选项2（混合格点算重叠矩阵） | 已生成流域 | 输出 LI 与 DI 矩阵；DI 可视为共价键级 | [4.17](sec-4-17-basin-analysis.md) |
| 含非核吸引子（NNA）的流域分析（Li₆） | 主功能17（流域分析）→ 选项1 → 选项1（电子密度）→ 选项7 → 选项2 | .fch 波函数文件 | 遇 NNA 警告直接回车继续；NNA 流域单独列出布居与电荷 | [4.17](sec-4-17-basin-analysis.md) |
| ELF 流域分析（乙炔） | 主功能17（流域分析）→ 选项1 → 选项9（ELF） | .wfn 波函数文件 | 简并环状吸引子自动聚类；按 ELF 符号记流域为 V/C 类型 | [4.17](sec-4-17-basin-analysis.md) |
| 静电势（ESP）流域分析（H₂O） | 主功能17（流域分析）→ 选项1 → ESP 对应选项 | .wfn 波函数文件 | 揭示孤对电子出现区域；同样可用选项2/7积分 | [4.17](sec-4-17-basin-analysis.md) |
| 电子密度差流域分析（H₂O） | 主功能17（流域分析）→ 选项1 → 电子密度差选项 | 分子与 promolecular 密度可比的输入 | 定量研究成键过程电子密度变形在各流域的得失 | [4.17](sec-4-17-basin-analysis.md) |
| AIM 流域中的源函数分析（乙烷 C–H 键 BCP） | 主功能2（拓扑分析）定位 BCP → 主功能17 → 源函数相关选项 | .wfn 波函数文件＋BCP 坐标 | 给出各原子（流域）对 BCP 处密度的贡献 | [4.17](sec-4-17-basin-analysis.md) |
| 局域区域流域分析（聚炔 C₁₄H₂） | 主功能17（流域分析）→ 选项1（选局域区域函数） | .wfn 波函数文件 | 适用于伸展体系的局域特征划分与积分 | [4.17](sec-4-17-basin-analysis.md) |
| ELF 流域布居数的原子贡献（CH₃NH₂ 的 V(C,N)） | 主功能17（流域分析）→ ELF 流域积分＋AIM 划分组合选项 | .wfn 波函数文件 | 基于 AIM 划分得到各原子对键流域布居的贡献，考察键极性 | [4.17](sec-4-17-basin-analysis.md) |
| HELP/HELV（高 ELF 定域域布居/体积） | 主功能17（流域分析）→ HELP/HELV 相关选项 | .wfn 波函数文件 | 表征孤对电子，与电离势、前线轨道能量相关 | [4.17](sec-4-17-basin-analysis.md) |
| 体系电子能量的原子贡献 | 主功能17（流域分析）→ 能量划分相关选项 | .wfn/.fch 波函数文件 | 把总电子能量分解到各 AIM 原子流域 | [4.17](sec-4-17-basin-analysis.md) |
| 按流域类型着色的 ELF 等值面图 | 主功能17（流域分析）→ 流域着色导出选项 → 第三方显示 | 已划分 ELF 流域 | 不同类型流域子区域着不同颜色，不随等值面值漂移 | [4.17](sec-4-17-basin-analysis.md) |
| 空穴-电子分析完整表征激发（D–π–A、Ru(bpy₃)²⁺） | 主功能18（电子激发分析）→ 选项1（空穴-电子分析）→ 选激发态 → 选项1（算分布与指标） | Gaussian TDDFT 的 .fch/.fchk＋含组态系数的 .out（须 IOp(9/40=4)） | 子功能2/3分别给出轨道贡献与原子/片段贡献；后处理菜单可视化空穴、电子、Sr、CDD 并算库仑吸引能 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| 跃迁密度/跃迁偶极（磁偶）极矩密度的实空间分析 | 主功能18（电子激发分析）→ 选项1 → 后处理可视化选项 | 同上（.fch＋.out） | 输出跃迁密度与 T(r) 等值面 cube；磁偶极密度须先开 -1 开关 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| 跃迁密度矩阵（TDM）热图分析 | 主功能18（电子激发分析）→ 选项2（跃迁矩阵热图） | .fch＋.out | 计算 TDM 后以原子/基函数热图展示离域与 CT 特征 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| 跃迁偶极矩矩阵分析 | 主功能18（电子激发分析）→ 选项2（载入 AAtrdipX.txt 类矩阵） | 已有跃迁偶极矩阵文本 | 把矩阵转为原子贡献并可视化 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| 基于电子密度差的电荷转移分析 | 主功能18（电子激发分析）→ 选项3（基于密度差格点分析 CT） | .fch＋.out | 定量给出激发前后电荷重排与 CT 量 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| Δr 指标计算（N-苯基吡咯） | 主功能18（电子激发分析）→ 选项4（计算 Δr） | .fch＋.out | 一次可算多个激发态的电荷转移长度 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| Λ 指标计算 | 主功能18（电子激发分析）→ 选项14（计算 Λ） | .fch＋.out | 表征激发的空间重叠/短程特征 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| 各态偶极矩与态间跃迁偶极矩（4-硝基苯胺） | 主功能18（电子激发分析）→ 选项5（算所有态间跃迁偶极矩与各态偶极矩） | .fch＋.out | 选项4取各态电偶极；选项0切换电/磁偶极类型 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| 自然跃迁轨道（NTO）产生与分析（尿嘧啶） | 主功能18（电子激发分析）→ 选项6（产生 NTO） | .fch＋.out | 选定激发态后输出 NTO 对，化简多组态跃迁图像 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| IFCT 片段间电荷转移与电荷转移矩阵热图 | 主功能18（电子激发分析）→ 选项8（IFCT） | .fch＋.out＋片段定义 | Mulliken 划分给出片段间转移矩阵并绘热图 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| 跃迁密度矩阵产生、导出与轨道表象变换 | 主功能18（电子激发分析）→ 选项9（产生并导出 TDM） | .fch＋.out | 可在基态-激发态或两激发态间产生 TDM 并变换表象 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| 跃迁偶极矩的分子轨道对分解 | 主功能18（电子激发分析）→ 选项10（分解为 MO 对贡献）→ 选项1（电偶极） | .fch＋.out | 输出各 MO 对对跃迁偶极的贡献（含 S1.txt 批量） | [4.18](sec-4-18-electron-excitation-analysis.md) |
| 片段贡献跃迁偶极矩箭头图 | 主功能18（电子激发分析）→ 片段箭头可视化选项 | .fch＋.out＋片段定义 | 把各片段对跃迁偶极的贡献画成空间箭头 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| 单个激发态电子结构/两激发态差别分析 | 主功能18（电子激发分析）→ 激发态波函数（自然轨道）→ 常规波函数分析 | CIS/TDDFT 激发态自然轨道文件 | 对激发态做与基态同类的波函数分析以比较差异 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| 电荷转移光谱与全激发态特征汇总（N-苯基吡咯） | 主功能18（电子激发分析）→ CTS 相关选项 | .fch＋.out | 一次输出所有激发态主要特征并绘 CTS | [4.18](sec-4-18-electron-excitation-analysis.md) |
| 基于电子激发的电子密度极化分析（CH₃Cl＋点电荷） | 主功能18（电子激发分析）→ 极化分析对应选项 | .fch＋.out | 考察外电场/点电荷下激发态密度极化 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| ECD/CPL 不对称因子 g 计算（(P)-[6]螺烯） | 主功能18（电子激发分析）→ g 因子（ECD/CPL）选项 | Gaussian/ORCA 电子激发输出 | 输出 g_abs/g_CPL，并可导出跃迁电/磁偶极矢量作图 | [4.18](sec-4-18-electron-excitation-analysis.md) |
| Pipek-Mezey 轨道定域化（丁二烯） | 主功能19（轨道定域化）→ 选项2（定域占据＋非占据轨道） | .fch（如 butadiene.fch） | 默认 PM-Mulliken；结果自动存 new.fch 并载入，主功能0查看 LMO | [4.19](sec-4-19-orbital-localization-analysis.md) |
| LMO 能量计算 | 主功能19（轨道定域化）→ 选项-4（允许算 LMO 能量）→ 选项1（由 MO 能量/系数经 F=SCEC⁻¹ 构建 Fock 矩阵） | .fch（或外供 Fock/.47 文件选选项2） | 按能量排序输出全部 LMO 能量 | [4.19](sec-4-19-orbital-localization-analysis.md) |
| LMO 中心位置显示（Foster-Boys，丁二烯） | 主功能19（轨道定域化）→ 选项-8（算 LMO 中心/偶极矩）→ 选项-6选方法10（Foster-Boys）→ 选项1（只定域占据轨道） | .fch | 中心以 Bq 原子标记并导出 LMOcen.txt，主功能0叠加显示 | [4.19](sec-4-19-orbital-localization-analysis.md) |
| SN₂ 反应路径 LMO 演化跟踪 | 主功能19（轨道定域化）→ 选项1（定域占据轨道）→ 选项0可视化 | IRC 各点 .fch（R/TS-1/TS/TS+1/P） | 对各点同法处理后并排比较 F–C/C–H 相关 LMO | [4.19](sec-4-19-orbital-localization-analysis.md) |
| [Re₂Cl₈]²⁻ 四重键的 LMO 表征＋微扰 Mayer 键级 | 主功能19（轨道定域化）→ 主功能9（键级分析，轨道占据数微扰 Mayer） | .fchk | σ/π/δ 四个 LMO 对键级的贡献分别为 ~0.94/0.66/0.47 | [4.19](sec-4-19-orbital-localization-analysis.md) |
| 基于双中心 LMO 的键偶极矩（CH₃NH₂） | 主功能19（轨道定域化）→ 选项-8（算中心/偶极）→ 选项1 → y（做偶极分析） | .fch | 结果存 LMOdip.txt，单/双中心轨道偶极分别列出 | [4.19](sec-4-19-orbital-localization-analysis.md) |
| NCI 弱相互作用分析 | 主功能20（弱相互作用可视化）→ 选项1（NCI） | .wfn 波函数文件 | 选项-1看 RDG–sign(λ₂)ρ 散点；选项3导出 cube 用 VMD 着色 | [4.20](sec-4-20-visual-study-of-weak-interactions.md) |
| 基于前分子密度的 NCI 分析（DNA 大体系） | 主功能20（弱相互作用可视化）→ 选项2（前分子 NCI）→ 模式7定格点盒 | .pdb 结构文件 | 无需波函数；格点盒中心/点数/延伸须手动设定 | [4.20](sec-4-20-visual-study-of-weak-interactions.md) |
| aNCI 动态环境弱相互作用（体相水 MD） | 主功能20（弱相互作用可视化）→ 选项3（aNCI） | .xyz 轨迹文件 | 平均 RDG/平均 sign(λ₂)ρ＋热涨落指数（TFI）评估稳定性 | [4.20](sec-4-20-visual-study-of-weak-interactions.md) |
| IRI 等值面/散点/平面图（苯酚二聚体、GC） | 主功能20（弱相互作用可视化）→ 选项4（IRI）→ 主功能4 → 选项24（IRI平面图） | .wfn 波函数文件 | 选项9屏蔽共价区只看非共价区；可导出散点数据用 gnuplot 绘图 | [4.20](sec-4-20-visual-study-of-weak-interactions.md) |
| DORI 分析（苯酚二聚体） | 主功能20（弱相互作用可视化）→ 选项4（DORI） | .wfn 波函数文件 | 与 IRI 流程相同；一般推荐用 IRI 代替 | [4.20](sec-4-20-visual-study-of-weak-interactions.md) |
| 范德华势可视化与极小点分析 | 主功能20（弱相互作用可视化）→ 选项6（范德华势） | .xyz 结构文件 | 可导出极小点 pdb/pqr/txt/gjf，在 VMD 中按残基号显示 | [4.20](sec-4-20-visual-study-of-weak-interactions.md) |
| IGM 可视化与定量分析 | 主功能20（弱相互作用可视化）→ 选项10（IGM）→ 选项2/3定义片段 | .wfn/.pdb/.xyz | δg 等值面＋原子对 δg 贡献；BCP 处 δg 与强度正相关 | [4.20](sec-4-20-visual-study-of-weak-interactions.md) |
| IGMH 分析（Hirshfeld 分割） | 主功能20（弱相互作用可视化）→ 选项11（IGMH）→ 定义片段 | 含波函数信息的 .wfn/.fch/.mwfn/.molden | 比 IGM 更少人为参数，显著改善离子体系描述 | [4.20](sec-4-20-visual-study-of-weak-interactions.md) |
| mIGM 分析（三聚体） | 主功能20（弱相互作用可视化）→ 选项-10（mIGM）→ 定义片段 | .xyz 结构文件 | 揭示多片段体系内部相互作用 | [4.20](sec-4-20-visual-study-of-weak-interactions.md) |
| amIGM 动态环境分析（配体-蛋白） | 主功能20（弱相互作用可视化）→ 选项-12（amIGM）→ 定义片段 | .xyz 轨迹文件 | aNCI 在 IGM 框架下的推广，做法与 aNCI 相同 | [4.20](sec-4-20-visual-study-of-weak-interactions.md) |
| EDA-FF 力场能量分解（水二聚体、C3GC 三聚体） | 主功能21（能量分解）→ 选项1（EDA-FF）→ 选项3载入 mollist → 选项2定义片段 → 选项1计算 | 结构文件（.mol/.pdb/.fch）＋原子类型/电荷文件（mollist.txt） | 输出静电/排斥/色散/总量及原子贡献；选项-3另存原子对明细 interatm.txt；选项-4输出 .pqr 着色 | [4.21](sec-4-21-energy-decomposition-analysis.md) |
| Shubin Liu 能量分解 EDA-SBL（乙烷旋转位垒） | 主功能21（能量分解）→ 选项2（EDA-SBL） | .fch＋含 ExtraLinks=L608 的 Gaussian .out | 输出 steric 等能量分量，比较 staggered/eclipsed 差值来源 | [4.21](sec-4-21-energy-decomposition-analysis.md) |
| sobEDA/sobEDAw 能量分解 | 理论（无直接菜单）：外部 sobEDA.sh 脚本调用 Gaussian＋Multiwfn | Gaussian 输入/输出 | 详见 sobEDA_tutorial.zip，本节仅作指向 | [4.21](sec-4-21-energy-decomposition-analysis.md) |
| 原子对色散能贡献/差值分析 | 主功能21（能量分解）→ 选项4（原子色散能贡献）→ 选项1算当前体系/选项3算两体系差值 | .xyz/.cif 结构文件 | 两体系比较时感兴趣原子数与顺序必须一致 | [4.21](sec-4-21-energy-decomposition-analysis.md) |
| CDFT 全局/凝聚量自动计算（苯酚） | 主功能22（CDFT）→ 选项1（生成 N/N+1/N−1 的 .gjf/.wfn）→ 选项2（算各指数，存 CDFT.txt） | .xyz 结构（如 phenol.xyz，需另行产生 N±1 波函数） | 一次给出 IP/EA、电负性、硬度、亲电/亲核指数及凝聚 Fukui/对偶描述符 | [4.22](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md) |
| 轨道加权 Fukui/对偶描述符（C₆₀、环[18]碳、CH₃Cl） | 主功能22（CDFT）→ 选项4设 Δ 参数 → 选项7算格点 → 选项5看权重/选项6算凝聚量 | .fch/.fchk | 解决前线轨道简并体系反应位点预测；Δf_w 对应自定义函数 98，可作平面图与表面极值分析 | [4.22](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md) |
| 准简并 HOMO/LUMO 的基于密度 CDFT（苯、C₆₀、O₂） | 主功能22（CDFT）→ 选项-3（设前线轨道简并度）→ 选项1准备 N/N+p/N−q 波函数 | .fch＋额外 N+p/N−q 波函数 | 仅依赖电子密度，理论更严格但需额外波函数；O₂ 用选项12（自旋极化 CDFT） | [4.22](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md) |
| Fukui 势与对偶描述符势（马来酸酐） | 主功能22（CDFT）→ 势函数相关选项 | .xyz＋N±1 波函数 | 在 M06-2X/6-311++G(d,p) 下复现文献结果 | [4.22](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md) |
| 键对偶描述符 BDD | 主功能22（CDFT）→ BDD 相关选项 | .fch | 输出各键的对偶描述符，判断键的亲电/亲核性 | [4.22](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md) |
| 对偶离域描述符 DDD（氨基苯） | 主功能22（CDFT）→ 选项11（DDD）→ 选项2（Hirshfeld 求 AOM） | .fch | 输出 DDD 框架下各量；g⁻ 为原文两倍才是正确值 | [4.22](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md) |
| 闭壳层 ETS-NOCV 分析（CO–BH₃） | 主功能23（ETS-NOCV）→ 选项2（两片段）→ 后处理 -2 生成 Fock/KS 矩阵求 NOCV 能量 | 配合物＋片段 .fch（片段用 nosymm、几何与配合物一致） | 选项2/1分别看 NOCV 对/轨道等值面；选项14算组成；选项3–5看 Pauli/轨道/总形变密度 | [4.23](sec-4-23-examples-of-ets-nocv-analysis.md) |
| 开壳层 ETS-NOCV（乙烷 2×CH₃、乙烯 2×CH₂） | 主功能23（ETS-NOCV）→ 选项2 → n/y 翻转其中一片段自旋 |  whole＋两自由基/卡宾 .fch | 乙烯中两 CH₂ 取三重态且自旋相反；α/β 各有一主导 NOCV 对 | [4.23](sec-4-23-examples-of-ets-nocv-analysis.md) |
| 弱相互作用 ETS-NOCV（A–T 碱基对） | 主功能23（ETS-NOCV）→ 选项2（两片段） | 碱基对＋单体波函数文件 | 氢键对应的 NOCV 对能量小但本征值可观 | [4.23](sec-4-23-examples-of-ets-nocv-analysis.md) |
| 过渡金属配位与多片段 TS 的 ETS-NOCV（(CO)₅Cr=CH₂、乙炔三聚 TS） | 主功能23（ETS-NOCV）→ 选项2（两片段）/多片段选项 | 配合物/TS＋片段波函数文件 | 乙炔间 π 相互作用仅 −1.85 kcal/mol，可忽略 | [4.23](sec-4-23-examples-of-ets-nocv-analysis.md) |
| 解析 Gaussian polar 任务：静态（超）极化率（NH₃） | 主功能24（超极化率）→ 选项1（解析 polar）→ 选项1开始 | Gaussian polar 输出 .out（大基组＋足量弥散函数） | 直接给出 α/β 张量、各向同性平均、各向异性、β∥ 等（已校正 G09/G16 符号） | [4.24](sec-4-24-examples-of-hyperpolarizability-analyses.md) |
| 解析频率相关（超）极化率与 HRS（NH₃） | 主功能24（超极化率）→ 选项1 → 选项-1（载入动态数据）→ 选频率/β 类型 | Gaussian polar=DCSHG 输出 .out | 选项2 β(−2ω;ω,ω) 另给 HRS 强度、退偏比、J=1/3 分量；可导出 HRS 偏振角曲线 | [4.24](sec-4-24-examples-of-hyperpolarizability-analyses.md) |
| 解析第二超极化率 γ（NH₃） | 主功能24（超极化率）→ 选项1 → 选项-1 → 选项7（解析 α＋γ）→ 选波长 | Gaussian polar=gamma 输出 .out | 输出 γ 张量分量与多种平均定义 | [4.24](sec-4-24-examples-of-hyperpolarizability-analyses.md) |
| SOS 方法计算（超）极化率（NH₃/CIS 150 态） | 主功能18 → 选项5 → 选项3（由 .fch＋.out 生成 SOS.txt）→ 主功能24 → 选项2（SOS）→ 选项1/2/3算 α/β/γ | CIS/TDHF/TDDFT 的 .fch＋.out（IOp(9/40=5)，150 态） | 选项6/5/7检验 α/β/γ 随态数收敛；选项15/16/17/19扫频率 | [4.24](sec-4-24-examples-of-hyperpolarizability-analyses.md) |
| β 的二/三能级模型分析（NH₂-biphenyl-NO₂） | SOS.txt → 主功能24 → 选项2 → 选项20（二/三能级分析） | SOS.txt | 要求仅一个 β 分量主导且一/两个激发态贡献主导 | [4.24](sec-4-24-examples-of-hyperpolarizability-analyses.md) |
| （超）极化率密度分析（H₂CO 的 γ 密度） | 主功能24（超极化率）→ 选项3（极化率密度）→ 选阶数与方向 | 几何文件＋polar 输出 | 输出密度 cube 并作平面图/等值面，分解空间贡献 | [4.24](sec-4-24-examples-of-hyperpolarizability-analyses.md) |
| 单位球表示（超）极化率（CH₃NHCHO、C₁₈） | 主功能24（超极化率）→ 选项1 → 选项-1 → 选项-4（导出 .txt）→ 单位球表示模块 | Gaussian polar 输出 .out | 以三向双箭头矢量直观比较各向响应大小 | [4.24](sec-4-24-examples-of-hyperpolarizability-analyses.md) |
| ICSS/ICSS_ZZ 与磁屏蔽分布（苯） | 主功能25（离域/芳香性）→ 选项3（ICSS 格点）→ Gaussian 跑 NICS 系列 .gjf → 载入 NICS*.out → 选项5（ZZ 分量） | 模板 .gjf（如 benzene.gjf） | 等值面/平面图（主功能4＋cube）/曲线图（主功能3）均可由 ICSSZZ.cub 插值得到；NICS(1)_ZZ=−ICSS 值 | [4.25](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md) |
| HOMA 与 Bird 芳香性指数（菲） | 主功能25（离域/芳香性）→ 选项6（HOMA/Bird）→ 选项0开始 → 输入成环原子序号 | 含坐标文件（.pdb/.xyz/.wfn/.fch 均可） | 按连接顺序输入环原子；HOMA 越近 1、Bird 越近 100 芳香性越强 | [4.25](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md) |
| NICS-1D 曲线、INICS 积分与 FiPC-NICS（infinitene、苯 σ/π 分辨） | 主功能25（离域/芳香性）→ 选项13（NICS-1D/INICS/FiPC-NICS）→ 定义扫描线 → Gaussian 跑 NICS_1D.gjf → 选项2载入输出 | 结构文件（.pdb） | 选项1绘曲线并给积分；选项5找极值；π 分辨用 nmr=csgt＋iop(10/93=2) 模板 | [4.25](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md) |
| NICS-2D 平面图（coronene、N(phenyl)₃） | 主功能25（离域/芳香性）→ 选项14（NICS-2D）→ 选项1填色图 | 结构文件（.pdb） | 比三维 ICSS 便宜得多；只关心平面/曲线时优先用选项13/14 | [4.25](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md) |
