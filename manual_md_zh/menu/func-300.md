# 主功能300：其它功能，第三部分

功能概述：主功能 300 是 Multiwfn“其它功能”的第三部分，共 8 个子功能（编号 1、2、4、5、6、7、8、9；编号 3 空缺）。内容覆盖晶胞自由区域可视化与自由体积、原子径向密度拟合为 STO/GTF、STM 图像模拟、电偶极/多极矩与电子空间范围、输入 Fock 矩阵求轨道能量、几何相关操作、表面距离投影图与 Fermi 能级确定。这些功能多面向周期体系、实空间建模与实验图像模拟，输入从普通波函数文件到 `.cif`/`.pdb`/`.47` 矩阵文件不等。

## 子功能 1：查看胞中的自由区域并计算自由体积

说明：对分子动力学胞或实验晶体计算原始格点数据（格点到任一原子距离小于 Bondi vdW 半径则记为占据）与平滑格点数据（高斯/Becke/误差开关函数），等值面展示自由区域并输出自由体积与占比；支持非正交胞。选项 1 设格点并计算，2 开关周期边界，3 开关平滑数据，4 选平滑函数，5 设边界闭合，6 设 vdW 半径缩放。

菜单路径：主功能 `300` → 子功能 `1`。

输入要求：含胞信息的文件（如 `.cif`、`.gro`、带 CRYST1 的 `.pdb`）；无胞信息则假设正交盒。实例文件 `examples\coal.pdb`（含 `CRYST1 31.064 31.100 31.093 90.00 90.00 90.00`）、`examples\COF_12000N2.cif`。

操作步骤（原始格式，煤结构）：

```text
examples\coal.pdb
300  // Other functions (Part 3)
1  // Viewing free regions and calculating free volume in a cell
4  // Set method of smoothing
1  // Gaussian function
1.8  // FWHM of Gaussian function is 1.8 times of vdW radius, which is found to be able to result in satisfactory isosurface map of smoothed grid data for present system
1  // Set grid and start calculation
[Press ENTER button]  // Use default origin (0,0,0), which is suitable for present system
[Press ENTER button]  // Use default box lengths, which correspond to the lengths of the three sides of the present cell
[Press ENTER button]  // Use default grid space 0.25 Å, which is usually fine enough
```

COF 晶体（非正交胞，默认设置直接计算）：

```text
examples\COF_12000N2.cif
300  // Other functions (Part 3)
1  // Viewing free regions and calculating free volume in a cell
1  // Set grid and start calculation
[Press ENTER button]  // Use default origin (0,0,0)
[Press ENTER button]  // Use default box lengths
[Press ENTER button]  // Use default grid space 0.25 Å
```

产出：`Volume of entire box` 与 `Free volume`（煤 14783.074 Å³、占比 49.21%；COF 1953.217 Å³、占比 65.19%）；后处理菜单可视化等值面（默认 0.5）或导出 cube（非正交胞导出 `free_smooth.cub` 用 VMD/VESTA 渲染）。

来源链接：[3.300.1](sec-3-300-other-functions-part-3.md#33001-查看胞中的自由区域并计算自由体积)；实例 [4.300.1](sec-4-300-other-functions-part-3.md#43001-可视化晶胞中的自由区域并计算自由体积的例子)；博客 <http://sobereva.com/539>、<http://sobereva.com/617>。

## 子功能 2：将原子径向密度拟合为多个 STO 或 GTF 的线性组合

说明：把 $\rho(r) \approx \sum_i c_i e^{-\zeta r}$（STO）或 $\sum_i c_i e^{-\zeta r^2}$（GTF）用 Levenberg-Marquardt 算法拟合球平均原子径向密度；拟合类别可选绝对误差/相对误差（默认，推荐）/RDF 误差；指数可固定或优化；自动删除冗余函数并按电子数缩放系数。常用流程：载入原点处单原子波函数 → 子功能 2 → 选项 3 设初猜 → 选项 1 拟合 → 检查 RMSE、$r^2$、曲线与积分。

菜单路径：主功能 `300` → 子功能 `2`。

输入要求：单原子波函数文件（GTF，原子须在原点），如 `examples\atomwfn\Si.wfn`、`Br.wfn`（ROHF/6-31G*）。

操作步骤（原始格式，Si 粗拟合）：

```text
examples\atomwfn\Si.wfn  // Generated at ROHF/6-31G* level
300  // Other functions (Part 3)
2  // Fitting atomic radial density as multiple STOs or GTFs
3  // Check or set initial guess of coefficients and exponents of fitting functions
2  // Set initial guess as "crude fitting by a few STOs with variable exponents". Then from screen you can find only four STOs will be employed in the fitting, their initial status are
```

```text
           Coefficient       Exponent
STO  1:    1.000000E+03    2.700000E+01
STO  2:    3.000000E+02    9.000000E+00
STO  3:    2.000000E+01    3.000000E+00
STO  4:    1.000000E+00    1.000000E+00
```

```text
0  // Return to upper level of menu
1  // Start fitting
```

拟合函数初猜文件格式（选项 1 载入，第一、二列为系数与指数）：

```text
4.0 1000
2.0 100
1.0 1.5
```

产出：拟合系数与指数、缩放因子、RMSE 与 Pearson $r$/$r^2$（Si 用 4 STO 得 $r^2=0.9907$；Br 用 30 GTF 固定指数得 $r^2=0.9994`，指数相近者可经选项 10 合并重拟合）；拟合后选项支持对数曲线可视化、导出 `fitdens.txt`、多求积点积分检验与 Fortran 代码输出。

来源链接：[3.300.2](sec-3-300-other-functions-part-3.md#33002-将原子径向密度拟合为多个-sto-或-gtf-的线性组合)；实例 [4.300.2](sec-4-300-other-functions-part-3.md#43002-将原子径向密度拟合为-sto-或-gtf-的例子)。

## 子功能 4：模拟扫描隧道显微镜（STM）图像

说明：基于 Tersoff-Hamann 模型，$I(\mathbf{r}) \propto \sum |\varphi_i(\mathbf{r})|^2$（V<0 取 $E_F+eV\to E_F$ 占据轨道，V>0 取 $E_F\to E_F+eV$ 非占据轨道），$E_F$ 默认取 HOMO/LUMO 平均；支持恒高模式（固定 Z 平面算电流）与恒流模式（选项 1 切换，算三维 LDOS 再定电流求 $z_c(x,y)$）。仅 HF/KS-DFT（禁双杂化与多组态），分子须平行 XY 平面（菲 `examples\phenanthrene.fch` 在 YZ 平面，需先经主功能 6 子功能 33 两次旋转至 Z=0 平面并经主功能 100 子功能 2 存为 `mol.mwfn`）。

菜单路径：主功能 `300` → 子功能 `4`。

输入要求：含基函数文件（HF/KS-DFT；V>0 需含非占据轨道，故纯 `.wfn` 不可用）。

操作步骤（原始格式，旋转到 XY 平面）：

```text
examples\phenanthrene.fch
6  // Check & modify wavefunction
33  // Rotate wavefunction, namely X→Y, Y→Z, Z→X
0  // Rotate all orbitals
y  // Also rotate molecule structure. Then the molecule will be on XZ plane
33  // Rotate wavefunction again
0  // Rotate all orbitals
y  // Also rotate molecule structure
```

恒高模式（V=−5.0 V、Z=1.2 Å）：

```text
mol.mwfn
300  // Other function (Part 3)
4  // Simulating STM image
```

```text
2  // Set bias voltage
-5  // Bias voltage of -5.0 V
7  // Set Z coordinate
1.2  // Z=1.2 Å
0  // Calculate tunneling current on the plane
```

恒流模式：

```text
mol.mwfn
300  // Other function (Part 3)
4  // Simulating STM image
1  // Switch the mode of STM image to constant current
2  // Set bias voltage
-5  // Again we use bias voltage of -5.0 V
```

再选选项 0 算三维 LDOS（最大 0.048 a.u.），后处理选项 3 输入电流值（如 `0.01`）得 $z_c$ 图（Z 范围 0.70–1.206 Å）。

产出：恒高 LDOS/电流平面图（4 个占据 MO 贡献，最大 0.010218 a.u.）、恒流 $z_c(x,y)$ 图与 LDOS 等值面/cube。

来源链接：[3.300.4](sec-3-300-other-functions-part-3.md#33004-模拟扫描隧道显微镜-stm-图像)；实例 [4.300.4](sec-4-300-other-functions-part-3.md#43004-模拟扫描隧道显微镜stm图像的例子)；博客 <http://sobereva.com/549>。

## 子功能 5：计算电偶极/多极矩和电子空间范围

说明：解析积分计算偶极矩 $\boldsymbol{\mu}$、四极矩（标准/无迹/球谐形式）、八极矩、十六极矩、正负电荷中心与电子空间范围 $\langle r^2\rangle$（附 XYZ 分量）；`.chg`/`.pqr` 输入则基于原子电荷计算。

菜单路径：主功能 `300` → 子功能 `5`。

输入要求：原子坐标，加 GTF/基函数或原子电荷之一。实例 `examples\uracil.wfn`。

操作步骤（原始格式）：

```text
examples\uracil.wfn
300  // Other function (Part 3)
5  // Calculate electric dipole moment and multipole moments
```

产出：偶极矩 1.884103 a.u.（4.788911 Debye）、四极/八极/十六极各形式分量与大小、$\langle r^2\rangle = 822.650952$（X/Y/Z 分量 501.33/286.86/34.46）。`settings.ini` 中 `ispecial=1` 则先平移使核偶极贡献为零。

来源链接：[3.300.5](sec-3-300-other-functions-part-3.md#33005-计算电偶极多极矩和电子空间范围)；实例 [4.300.5](sec-4-300-other-functions-part-3.md#43005-计算尿嘧啶的电偶极矩多极矩和电子空间分布范围)；博客 <http://sobereva.com/616>。

## 子功能 6：通过输入 Fock 矩阵计算当前轨道能量

说明：载入外部 Fock/KS 矩阵（纯文本、`new.fch` 反推的 `KS.txt` 或 Gaussian `.47` 文件，详见附录 7）后，把矩阵对内存中任意轨道（特别适合 NTO）求期望值得轨道能量。

菜单路径：主功能 `300` → 子功能 `6`。

输入要求：含基函数文件与 Fock/KS 矩阵纯文本文件。实例：给体-π-受体 S0→S1 的 NTO（`examples\excit\D-pi-A.fchk`/`.out`）。

操作步骤（原始格式，三步）：

```text
examples\excit\D-pi-A.fchk
18  // Electron excitation analysis
6  // Generate natural transition orbitals (NTOs)
examples\excit\D-pi-A.out
1  // The first excited state (S1 state)
```

```text
examples\excit\D-pi-A.fchk
100  // Other functions (Part 1)
17  // Generate Fock/KS matrix based on orbital energies and coefficients
KS.txt
```

```text
NTO.mwfn
300  // Other functions (Part 3)
6  // Calculate energies of the present orbitals
KS.txt
```

或用 Gaussian 输入 `# CAM-B3LYP/6-31g(d) pop=nboread`（配 `$NBO archive file=C:\D-PI-A $END`）产生 `.47` 文件直接载入。NTO 对本例贡献 99.2%；最高占据/非占据 NTO（轨道 56/57）能量为 −9.4672/−0.7101 eV，可经选项 1 导出 `orbene.txt`。

产出：内存各轨道能量与 `orbene.txt`。

来源链接：[3.300.6](sec-3-300-other-functions-part-3.md#33006-通过输入-fock-矩阵计算当前轨道能量)；实例 [4.300.6](sec-4-300-other-functions-part-3.md#43006-计算轨道能量以-nto-轨道为例)；[附录 7](sec-6-7-about-providing-fock-ks-matrix-to-multiwfn.md)。

## 子功能 7：当前体系的几何相关操作

说明：对当前体系做平移、旋转、重取向、缩放、增删原子、超胞构建等 28 类几何操作（效果可累积；选项 0 可视化，−1/−2/−3/−4 导出 `.xyz`/`.pdb`/`.gjf`/`.cif`，−9 恢复初始几何；旋转不变换轨道系数）。注意选项 14 空缺。

菜单路径：主功能 `300` → 子功能 `7`。

输入要求：原子坐标（含胞体系同时操作胞矢量；选项 19–28 需胞信息）。

操作步骤（原始格式，选项清单照搬原文）：`1 Translate selected atoms according to a translation vector`；`2 Translate the system such that the center of selected atoms is at origin`；`3 Rotate selected atoms around a Cartesian axis or a bond`；`4 Rotate selected atoms by applying a given rotation matrix`（$\mathbf{v}_{new}=\mathbf{M}\mathbf{v}_{old}$ 或 $\mathbf{w}_{new}=\mathbf{w}_{old}\mathbf{M}$）；`5 Make a bond parallel to a vector or Cartesian axis`；`6 Make a vector parallel to a vector or Cartesian axis`；`7 Make electric dipole moment parallel to a vector or Cartesian axis`（需波函数）；`8 Make longest axis of selected atoms parallel to a vector or Cartesian axis`；`9 Mirror inversion for selected atoms`；`10 Center inversion for selected atoms`；`11 Make the plane defined by selected atoms parallel to a Cartesian plane`；`12 Scale Cartesian coordinates of selected atoms`；`13 Reorder atom sequence`；`15 Add an atom`；`16 Remove some atoms`；`17 Crop some atoms`；`18 Generate randomly displaced geometries`（导出 `new.xyz`）；`19 Translate and duplicate cell (construct supercell)`；`20 Make truncated molecules by cell boundary whole`；`21 Scale cell length and atom coordinates correspondingly`；`22 Wrap all atoms outside the cell into the cell`；`23 Translate system along cell axes by given distances`；`24 Translate system to center selected part in the cell`；`25 Extract a molecular cluster (central molecule + neighbouring ones)`（判据默认 1.2，尿素 Hirshfeld 面/指纹图分析前用此提团簇）；`26 Set cell information`；`27 Add boundary atoms`；`28 Axes interconversion`。

产出：变换后的内存几何（可导出文件/超胞/分子簇/随机位移系综）。

来源链接：[3.300.7](sec-3-300-other-functions-part-3.md#33007-当前体系的几何相关操作)；博客 <http://sobereva.com/610>。

## 子功能 8：绘制表面距离投影图

说明：在每 $(x,y)$ 点从 $Z_{\mathrm{start}}$ 向 $Z_{\mathrm{end}}$ 扫描至分子表面，绘制相对高度的填充色图加等值线，直观表征位阻与表面起伏，也兼容周期固体表面。选项 1 选表面定义（promolecular 密度等值面/波函数密度等值面/vdW 球叠加），选项 2–4 设 XY 范围与格点数，选项 6–8 设 Z 扫描步数与起止，选项 9 设等值线数，选项 0 计算绘图。

菜单路径：主功能 `300` → 子功能 `8`。

输入要求：原子坐标（promolecular/vdW 表面）；波函数电子密度表面需 GTFs。实例 `examples\excit\Ru(bpy3)2+.gjf`（[Ru(bpy)₃]²⁺，已处合适取向）。

操作步骤（原始格式，默认 promolecular 0.05 a.u. 直接计算）：

```text
examples\excit\Ru(bpy3)2+.gjf
300  // Other functions (Part 3)
8  // Plot molecular surface distance projection map
```

```text
-1  // Return
1  // Set definition of molecular surface
3  // Superposition of atomic van der Waals spheres scaled by a factor
1  // We do not scale van der Waals radii in this example, so we set scale factor to 1
0  // Start calculation
0  // Show the map on screen
```

vdW 图显示 Ru 被配体深深包埋；切 0.005 a.u. 密度等值面（选项 1→1→输入 `0.005`）得更光滑的同类图。

产出：表面距离投影填充色图（默认 25 条等值线）与配体包埋 Ru 的直观证据。

来源链接：[3.300.8](sec-3-300-other-functions-part-3.md#33008-绘制表面距离投影图)；实例 [4.300.8](sec-4-300-other-functions-part-3.md#43008-为rubpy₃²-配位体绘制表面距离投影图)；博客 <http://sobereva.com/589>。

## 子功能 9：确定 Fermi 能级

说明：按 Fermi-Dirac 分布 $\eta_i = n/\{1+\exp[(E_i-E_f)/(k_BT)]\}$（限制/非限制 $n=2.0/1.0$），二分迭代调 $E_f$ 使总电子数与实际一致（偏差<1E-6，最多 1000 步）；初猜为 HOMO/LUMO 平均；T=0 K 时定义不明。

菜单路径：主功能 `300` → 子功能 `9`。

输入要求：含占据与非占据轨道文件（`.mwfn`/`.fch`/`.molden`；`.wfn` 通常无虚轨道不可用）或手写轨道能量纯文本。实例 `examples\Li6.fch`。

操作步骤（原始格式）：

```text
examples\Li6.fch
300   //Other function (Part 3)
9   //Determine Fermi level
3000   //Temperature (K)
```

输出迭代收敛于 `Fermi level is -0.09117890 Hartree -2.481104 eV`（500 K 时为 −2.476 eV，即 HOMO/LUMO 平均）。

纯文本输入格式（闭壳：第一行占据数与非占据数，后接 Hartree 能量）：

```text
5 20
 -19.138047 -0.997376 -0.514852 -0.371177 -0.291987
   0.065333 0.151203 0.756610 [...ignored] 3.307120 3.531811 3.692553
```

开壳（第一行依次为 alpha 占据、alpha 非占据、beta 占据、beta 非占据数）：

```text
6 13 4 15
-19.33565   //The first alpha orbital
 -1.18124
 -0.66585
[...ignored]
  2.13855
  2.46757
  3.40210   //The last alpha orbital
-19.30115   //The first beta orbital
 -1.09028
 -0.63075
[...ignored]
  2.49486
  3.45566   // The last beta orbital
```

产出：给定温度下的 Fermi 能级。

来源链接：[3.300.9](sec-3-300-other-functions-part-3.md#33009-确定-fermi-能级)。
