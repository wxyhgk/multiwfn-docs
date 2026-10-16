# 主功能17：盆分析

功能概述：Basin（盆）指实空间函数由零通量面分隔、每个只含一个吸引子的子空间，最典型的是 AIM 原子空间和 ELF basin。Multiwfn 用基于格点的 near-grid 方法（默认带边界精修）生成 basin 并定位吸引子，适用于电子密度、ELF、LOL、静电势等任何实空间函数，也可直接用第三方 cube/.grd 格点。生成 basin 后可做积分、电多极矩、定域化/离域化指数、重叠矩阵计算，并可导出 basin cube 与吸引子文件。AIM basin 的高精度积分与多极矩务必改用混合格点选项 7/8。

## 生成 basin 并定位吸引子（选项1）

说明：选择实空间函数与格点设置，Multiwfn 计算格点数据后生成 basin 并定位吸引子；值相近且位置靠近的吸引子会被自动聚类（聚类参数由选项-6 控制）。内存中已有格点（输入文件自带 .cub/.grd，或之前用主功能5/13 算好）时可直接使用。

菜单路径：主功能17（Basin 分析）→ 选项1（选项-1 选算法/极值，选项-6 调聚类参数）

输入要求：波函数文件，或含目标实空间函数的 .cub/.grd 格点文件（或主功能5/13 预先算好的内存格点）。

操作步骤（原始格式，HCN 的 AIM basin 例）：

```text
examples\HCN.wfn
17  // Basin analysis
1  // Generate basins and locate attractors
1  // The grid data to be calculated and thus analyzed is for electron density
2  // Medium-quality grid. This is enough for most cases, if you want to obtain a better result, you can choose "High-quality grid", but much more computational time will be spent
```

Multiwfn 计算电子密度格点、生成 basin 并寻找吸引子后显示吸引子信息：

```text
Attractor       X,Y,Z coordinate (Angstrom)                Value
    1   -0.02645886   -0.02645886   -1.52058663          0.33959944
    2    0.02645886    0.02645886   -0.51514986         49.48609717
    3   -0.02645886   -0.02645886    0.64904009         76.55832377
```

研究整个体系的 basin，定性分析用“中等质量格点”，定量用“高质量格点”；只研究局域区域时用 "Input center coordinate, grid spacing and box length" 自定义范围。想定位极小值（如 RDG/IRI 极小）时，在选项-1 中切换定位对象，或把 settings.ini 中 "ibasinlocmin" 设为 1。

产出：各 basin 与吸引子（坐标＋函数值）；未归属格点数与跑到盒子边界的格点数（一般应为零）。

来源：[3.20.3](sec-3-20-basin-analysis.md#3203-用法)、[4.17.1](sec-4-17-basin-analysis.md#4171-hcn-和-li₆-的-aim-流域分析)

## 可视化吸引子与 basin（选项0）

说明：在 GUI 中显示吸引子球与 basin 等值面；默认只显示 basin 边界格点，勾选 "Show basin interior" 显示整个 basin；"Set basin drawing method" - "rho>0.001 region only" 只显示 ρ>0.001 区域。浅绿色球为（正值区）吸引子，浅蓝色球为负值区的排斥子。

菜单路径：主功能17 → 选项0

输入要求：已生成 basin。

操作步骤（原始格式）：选择选项 0 可视化 basin 和吸引子。紫色标号表示吸引子编号；电子密度吸引子非常靠近原子核，先取消勾选 "Show molecule" 复选框再看。在右下角 basin 列表中选择编号即显示对应 basin。命令行窗口一般应显示：

```text
The number of unassigned grids:           0
The number of grids travelled to box boundary:           0
```

看完点击 "RETURN" 按钮关闭 GUI。用选项1定位吸引子后，主功能5/13 的等值面 GUI 中也能看到吸引子标签，便于对比。

产出：GUI 中的 basin 等值面与吸引子球显示。

来源：[3.20.3](sec-3-20-basin-analysis.md#3203-用法)、[4.17.1](sec-4-17-basin-analysis.md#4171-hcn-和-li₆-的-aim-流域分析)

## basin 内积分实空间函数（选项2；AIM 高精度用选项7）

说明：选项2在已生成的 basin 中积分所选实空间函数（可选内存格点或外部 .cub/.grd，但格点设置必须与生成 basin 时严格一致）。若分析的是 AIM basin，强烈推荐改用选项7（原子中心＋均匀混合格点），精度远好于选项2；选项7的子选项 (2)/(3) 还做边界精修（近似/精确），做过一次后归属被永久更新。

菜单路径：主功能17 → 选项2（AIM 高精度改用选项7）

输入要求：GTF 波函数，或与生成 basin 格点设置严格一致的 .cub/.grd/内存格点。

操作步骤（原始格式，HCN 例）：选功能 2，再选选项 0（使用内存中已存的电子密度格点），积分立刻输出：

```text
  #Basin        Integral(a.u.)      Volume(a.u.^3)
      1          0.7356142812        441.70000000
      2          5.3511723358        566.84900000
      3          7.9020047534        829.72600000
Sum of above values:         13.98879137
```

总和 13.98879 明显偏离 14 个电子，改用功能 7：

```text
7  // Integrate real space functions in AIM basins with mixed type of grids
1  // Integrate a specific function with atomic-center + uniform grids
1  // Select electron density as the integrand
```

结果为：

```text
   #Basin        Integral(a.u.)      Vol(Bohr^3)    Vol(rho>0.001)
       1          0.7356461300         441.710          34.884
       2          5.3552275427         566.347         102.832
       3          7.9086499057         830.218         134.228
 Sum of above integrals:         13.99952358
 Sum of basin volumes (rho>0.001):     271.944 Bohr^3
```

同时输出归一化后的 AIM 电荷与原子体积。要更准确，在功能 7 中选选项 2（精确边界精修）或 3（近似边界精修）。获得可靠 AIM 电荷的常用步骤是：

```text
1  // Generate basin
1  // Electron density
2  // Medium-quality grid. Select high-quality grid if you wish to get more accurate result
7  // Integrate real space functions in AIM basins with mixed type of grids
2  // Integrate and meantime refine basin boundary
1  // Electron density
```

在 Multiwfn 中算 AIM 电荷最方便的方法是直接选主功能 7 的子功能 14，它自动完成上述步骤。

产出：每个 basin 的积分与体积；选项7额外输出 AIM 电荷、归一化因子与 ρ>0.001 体积（原子尺寸）。

来源：[3.20.3](sec-3-20-basin-analysis.md#3203-用法)、[4.17.1](sec-4-17-basin-analysis.md#4171-hcn-和-li₆-的-aim-流域分析)

## basin 电多极矩与 <r²>（选项3；AIM 高精度用选项8）

说明：计算各 basin 的电多极矩（以吸引子为原点，输出到四极矩）与电子空间范围 <r²>。AIM basin 强烈推荐改用选项8（混合格点，精度更好且无明显额外代价），可同时写入 multipole.txt（并附 atom_moment.txt，可用脚本在 VMD 中可视化）。

菜单路径：主功能17 → 选项3（AIM 高精度改用选项8）

输入要求：GTF 波函数。

操作步骤（原始格式）：进入功能 8，用混合格点计算 AIM basin 的电多极矩（也可用功能 3 基于均匀格点做，但精度明显更差）。计算后询问是否把结果写入 *multipole.txt*，若选 y，当前文件夹下还会产生 *atom_moment.txt*。

产出：各 basin 的单极（电荷）、偶极、四极矩及 <r²>；multipole.txt 与 atom_moment.txt（选项8 选 y 时）。

来源：[3.20.3](sec-3-20-basin-analysis.md#3203-用法)、[4.17.1](sec-4-17-basin-analysis.md#4171-hcn-和-li₆-的-aim-流域分析)

## basin 定域化/离域化指数（选项4）

说明：计算 basin 的定域化指数 LI 与 basin 间的离域化指数 DI（DI 可视为共价键级），理论同模糊空间 LI/DI，积分域换为 basin。该选项涉及 basin 重叠矩阵（BOM）；若用电子密度定义 basin，一般应选混合型格点算 BOM。

菜单路径：主功能17 → 选项4（BOM 积分格点一般选混合型）

输入要求：GTF 波函数。

操作步骤（原始格式）：进入选项 4，按提示选择计算 BOM 所用的积分格点类型（AIM basin 选混合型），再按屏幕提示完成 LI/DI 计算。

产出：各 basin 的 LI 与 basin 对之间的 DI 矩阵。

来源：[3.20.3](sec-3-20-basin-analysis.md#3203-用法)、[4.17.1](sec-4-17-basin-analysis.md#4171-hcn-和-li₆-的-aim-流域分析)

## 输出 basin/原子重叠矩阵（选项5/6）

说明：选项5计算所有 basin 的轨道重叠矩阵（BOM）并写 BOM.txt；选项6（仅电子密度定义 basin 时可见）计算原子重叠矩阵（AOM）并写 AOM.txt（跳过非核吸引子 basin）。BOM 的 (i,j) 元定义为 $S_{ij}\left(K\right)=\int_{\Omega_K}\varphi_i\left(\mathbf{r}\right)\varphi_j\left(\mathbf{r}\right)\mathrm{d}\mathbf{r}$，只考虑占据轨道。

菜单路径：主功能17 → 选项5 / 选项6（6 仅电子密度定 basin 时可见）

输入要求：GTF 波函数。

操作步骤（原始格式）：选选项 5，BOM 输出到当前文件夹下的 *BOM.txt*；选选项 6，AOM 输出到当前文件夹下的 *AOM.txt*。

产出：当前文件夹下的 *BOM.txt*（选项5）、*AOM.txt*（选项6）。

来源：[3.20.3](sec-3-20-basin-analysis.md#3203-用法)

## 导出 basin 与吸引子（选项-5/-4/-45/-3/-2）

说明：-5 导出 basin cube；-4 导出吸引子为 pdb/pqr/txt/gjf；-45 存档 basinana.txt＋basinana.cub 以便下次直接载入复用；-3 查看吸引子坐标数值；-2 测量吸引子/原子间距离夹角二面角。

菜单路径：主功能17 → 选项-5 / -4 / -45 / -3 / -2

输入要求：已生成 basin。

操作步骤（原始格式）：

- **-5 把 basin 导出为 cube 文件**：输入 basin 编号，所选 basin 输出到 *basinXXXX.cub*（XXXX 为 basin 编号），可用 VMD 以等值 0.5 渲染；输入 `a` 则所有 basin 集体导出到 *basin.cub*（格点值＝所属 basin 编号）；输入 `b` 进入特殊模式，用于在 VMD 中绘制 ELF/LOL 按 basin 类型着色的等值面图；输入 `c` 再输 basin 编号，把该 basin 区域内函数值的格点数据导出到 *basinsel.cub*。
- **-4 把吸引子导出为 pdb/pqr/txt/gjf 文件**：*attractors.pdb*（原子编号＝聚类前编号，残基编号＝聚类后编号）、*attractors.pqr*（charge 列＝吸引子处函数值）、*attractors.txt*（每行 X/Y/Z 坐标 Bohr＋函数值）、*attractors.gjf*（真实原子高层＋Bq 幽灵原子中层，可载入 GaussView；在 Preference-Display Format-Molecule 中把低层设 Tube 并关闭原子标签）。
- **-45 导出吸引子信息和当前格点数据**：写出 *basinana.txt*（吸引子＋basin 信息）与 *basinana.cub*（当前格点数据）；下次做相同分析选选项1时若发现这两个文件，选 y 即直接载入，避免重新生成。
- **-3 显示吸引子信息**：输出所有吸引子坐标数值（简并吸引子显示平均值及各成员值），并询问是否按值从最负到最正排序打印。
- **-2 测量吸引子或原子之间的距离、夹角和二面角**：按屏幕提示操作。

产出：basinXXXX.cub / basin.cub / basinsel.cub；attractors.pdb/.pqr/.txt/.gjf；basinana.txt＋basinana.cub；屏幕上的吸引子信息与几何测量值。

来源：[3.20.3](sec-3-20-basin-analysis.md#3203-用法)、[4.17.10](sec-4-17-basin-analysis.md#41710-绘制按流域类型着色的-elf-等值面图)

## ELF 专项与外部 basin 分析（选项12/10/9/11）

说明：选项12自动指定 ELF basin 标签（芯/价，如 C(C1)、V(C1,C3)、V(C1,H2)）并打印布居体积；选项10算 HELP/HELV 表征孤对；选项9基于外部 basin.cub 求 ELF 键 basin 布居的 AIM 原子贡献；选项11算各 basin 对指定轨道组成的贡献。

菜单路径：主功能17 → 选项12 / 选项10 / 选项9 / 选项11（12/10 仅 ELF basin 时出现，9 需当前目录有 basin.cub）

输入要求：ELF basin（12/10），或外部 basin.cub（9）；GTF 波函数。

操作步骤（原始格式，乙炔 ELF 例）：对 ELF 生成 basin 后选选项 12，自动指定标签并输出布居体积，例如：

```text
#    1  Basin    4  Pop.:  2.0949  Vol.:    0.123  Label: C(C1)
#    2  Basin    3  Pop.:  2.0949  Vol.:    0.123  Label: C(C3)
#    3  Basin    5  Pop.:  2.2160  Vol.:  113.884  Label: V(C1,H2)
#    4  Basin    2  Pop.:  5.3670  Vol.:  144.158  Label: V(C1,C3)
#    5  Basin    1  Pop.:  2.2160  Vol.:  113.865  Label: V(C3,H4)
```

标签输出两次：先按 basin 编号，再按排序后的标签。选项10（HELP/HELV）、选项9（外部 basin 的 AIM 原子贡献）、选项11（basin 对轨道组成的贡献）按屏幕提示操作；选项11 的例子见轨道组成分析（AIM/ELF 盆贡献的轨道组成）。

产出：ELF basin 标签＋布居＋体积；HELP/HELV；外部 basin 的原子贡献；指定轨道的各 basin 组成（选项11 可用 -9 定义原子组输出片段贡献，-4 导出全部至 orbcomp.txt）。

来源：[3.20.3](sec-3-20-basin-analysis.md#3203-用法)、[4.17.2](sec-4-17-basin-analysis.md#4172-elf-流域分析例子)、[4.17.7](sec-4-17-basin-analysis.md#4177-计算-elf-流域布居数的原子贡献)、[4.17.8](sec-4-17-basin-analysis.md#4178-计算高-elf-定域域布居数和体积-helphelv)
