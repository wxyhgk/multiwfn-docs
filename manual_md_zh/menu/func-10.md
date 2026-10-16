# 主功能10：态密度（DOS）、光电子能谱（PES）与 COHP 分析

功能概述：主功能 10 用于绘制总态密度 TDOS、片段分态密度 PDOS、片段间重叠布居态密度 OPDOS（$\mathrm{TDOS}(E)=\sum_i\delta(E-\varepsilon_i)$，$\mathrm{PDOS}_A(E)=\sum_i\Theta_{i,A}F(E-\varepsilon_i)$，$\mathrm{OPDOS}_{A,B}(E)=\sum_i X_{A,B}^i F(E-\varepsilon_i)$；展宽函数可选高斯/洛伦兹/赝 Voigt），以及局域态密度 LDOS、光电子能谱 PES（选项 12）与晶体轨道哈密顿布居 COHP（选项 -7 切换模式）。PDOS/OPDOS 需要 `.mwfn`/`.fch`/`.molden`/`.gms` 输入；仅画 TDOS 时也可用 `pop=full` 的 Gaussian 单点输出或纯文本轨道文件。含弥散函数时画 PDOS 必须用 Hirshfeld/Becke 成分法（此时无 OPDOS）。界面中 `s` 保存当前状态（绘图设置、片段定义、轨道信息），`l` 载入状态快速重绘。

## 子功能 -1/0/00：TDOS / PDOS / OPDOS 作图

说明：$\mathrm{PDOS}_A$ 揭示片段 $A$ 的轨道组成随能量的分布；$\mathrm{OPDOS}_{A,B}$ 为正表示该能量处两片段成键，为负表示反键。未定义片段时选项 0 只画 TDOS；定义片段后画 TDOS+PDOS；同时定义片段 1、2 后画 TDOS+PDOS+OPDOS（此时也可用 `-0` 只画 TDOS+PDOS）。选项 00 直接画 TDOS + 最近邻原子间 OPDOS（$\mathrm{OPDOS}^{\mathrm{near}}$），无需定义片段。注意片段 1、2 可共用基函数甚至定义相同，此时只算交叉项而忽略局域项。定义片段后程序自动按当前 X 轴范围计算并打印每个片段的 PDOS 中心（可用于 d 带中心分析）。

菜单路径：主功能 `10` → `-1` 定义片段（最多 10 个）→ `0` 绘图；或直接 `0`（只画 TDOS）/ `00`（TDOS + 最近邻 OPDOS）。

输入要求：画 PDOS/OPDOS 需 `.mwfn`/`.fch`/`.molden`/`.gms`（`.wfn`/`.wfx` 无基函数与虚轨道信息，不可用）；仅 TDOS 可用 Gaussian 单点输出（`pop=full`）或纯文本轨道文件，格式为：

```text
nmo inp
energy occ [strength] [FWHM]         ← For orbital 1
energy occ [strength] [FWHM]         ← For orbital 2
energy occ [strength] [FWHM]         ← For orbital 3
...
energy occ [strength] [FWHM]         ← For orbital nmo
```

其中 `inp` 为 1（只读能量+占据数，强度/半高宽自动设 1.0/0.25 a.u.）、2（另读强度与半高宽列）、3（同 1 但能量单位 eV）、4（同 2 但 eV）。

操作步骤（N-phenylpyrrole TDOS；片段 PDOS/OPDOS）：

```text
examples\N-phenylpyrrole.fch
10  // Plot various kinds of DOS maps
0  // Plot map
```

```text
examples\N-phenylpyrrole.fch
10  // Plot various kinds of DOS maps
-1  // Enter the interface for defining fragments. You can define up to 10 fragments. PDOS will be plotted for all of them, but OPDOS will only be drawn between fragments 1 and 2
1   // Define fragment 1
a 1-5  // Add carbons and nitrogen of pyrrole moiety (atoms 1~5) to the fragment
q  // Save fragment 1
2  // Define fragment 2
a 10-13,15,17  // Add phenyl moiety (atoms 10~13, 15 and 17) to the fragment
q  // Save fragment 2
3  // Define fragment 3
a 6-9,14,16,18-20  // Add all hydrogens to the fragment
q  // Save fragment 3
0  // Return to last menu
2  // Set X-axis
-1.1,-0.1,0.1  // Set the range of X-axis to -1.2 ~ -0.1 a.u., so that all valence MOs can be shown in the graph. The step between labels is set to 0.1 a.u.
0  // Draw TDOS+PDOS+OPDOS
```

常用选项：`1` 选展宽函数（默认高斯）；`2` 设能量范围与步长；`3` 设 FWHM；`4` 设曲线缩放比；`6` 选 α/β/双自旋（仅非限制波函数）；`7` 选 PDOS 成分法（Mulliken/SCPA/Hirshfeld/Becke）；`8` 切换 a.u./eV；`9` 用线高显示简并度（设能量差阈值，如 `0.05` eV，TDOS 与 MO-PDOS 可用，PDOS 不可用）；`-6` 设能级位移（输 `H` 把 HOMO 移到零点）；`-5` 自定义特定 MO 的能级/占据数/强度/半高宽；`-4` 显示全部轨道信息；`-3` 导出能级/强度/半高宽到 `orginfo.txt`（可直接作输入文件）。后处理菜单可调颜色图例、重画（选项 1）、导出图形或 X-Y 数据集；选项 `13` 可关闭 Y 轴标签刻度（TDOS 曲线绝对值无意义，只看相对高度）。

产出：TDOS/PDOS/OPDOS 曲线图（左轴 TDOS/PDOS，右轴 OPDOS；选项 14 调右轴缩放；竖线为 MO 能级，虚线标 HOMO，黑/灰线区分占据/虚轨道）与 PDOS 中心打印值。

来源：[3.12.1](sec-3-12-plotting-density-of-states-pes-and-cohp.md#3121-理论theory) · [3.12.2](sec-3-12-plotting-density-of-states-pes-and-cohp.md#3122-输入文件input-file) · [3.12.3](sec-3-12-plotting-density-of-states-pes-and-cohp.md#3123-绘制态密度dos图的选项与基本用法) · 实例 [4.10.1](sec-4-10-plot-density-of-states-dos-maps.md#4101-绘制-n-phenylpyrrole-的总态密度偏态密度和重叠态密度-total-partial-and-overlap-dos)

## 子功能 -2/00：MO-PDOS 与最近邻 OPDOS

说明：MO-PDOS 是特殊的 PDOS：按分子轨道集合（而非原子/基函数）分组揭示不同 MO 集合的贡献，不同组曲线与离散线用不同颜色绘制。选项 00 无需定义片段，直接画 TDOS + 最近邻原子间 OPDOS。

菜单路径：主功能 `10` → `-2` 定义 MO 片段 → `0` 绘图；或直接 `00`。

输入要求：`.mwfn`/`.fch`/`.molden`/`.gms`（含基函数信息）。

操作步骤：进入 `-2` 按提示输入各组 MO 序号（如 cyclo[18]carbon 的 σ/面内 π/面外 π 三组），`s` 可存状态文件（`.dat`），`l` 可载入重绘；`00` 直接回车即画。

产出：MO-PDOS 图（三组曲线高度之和等于 TDOS；选项 9 可用线高表简并度）或最近邻 OPDOS 图。

来源：[3.12.3](sec-3-12-plotting-density-of-states-pes-and-cohp.md#3123-绘制态密度dos图的选项与基本用法) · 实例 [4.10.5](sec-4-10-plot-density-of-states-dos-maps.md#4105-绘制cyclo18carbon的mo-pdos图-mo-pdos-map以揭示由不同分子轨道-molecular-orbitals-mos贡献的投影态密度-projected-density-of-states-pdos)

## 子功能 10/11：局域态密度 LDOS（点/沿线）

说明：给定点 $\mathbf{r}$ 的 LDOS 为 $\mathrm{LDOS}(\mathbf{r},E)=\sum_i\varphi_i^2(\mathbf{r})f(E-\varepsilon_i)$（空间分辨的态密度；注意部分文献把 PDOS 也叫 LDOS，勿混淆）。选项 10 画单点的 LDOS 曲线；选项 11 把均匀分布在一条直线上的点的 LDOS 画成颜色填充图（X 轴能量，Y 轴线上相对起点坐标）。FWHM/能量单位/范围/缩放比选项同样生效；片段定义不影响 LDOS（恒对应 TDOS）。若想分离角动量贡献，先用主功能 6 子功能 25 把不需要的 GTF 系数清零。

菜单路径：主功能 `10` → `10`（单点 LDOS，输入点坐标）/ `11`（沿线 LDOS，输入直线起终点与点数）。

输入要求：同 DOS 输入（`.fch` 等）。

操作步骤：进入 `10` 后输入点坐标（可先用主功能 0 查坐标）；进入 `11` 后输入直线两端点坐标与取点数（如 200），选项 4 可调纵横比。

产出：单点 LDOS 曲线（可与 TDOS 对比解释 STM 数据；例：丁二烯端碳上方）或沿线 LDOS 颜色填充图。

来源：[3.12.4](sec-3-12-plotting-density-of-states-pes-and-cohp.md#3124-局域态密度local-dos) · 实例 [4.10.2](sec-4-10-plot-density-of-states-dos-maps.md#4102-绘制13-丁二烯-13-butadiene的局域态密度-local-dos)

## 子功能 12：光电子能谱 PES

说明：基于（广义）Koopmans 定理画 PES：Koopmans 定理下电离能等于轨道能量负值，模拟 PES 即把占据轨道展宽的 TDOS（展宽前能量符号反转，对应电子结合能）；广义 Koopmans 定理再对全部结合能加偏移 `VIP + E(HOMO)`（选项 3 设置），使第一峰恰对第一垂直电离能。PES 只能用 eV + 高斯展宽；非限制开壳层不区分自旋；Y 轴绝对值无意义（选项 13 可隐藏 Y 轴）。默认各轨道强度 1.0、FWHM 0.2 eV（选项 6 可改）；选项 `-3` 导出 `PESinfo.txt`（3.12.2 节格式）手动微调各轨道强度/半高宽后再作输入，可更贴近实验。

菜单路径：主功能 `10` → `12` → `1` 绘图（Koopmans）/ `3` 设偏移（广义 Koopmans）→ `4` 设 X 轴 → `1` 绘制。

输入要求：同 DOS（`.mwfn`/`.fch`/`.molden`/`.gms`、带 `pop=full` 的 Gaussian 输出或纯文本文件）；体系第一垂直电离能 VIP 需另行算好。

操作步骤（Cr₃Si₁₂⁻ 广义 Koopmans PES）：进入 `10 → 12`，选 `3` 设位移为 VIP+HOMO 能量，选 `4` 设 X 轴，选 `1` 绘制；选项 11 调曲线/分立线相对高度；若选 1 后无显示，先 `-2` 检查结合能值与 X 轴范围（范围内必须至少有一个结合能）。

产出：PES 曲线与结合能分立线；峰位与实验 PES 对照验证。

来源：[3.12.5](sec-3-12-plotting-density-of-states-pes-and-cohp.md#3125-光电子能谱photoelectron-spectrum) · 实例 [4.10.4](sec-4-10-plot-density-of-states-dos-maps.md#4104-绘制cr₃si₁₂团簇的光电子谱-photoelectron-spectrum-pes)

## 子功能 -7：COHP 分析

说明：COHP 把 OPDOS/COOP 中的重叠矩阵换成 Kohn-Sham 矩阵，从能量角度关联原子间/片段间相互作用（*J. Phys. Chem.*, **97**, 8617 (1993)）。每条 MO 既有 COOP 值又有 COHP 值：正 COOP、负 COHP 表明该 MO 被占据时（成键态）对成键有正贡献；反之负 COOP、正 COHP 为反键态。画的是 −COHP：正为成键态、负为反键态。COHP 曲线对基组较敏感，比较不同情形时用完全相同基组。

菜单路径：主功能 `10` → `-7` 切换到 COHP 模式 → 提供 Kohn-Sham 矩阵 →（片段间则 `-1` 定义片段）→ `0` 绘图。

输入要求：含基函数信息的 `.mwfn`/`.fch`/`.molden` + Kohn-Sham 矩阵（可由 Multiwfn 基于波函数生成，或从外部文件载入，见 6.7 节）。

操作步骤：

- (1) 载入含基函数信息的文件；
- (2) 进主功能 10，选 `-7` 切换到 COHP 绘制模式；
- (3) 按提示提供 Kohn-Sham 矩阵（Multiwfn 生成或外部载入）；
- (4) 最近邻原子间 COHP 直接选 `0`；两片段间 COHP 先在 `-1` 定义两片段再选 `0`；
- (5) 程序计算能量范围内每条 MO 的 COHP 并展宽成曲线显示；
- (6) 后处理与 DOS 菜单类似，专用选项 `-2` 打印各 MO 的 COHP 原始数据与 ICOHP 求和（占据能级 COHP 之和评估成键贡献）。

产出：−COHP 曲线（左轴展宽曲线、右轴尖峰高度）与 ICOHP 求和（例：C₆₀ 近邻原子、N-phenylpyrrole 片段间）。

来源：[3.12.6](sec-3-12-plotting-density-of-states-pes-and-cohp.md#3126-cohp) · 实例 [4.10.7](sec-4-10-plot-density-of-states-dos-maps.md#4107-为c₆₀富勒烯-fullerene和n-phenylpyrrole绘制晶体轨道哈密顿布居-cohp)

## 附：开壳体系 DOS 与 d 带中心

说明：非限制开壳体系用选项 6 切换 α/β/双自旋分别画 DOS；导出 `alpha.txt`/`beta.txt` 后可在 Origin 中取负值拼上下对称的 α/β 对比图。d 带中心：把过渡金属 D 型基函数定义为片段（`cond` 条件选基函数），切 eV（选项 8）、设 X 轴包住 d 带（选项 2）后绘图，命令行直接打印 TDOS/PDOS 中心，减去 HOMO（费米能级惯例）即 d 带中心；X 轴上限一般取 0。

菜单路径：主功能 `10` → `-1`（定义片段）→ `0`；自旋用 `6` 切换；后处理选项 3 导出曲线数据。d 带中心：`-1` → `cond` 选 D 型基函数 → `8` → `2` → `0`。

输入要求：非限制 `.fchk`（开壳 DOS）、含过渡金属 D 基函数的 `.fchk`（d 带中心；例 Cu₁₃）。

产出：α/β DOS 对比图；TDOS/PDOS 中心与 d 带中心数值。

来源：实例 [4.10.3](sec-4-10-plot-density-of-states-dos-maps.md#4103-绘制非限制开壳体系的dos图na₃osi₁₂c₁₂) · [4.10.6](sec-4-10-plot-density-of-states-dos-maps.md#4106-计算过渡金属团簇的-d-带中心-d-band-center)
