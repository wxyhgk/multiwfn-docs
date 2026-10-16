# Multiwfn 应用导览（按实验问题组织）

> 不知道用哪个功能？先找你的问题。每场景：能解决什么 → 用哪些主功能 → 典型流程 → 延伸阅读。

> 另见：[菜单操作路径总表](MENU_INDEX.md)（按编号查）、[分功能详表](menu/func-00.md)（从主功能0开始顺查）、[术语表](GLOSSARY.md)。

## 一、看结构、量几何、算电荷

> 按实验人员的问题组织。每场景先一句话说明解决什么问题，再给任务→功能映射表、典型流程（菜单数字原样）、延伸阅读（只链文件，不写锚点）。

## 场景一：轨道与分子结构可视化

一句话：想"看见"分子长什么样、某个轨道长什么样、一次批量导出大量轨道图时，看这里。

| 任务 | 用哪个主功能 | 关键选项 |
|---|---|---|
| 看分子结构、旋转缩放、切换显示风格 | [主功能 0](menu/func-00.md) | 右侧视角按钮 / `Set view` / `Other settings`（CPK、vdW、线型风格）/ `Bonding threshold` 调成键判据 |
| 看单个分子轨道等值面 | [主功能 0](menu/func-00.md) | 右下角轨道列表选序号或直接输编号；开壳层负序号选 beta 轨道（如 `-5`）；`h`、`l+2`、`la`、`hb-3` 快捷选轨 |
| 提高轨道图质量、显示弥散轨道、看概率密度 | [主功能 0](menu/func-00.md) | `Isosur. quality` 提质量；`Other settings` → `Set extension distance`（如 `12`，单位 Bohr）；`Choose plotting wavefunction or density` → `Density` |
| 同屏叠加两个轨道（如 NBO 孤对与反键轨道的重叠） | [主功能 0](menu/func-00.md) | 先选轨道 #1 → 勾选 `Show+Sel. Isosur#2` → 再选轨道 #2；`Isosur#1 style` / `Isosur#2 style` 切网格或透明面 |
| 看 NBO / NHO / NAO | [主功能 0](menu/func-00.md) | 载入 `.31`+`.37` plot 文件，或载入含 `saveNBO` 的 `.fch` 后直接选号查看 |
| 测键长、键角、二面角；找片段；查某元素原子序号；导出坐标 | [主功能 0](menu/func-00.md) | `Tools` → `Measure geometry`（输 2/3/4 个原子序号）/ `Select fragment` / `Get atom indices of a given element` / `Print XYZ coordinates` / `Export all internal coordinates`（无 GUI 版输 `geomparm`） |
| 批量绘制大量轨道图 | [主功能 0](menu/func-00.md) | `Tools` → `Batch plotting orbitals`，每个轨道存一张图 |
| 出版级轨道图（Multiwfn + VMD + Tachyon） | [主功能 0](menu/func-00.md) | `showorb.bat` + `showorb.txt`（第三行设轨道范围如 `54-59`）算格点 → VMD `orb` / `orbiso` → `VMDrender.txt` + Tachyon 渲染 |

典型流程（看单个轨道并调质量）：

1. 启动 Multiwfn，载入含轨道信息的文件（如 `examples\cycloheptatriene.fch`）。
2. 主菜单输 `0`，进入 GUI。
3. 在右下角轨道列表选序号，或在文本框输入编号后回车（beta 轨道输负号）。
4. 绿色/蓝色分别为正值/负值部分；拖等值面值滑条或经 `Other settings` → `Set isovalue` 改等值面值。
5. 经 `Isosur. quality` 提高质量；Rydberg 等弥散轨道经 `Other settings` → `Set extension distance` 输入 `12`。
6. 需要概率密度时经 `Other settings` → `Choose plotting wavefunction or density` → `Density`。
7. 需要同屏看两个轨道时：选好 #1 后勾选 `Show+Sel. Isosur#2`，再选 #2。

延伸阅读：

- sec-3-2-showing-molecular-structure.md
- sec-4-0-view-orbitals-and-structure.md

## 场景二：几何结构表征

一句话：只用原子坐标回答"分子有多大、多扁、有没有洞、离得有多远"时，看这里。

| 任务 | 用哪个主功能 | 关键选项 |
|---|---|---|
| 算分子范德华体积 | [主功能 100](menu/func-100.md) | 子功能 `3`；`settings.ini` 的 `MCvolmethod` 选区域定义（vdW 球叠加 / 电子密度等值面）；输入指数 `i` 定点数（`N=100×2^i`），密度定义另输等值面值与盒子因子 `k` |
| 算质心、回转半径、惯量张量、转动常数、核电荷静电能 | [主功能 100](menu/func-100.md) | 子功能 `21`，输入原子范围或 `all` |
| 算分子直径、长宽高、包围盒 | [主功能 100](menu/func-100.md) | 子功能 `21`，输 `size`（按 Bondi vdW 半径）；选项 1 图形化包围盒，选项 2 导出 `new.pdb` |
| 算两片段间距（最小/最大距离、中心间距） | [主功能 100](menu/func-100.md) | 子功能 `21`，输 `dist` 后定义两片段 |
| 算环面积与周长 | [主功能 100](menu/func-100.md) | 子功能 `21`，输 `ring` 后按顺时针输环原子序号 |
| 定量分子平面性 | [主功能 100](menu/func-100.md) | 子功能 `21`，输 `MPP`（主菜单直接输 `MPP` 也可），输出 MPP/SDP 与拟合平面，可导出 `.pqr` 用 VMD 着色；多帧 `.xyz` 得 `MPP_SDP.txt` |
| 算分子空腔直径与体积 | [主功能 100](menu/func-100.md) | 子功能 `21`，输 `cav`，选周围原子 + 球心初位（常用几何中心），自动迭代使球最大 |
| 判成键、算配位数 | [主功能 100](menu/func-100.md) | 子功能 `9`，输出原子对连接性指数与每原子连接性和，可导 `connmat.txt` |
| 团簇平均键长与平均配位数 | [主功能 200](menu/func-200.md) | 子功能 `9`，输入两种元素（如 `Ge,Au`）与距离截断（如 `3.2`） |

典型流程（算分子直径与长宽高）：

1. 启动 Multiwfn，载入结构文件（如 `examples/alpha-cyclodextrin.pdb`，仅需坐标）。
2. 主菜单输 `100`，进其他功能第 1 部分。
3. 输 `21`，进几何性质功能。
4. 输 `size`，计算分子直径与长宽高。
5. 读输出：最远原子对距离、直径、半径、三边长。
6. 选项 `1` 图形化包围盒；选项 `2` 导出旋转平移后的 `new.pdb`（VMD 用 `pbc box` 显示）。

典型流程（算空腔直径，以开口富勒烯为例）：

1. 载入 `open_fullerene.pdb`。
2. 主菜单直接输 `cav`（或经 `100` → `21` → `cav`）。
3. 输入包围空腔的原子（如 `1,12-20,23-67,101`）。
4. 选 `1`，用所输原子的几何中心作球心初位。
5. 选 `1`，允许自动调整球心使球最大。
6. 读输出：球心坐标、半径、直径、体积；把给出的 VMD `draw sphere` 命令粘到 VMD 控制台验证。

延伸阅读：

- sec-3-100-other-functions-part-1.md
- sec-4-100-other-functions-part-1.md
- sec-3-200-other-functions-part-2.md

## 场景三：原子电荷与布居分析

一句话：想给每个原子定"带了多少电"、比较不同电荷模型的含义和用法、检验电荷好坏时，看这里。

| 任务 | 用哪个主功能 | 关键选项 |
|---|---|---|
| 快速得到化学合理、电荷值适中、偶极复现好的电荷（日常首选） | [主功能 7](menu/func-07.md) | 选项 `11`（ADCH）；选项 `1`（内建球化自由原子密度） |
| 要最经典、与电负性直觉一致的实空间电荷 | [主功能 7](menu/func-07.md) | 选项 `1`（Hirshfeld）；电荷总和偏离整数时调大 `settings.ini` 的 `radpot`/`sphpot`；用归一化后的 Final 电荷发表 |
| 要拟合分子表面静电势、做力场/对接的电荷 | [主功能 7](menu/func-07.md) | 选项 `12`（CHELPG，选项 `1` 开始拟合）/ 选项 `13`（MK）/ 选项 `18`（RESP，选项 `1` 两步标准 RESP、选项 `2` 一步拟合、选项 `-1` 多构象） |
| 要与实验/高精度偶极一致、不依赖当前计算水平的电荷 | [主功能 7](menu/func-07.md) | 选项 `16`（CM5）/ `-16`（1.2×CM5，供 OPLS-AA 的 MD） |
| 要 AIM（Bader）盆定义的电荷 | [主功能 7](menu/func-07.md) | 选项 `14`，选格点质量（`2` 为性价比折中）后自动积分 |
| 要迭代优化原子空间的大电荷值（HI / MBIS 系） | [主功能 7](menu/func-07.md) | 选项 `15`（Hirshfeld-I，需 `.rad` 文件，`examples/atmrad` 可直接用）/ 选项 `20`（MBIS，选项 `1` 开始迭代）/ `21`、`22`、`23`（cMBIS/EMBIS/AEMBIS） |
| 要最老的轨道布居数（基函数/壳层/原子分解） | [主功能 7](menu/func-07.md) | 选项 `5` → 子功能 `1`–`4`；禁带弥散函数；大体系先用 `-1` 重定向输出到文件 |
| 只要基组稳定性稍好的轨道布居变体 | [主功能 7](menu/func-07.md) | 选项 `6`（Löwdin）/ `7`（SCPA）/ `8`（Stout-Politzer）/ `9`（Bickelhaupt） |
| 大体系秒出粗估电荷 | [主功能 7](menu/func-07.md) | 选项 `17`（EEM，需 `.mol`/`.mol2`，离子先用选项 `2` 设净电荷）/ 选项 `19`（PEOE，仅坐标，仅中性有机子集元素） |
| 要某片段总电荷、存电荷文件、算片段间静电作用能 | [主功能 7](menu/func-07.md) | 先选项 `-1` 定义片段；算完选 `y` 存 `.chg`；`.chg` 作输入时选项 `-2` 算库仑作用能 |
| 检验一套电荷复现静电势的能力 | [主功能 7](menu/func-07.md) | 选项 `13`/`12` → `-3` 载入待检 `.chg` → `1`，只输出 RMSE/RRMSE 不做新拟合 |
| 由电荷算凝聚 Fukui 函数与对偶描述符 | [主功能 7](menu/func-07.md) | N/N+1/N−1 三态各算 Hirshfeld 电荷（选项 `1`），代入 `f+=qN−qN+1`、`f−=qN−1−qN` |

典型流程（算 ADCH 电荷并存文件）：

1. 启动 Multiwfn，载入含 GTF 的文件（如 `examples\CH3CONH2.fch`）。
2. 主菜单输 `7`，进布居分析与原子电荷。
3. 输 `11`，选 ADCH。
4. 输 `1`，用内建自由原子密度。
5. 读汇总栏：corrected 列为 ADCH 电荷，before 列为 Hirshfeld 电荷；用归一化后的 Final 电荷发表。
6. 按提示选 `y`，把坐标与电荷存为 `.chg`（供画原子电荷 ESP 或算片段作用能用）。

典型流程（检验一套电荷的 ESP 再现性）：

1. 先按常规流程算出电荷并存 `.chg`（如 Hirshfeld 电荷）。
2. 主功能 `7` → `13`（MK）→ `-3`，载入待检 `.chg`。
3. 选 `1` 开始计算（不产生新拟合电荷，只输出 RMSE/RRMSE）。
4. 比较 RRMSE：越小复现越好（如乙酰胺例 Hirshfeld 约 0.31，MK 约 0.05，ADCH 约 0.21）。
5. 需要看空间分布时用选项 `6` 导出 `ESPfitpt.pqr` / `ESPerr.pqr`，用 VMD 按 Charge 着色。

延伸阅读：

- sec-3-9-population-analysis-and-calculation-of-atomic-charges.md
- sec-4-7-population-analysis-and-atomic-charge-calculation.md

## 二、表征化学键、芳香性与表面

> 面向实验人员的问题组织：每个场景先说解决什么问题，再给"用哪个主功能、按什么菜单走、看什么关键选项"。
> 链接约定：menu 用 `menu/func-NN.md` 相对路径；sec 用裸文件名链接；不写锚点。

---

## 场景 B1：化学键表征（这根键是什么键、有多强、电子局域在哪里）

一句话：判断成键类型与强度、定位键临界点与电子局域区、把离域正则轨道转成"化学键/孤对"图像。

| 任务 | 用哪个主功能（链 menu/func-NN.md） | 关键选项 |
|---|---|---|
| AIM 拓扑找键临界点 BCP、生成键径、查 BCP 处性质 | [主功能 2 拓扑分析](menu/func-02.md) | `2→2/3→0` 搜 CP 并校验 Poincaré-Hopf；`8` 生成键径；`7` 查 CP 处函数值；`-11` 切换被分析函数；ELF/LOL/拉普拉斯用模式 `6→-1` 多撒点重搜 |
| 画 ELF / LOL / 拉普拉斯 / 变形密度平面图与等值面 | [主功能 4 平面图](menu/func-04.md)、[主功能 5 空间格点](menu/func-05.md) | 主功能 4 选函数→选图类别→设格点→8 种平面定义；主功能 5 生成 cube 后 `-1` 看等值面 / `2` 导出 .cub；变形密度经自定义操作 `-2` 得到 |
| 定量键级：Mayer / FBO / LBO / Wiberg | [主功能 9 键级分析](menu/func-09.md) | `1` Mayer（禁弥散）；`7` FBO（弥散稳健）；`8` LBO（共价强度，与 BDE 相关）；`3` Löwdin-Wiberg；`4/5` Mulliken 键级及轨道分解；`6` 占据微扰 Mayer 找关键轨道 |
| 键强度：IBSI（尤其弱作用与配位键定级） | [主功能 9 键级分析](menu/func-09.md) | `10→0` 计算；`2` 选 IGM-pro/IGMH/mIGM（默认 IGM-pro，只需坐标；IGMH 需波函数）；`5` 设打印距离阈值 |
| 离域指数 DI / 定域指数 LI（模糊空间或 AIM 盆） | [主功能 15 模糊原子空间](menu/func-15.md)、[主功能 17 盆分析](menu/func-17.md) | 主功能 15→`4/44`（DI 即模糊键级）；主功能 9→`12` 为 AIM 盆间 DI 快捷入口；主功能 17→`4` 为 basin 版 LI/DI |
| ELF 盆划分：孤对/成键盆布居与体积 | [主功能 17 盆分析](menu/func-17.md) | `1` 生成 basin；`12` 自动标 ELF 芯/价标签；HELP/HELV 表征孤对 |
| 定域化轨道 LMO：把 CMO 转成 σ/π 键与孤对 | [主功能 19 轨道定域化](menu/func-19.md) | `1` 只定域占据轨道（默认 PM-Mulliken，`-6` 可换 PM-Becke/FB；弥散多时不用默认法）；结果写 new.fch，用主功能 0 看等值面、主功能 8 看组成 |
| 键极性 BPI / 能量指数、CVB 氢键指数 | [主功能 200 其他功能 2](menu/func-200.md) | `12` 算 EI/BPI（禁弥散）；`1` 算 CVB（输入给体/氢/受体序号） |

典型流程（AIM + 键级 + LMO 联用，HF/DFT 波函数如 .fch/.molden）：

1. 载入波函数 → 主功能 `2` → `2`（核位置找极大）→ `3`（原子对中点找 BCP）。
2. `0` 可视化并核对 Poincaré-Hopf 关系；缺 BCP 时经 `-1` 调步长/算法重搜。
3. `8` 生成键径（分子图）；`7` 查目标 BCP 处 ρ、∇²ρ、能量密度。
4. 回主菜单 → 主功能 `9` → `1` 算 Mayer 键级；有弥散函数改 `7` 算 FBO；要共价强度再算 `8` LBO。
5. 对关键键做 `5`（Mulliken 分解）或 `6`（占据微扰）定位成键/反键轨道。
6. 主功能 `4` 画该键平面的 ELF/LOL/∇²ρ 填充色图，或主功能 `5` 生成 cube 看等值面。
7. 主功能 `19` → `1` 定域占据轨道 → new.fch 自动载入 → 主功能 `0` 观察 σ/π 键与孤对 LMO。
8. （可选）主功能 `17` → `1` 生成 ELF basin → `12` 标定并积分孤对盆布居。

延伸阅读：[sec-4-2-topology-analysis.md](sec-4-2-topology-analysis.md)、[sec-4-9-bond-order-analysis.md](sec-4-9-bond-order-analysis.md)、[sec-4-19-orbital-localization-analysis.md](sec-4-19-orbital-localization-analysis.md)、[sec-4-17-basin-analysis.md](sec-4-17-basin-analysis.md)、[sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md)、[sec-3-14-topology-analysis.md](sec-3-14-topology-analysis.md)、[sec-3-22-orbital-localization-analysis.md](sec-3-22-orbital-localization-analysis.md)、[sec-4-5-generate-grid-data-and-view-isosurface-map.md](sec-4-5-generate-grid-data-and-view-isosurface-map.md)

---

## 场景 B2：芳香性与电子离域（这个环芳香还是反芳香、离域有多强）

一句话：用磁性（NICS/ICSS）、几何（HOMA/Bird）、电子离域（MCBO/PDI/FLU）三类独立判据交叉验证，避免单一指标误判。

| 任务 | 用哪个主功能（链 menu/func-NN.md） | 关键选项 |
|---|---|---|
| NICS/ICSS 三维芳香性图像 | [主功能 25 离域与芳香性](menu/func-25.md) | `3` 生成 ICSS 格点（需 Gaussian NMR 输出；平面体系优先看 ICSS_ZZ）；结果可视化或导出 .cub |
| 非平面/倾斜环 NICS_ZZ | [主功能 25 离域与芳香性](menu/func-25.md) | `4`：输入环中心（RCP 或几何中心）+ 拟合平面原子 + 磁屏蔽张量，法向分量负值即 NICS_ZZ |
| NICS-1D 扫描 / INICS / FiPC-NICS | [主功能 25 离域与芳香性](menu/func-25.md) | `13`：定义扫描线 → 生成 NICS_1D.gjf → Gaussian 跑 NMR → 载入输出选分量绘图/积分 |
| NICS-2D 平面图 | [主功能 25 离域与芳香性](menu/func-25.md) | `14`：定义平面 → 生成 NICS_2D.gjf → 跑 NMR → 载入显示平面图 |
| HOMA / Bird / HOMAc / HOMER 几何指数 | [主功能 25 离域与芳香性](menu/func-25.md) | `6→0` HOMA、`6→2` Bird（只需坐标，按连接顺序输环原子）；`6a/6b` 为 HOMAc（基态）/HOMER（T1 态） |
| 多中心键级 MCBO / MCI | [主功能 9 键级分析](menu/func-09.md) | `2` 标准 / `-2` NAO 基（有弥散必须用）/ `-3` Löwdin 基；按环连接顺序输入；比较归一化值 |
| 大环 AV1245 / AVmin | [主功能 200 其他功能 2](menu/func-200.md) | `19`：按连接顺序输环原子（`d` 可自动推连接）；输出 AV1245、各 4c-ESI 与 AVmin |
| PDI / FLU / FLU-π / PLR / 信息论指数 | [主功能 15 模糊原子空间](menu/func-15.md) | `5` PDI（六元环）、`6/7` FLU/FLU-π（任意元环）、`10` PLR、`12` 信息论指数 |
| Shannon 指数 / RCP 垂直曲率（密度拓扑） | [主功能 2 拓扑分析](menu/func-02.md) | 电子密度拓扑下 `20` Shannon（越小越芳香）、`21` RCP 垂直曲率（越负越芳香） |

典型流程（以菲的边界环 vs 中心环为例）：

1. 优化几何 → 载入坐标文件 → 主功能 `25` → `6` → `0`，按连接顺序输入环原子，得 HOMA（边界环 ~0.86、中心环 ~0.43 即判据之一）。
2. 同界面 `2` 算 Bird 指数交叉验证（越接近 100 越芳香）。
3. 主功能 `9` → `2`，同样按连接顺序输入环原子算 MCBO，比较归一化值。
4. 主功能 `15` → `5/6` 算 PDI/FLU（模糊空间离域指数视角）。
5. 需要磁性判据：主功能 `25` → `13` 做 NICS-1D 扫描（或 `3` 做 ICSS_ZZ），用 Gaussian NMR 输出载入后看 NICS(1)_ZZ / FiPC-NICS。
6. 大环体系改用主功能 `200` → `19` 算 AV1245/AVmin。

延伸阅读：[sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md)、[sec-3-28-electron-delocalization-and-aromaticity-analyses.md](sec-3-28-electron-delocalization-and-aromaticity-analyses.md)、[sec-3-11-bond-order-analysis.md](sec-3-11-bond-order-analysis.md)、[sec-3-18-fuzzy-atomic-space-analysis.md](sec-3-18-fuzzy-atomic-space-analysis.md)、[sec-3-14-topology-analysis.md](sec-3-14-topology-analysis.md)

---

## 场景 B3：分子表面与静电势分析（哪里亲电/亲核、σ-hole 在哪、极性与凝聚相性质）

一句话：在 vdW 表面上定量 ESP（及 ALIE 等）分布，定位极值与 σ-hole/π-hole，由表面描述符预测极性与晶体密度等凝聚相性质。

| 任务 | 用哪个主功能（链 menu/func-NN.md） | 关键选项 |
|---|---|---|
| 常规表面 ESP 定量分析（面积/体积/极值/统计量） | [主功能 12 分子表面定量分析](menu/func-12.md) | `1` 选面（默认 ρ=0.001 vdW 面，凝聚相用 0.002）→ `2` 选映射函数（默认 ESP）→ `0` 启动；`6` 为无映射函数快速版 |
| ALIE / D(r) / Fukui 等映射函数表面分析 | [主功能 12 分子表面定量分析](menu/func-12.md) | `2` 切换映射函数（`2`=ALIE 找亲电位点；`6`=D(r)；Fukui 经 `5` 外部加载三态密度 cube） |
| σ-hole / π-hole 位置、数值与面积 | [主功能 12 分子表面定量分析](menu/func-12.md) | 先 `0` 做 ESP 分析 → 后处理 `14` 选极大点编号 + 判据（如 π-hole 0.04、σ-hole 0.03 a.u.，常取极大值约 60%） |
| 原子局域表面（哪个原子最亲电/亲核） | [主功能 12 分子表面定量分析](menu/func-12.md) | 分析后 → 后处理 `11`（每原子表面性质，可导出 locsurf.pqr）/ `12`（指定片段） |
| 表面类盆分割（化学上有用的 ESP 盆） | [主功能 12 分子表面定量分析](menu/func-12.md) | 后处理 `15`（导出 surfbasin.pdb，B 因子为盆编号） |
| ESP 区间面积统计 / 非键半径与互穿距离 | [主功能 12 分子表面定量分析](menu/func-12.md) | 后处理 `9`（值区间面积统计）/ `10`（表面与指定点最近/最远距离，得 AIM 非键半径） |
| 晶体密度等凝聚相性质预测 | [主功能 12 分子表面定量分析](menu/func-12.md) | `0` 得 M/V 与 νσ²，代入经验式（如 ρ=0.9183(M/V)+0.0028(νσ²)+0.0443，仅适配 B3PW91/6-31G** 的 C/H/N/O 小有机物） |
| Hirshfeld/Becke 表面与指纹图（晶体接触） | [主功能 12 分子表面定量分析](menu/func-12.md) | `1→5/6` 选 Hirshfeld/Becke 面并输片段原子 → `0` 启动 → 后处理 `20` 做指纹图与局域接触分析 |
| ESP 等值面/平面图可视化 | [主功能 5 空间格点](menu/func-05.md)、[主功能 4 平面图](menu/func-04.md) | 主功能 5 生成 ESP cube 看等值面；主功能 4 画 ESP 平面填充色图 |

典型流程（苯酚 ESP + ClPO2 σ-hole，B3PW91/6-31G** 或 def-TZVP 波函数）：

1. 载入 .wfn → 主功能 `12` → `0`（默认 ESP + 0.001 面）启动分析。
2. 查看表面极大/极小位置数值、面积/体积、均值/方差、Π/σ²/ν/MPI。
3. 后处理 `0` 可视化极值点；`9` 按 ESP 区间统计面积分布。
4. 定量 σ-hole：后处理 `14` → 选极大点编号 → 输判据（如 0.03 a.u.）得面积与平均值。
5. 找反应位点：后处理 `11` 看每原子局域表面 ESP 均值（最正处为硬亲核进攻位点）；或重做 `2→2` 切 ALIE 找亲电位点。
6. （可选）后处理 `15` 做类盆分割；`10` 算目标原子的非键半径。
7. 预测晶体密度：取 M/V 与 νσ² 代入对应经验式（注意方法与元素适用范围）。

延伸阅读：[sec-3-15-quantitative-analysis-of-molecular-surface.md](sec-3-15-quantitative-analysis-of-molecular-surface.md)、[sec-4-12-quantitative-analysis-of-molecular-surface.md](sec-4-12-quantitative-analysis-of-molecular-surface.md)、[sec-4-4-output-and-plot-various-properties-in-a-plane.md](sec-4-4-output-and-plot-various-properties-in-a-plane.md)、[sec-4-5-generate-grid-data-and-view-isosurface-map.md](sec-4-5-generate-grid-data-and-view-isosurface-map.md)

## 三、弱相互作用、激发态与反应性

> 按实验人员的问题组织：每节先一句话说明解决什么问题，再给任务→主功能对照表、典型流程（菜单数字原样）、延伸阅读。菜单详表链 `menu/func-NN.md`，sec 链裸文件名，不写锚点。

## 场景 1：弱相互作用在哪里、有多强

一句话：判断氢键、卤键、π–π 堆积、范德华接触的位置、类型与相对强度，并做可视化与定量分解。

| 任务 | 用哪个主功能（链 menu/func-NN.md） | 关键选项 |
|---|---|---|
| 画 NCI（RDG）填色等值面，区分氢键/范德华/位阻 | [主功能 20](menu/func-20.md) | 子功能 1，格点质量 2/3，选项 3 导出 func1.cub、func2.cub，VMD 脚本 RDGfill.vmd |
| 无波函数大体系快速看 NCI | [主功能 20](menu/func-20.md) | 子功能 2（前分子密度），仅需坐标，脚本 RDGfill_pro.vmd |
| 同时看化学键与弱相互作用、效果最清晰 | [主功能 20](menu/func-20.md) | 子功能 4（IRI / IRI-π），等值面取 1.0，选项 9 屏蔽共价区，选项 3 导出 cube |
| 只需几何即可分离片段间/片段内作用并定量原子对贡献 | [主功能 20](menu/func-20.md) | 子功能 10（IGM），先定义两/三片段，选项 6 算 δg 指标与 IBSIW，得 atmdg.txt、IBSIW.txt |
| 有波函数时更严格的 IGM，薄等值面、着色更合理 | [主功能 20](menu/func-20.md) | 子功能 11（IGMH），需 GTF 文件，settings.ini 中 IGMvdwscl 可加速 |
| DORI 同时显示共价与非共价区 | [主功能 20](menu/func-20.md) | 子功能 5，等值面取 0.95，脚本 DORIfill.vmd |
| 动力学轨迹平均弱相互作用 | [主功能 20](menu/func-20.md) | 子功能 3（aNCI，≥500 帧）；更推荐子功能 −12（amIGM） |
| 找范德华势极小点（σ-hole 附近吸附位） | [主功能 20](menu/func-20.md) | 子功能 6，只需坐标；极小点再经主功能 17 盆分析定位 |
| AIM 键径与键临界点证认弱相互作用 | [主功能 2](menu/func-02.md) | 模式 2＋3 搜 CP，选项 0 校验 Poincaré-Hopf，选项 8 生成键径，选项 7 查 BCP 处性质 |
| 片段间静电/排斥/色散能量分解（大体系） | [主功能 21](menu/func-21.md) | 子功能 1（EDA-FF，需电荷＋片段定义）；精确分解用 sobEDA/sobEDAw 外部脚本 |
| 表面 ESP 极值找 σ-hole/孤对电子作用位 | [主功能 12](menu/func-12.md) | 映射函数 ESP，选项 0 启动，选项 14 定量极值点周围面积 |

典型流程（氢键二聚体，NCI＋AIM 双证）：

1. 载入 `xxx.wfn`，进 `20`，选 `1`（NCI 分析）。
2. 选格点质量 `2` 或 `3`（中等/高）。
3. 后处理选 `-1` 看 RDG–sign(λ₂)ρ 散点图，确认尖峰位置。
4. 选 `3` 导出 func1.cub、func2.cub，用 VMD 脚本 `RDGfill.vmd` 画填色等值面（默认等值面 0.5）。
5. 回主菜单进 `2`，依次用 `2`（核位置）＋`3`（原子对中点）搜索临界点。
6. 选 `0` 可视化并校验 Poincaré-Hopf 关系，选 `8` 生成键径，选 `7` 查氢键 BCP 处密度与 Laplacian。
7. 如需能量分解，进 `21` 选 `1` 做 EDA-FF（先备电荷与片段定义）。

典型流程（大体系片段间作用，IGM 定量）：

1. 载入 `.pdb`/`.xyz`，进 `20`，选 `10`（IGM 分析）。
2. 选 `2` 定义两片段，输入原子范围（如 `1-13` 与 `14-29`）。
3. 选合适格点质量计算，选 `-1` 看散点图。
4. 选 `3` 导出 cube，用 `IGM_inter.vmd` 绘图。
5. 选 `6` 计算原子/原子对 δg 指标，得 atmdg.txt 与 IBSIW.txt，定位热点原子。

延伸阅读：sec-3-23-visual-study-of-weak-interaction.md、sec-4-20-visual-study-of-weak-interactions.md、sec-3-14-topology-analysis.md、sec-4-2-topology-analysis.md、sec-3-24-energy-decomposition-analysis.md、sec-4-21-energy-decomposition-analysis.md、sec-3-15-quantitative-analysis-of-molecular-surface.md。

## 场景 2：电子激发是什么类型、电荷往哪转

一句话：判断激发是局域还是电荷转移、可视化空穴–电子去向、定量片段间转移量与跃迁偶极矩来源。

| 任务 | 用哪个主功能（链 menu/func-NN.md） | 关键选项 |
|---|---|---|
| 空穴–电子分布、重叠、Sr/Sm、t/H/D/CT 指标与等值面 | [主功能 18](menu/func-18.md) | 子功能 1；功能 1 可视化，功能 2 看 MO 贡献，功能 3 看原子/片段贡献与热图 |
| 片段间电荷转移量、CT%/LE% | [主功能 18](menu/func-18.md) | 子功能 8（IFCT）；Hirshfeld 划分兼容弥散函数；输 `-1` 导出 atmCTmat.txt |
| 快速判长程 CT（Δr 指数） | [主功能 18](menu/func-18.md) | 子功能 4；大值警示纯泛函可能失效 |
| 判长程 CT（Λ 指数，较贵） | [主功能 18](menu/func-18.md) | 子功能 14；无特殊原因优先用 D/Sr 指数 |
| 画 NTO，一句话说清激发 | [主功能 18](menu/func-18.md) | 子功能 6；导出 .fch/.molden/.mwfn 后再看轨道组成 |
| 跃迁偶极矩分解到 MO 对（解释吸收强弱） | [主功能 18](menu/func-18.md) | 子功能 10，结果可存 transdip.txt |
| 跃迁偶极矩分解到原子/基函数（定位关键原子区） | [主功能 18](menu/func-18.md) | 子功能 11，得 trdipcontri.txt 与 AAtrdip 矩阵 |
| 态间跃迁偶极矩与各态偶极矩（SOS 输入） | [主功能 18](menu/func-18.md) | 子功能 5；选项 3 产生 SOS.txt；大体系选项 -1 跳过激发态之间 |
| 原子跃迁电荷（激子耦合） | [主功能 18](menu/func-18.md) | 子功能 12，得 atmtrchg.chg；更准的 TrEsp 见专题教程 |
| 只用密度差格点算 CT 量（无需组态系数） | [主功能 18](menu/func-18.md) | 子功能 3；Δρ 格点由主功能 5 自定义操作产生 |
| 激发态自然轨道文件（分析态间密度差） | [主功能 18](menu/func-18.md) | 子功能 13，得 NO_XXXX.mwfn |
| ghost 态排查 | [主功能 18](menu/func-18.md) | 子功能 7（MAC 指数）；判据偏严，仅作必要条件 |

典型流程（TDDFT 激发定性＋定量）：

1. 准备参考轨道文件（`.fch`/`.molden`）与组态系数文件（Gaussian 加 IOp(9/40=4)，ORCA 用 TPrint 1E-8）。
2. 进 `18`，选 `1` 做空穴–电子分析，设格点，检查空穴/电子全空间积分是否接近 1.0。
3. 功能 2 看 MO 贡献，功能 3 看原子/片段贡献并绘热图；导出 cube 画空穴–电子等值面。
4. 退回选 `8` 做 IFCT：选划分方法，选激发态编号，定义片段，得片段间转移矩阵与 CT%/LE%。
5. 选 `4` 算 Δr 指数佐证 CT 长度；需要时选 `6` 产生 NTO 并导出文件。
6. 解释强度时选 `10` 分解跃迁偶极矩到 MO 对，定位原子时选 `11`。
7. 一批态的吸收光谱去主功能 11 画 UV-Vis（见应用导览其它组）。

延伸阅读：sec-3-21-electron-excitation-analysis.md、sec-4-18-electron-excitation-analysis.md。

## 场景 3：反应位点在哪、哪种试剂进攻

一句话：预测亲电/亲核进攻位点，排序原子反应活性，给出可画图的位点图。

| 任务 | 用哪个主功能（链 menu/func-NN.md） | 关键选项 |
|---|---|---|
| 凝聚 Fukui 函数、对偶描述符、软度、亲电/亲核指数一张表 | [主功能 22](menu/func-22.md) | 选项 1 生成 N/N±1 输入 → 算完选 2，得 CDFT.txt（含 f⁺/f⁻/CDD、局域软度、相对亲电/亲核性） |
| Fukui 函数/对偶描述符等值面图 | [主功能 22](menu/func-22.md) | 选项 3；选项 -1 设缩放因子可直接得局域软度/局域超软度格点 |
| Fukui 势/对偶描述符势（ESP 差，定位反应位） | [主功能 22](menu/func-22.md) | 选项 9；Vf⁺ 越正越易亲核反应，Vf⁻ 越正越易亲电反应；用稀疏格点 |
| 键的亲电/亲核性排序 | [主功能 22](menu/func-22.md) | 选项 10（BDD）；负为亲核键、正为亲电键 |
| 简并体系（C₆₀、苯）对称性正确的 Fukui/对偶描述符 | [主功能 22](menu/func-22.md) | 选项 4 设 Δ → 选项 5 查权重 → 选项 6 凝聚值 / 选项 7 格点；Δf_w 对应自定义函数 98 |
| 考虑弛豫的简并 Fukui（基于电子密度） | [主功能 22](menu/func-22.md) | 选项 -3 设 p/q → 选项 1 生成输入 → 选项 2/3 计算 |
| vdW 面上 ESP 极值找亲电/亲核位、σ-hole | [主功能 12](menu/func-12.md) | 映射函数 ESP，选项 0 启动；后处理 14 定量极值周围面积 |
| vdW 面上 ALIE 找易亲电进攻位（越小越活泼） | [主功能 12](menu/func-12.md) | 选项 2 切映射函数为 ALIE（编号 I），选项 0 启动 |
| 前线轨道成分（谁主导 HOMO/LUMO） | [主功能 8](menu/func-08.md) | 选项 1/2/3 看单轨道成分；选项 -1/-2 定义片段后选项 4/5/6 看片段贡献 |
| 原子电荷辅助判断（静电主导位点） | [主功能 7](menu/func-07.md) | 选项 1（Hirshfeld）、11（ADCH）、12/13（CHELPG/MK 拟合）；比较多套电荷再下结论 |

典型流程（有机分子亲电/亲核位点）：

1. 优化 N 态几何，进 `22` 选 `1` 生成 N/N+1/N−1 输入（默认 B3LYP/6-31G*，EA 相关量建议带弥散函数）。
2. 跑完三个单点得 `.wfn` 文件后选 `2`，得 CDFT.txt，按 f⁻/CDD 负值找亲电位、按 f⁺/CDD 正值找亲核位。
3. 选 `3` 算 Fukui/对偶描述符格点（中等格点），等值面取约 0.007 a.u. 可视化验证。
4. 进 `12`，映射函数分别选 ESP 与 ALIE 做表面分析，交叉验证极值点与 ALIE 极小是否落在同一原子。
5. 进 `8` 看 HOMO/LUMO 片段成分，确认前线轨道是否定域在候选位点上。
6. 简并体系（苯、C₆₀）改用选项 4–7 轨道加权路线，或选项 -3 密度路线。

延伸阅读：sec-3-25-conceptual-density-functional-theory-analysis.md、sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md、sec-3-15-quantitative-analysis-of-molecular-surface.md、sec-4-12-quantitative-analysis-of-molecular-surface.md、sec-3-10-orbital-composition-analysis.md、sec-3-9-population-analysis-and-calculation-of-atomic-charges.md。

## 四、光谱、极化率与能量分解

> 按实验人员的问题组织：每节先一句话点明解决什么问题，再给任务→主功能映射表、典型流程与延伸阅读。菜单数字原样保留；链接只链文件不写锚点。

## 1. 各种光谱绘制

一句话：已有量子化学程序的频率 / 激发 / NMR 输出时，用 Multiwfn 把峰位强度展宽成可发表的光谱图（IR、Raman、UV-Vis、ECD、VCD、ROA、NMR、DOS/PES），并支持多构象加权与片段分解。

| 任务 | 用哪个主功能 | 关键选项 |
|---|---|---|
| 画 IR 光谱 | [主功能 11](menu/func-11.md) | 选 IR 类型 → 选项 0 绘图；选项 6 展宽函数、选项 8 半峰宽、选项 14 频率比例因子、选项 15 输出各跃迁贡献 |
| 画常规 Raman 光谱 | [主功能 11](menu/func-11.md) | 选 Raman 类型 → 选项 19 先把活性换算为强度（输入激发波长与温度）→ 选项 0 绘图 |
| 画预共振 Raman 光谱 | [主功能 11](menu/func-11.md) | 载入 freq=raman + CPHF=rdfreq 输出，选入射光频率 → 选项 19 换算强度 → 选项 0 绘图 |
| 画 UV-Vis 光谱 | [主功能 11](menu/func-11.md) | 选 UV-Vis → 选项 10 切 eV/nm、选项 15 输出指定跃迁贡献、选项 20 可清零除 S1 外振子强度画荧光谱 |
| 画定向 UV-Vis 光谱 | [主功能 11](menu/func-11.md) | 选 -3 定向 UV-Vis → 选方向（如 XY/Z）→ 选项 0 绘图，各方向曲线相加即总谱 |
| 画 ECD 光谱 | [主功能 11](menu/func-11.md) | 选 ECD → 选项 2 切速度表象旋光强度 → 选项 16 设极值标注 → 选项 0 绘图；SOC-TDDFT 输出可选载入 SOC 数据 |
| 画 VCD 光谱 | [主功能 11](menu/func-11.md) | 选 VCD 类型 → 选项 14 频率比例因子 → 选项 0 绘图（仅手性分子有信号） |
| 画 ROA 光谱 | [主功能 11](menu/func-11.md) | 选 ROA 类型 → 选入射光频率与散射类型（如 SCP(180) 背散射）→ 选项 0 绘图 |
| 画 NMR 光谱 | [主功能 11](menu/func-11.md) | 选 NMR → 选项 6 选元素、选项 7 定化学位移（TMS 参考或定标）→ 选项 0 显示、选项 1 存图 |
| 多体系同图 / 构象加权谱 | [主功能 11](menu/func-11.md) | 写 multiple.txt（每行"文件路径 权重或图例"）后载入绘图；选项 18 切换加权显示、选项 21 控制各曲线显示 |
| 部分振动谱 PVS / PVDOS / OPVS | [主功能 11](menu/func-11.md) | 进振动谱类型 → 选项 24 定义片段并选谱类型 → q 离开 → 选项 0 绘图（v 可切换振动 DOS 显示） |
| 由 UV-Vis 谱预测颜色 | [主功能 11](menu/func-11.md) | 理论谱用选项 25 预测；实验谱载入"波长-吸光度"两列文本后选 0 预测 |
| 画 TDOS / PDOS / OPDOS | [主功能 10](menu/func-10.md) | -1 定义片段（至多 10 个）→ 0 绘图；选项 1 展宽函数、选项 3 半峰宽、选项 7 成分方法、选项 8 切 eV |
| 画 MO-PDOS / 最近邻 OPDOS | [主功能 10](menu/func-10.md) | 最近邻用 00 直接画；MO-PDOS 用 -2 按 MO 集合分组 → 0 绘图 |
| 画 LDOS（单点 / 沿线） | [主功能 10](menu/func-10.md) | 选项 10 输入点坐标画单点 LDOS；选项 11 输入直线起终点与点数画沿线颜色填充图 |
| 画光电子能谱 PES | [主功能 10](menu/func-10.md) | 进 12 → 选项 1 绘图（Koopmans）/ 选项 3 设偏移（广义 Koopmans）→ 选项 6 设 FWHM（默认 0.2 eV） |

典型流程（以 IR 与 UV-Vis 为例，菜单数字原样）：

IR 流程：

1. 用 Gaussian / ORCA / CP2K 跑频率任务得到含频率与强度的输出。
2. 进主功能 11，选 IR 类型。
3. 用选项 14 设频率比例因子校正谐振误差，用选项 6 / 选项 8 设展宽函数与半峰宽。
4. 选项 0 绘图；需要时用选项 15 输出各振动模式贡献，用 s / l 存取绘图设置。

UV-Vis 流程：

1. 用 Gaussian / ORCA 跑 TDDFT（或 sTDA / xtb / BDF），得到激发能与振子强度输出；勿用 .fch / .molden 做输入。
2. 进主功能 11，选 UV-Vis 类型。
3. 用选项 10 切换横轴单位（eV / nm），用选项 6 / 选项 8 设展宽与半峰宽。
4. 选项 0 绘图；要分析某峰来源时用选项 15 输出指定跃迁贡献（得 spectrum_curve.txt 与 spectrum_line.txt）。
5. 多构象体系先写 multiple.txt（每行"构象输出路径 Boltzmann 权重"），载入后再选 UV-Vis 类型绘图，粗红线即加权谱。

延伸阅读：

- [sec-3-13-plotting-spectra.md](sec-3-13-plotting-spectra.md)
- [sec-4-11-plot-various-kinds-of-spectra.md](sec-4-11-plot-various-kinds-of-spectra.md)
- [sec-3-12-plotting-density-of-states-pes-and-cohp.md](sec-3-12-plotting-density-of-states-pes-and-cohp.md)
- [sec-4-10-plot-density-of-states-dos-maps.md](sec-4-10-plot-density-of-states-dos-maps.md)
- [sec-1-overview.md](sec-1-overview.md)

## 2. （超）极化率与电导分析

一句话：回答"分子非线性光学响应有多大、来自哪里、沿什么路径传导"时，用解析 polar 输出、SOS 求和、极化率密度与单位球表示定量刻画 α/β/γ，并用 DOS、轨道重叠与输运路径分析导电能力。

| 任务 | 用哪个主功能 | 关键选项 |
|---|---|---|
| 解析静态（超）极化率 | [主功能 24](menu/func-24.md) | 子功能 1 → 选项 1 开始；输出 α/β 张量、各向同性平均、各向异性、β∥（已校正 G09/G16 符号） |
| 解析频率相关（超）极化率与 HRS | [主功能 24](menu/func-24.md) | 子功能 1 → 选项 -1 载入动态数据 → 选频率 / β 类型；β(−2ω;ω,ω) 另给 HRS 强度、退偏比、J=1/3 分量 |
| 解析第二超极化率 γ | [主功能 24](menu/func-24.md) | 子功能 1 → 选项 -1 → 选项 7 解析 α＋γ → 选波长 |
| SOS 方法算 α/β/γ/δ | [主功能 24](menu/func-24.md) | 子功能 2 → 选项 1–4 定频计算、选项 5–7 随态数收敛检验、选项 15–17 随频率扫描、选项 19 β 双频扫描 |
| β 的二能级 / 三能级模型分析 | [主功能 24](menu/func-24.md) | 子功能 2 → 选项 20，输入一个态序号做二能级、两个做三能级；给出跃迁偶极矩、偶极矩差、振子强度分解 |
| （超）极化率密度 | [主功能 24](menu/func-24.md) | 子功能 3 → 选阶数与方向 → 选项 1 生成各电场下 Gaussian 输入 → 选项 2 载入 .wfx；有限差分得密度并作平面图 / 等值面 |
| 单位球与矢量表示 | [主功能 24](menu/func-24.md) | 子功能 5 → 选项 1/2/3 分别载入 α/β/γ 张量生成 VMD 脚本（alpha/beta/gamma.tcl 与矢量版），在 VMD 中运行 |
| 分子中原子的极化率 | [主功能 15](menu/func-15.md) | 选项 13 输出原子有效体积、自由体积、有效极化率与 C6 系数 |
| TDOS / PDOS 判断导电 / 能级对齐 | [主功能 10](menu/func-10.md) | -1 定义片段 → 0 绘图；选项 7 切成分方法、选项 8 切 eV、-6 可把 HOMO 移到零点 |
| COHP 判断成键 / 反键态贡献 | [主功能 10](menu/func-10.md) | -7 切 COHP 模式 → 提供 Kohn-Sham 矩阵 → -1 定义片段 → 0 绘图（画的是 −COHP，正为成键） |
| 分子间轨道重叠（转移积分粗估） | [主功能 100](menu/func-100.md) | 子功能 15：依次载入二聚体与两单体文件，输出单体轨道间重叠积分（如 HOMO-HOMO） |
| Yoshizawa 电子输运路径 | [主功能 100](menu/func-100.md) | 子功能 18：需 NBO 的 NAOMO 信息，计算原子间输运概率并输出有利传输路径 |
| 键长 / 键级交替 BLA / BOA | [主功能 200](menu/func-200.md) | 子功能 18：定义路径原子序列，输出 BLA / BOA 及键角二面角演化曲线 |

典型流程（菜单数字原样）：

解析 polar 输出流程：

1. 在 Gaussian 中跑 polar 任务（输入须用 #P；频率相关需在几何后给频率并用 CPHF=RdFreq / DCSHG）。
2. 进主功能 24，选子功能 1。
3. 静态量直接选对应选项 1–7 开始解析；频率相关先用选项 -1 切换解析动态结果再选频率 / β 类型。
4. 读屏幕打印的各分量、各向同性值、各向异性与 HRS 量；需要时用选项 -3 切单位、用选项 -4 导出张量 txt 供单位球模块使用。

SOS 流程：

1. 先经主功能 18 选项 5 选项 3 由 .fch＋.out 生成 SOS.txt（或按手册格式手写激发能＋跃迁偶极矩文件）。
2. 进主功能 24 选子功能 2。
3. 用选项 1 / 2 / 3 算 α / β / γ，用选项 5–7 检验随态数收敛。
4. 解释 β 来源时用选项 20 做二 / 三能级模型分析。

电导初筛流程：

1. 进主功能 10，用 -1 定义给体 / 受体片段，用 0 画 TDOS / PDOS 看能级对齐与片段贡献。
2. 用主功能 100 子功能 15 算二聚体中单体 HOMO-HOMO / LUMO-LUMO 重叠积分。
3. 用主功能 100 子功能 18 做 Yoshizawa 输运路径分析，指认有利电子传输通道。
4. 需要时用主功能 200 子功能 18 沿共轭路径算 BLA / BOA，判断离域程度。

延伸阅读：

- [sec-3-27-hyperpolarizability-analysis.md](sec-3-27-hyperpolarizability-analysis.md)
- [sec-4-24-examples-of-hyperpolarizability-analyses.md](sec-4-24-examples-of-hyperpolarizability-analyses.md)
- [sec-3-12-plotting-density-of-states-pes-and-cohp.md](sec-3-12-plotting-density-of-states-pes-and-cohp.md)
- [sec-3-18-fuzzy-atomic-space-analysis.md](sec-3-18-fuzzy-atomic-space-analysis.md)
- [sec-3-100-other-functions-part-1.md](sec-3-100-other-functions-part-1.md)
- [sec-3-200-other-functions-part-2.md](sec-3-200-other-functions-part-2.md)
- [sec-1-overview.md](sec-1-overview.md)

## 3. 能量分解与片段相互作用

一句话：回答"两个片段为什么结合在一起、静电 / 排斥 / 色散 / 轨道作用各占多少、电荷如何转移"时，用 EDA-FF / sobEDA / EDA-SBL 做能量分解，用 CDA / ETS-NOCV 做轨道相互作用与电荷转移分析。

| 任务 | 用哪个主功能 | 关键选项 |
|---|---|---|
| EDA-FF 力场能量分解 | [主功能 21](menu/func-21.md) | 子功能 1：选项 3 载入分子列表 → 选项 2 定义片段 → 选项 1 计算；输出静电 / 排斥 / 色散分量与原子贡献 |
| 导出原子对能量明细与着色文件 | [主功能 21](menu/func-21.md) | EDA-FF 后处理选项 -3 另存 interatm.txt、选项 -4 输出按能量着色的 .pqr 文件 |
| Shubin Liu 能量分解 EDA-SBL | [主功能 21](menu/func-21.md) | 子功能 2：输入 .fch ＋ 含 ExtraLinks=L608 的 Gaussian 输出；输出位阻 / 静电 / 量子三分量 |
| sobEDA / sobEDAw 能量分解 | [主功能 21](menu/func-21.md) | 无直接菜单，走外部 sobEDA.sh 脚本调用 Gaussian＋Multiwfn；稳健通用的 DFT 能量分解，作者推荐 |
| 原子对色散能贡献 / 差值分析 | [主功能 21](menu/func-21.md) | 子功能 4：选项 1 算当前体系、选项 3 算两体系差值；输出 atomdisp.pqr 与色散密度 cube |
| 碎片波函数组合初猜（含简单能量分解） | [主功能 100](menu/func-100.md) | 子功能 8：依次载入各片段 Gaussian 输出得 new.gjf；首末 SCF 迭代能量差即轨道相互作用能 |
| CDA / ECDA 电荷分解 | [主功能 16](menu/func-16.md) | 选项 0 / 1 打印 d / b / r 与 ECDA 净转移电子数；选项 -3 设阈值、选项 -2 切输出到 CDA.txt |
| 复合物轨道的片段轨道组成 | [主功能 16](menu/func-16.md) | 选项 2：Mulliken（或 SCPA）组成，定位关键片段轨道贡献 |
| 分解 CDA 到片段轨道对贡献 | [主功能 16](menu/func-16.md) | 选项 6：按片段轨道对阈值过滤，揭示 d / b / r 的轨道对来源 |
| 绘制轨道相互作用图 | [主功能 16](menu/func-16.md) | 选项 5：按能量画线、超组成判据连红线，可调标签 / 能量范围 / 平移与连接规则 |
| 导出片段轨道系数 / 重叠矩阵 | [主功能 16](menu/func-16.md) | 选项 3 / 4 写 coFO.txt（复合物轨道在片段轨道基下系数）与 ovlpint.txt（片段轨道间重叠） |
| ETS-NOCV 分析 | [主功能 23](menu/func-23.md) | 输入片段数并依次载入片段文件 → 后处理 -1 / -2 求 NOCV 能量、1 / 2 看轨道与对密度、3–5 看 Pauli / 轨道 / 总形变密度、14 算 SCPA 组成 |
| 碎片间静电作用能（点电荷近似） | [主功能 7](menu/func-07.md) | 先算出原子电荷 → -1 定义碎片 → -2 载入 .chg / .pqr 算两碎片库仑作用能 |
| 激发态的片段间电荷转移 IFCT | [主功能 18](menu/func-18.md) | 选项 8：定义片段后给出片段间转移矩阵并绘热图 |

典型流程（菜单数字原样）：

EDA-FF 流程：

1. 准备体系几何文件与分子列表文件（含原子电荷 / 类型）。
2. 进主功能 21，选子功能 1。
3. 用选项 3 载入分子列表，用选项 2 定义片段。
4. 用选项 1 计算，读每对片段的静电 / 排斥 / 色散分量与原子贡献；需要时用选项 -3 导出 interatm.txt、用选项 -4 输出着色 .pqr。

CDA 流程：

1. 准备复合物与各片段文件（方法基组坐标原子顺序一致，避免弥散函数；开壳层需翻转其中一片段自旋）。
2. 进主功能 16，按片段数选选项 2（两片段）或选项 3（多片段）。
3. 用选项 0 / 1 打印 d / b / r 与 ECDA 净转移电子数。
4. 用选项 2 查关键复合物轨道的片段轨道组成，用选项 6 分解到片段轨道对贡献。
5. 用选项 5 绘制轨道相互作用图。

ETS-NOCV 流程：

1. 准备复合物与各片段波函数文件（片段用 nosymm、几何与复合物一致；另需 Fock 矩阵文件或由轨道能量生成）。
2. 进主功能 23，输入片段数并依次载入各片段文件。
3. 用后处理 -1 / -2 生成矩阵并求 NOCV 能量。
4. 用选项 1 / 2 看 NOCV 轨道与对密度等值面，用选项 3–5 看 Pauli / 轨道 / 总形变密度，用选项 14 算组成。

延伸阅读：

- [sec-3-24-energy-decomposition-analysis.md](sec-3-24-energy-decomposition-analysis.md)
- [sec-4-21-energy-decomposition-analysis.md](sec-4-21-energy-decomposition-analysis.md)
- [sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md](sec-3-19-charge-decomposition-analysis-and-orbital-interaction-diagram.md)
- [sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md](sec-4-16-charge-decomposition-analysis-and-orbital-interaction-diagram.md)
- [sec-4-23-examples-of-ets-nocv-analysis.md](sec-4-23-examples-of-ets-nocv-analysis.md)
- [sec-3-9-population-analysis-and-calculation-of-atomic-charges.md](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md)
- [sec-4-18-electron-excitation-analysis.md](sec-4-18-electron-excitation-analysis.md)
- [sec-1-overview.md](sec-1-overview.md)
