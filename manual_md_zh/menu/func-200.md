# 主功能200：其它功能，第二部分

功能概述：主功能 200 是 Multiwfn “其它功能”的第二部分，收录不便归入前 25 个主功能的杂项分析工具，共 18 个子功能（编号 1、2、3、5、6、9、10、11、12、13、14、15、16、17、18、19、20、21；编号 4、7、8 空缺）。内容覆盖氢键 CVB 指数、Hilbert 空间原子/键偶极矩、多轨道 cube 生成、径向分布函数、两波函数轨道对应、团簇平均键长配位数、轨道间积分、函数矩与回转半径、EI/BPI 指数、轨道对密度差贡献、域分析、电子相关指数、NO/NSO/SNO 生成、Coulomb/交换积分、BLA/BOA 交替、SDI 离域指数、BOD/NAdO 分析与 Löwdin 正交化。多数子功能只需要原子坐标与 GTFs/基函数即可运行，是日常分析的“工具箱”。

## 子功能 1：计算核-价分叉（CVB）指数及相关量

说明：基于 ELF 定义的 CVB 指数 `CVB = ELF(C-V) − ELF(DH-A)` 用于区分氢键强弱（弱复合物为正、强复合物为负）。Multiwfn 提供全自动计算，也支持手动（ELF 曲线图/拓扑分析）处理强氢键与 π 氢键等特殊情形。

菜单路径：主功能 `200` → 子功能 `1`。

输入要求：原子坐标、GTFs。示例文件 `examples\HF_HF.wfn`（B3LYP-D3(BJ)/def2-TZVP 优化，D、H、A 分别为 F2、H1、F3）。

操作步骤（原始格式）：

```text
examples\HF_HF.wfn
200  // Other function, part 2
1  // Calculate CVB index and related quantities
2,1,3  // Index of donor atom, hydrogen and acceptor atom of the H-bond, respectively
```

产出：屏幕输出 `ELF(C-V,D)`、`ELF(C-V,A)`、`ELF(DH-A)` 与 `CVB index = ELF(C-V,D) − ELF(DH-A)`（示例值 `0.028768`），以及各极小点到氢的距离。π 氢键（如 `examples\C2H4_HF.wfn`）需手动：F7–H8 间 ELF 曲线读 `ELF(C-V,D)=0.0944`，ELF 拓扑分析找 V(D,H)–π basin 分叉点得 `ELF(DH-A)=0.1241`，CVB = −0.0297。拓扑分析输入序列（原文）：

```text
2  // Topology analysis
-11  // Select the real space function to be analyzed
9  // ELF
6  // Search critical points by randomly distribute initial guesses within a sphere
4  // Set the sphere center as geometry center of three atoms
1,4,8  // Center of C1, C4 and H8 will be set as the sphere center
0  // Start searching (the sphere radius, the number of starting points can be set by corresponding options in the interface)
-9  // Return
0  // Visualize topology analysis result
```

来源链接：[3.200.1](sec-3-200-other-functions-part-2.md#32001-计算核-价分叉-cvb-指数及相关量)；博客 <http://sobereva.com/461>。

## 子功能 2：在 Hilbert 空间计算原子与键偶极矩

说明：直接基于基函数把体系偶极矩 $\boldsymbol{\mu} = \boldsymbol{\mu}^{\mathrm{nuc}} + \boldsymbol{\mu}^{\mathrm{ele}} = \sum_{A} Z_{A}\mathbf{R}_{A} - \sum_{i}\sum_{j} P_{i,j}\left\langle \chi_{i} \left| \mathbf{r} \right| \chi_{j} \right\rangle$ 分解为单原子项与原子对项之和，输出原子局域布居、原子偶极矩、键布居、键偶极矩及 Mulliken 划分的原子总偶极矩。

菜单路径：主功能 `200` → 子功能 `2`。

输入要求：必须含基函数信息的文件（例如 `.mwfn`、`.fch`、`.molden`、`.gms`）。

操作步骤（原始格式）：进入本功能后按选项号选择：选项 `1` 输出特定原子的信息；选项 `2` 输出特定原子对之间的信息；选项 `3` 输出所选原子的原子总偶极矩及相关信息；选项 `10` 则电子偶极矩矩阵的 X/Y/Z 分量分别输出到 `dipmatx.txt`、`dipmaty.txt` 和 `dipmatz.txt`。

产出：$\boldsymbol{\mu}_{A}^{\mathrm{nuc}}$、$\boldsymbol{\mu}_{A}^{\mathrm{pop}}$、$\boldsymbol{\mu}_{A}^{\mathrm{dip}}$、$\boldsymbol{\mu}_{AB}^{\mathrm{pop}}$、$\boldsymbol{\mu}_{AB}^{\mathrm{dip}}$ 及 Mulliken 版 ${\boldsymbol{\mu}'}_{A}^{\mathrm{pop}}$、${\boldsymbol{\mu}'}_{A}^{\mathrm{dip}}$ 等；选项 10 导出三个偶极矩矩阵文件。

来源链接：[3.200.2](sec-3-200-other-functions-part-2.md#32002-在-hilbert-空间计算原子与键偶极矩)。

## 子功能 3：为多个轨道波函数生成 cube 文件

说明：一次计算多个轨道波函数的格点数据，可导出为多个 cube 文件（如 `orb000003.cub`）或合并为单个 `orbital.cub`（VMD 与 Multiwfn 均支持多套格点数据的 cube）。

菜单路径：主功能 `200` → 子功能 `3`。

输入要求：原子坐标、GTFs。

操作步骤（原始格式）：进入该功能后，先选择感兴趣的轨道（例如 `3,5,9-17`），再定义格点设置，再选择导出方案：方案 `1` 导出为多个文件；方案 `2` 集体导出到 `orbital.cub`。限制性/非限制性单行列式波函数支持基于 HOMO/LUMO 的相对选择，例如 `h-3` 指 HOMO−3，`l+2` 对应 LUMO+2。

产出：多个 `orbXXXXXX.cub` 或单个 `orbital.cub`。

来源链接：[3.200.3](sec-3-200-other-functions-part-2.md#32003-为多个轨道波函数生成-cube-文件)。

## 子功能 5：对实空间函数绘制径向分布函数（RDF）

说明：计算 $RDF(r) = \int f(r,\Omega) r^{2} \mathrm{d}\Omega$ 及其积分曲线 $I(r^{\prime}) = \int_{r_{\mathrm{low}}}^{r^{\prime}} RDF(r) \mathrm{d}r$，可选球心、上下限与径向/角向点数；后处理菜单可绘制 RDF 与积分曲线、导出数据与球平均函数 $f^{\mathrm{sph}}(r) = RDF(r)/(4\pi r^{2})$。

菜单路径：主功能 `200` → 子功能 `5`。

输入要求：原子坐标、GTFs。

操作步骤（原始格式，实例 C₆₀）：

```text
C60.wfn
200  // Other functions (Part 2)
5  // Plot RDF for a real space function
3
1,6  // Set the lower and upper limit of RDF to 1.0 and 6.0 Å, respectively
0  // Calculate RDF and its integration curve
```

Rydberg 轨道实例（先把 MO11 占据数设为 2，其余清零，再画 0–10 Å 的 RDF）：

```text
6  // Modify wavefunction
26  // Modify orbital occupation number
0  // Select all orbitals
0  // Select occupation number of all orbitals to zero
11  // Select orbital 11
2  // Set occupation number of orbital 11 to 2.0 (assume it is doubly occupied)
q  // Return
-1  // Return to main menu
200
5  // Plot RDF
3  // Set lower and upper limit of radial plotting
0,10  // From 0 to 10 Å
4  // Set angular number of integration points. The default value is unnecessarily high for present purpose, therefore we set it to a smaller value to reduce computational time
302  // 302 angular points
0  // Calculate RDF for electron density (which is the default real space function)
1  // Plot the RDF map
```

产出：RDF 曲线（C₆₀ 峰≈3.5 Å；甲醛 MO11 主峰≈4.6 Å，证实 Rydberg 弥散特征）、积分曲线与积分值、球平均函数。

来源链接：[3.200.5](sec-3-200-other-functions-part-2.md#32005-对实空间函数绘制径向分布函数)；实例 [4.200.5](sec-4-200-other-functions-part-2.md#42005-绘制电子密度的径向分布函数)。

## 子功能 6：分析两个波函数中轨道的对应关系

说明：把当前波函数轨道表示为另一波函数轨道的线性组合 $|i\rangle = \sum_{j} C_{i,j}|j\rangle$（$C_{i,j}=\langle i|j\rangle$），用 Becke 多中心数值积分算重叠矩阵，输出每个轨道的前五大贡献与展开系数；`−1` 输出全部重叠积分到 `convmat.txt`，`−2`/`−3` 输出模重叠积分到 `Snormmat.txt`/`Snorm2mat.txt`。

菜单路径：主功能 `200` → 子功能 `6`。

输入要求：当前波函数与第二个波函数文件（方法/基组/几何可不同）；原子坐标、GTFs。

操作步骤（原始格式，CH₃NH₂ 的 HF 与 MP2 轨道对应）：

```text
C:\CH3NH2_MP2.wfn  // MP2/6-31+G* wavefunction file, there are 48 NOs
200  // Other function, part 2
6  // Analyze correspondence between orbitals in two wavefunctions
[Press ENTER button directly to choose all orbitals]
C:\CH3NH2_HF.wfn  // HF/6-31+G* wavefunction file, there are 9 MOs
[Press ENTER button directly to choose all orbitals]
```

产出：每个轨道的五大贡献列表（如 `NO5 = 0.7408·MO6 − 0.6412·MO7…`，总计 99.98%）；氮孤对 LMO44 对多巴胺 MO49 贡献 33.29%（定域 LMO 先经主功能 19 产生）。

来源链接：[3.200.6](sec-3-200-other-functions-part-2.md#32006-分析两个波函数中轨道的对应关系)；实例 [4.200.6](sec-4-200-other-functions-part-2.md#42006-研究不同波函数文件中轨道之间的对应关系)。

## 子功能 9：计算平均键长和平均配位数

说明：对团簇等体系计算两种元素间的平均键长 $\langle R \rangle = \frac{1}{n_{\mathrm{b}}} \sum_{i>j} R_{ij}$ 与平均配位数 $CN = \frac{1}{n} \sum_{i} N_{i}$（示例 Ge₁₂Au 团簇 `examples\Ge12Au.pdb`）。

菜单路径：主功能 `200` → 子功能 `9`。

输入要求：原子坐标（如 `Ge12Au.pdb`）。

操作步骤（原始格式）：进入该功能后，输入两种元素（例如 `Ge,Au`），再输入距离截断（例如 `3.2`，≤3.2 Å 的 Ge–Au 接触视为键并计算平均键长，同时输出最短和最长键长）；之后若选 `y`，显示 Ge 由于 Ge–Au 键的平均配位数。

产出：平均键长、最短/最长键长、平均配位数。

来源链接：[3.200.9](sec-3-200-other-functions-part-2.md#32009-计算平均键长和平均配位数)。

## 子功能 10：输出轨道之间的各种积分

说明：计算两轨道间的电偶极矩积分 $\boldsymbol{\mu}_{ij} = \langle \varphi_i|-\mathbf{r}|\varphi_j \rangle$、磁偶极矩积分 $\mathbf{M}_{ij} = i\langle \varphi_i|\mathbf{r}\times\nabla|\varphi_j \rangle$、速度积分 $\mathbf{v}_{ij} = i\langle \varphi_i|\nabla|\varphi_j \rangle$、动能积分 $K_{ij} = -\frac{1}{2}\langle \varphi_i|\nabla^2|\varphi_j \rangle$ 与重叠积分 $S_{ij}$。一批轨道的结果导出到 `orbint.txt`（第一、二列为轨道编号），一对轨道直接打印屏幕。

菜单路径：主功能 `200` → 子功能 `10`。

输入要求：原子坐标、GTFs。

操作步骤（原始格式）：进入本功能后输入一对或一批轨道编号即可；Coulomb/交换积分改用子功能 17。

产出：屏幕打印或 `orbint.txt`。

来源链接：[3.200.10](sec-3-200-other-functions-part-2.md#320010-输出轨道之间的各种积分)。

## 子功能 11：计算函数的中心、一阶/二阶矩、回转半径和 ⟨r²⟩

说明：用 Becke 多中心积分计算实空间函数分布的中心 $\mathbf{r}_c$、一阶矩 $\boldsymbol{\mu}$、二阶矩 $\mathbf{\Theta}$、各向异性、回转半径与空间范围 $\langle r^2\rangle$。选项 1 计算全部量，选项 3 选函数，选项 4 设中心，选项 2 算中心，选项 5 用绝对值算中心（适合正负相当的函数如轨道波函数），选项 −1 切换绝对值模式。

菜单路径：主功能 `200` → 子功能 `11`。

输入要求：原子坐标、GTFs。

操作步骤（原始格式，自旋密度例子）：

```text
200  // Other function (Part 2)
11  // The present function
3  // Select a real space function
5  // Spin density
2  // Calculate center of spin density
y  // Take the calculated center for evaluating various data in option 1
1  // Evaluate various data for spin density
```

产出：分布中心、各阶矩、回转半径、$\langle r^2\rangle$；电子密度情形还输出四极矩核贡献与分子四极矩张量。

来源链接：[3.200.11](sec-3-200-other-functions-part-2.md#320011-计算函数的中心一阶二阶矩回转半径和-)；博客 <http://sobereva.com/658>。

## 子功能 12：计算能量指数（EI）或键极性指数（BPI）

说明：$\mathrm{EI}_{A} = \frac{\sum_{i}^{\mathrm{val}} \varepsilon_{i} \eta_{i} \Theta_{i,A}}{\sum_{i}^{\mathrm{val}} \eta_{i} \Theta_{i,A}}$（Mulliken 组成，禁弥散基），$\mathrm{BPI}_{AB} = (\mathrm{EI}_{A} - \mathrm{EI}_{A}^{\mathrm{ref}}) - (\mathrm{EI}_{B} - \mathrm{EI}_{B}^{\mathrm{ref}})$；自由基 −EI 即基团电负性。支持 R/RO/U 型 HF/DFT 波函数，自动识别价轨道。

菜单路径：主功能 `200` → 子功能 `12`。

输入要求：原子坐标、基函数（禁弥散基）。实例用 `examples\EI_BPI` 下 ethane/N2H4/CH3NH2/CH3F/CH3/F 的 `.fch`（HF/6-31G*，无弥散）。

操作步骤（原始格式）：进入本功能后输入原子序号即得 EI；结合参考分子（如乙烷 C 的 EI −0.667639 a.u.）算 BPI。实例结果：BPI(CN)=−0.046、BPI(CF)=−0.189，C–F 极性更强。

产出：各原子 EI、参考 EI、BPI 与基团电负性。

来源链接：[3.200.12](sec-3-200-other-functions-part-2.md#320012-计算能量指数-ei-或键极性指数-bpi)；实例 [4.200.12](sec-4-200-other-functions-part-2.md#420012-计算能量指数ei与键极性指数bpi)。

## 子功能 13：计算轨道对密度差或其它格点数据的贡献

说明：把 $\Delta\rho(\mathbf{r}) \approx \sum_i p_i|\varphi_i(\mathbf{r})|^2$ 经带约束 $\sum_i p_i = P$ 的最小二乘求解 $\{p\}$，定量各轨道对 Fukui 函数、激发密度差等的贡献；选项 1 设约束 P（默认 1.0），选项 2 切换内存/cube 模式，选项 0 选轨道范围计算；后处理可视化拟合密度与残差等值面。

菜单路径：主功能 `200` → 子功能 `13`。

输入要求：含感兴趣轨道的文件与 Δρ 的 cube 文件（如苯酚 `phenol.wfn`、`phenol_N-1.wfn` 与 `density.cub`，f⁻ cube 先经主功能 5 自定义操作生成）。

操作步骤（原始格式）：(1) 生成 Δρ 的 cube 文件；(2) 载入轨道文件后进入主功能 200 的子功能 13；(3) 输入 Δρ cube 路径；(4) 选项 1 设定约束 P；(5) 选项 0 设定轨道范围并计算；(6) 后处理菜单可视化 Δρ、拟合密度或差值的等值面。实例：苯酚 HOMO（轨道 25）对 f⁻ 贡献 0.766，拟合误差仅 0.0038。

产出：各轨道贡献 p、拟合误差（两种定义）、拟合密度 cube。

来源链接：[3.200.13](sec-3-200-other-functions-part-2.md#320013-计算轨道对密度差或其它格点数据的贡献)；实例 [4.200.13](sec-4-200-other-functions-part-2.md#420013-研究轨道对密度差的贡献)。

## 子功能 14：域分析（求函数等值面内的性质）

说明：在特定实空间函数等值面定义的各域内积分任意函数（如 RDG<0.5 各域积分电子密度定量弱相互作用；EDD 域内积分；空腔域体积）。选项 2/3 定义域，选项 1（或 −1 用内存格点）算格点并识别域，选项 1/2 对单域/全域积分，−1 合并域，10/11 导出 `domain.cub`/`domain.pdb`，12 导出 `domain.txt`；后处理有 $q_{\mathrm{bind}}$ 指数与按 sign(λ₂)ρ 取子域积分的灵活选项。

菜单路径：主功能 `200` → 子功能 `14`。

输入要求：原子坐标、GTFs（内存格点模式可直接用 `.cub`）。

操作步骤（原始格式）：(1) 选项 2 选 RDG、选项 3 输入 `<0.5`（选项 4 可开周期性）；(2) 选项 1 定义格点并计算识别域（内存已有格点可用 −1）；(3) 选项 3 可视化域找感兴趣编号，再用 1/2 积分（被积函数可选任意实空间函数、内存格点或同格点 `.cub`）。实例：苯酚二聚体各 RDG 域积分表征弱相互作用；PP 体系用 q_int 判断氢键；空腔域积分得体积；苯 EDD 域内积分 EDD。

产出：各域体积、积分值、平均/最大/最小值、XYZ 范围；`domain.cub`、`domain.pdb`、`domain.txt`。

来源链接：[3.200.14](sec-3-200-other-functions-part-2.md#320014-域分析求函数等值面内的性质)；实例 [4.200.14](sec-4-200-other-functions-part-2.md#420014-域分析例子)。

## 子功能 15：计算电子相关指数

说明：计算 Matito 等的总/动态/非动态电子相关指数 $I_{\mathrm{D}} = \frac{1}{4}\sum_i\{[\eta_i(1-\eta_i)]^{1/2} − 2\eta_i(1-\eta_i)\}$、$I_{\mathrm{ND}} = \frac{1}{2}\sum_i \eta_i(1-\eta_i)$、$I_{\mathrm{T}} = I_{\mathrm{D}} + I_{\mathrm{ND}}$（η 为自然自旋轨道占据数，>1/为负自动钳位）。

菜单路径：主功能 `200` → 子功能 `15`。

输入要求：含自然轨道占据数的文件（`.mwfn`/`.wfn`/`.wfx`/`.molden`）。

操作步骤（原始格式）：载入文件后进入本功能直接输出三个指数；局域版本见实例。

产出：$I_{\mathrm{T}}$、$I_{\mathrm{D}}$、$I_{\mathrm{ND}}$。

来源链接：[3.200.15](sec-3-200-other-functions-part-2.md#320015-计算电子相关指数)；实例 [4.A.6](sec-4-A-special-topics-and-advanced-tutorials.md#4a6-计算奇电子密度)。

## 子功能 16：基于 .fch/.fchk 密度矩阵生成 NO/NSO/SNO

说明：对角化 `.fch` 中记录的总/SCF/MP2/CI/自旋密度矩阵，生成自然轨道（NO，占据 0–2）、alpha/beta 自然轨道（NSO，占据 0–1）与自旋自然轨道（SNO，占据 −1–1），可导出 `new.mwfn` 继续分析。

菜单路径：主功能 `200` → 子功能 `16`。

输入要求：`.fch`/`.fchk` 文件（含各类密度矩阵记录）。

操作步骤（原始格式，三重态水 CCSD/cc-pVDZ 的 SNO）：

```text
C:\CCSD_water_m3.fch
200
16
CC   // Meaning that we want to analyze coupled-cluster density matrix. You can also input SCF here to analyze Hartree-Fock density matrix
3  // Generate SNOs (if the system is closed-shell, this selection will not occur, since only NOs can be generated in this case)
```

产出：内存轨道更新为 NO/NSO/SNO；选 `y` 导出 `new.mwfn` 并自动载入（SNO 的 mwfn 中只有 alpha 轨道有意义）。

来源链接：[3.200.16](sec-3-200-other-functions-part-2.md#320016-基于-fchfchk-文件中的密度矩阵生成自然轨道自然自旋轨道-nso-和自旋自然轨道-sno)；博客 <http://sobereva.com/403>。

## 子功能 17：计算两轨道之间的 Coulomb 和交换积分

说明：基于均匀格点数值积分算 $(ii|jj)$ 与 $(ij|ji)$，支持波函数文件（输入两轨道编号与格点设置）或两个轨道 cube 文件；$\zeta_J$/$\zeta_K$ 截断值可调（默认即可）。

菜单路径：主功能 `200` → 子功能 `17`。

输入要求：含轨道波函数的文件，或两个轨道 cube 文件；原子坐标、GTFs。

操作步骤（原始格式，水分子 MO4/MO10）：

```text
examples\H2O_iijj.fch  // Containing molecular orbitals at HF/6-31G* level
200  // Other functions (Part 2)
17  // Calculate Coulomb and exchange integrals between two orbitals
4,10  // The two orbitals are selected to be MO4 and MO10
1  // Low-quality grid (corresponding to grid spacing of 0.2 Bohr)
1  // Calculate Coulomb integral with default truncation level. The result is 0.615700
3  // Calculate exchange integral with default truncation level. The result is 0.122246
```

产出：J 与 K 积分（上例低质量格点 0.615700/0.122246，精确值 0.623256/0.129893；中等格点 0.62143/0.12793）。

来源链接：[3.200.17](sec-3-200-other-functions-part-2.md#320017-计算两轨道之间的-coulomb-和交换积分)。

## 子功能 18：计算键长/键级交替（BLA/BOA）以及键角/二面角交替

说明：沿共轭链原子序列算 BLA（偶数键均长 − 奇数键均长）、BOA（Mayer 键级版，禁弥散基）及键角/二面角演化；闭合路径起止原子相同；键数据导出 `bondalter.txt`。

菜单路径：主功能 `200` → 子功能 `18`。

输入要求：原子坐标（同时要键级需基函数、无弥散，如 `.mwfn`/`.fch`/`.molden`；纯 `.xyz`/`.mol2`/`.pdb` 只给键长；连接关系优先用 `.mol`/`.mol2`）。

操作步骤（原始格式）：进入本功能后输入序列原子编号，再输入起止原子编号，检查自动识别的序列；屏幕打印每根键的编号、原子、键长与 Mayer 键级及 BLA/BOA；最后可选输出键角与二面角。实例：噻吩低聚物 BLA/BOA、环[18]碳的键长键角二面角变化。

产出：BLA、BOA 值与 `bondalter.txt` 曲线数据。

来源链接：[3.200.18](sec-3-200-other-functions-part-2.md#320018-计算键长键级交替-blaboa-以及键角二面角交替)；实例 [4.200.18](sec-4-200-other-functions-part-2.md#420018-研究特定路径的键长键级交替blaboa以及键角与二面角的变化)。

## 子功能 19：计算轨道或函数的空间离域指数（SDI）

说明：$\mathrm{SDI} = 1/\sqrt{\int|f_{\mathrm{norm}}|^n}$（默认 n=2，选项 −1 可调），越大越离域；三种模式：(1) 选实空间函数，(2) 输入轨道编号（Becke 积分），(3) 启动时载入 `.cub` 走内存格点模式（均匀格点积分）。

菜单路径：主功能 `200` → 子功能 `19`。

输入要求：轨道波函数文件，或格点数据文件（`.cub`）。

操作步骤（原始格式）：进入本功能后按模式输入实空间函数序号或轨道编号（内存格点模式直接用载入的格点）；选项 `−1` 调整指数 n。

产出：各轨道/函数的 SDI 定量比较（实例：轨道密度 SDI、自旋密度 cube 的 SDI）。

来源链接：[3.200.19](sec-3-200-other-functions-part-2.md#320019-计算轨道或函数的空间离域指数-sdi)；实例 [4.200.19](sec-4-200-other-functions-part-2.md#420019-计算空间离域指数的例子)。

## 子功能 20：键级密度（BOD）与自然适应轨道（NAdO）分析

说明：$\mathrm{BOD}_{AB}(\mathbf{r}) = 2\rho_{AB}(\mathbf{r})$ 全空间积分为离域指数 DI，NAdO 以轨道图像展示 DI 来源；支持原子间（AOM）、basin 间（BOM）与片段间（FOM）三种分析；NAdO 导出 `NAdOs.mwfn`（占据数之和恰为 DI），选 y 载入后可用主功能 0/5/8 可视化 BOD 与 NAdO；选项 −1 可开 NAdO 能量计算（F=SCEC⁻¹ 或外部 Fock 矩阵）。

菜单路径：主功能 `200` → 子功能 `20`（或主功能 `9` → 子功能 `20`）。

输入要求：原子坐标、基函数；AOM/BOM/FOM 文件（模糊原子空间或 basin 模块生成，或主功能 15 子功能 33 生成 FOM）。

操作步骤（原始格式）：选分析类型 1/2/3（片段间再选 FOM 提供方式 3/4），输入两原子/basin 编号或两片段原子范围与 AOM/FOM 文件；生成 `NAdOs.mwfn` 后选 `y` 载入查看。实例：N₂ 键级密度绘制、丁二烯 C–C 键 BOD/NAdO、两片段相互作用。

产出：`NAdOs.mwfn`、BOD 等值面（主功能 5 算电子密度即 BOD）、DI/LI 定量与 NAdO 图像。

来源链接：[3.200.20](sec-3-200-other-functions-part-2.md#320020-键级密度-bod-和自然自适应轨道-nado-分析)；实例 [4.200.20](sec-4-200-other-functions-part-2.md#420020-用键级密度与自然适应性轨道研究化学键)。

## 子功能 21：在占据轨道之间做 Löwdin 正交化

说明：对组合碎片波函数等非正交占据轨道做 Löwdin 正交化，更新内存系数矩阵与密度矩阵；仅支持单行列式闭壳与开壳（后者 alpha/beta 分别正交化）。

菜单路径：主功能 `200` → 子功能 `21`。

输入要求：原子坐标、基函数。

操作步骤（原始格式）：进入本功能一键执行，无额外输入。

产出：内存中正交归一的占据轨道与更新的密度矩阵。

来源链接：[3.200.21](sec-3-200-other-functions-part-2.md#320021-在占据轨道之间做-löwdin-正交化)。
