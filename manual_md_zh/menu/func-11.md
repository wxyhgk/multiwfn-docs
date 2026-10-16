# 主功能11：光谱绘制

功能概述：主功能 11 是绘制 IR、普通/预共振 Raman、UV-Vis、ECD、VCD、ROA 与 NMR 光谱的强大灵活模块：把每条跃迁的分立谱线按展宽函数展宽为曲线（振动光谱常用洛伦兹函数，电子光谱常用高斯函数；DOS 图每能级强度恒为 1.0，而光谱跃迁强度是关键数据）。IR/Raman/VCD/ROA 跃迁能量单位为 cm⁻¹，UV-Vis/ECD 常用 eV（1 eV=8.0655×1000 cm⁻¹）、nm、1000 cm⁻¹。还支持多体系同图与构象加权光谱（`multiple.txt`）、部分振动光谱 PVS/PVDOS（选项 24）、定向 UV-Vis（选项 -3）与基于 UV-Vis 曲线的颜色预测（选项 25）。界面中 `s` 存绘制设置、`l` 载入设置；实际点数由 `settings.ini` 的 `num1Dpoints` 控制。切勿用 `.fch`/`.molden`/`.wfn` 作光谱输入（跃迁数据不在其中）。

## 子功能：IR / Raman / VCD 光谱

说明：IR 强度单位 km/mol（某模式强度 $p$ km/mol 则展宽曲线归一化为 $100p$；esu²cm² 换算 1 esu²cm² = 2.5066 km/mol）。Raman 需区分活性 $S_i$ 与强度 $I_i$：$I_i=C(\nu_0-\nu_i)^4S_i/[\nu_i B_i]$，$B_i=1-\exp(-hc\nu_i/kT)$，$C$ 在 Multiwfn 中固定为 10⁻¹²；只有基于强度展宽的 Raman 谱才能与实验严格比较。VCD 曲线为 $\Delta\varepsilon(\lambda)=\varepsilon_L(\lambda)-\varepsilon_R(\lambda)$，把各振动模式旋光强度展宽即得。

菜单路径：载入频率任务输出 → 主功能 `11` → 选 `IR`/`Raman`/`VCD` 类型 → `0` 绘图。Gaussian 非谐（`freq=anharm`）会提示选非谐数据；Raman 活性转强度用选项 `19`（输入射频率与温度）。

输入要求：Gaussian `freq`（IR）、`freq=raman`（Raman；预共振另加 `CPHF=rdfreq` 并在几何后空行写入射光频率如 `300nm 400nm 500nm`）、`freq=VCD`（VCD）任务输出；ORCA `freq`（IR）、`%elprop Polar 1 end` + `numfreq`（Raman）、`%freq doVCD true end`（VCD）；CP2K 振动分析输出（含 `INTENSITIES T` 与 `&MOMENTS`/`&LINRES` 设置）；xtb 的 `vibspectrum`；或纯文本跃迁文件（`numdata inptype` + `energy strength [FWHM]`，IR 的能量/FWHM 单位 cm⁻¹、强度 km/mol）：

```text
6 2
  81.32920        0.72170    8.0
 417.97970        3.58980    8.0
 544.67320       21.06430    8.0
 583.12940       41.33960    8.0
 678.66900       91.47940    8.0
 867.37410        2.94480    8.0
```

操作步骤（NH₃BF₃ 的 IR 谱；2-methyloxirane 的 Raman 谱需先转强度）：载入输出文件后进 `11` 选类型，`0` 绘制（左轴曲线、右轴分立线；控制台给出极值位置高度）。常用选项：`6` 选展宽函数；`8` 设 FWHM；`14` 缩放频率（均匀缩放或幂律缩放 ${\lambda}_1{\omega}^{{\lambda}_2}$）；`15` 输出各跃迁贡献；`9` 开关分立谱线；`19` 把 Raman 活性换算为强度。

产出：IR/Raman/VCD 谱图（`1` 存图，`-4` 选格式，推荐 ps/pdf/svg 矢量格式；`2` 导出 `spectrum_line.txt`/`spectrum_curve.txt`；`-2` 导出跃迁数据到 `transinfo.txt`；`-1` 屏幕打印跃迁数据）。

来源：[3.13.1](sec-3-13-plotting-spectra.md#3131-理论theory) · [3.13.2](sec-3-13-plotting-spectra.md#3132-输入文件input-file) · [3.13.3](sec-3-13-plotting-spectra.md#3133-用法和选项usage-and-options) · 实例 [4.11.1](sec-4-11-plot-various-kinds-of-spectra.md#4111-绘制nh₃bf₃的红外-infrared-ir-光谱) · [4.11.5](sec-4-11-plot-various-kinds-of-spectra.md#4115-绘制2-methyloxirane的拉曼光谱-raman-spectrum和预共振光谱-pre-resonance-spectra)

## 子功能：UV-Vis / ECD 光谱

说明：UV-Vis 跃迁强度用振子强度 $f_{ij}=\frac{2}{3}(E_j-E_i)|\boldsymbol{\mu}_{ij}|^2$；X/Y 轴用 1000 cm⁻¹ 与 L/mol/cm 时每单位 $f$ 展宽曲线面积为 $1/(4.32\times10^6)$，X 用 eV 时为 28700。荧光谱与 UV-Vis 画法完全相同，区别是按 Kasha 规则只保留 S1（用优化 S1 几何，只考虑 S1 → S0；磷光只考虑 T1 且须计入旋轨耦合才有非零 $f$）。ECD 把旋光强度展宽即得；Gaussian 的长度/速度表象（`R(length)`/`R(velocity)`）均可载入，推荐与原点无关的速度表象（完备基下两者收敛一致）；sTDA 另有混合表象 $R_M=R_V f_L/f_V$。

菜单路径：载入激发计算输出 → 主功能 `11` → 选 `UV-Vis`/`ECD` → `0` 绘图。选项 `10` 切换 eV/nm/1000cm⁻¹；选项 `20` 改强度（清零除 S1 外振子强度画荧光谱）；ORCA SOC-TDDFT 输出可选载入 SOC 修正数据。

输入要求：Gaussian TDDFT/TDHF/CIS/ZINDO/EOM-CCSD 输出（激发态优化输出亦可，只取最后一次跃迁信息）；ORCA TDDFT 输出（`%tddft nroots 20 TDA false end`，`TDA false` 关掉默认 TDA；SOC 用 `dosoc true`；sTDA/sTD-DFT 亦支持）；sTDA 的 `tda.dat`；xtb 输出；BDF TDDFT 输出；CP2K TDDFPT 输出（含 SOC 区可画 SOC 修正谱）；或纯文本跃迁文件（能量/FWHM 单位 eV，UV-Vis 振子强度无量纲、ECD 旋光强度 cgs 即 10⁻⁴⁰ erg-esu-cm/Gauss）。

操作步骤（乙酸 UV-Vis 及单跃迁贡献；天冬酰胺 ECD；BODIPY 荧光）：载入输出进 `11` 选 `3`（UV-Vis）或 `4`（ECD，ECD 先选 `2` 用速度表象旋光强度）。单跃迁贡献：`15`（输出指定跃迁贡献，设振子强度阈值）→ `0`，得 `spectrum_curve.txt`（含各跃迁列）与 `spectrum_line.txt`，可算某峰处各跃迁百分比；或先输 `0` 再输光谱 X 位置，直接显示贡献最大的 10 个跃迁。ECD 极值标注：选项 `16` 设标签内容格式；`s` 存设置（`.dat`），`l` 载入重绘。荧光：`20` 把 S2 及以上激发态振子强度清零后绘制。

产出：UV-Vis/ECD/荧光谱图、各跃迁贡献数据（例：乙酸各跃迁列文件；天冬酰胺 ECD 极值标注；BODIPY 仅 S1 的荧光谱）。

来源：[3.13.1](sec-3-13-plotting-spectra.md#3131-理论theory) · [3.13.2](sec-3-13-plotting-spectra.md#3132-输入文件input-file) · 实例 [4.11.2](sec-4-11-plot-various-kinds-of-spectra.md#4112-绘制乙酸-acetic-acid的紫外-可见光谱及单个跃迁-individual-transitions的贡献) · [4.11.3](sec-4-11-plot-various-kinds-of-spectra.md#4113-绘制天冬酰胺-asparagine的电子圆二色-electronic-circular-dichroism-ecd光谱) · [4.11.11](sec-4-11-plot-various-kinds-of-spectra.md#41111-绘制-bodipy-的荧光光谱)

## 子功能：预共振 Raman / ROA 光谱

说明：预共振 Raman 与普通 Raman 画法相同，只是输入为 `freq=raman + CPHF=rdfreq`（含入射光频率）输出，进入界面时先选入射频率。ROA 测右旋与左旋圆偏振散射强度之差：$I_i^R-I_i^L \propto (\nu_0-\nu_i)^4A_i/[\nu_i B_i]$，Gaussian ROA 输出的是 $A_i$ 项，需按此式换算为实际 ROA 强度（选项 19，输入射频率与温度）；同时输出的 $R_i$ 项按 $I_i^R+I_i^L$ 式换算为远离共振 Raman 强度。ROA 形式有 SCP(180/90)、DCP(180) 等，常用背散射 SCP(180)。

菜单路径：载入预共振 Raman / ROA 输出 → 主功能 `11` → 选预共振 Raman（选入射光频率）/ ROA（选散射类型如 SCP(180)）→ 先 `19` 换算强度 → `0` 绘图。

输入要求：Gaussian `freq=raman + CPHF=rdfreq`（几何后空行指定入射频率）输出；Gaussian `freq=ROA` 输出（几何后空行指定入射频率，如 `0.02, 0.03, 0.04, 0.05`（默认 a.u.）或 `500nm 520nm 550nm`）。

操作步骤：载入输出后按提示选入射频率（ROA 再选散射类型），选项 `19` 输入射波数与温度把活性换算为强度，选项 `14` 做频率比例校正，`0` 绘制。

产出：预共振 Raman / ROA 谱图（例：2-methyloxirane 预共振谱；S-methyloxirane 的 VCD/ROA 谱；仅手性分子有 VCD/ROA 信号）。

来源：[3.13.1](sec-3-13-plotting-spectra.md#3131-理论theory) · 实例 [4.11.5](sec-4-11-plot-various-kinds-of-spectra.md#4115-绘制2-methyloxirane的拉曼光谱-raman-spectrum和预共振光谱-pre-resonance-spectra) · [4.11.7](sec-4-11-plot-various-kinds-of-spectra.md#4117-为手性分子-s-methyloxirane-绘制-vcd-和-roa-光谱)

## 子功能：NMR 光谱

说明：各向同性磁屏蔽 $\sigma_{iso}$ 换算化学位移 $\delta=(\sigma^{\mathrm{ref}}-\sigma)/(1-\sigma^{\mathrm{ref}})\approx\sigma^{\mathrm{ref}}-\sigma$（参比与样品必须完全相同计算设置），或缩放法定 $\delta=a\sigma+b$（如 B3LYP/6-31G* 真空优化 + SMD 氯仿算屏蔽：¹H 用 $a=-1.0157$、$b=32.2109$，¹³C 用 $a=-0.9449$、$b=188.4418$）。甲基三氢 δ 取平均；多构象按权重 $\overline{\delta^A}=\sum_i p_i\delta_i^A$ 平均。有了 δ 即画分立谱线（X 为 δ，Y 为简并度：最大间隔小于阈值如 0.05 ppm 即简并），洛伦兹展宽得实际谱（FWHM 控峰形，峰高即信号强度）。

菜单路径：载入 NMR 输出 → 主功能 `11` → 选 `NMR` → 选项 `6` 选元素 → 选项 `7` 定化学位移（TMS 参考/斜率截距定标法）→ `0` 绘图，`1` 存图（推荐 pdf 矢量格式）。

输入要求：Gaussian NMR 任务输出（示例 `# B972/def2tzvp scrf=solvent=chloroform NMR`）、ORCA NMR 输出（`! B3LYP/G 6-31G* NMR cpcm(chloroform) RIJK autoaux`）、BDF NMR 输出、CP2K `.data` 文件，或记录原子名+屏蔽值的纯文本文件（例 `examples\spectra\NMR\general.txt`）。构象加权用文件名含 `multiple` 的纯文本权重文件：

```text
D:\valine\conf1.out 0.43
D:\valine\conf2.out 0.25
D:\valine\conf3.out 0.32
```

多体系同图则每行写文件路径 + 图例（注意体系原子数必须相同）。常用选项：`-2` 导出屏蔽到 `NMRdata.txt`（用选项 7 换算后两者都导出）；`10` 对特定原子（如甲基 H）平均屏蔽；`11` 设特定原子强度（设 0 则该原子在谱中消失）；`16` 改峰上原子序号标记设置；`-3` 选图形格式（`settings.ini` 的 `graphformat` 改默认）。

产出：NMR 谱图与原始数据（控制台显示；例：乙醛 ¹³C、吡啶定标、缬氨酸构象加权谱；可指定只显示某元素或隐藏特定核）。

来源：[3.13.5](sec-3-13-plotting-spectra.md#3135-绘制nmr光谱plotting-nmr-spectrum) · 实例 [4.11.10](sec-4-11-plot-various-kinds-of-spectra.md#41110-绘制-nmr-谱-nmr-spectrum)

## 子功能：多体系同图与构象加权光谱

说明：柔性分子有多个热可及构象时，把各构象谱按 Boltzmann 权重求和得实际谱。加权谱 = Σ 权重 × 各构象谱（粗红曲线）；分立谱线高度已乘相应权重。选项 18 切换各构象谱是否乘权重（即看贡献分解）；选项 21 控制加权曲线与各体系曲线的显示。

菜单路径：写 `multiple.txt` 作输入 → 进主功能 `11` 照常绘图。

输入要求：名为 `multiple.txt` 的纯文本文件（其它文件名不被识别；Linux 路径含 `/` 或空格时加双引号）。加权谱每行“文件路径 权重”：

```text
boltz\Excit\a.out 0.6046
boltz\Excit\b.out 0.1950
boltz\Excit\c.out 0.1686
boltz\Excit\d.out 0.0317
```

只同图不加权则第二列写自定义图例：

```text
boltz\Excit\a.out Molecule A
boltz\Excit\b.out Molecule B
boltz\Excit\c.out Molecule C
boltz\Excit\d.out Molecule D
```

全数字图例会被当权重，数字图例前加 `$`（如 `$50` 表图例“50”）。NMR 加权文件名须含 `multiple`（如 `valine_multiple.txt`），且各体系原子数相同。

操作步骤：以 `multiple.txt` 为输入进 `11`，选光谱类型后 `0` 绘图；`18` 切换加权显示；SOC-TDDFT 多体系对比时按提示选每套数据用 SOC 与否（含 SOC 态数大增：50 单重 + 50 三重 → 50+3×50=200 个态，图例自动标注）。

产出：加权谱（粗红）+ 各构象/体系谱同图（例：plumericin 构象加权 UV-Vis/ECD；Ir 配合物 SOC 与否对比）。

来源：[3.13.4](sec-3-13-plotting-spectra.md#3134-同时绘制多体系和加权光谱plotting-multiple-systems-together-and-weighted-spectrum) · 实例 [4.11.4](sec-4-11-plot-various-kinds-of-spectra.md#4114-绘制-plumericin-的构象加权-conformational-weighted-uv-vis-和-ecd-光谱) · [4.11.6](sec-4-11-plot-various-kinds-of-spectra.md#4116-同时绘制多个体系)

## 子功能 24：PVS / PVDOS（部分振动光谱/部分振动态密度）

说明：PVS 把总振动光谱分解为碎片贡献：$\varepsilon_A(E)=c\sum_i\Theta_A^i f_i G(E-E_i^{\mathrm{vib}})$；PVDOS 分解振动态密度：$\rho_A(E)=c\sum_i\Theta_A^i G(E-E_i^{\mathrm{vib}})$。碎片可为一组原子（全部/特定笛卡尔分量）或一组冗余内坐标（键/角/二面角，可混合），最多 10 个。组成分两种：NC（对简正坐标的百分比贡献 $\Theta_A^i=100\%\sum_{j\in A}L_{j,i}^2$）与 I（对 IR 强度的百分比贡献，目前只适用于 IR；可略为负或超 100%，属正常，源于片间耦合可为负）。Multiwfn 支持 PVS-NC(atom/RIC)、PVS-I(atom，仅 IR)、PVDOS-NC(atom/RIC)；OPVS/OPVDOS 研究两碎片耦合（NC 型 $\Theta_{AB}^i=200\%\min(\Theta_A^i,\Theta_B^i)$；I 型 $\Theta_{AB}^i=100\%I_{AB}^i/I^i$）。

菜单路径：载入振动光谱输入 → 主功能 `11` → 选振动光谱类型 → `24` 定义碎片并选谱类型（`t`）→ `q` 离开 → `0` 绘图（`v` 切换振动 DOS 显示）。

输入要求：PVS-NC(atom)/PVDOS-NC(atom)：Gaussian/ORCA/CP2K 频率输出（xtb 需另给 `g98.out` 提供简正坐标）；PVS-NC(RIC)/PVDOS-NC(RIC)：Gaussian `freq=intmodes` 输出；PVS-I(atom)：Gaussian 频率输出 + 同任务 `.fch`/`.fchk`（载入算 IR 强度所需数据，可选输出 `IRinten.txt` 详单）。

操作步骤：进 `24` 后输 `t` 选碎片光谱类型，按序号定义碎片（仔细按屏显操作），两碎片以上时用选项 0 选画 OPVS/OPVDOS 的两碎片；`q` 离开后程序载入数据并显示各碎片在每振动模式中的定量组成；Raman/ROA 先照常把活性换算为强度；`q` 后照常 `0` 绘制（总谱 + PVS/OPVS 或 VDOS/OPVDOS 曲线同图）。

产出：总谱分解为各片段 PVS 与片段间 OPVS 曲线（`v` 切换后 PVS/PVDOS、OPVS/OPVDOS 对应；例：C18-B9N9 体系）。

来源：[3.13.6](sec-3-13-plotting-spectra.md#3136-部分振动光谱-partial-vibrational-spectrum-pvs和部分振动态密度-partial-vibrational-density-of-states-pvdos) · 实例 [4.11.12](sec-4-11-plot-various-kinds-of-spectra.md#41112-绘制部分振动谱-partial-vibrational-spectrum-pvs和部分振动能态密度-partial-vibrational-density-of-states-pvdos)

## 子功能 25/0：颜色预测、定向 UV-Vis 与作图技巧

说明：基于 UV-Vis 吸收谱预测颜色：按 CIE1931 2° 三刺激函数由 360–830 nm 谱算 XYZ，转 sRGB（不做 Gamma 校正），超界缩放到 [0,1]，取互补色 (1−R,1−G,1−B)，再把吸收色与互补色的最大分量移到 1.0 得最大亮度色（窗口右下角大致为实际观感色）。荧光色预测：先清零除 S1 外振子强度再预测，此时“color”标签色为发射色、互补色无用。柔性分子用 `multiple.txt` 加权谱预测。定向 UV-Vis：只取 $|\boldsymbol{\mu}_{ij}|^2$ 的特定分量（如 X+Y 即 $(\mu^X)^2+(\mu^Y)^2$；手动方向 (1,0,1) 即归一化 $(1/\sqrt2,0,1/\sqrt2)$ 加权），分方向曲线相加即常规总谱，用于判定吸收峰跃迁偶极主方向。各向异性来源。作图技巧：选项 23 在谱底画尖峰标示指定跃迁能级位置（可按组设颜色；多体系同图时不可用）；shell 循环逐个调主功能 11 可批量画一批文件的谱。

菜单路径：理论谱：主功能 `11` → `3` → `25` 按可见区谱评价颜色；实验谱文本：主功能 `11` → `0` 直接预测。定向 UV-Vis：主功能 `11` → `-3` → 选方向（如 `4` 为 XY 方向）→ `0`。尖峰标记：主功能 `11` → `1` → `23` 设尖峰显示状态 → 选尖峰组/模式/颜色 → `0`。

输入要求：颜色预测情形 1 同 UV-Vis 输入；情形 2 为“波长(nm) 吸光度”两列纯文本（例 `examples\spectra\Allura_red_UV-Vis.txt`，范围间隔任意，空格/逗号分隔）。定向 UV-Vis 需含跃迁偶极矩的 Gaussian TDDFT 输出。尖峰标记需 Gaussian freq 输出（模式序号查 GaussView）。

操作步骤：颜色预测按上述路径进入后先显示 360–830 nm 谱，关闭后看到吸收色、互补色及最大亮度版，命令行给出 CIE XYZ/RGB 参数。定向谱按方向选项画分方向曲线。尖峰：`23` 中设组、模式与颜色后绘制（如 NH₃BF₃ B–N/N–H 振动以不同颜色尖峰标于谱底）。

产出：吸收色/互补色（含最大亮度版）与 XYZ/RGB 参数（例：靛蓝理论谱、诱惑红实验谱；互补色即溶液实际呈现颜色）；定向 UV-Vis 分方向曲线（例：碳纳米管片段 XY/Z 方向）；带跃迁位置尖峰的光谱图。

来源：[3.13.7](sec-3-13-plotting-spectra.md#3137-基于uv-vis光谱曲线预测颜色predicting-color-based-on-uv-vis-spectrum-curve) · 实例 [4.11.14](sec-4-11-plot-various-kinds-of-spectra.md#41114-靛蓝-indigo和诱惑红-allura-red颜色的预测) · [4.11.13](sec-4-11-plot-various-kinds-of-spectra.md#41113-绘制定向uv-vis光谱-directional-uv-vis-spectrum) · [4.11.9](sec-4-11-plot-various-kinds-of-spectra.md#4119-技巧使用尖峰-spikes指示跃迁能级-transition-levels的位置) · [4.11.8](sec-4-11-plot-various-kinds-of-spectra.md#4118-技巧通过-shell-脚本为一批文件绘制光谱)
