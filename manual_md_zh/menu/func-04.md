# 主功能4：在平面内输出并绘制特定性质

功能概述：主功能4用于把任一实空间函数绘制为平面图，是 Multiwfn 最常用的可视化入口之一。基本流程固定为六步：选实空间函数、选图类别、设格点数、定义平面、查看图形、后处理微调。支持填充色图、等值线图、浮雕图、梯度线图、矢量场图等七类图，平面定义有 8 种模式，并可在图上叠加临界点、键径与盆间路径。

## 基本流程

说明：进入主功能4后的标准六步，程序全程给出提示，只有少数关键点需要人工判断。

菜单路径：主菜单 → `4`

输入要求：GTFs（依所选实空间函数而定）＋原子坐标。`settings.ini` 中 `iplaneextdata=1` 时平面数据改从外部纯文本文件载入（各点坐标会自动输出到当前文件夹，可用 Gaussian 的 cubegen 等第三方工具在这些点上算函数值）。

操作步骤（原始格式）：

```text
1.  选择一个实空间函数
2.  选择图的类别
3.  设定两个维度上的格点数
4.  定义一个平面
5.  查看图形
6.  后处理（调整作图参数、保存图形、将数据导出为纯文本文件等）
```

产出：平面图图形文件、平面数据文本（`plane.txt`）。

来源：[3.5](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md)；[MENU_INDEX.md](MENU_INDEX.md)；实例见 [4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md)。

## 图的类别（共7种）

说明：Multiwfn 支持七种展示平面内数据的图类别，特点与后处理选项如下。

菜单路径：主功能4 → 选实空间函数 → 选图类别编号

输入要求：同上。

操作步骤（原始格式）：

```text
1 填充色图 (Color-filled map)：不同颜色表示不同区域的函数值。默认 "Rainbow" 颜色过渡，
   低于色标下限填黑色、高于上限填白色；后处理 "Set color transition" 可换颜色过渡；
   "Enable showing contour lines" 可叠加等值线；可控制原子标签与成键显示。
2 等值线图 (Contour line map)：实线表正值区、虚线表负值区。"2 Enable showing isovalue
   on contour lines" 在等值线上标数值；"9 Enable filling colors for contour lines"
   在等值线间填色（再选一次可调填充效果）。仅对轨道波函数可一次输入两个轨道序号
   （如 3,5）同时绘制两个轨道。
3 浮雕图 (Relief map)：高度表数值；数值太大被截断时可乘因子缩放；交互界面可旋转/放大缩小。
4 阴影浮雕图 (Shaded relief map) / 5 带投影的阴影浮雕图 (Shaded relief map with projection)：
   带阴影，后者另加一幅填充色图作投影；表面网格线可在后处理关闭。
6 带/不带等值线的梯度线图 (Gradient line map with/without contour lines)：表函数梯度方向，
   可决定是否同时显示等值线；计算与作图代价明显高于其它类别。后处理
   "11 Set detailed parameters of plotting gradient line" 设参数：
   子选项1梯度线积分步长（越小越精细）、子选项2梯度线间隔（越小越密）、
   子选项3绘制新梯度线判据、子选项4积分方法（RK4最稳健但最耗时，默认RK2兼顾精度速度）、
   子选项5和6梯度线颜色和宽度。
7 带/不带等值线的矢量场图 (Vector field map with/without contour lines)：梯度线换成均匀
   分布的箭头；可设箭头颜色、按函数值着色、反转箭头方向。选项10设缩放上限 x，
   梯度矢量模超 x 时被缩放为 x。
```

产出：各类平面图。

来源：[3.5.1](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md#351-图的类别)。

## 格点数与8种平面定义模式

说明：格点数如 `100,150` 表示两维度格点数，总数均匀分布在作图区域。浮雕类推荐 `100,100`（再密则线太挤），其它类别推荐 `200,200`；越大越光滑但等待越久。总 ESP 计算非常耗时，宜用较少格点。

菜单路径：主功能4 → 选函数 → 选图类别 → 输入格点数 → 选平面模式

输入要求：同上。

操作步骤（原始格式）：

```text
1.  XY 平面：输入 Z 值唯一确定。
2.  XZ 平面：输入 Y 值唯一确定。
3.  YZ 平面：输入 X 值唯一确定。
4.  由三个原子定义：输入三个原子序号，用原子核坐标定义平面。
5.  由三个点定义：输入三个点坐标定义平面。
6.  输入原点和平移矢量（只适合专家，两个平移矢量必须正交）。
7.  定义一个平行于某化学键、同时垂直于由三个原子定义的平面的平面。
    先输入如 3,5 以定义所平行于的轴，再输入如 2,3,10 以定义所垂直于的平面，
    再输入 X、Y 轴长度（如 10 和 7 Bohr）。
8.  在特定原子组成的上方或下方（局域平面，常用于研究环上/下方分布）：
    输入原子序号定义拟合平面（作图平面平行于它）和几何中心，再输入作图平面与
    几何中心间的垂直距离 d（正负对应上/下方），再输入作图平面边长（正方形，
    几何中心投影点为平面中心）。
模式 1~5：作图区域自动包住整个分子（模式1、2、3）或覆盖输入的三原子核/点
    （模式4、5），再向外扩展（默认 4.5 Bohr，选项 "0 Set extension distance
    for plane type 1~5" 可改，或改 settings.ini 的 "Aug2D"）。
模式 4、5、8 的平移旋转：在选模式前先选 "-1: Set translation and rotation of
    the map for plane types 4, 5 and 8"，如先输入 -3,1.5 再输入 35 表示
    平移 (-3,1.5) Bohr 再旋转 35°。
```

产出：确定作图平面与区域；模式8会在命令行给出三条命令，复制到 VMD 控制台可画出作图平面以核对定义。

来源：[3.5.2](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md#352-格点平面和作图区域的设置)。

## 后处理常用选项

说明：图形弹出后出现的后处理菜单选项，多数自明，这里列出关键项原文。

菜单路径：主功能4 → 绘图完成后后处理菜单

输入要求：同上。

操作步骤（原始格式）：

```text
-9 Only plot the data around certain atoms：只绘制关注区域。如输入 2,4,8-10，
   则只绘制原子 2,4,8,9,10 周围的实空间函数（原平面数据乘以输入片段的 Hirshfeld
   权重）。下次再选此选项恢复原数据。
-7 Multiply data by a factor：缩放平面数据范围。
-6 Export the current plane data to plane.txt in current folder：导出平面数据，
   可用 Sigmaplot 等第三方软件重绘。
-2 Set label interval in X, Y (and color scale) axes：设坐标轴标签间隔；
   图上无坐标轴标签说明当前间隔太大。
-1 Show the graph again：调参后重绘。
0 Save the graph to a file：导出图形文件（格式尺寸见 2.8 节）。
19 Enable showing extrema of a function on a contour line：在电子密度等值线上
   绘如静电势的极大极小值（见 4.4.12 节）。
4 是否显示原子标签/参考点：标签大小与形式由 settings.ini 的 "pleatmlabsize" 和
   "iatmlabtype" 定；参考点为蓝色星号；默认仅原子到平面距离小于 "disshowlabel"
   才显示标签；选项 17 可改阈值。
8 是否显示成键：两原子都离平面足够近（小于 "disshowlabel"）且间距小于成键阈值
   （主功能0 GUI 滑块可调）才显示。
15 绘制 vdW 表面等值线（电子密度=0.001 a.u.，Bader 定义），有助于分析 vdW 表面
   ESP 分布；梯度线图/矢量场图同样可用；选项 16 调其颜色、标签大小和线型。
```

产出：微调后的图形、`plane.txt`。

来源：[3.5.1](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md#351-图的类别)、[3.5.3](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md#353-后处理界面中的选项)。

## 等值线设置

说明：对图类别 1、2、6、7 可绘制等值线（未显示时选 "2 Enable showing contour lines"）。"Change setting of contour lines" 界面先列当前等值线值，子选项如下。

菜单路径：后处理 → Change setting of contour lines

输入要求：同上。

操作步骤（原始格式）：

```text
选项 1：保存当前设置并返回上级菜单；再选 "Show the graph again" 即用新设置作图。
选项 2：输入新值替换某条等值线旧值。
选项 3：新增一条等值线并输入等值。
选项 4：删除某些等值线。
选项 6：将当前等值线设置导出为纯文本文件（可为不同体系/函数存多套常用设置）。
选项 7：从外部文件载入等值线设置（格式与子功能 6 输出相同）。
选项 8：按等差数列生成等值线，输入初值、步长和总数。绘 ELF/LOL 建议输入
   0,0.05,21（0.0~1.0 步长 0.05）；可选是否清除已有等值线，选 n 则追加。
选项 9：与 8 类似，按等比数列生成。
选项 10：加粗某些等值线：先输入加粗几条，再依次输入序号；已有加粗时再选则取消全部加粗。
选项 11：设正等值线颜色（输入颜色序号）。
选项 12：设正等值线线型（输入两个整数：线段长度、空隙长度。如 10,15 表长度10线段与长度15空隙交替）。
选项 13、14：与 11、12 类似，针对负值部分。
选项 15：正负线分别设为"深红、宽度=6、实线"和"蓝色、宽度=6、长虚线"，所得图适合发表。
```

产出：自定义等值线图形（建议等值线图存为 `.pdf` 矢量格式：`settings.ini` 的 `graphformat` 改为 `pdf`）。

来源：[3.5.4](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md#354-等值线的设置)。

## 隐藏选项：Becke/Hirshfeld 权重平面图

说明：实空间函数选择菜单中的两个隐藏选项，直接绘制原子空间权重函数。

菜单路径：主功能4 → 隐藏选项 `111` / `112`

输入要求：原子坐标。

操作步骤（原始格式）：

```text
111：待绘制函数为某个原子的 Becke 权重或两个原子间的 Becke 交叠权重。
112：绘制给定原子或片段的 Hirshfeld 权重。
```

产出：权重函数平面图。

来源：[3.5](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md) 注；[MENU_INDEX.md](MENU_INDEX.md)。

## 在平面图上叠加临界点、拓扑路径与盆间路径

说明：临界点与路径可绘制在填充色图、等值线图、梯度线图和矢量场图上。棕、蓝、橙、绿圆点分别表示 (3,-3)、(3,-1)、(3,+1)、(3,+3) 临界点，深棕粗线为键路径，深蓝线为盆间路径。

菜单路径：先主功能2搜 CP 并生成路径 → 主功能4 常规绘图 → 后处理选项 `4` / `Generate interbasin paths`

输入要求：GTFs ＋原子坐标；盆间路径要求拓扑模块已找到至少一个离平面足够近（小于 `disshowlabel`）的 (3,-1) CP。

操作步骤（原始格式）：

```text
1. 进入拓扑分析模块（主功能 2），搜索 CP 并生成路径（键径）。
2. 返回主菜单，按常规用主功能 4 绘制平面图，CP 和路径已出现在图上。
3. 后处理选项 "4 Set details of plotting critical points and paths"：选允许显示
   哪些类别 CP，设标记大小、粗细、距离阈值和路径线颜色。默认 CP 或路径点与平面
   垂直距离超 0.5 Bohr 则不显示；"8 Set distance threshold for showing CPs" 和
   "9 Set distance threshold for showing paths" 可改阈值。
4. 盆间路径：后处理选 "Generate and show interbasin paths"，等生成完重绘平面图
   即呈现。想改变长度，先选 "Set stepsize and maximal iteration for interbasin
   path generation" 输入步长和迭代数（最大长度=两者乘积）；路径点与平面距离超
   "disshowlabel" 的部分不显示。
```

产出：含 CP/键径/盆间路径的平面图（临界点颜色可用 `settings.ini` 的 `CP_RGB_2D` 改）。

来源：[3.5.5](sec-3-5-outputting-and-plotting-specific-property-in-a-plane.md#355-在平面图上绘制临界点路径和盆间路径)；实例 [4.4.6](sec-4-4-output-and-plot-various-properties-in-a-plane.md#446-过氧化氢电子密度的梯度等值线图及拓扑路径)。

## 实例：HCN 电子密度填充色图与等值线图

说明：最基础的平面图例子。Z 轴为 HCN 分子轴，先画 XZ 面填充色图，再微调标签与键，最后换等值线图。

菜单路径：主功能4 → `1` 电子密度 → `1` 填充色图 / `2` 等值线图

输入要求：`examples\HCN.wfn`。

操作步骤（原始格式）：

```text
examples\HCN.wfn
4  // Plot graph in a plane
1  // Electron density
1  // Color-filled map
[Press ENTER button directly]  // Use the recommended grid setting, namely 200,200
2  // XZ plane (Z-axis is the molecular axis)
0  // The XY plane with Y=0 Bohr
```

后处理美化（原始格式）：

```text
-8  // Change length unit of the graph to Å
-2  // Set label interval in X, Y and color scale axes
1,1,0.1
4  // Enable showing atom labels
1  // Red labels
8  // Enable showing bonds
3  // Blue color for bonds
-1  // Redraw the graph
```

产出：HCN 电子密度填充色图（C、N 中心白色区表示密度超色标上限 0.65）与等值线图；数据可导出用 Origin/Sigmaplot 重绘。

来源：[4.4.1.1](sec-4-4-output-and-plot-various-properties-in-a-plane.md#4411-绘制氰化氢的电子密度)。

## 实例：FOX-7 的 LOL 填充色图

说明：由 N9、C2、N12 三原子定面画 LOL；演示标签阈值、颜色过渡与叠加等值线。

菜单路径：主功能4 → `10` LOL → `1` 填充色图 → 模式 `4` 三原子定面

输入要求：`examples\FOX-7.wfn`。

操作步骤（原始格式）：

```text
examples\FOX-7.wfn
4  // Plot plane map
10  // Localized orbital locator (LOL)
1  // Color-filled map
[Press ENTER button directly]
4  // Define the plane by three atoms
9,2,12  // Use nuclear position of the three atoms to define the plane
```

后处理（原始格式）：

```text
8  // Enable showing bonds
14  // Brown color
4  // Enable showing atom labels
1  // Red color
18  // Change style of atomic labels
3  // Plot both element symbol and atomic index
-1  // Show the graph again
```

标签缺失时（原子离平面距离大于 `disshowlabel`）（原始格式）：

```text
17  // Set distance threshold for showing atom labels
10  // Enlarge the threshold to 10 Bohr
y  // 超阈值的原子标签仍显示但用细体
-1  // Plot the map again to check effect
```

换颜色过渡示例（原始格式）：

```text
19  // Set color transition
17  // Black-Blue-Cyan
1  // Set lower&upper limit of color scale
0,0.7
-1  // Replot
```

叠等值线示例（原始格式）：

```text
19  // Set color transition
8  // Blue-White-Red
2  // Enable showing contour lines
1  // Set lower&upper limit of color scale
0,1
-2  // Set label interval in X, Y and color scale axes
2,2,0.1
-1  // Replot
```

产出：FOX-7 LOL 平面图；红色区揭示成键区高定域，N–O 间定域弱于 C–N/C–C（电荷移键特征）。

来源：[4.4.1.2](sec-4-4-output-and-plot-various-properties-in-a-plane.md#4412-绘制-fox-7-的定域轨道定位函数lol)。

## 实例：一氟乙烷 ELF 带投影阴影浮雕图

说明：画 C–C–F 面（原子 1,5,8）的带投影阴影浮雕图；注意手动加大扩展距离防边界截断。

菜单路径：主功能4 → `9` ELF → `5` 带投影阴影浮雕图 → 模式 `4`

输入要求：`examples\C2H5F.wfn`（先用主功能0确认 C–C–F 平面原子序号 1,5,8）。

操作步骤（原始格式）：

```text
examples\C2H5F.wfn
0  // View the molecular structure first to find the plane we are interested in
4  // Plot graph in a plane
9  // Electron localization function (ELF)
5  // Shaded relief map with projection effect
[Press ENTER button]  // Use recommended grid setting, namely 100,100
0  // Manually set extension distance
6  // Set extension distance to 6 Bohr
4  // Define the plotting plane by three atoms
1,5,8  // Indices of the three atoms
```

产出：ELF 浮雕图；C–C/C–F 键区高值表定域强，原子核周围蓝色环为价层–内层低定域区分隔，箭头处为 F 孤对；选项 `0` 存图（边缘截断时先 `-1` 回界面缩小再导出）。

来源：[4.4.2](sec-4-4-output-and-plot-various-properties-in-a-plane.md#442-一氟乙烷电子定域函数elf带投影效果的阴影浮雕图)。

## 实例：不含某些原子贡献的平面图（两种做法）

说明：做法一经主功能6子功能-3/-4删 GTF（不可逆但省后续计算量）；做法二经后处理-9乘 Hirshfeld 权重（只影响当前图，可恢复）。

菜单路径：做法一：主功能6 → `-4` → 主功能4；做法二：主功能4 绘图后 → 后处理 `-9`

输入要求：`examples\uracil.wfn`。

操作步骤（例1，去掉原子3、4贡献的拉普拉斯等值线图，原始格式）：

```text
examples\uracil.wfn
6  // Modify wavefunction
-4  // Discard contribution of some atoms
3,4  // All GTFs centered on atoms 3 and 4 will be discarded
-1  // Return to main menu
4  // Plot graph in a plane
3  // Laplacian function
2  // Contour line map
[Press ENTER button to use default grid setting]
1  // XY plane will be plotted
0  // The Z-position of the XY plane is zero, that is molecular plane
```

操作步骤（例2，只留环内六原子贡献的 LOL 图，原始格式）：

```text
examples\uracil.wfn
4  // Plane map
10  // LOL
1  // Color-filled map
[Press ENTER button to use default grid setting]
1  // XY plane will be plotted
0  // Z=0
```

后处理（原始格式）：

```text
-9  // Only plot the data around certain atoms
1-6  // The index of the six atoms in the uracil ring
8  // Enable showing bonds
14  // Brown
-1  // Replot
```

产出：去贡献平面图；做法二再选 `-9 Recovery original plane data` 可恢复原图。

来源：[4.4.3](sec-4-4-output-and-plot-various-properties-in-a-plane.md#443-绘制不含某些原子贡献的平面图)。

## 实例：ClF₃ 静电势等值线图叠 vdW 表面

说明：ESP 计算耗时，需等待；画完后叠 `ρ=0.001` 的 vdW 线（实/虚线区分正负），判断亲核亲电区。也可用 `.chg` 画原子电荷 ESP。

菜单路径：主功能4 → `12` 总 ESP → `2` 等值线图 → 后处理 `15`

输入要求：`examples\ClF3.wfn`（B3LYP/6-31G*）。

操作步骤（原始格式）：

```text
examples\ClF3.wfn  // Generated at B3LYP/6-31G* level
4  // Plot graph in a plane
12  // Total electrostatic potential
2  // Draw contour line map
120,120  // Number of grids in each direction
3  // YZ plane
0  // Set X coordinate of the YZ plane to 0
```

后处理：关闭图形 → 后处理选 `15` → `-1` 重绘。

`.chg` 输入格式示例（第一列元素名，2–4 列 XYZ/Å，末列电荷；此时选函数 `8` 原子电荷 ESP）：

```text
  Cl    0.000000    0.000000    0.359408    0.529971
  F     0.000000    1.726507    0.294501   -0.228394
  F     0.000000    0.000000   -1.267884   -0.073185
  F     0.000000   -1.726507    0.294501   -0.228394
```

产出：ClF₃ ESP 等值线图；近 Cl 的 vdW 面多与实线相交（Cl 整体带正电），平伏 F 电子少于轴向 F（与 4.7.1 电荷结论一致）。

来源：[4.4.4](sec-4-4-output-and-plot-various-properties-in-a-plane.md#444-三氟化氯静电势的等值线图)。

## 实例：两个轨道波函数的等值线图

说明：同时画 NH₂COH 的 NBO 12 与 NBO 56；用模式7定义平行 C1–N4 且垂直 O3–C1–N4 面的平面；删小值等值线去噪并设发表风格。

菜单路径：主功能4 → `4` 轨道波函数 → 输入 `12,56` → 模式 `7`

输入要求：`examples\NH2COH.31`（再载入 `NH2COH.37`）。

操作步骤（原始格式）：

```text
examples\NH2COH.31
37  // Load NH2COH.37
4  // Plot plane graph
4  // Orbital wavefunction
12,56  // The two orbital indices
[Press ENTER button to use default grid setting]
7  // Define a plotting plane parallel to a bond and meantime normal to a plane defined by three atoms
1,4  // The plotting plane is parallel to C1-N4
3,1,4  // The plotting plane is perpendicular to the plane defined by O3-C1-N4
10  // The length of X-axis of the resulting map is 10 Bohr
10  // The length of Y-axis of the resulting map is 10 Bohr
```

后处理去噪并设发表风格（原始格式）：

```text
3  // Change contour line setting
4  // Delete some contour lines
1-4  // Delete contour lines 1~4 (0.001, 0.002, 0.004, 0.008)
4  // Delete some contour lines
28-31  // Delete -0.001, -0.002, -0.004, -0.008
15  // Set the drawing style suitable for publication (positive: red solid, negative: blue dashed)
1  // Save setting and return to the upper menu
-8  // Change length unit of the graph to Å
-2  // Set label interval in X and Y axes
1,1
-1  // Replot the contour map
2  // Enable showing isovalue on contour lines
30  // Use label size of 30
```

产出：双轨道等值线图，同相重叠区清晰；选项 `6` 可导出等值线设置供下次选项 `7` 载入。

来源：[4.4.5](sec-4-4-output-and-plot-various-properties-in-a-plane.md#445-两个轨道波函数的等值线图)。

## 实例：H₂O₂ 梯度图叠 CP/键径/盆间路径

说明：先画普通电子密度梯度图；再经主功能2（`2` 核位置初猜 → `3` 原子对中点初猜 → `8` 生成键径）产生 CP 与路径后重画，自动叠加；后处理 `4` 调显示，`Generate and show interbasin paths` 加盆间路径。

菜单路径：主功能4 → `1` 电子密度 → `6` 梯度线图；叠加前先主功能2 → `2` → `3` → `8`

输入要求：`examples\H2O2.fch`。

操作步骤（梯度图，原始格式）：

```text
examples\H2O2.fch
4  // Plotting plane map
1  // Electron density
6  // Gradient line with/without contour line map
[Press ENTER button to use default grid setting]
4  // Use three atoms to define the plotting plane
2,1,3  // Define the plane by nuclear positions of atoms 2, 1 and 3
```

操作步骤（拓扑分析产生 CP 与键径，原始格式）：

```text
-5  // Return to main menu
2  // Topology analysis
2  // Search CPs from nuclear positions
3  // Search CPs from midpoint of atomic pairs
8  // Generating the paths connecting (3,-3) and (3,-1) CPs, namely bond paths
0  // Visually check (optional)
-10  // Return to main menu
```

再按上法重画梯度图即叠加 CP/键径。拉普拉斯等值线叠加版（原始格式）：

```text
4  // Plotting plane map
3  // Laplacian of electron density
2  // Contour line map
[Press ENTER button to use default grid setting]
4  // Use three atoms to define the plotting plane
2,1,3
```

产出：棕/蓝/橙圈为 (3,-3)/(3,-1)/(3,+1) CP，深棕粗线为键径，深蓝线为盆间路径；后处理选项 11–14 调梯度线光滑度/密度/颜色，选项 `7` 设盆间路径步长与迭代数。

来源：[4.4.6](sec-4-4-output-and-plot-various-properties-in-a-plane.md#446-过氧化氢电子密度的梯度等值线图及拓扑路径)；视频 <https://youtu.be/gv5FkiFWUY0>。

## 实例：乙酰氯电子密度变形图

说明：变形图＝实际密度 − 自由原子密度之和；选 `-2` 后 Multiwfn 自动调 Gaussian 算原子波函数并球化，存 `wfntmp` 文件夹（可复用；`examples\atomwfn` 有前四周期 6-31G* 原子波函数，直接复制到当前目录可免调 Gaussian；重于 Kr 的元素须手算原子 `.wfn` 入 `atomwfn`）。

菜单路径：主功能4 → `-2` 变形图

输入要求：`examples\CH3COCl.wfn` ＋ Gaussian 可用（`settings.ini` 的 `gaupath` 设好则不每次询问）。

操作步骤（原始格式）：

```text
examples\CH3COCl.wfn
4  // Plot plane map
-2  // Tell Multiwfn you want to draw deformation map
B3LYP/6-31G*  // The level used to generate atomic wavefunction files by Gaussian
D:\study\g09w\g09.exe  // Path of Gaussian executable (skip if gaupath set)
1  // Electron density function
2  // Contour map
[Press ENTER button to use default grid setting]
1
0  // The XY plane with Z=0 is the plane of acyl chloride
```

产出：变形等值线图；密度向成键区集中，Cl 周围明显偏离球形（sp³ 杂化特征）。

来源：[4.4.7](sec-4-4-output-and-plot-various-properties-in-a-plane.md#447-乙酰氯电子密度的变形图)；原子波函数生成见 [3.7.3](sec-3-7-custom-operation-promolecular-and-deformation-properties.md)。

## 实例：水四聚体相对单体的密度/ELF 差值图

说明：配合物减四个单体；单体坐标取自配合物且均用 `nosymm`，否则差值无意义。

菜单路径：主功能4 → `0` 自定义操作 → 输入四个 `-` 文件

输入要求：`examples\water_tetramer\wfn\complex.wfn` ＋ `water1/2/3/4.wfn`。

操作步骤（密度差等值线图，原始格式）：

```text
examples\water_tetramer\wfn\complex.wfn
4  // Plot plane map
0  // Custom operation
4  // Four files will be operated on the firstly loaded system
-,examples\water_tetramer\wfn\water1.wfn
-,examples\water_tetramer\wfn\water2.wfn
-,examples\water_tetramer\wfn\water3.wfn
-,examples\water_tetramer\wfn\water4.wfn
1  // Electron density
2  // Contour map
[Press ENTER to use default grid setting]
4  // Define plane by three atoms
7,10,1
```

后处理发表风格（原始格式）：

```text
3  // Change contour line settings
15  // Set line style and width suitable for publication
1  // Save and return
17  // Set distance threshold for showing atom labels
0.2
y
0  // Save the plot as graphic file in current folder
```

操作步骤（ELF 差填充色图，原始格式）：

```text
-5  // Return to main menu
4  // Plot plane map
0  // Custom operation
4
-,examples\water_tetramer\wfn\water1.wfn
-,examples\water_tetramer\wfn\water2.wfn
-,examples\water_tetramer\wfn\water3.wfn
-,examples\water_tetramer\wfn\water4.wfn
9  // ELF
1  // Color-filled map
[Press ENTER button]
4  // Define plane by three atoms
7,10,1
```

后处理改色标（原始格式）：

```text
1  // Set lower&upper limit of color scale
-1.5,0.1
4  // Disable showing atomic labels
4  // Enable showing atomic labels again
3  // Blue labels
-1  // Show the graph again
```

产出：密度差图红实/蓝虚线表密度增减；ELF 差图深蓝区表分子间区定域降低（Pauli 排斥）。

来源：[4.4.8](sec-4-4-output-and-plot-various-properties-in-a-plane.md#448-绘制水四聚体相对其组成单体的电子密度和-elf-差值图)。

## 实例：卟啉 LOL-π 图

说明：先经主功能100子功能22自动识别 π 轨道并清零其余占据，再在分子平面上 1.2 Bohr 处作图。

菜单路径：主功能100 → `22` → 主功能4 → `10` LOL

输入要求：卟啉 `.fch`（B3LYP/6-31G*，下载 <http://sobereva.com/multiwfn/extrafiles/porphyrin.rar>）。

操作步骤（原始格式）：

```text
100  // Other functions
22  // Detect π orbitals
0  // Detect π orbitals for delocalized orbitals of exactly planar system
2  // Set occupation number of all other orbitals to zero
0  // Return to main menu
4  // Plot plane map
10  // LOL
1  // Color-filled map
[Press ENTER button]  // Use default grids
3  // Plot YZ plane
1.2  // X=1.2 Bohr
```

后处理（原始格式）：

```text
1  // Set lower&upper limit of color scale
0,0.66
4  // Enable showing atom labels
7  // Cyan color
17  // Set distance threshold for showing atom labels
2
y
8  // Enable showing bonds
14  // Brown color
-1  // Replot
```

产出：LOL-π 填充色图；高值（红/橙）区即优势离域路径，与诱导电流路径一致；另有等值线间填色＋Viridis＋pdf 矢量导出做法，输入序列见 4.4.9 后半。

来源：[4.4.9](sec-4-4-output-and-plot-various-properties-in-a-plane.md#449-绘制卟啉的-lol-π-图以揭示有利的电子离域路径)。

## 实例：LiF 电场梯度线图与矢量场图

说明：电场为 ESP 负梯度；梯度线图箭头实际应反向理解，矢量场图用选项13反转箭头使其指向电场方向。

菜单路径：主功能4 → `12` ESP → `6` 梯度线图 / `7` 矢量场图

输入要求：`examples\LiF.wfn`。

操作步骤（梯度线图，原始格式）：

```text
examples\LiF.wfn  // Generated at B3LYP/6-31G* level
4  // Plot plane map
12  // ESP
6  // Gradient line map
[Press ENTER button to use default grid setting]
0  // Modify extension distance
6  // 6 Bohr
3  // YZ plane
0  // X=0
```

后处理（原始格式）：

```text
15  // Show a contour line to reveal van der Waals surface
10  // Show arrow on the gradient lines
```

操作步骤（矢量场图，原始格式）：

```text
-5  // Return to main menu
4  // Plot plane map
12  // ESP
7  // Vector field map
50,50  // Number of grids in the two dimensions
3  // YZ plane
0  // X=0
```

后处理（原始格式）：

```text
11  // Map color to arrows
10  // Set upper limit of absolute value for scaling arrows
0.05
15  // Show a contour line to reveal van der Waals surface
13  // Invert gradient vectors, so that the arrows will correspond to direction of electric field
1  // Disable showing atom labels and reference point
1  // Enable showing atom labels and reference point
3  // Use blue label color
```

产出：电场方向图；箭头越红场强越大，顶部半圆小场区为 ESP 最负区（电场终点）。

来源：[4.4.10](sec-4-4-output-and-plot-various-properties-in-a-plane.md#4410-绘制静电势的梯度线和矢量场图以揭示-lif-的电场)。

## 实例：Kr 原子 4p 轨道图

说明：用内置轨道波函数等值线档（`±0.01×2^(i-1)`）＋等值线间填色＋pdf 导出，得出版级轨道图。

菜单路径：主功能4 → `4` 轨道波函数 → `2` 等值线图

输入要求：`examples\atomwfn\Kr.wfn`（先用主功能0确认 4p_z 为轨道 17）。

操作步骤（原始格式）：

```text
examples\atomwfn\Kr.wfn
4  // Output and plot specific property in a plane
4  // Value of orbital wavefunction
17  // The orbital corresponding to 4p_z
2  // Contour line map
[Press ENTER button]  // Use default number of grids
0  // Modify extension distance
5  // 5 Bohr
2  // XZ plane
0  // Y=0
```

后处理（原始格式）：

```text
9  // Enable filling colors for contour lines
9  // Set status of filling colors between the contour lines
3  // Set color transition
8  // Blue-White-Red
0  // Return
3  // Change setting of contour lines
5  // Use built-in contour values suitable for special purpose
3  // Suitable for plotting orbital wavefunction (namely ±0.01*2^(i-1), i = 1-28)
1  // Save setting and return
```

改 pdf 导出（原始格式）：

```text
-3  // Change other plotting settings
10  // Set format of exporting image file
7  // pdf
0  // Return
```

最后选 `0` 保存图形。

产出：Kr 4p 填充色等值线图（pdf 矢量）。

来源：[4.4.11](sec-4-4-output-and-plot-various-properties-in-a-plane.md#4411-绘制漂亮的-kr-原子-4p-轨道)。

## 实例：等值线上的函数极值点

说明：在电子密度等值线（`ρ=0.001`）上标 ESP 极大（红球）极小（蓝球），并输出坐标与数值。

菜单路径：主功能4 → `1` 电子密度 → `2` 等值线图 → 后处理 `19`

输入要求：`examples\phenol.wfn`。

操作步骤（原始格式）：

```text
examples\phenol.wfn
4  // Plot plane map
1  // Electron density
2  // Contour line map
[Press ENTER button]  // Use default number of grids
1  // XY plane
0  // Z=0
```

后处理（原始格式）：

```text
19  // Enable showing extrema of a function on a contour line
0.001  // Isovalue of present function (i.e. electron density)
12  // ESP
-1  // Replot plane map
```

产出：极值点图＋控制台极值表（示例输出 `Minimum found at -2.757166 -6.243420 Value: 0.0124521154` 等，共 5 极大 5 极小）；三维分子表面极值用主功能12（见 4.12.1）。

来源：[4.4.12](sec-4-4-output-and-plot-various-properties-in-a-plane.md#4412-在等值线上显示函数的极值点)。
