# 主功能0：显示分子结构与查看轨道/等值面

功能概述：主功能 0 是 Multiwfn 启动后查看体系几何与轨道等值面的入口。载入文件后文本窗口打印原子信息与特征轨道信息（如 HOMO/LUMO 编号、HOMO-LUMO 能隙），GUI 窗口显示分子结构。若输入文件含轨道信息，可在右下角列表选轨道或直接输入编号查看轨道等值面；若输入为 `.cub`/`.grd`，可直接查看格点数据等值面。视角、绘制风格、成键判据、等值面质量与风格、双轨道叠加、几何测量、片段操作、批量出图等均在此完成。

## 子功能/选项：查看分子轨道等值面

说明：以环庚三烯为例，载入 `.fch` 后进主功能 0，在 GUI 右下角选轨道序号或直接输入编号查看轨道。绿色/蓝色分别对应正值/负值部分，可拖动等值面值滑条或经 `Other settings` → `Set isovalue` 输入数值。

菜单路径：主菜单 → `0`（显示分子结构与查看轨道/等值面）

输入要求：含 GTFs 与轨道信息的波函数文件（如 `.fch`）；仅看结构只需原子坐标。

操作步骤（原始格式）：

```text
examples\cycloheptatriene.fch
0  // 进入 GUI
```

继续在 GUI 右下角列表选轨道序号，或在文本框输入编号后回车；非限制性开壳层输入负序号选 beta 轨道（如 `-5` 对应第 5 个 beta 轨道）；R/U/RO 波函数可直接输入轨道标记（如 `h` 为 HOMO，`l+2` 为 LUMO+2，`la` 为 alpha LUMO，`hb-3` 为 beta HOMO-3）。

产出：GUI 中显示轨道等值面；经 `Orbital info.` → `Show all`（或 `Show up to LUMO+10`/`Show occupied orbitals`）在控制台打印轨道能量、占据数与类型。

来源链接：[3.2](sec-3-2-showing-molecular-structure.md) · [4.0.1](sec-4-0-view-orbitals-and-structure.md)

## 子功能/选项：轨道显示质量与风格、波函数/密度切换

说明：默认格点较粗糙，经 `Isosur. quality` 提高质量（也可用 `settings.ini` 的 `nprevorbgrid` 设默认值，注意调整后当前等值面会被删除）。等值面风格经 `Isosur#1 style` 修改（实面/网格/点/实面+网格/透明面），颜色经对应子选项按 RGB 分量（0.0–1.0，如 `1.0,0.0,0.0` 为纯红）依次输入正值/负值部分（默认由 `settings.ini` 的 `isoRGB_same`/`isoRGB_oppo` 控制）。Rydberg 等弥散轨道经 `Other settings` → `Set extension distance` 增大盒子外延（默认由 `Aug3D` 控制，如输入 `12`，单位 Bohr）。绘制概率密度经 `Other settings` → `Choose plotting wavefunction or density` → `Density`。

菜单路径：主功能 `0` → 右下角轨道列表 / `Isosur. quality` / `Isosur#1 style` / `Other settings`

输入要求：同上。

操作步骤（原始格式）：

```text
0
[在 GUI 右下角选轨道] → Isosur. quality → 设 high-quality / very high-quality
Other settings → Set extension distance → 12
Other settings → Choose plotting wavefunction or density → Density
```

产出：更光滑的等值面；Rydberg 轨道不被截断；或显示概率密度而非波函数。

来源链接：[3.2](sec-3-2-showing-molecular-structure.md) · [4.0.1](sec-4-0-view-orbitals-and-structure.md)

## 子功能/选项：同时显示两个轨道（等值面 #1 + #2）

说明：分析两个 NBO 相位重叠等情形时有用。先选定一个轨道（等值面 #1），此时 `Show+Sel. Isosur#2` 复选框被激活，勾选后再选新轨道即与之前轨道同显（等值面 #2，黄绿色/紫色分别对应正值/负值）。取消勾选则 #2 消失，重勾则重绘。两者风格经 `Isosur. #1`/`Isosur. #2` 各自子选项分别调整。

菜单路径：主功能 `0` → 选轨道 → `Show+Sel. Isosur#2` → 再选轨道

输入要求：含轨道信息的文件；实例用 NBO plot 文件。

操作步骤（原始格式）：

```text
examples\NH2COH.31
examples\NH2COH.37
0  // Enter the GUI
```

```text
[在列表选 12 绘制 NBO 12] → 勾选 Show+Sel. isosur#2 → 点击列表中的 56
[Isosur#1 style / Isosur#2 style → Use mesh，便于观察重叠；也可试 transparent face]
```

产出：NBO 12（氮孤对）与 NBO 56（C–O 反 π*）同屏显示，可直观判断重叠与离域强度。

来源链接：[3.2](sec-3-2-showing-molecular-structure.md) · [4.0.2](sec-4-0-view-orbitals-and-structure.md)

## 子功能/选项：查看 NBO/NHO/NAO（plot 文件方式 / .fch 载体方式）

说明：方式 1 用 Gaussian `pop=nboread` + 输入文件末尾 `$NBO plot file=C:\NH2COH $END` 生成 `.31`~`.41`，载入 `.31`（基函数信息）+ `.37`（NBO 信息）后查看。方式 2 在 Gaussian 输入加 `pop=saveNBO`，NBO 存入 checkpoint，用对应 `.fch` 直接查看（HF/DFT 首行加 `saveNBOene`，post-HF 加 `density` 时首行加 `saveNBOocc`）。

菜单路径：主功能 `0`（载入 `.31`+`.37`，或载入含 `saveNBO` 的 `.fch`）

输入要求：NBO plot 文件（`.31`~`.41`，Gaussian 用 `pop=nboread` + `plot` 产生）；或含 `saveNBO` 的 `.fch`。

操作步骤（原始格式）：

```text
examples\NH2COH.31  // .31 file contains necessary basis function information for plotting
examples\NH2COH.37  // .37 file contains NBO information. .32~.40 files correspond to PNAO/NAO/PNHO/NHO/PNBO/NBO/PNLMO/NLMO/MO respectively. Hint: You can only input 37, because in present example the .37 and the .31 file share the same name
0  // Enter the GUI
```

注意 Gaussian 存盘可能重排 NBO 顺序，如输出出现：

```text
Reordering of NBOs for storage:     7    8    3    1    2    4    6    5    9   38 ...
```

即 `.chk`/`.fch` 中第 1、2、3… 个轨道实际对应 NBO 模块产生的第 7、8、3… 个 NBO。

产出：可在列表中选 NBO/NAO/NHO 等序号查看等值面；可联用 VMD 绘制出版级 NBO 图。

来源链接：[4.0.2](sec-4-0-view-orbitals-and-structure.md)

## 子功能/选项：改变视角与绘制设置

说明：左键拖拽旋转；Ctrl+水平拖拽沿屏幕旋转、Ctrl+垂直拖拽缩放；Shift+拖拽平移（Linux 先单击绘图区使图标变手形）。右侧 `Left/Right/Up/Down` 旋转视角，滚轮缩放；`Set view` → `Set rotation of viewpoint` 精确输入旋转角。`Ratio of atomic size` 为显示原子半径四分之一与 vdW 半径之比（拖到 4.0 即显示 vdW 表面）；`Other settings` 下 `Use CPK style`/`Use vdW style`/`Use line style` 切换预设风格。成键按经验判据（距离短于 CSD 共价半径和 1.15 倍则成键），`Bonding threshold` 滑条可调；`.mol`/`.mol2` 直接用自带连接信息。

菜单路径：主功能 `0` → 右侧视角按钮 / `Set view` / `Other settings` / `Bonding threshold` 滑条

输入要求：原子坐标。

操作步骤（原始格式）：

```text
0
[Other settings → Use CPK style / Use vdW style / Use line style]
[拖拽 Bonding threshold 滑条调整成键判据]
[Set view → Set rotation of viewpoint 输入旋转角度]
```

产出：视角与风格按需调整；键连线、原子标签/颜色按 `settings.ini`（`bondRGB`、`atmlabRGB`、`atmcolorfile`，改后重启生效）或 `Other settings` → `Set atomic label color` 实时修改。

来源链接：[3.2](sec-3-2-showing-molecular-structure.md)

## 子功能/选项：Tools——几何测量、片段识别、元素查询、坐标/内坐标导出

说明：`Measure geometry` 输入 2/3/4 个原子编号回车，返回键长/键角/二面角；`Select fragment` 输入一原子编号，高亮其所在片段并返回全部原子编号；`Get atom indices of a given element` 输入元素名返回全部属该元素的原子编号；`Print XYZ coordinates` 显示 Å 单位坐标；`Export all internal coordinates` 导出全部键角二面角到 `int_coord.txt`（无 GUI 版进主菜单输入 `geomparm` 导出到指定文件）。

菜单路径：主功能 `0` → `Tools` → `Measure geometry` / `Select fragment` / `Get atom indices of a given element` / `Print XYZ coordinates in Angstrom` / `Export all internal coordinates`

输入要求：原子坐标（`.mol`/`.mol2` 直接用自带连接信息）。

操作步骤（原始格式）：

```text
0 → Tools → Measure geometry → [输入两个/三个/四个原子序号并按 ENTER]
0 → Tools → Select fragment → [输入一个原子编号]
0 → Tools → Batch plotting orbitals
[无 GUI 版] geomparm
```

产出：键长/键角/二面角数值；片段原子编号；`int_coord.txt`。

来源链接：[3.2](sec-3-2-showing-molecular-structure.md)

## 子功能/选项：Tools——批量绘制轨道图

说明：经 `Batch plotting orbitals` 把大量选定轨道分别存为当前文件夹图片文件。

菜单路径：主功能 `0` → `Tools` → `Batch plotting orbitals`

输入要求：含轨道信息的波函数文件。

操作步骤（原始格式）：

```text
0 → Tools → Batch plotting orbitals
```

视频演示见 <https://youtu.be/SHwrQhqBHZ0>。

产出：每个选定轨道一张图像文件。

来源链接：[3.2](sec-3-2-showing-molecular-structure.md) · [4.0.1](sec-4-0-view-orbitals-and-structure.md)

## 子功能/选项：Multiwfn+VMD 高质量轨道等值面（showorb 脚本流程）

说明：用脚本联用 Multiwfn 与 VMD：`showorb.bat` 调用 Multiwfn 算选定轨道格点并导出 `orb??????.cub` 后移到 VMD 文件夹；`showorb.txt` 为输入流文件（第三行设轨道序号如 `54-59`，第四行设格点质量）；`showorb.vmd` 在 VMD 定义 `orb`/`orbiso`/`orbclean` 命令；`VMDrender.txt` + `VMDrender_full.bat`（或去阴影的 `VMDrender_noshadow.bat`）经 Tachyon 渲染出版级图片。

菜单路径：主功能 `0` 之外的工作流：静默 Multiwfn（`showorb.bat`+`showorb.txt`）→ VMD（`orb`/`orbiso`）→ Tachyon 渲染

输入要求：`.fch`/`.fchk`（实例为 `examples\excit\D-pi-A.fchk`）+ VMD 1.9.3。

操作步骤（原始格式）：

```text
-10
12
```

上两行加在 `showorb.txt` 第三、四行之间时，把延伸距离增大到 12 Bohr（Rydberg 轨道可视化必需）。VMD 控制台命令：

```text
orb 56
orbiso 0.02
orbclean
```

渲染流程：VMD 绘好轨道 → 把 `examples\scripts\VMDrender.txt` 全文粘到 VMD 控制台 → VMD 选 `File` → `Render` → `Tachyon` → `Start Rendering`（得 `vmdscene.dat`）→ 把 `examples\scripts\VMDrender_full.bat` 复制到 VMD 文件夹 → 双击运行得 `full.bmp`。

产出：`orb000054.cub` 等轨道 cube 文件；VMD 中红色/蓝色（正/负相）等值面；Tachyon 渲染的出版级图片。

来源链接：[4.0.3](sec-4-0-view-orbitals-and-structure.md)
