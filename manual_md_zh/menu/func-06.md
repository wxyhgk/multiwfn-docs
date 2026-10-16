# 主功能6：检查和修改波函数

功能概述：主功能6提供大量检查与修改已载入波函数的子功能，所有修改立即生效，返回主菜单后一切后续分析都受影响，界面标题显示当前 GTF 数、轨道数、原子数与 α/β/总电子数。修改前可用子功能 1–7 检查内容是否正确，改完用子功能 0 存为 `new.wfn`（零占据轨道与无 GTF 原子自动丢弃），其它格式经主功能100子功能2转存。片段丢弃（-3/-4）不可逆，改错只能重启重载。

## 检查波函数内容（子功能1–7）

说明：打印 GTF、基函数、轨道与矩阵信息，用于检查线性依赖与波函数正确性；修改后用它们验证操作。

菜单路径：主功能6 → 子功能 `1` / `2` / `3` / `4` / `5` / `6` / `7`

输入要求：波函数文件；子功能 2、5、6、7 需含基函数信息。

操作步骤（原始格式）：

```text
子功能 1：打印全部 GTF 信息（所属中心、GTF 类型、指数）。
子功能 2：打印全部基函数信息（归属壳层/中心、类型、GTF 序号范围）。
子功能 3：打印全部轨道基本信息（能量、占据数、轨道类型 Alpha/beta/alpha+beta）。
子功能 4：打印某轨道详细信息（相对 GTF 的展开系数连同 GTF 信息，系数含 GTF 归一化常数）。
子功能 5：打印基函数表示下的系数矩阵（非相对 GTF 的系数）。
子功能 6：打印基函数表示下的单粒子密度矩阵。
子功能 7：打印基函数间各种积分矩阵（重叠、电磁偶极矩、动能、速度、电四极矩和八极矩）；
   重叠矩阵一并打印本征值，可用于检查线性依赖。
```

产出：屏幕打印的各类检查信息。

来源：[3.8](sec-3-8-checking-and-modifying-wavefunction.md)；[MENU_INDEX.md](MENU_INDEX.md)。

## 定义片段丢弃无关 GTF（子功能-3/-4）

说明：中心不在片段内的 GTF 被丢弃（相当于相应轨道 GTF 系数置零），后续一切用 GTF 的分析（尤其格点计算）加速，或只取片段贡献。可与主功能 1–6 安全联用；其它任务不懂勿用；不可逆。

菜单路径：主功能6 → `-3` 按原子序号定义片段 / `-4` 按排除原子定义片段

输入要求：波函数文件（GTFs ＋原子坐标）。

操作步骤（原始格式）：

```text
-3：直接输入原子序号定义片段。
-4：输入要排除的原子序号，其余原子构成片段。
中心不属于该片段的 GTF 将被丢弃。注意不可逆，被丢弃的 GTF 无法恢复，
除非重启程序并重新载入波函数文件。
```

产出：内存中片段化波函数；典型用法见本文件"实例：去原子贡献"与 func-04 去贡献平面图实例。

来源：[3.8](sec-3-8-checking-and-modifying-wavefunction.md)；实例 [4.4.3 例1](sec-4-4-output-and-plot-various-properties-in-a-plane.md#443-绘制不含某些原子贡献的平面图)。

## 修改 GTF 与轨道系数/占据数/能量（子功能11/21–30/36）

说明：交换或设定 GTF 中心/类型/指数/系数、轨道占据数/能量/相位。最常用的是子功能 26 置零占据数以屏蔽轨道贡献，以及子功能 28 修正轨道能量以画 DOS。

菜单路径：主功能6 → 子功能 `11` / `21`–`26` / `28`–`30` / `36`

输入要求：波函数文件。

操作步骤（原始格式）：

```text
子功能 11：交换两个 GTF 的中心、类型、指数或轨道展开系数，或一次交换两个 GTF
   的全部信息（相当于交换记录顺序，不影响任何分析结果）。
子功能 21 至 24：分别设定某轨道中特定 GTF 的中心、类型、指数和展开系数。
子功能 25：将某些轨道中某些 GTF 的展开系数设为特定值。同时满足三个输入条件
   的 GTF 被选中：GTF 序号范围、GTF 所在原子序号范围、GTF 类型（具体类型如
   YZ、XXZ，或角动量如 S、P、D）。含基函数信息时还可设基函数展开系数。
   细节与例子见 4.6.1 节。
子功能 26：设定某些轨道占据数（直接设值，或加/减/乘/除给定值）。屏蔽某些轨道
   对实空间函数贡献即将其占据数置零。细节与例子见 4.6.2 节。
子功能 28：设定某些轨道能量（直接设值，或加/减/乘/除）。适用于画 DOS 前按给定
   关系（如 J. Am. Chem. Soc., 121, 3414 (1999)）修正轨道能量。
子功能 29：输入两个轨道序号，交换它们的所有信息（能量、占据数、系数）。
子功能 30：交换所有轨道的能量和占据数。基于 EDDB 程序 .fchk 画 EDDB 格点时用：
   载入 EDDB 导出的 .fchk 后选选项 1（用占据数交换以 eV 为单位的轨道能量），
   占据数即对应 NOBD 本征值，再按常规用主功能 5 算电子密度格点即得 EDDB。
子功能 36：反转某些轨道相位（基函数和 GTF 展开系数取负）。
```

产出：修改后的内存波函数（用子功能 3/4 验证占据数与系数）。

来源：[3.8](sec-3-8-checking-and-modifying-wavefunction.md)；实例 [4.6.1](sec-4-6-modify-and-check-wavefunction.md#461-删除特定的高斯函数)、[4.6.2](sec-4-6-modify-and-check-wavefunction.md#462-价层电子密度分析去掉某些轨道对实空间函数贡献的例子)。

## 平移/复制/旋转波函数与坐标（子功能31–33）

说明：平移整个波函数与坐标，或平移复制原胞波函数建超胞（粗糙近似，忽略相邻原胞轨道混合），或做 X→Y→Z 旋转。周期体系分析推荐 Multiwfn 联用 CP2K（见 2.9.2）。

菜单路径：主功能6 → `31` 平移 / `32` 平移复制 / `33` 旋转

输入要求：波函数文件（GTFs ＋原子坐标）；PBC 原胞 `.fch`。

操作步骤（原始格式）：

```text
子功能 31：输入平移矢量及其单位，平移整个波函数和所有原子坐标。
子功能 32：输入平移矢量、单位、按该矢量平移复制的次数。适用于把 Gaussian PBC
   原胞波函数扩展为超胞波函数（直接算超胞耗时多得多）。注意只是近似。
子功能 33：旋转波函数，即 X→Y、Y→Z、Z→X。
```

完整超胞例子输入序列见本文件"实例：石墨烯超胞"。

来源：[3.8](sec-3-8-checking-and-modifying-wavefunction.md)；实例 [4.6.3](sec-4-6-modify-and-check-wavefunction.md#463-平移和复制石墨烯原胞波函数到周期体系)。

## 按轨道类别丢弃贡献（子功能34/35/37/38）

说明：一键清零核轨道、按 IRREP 丢弃、R/RO 转 U、整数占据 Aufbau 化。注意适用文件类型限制。

菜单路径：主功能6 → `34` / `35` / `37` / `38`

输入要求：波函数文件；子功能 35 仅 `.mwfn`/`.molden`/`.gms` 且限 SCF 波函数。

操作步骤（原始格式）：

```text
子功能 34：将所有内层分子轨道占据数置零，只留价轨道贡献。内层 MO 数自动判定，
   用赝势的原子不计入。
子功能 35：丢弃某种 IRREP 轨道贡献。进入后显示全部占据轨道 IRREP（"N_orb" 为
   该 IRREP 占据轨道数）；选项 1 输入 IRREP 序号则相应轨道占据置零（状态变
   "discarded"）；选项 0 保存并退出；选项 2 恢复原始占据；选项 3 反转各 IRREP
   的 Normal/Discarded 状态。仅 .mwfn/.molden/.gms（很多程序 .molden 缺 IRREP
   或不正确），仅限制性/非限制性 SCF 波函数。
子功能 37：将 R 或 RO 波函数转非限制性：每个空间轨道拆为能量形状相同、占据
   可能不同的 α 和 β 轨道。适用于基于 ROKS 波函数的 CDA（见 4.16.4 节乙烷例）。
子功能 38：使占据为整数并满足 Aufbau（如 2.0 1.95 1.93 0.09 0.03 0.0 变为
   2.0 2.0 2.0 0.0 0.0 0.0）；电子数为整数且原判为多行列式时自动改单行列式。
   假设轨道已按能量升序排列。
```

产出：类别过滤后的内存波函数。

来源：[3.8](sec-3-8-checking-and-modifying-wavefunction.md)。

## 保存修改后的波函数（子功能0）

说明：全部修改完成后保存；想存其它格式先回主菜单经主功能100子功能2。

菜单路径：主功能6 → `0`；或主菜单 → 主功能100 → 子功能 `2`

输入要求：内存中的波函数。

操作步骤（原始格式）：

```text
子功能 0：将当前波函数保存为当前目录 new.wfn（占据数为零的轨道和不具有 GTF
的原子自动丢弃）。若想存其它格式，先返回主菜单，再进主功能 100 的子功能 2
选相应选项保存。
```

产出：`new.wfn` 或其它格式波函数文件。

来源：[3.8](sec-3-8-checking-and-modifying-wavefunction.md)。

## 实例：删除特定高斯函数

说明：子功能 25 按（GTF 序号范围、归属原子范围、GTF 类型）三条件筛选后置零系数；选项 4 可查看系数验证。

菜单路径：主功能6 → `25` → `0` 存盘

输入要求：`examples\phenol.wfn`。

操作步骤（原始格式）：

```text
examples\phenol.wfn
6  // Modify wavefunction
25  // Set the coefficients of some GTFs that satisfied certain conditions
0,0  // GTF index range ALL
2,4  // Only GTFs attributed to atoms 2, 3, 4
Z  // Only reserve Z-type GTFs
23,23  // Only orbital 23
0  // Set coefficients of selected GTFs in orbital 23 to zero
0  // Save current wavefunction to new.wfn in current directory
```

产出：`new.wfn`；对比修改前后轨道 23 等值面（分子面平行 XY，Z 型删后相应部分消失）。看修改后轨道：关 Multiwfn 重载 `new.wfn`，或选 `-1` 回主菜单进主功能0画等值面。

来源：[4.6.1](sec-4-6-modify-and-check-wavefunction.md#461-删除特定的高斯函数)。

## 实例：价层电子密度分析（HCN 填充色图 / 乙烷等值面）

说明：将内层 MO 占据置零即得价层密度（电子密度、动能密度等线性函数可分解到轨道；ELF/LOL 非线性不能分解）。手动做法用于 HCN，子功能 34 一键做法用于乙烷；同法分离 ELF-σ/ELF-π。

菜单路径：主功能6 → `26` / `34` → 主功能4/5/2/17 分析

输入要求：`examples\HCN.wfn` / `examples\ethane.wfn`。

操作步骤（例1 HCN：C、N 各一个内层轨道，前两个 MO 置零，原始格式）：

```text
examples\HCN.wfn
6  // Modifying wavefunction
26  // Set occupation numbers
1,2  // Select MOs 1 and 2
0  // Set their occupation numbers to zero
q  // Return to last menu
-1  // Return to main menu
```

再按常规用主功能4画电子密度填充色图（见 4.4）：C–N/C–H 成键区与 N 孤对清晰，C/N 中心白小圈为价轨道向芯区穿透所致。

操作步骤（例2 乙烷一键清零内层，原始格式）：

```text
examples\ethane.wfn
6  // Modify wavefunction
34  // Set occupation number of inner orbitals to zero
-1  // Return to main menu
5  // Calculate grid data and visualize isosurface map
1  // Electron density
3  // High-quality grid
-1  // Show isosurface map
```

等值面取 0.25 并关结构显示：内层电子与 C–C/C–H 成键电子清晰呈现。

产出：价层电子密度平面图/等值面图；也可对价层密度做拓扑（主功能2）与盆分析（主功能17）。

来源：[4.6.2](sec-4-6-modify-and-check-wavefunction.md#462-价层电子密度分析去掉某些轨道对实空间函数贡献的例子)；价层分析综述 *Acta Phys.-Chim. Sin.* **34**, 503 (2018)。

## 实例：平移复制石墨烯原胞波函数建超胞

说明：Gaussian PBC 输入 `TV` 给平移矢量（route 如 `#P PBEPBE/3-21g/Auto SCF=Tight`，formchk 得 `graphene.fch`）；若 PBC 计算未加 `nosymm`，Gaussian 可能标准取向，此时平移矢量以后 `.fch` 的 Translation vectors（或输出文件 PBC vector）为准，不用输入文件原值。

菜单路径：主功能6 → `32`

输入要求：`examples\graphene.fch`。

操作步骤（原始格式）：

```text
examples\graphene.fch
6  // Modify wavefunction
32  // Translate and duplicate primitive cell wavefunction
2.475315,0.0,0.0  // Translation vector 1
2  // Unit is Å
3  // Translate and duplicate present system three times in this direction
32  // Current system already has four primitive cells, translate and duplicate in another direction
-1.219952,2.133447,0.0  // Translation vector 2
2  // Unit is Å
3  // Translate and duplicate present system three times in this direction
```

Gaussian 输入坐标部分示例：

```text
C                  0.000000    0.000000    0.000000
C                  0.000000    1.429118    0.000000
TV                 2.475315    0.000000    0.000000
TV                -1.219952    2.133447    0.000000
```

产出：16 原胞超胞波函数；中央区 LOL 显示正确周期特征，边界仍不对（可继续扩大）。

来源：[4.6.3](sec-4-6-modify-and-check-wavefunction.md#463-平移和复制石墨烯原胞波函数到周期体系)。
