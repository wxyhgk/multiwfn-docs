# 主功能7：布居分析与原子电荷计算

功能概述：主功能7计算基函数、壳层、原子、碎片的布居数或原子电荷，涵盖 Hirshfeld、VDD、Mulliken 系、ESP 拟合（CHELPG/MK/RESP）、ADCH、CM5、Hirshfeld-I、EEM、PEOE、MBIS 等近二十种模型。通用规则有三：想得碎片电荷先选 `-1 Define fragment` 定义片段；算完可选存 `[载入文件名].chg`（格式见 2.5 节），该 `.chg` 可作输入研究原子电荷 ESP 或用 `-2` 算碎片间库仑作用能。不熟悉原子电荷者强烈建议先读综述：Tian Lu, Qinxue Chen, Partial Charges, WILEY-VCH (2024), DOI: [10.1002/9783527843435.ch6](https://doi.org/10.1002/9783527843435.ch6)。

## 通用操作：碎片定义、chg 输出、碎片间静电作用能

说明：片段电荷＝片段内原子电荷之和；`.chg`/`.pqr` 作输入时 `-1` 直接加和其中电荷。

菜单路径：主功能7 → `-1` 定义片段；算完后按提示存 `.chg`；`.chg` 作输入时 → `-2`

输入要求：波函数文件（`-2` 需 `.chg`/`.pqr`）。

操作步骤（原始格式）：

```text
-1 Define fragment：输入原子序号定义碎片；之后原子电荷打印时一并打印碎片电荷。
算完后选 y：原子坐标＋电荷输出到 [载入文件名].chg（格式见 2.5 节）。
-2 Calculate interaction energy between fragments based on atomic charges
（仅 .chg/.pqr 作输入时）：用经典库仑公式算两给定碎片间静电相互作用能：
E = sum_{A in frag1} sum_{B in frag2} qA*qB / |RA-RB|。
可用于分子相互作用能中的静电分量，或基于原子跃迁电荷算分子间激子耦合能
（跃迁电荷得法见 4.A.9 节）。
```

产出：片段电荷、`.chg` 文件、碎片间库仑能。

来源：[3.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md) 开头；实例 [4.7.1 片段电荷](sec-4-7-population-analysis-and-atomic-charge-calculation.md#471-计算三氟化氯的hirshfeld和chelpg原子电荷以及片段电荷)。

## Hirshfeld 原子电荷（1）

说明：基于变形密度划分：$q_A=-\int w_A^{\mathrm{Hirsh}}(\mathbf{r})\rho_{\mathrm{def}}(\mathbf{r})\mathrm{d}\mathbf{r}$，$\rho^{\mathrm{def}}=\rho-\rho^{\mathrm{pro}}$，亦可写成 $q_A=-p_A+Z_A$。优点：合电负性直觉、权重有明确物理意义、只计转移密度、对波函数质量不敏感、可用 DFT 格点高效积分、适用固体与实验变形密度。缺点：电荷总偏小、偶极矩/ESP 复现差（完全忽略原子偶极矩）。

菜单路径：主功能7 → `1`

输入要求：GTF ＋原子坐标。

操作步骤（原始格式）：

```text
7  // Population analysis and atomic charges
1  // Hirshfeld population
1  // 使用内建（球化）自由原子密度（最方便；或选 2 基于原子 .wfn 文件，见 3.7.3 节）
```

判据：打印电荷总和应接近整数，否则数值积分不可靠，把 `settings.ini` 的 `radpot`/`sphpot` 调大（默认 75/434，可改为 100/590）重算。请用"归一化到实际电子数之后"（Final atomic charges）的电荷发表。

产出：Hirshfeld 电荷、由电荷算的偶极矩、可选 `.chg`（供主功能3/4/5选"原子电荷 ESP"研究）。

来源：[3.9.1](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#391-hirshfeld-原子电荷-1)；实例 [4.7.1](sec-4-7-population-analysis-and-atomic-charge-calculation.md#471-计算三氟化氯的hirshfeld和chelpg原子电荷以及片段电荷)。

## VDD 原子布居（2）

说明：与 Hirshfeld 唯一区别是权重函数换成类 Voronoi 胞划分（见 *J. Comput. Chem.* **25**, 189 (2004)）；变形密度量级小，换权重电荷变化不大，输出项与 Hirshfeld 完全相同；作者建议直接用 Hirshfeld。

菜单路径：主功能7 → `2`

输入要求：GTF ＋原子坐标。

操作步骤（原始格式）：与 Hirshfeld 相同。若 VDD 电荷之和明显偏离净电荷，增大 `settings.ini` 的 `sphpot`（`radpot` 也有影响但不如 `sphpot` 显著）。

产出：VDD 电荷。

来源：[3.9.2](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#392-voronoi-变形密度-vdd原子布居-2)。

## Mulliken 布居分析（5）

说明：最老的轨道波函数布居法：$\Theta_{i,a}=C_{a,i}^2+\sum_{b\ne a}C_{a,i}C_{b,i}S_{a,b}$（交叉项 $2C_{a,i}C_{b,i}S_{a,b}$ 平均分配），$q_A=Z_A-\sum_i\eta_i\sum_{a\in A}\Theta_{i,a}$。缺点：偶极矩复现差、平均分配无严格物理意义、基组依赖极强（**禁带弥散函数**）、偶发负布居。

菜单路径：主功能7 → `5` → 子功能 `1`–`4`（大体系先用 `-1` 把输出重定向到文本文件）

输入要求：含基函数信息的文件（`.fch`/`.molden`/`.mwfn`/`.wfn` 等）。

操作步骤（原始格式）：

```text
7  // Population analysis and atomic charges
5  // Mulliken population analysis
1  // 输出 Mulliken 布居与原子电荷：基函数布居、壳层布居、角动量布居、原子电荷
   //（开壳层另给 α/β/自旋布居；-1 可改输出到文件）
2  // 输出总原子布居矩阵并分解：对角元为局域项，非对角元×2 为原子对交叉项
   // 矩阵元 Ω(A,B) = sum_i ηi sum_{a in A} sum_{b in B} C(a,i)C(b,i)S(a,b)；
   // 最后一行为列和（原子总布居）；可选分解到各占据轨道（groatmdcp.txt）。
   // 顺带：2Ω(A,B)^i 即轨道 i 对 A-B 间 Mulliken 键级的贡献（见 3.11.4 节）。
3  // 输出总基函数布居矩阵并分解：Γ(a,b) = sum_i ηi*C(a,i)C(b,i)S(a,b)；
   // 可选各占据轨道贡献到 grobasdcp.txt（即使中等体系也极其庞大，慎用）。
4  // 各占据轨道对原子布居贡献输出到 atmpopdcp.txt。
```

产出：四级布居表与原子电荷（实例输出见 [4.7.0](sec-4-7-population-analysis-and-atomic-charge-calculation.md#470-三重态乙醇的mulliken布居分析)，输入 `examples\ethanol_triplet.fch` → `7` → `5` → `1`）。

来源：[3.9.3](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#393-mulliken-原子与基函数布居分析-5)。

## Löwdin 布居（6）/ SCPA（7）/ Stout-Politzer（8）/ Bickelhaupt（9）

说明：三种修正 Mulliken 都是换交叉项划分方式；Löwdin 是先做 Löwdin 正交化（变换 $\mathbf{X}=\mathbf{U}\mathbf{s}^{1/2}\mathbf{U}^{\mathrm{T}}$，新系数 $X^{-1}\mathbf{C}$）再做 Mulliken 型划分——划分只是藏进了正交化，没有更优的物理意义，实际也不优于 Mulliken（Cartesian 基还有轻微转动依赖性）。

菜单路径：主功能7 → `6` / `7` / `8` / `9`

输入要求：含基函数信息的文件。

操作步骤（原始格式）：

```text
6  // Löwdin：先 Löwdin 正交化再 Mulliken 型划分；输出同 Mulliken。
7  // SCPA（Ros & Schuit, Theo. Chim. Acta 4, 1 (1966)）：
   // Θ(i,a) = C(a,i)^2 / sum_b C(b,i)^2；输出同 Mulliken。
8  // Stout & Politzer 修正 Mulliken：用其交叉项划分；输出同 Mulliken。
9  // Bickelhaupt 修正 Mulliken：用其基函数布居定义；输出同 Mulliken。
```

产出：各修正模型的布居与电荷。

来源：[3.9.4](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#394-löwdin-原子与基函数布居-6)–[3.9.7](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#397-bickelhaupt-定义的修正-mulliken-原子布居-9)。

## Becke 原子电荷（10，含原子偶极矩校正）

说明：借 Becke 权重（*J. Chem. Phys.* **88**, 2547 (1988)）做原子空间划分：$q_A=Z_A-\int w_A(\mathbf{r})\rho(\mathbf{r})\mathrm{d}\mathbf{r}$，半径用户可控（默认 modified CSD 半径对典型有机体系合理，离子体系不太合适）。算完自动做原子偶极矩校正（与 ADCH 同过程），校正后精确复现偶极矩。

菜单路径：主功能7 → `10`

输入要求：GTF ＋原子坐标（无需原子波函数文件）。

产出：Becke 电荷（校正后）。

来源：[3.9.8](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#398-含原子偶极矩校正的-becke-原子电荷-10)。

## ADCH 原子电荷（11，高度推荐）

说明：Hirshfeld＋原子偶极矩展开为邻近原子校正电荷（*J. Theor. Comput. Chem.* **11**, 163 (2012)）；化学合理、精确复现当前水平偶极矩、ESP 复现接近 ESP 拟合电荷；代价可忽略。汇总栏 corrected＝ADCH、before＝Hirshfeld，末尾 Error≈0。`settings.ini` 的 `ishowchgtrans=1` 可看原子间电荷转移细节。

菜单路径：主功能7 → `11`

输入要求：GTF ＋原子坐标。

操作步骤（原始格式）：

```text
examples\CH3CONH2.fch
7  // Population analysis and atomic charges
11  // Calculate ADCH charges
1  // Use built-in atomic densities in free-state
```

产出示例：C1 −0.265840（校正前 −0.090370）、N −0.677574（校正前 −0.159120）；ADCH 偶极 1.4368 a.u. 与实际一致，Hirshfeld 只给出 1.0738 a.u.。请用 Final atomic charges 归一化电荷。

来源：[3.9.9](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#399-原子偶极矩校正的-hirshfeld-原子电荷-adch-11)；实例 [4.7.2](sec-4-7-population-analysis-and-atomic-charge-calculation.md#472-计算并比较乙酰胺的adch原子电荷与hirshfeld原子电荷)。

## CHELPG ESP 拟合电荷（12）

说明：立方格点分布拟合点（盒子每侧扩展 2.8 Å，默认间距 0.3 Å；舍去离核太近或离全部分子太远的点），最小化 $F=\sum_i[V_q-V]^2$ 即解 $\mathbf{A}\mathbf{q}=\mathbf{B}$（含总电荷约束行）；转动不变性好。

菜单路径：主功能7 → `12`

输入要求：GTF ＋原子坐标。

操作步骤（原始格式）：

```text
选项 1：开始计算各拟合点 ESP 并输出拟合电荷，同时输出 RMSE/RRMSE（越小复现越好）。
选项 2~4：设拟合点分布参数（默认合理，无特殊理由勿改）；选项 4 可只在某片段周围布点。
选项 5：ESP 类型（默认 Nuclear+Electronic；算 TrEsp 跃迁电荷选 Transition electronic，见 4.A.9）。
选项 6：Yes 则导出 ESPfitpt.txt/ESPfitpt.pqr（后者 VMD 按 charge 列着色可视化拟合点）
   与 ESPerr.pqr（精确与电荷 ESP 差大的点，见 4.7.8）。
选项 8：Yes 则加约束精确复现波函数偶极矩（通常不必要，ESP 拟合电荷本来复现偶极就很好）。
选项 10：选原子半径模式：(1)默认 CHELPG 原文半径（只到第三行，缺的回车用 UFF×1/1.2）；
   (2)全用 UFF×1/1.2；(3)外部文件载入，格式如 "H 1.2 / O 1.8 / Cu 2.2"（Å，全元素须定义）。
选项 -1：外部文件读拟合点代替 CHELPG 点：首行 numdata，后每行 "X Y Z [ESPval]"；
   numdata 为负则第四列直接作 ESP 用。
选项 -2：外部文件读额外拟合中心（孤对/σ-hole 区增强描述）：首行 numdata，后每行 XYZ（Å）。
选项 -3：从 .chg 载入给定电荷只检验复现性（选 1 时不产生新拟合电荷，只输出 RMSE/RRMSE）；
   配合选项 4 可只检验某片段周围。
```

产出：CHELPG 电荷＋RMSE/RRMSE（ClF₃ 例：Cl 0.5772，轴向 F −0.2496，平伏 F −0.0779，与 Hirshfeld 结论一致）。

来源：[3.9.10](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3910-chelpg-charges-from-electrostatic-potentials-using-a-grid-based-method-esp-拟合原子电荷-12)；实例 [4.7.1](sec-4-7-population-analysis-and-atomic-charge-calculation.md#471-计算三氟化氯的hirshfeld和chelpg原子电荷以及片段电荷)。

## MK ESP 拟合电荷（13）

说明：与 CHELPG 唯一区别是拟合点布在各原子 vdW 半径 1.4/1.6/1.8/2.0 倍层上（离核 <1.4 倍舍去）。其余选项与输出同 CHELPG。

菜单路径：主功能7 → `13`

输入要求：GTF ＋原子坐标。

操作步骤（原始格式）：

```text
选项 2 设每 Å² 点密度；选项 3 设层数与半径缩放因子；选项 4 设参与建点的原子。
选项 10 选半径模式（默认 automatic 用 MK 半径：一二行与 P、S、Cl 同 Gaussian MK，
Na-Si 为 1.57、1.65、1.65、1.80 Å；CHELPG 点则用 CHELPG 半径）。
其余选项（1/-1/-2/-3/6/8）见 CHELPG 一节。
```

产出：MK 电荷（CH₃CONH₂ 的 MK RRMSE≈0.05，远好于 Hirshfeld 的 0.31；用法见 4.7.8 检验节）。

来源：[3.9.11](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3911-merz-kollmann-mk-esp-拟合原子电荷-13)。

## AIM 原子电荷（14）

说明：核电荷减 AIM 盆电子数（常被误称 Bader 电荷）。最方便做法就是本子功能：选格点质量后自动用原子中心＋均匀混合格点＋盆边界精修，直接打印 AIM 电荷。

菜单路径：主功能7 → `14`

输入要求：GTF ＋原子坐标。

操作步骤（原始格式）：

```text
examples\CH3NH2.wfn
7  // Population analysis and atomic charge calculations
14  // AIM charge
2  // Medium-quality grid (cost/accuracy compromise; 质量越高越准但越贵)
```

产出：AIM 电荷（CH₃NH₂ 例 C +0.388、N −0.989，但甲基 H2/H3 带轻微负电，化学合理性不佳是 AIM 众所周知的缺陷）。

来源：[3.9.12](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3912-aim-原子电荷-14)；实例 [4.7.11](sec-4-7-population-analysis-and-atomic-charge-calculation.md#4711-计算-aim-电荷)。

## Hirshfeld-I 原子电荷（15）

说明：迭代优化原子空间（*J. Chem. Phys.* **126**, 144111 (2007)），权重 $w_A^{(n)}=\rho_A^{(n-1)}/\rho_{\mathrm{pro}}^{(n-1)}$，原子密度由相邻整数电荷态球平均密度线性插值；迭代至最大变化 <0.0002。需各元素各带电态 `.rad` 文件：最简是把 `examples\atmrad` 复制到当前目录直接用内置（PBE0 大基组＋DKH2 精心生成，前三行 PBE0/def2-QZVPP，主族 PBE0/ANO-RCC，过渡金属 PBE0/Sapporo-DK3-QZP-2012）；缺失时 Multiwfn 自动调 Gaussian 现算（`settings.ini` 的 `gaupath` 须设好；镧系锕系只能手算 `.wfn` 经主功能1000子功能14 转 `.rad`）。选项 `-3` 为距离截断加速（默认开、截断 2.0；出问题先关一次，不行再选两次改大截断值）。

菜单路径：主功能7 → `15` → 选项 `0` 开始迭代

输入要求：GTF ＋原子坐标 ＋ `.rad` 文件。

操作步骤（原始格式）：

```text
examples\CH3COCl.wfn  // Generated at B3LYP/6-31G* level
7  // Population analysis and atomic charges
15  // Hirshfeld-I method
1  // Start calculation with default settings
```

迭代显示 `Maximum change` 逐轮下降；收敛打印归一化 HI 电荷（CH₃COCl 例 C1 −0.646、羰基 C +0.727、O −0.420、Cl −0.203），绝对值远大于 Hirshfeld。可存 `.chg`。自动调 Gaussian 版多一步输入原子计算关键词：

```text
examples\CH3COCl.wfn
7
15
1  // Start calculation with default settings
B3LYP/6-31G*  // Gaussian keyword for atomic .wfn files
```

（先删已有 atmrad；`.gjf`/`.out`/`.rad` 均在 `atmrad` 文件夹；水例子需 O-2..O+2、H-1..H+1 的 `.rad`。）

产出：HI 电荷（另有快/慢两种数值算法，默认快但内存 $7n_{\mathrm{atm}}^2n_{\mathrm{rad}}n_{\mathrm{ang}}$，大体系切慢算法；格点经 `iautointgrid=0`＋`radpot`/`sphpot` 手调）。

来源：[3.9.13](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3913-hirshfeld-i-原子电荷-15)；实例 [4.7.4](sec-4-7-population-analysis-and-atomic-charge-calculation.md#474-hirshfeld-i原子电荷计算示例)。

## CM5 / 1.2×CM5（16 / -16）

说明：Hirshfeld＋经验键级校正（*J. Chem. Theory Comput.* **8**, 527 (2012)）：$q_i^{\mathrm{CM5}}=q_i^{\mathrm{Hirsh}}+\sum_{j\ne i}T_{ij}B_{ij}$，$B_{ij}=\exp[-\alpha(r_{ij}-R_i-R_j)]$，$\alpha=2.474$ Å⁻¹。与 ADCH 不同，CM5 复现的是真实偶极矩而非当前水平偶极矩，故 B3LYP/6-31G* 这种低水平仍可用。1.2×CM5 供 OPLS-AA 力场 MD（*J. Phys. Chem. B* **121**, 3864 (2017)）。`settings.ini` 设 `uESEinp=1` 可生成 uESE 溶剂化模型输入（CM5 应在气相 B3LYP/def2-TZVP 下算）。

菜单路径：主功能7 → `16` / `-16`

输入要求：GTF ＋原子坐标（建议真空下小基组 DFT，如 B3LYP/def2-SVP）。

操作步骤（原始格式）：

```text
examples\oxirane.fchk
7  // Population analysis and atomic charges
16  // CM5
1  // Use built-in sphericalized atomic densities in free-states
```

产出：CM5 电荷（环氧乙烷例 O −0.273、C −0.074、H +0.105；偶极 0.811 a.u. 即气相偶极估计）。1.2×CM5 全自动脚本 `examples\scripts\1.2CM5.sh`（ORCA 版 `1.2CM5_ORCA.sh`）：`./1.2CM5.sh phenol.xyz` 自动优化＋算电荷得 `phenol.chg`。

来源：[3.9.14](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3914-cm5-与-12cm5-原子电荷-16--16)；实例 [4.7.10](sec-4-7-population-analysis-and-atomic-charge-calculation.md#4710-计算-cm5-和-12cm5-电荷)。

## EEM 原子电荷（17）

说明：电负性均衡解线性方程（*J. Am. Chem. Soc.* **107**, 829 (1985)），秒算数百原子，适合大体系粗估。必须用含连接信息的 `.mol`/`.mol2` 作输入（超 999 原子用 `.mol2`）；π 共轭须写成 Lewis 单双交替（GaussView 存的芳香键会变成 4 号键导致 `Multiplicity ... exceeded upper limit`，用 `obabel old.mol -O new.mol` 转一道）；离子体系先用选项 `2` 设净电荷。

菜单路径：主功能7 → `17` → 选项 `0` 计算；选项 `1` 选参数集

输入要求：`.mol`/`.mol2`（离子先设净电荷）。

操作步骤（原始格式）：

```text
examples\ethanol_water.mol  // 492-atom MD snapshot
7  // Population analysis and atomic charges
17  // EEM charge
0  // Start calculation
```

输出各原子 EEM 电荷＋分子电负性。内置三套参数：(1)拟合 HF/STO-3G Mulliken（H、C、N、O、S）；(2)拟合 B3LYP/6-31G* 与 HF/6-31G* MK（H、C、N、O、F、S、Cl、Br、Zn，默认）；(3)拟合 B3LYP/6-311G* NPA。外部参数文件格式：

```text
    0.302000
 H   1  2.38500  0.73700
 C   1  2.48200  0.46400
 C   2  2.46400  0.39200
 N   1  2.59500  0.46800
 N   2  2.55600  0.37700
 O   1  2.82500  0.84400
 O   2  2.78900  0.83400
```

（首行 κ，后为多重度/A/B；选项 `1` 子选项 `0` 载入，另可导出当前参数到 `EEMparm.txt`。）

产出：EEM 电荷（乙醇–水团簇例 O≈−0.62~−0.66、H≈+0.27~+0.32）。

来源：[3.9.15](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3915-电负性均衡方法-eem-原子电荷-17)；实例 [4.7.5](sec-4-7-population-analysis-and-atomic-charge-calculation.md#475-计算乙醇-水团簇的eem原子电荷)。

## RESP / 带约束 ESP 拟合（18）

说明：既算 Kollman 标准两步 RESP（*J. Phys. Chem.* **97**, 10269 (1993)），也算带等价/电荷约束的一步 ESP 拟合；支持多构象加权、TrEsp、RESP2（RESP 扩展，更适合凝聚相 MD，见 4.7.7.9）。任何带 GTF 的文件均可。理论细节与博客 <http://sobereva.com/441> 不赘述，这里只列选项原文。

菜单路径：主功能7 → `18`

输入要求：带 GTF 的波函数文件（多构象时用选项 `-1` 的列表文件，启动时载入文件可为任意几何文件）。

操作步骤（原始格式）：

```text
选项 1：标准 RESP（两步拟合），直接算并打印。
选项 2：普通 ESP 拟合（一步），带/不带约束。
选项 -1：多构象拟合。输入"文件路径+权重"列表文件，如：
  D:\a\conf1.fch  0.2
  D:\a\conf2.fch  0.75
  D:\b\conf.fch  0.05
  权重和须恰为或接近 1.0；之后依次载入计算。
选项 3：拟合点类型与密度（默认 MK 型已足够密；可换 CHELPG）。
选项 4：双曲惩罚函数参数 a（一步默认 0.0005；两步各自 a 与 b 可改）＋最大迭代数与收敛阈值。
选项 5：等价约束。提供文本文件，如：
  4,6,9-11
  5,7
  表原子 4,6,9,10,11 等价、5,7 等价；对一步拟合与两步第一步生效。
  一步拟合默认 CH3/CH2 氢等价（可改可删）；子选项 10 生成 eqvcons_H.txt；
  子功能 11 按点群自动生成 eqvcons_PG.txt。
选项 6：电荷约束（仅一步拟合与两步第一步）。文件如：
  4,6,9-11 0.8
  5,7  -0.32
  表前组电荷和约束 0.8、后组 -0.32。
选项 7：连通性。默认两原子距小于 CSD 共价半径和×1.15 判成键；不符可用 .mol
  读入连通性（或主功能 0 调成键阈值，阈值保留给 RESP 用）。
选项 8：从 Gaussian 输出直接载入拟合点+ESP（pop=MK/CHELPG + IOp(6/33=2) 任务；
  IOp(6/42=x) 设 MK 密度，建议 x=6 对应 Multiwfn 默认）。
选项 9：额外拟合中心（孤对/σ-hole 增强）。文件格式：首行 numdata（每构象同数），
  后 XYZ（Å），不同构象间空行隔开；拟合中视为极性非氢原子但半径为零。
选项 10：原子半径（默认 automatic：MK 点用 MK 半径，CHELPG 点用 CHELPG 半径）。
选项 11：ESP 类型（默认通常 ESP；算跃迁电荷选 3 Transition electronic，见 4.A.9）。
约束规则：等价约束条目间原子不可共享；电荷约束条目间可相交；电荷约束与等价约束
  条目间不可相交。空间等价原子电荷 helft 差异源于拟合点不对称，办法是选项 5
  加等价约束（子功能 11 自动按点群生成），而非一味加密 CHELPG 格点。
```

产出：RESP/约束 ESP 电荷；多构象、等价/电荷约束、额外拟合中心、RESP2（`calcRESP2.sh`/`RESP.sh` 一键流程）实例见 [4.7.7](sec-4-7-population-analysis-and-atomic-charge-calculation.md#477-推导-resp-电荷和带额外约束的常规-esp-拟合电荷的示例说明)（例1 多巴胺标准 RESP、例2 多构象、例3 磷酸二甲酯等价约束、例4 天冬氨酸等价＋电荷约束、例5 点群对称、例6 额外拟合中心、技巧1 两次单阶段等价两阶段、技巧2 一条命令出 RESP、专题 RESP2）。

来源：[3.9.16.2](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#39162-用法与一些细节)。

## PEOE（Gasteiger）电荷（19）

说明：纯经验迭代（*Tetrahedron Lett.* **19**, 3181 (1978)；*Tetrahedron* **36**, 3219 (1980)），秒出结果，适合大有机体系快速电荷。仅支持 H/C/N/P/O/S/F/Cl/Br/I，不支持带电体系；连通性按键长＋共价半径猜（`.mol`/`.mol2` 直接读），几何须优化过（尤其含 N 时三配位 N 杂化由位置判定）。

菜单路径：主功能7 → `19`

输入要求：仅原子坐标（`.xyz`/`.pdb`/`.mol` 等）。

操作步骤（原始格式）：

```text
examples\dopamine.xyz
7  // Population analysis
19  // PEOE (Gasteiger) charge
```

先打印各原子参数（`numbond/a/b/c`），再迭代（`Max cycles: 50, 收敛 0.00010, damping 0.5`，约 10 轮收敛），最后打印电荷（多巴胺例 O −0.358、N −0.330）。`settings.ini` 的 `outmedinfo=1` 可监视每轮电荷/电负性。

产出：PEOE 电荷。

来源：[3.9.17](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3917-peoe-partial-equalization-of-orbital-electronegativity-或-gasteiger-电荷-19)；实例 [4.7.9](sec-4-7-population-analysis-and-atomic-charge-calculation.md#479-计算-peoe-gasteiger-电荷)。

## MBIS（20）/ cMBIS（21）/ EMBIS（22）/ AEMBIS（23）

说明：MBIS（*J. Chem. Theory Comput.* **12**, 3894 (2016)）迭代优化类 Slater 壳层布居 $N_{Ai}$ 与宽度 $\sigma_{Ai}$，无需预先算带电态原子密度，多数情形值与 HI 相当，支持到 Rn。cMBIS/EMBIS/AEMBIS 为 Jensen 组带多极矩约束/椭球原子变体（cMBIS *JCTC* **21**, 1179 (2025)；EMBIS *JCTC* **21**, 8753 (2025)；AEMBIS 未发表），额外输出原子体积与键级矩阵；进功能先选积分格点（高阶多极建议 fine/ultrafine 到 1e-4 精度）。

菜单路径：主功能7 → `20` / `21` / `22` / `23`

输入要求：GTF ＋原子坐标。

操作步骤（原始格式）：

```text
20 MBIS：选项 1 开始迭代并打印电荷；选项 -2 切 Yes 则一并打印收敛的壳层布居 N
   与宽度 σ；最大迭代数与收敛阈值可自定义。
21/22/23：进入先选积分格点，再按提示计算；cMBIS 可选数值/双重数值算 Vne/Vee
   原子贡献（Vee 很耗时，但可做 IQA 原子对能量分解）；还有沿方向绘密度选项。
```

产出：MBIS 系电荷（＋壳层布居/宽度、原子体积、键级矩阵）。

来源：[3.9.18](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3918-最小基迭代-stockholder-mbis-电荷-20)、[3.9.19](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3919-约束-mbis-cmbis椭球-mbis-embis非对称椭球-mbis-aembis-21-22-23)。

## 实例：三重态乙醇 Mulliken 分析

说明：Mulliken 与弥散函数不兼容；开壳层输出 α/β/总/自旋四套布居。

菜单路径：主功能7 → `5` → `1`

输入要求：`examples\ethanol_triplet.fch`（UB3LYP/6-31G**）。

操作步骤（原始格式）：

```text
examples\ethanol_triplet.fch
7  // Population analysis and atomic charges
5  // Mulliken population analysis
1  // Output Mulliken analysis result (default screen; -1 可改到文本文件)
```

产出：基函数/壳层/角动量/原子四级布居与电荷（例 O8 P 壳自旋 0.648、大部分未成对电子在羟基；三重态 O 竟带微弱正电，反映不同电子态电子结构差异大）。基函数–原子轨道对应关系判定法见 4.7.6（硫 cc-pVTZ：看壳层总/自旋布居定 1s/2s/3s 与 2p/3p 归属；Au def2-TZVP 赝势例同理）。

来源：[4.7.0](sec-4-7-population-analysis-and-atomic-charge-calculation.md#470-三重态乙醇的mulliken布居分析)、[4.7.6](sec-4-7-population-analysis-and-atomic-charge-calculation.md#476-通过布居分析确定基函数与原子轨道的对应关系)。

## 实例：ClF₃ Hirshfeld＋CHELPG＋片段电荷

说明：一站式演示 Hirshfeld 计算、CHELPG 计算与片段电荷（两轴向 F）。

菜单路径：主功能7 → `-1` → `1` / `12` → `1`

输入要求：`examples\ClF3.wfn`。

操作步骤（Hirshfeld，原始格式）：

```text
examples\ClF3.wfn
7  // Population analysis and atomic charges
1  // Hirshfeld population
1  // 使用内建原子密度（或选 2 基于原子 .wfn）
```

输出 Cl +0.523、轴向 F −0.224、平伏 F −0.076；选 `y` 导出 `.chg`。CHELPG：在布居模块选 `12`，直接选项 `1` 开始（Cl 0.5772、轴向 F −0.2496、平伏 F −0.0779）。

操作步骤（片段电荷，原始格式）：

```text
examples\ClF3.wfn
7  // Population analysis
-1  // Define fragment
2,4  // Index of the two axial F atoms
12  // CHELPG charge
1  // Start calculation
```

末尾输出 `Fragment charge: -0.499331`。

来源：[4.7.1](sec-4-7-population-analysis-and-atomic-charge-calculation.md#471-计算三氟化氯的hirshfeld和chelpg原子电荷以及片段电荷)。

## 实例：凝聚 Fukui 函数与凝聚对偶描述符（苯酚）

说明：$f^+=q_N-q_{N+1}$、$f^-=q_{N-1}-q_N$、$\Delta f=2q_N-q_{N+1}-q_{N-1}$；Hirshfeld 电荷被证明是非常合适的选择（*Theor. Chem. Acc.* **138**, 124 (2019) 全面比较）。日常建议直接用主功能22自动算（见 3.25/4.22.1）。

菜单路径：理论无直接菜单——主功能7 → `1` 分算 N/N+1/N−1 三态 Hirshfeld 电荷再代公式

输入要求：`phenol.wfn`、`phenol_N+1.wfn`、`phenol_N-1.wfn`（同几何，B3LYP/6-31G*）。

操作步骤：三态分别按 4.7.1 算 Hirshfeld 电荷（内置球化原子密度），结果（C1 对位 / C2 间位 / C3 邻位 / C4 / C5 邻位 / C6 间位）：

|        | N      | N−1   | N+1    | f⁻    | f⁺    | Δf     |
|--------|--------|-------|--------|-------|-------|--------|
| C1 (p) | −0.059 | 0.085 | −0.119 | 0.144 | 0.060 | −0.084 |
| C2 (m) | −0.039 | 0.027 | −0.167 | 0.066 | 0.128 | 0.063  |
| C3 (o) | −0.060 | 0.032 | −0.187 | 0.092 | 0.128 | 0.036  |
| C4     | 0.074  | 0.174 | 0.022  | 0.100 | 0.052 | −0.048 |
| C5 (o) | −0.073 | 0.009 | −0.196 | 0.082 | 0.123 | 0.040  |
| C6 (m) | −0.041 | 0.034 | −0.173 | 0.075 | 0.131 | 0.056  |

产出：f⁻ 最小在间位 C2/C6（不利亲电）；Δf 最正在间位（最不利亲电），C1 大负值最受亲电青睐，邻位次之——与 4.5.4 等值面结论一致。

来源：[4.7.3](sec-4-7-population-analysis-and-atomic-charge-calculation.md#473-计算凝聚fukui函数和凝聚对偶描述符)。

## 实例：原子电荷 ESP 再现性检验与可视化

说明：用 MK/CHELPG 模块的选项 `-3` 载入待检 `.chg` 再选 `1`，不产生新拟合电荷只输出 RMSE/RRMSE；选项 `6` 导出 `ESPfitpt.pqr`/`ESPerr.pqr` 用 VMD 可视化；选项 `4`/`3` 限定特定原子/片段的拟合点。

菜单路径：主功能7 → `13` MK（或 `12` CHELPG）→ `-3` → `1`

输入要求：`examples\CH3CONH2.fch` ＋ 待检 `.chg`（先按 4.7.1 常规算 Hirshfeld 存 `CH3CONH2.chg`）。

操作步骤（整体检验，原始格式）：

```text
-3  // Using atomic charges from a .chg file instead of fitting new charges
CH3CONH2.chg  // Hirshfeld charges loaded from this file
1  // Start calculation (no MK charges yielded)
```

输出 Hirshfeld RMSE 0.006214 / RRMSE 0.310394（MK 电荷 RRMSE≈0.05；ADCH 的 RRMSE 为 0.21，好于 Hirshfeld）。

操作步骤（氨基 7–9 周围两层点检验，原始格式）：

```text
-3
CH3CONH2.chg
3  // Set number and scale factors of layers
1.4
1.6
q  // Setting finished, quit
4  // Choose atoms for fitting points
7-9  // Amino group
1  // Start calculation
```

Hirshfeld RRMSE 0.374 vs ADCH 0.163。拟合点可视化：选项 `6` 切 Yes 后选项 `1` 计算，选 `2` 导出 `ESPfitpt.pqr`（VMD：VDW 画法、Sphere Scale 0.8、Coloring Charge、BWR）；误差可视化：常规算 MK 后选 `3` 导出 `ESPerr.pqr`（Charge 列为 |精确−电荷| ESP，kcal/mol，VMD Red-White-Blue，范围 −1.5~1.5，正交视角）。

产出：RMSE/RRMSE 对比表与 VMD 可视化图。

来源：[4.7.8](sec-4-7-population-analysis-and-atomic-charge-calculation.md#478-检验原子电荷的静电势再现性)。
