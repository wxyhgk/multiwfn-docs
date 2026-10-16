# 主功能5：在空间区域内输出并绘制特定性质

功能概述：主功能5用于计算实空间函数的三维格点数据或生成 Gaussian 型 cube 文件（`.cub`，VMD、GaussView、VESTA 均支持），格点等值面可直接在 Multiwfn 内查看。流程固定为三步：选实空间函数、设格点、后处理（看等值面、修改导出数据）。另支持计算任意分布点集的函数值，以及只显示特定片段的等值面。

## 基本流程与格点模式1–11

说明：格点模式 1–3 为固定总点数的快/中/高质量（相对中等体系而言，大体系模式3只算中等质量，小体系模式1已足够）；模式 4–7 自定义；模式 8 套用已有 cube 格点；模式 10 GUI 设盒子；模式 11 片段扩展盒子。算完后屏幕打印数据统计（总和、最值坐标；电子密度还打印偶极矩）。

菜单路径：主菜单 → `5` → 选实空间函数 → 选格点模式

输入要求：原子坐标 ＋ GTFs（依所选函数而定）。

操作步骤（原始格式）：

```text
(1) 选择一个实空间函数
(2) 设置格点：
模式 1 (Mode 1)：低质量格点，总共约 125000 个点（立方体对应 50*50*50），推荐用于预览。
模式 2 (Mode 2)：中等质量格点，总共约 512000 个点（立方体对应 80*80*80）。
    小分子该质量足以满足大多数分析需求。
模式 3 (Mode 3)：高质量格点，总共约 1728000 个点（立方体对应 120*120*120）。
    模式1、2、3各方向实际点数由程序自动定，使格点间距近似相等；空间范围为恰好
    包围分子的盒子再各维扩展（扩展距离选项 "-10 Set extension distance of grid
    range" 可改，或改 settings.ini 的 "Aug3D"）。
模式 4 (Mode 4)：自定 X、Y、Z 方向格点数或格点间距，空间范围自动确定。
模式 5 (Mode 5)：自定全部细节（原点、各方向点数、X/Y/Z 格点间距），适合有经验用户。
模式 6 (Mode 6)：指定中心坐标、各方向点数和扩展距离。如中心 2.3,1.0,5.5，
    扩展 k,k,m，则两远端为 (2.3-k,1.0-k,5.5-m) 和 (2.3+k,1.0+k,5.5+m)。适合局域性质。
模式 7 (Mode 7)：输入两个原子序号，以其中点为中心（两序号相同则以该核为中心）。
    研究二聚体间弱作用区常用，如输入 1,14。
模式 8 (Mode 8)：套用一个已有 cube 文件的格点设置（原点、点数、间距），
    适合生成多个格点设置完全相同的 cube。
模式 9 (Mode 9)：仅输入文件含晶胞信息时可见。输入原点、盒子边长和格点间距
    （三方向共用）；直接回车则盒子与晶胞差一个格点间距，此时函数积分可直接
    基于格点求和 sum_i f(i)*v。
模式 10 (Mode 10)：GUI 窗口设格点：盒子可见，拖标尺改边长/中心/间距
    （三方向共用间距），右下角显示当前格点总数。
模式 11 (Mode 11)：输入原子序号定义片段＋扩展距离＋格点间距（三方向共用），
    盒子由片段向外扩展确定；用 IRI/IGMH-mIGM 研究片段与环境相互作用时特别有用。
(3) 后处理：可视化等值面、修改并导出数据。
```

产出：内存格点数据；统计信息；后处理见下节。

来源：[3.6](sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md)；[MENU_INDEX.md](MENU_INDEX.md)。

## 后处理选项

说明：格点算完后的后处理菜单，关键选项原文如下。等值面 GUI 中拖滑动条（上下限 −5/+5）或文本框输入精确值回车改等值面；`Show data range` 以蓝框标空间范围；与当前值同号等值面绿、反号蓝。

菜单路径：主功能5 → 格点算完后后处理菜单

输入要求：内存格点数据。

操作步骤（原始格式）：

```text
-1 Show isosurface graph：弹 GUI 看等值面。
1  将等值面图导出为图形文件。
2  将格点数据导出为 .cub 文件。
3  将格点数据导出为纯文本 output.txt。
4  不进 GUI 直接设等值面数值（适合批处理/命令行）。
5~8 对格点数据做加、减、乘、除运算；选项 10 恢复原始格点数据。
9  只可视化特定片段等值面：输入片段原子序号，每格点算该片段 Hirshfeld 权重
   并乘到原始数据上，远离片段处归零。远离片段处归零后等值面即只显示该片段。
```

产出：等值面图、`.cub`、`output.txt`。

来源：[3.6 后处理选项](sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md#后处理选项)。

## 隐藏选项：Becke/Hirshfeld 权重的空间格点

说明：实空间函数选择菜单中的两个隐藏选项，直接计算原子空间权重函数的格点。

菜单路径：主功能5 → 隐藏选项 `111` / `112`

输入要求：原子坐标。

操作步骤（原始格式）：

```text
111：待计算函数为某个原子的 Becke 权重或两个原子间的 Becke 交叠权重。
112：计算给定原子或片段的 Hirshfeld 权重。
```

产出：权重函数格点数据/等值面。

来源：[3.6](sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md) PS；[MENU_INDEX.md](MENU_INDEX.md)。

## 特殊情形：计算任意分布点集的函数值

说明：用外部文件提供的一组任意点坐标批量算函数值，坐标单位必须为 Bohr。

菜单路径：主功能5 → 设格点界面选 `100 Load a set of points from external file`

输入要求：点坐标文本文件（首行点数，后为 X/Y/Z 坐标）＋ GTFs。

操作步骤（原始格式）：

```text
100 Load a set of points from external file
输入点文件路径，文件格式如：
```

```text
1902
   -3.3790050   -2.0484700    0.0274117
   -3.3844930   -1.9472468   -0.2500274
   -3.4064601   -1.9221635   -0.1287148
   -3.4118258   -1.9232203   -0.0003350
   -3.4059106   -1.9218280    0.1351179
....
```

```text
坐标必须以 Bohr 为单位，自由格式，多于四列时第四列之后被忽略。
Multiwfn 载入坐标并计算函数值，最后将 X/Y/Z 坐标和函数值输出到用户指定的纯文本文件。
```

产出：坐标＋函数值文本文件。

来源：[3.6 特殊情形](sec-3-6-outputting-and-plotting-specific-property-within-a-spatial-region.md#特殊情形计算一组任意分布的点的数据)。

## 实例：ClF₃ 的 ELF 等值面

说明：最基础的格点＋等值面例子；中等质量格点对小体系足够，大体系应提高。

菜单路径：主功能5 → `9` ELF → `2` 中等质量格点 → `-1` 看图

输入要求：`examples\ClF3.wfn`（B3LYP/6-31G*）。

操作步骤（原始格式）：

```text
examples\ClF3.wfn  // Generated at B3LYP/6-31G* level
5  // Generate grid data and view isosurface
9  // Electron localization function (ELF)
2  // Medium-quality grid, about 512000 points
```

算完选 `-1` 看等值面，文本框输入 `0.85` 回车；选项 `2` 导出 cube（可用 VMD/ChimeraX 高质量渲染，见 4.A.14）。

产出：ELF=0.85 等值面，F/Cl 孤对区清晰；按盆类型着色的 ELF 图做法见 4.17.10。

来源：[4.5.1](sec-4-5-generate-grid-data-and-view-isosurface-map.md#451-三氟化氯的电子定域函数)。

## 实例：1,3-丁二烯电子密度拉普拉斯等值面

说明：拉普拉斯分辨能力不如 ELF/LOL（重于 Kr 的壳层显示不全、数值范围太大），但对很多体系仍有用；等值面不光滑时改高质量格点。

菜单路径：主功能5 → `3` 电子密度拉普拉斯 → `2` → `-1`

输入要求：`examples\butadiene.fch`（B3LYP/6-31G**）。

操作步骤（原始格式）：

```text
examples\butadiene.fch  // Yielded at B3LYP/6-31G** level
5  // Generate grid data and view isosurface
3  // Electron density Laplacian
2  // Medium-quality grid
-1  // View isosurface
```

等值面数值改 `0.3`（绿/蓝分别对应 ±0.3）。

产出：拉普拉斯等值面；C–C/C–H 间蓝色区表价层电子集中（共价特征），两侧 C–C 面宽于中央（键级 1.863 vs 1.136，Mayer 键级可验证）。

来源：[4.5.2](sec-4-5-generate-grid-data-and-view-isosurface-map.md#452-13-丁二烯的电子密度拉普拉斯)。

## 实例：苯 ELF-σ/ELF-π 芳香性指标

说明：分岔点（3,-1）处 ELF 值即指标，>0.70 判有相应芳香性。先用主功能0确认 π 轨道为 MO 17、20、21；置零 σ 或 π 占据分离 ELF-π/ELF-σ（或主功能100子功能22自动识别 π：选 `0` 后选 `1` 清零其余占据，重元素选 `3`）。

菜单路径：主功能0 看轨道 → 主功能6 → `26` 设占据数 → 主功能5 ELF 等值面找分岔 → 主功能2 → `-11` → `9` → `6` 搜 CP → `7` 读值

输入要求：`examples\benzene.wfn`（B3LYP/6-311G*）。

操作步骤（先看轨道，原始格式）：

```text
examples\benzene.wfn  // Optimized at B3LYP/6-311G* level
0  // View molecular orbitals (MOs)
```

逐个查看发现 π 轨道为 17、20、21。求 ELF-π：清零全部 σ 占据（原始格式）：

```text
6  // Enter "Modify & Check wavefunction" interface
26  // Set occupation number for some orbitals
0  // Selecting all orbitals
0  // Set occupation number of all orbitals to zero
17,20,21  // Select MO 17, 20 and 21, namely all π orbitals
2  // Set occupation numbers of MO 17, 20 and 21 to 2.0
q  // Return to last menu
-1  // Return to main menu
```

方式1：主功能5 常规产生 ELF 等值面（建议高质量格点），渐增等值面数值，≈0.91 时两圆环域分岔为十二球状域 → ELF-π≈0.91。方式2（精确，原始格式）：

```text
2  // Topology analysis
-11  // Select real space function
9  // ELF
6  // Starting points distributed around each atom, most appropriate for ELF CPs
-1  // Start the CP search
-9  // Return to upper menu
0  // Visualize results
```

再查 (3,-1) 点 ELF 值（原始格式）：

```text
7  // Show all properties at a CP
23  // CP23
```

产出：CP23 处 ELF=0.91247 即 ELF-π（文献 0.913）；同法清零 MO 17、20、21 求 ELF-σ≈0.70907（CP48，文献 0.717）；均值 0.81077>0.70 → 全局芳香。

来源：[4.5.3](sec-4-5-generate-grid-data-and-view-isosurface-map.md#453-计算-elf-σ-和-elf-π-以研究苯的芳香性)。

## 实例：苯酚 Fukui 函数 f⁻ 与 f⁰

说明：日常建议直接用主功能22自动算（见 3.25/4.22.1）；此处演示手动经自定义操作做密度差。N−1 态做单点不优化几何（偏导中外势 ν 即核坐标为常数）。

菜单路径：主功能5 → `0` 自定义操作 → `1` 一个文件 → `-` 相减 → `1` 电子密度

输入要求：`phenol.wfn`（中性）＋ `phenol_N-1.wfn`（阳离子，同几何，B3LYP/6-31G*）。

操作步骤（f⁻，原始格式）：

```text
examples\phenol.wfn  // Phenol of neutral state
5  // Calculate grid data
0  // Set custom operation
1  // Only one file will be operated with the file that has been loaded
-,examples\phenol_N-1.wfn  // Property of phenol.wfn minus that of phenol_N-1.wfn
1  // Electron density
2  // Medium-quality grid
```

`-1` 看等值面，取 0.007：绿/蓝为 f⁻ 正/负区，O12、C1、C3、C4、C5 最正 → 羟基邻对位为亲电活泼位点。

操作步骤（丙烯 f⁰=(ρN+1−ρN−1)/2，原始格式）：

```text
examples\propylene\N+1.fch  // N+1 electrons state
5  // Calculate grid data
0  // Set custom operation
1  // One file will be operated
-,examples\propylene\N-1.fch  // N-1 electrons state
1  // Electron density
2  // Medium-quality grid
6  // Divide all grid data by a factor
2  // Divided by 2
-1  // Visualize isosurface map
```

等值面取 0.01。

产出：f⁻/f⁰ 等值面图，定位亲电/自由基活泼位点。

来源：[4.5.4.1](sec-4-5-generate-grid-data-and-view-isosurface-map.md#4541-福井函数)。

## 实例：苯酚对偶描述符（自旋近似 vs 电子密度精确式）

说明：Δf>0 利于亲核、Δf<0 利于亲电；比较多位点时只看相对正负即可。自旋近似辨别力常更好。

菜单路径：主功能5 → `0` 自定义操作 → `5` 自旋密度（近似）或 `1` 电子密度三文件精确式

输入要求：`phenol_N+1.wfn` ＋ `phenol_N-1.wfn`（＋精确式另需 `phenol.wfn`）。

操作步骤（自旋密度近似，原始格式）：

```text
examples\phenol_N+1.wfn  // N+1 electron system, namely anionic state
5  // Calculate grid data
0  // Set custom operation
1  // Only one file will be operated
-,examples\phenol_N-1.wfn  // N-1 electron system, namely cationic state
5  // Electron spin density
2  // Medium-quality grid
-1  // Visualize isosurface of dual descriptor
```

等值面取 0.02：对位 C 大负值、邻位不如间位正 → 邻对位为亲电位点，与 f⁻ 一致。

操作步骤（电子密度精确式 Δf=ρN+1−2ρN+ρN−1，原始格式）：

```text
examples\phenol_N+1.wfn  // N+1 electron system
5  // Calculate grid data
0  // Set custom operation
3  // Three files will be operated
-,examples\phenol.wfn  // N electron system
-,examples\phenol.wfn  // N electron system
+,examples\phenol_N-1.wfn  // N-1 electron system
1  // Electron density
2  // Medium-quality grid
-1  // Visualize isosurface of dual descriptor
```

等值面取 0.01：与近似式定性一致但邻/间差别不显著。定量化用凝聚 Fukui/对偶描述符（见 4.7.3）或表面局域平均（见 4.12.4）。

产出：对偶描述符等值面图。

来源：[4.5.4.2](sec-4-5-generate-grid-data-and-view-isosurface-map.md#4542-对偶描述符)。

## 实例：电子密度差值等值面与等值线（咪唑–镁卟啉）

说明：复合物减各片段；Gaussian 默认标准取向会重定向坐标，route 须加 `nosymm`。大体系用高质量格点；等值面取 ±0.001 左右看电荷转移/极化，cube 用 VMD 双色渲染。

菜单路径：主功能5 → `0` → `2` 两文件 → `1` 电子密度 → `3` 高质量格点

输入要求：`MN-NN.wfn` ＋ `MN.wfn` ＋ `NN.wfn`（同坐标，`nosymm`）。

操作步骤（原始格式）：

```text
MN-NN.wfn
5  // Calculate grid data
0  // Set custom operation
2  // Two files will be operated with MN-NN.wfn
-,MN.wfn  // Will subtract property of MN.wfn from that of MN-NN.wfn
-,NN.wfn  // Will subtract property of NN.wfn from that of MN-NN.wfn
1  // The property is selected as electron density
3  // High-quality grid (system relatively huge)
```

`-1` 看等值面取约 0.001；选项 `2` 导出 cube 用 VMD 画双色图（红 +0.0012/蓝 −0.0012，见 4.5.5 注记）。配套等值线画法：回主菜单进主功能4同样自定义操作后选 `2` 等值线图，再按 3.5.4 用等比数列 `0.0001,2,30` / `-0.0001,2,30` 加密等值线。

产出：密度差等值面/等值线；电子由 NN 氮背侧移向 Mg 加强配位键，卟啉环仅四配位 N 轻微极化。

来源：[4.5.5](sec-4-5-generate-grid-data-and-view-isosurface-map.md#455-绘制电子密度差值图以研究咪唑配位镁卟啉的电子转移)。

## 实例：EDR 电子离域范围函数（阴离子水二聚体）

说明：EDR(**r**;d) 生动显示溶剂化电子分布；长度尺度 d 大对应更离域电子。

菜单路径：主功能5 → `20` EDR → 输入 d → `2` → `-1`

输入要求：`examples\solvatedelectron.wfn`（(H₂O)₂⁻，B3LYP/6-311++G(2d,2p)）。

操作步骤（原始格式）：

```text
examples\solvatedelectron.wfn  // Anionic water dimer
5  // Calculate grid data
20  // EDR(r;d)
11.22  // Input length scale d (Bohr)
2  // Medium-quality grid
-1  // Show isosurface graph
```

等值面取 0.74。

产出：EDR 等值面；d=11.22 Bohr 下溶剂化电子位于两水分子之间。

来源：[4.5.6](sec-4-5-generate-grid-data-and-view-isosurface-map.md#456-研究阴离子水二聚体的电子离域范围函数-edrrd)。

## 实例：D(r) 轨道重叠距离函数映射（硫代甲酸）

说明：D(**r**) 对 d 最大化 EDR；指数用均匀递变格点拟合（默认 n=20、α₁=2.50、αinc=1.50 对常见体系足够）。两次格点设置必须相同，再把 D(**r**) 映射到 ρ=0.001 面上。

菜单路径：主功能5 → `21` D(r) → `2` 导出 `EDRDmax.cub` → 回主菜单主功能5 → `1` 密度 → `2` 导出 `density.cub`

输入要求：`examples\ThioformicAcid.wfn`（B3LYP/6-311++G(2d,2p)）。

操作步骤（原始格式）：

```text
examples\ThioformicAcid.wfn
5  // Calculate grid data
21  // Orbital overlap length function D(r), which maximizes EDR(r;d) with respect to d
```

选手动输入（选项1）或默认（选项2）设指数总数/起始值/增量后：

```text
2  // Medium-quality grid
```

算完选项 `2` 导出 `EDRDmax.cub`，再：

```text
0  // Return to main menu
5  // Calculate grid data
1  // Electron density
2  // Medium-quality grid (The grid setting must be the same as for D(r) calculation)
```

选项 `2` 导出 `density.cub`；用 VMD/GaussView 把 D(**r**) 映射到 ρ=0.001 面（做法见 <http://sobereva.com/402>）。

产出：2.9 Bohr（红，硬 O 孤对）到 3.4 Bohr（蓝，软 S 孤对）的颜色映射面；定量分析见 4.12.8。

来源：[4.5.7](sec-4-5-generate-grid-data-and-view-isosurface-map.md#457-研究硫代甲酸的轨道重叠距离函数-dr)。
