# 主功能3：在一条线上输出并绘制特定性质

功能概述：选定一个实空间函数并定义一条直线，Multiwfn 均匀取点（默认 3000 点，可经 `settings.ini` 的 `num1Dpoints` 调整；ESP 自动降为六分之一）计算函数值并弹窗显示曲线。定线有两种方式：输入两原子序号（两侧自动延长，延长距离由 `settings.ini` 的 `aug1D` 或选项 `0` 调整，默认 1.5 Bohr），或输入两端点坐标。图上右键可重设 Y 轴范围、导出 `line.txt`、存图、定位极大极小（基于已算数据点，点越密 X 越准）。灰色虚线为 Y=0；方式 2 定线时两红圈标原子核位置。

## 子功能/选项：沿两原子连线绘制自旋密度曲线（三重态甲酰胺实例）

说明：选函数 5（自旋密度），方式 1 用 C（原子 1）与 O（原子 6）核定线，图形即时显示；X 轴为线上位置，虚线 Y=0，左右红圈为所选第一/第二原子位置。关图后新菜单可存图、调 Y 轴、导出 XY 数据、重绘；选项 6 定位极值。

菜单路径：主菜单 → `3`（在一条线上输出并绘制特定性质）→ 选函数 → `1`（两原子定线）

输入要求：GTFs（核电荷 ESP 与 RDG 等 promolecular 近似除外）+ 原子坐标；实例文件 `examples\formamide-m3.wfn`。

操作步骤（原始格式）：

```text
examples\formamide-m3.wfn
3  // Main function 3, plot real space function along a line
5  // Spin density
1  // Defining the line by nuclear coordinate of two atoms
1,6  // Indices of the two atoms, carbon and oxygen atoms correspond to 1 and 6 in present example, respectively
```

选项 6 输出摘录（原始格式）：

```text
Local maximum X:    0.753677  Value:    0.20104903D-01
Local minimum X:    1.219518  Value:   -0.55161276D-02
Local maximum X:    1.503567  Value:    0.29655008D+00
Local minimum X:    2.145518  Value:   -0.70202704D-02
Local maximum X:    3.736194  Value:    0.51047629D-01
Local minimum X:    4.006988  Value:    0.18918295D-01
Local maximum X:    4.184992  Value:    0.24448996D+00
Totally found    3 local minimum,    4 local maximum
```

产出：自旋密度沿 C–O 线曲线；`line.txt`（X–Y 数据，可供 Origin 重绘）。

来源链接：[3.4](sec-3-4-outputting-and-plotting-specific-property-in-a-line.md) · [4.3.1](sec-4-3-output-and-plot-various-properties-in-a-line.md)

## 子功能/选项：定线方式 2（两端点坐标）与延伸/点数/作图设置

说明：方式 1 输两原子序号，两侧各延长（默认 1.5 Bohr，经选项 `0 Set extension distance for mode 1` 或 `settings.ini` 的 `aug1D` 调整）；方式 2 直接输两端点坐标。数据点均匀分布，默认 3000（`num1Dpoints` 调整；ESP 自动六分之一）。右键菜单可重设 Y 轴、导出 `line.txt`、存图、定位极值与 Y 等于指定值的位置。

菜单路径：主功能 `3` → `1`（两原子定线）/ 坐标方式（两端点坐标）→ 关图后选项 `0`–`11`（存图/调轴/导出/重绘/定位极值）

输入要求：同上。

操作步骤（原始格式）：

```text
0  // Adjust extension size at both sides
3  // 3 Bohr, which is larger than the default value
1  // Use two nuclei to define the line
1,2
```

```text
11  // Change length unit of the graph to Å
3  // Change range of Y axis
-3,0.1  // From -3.0 a.u. to 0.1 a.u.
10  // Set label intervals of X and Y axes
0.5,0.5
-1  // Replot
```

产出：按需延长/换单位/调轴后的曲线图；`line.txt`。

来源链接：[3.4](sec-3-4-outputting-and-plotting-specific-property-in-a-line.md) · [4.3.3](sec-4-3-output-and-plot-various-properties-in-a-line.md)

## 子功能/选项：Fermi/Coulomb/总关联空穴曲线（H₂ 实例）

说明：关联空穴涉两电子坐标，须先定参考电子位置：改 `settings.ini` 的 `refxyz`（本例 `0.0,0.0,-0.3`，单位 Bohr）；`paircorrtype` 取 1/2/3 分别画 Fermi/Coulomb/总关联空穴（闭壳层 α/β 相同，开壳层用 `pairfunctype` 选自旋，亦可选交换-关联密度或关联因子）。文件 `examples\H2_CCSD.wfn` 为 CCSD/cc-pVTZ 优化 H₂（H1 `(0.0,0.0,0.7016)`、H2 `(0.0,0.0,-0.7016)` Bohr）。图上参考点 X 可由延伸距离推算（相对 H2/H1 各延 1.5 Bohr，参考点 Z 比 H2 大 0.4016 Bohr，故 X=1.5+0.4016=1.9016 Bohr；选 `4 Draw a vertical line at specific X` 输入 `1.9016` 可标出）。

菜单路径：主功能 `3` → `17`（关联空穴）→ `1`（两原子定线）

输入要求：CCSD 等 post-HF `.wfn`（`examples\H2_CCSD.wfn`）+ `settings.ini` 设 `refxyz` 与 `paircorrtype`。

操作步骤（原始格式）：

```text
examples\H2_CCSD.wfn
3  // Draw curve map
17  // Correlation hole
1  // Defining the line by nuclear coordinate of two atoms
2,1  // Draw curve graph along H2 and H1
```

`paircorrtype` 取 1 得 Fermi 空穴；关 Multiwfn 改 `paircorrtype` 为 2 重跑得 Coulomb 空穴；改为 3 得总关联空穴（前两图之和）。

产出：沿 H–H 轴三张空穴曲线；Fermi 空穴示 Pauli 排斥致两核周同自旋概率同降、成键区亦降；Coulomb 空穴示参考电子近端 H 周异/同自旋概率大降、远端 H 背侧补偿升高。

来源链接：[4.3.2](sec-4-3-output-and-plot-various-properties-in-a-line.md)

## 子功能/选项：PAEM-MO 原子间相互作用分析（H₂ / He₂ 实例）

说明：$V_{\mathrm{PAEM}}({\mathbf{r}})=-V_{\mathrm{ESP}}({\mathbf{r}})+V_{\mathrm{XC}}({\mathbf{r}})$，其中 $V_{\mathrm{XC}}({\mathbf{r}})=\frac{1}{\rho({\mathbf{r}})}\int\frac{\Gamma_{\mathrm{XC}}({\mathbf{r}},{\mathbf{r}}')}{|{\mathbf{r}}-{\mathbf{r}}'|}\mathrm{d}{\mathbf{r}}'$（波函数理论）或 $V_{\mathrm{XC}}({\mathbf{r}})=\delta E_{\mathrm{XC}}[\rho]/\delta\rho$（DFT）。`settings.ini` 的 `iuserfunc=33` 基于 $\Gamma$ 算 $V_{\mathrm{XC}}$，`=34` 用 DFT XC 势（快数倍，结果相近）。判据：占据 MO 能量高于两原子间 $V_{\mathrm{PAEM}}$ 势垒则电子可自由离域、直接贡献共价成键。H₂ 势垒 $-1.903$ a.u.（$-51.78$ eV），唯一双占据 MO 能量 $-16.23$ eV 远高于势垒，故 H–H 为共价键；He₂（间距 2.97 Å，`examples\He2.fch`）势垒 $-9.78$ eV，两 MO 能量 $-25.03$/$-24.91$ eV 均低于势垒，故 He–He 为非共价。局限：水二聚体氢键被误判共价；多原子体系占据轨道太多太复杂；原子靠太近几乎总判共价。

菜单路径：主功能 `3` → `100`（自定义函数，`iuserfunc=33` 基于 $\Gamma$ 或 `34` 基于 DFT 势）→ `0`/`1`（设延伸与定线）

输入要求：HF `.fch`（`examples\H2.fch`，HF/def2-TZVP；He₂ 用 `examples\He2.fch`）+ `settings.ini` 设 `iuserfunc`。

操作步骤（原始格式）：

```text
examples\H2.fch  // Produced at HF/def2-TZVP level
3  // Plot real space function along a line
100  // User-defined function
0  // Adjust extension size at both sides
3  // 3 Bohr, which is larger than the default value
1  // Use two nuclei to define the line
1,2
```

```text
11  // Change length unit of the graph to Å
3  // Change range of Y axis
-3,0.1  // From -3.0 a.u. to 0.1 a.u.
10  // Set label intervals of X and Y axes
0.5,0.5
-1  // Replot
```

关图后选 `6` 定位势垒准确值（H₂ 最大值 $-1.903$ a.u.）。

产出：沿键轴 PAEM 曲线；势垒值；共价/非共价判断。

来源链接：[4.3.3](sec-4-3-output-and-plot-various-properties-in-a-line.md)

$$
\hat{h}\varphi({\mathbf{r}})=\varepsilon\varphi({\mathbf{r}})
$$

$$
\hat{h}=-(1/2)\nabla^2+V_{\mathrm{PAEM}}({\mathbf{r}})
$$
