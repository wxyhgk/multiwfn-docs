# 主功能100：其他功能，第1部分

Multiwfn 功能太多，其中相对“小”、或与波函数分析关系不密切的功能归为“其他功能”。子功能数量庞大，分为第 1 部分（主功能 100，本文件）与第 2 部分（主功能 200）。本文件按子功能编号逐个给出说明、菜单路径、输入要求、操作步骤与产出。

理论与实例来源：[3.100](../sec-3-100-other-functions-part-1.md)、[4.100](../sec-4-100-other-functions-part-1.md)。

## 子功能1：绘制两个函数之间的散点图并生成它们的 cube 文件

### 说明

在共享网格设置下同时生成两个实空间函数的网格数据，可导出 cube、看等值面、绘制散点图。每个散点对应一个网格点，X/Y 分别为函数 1/2 的值；坐标轴范围按最值自动定，有时须用选项 4/5 手动重置，否则几乎看不到点；点大小由 *settings.ini* 中 `symbolsize` 调；选项 1 存图，选项 2 导出 X-Y 数据到 *output.txt*。选项 -2/-3 分别将函数 1 在特定范围内/外处函数 2 的值设为指定值（修改不可恢复）。

### 菜单路径

主功能100 → 子功能1。进入后输入如 `16,14` 选择两个实空间函数（依次为函数 1、函数 2），再选网格设置方式；算完打印 Pearson 相关系数并出现后处理菜单（选项 -1 绘散点图）。

### 输入要求

任意波函数文件。特殊用法：已有两函数 cube（*func1.cub*、*func2.cub*，网格必须完全相同）时，启动输入 *func1.cub*，进子功能 1 选函数时输入 `0,0`，再输入 *func2.cub*，两 cube 网格直接当作函数 1/2 用。

### 产出

Pearson 相关系数、散点图、*output.txt*、两函数 cube 文件。

### 来源

[3.100.1](../sec-3-100-other-functions-part-1.md#31001-绘制两个函数之间的散点图并生成它们的cube文件draw-scatter-graph-between-two-functions-and-generate-their-cube-files)。

## 子功能2：导出各类文件或生成量子化学程序的输入文件

### 说明

文件格式转换器：当前结构输出 .pdb/.xyz/.gro/.cif/.cml；仅有 GTF 时波函数导出 .wfn/.wfx；有基函数时还可导出 .mwfn/.molden/.fch/GENNBO 输入（.47）/旧 Molekel 输入（.mkl）。例如 Gaussian/其它程序产生 .fch/.molden → Multiwfn 转 .mkl → `orca_2mkl test -gbw` 得 *test.gbw* 作 ORCA 初猜（自动脚本见 <http://sobereva.com/517>）。输入为 .chg（含原子信息+电荷）时选项 1 转 .pqr（电荷列同 .chg，半径列为 Bondi vdW 半径；第四列若为自旋布居等也可按之着色；用法见 [4.A.10](../sec-4-A-special-topics-and-advanced-tutorials.md#4a10-通过给原子着色直观展示原子性质)）。

内存有网格数据时（.cub 载入或主功能 5 算得）：选项 35 导出 .cub；选项 36 导出 .vti（ParaView 格式，可同时导出 Bohr 单位 .cml 以便叠加结构）；选项 37 导出 VASP 网格（CHGCAR/LOCPOT 格式）。

生成输入文件：Gaussian、GAMESS-US、ORCA、MOPAC、Dalton、MRCC、Molpro、NWChem、PSI4、CFOUR、Molcas，以及 CP2K、Quantum ESPRESSO。Gaussian/GAMESS-US 有基函数时可选写轨道系数作 SCF 初猜（须手动指定与原波函数相同的基组）。Dalton 可写轨道系数作初猜（如 UHF/UKS 的 UNO 作 CASSCF 初猜，Dalton 本身不支持 UHF/UKS，见 <http://sobereva.com/740>）。ORCA 有专用界面（详见 <http://sobereva.com/490>，UV-Vis/ECD 例子 <http://sobereva.com/485>）。PSI4 输入专为 SAPT 设计。CP2K 输入功能强大（见 <http://sobereva.com/587>）。

### 菜单路径

主功能100 → 子功能2。

### 输入要求

原子坐标；导出 .wfn/.wfx 需 GTF；导出 .mwfn/.fch/.molden/.47 需基函数；导出 cub/vti/VASP 网格需内存网格数据。

### 产出

各类结构/波函数/输入文件；选项 35/36/37 导出网格数据。

### 来源

[3.100.2](../sec-3-100-other-functions-part-1.md#31002-导出各类文件或生成量子化学程序的输入文件export-various-files-or-generate-input-file-of-quantum-chemistry-programs)。

## 子功能3：计算分子范德华体积

### 说明

蒙特卡罗法算 vdW 体积，两种区域定义（*settings.ini* 中 `MCvolmethod` 选择）：(1) 原子 vdW 球叠加（快、无需波函数、不准、忽略电子效应）；(2) 电子密度等值面包围区（0.001 适合孤立体系，0.002 更适合凝聚相）。

原理：盒子体积 $L$ 内随机撒 $N$ 点，$n$ 点落入 vdW 区 → 体积 $n/N\times L$。输入指数 $i$ 定 $N=100\times 2^{i}$（小分子 i=9 一般可接受，大体系逐渐增大至 i 与 i+1 结果收敛）。定义 2 还需输入密度等值面值与盒子因子 $k$（$k$ 太小截断区域，太大则需更多点；等值面 0.001 推荐 $k$=1.7）。

### 菜单路径

主功能100 → 子功能3。

### 输入要求

原子坐标（定义 1）；GTFs（定义 2）。

### 产出

vdW 体积。

### 来源

[3.100.3](../sec-3-100-other-functions-part-1.md#31003-计算分子范德华体积calculate-molecular-van-der-waals-volume)。

## 子功能4：在全空间对函数积分

### 说明

Becke 数值积分（*J. Chem. Phys.*, **88**, 2547 (1988)，DFT 泛函积分法，适用于任何光滑且无穷远趋零的实空间函数）。精度由积分点数定（*settings.ini* 中 `radpot` 径向、`sphpot` 角向）。被积函数选内置或自定义 userfunc（见 sec-2.6、sec-2.7）。`outmedinfo`=1 时导出 *integrate.txt*（序号、坐标、函数值、Lebedev 权重、原子权重）。

隐藏功能 -4/-5：检验两波函数文件间某实空间函数差异，被积分别为 $[f\,(\text{file1})-f\,(\text{file2})]^2$ 或 $\left|f\,(\text{file1})-f\,(\text{file2})\right|$（file1 为启动载入文件，file2 功能内选；可设电子密度判据只算低密度区忽略核区）。算后自动导出 file1 网格纯文本（如 *a.wfn_003_0075_0434* 表 file1=a.wfn、函数 3、径向 75 角向 434），条件相符时直接载入省时间。

选 ELF 自动输出球对称平均 ELF $r_{\mathrm{ELF}}$（*J. Comput. Chem.*, **38**, 2258 (2017)，用于定 universal range-separated 泛函最优 ω）：

$$
\begin{gathered}r_{\mathrm{ELF}}=\sqrt{\frac{\int \mathrm{ELF}(\mathbf{r})\mathbf{r}^2\mathrm{ELF}(\mathbf{r})\mathrm{d}\mathbf{r}}{\int \mathrm{ELF}(\mathbf{r})\mathrm{ELF}(\mathbf{r})\mathrm{d}\mathbf{r}}}\end{gathered}
$$

选 LOL 输出 $r_{\mathrm{LOL}}$（LOL-tuning，*J. Phys. Chem. C*, **123**, 4407 (2019)）：

$$
\begin{gathered}r_{\mathrm{LOL}}=\sqrt{\frac{\int \mathrm{LOL}(\mathbf{r})\mathbf{r}^2\mathrm{LOL}(\mathbf{r})\mathrm{d}\mathbf{r}}{\int \mathrm{LOL}(\mathbf{r})\mathrm{LOL}(\mathbf{r})\mathrm{d}\mathbf{r}}}\end{gathered}
$$

### 菜单路径

主功能100 → 子功能4（隐藏 -4/-5 比较两文件）。

### 输入要求

原子坐标、GTFs；比较两文件时另需第二个波函数文件。

### 操作步骤（实例 4.100.4：光气动能与核吸引势能）

```text
examples\COCl2.wfn  // HF/6-31G* wavefunction
100  // Other functions (Part 1)
4  // Integrate a function over the whole space
6  // Hamiltonian kinetic density K(r)
```

结果 1031.1092（Gaussian 1031.1107）。核吸引势能是 userfunc 内置（`iuserfunc`=12：`userfunc = -nucesp(x,y,z)*fdens(x,y,z)`；r² 期望是 `iuserfunc`=3），无需改源码重编译：设 *settings.ini* 中 `iuserfunc` 为 12（或 3），选被积函数 100（userfunc）重做即可。核吸引得 −2839.1668（Gaussian −2839.1629）；r² 期望得 444.6523（主功能 300 子功能 5 解析值 444.652363）。特定轨道贡献：先用主功能 6 子功能 26 把其余轨道占据置零再积分。

### 产出

被积函数全空间积分值（动能、核吸引、球平均 ELF/LOL 等）。

### 来源

[3.100.4](../sec-3-100-other-functions-part-1.md#31004-在全空间对函数积分integrate-a-function-over-the-whole-space)、[4.100.4](../sec-4-100-other-functions-part-1.md#41004-通过数值积分-numerical-integration计算光气-phosgene的动能-kinetic-energy和核吸引势能-nuclear-attraction-potential-energy)。

## 子功能5：显示 alpha 和 beta 轨道之间的重叠积分

### 说明

非限制波函数 α/β 轨道一般不正交归一。计算重叠矩阵：

$$
\begin{gathered}S_{i,j}^{\alpha\beta}=\int \varphi_{i}^{\alpha}(\mathbf{r})\varphi_{j}^{\beta}(\mathbf{r})\mathrm{d}\mathbf{r}\end{gathered}
$$

对角元明显偏离 1 → 自旋极化显著。选项 1：完整矩阵（对角元打印屏幕，全矩阵可选存 *ovlpmat.txt*，另给最大配对；大体系可能耗时）＋ 输出单行列式 $\langle S^2\rangle$：

$$
\begin{gathered}\left\langle S^2 \right\rangle_{\mathrm{SD}}=\left\langle S^2 \right\rangle_{\mathrm{exact}}+N^{\beta}-\sum_{i}^{N^{\alpha}}\sum_{j}^{N^{\beta}}\left| S_{i,j}^{\alpha\beta} \right|^2\end{gathered}
$$

$$
\begin{gathered}\left\langle S^2 \right\rangle_{\mathrm{exact}}=S(S+1)=\frac{N^{\alpha}-N^{\beta}}{2}\left( \frac{N^{\alpha}-N^{\beta}}{2}+1 \right)\end{gathered}
$$

选项 2：只算对角元（总是很快）。

### 菜单路径

主功能100 → 子功能5。

### 输入要求

GTFs（非限制波函数）。

### 产出

重叠矩阵/对角元、最大配对、$\langle S^2\rangle$。

### 来源

[3.100.5](../sec-3-100-other-functions-part-1.md#31005-显示alpha和beta轨道之间的重叠积分show-overlap-integral-between-alpha-and-beta-orbitals)。

## 子功能6：监控 Gaussian 的 SCF 收敛过程

### 说明

路线须 `#P` 否则无中间信息。进入后屏幕打印各步信息与收敛阈值，例如：

```text
Step#   RMSDP  Conv?   MaxDP  Conv?     DE    Conv?
    8  3.51D-06  NO   5.15D-05  NO   -8.43D-08  YES
    9  1.37D-06  NO   9.11D-06  NO   -2.17D-09  YES
   10  3.03D-07  NO   2.91D-06  NO   -3.75D-10  YES
   11  3.12D-08  NO   4.76D-07  YES  -1.07D-11  YES
   12  7.69D-09  YES  5.72D-08  YES  -1.56D-13  YES
Goal   1.00D-08       1.00D-06        1.00D-06
 SCF done!
```

同时弹窗画能量/密度矩阵最大与 RMS 变化曲线（关窗后可选相应选项在指定步数范围重画，Y 轴自动调）。输出文件更新时每次重载 → 显示最新；耗时 SCF 可停留此界面隔段选选项 2 看最近 5 步趋势。灰虚线 Y=0，红虚线收敛阈值；最右 `Done` 表该项收敛。兼容 `SCF=QC`/`XQC`，不兼容 `SCF=DM`。

### 菜单路径

主功能100 → 子功能6。

### 输入要求

Gaussian 输出文件（路线含 #P）。

### 产出

收敛表 + 能量/密度矩阵变化曲线。

### 来源

[3.100.6](../sec-3-100-other-functions-part-1.md#31006-监控gaussian的scf收敛过程monitor-scf-convergence-process-of-gaussian)。

## 子功能8：生成以碎片波函数组合为初猜的 Gaussian 输入文件

### 说明

三用途：(1) 为复合物生成高质量初猜（碎片已收敛、相互作用不强时加速 SCF）；(2) 简单能量分解（强烈建议改用 sobEDA/sobEDAw，*J. Phys. Chem. A*, **127**, 7023 (2023)，教程 <http://sobereva.com/soft/sobEDA_tutorial.zip>）；(3) 建模反铁磁耦合体系。

能量分解公式：

$$
\Delta E_{\mathrm{tot}} = E^{\mathrm{complex}} - \sum_{i} E_{i}^{\mathrm{frag}} = \left( \Delta E_{\mathrm{els}} + \Delta E_{\mathrm{XC}} + \Delta E_{\mathrm{Pauli}} \right) + \Delta E_{\mathrm{orb}} = \Delta E_{\mathrm{steric}} + \Delta E_{\mathrm{orb}}
$$

$$
\Delta E_{\mathrm{orb}}=E_{\mathrm{SCF,last}}-E_{\mathrm{SCF,1st}}
$$

$$
\Delta E_{\mathrm{steric}} = \Delta E_{\mathrm{tot}} - \Delta E_{\mathrm{orb}} = E_{\mathrm{SCF,1st}} - \sum_{i} E_{i}^{\mathrm{frag}}
$$

色散评估两法：(1) $\Delta E_{\mathrm{disp}}=\Delta E_{\mathrm{tot}}^{\mathrm{MP2}}-\Delta E_{\mathrm{tot}}^{\mathrm{HF}}$；(2) 无色散 DFT/HF 相互作用能 + Grimme DFT-D3 校正（见 <http://sobereva.com/210>）。

反铁磁示例 Mn₂O₂(NH₃)₈（基态单重态、两 Mn 高自旋反平行；限制闭壳层不适用，默认初猜回塌到闭壳层）：四碎片各算（`nosymm pop=full`）：碎片1 左 Mn(NH₃)₄（+2，六重态）、碎片2 右 Mn(NH₃)₄（+2，六重态）、碎片3/4 各一桥氧（−2，单重态）。先载入 *frag1.out* 进子功能 8，输入 `4`，依次输入 *frag2/3/4.out*；每碎片问是否翻转自旋——仅碎片2 选 `y`（自旋向下抵消碎片1，多重度 1）。得 *new.gjf*（注释 `!` 后标明各复合物 MO 来源，如 `! Alpha orbital:    12 Occ:  1.000000 from fragment   2` 接系数，前 8 个属碎片1基函数故为零）。用弥散函数 Link401 报错可加 `IOp(3/32=2)`。

### 菜单路径

主功能100 → 子功能8。输入碎片总数并依次载入（首个为启动时已载入文件），可选翻转碎片自旋，得 *new.gjf*。

### 输入要求

各碎片 Gaussian 输出文件（`nosymm pop=full`）。

### 操作步骤（实例 4.100.8：NH₃BH₃ 简单能量分解，B3LYP/6-31G*，文件 *examples\EDA\EDA_simple*，G16 B.01）

- (1) 优化 NH₃BH₃，用优化坐标建 *NH3BH3.gjf*；(2) 复制为 *NH3.gjf*/*BH3.gjf*，分别删去另一碎片，加 `pop=full nosymm`；(3) 运行得 *NH3.out*、*BH3.out*；(4) 启动：

```text
NH3.out  // Fragment 1
100  // Other functions (Part 1)
8  // Generate Gaussian input file with initial     guess combined from fragment wavefunctions
2  // There are two fragments in total
BH3.out  //Fragment 2
```

得 *new.gjf*；(5) 确保有 `nosymm`，`#` 改 `#P`（每迭代打印能量），可删 `pop=full`；(6) 运行得 *new.out*。

能量：*E*(NH₃)=−56.5477099，*E*(BH₃)=−26.5929634，*E*(NH₃BH₃)=$E_{\mathrm{SCF,last}}$=−83.2132069；*new.out* 第 639 行 $E_{\mathrm{SCF,1st}}$=−83.12546124。

$\Delta E_{\mathrm{tot}}$ = −0.0725336 a.u. = −190.44 kJ/mol；$\Delta E_{\mathrm{orb}}$ = −0.0877456 a.u. = −230.37 kJ/mol；$\Delta E_{\mathrm{steric}}$ = +0.017218 a.u. = +39.93 kJ/mol。色散本体系可忽略；弱作用复合物须另评估色散。

### 产出

*new.gjf*（碎片组合初猜）；首末 SCF 能量差即轨道作用能。

### 来源

[3.100.8](../sec-3-100-other-functions-part-1.md#31008-生成以碎片波函数组合为初猜的gaussian输入文件generate-gaussian-input-file-with-initial-guess-combined-from-fragment-wavefunctions)、[4.100.8](../sec-4-100-other-functions-part-1.md#41008-使用组合的碎片波函数-fragment-wavefunction进行简单的能量分解-energy-decomposition)。

## 子功能9：计算原子间连接性和原子配位数

### 说明

DFT-D3 配位数思想（*J. Chem. Phys.*, **132**, 154104 (2010)；Pyykkö 共价半径 *Chem. Eur. J.*, **15**, 186 (2009)）。连接性指数：

$$
I_{AB}(r_{AB}) = \frac{1}{1 + \exp\{-16 \times [(4/3)(R_{A} + R_{B}) / r_{AB} - 1]\}}
$$

$$
CN_{A} = \sum_{B \neq A} \frac{1}{1 + \exp\{-16 \times [(4/3)(R_{A} + R_{B}) / r_{AB} - 1]\}}
$$

$I$ 接近 1 成键、接近 0 无键；$I$ 不可用作键级（无成键类型/强度分辨）。输出每对原子 $I$（可设打印阈值）与最接近整数 nint($I$)；每原子“连接性之和”（粗略配位数）与“整数连接性之和”（实际配位数）；可选导出 *connmat.txt* 矩阵。乙炔示例输出：

```text
    1C   ---    2C  :   0.99951   Nearest integer:  1
    1C   ---    3H  :   0.99974   Nearest integer:  1
    2C   ---    4H  :   0.99974   Nearest integer:  1

    1  C   Sum of connectivity:  2.0016   Sum of integer connectivity:  2
    2  C   Sum of connectivity:  2.0016   Sum of integer connectivity:  2
    3  H   Sum of connectivity:  1.0021   Sum of integer connectivity:  1
    4  H   Sum of connectivity:  1.0021   Sum of integer connectivity:  1
```

### 菜单路径

主功能100 → 子功能9。

### 输入要求

原子坐标。

### 产出

原子对 $I$、每原子连接性和、可选 *connmat.txt*。

### 来源

[3.100.9](../sec-3-100-other-functions-part-1.md#31009-计算原子间连接性和原子配位数evaluate-interatomic-connectivity-and-atomic-coordination-number)。

## 子功能11：计算两个轨道之间的重叠和质心距离

### 说明

用于电荷转移分析等。输入两轨道序号，质心：

$$
\begin{gathered} X_{i} = \int \left| \varphi_{i}(\mathbf{r}) \right|^{2} x \, \mathrm{d}\mathbf{r} \quad\quad Y_{i} = \int \left| \varphi_{i}(\mathbf{r}) \right|^{2} y \, \mathrm{d}\mathbf{r} \quad\quad Z_{i} = \int \left| \varphi_{i}(\mathbf{r}) \right|^{2} z \, \mathrm{d}\mathbf{r} \end{gathered}
$$

$$
D_{ij} = \sqrt{\left( X_{i} - X_{j} \right)^{2} + \left( Y_{i} - Y_{j} \right)^{2} + \left( Z_{i} - Z_{j} \right)^{2}}
$$

重叠程度（直接算波函数重叠因正交归一恒零、无意义，故算下两量，Becke 格点数值积分，`radpot`/`sphpot` 可调）：

$$
\begin{gathered} \int \left| \varphi_{i}(\mathbf{r}) \right| \left| \varphi_{j}(\mathbf{r}) \right| \mathrm{d}\mathbf{r} \quad\quad \int \left| \varphi_{i}(\mathbf{r}) \right|^{2} \left| \varphi_{j}(\mathbf{r}) \right|^{2} \mathrm{d}\mathbf{r} \end{gathered}
```

算完可问是否把两质心作为虚拟原子（Bq）加入 → 主功能 0 以透明/网格风格看轨道等值面与质心对应关系。

### 菜单路径

主功能100 → 子功能11，输入两轨道序号。

### 输入要求

GTFs、原子坐标。

### 产出

质心距离、两类重叠量、可选质心虚拟原子。

### 来源

[3.100.11](../sec-3-100-other-functions-part-1.md#310011-计算两个轨道之间的重叠和质心距离calculate-overlap-and-centroid-distance-between-two-orbitals)。

## 子功能12：alpha 与 beta 轨道之间的双正交化

### 说明

UHF/UKS 的 α/β 轨道常不匹配，分析须同时看两套；ROHF/ROKS 无此问题但能量/分布不如非限制准。本功能对多重度>1 非限制开壳层做双正交化：两套轨道各自正交归一、且 α 与异号 β 正交；变换后同号轨道几乎完美匹配，之后只讨论一套即可。

SVD 实现：**O**=**UΣV**†（**O** 为 α/β 重叠矩阵，奇异值≈1 为正常），新系数 $\mathbf{C}_{\mathrm{biortho}}^{\alpha} = \mathbf{U}\mathbf{C}_{\mathrm{original}}^{\alpha}$，$\mathbf{C}_{\mathrm{biortho}}^{\beta} = \mathbf{V}\mathbf{C}_{\mathrm{original}}^{\beta}$（**U**、**V** 酉 → 可观测量不变）。分三步（防占据-空混合改变性质；步骤 2/3 的 **O** 基于上步更新系数重建；记 α/β 电子数 $n_α$、$n_β$（$n_α$>$n_β$），总数 $n_{\mathrm{tot}}$）：(1) 占据α(1~$n_α$)与占据β(1~$n_β$)；(2) α($n_β$+1~$n_α$)与虚β($n_β$+1~$n_{\mathrm{tot}}$)（得“单占据”配对）；(3) 虚α($n_α$+1~$n_{\mathrm{tot}}$)与剩余虚β($n_α$+1~$n_{\mathrm{tot}}$)。结果近乎一一配对（非严格正交，否则须混占据/空）。可跳过步骤 3（此时 $n_α$+1~$n_{\mathrm{tot}}$ 的轨道无意义）。

轨道能量（非 Fock 本征函数，能量为相应自旋 Fock 期望）：$\mathbf{F}_{\mathrm{biortho}}^{\alpha} = (\mathbf{C}^{\alpha})^{\mathrm{T}} \mathbf{F}_{\mathrm{AO}}^{\alpha} \mathbf{C}^{\alpha}$（β 同），对角元即能量。α/β 有效势不同 → 同形轨道能量可显著不同。排序按同号 α/β 平均能量，且三批（1~$n_β$）、（$n_β$+1~$n_α$）、（$n_α$+1~$n_{\mathrm{tot}}$）分别单独排序。

### 菜单路径

主功能100 → 子功能12。程序依次问：是否对未占据 MO 做、是否算能量、是否按能量排序。Fock 矩阵可由 **F**=**SCEC**⁻¹ 从 MO 能量系数生成，或从文件载入（见附录 7）。

### 输入要求

UHF/UKS 含基函数文件（.mwfn/.fch/.molden/.gms）。

### 操作步骤（实例 4.100.12：三重态乙醇 *examples\ethanol_triplet.fch*，14 α占据、12 β占据）

```text
examples\ethanol_triplet.fch
100  // Other functions (Part 1)
12  // Perform biorthogonalization between alpha and beta orbitals
2  // Do biorthogonalization for all orbitals
0  // Do not evaluate energies of biorthogonalized orbitals
```

第一步输出示例：

```text
 Doing biorthogonalization for alpha    1 to   14, Beta    1 to   12
 Singular values of orbital overlap matrix:
   1.0000   1.0000   1.0000   1.0000   1.0000   1.0000   1.0000   0.9999
   0.9999   0.9998   0.9995   0.9992
```

三步后得 *biortho.txt*（奇异值+占据数，计能量时还有能量）：

```text
S = Singular value, E = Energy (in eV), O= Occupancy, A=Alpha, B=Beta

 Orb:     1   S= 1.0000   O(A)= 1.0   O(B)= 1.0
...[ignored]
 Orb:    11   S= 0.9995   O(A)= 1.0   O(B)= 1.0
 Orb:    12   S= 0.9992   O(A)= 1.0   O(B)= 1.0
 -----------------------------------------------
 Orb:    13   S= 1.0000   O(A)= 1.0   O(B)= 0.0
 Orb:    14   S= 1.0000   O(A)= 1.0   O(B)= 0.0
 -----------------------------------------------
 Orb:    15   S= 1.0000   O(A)= 0.0   O(B)= 0.0
 Orb:    16   S= 1.0000   O(A)= 0.0   O(B)= 0.0
...[ignored]
```

*biortho.fch* 含双正交化轨道（未算能量时“轨道能量”栏为奇异值）。输入 `y` 即载入，主功能 0 可见 α/β 完美匹配；轨道 13/14 即 SOMO（自旋密度仅由其贡献）；对比单重态乙醇 HOMO/LUMO 可知三重态跃迁即 HOMO→LUMO。双正交化不改变可观测量；未算能量时能量栏无意义、顺序不反映能量。

计能量并排序：

```text
examples\ethanol_triplet.fch
100  // Other functions (Part 1)
12  // Biorthogonalization between alpha and beta orbitals
2  // Perform biorthogonalization for all orbitals
1  // Evaluate energies of the biorthogonalized orbitals using the Fock matrix generated by MO energies and coefficients via F=SCEC^-1 relationship
y  // Ordering the biorthogonalized orbitals according to their energies
```

*biortho.txt* 内容如：

```text
...[ignored]
 Orb:    11   S= 0.9992  E(A)=    -13.057  O(A)= 1.0  E(B)=    -11.821  O(B)= 1.0
 Orb:    12   S= 1.0000  E(A)=    -11.918  O(A)= 1.0  E(B)=    -11.866  O(B)= 1.0
 -------------------------------------------------------------------------------
 Orb:    13   S= 1.0000  E(A)=    -11.439  O(A)= 1.0  E(B)=     -5.806  O(B)= 0.0
 Orb:    14   S= 1.0000  E(A)=     -0.293  O(A)= 1.0  E(B)=      2.817  O(B)= 0.0
 -------------------------------------------------------------------------------
 Orb:    15   S= 0.9992  E(A)=     13.876  O(A)= 0.0  E(B)=     15.431  O(B)= 0.0
 Orb:    16   S= 1.0000  E(A)=     15.057  O(A)= 0.0  E(B)=     15.305  O(B)= 0.0
...[ignored]
```

配对轨道能量可差明显（如 α11 −13.057 vs β11 −11.821 eV）。也可用外部 Fock（如 .47 文件，*examples\ETHANOL_TRIPLET.47*，Gaussian 跑 *examples\ethanol_triplet_47.gjf* 得；选 `2 Evaluate, loading Fock matrix from a file`）。双自由基等自旋极化单重态例子见博文 <http://sobereva.com/448>。

### 产出

*biortho.txt*、*biortho.fch*（`y` 直接载入分析/作图）。

### 来源

[3.100.12](../sec-3-100-other-functions-part-1.md#310012-alpha与beta轨道之间的双正交化biorthogonalization-between-alpha-and-beta-orbitals)、[4.100.12](../sec-4-100-other-functions-part-1.md#410012-非限制性开壳层波函数-unrestricted-open-shell-wavefunction轨道的双正交化-biorthogonalization分析)。

## 子功能14：计算 LOLIPOP

### 说明

LOLIPOP（*Chem. Commun.*, **48**, 9239 (2012)）衡量芳香环 π 堆积能力：值越小 π 缺乏越强 → 堆积越强。定义：LOL-π（纯 π 轨道贡献的 LOL）从距分子平面 0.5 Å 起的定积分，只计 LOL-π>0.55 的点；积分域为垂直分子平面的圆柱（半径默认 1.94 Å = 苯 C/H 环半径均值）。选项 3/4 改半径/高度；选项 1 先选 π 轨道；选项 0 触发（按连接顺序输入环原子序号）算环周围 LOL-π 网格再积分（默认间距 0.08 Bohr，一般够细）。选项 5 只计单侧；选项 7 计算后显示 LOL-π 等值面检查；选项 6 导出 *pt.xyz*（实际贡献点，VMD 看分布）。

### 菜单路径

主功能100 → 子功能14。

### 输入要求

GTFs、原子坐标（非平面体系先定域出 π LMO，见 4.100.14.2）。

### 操作步骤（实例 4.100.14.1：菲，完全平面，*examples/phenanthrene.wfn*）

```text
examples/phenanthrene.wfn
100  // Other functions (Part 1)
14  // Calculate LOLIPOP
1  // Choose π orbitals that to be taken into account
36,40,43,44,45,46,47  // Indices of π orbitals. You can manually find out π orbitals by visualizing orbital isosurfaces via main function 0, or let Multiwfn automatically identify π orbitals by subfunction 22 of main function 100
0  // Start the calculation
8,9,11,13,14,15  // The indices of the atoms in the ring that you are interested in. This ring is boundary ring. Note that you should input the indices according to atomic connectivity
```

边缘环 8.23；再输入 `0` + `7,3,4,8,9,10`（中央环）得 6.39 → 中央环堆积趋势更强。选项 6 导出 *pt.xyz*（VMD Points 显示）验证积分点分布合理。

非平面例 4.100.14.2 联苯（*examples\biphenyl.fch*，须含基函数以定域化）：

```text
examples\biphenyl.fch
19  // Orbital localization
1  // Only localize occupied MOs
100  // Other function (Part 1)
22  // Automatically detect π orbitals
-1  // Current orbitals are in localized form
0  // Start π orbital identification based on default settings
```

识别出 6 个 π LMO：

```text
Expected pi orbitals, occupation numbers and orbital energies (eV):
    32      2.000000    -10.110351
    34      2.000000     -9.633443
    38      2.000000     -7.386451
    39      2.000000     -6.768520
    40      2.000000     -6.755193
    41      2.000000     -6.046329
```

```text
0  // Do not modify orbital occupation numbers
14  // LOLIPOP calculation
1  // Choose π orbitals
32,34,38,39,40,41  // The indices of the π orbitals
0  // Start calculation
1,2,3,4,5,6  // Indices of the atoms in a ring
```

结果 8.82（略高于菲边缘环，π-π 堆积能力显著）。选项 5 选单侧 + 选项 6 导出点：单侧 4.41（恰一半，分布对称）。

### 产出

LOLIPOP 值、可选 *pt.xyz* 积分点。

### 来源

[3.100.14](../sec-3-100-other-functions-part-1.md#310014-计算lolipopcalculate-lolipop-lol-integrated-pi-over-plane)、[4.100.14](../sec-4-100-other-functions-part-1.md#410014-计算-lolipop-指数)。

## 子功能15：计算分子间轨道重叠

### 说明

$$
\begin{gathered}S_{i,j}^{\mathrm{inter}}=\int \varphi_{i}^{\mathrm{monomer1}}(\mathbf{r})\varphi_{j}^{\mathrm{monomer2}}(\mathbf{r})\mathrm{d}\mathbf{r}\end{gathered}
$$

讨论分子间电荷转移有用（*J. Phys. Chem. B*, **106**, 2093 (2002)）。需三文件（任含基函数文件）：(1) 二聚体（先载入）；进模块后依次输入 (2) 单体1、(3) 单体2。输入如 `8,15` 得 $S_{8,15}^{\mathrm{inter}}$；输入 `o` 全矩阵存 *ovlpint.txt*。(2)(3) 坐标须与 (1) 一致、原子顺序相同、基组相同；二聚体中 A 在 B 前则须先载入 A。Gaussian 用户也可用输出文件（不推荐，精度略低）：(1) 二聚体输出（`IOp(3/33=1) nosymm guess=only`，读重叠矩阵；加 `pop=none` 省系数输出）；(2)(3) 单体输出（`nosymm pop=full`，读系数）。

### 菜单路径

主功能100 → 子功能15。

### 输入要求

二聚体 + 两单体含基函数文件（坐标/顺序/基组一致）。

### 操作步骤（实例 4.100.15：DB-TTF 二聚体，B3LYP/6-31G*，MO78=HOMO、MO79=LUMO，CSD 结构，输入文件 *examples\intermol\\*，或下载 <http://sobereva.com/multiwfn/extrafiles/intermol.rar>）

单体坐标取自二聚体（单体1原子在前），均 `nosymm`；二聚体用 `guess(save,only)` 只存初猜（MO 不用）。启动：

```text
DB-TTFdimer.fchk  // Wavefunction file of dimer
100  // Other functions (Part 1)
15  // Function for calculating intermolecular orbital overlap integral
DB-TTF1.fchk  // Wavefunction file of monomer 1
DB-TTF2.fchk  // Wavefunction file of monomer 2
```

输入 `78,78` 得 HOMO-HOMO −0.01411983；`79,79` 得 LUMO-LUMO 0.01025897。中文版见 <http://sobereva.com/163>。

### 产出

指定轨道对重叠积分 / 全矩阵 *ovlpint.txt*。

### 来源

[3.100.15](../sec-3-100-other-functions-part-1.md#310015-计算分子间轨道重叠calculate-intermolecular-orbital-overlap)、[4.100.15](../sec-4-100-other-functions-part-1.md#410015-计算-db-ttf-的分子间轨道重叠积分-intermolecular-orbital-overlap-integral)。

## 子功能17：基于轨道能量和系数生成 Fock/KS 矩阵

### 说明

原理 HF/KS 方程 **FC**=**SCE** → **F**=**SCEC**⁻¹（HF 得 Fock，DFT 得 KS）。载入含全部轨道的基函数文件（.fch/.molden/.mwfn/.gms）进子功能 17，输入纯文本路径，以下三角形式导出：$F(1,1)\,F(2,1)\,F(2,2)\,F(3,1)\dots F(n_{\mathrm{basis}},n_{\mathrm{basis}})$；非限制分别输出 Fa、Fb 两组。精度略低于程序原生矩阵（数值误差，但差很小）。线性依赖被删基函数时不可用（MO 数 < 基函数数；多见弥散函数大量使用时）。

### 菜单路径

主功能100 → 子功能17。

### 输入要求

含基函数与全部轨道的文件（无线性依赖删除）。

### 操作步骤（为 *examples\ClPO2.fch* 生成 KS 矩阵）

```text
examples\ClPO2.fch
100
17
ClPO2_KSmat.txt
```

当前目录得下三角 KS 矩阵文件（符合其它需 Fock/KS 文件功能的要求）。

### 产出

下三角 Fock/KS 矩阵文本文件。

### 来源

[3.100.17](../sec-3-100-other-functions-part-1.md#310017-基于轨道能量和系数生成fockks矩阵generate-focks-matrix-based-on-orbital-energies-and-coefficients)。

## 子功能18：Yoshizawa 电子输运路径分析

### 说明

基于 Yoshizawa 公式（*Acc. Chem. Res.*, **45**, 1612 (2012)）：费米能处零阶格林函数：

$$
G_{rs}^{(0)\mathrm{R/A}}\left( E_{\mathrm{F}} \right) = \sum_{k} \frac{C_{rk} C_{sk}^{\ast}}{E_{\mathrm{F}} - \varepsilon_{k} \pm i\eta}
$$

只计 HOMO/LUMO 时：

$$
G_{rs}^{(0)\mathrm{R/A}}\left( E_{\mathrm{F}} \right) = \frac{C_{r\mathrm{HOMO}} C_{s\mathrm{HOMO}}^{\ast}}{E_{\mathrm{F}} - \varepsilon_{\mathrm{HOMO}} \pm i\eta} + \frac{C_{r\mathrm{LUMO}} C_{s\mathrm{LUMO}}^{\ast}}{E_{\mathrm{F}} - \varepsilon_{\mathrm{LUMO}} \pm i\eta}
$$

$r$、$s*两格点* $C$ 绝对值大、且 HOMO/LUMO 相对相位不同 → |G| 大 → 透射有利（G 正负无意义，只看绝对值）。Multiwfn 忽略 iη；系数来自 NBO `NAOMO`；只考虑 π 轨道（σ 对电导贡献小），分子平面须平行 XY/YZ/XZ 之一。

输入文件二选一：(1) 仅 Gaussian 输出（路线 `pop=nboread`，末行 `$NBO NAOMO $END`，如 `#P b3lyp/6-31g* pop=nboread`）；(2) 先载入含基函数文件，进功能后再载入 NBO 输出（GENNBO 则 .47 的 $NBO…$END 加 `NAOMO`）。

菜单：先选分子平面（XY/YZ/XZ），程序找垂直该面的 Val 型 p 自然原子轨道并加载 MO 系数。选项：-4 距离判据（下/上限，选项 2/3 超出不显示）；-3 数值判据（选项 1 贡献小于此 MO 不显示；选项 2/3 |G| 小于此路径不显示）；-2 设费米能 $E_F$；-1 选 MO 范围；0 看结构；1 两原子输运细节（输 $r$、$s$，输出 $G_{rs}$ Total 值 + 每 MO 贡献 + 距离 + 仅 HOMO/LUMO 的 $G$）；2 全部路径排序输出（满足 -3/-4 者，按 |G| 排）；3 某原子全部路径。

### 菜单路径

主功能100 → 子功能18。

### 输入要求

含 NAOMO 的 Gaussian/NBO 输出（见上）。

### 操作步骤（实例 4.100.18：菲，*examples\phenanthrene_NAOMO.out*）

```text
examples\phenanthrene_NAOMO.out  //The Gaussian output file containing "NAOMO" matrix
100  // Other functions (Part 1)
18  // Yoshizawa's electron transport route analysis
2  // Select YZ plane, which is the molecular plane
```

选 1，输入 `2,11`：传输概率 0.855879（每 MO 贡献、距离 5.674656 Å、仅 HOMO+LUMO 时 2.144432 → HOMO/LUMO 近似定量不成立）。只看 HOMO/LUMO：选 -1 输入 `47,48`，再选 2：

```text
Note: The routes whose absolute value <  0.010000 will not be shown
Note: The routes whose distance <    0.0000 or > 9999.0000 Angstrom will not be shown
Atom    7 -- Atom   10  Value and distance:    3.743670    1.359562
Atom    6 -- Atom   10  Value and distance:    3.098919    5.081382
Atom    7 -- Atom   14  Value and distance:    3.098919    5.081382
Atom    7 -- Atom   11  Value and distance:   -2.831680    3.720990
Atom    2 -- Atom   10  Value and distance:   -2.831680    3.720990
Atom    6 -- Atom   14  Value and distance:    2.565337    5.765892
...
Atom    6 -- Atom    9  Value and distance:   -0.016585    4.927289
Atom    3 -- Atom   14  Value and distance:   -0.016585    4.927289
Atom    2 -- Atom    4  Value and distance:   -0.014931    2.456189
Atom    8 -- Atom   11  Value and distance:   -0.014931    2.456189
```

忽略三碳连接与对称重复，最有利四路径 7-10、6-10、7-11、6-14，与 Yoshizawa 原文图一致（9-10 即 7-10 距离太近无法搭结故原文未标）。选 3 输入 `2` 看原子 2 出发的路径：

```text
To atom    10    Value and distance (Angstrom):   -2.831680    3.720990
To atom    14    Value and distance (Angstrom):   -2.344569    6.206600
To atom    11    Value and distance (Angstrom):    2.144432    5.674656
To atom     5    Value and distance (Angstrom):   -1.571512    2.787501
...
```

2-10 最有利。

### 产出

原子对透射 $G$ 值/各 MO 贡献/排序路径表。

### 来源

[3.100.18](../sec-3-100-other-functions-part-1.md#310018-yoshizawa电子输运路径分析yoshizawas-electron-transport-route-analysis)、[4.100.18](../sec-4-100-other-functions-part-1.md#410018-菲-phenanthrene-的-yoshizawa-电子传输路径分析-yoshizawas-electron-transmission-route-analysis)。

## 子功能19：通过组合碎片波函数生成新波函数

### 说明

组合碎片波函数得新波函数（.wfn/.fch/.mwfn），电子分布即碎片叠加（无极化/电荷转移），每组合轨道直接对应某碎片轨道。可组合无穷多碎片：导出 .wfn 时碎片可任格式；导出 .mwfn/.fch 则碎片须含基函数（.fch/mwfn/molden/gms）。先载入碎片 1，进子功能 19 选导出格式，输入总数 $N$，依次输入其余碎片路径。轨道按占据数降序。任一碎片非限制开壳层 → 组合也非限制（α/β 分列），每开壳层碎片问是否翻转自旋（`y` 则 α/β 互换；自由基拼人工波函数时有用）。ghost 原子特殊情形：各碎片同基函数同原子（仅 ghost 选择不同、实原子并集恰为全体系）→ 输入碎片数负数；仅支持单行列式，只取占据轨道（.fch/.mwfn 虚轨道系数能量置零），全记实原子。

### 菜单路径

主功能100 → 子功能19。

### 输入要求

各碎片波函数文件（导出格式要求见上）。

### 操作步骤（实例 4.100.19：COBH₃ 前分子波函数，文件 *examples\genpromol\COBH3*；前分子 ELF 不能由碎片 ELF 相加得到（非线性），须先合并波函数再算）

```text
examples\genpromol\COBH3\CO.wfn  // The path of wavefunction file of fragment 1
100  // Other functions (Part 1)
19  // Generate promolecular .wfn file from fragment wavefunctions
1  // Output to combine.wfn
2  // Two fragments in total
examples\genpromol\COBH3\BH3.wfn  // The path of wavefunction file of fragment 2
```

得 *combine.wfn*。重启载入画 ELF 平面：

```text
combine.wfn
4  // Draw plane map
9  // ELF
1  // Color-filled map
[Press ENTER button]
2  // XZ plane
0  // Y=0
```

前分子态下 C-B 间似已成键。画实际−前分子 ELF 差值：重启载入 *examples\genpromol\COBH3\COBH3.wfn*：

```text
examples\genpromol\COBH3\COBH3.wfn  // Wavefunction file of actual state of COBH_3
4  // Draw plane map
0  // Custom operation
1  // Deal with only one file
-,combine.wfn  // Subtracting property of COBH3.wfn by that of combine.wfn
9  // ELF
1  // Color-filled map
[Press ENTER button]  // Use default grid setting
2  // XZ plane
0  // Y=0
```

关图后：

```text
1  // Set lower and upper limit of color scale
-0.2,0.4  // Set the color scale from -0.2 to 0.4, since as you can see from the command-line window, in this plane the data range is from -0.248 to 0.436
2  // Enable showing contour lines
4  // Enable showing atom labels
1  // Red
-1  // Show the graph again
```

弛豫后 C-B 键定域性明显增强。开壳层碎片例（CH₃ + NH₂ → CH₃NH₂，*examples\genpromol\CH3NH2*）：

```text
examples\genpromol\CH3NH2\CH3.wfn
100  // Other functions (Part 1)
19  // Generate promolecular .wfn file from fragment wavefunctions
1  // Output as combine.wfn
2  // There are totally two fragments (including the loaded one)
examples\genpromol\CH3NH2\NH2.wfn  // Wavefunction file of the second fragment
n  // Do not flip spin of orbitals of CH_3
y  // Flip spin of orbitals of NH_2. If you do not understand why the spin should be flipped, you can consult the corresponding CDA example in Section 4.16.2.
```

再与实际态 *examples\genpromol\CH3NH2\CH3NH2.wfn* 比较 ELF。

### 产出

组合波函数文件（叠加态，可直接做 ELF 等非线性分析）。

### 来源

[3.100.19](../sec-3-100-other-functions-part-1.md#310019-通过组合碎片波函数生成新波函数generate-new-wavefunction-by-combining-fragment-wavefunctions)、[4.100.19](../sec-4-100-other-functions-part-1.md#410019-对由片段波函数组合而成的整体波函数的elf分析)。

## 子功能20：计算 Hellmann-Feynman 力

### 说明

$$
\mathbf{F}_{A} = -\left\langle \Psi \left| \frac{\partial \hat{H}}{\partial \mathbf{R}_{A}} \right| \Psi \right\rangle = \mathbf{F}_{A}^{\mathrm{ele}} + \mathbf{F}_{A}^{\mathrm{nuc}} = -Z_{A} \int \frac{\rho(\mathbf{r})\left( \mathbf{R}_{A} - \mathbf{r} \right)}{\left| \mathbf{R}_{A} - \mathbf{r} \right|^{3}} \mathrm{d}\mathbf{r} + Z_{A} \sum_{B \neq A} \frac{Z_{B}\left( \mathbf{R}_{A} - \mathbf{R}_{B} \right)}{\left| \mathbf{R}_{A} - \mathbf{R}_{B} \right|^{3}}
```

打印总 H-F 力及电子/核贡献。注意一般 ≠ 量子化学程序解析力 $\mathbf{F}_{A}^{\mathrm{QC}} = -\partial E/\partial\mathbf{R}_{A}$（后者多 Pulay 项 $-2\langle\partial\Psi/\partial\mathbf{R}_{A}|\hat{H}|\Psi\rangle$，含轨道/组态系数与基函数对核坐标偏导）；仅全变分波函数（HF/DFT/MCSCF）+ 基函数与核坐标无关（如平面波）时二者才相等。

### 菜单路径

主功能100 → 子功能20。

### 输入要求

GTFs、原子坐标。

### 产出

各原子总 H-F 力及电子/核贡献。

### 来源

[3.100.20](../sec-3-100-other-functions-part-1.md#310020-计算hellmann-feynman力calculate-hellmann-feynman-forces)。

## 子功能21：基于几何信息计算特定原子的性质

### 说明

多种纯几何结构性质：

- 选原子范围（或 `all`）：(1) 质量；(2) 几何中心/质心/核电荷中心；(3) 回转半径 $R_{\mathrm{g}} = \sqrt{\sum_i m_i (\mathbf{r}_i - \mathbf{r}_c)^2/\sum_j m_j}$；(4) 核电荷和与核电荷偶极矩；(5) X/Y/Z 最值原子；(6) 最小/最大距离；(7) 惯量张量（对角 $I_{XX}=\sum m(y^2+z^2)$ 等，非对角 $-\sum mxy$ 等）、主轴（`***** Principal axes` 矩阵三列本征矢）与主转动惯量（本征值）；(8) 转动常数（amu⋅Å² 惯量，Z 轴如 $h/(8\pi^2 I_{ZZ}\xi)\times10^{11}$ GHz，$\xi$=1.66053878×10⁻²⁷）；(9) 核电荷间静电能。（.chg 输入时“核电荷”即原子电荷。）
- 输入 `size`：旋转使三主轴平行笛卡尔轴，按边界原子 + Bondi vdW 半径（*J. Phys. Chem.*, **68**, 441 (1964)）算半径/直径/长宽高；GUI 可视化包围盒；导出 *new.pdb*（含 CRYST1，VMD `pbc box` 显示）。例见 4.100.21.1。
- 输入 `dist`：定义两碎片，输出最小/最大距离、几何中心/质心间距。
- 输入 `ring`：按顺时针输环原子序号（如菲中间环 `3,4,8,9,10,7`），三角剖分算面积周长（环须凸，大复杂环如卟啉分块算再加和；多环芳香性可用 ΣNICS(1)_ZZ/area²，*J. Org. Chem.*, **72**, 9163 (2007)）。
- 输入 `MPP`（主菜单直接输 `MPP` 也可）：分子平面性 MPP（均方根偏离）与 SDP（跨度）：$MPP=\sqrt{\sum d_i^2/N_{\mathrm{atom}}}$，$d_i^{\mathrm{s}}=(Ax_i+By_i+Cz_i+D)/\sqrt{A^2+B^2+C^2}$，$SDP=d_{\max}^{\mathrm{s}}-d_{\min}^{\mathrm{s}}$（*J. Mol. Model.*, **27**, 263 (2021)）。输原子序号后输出拟合平面、MPP/SDP，可导出 .pqr（“电荷”列即 $d^{\mathrm{s}}$，VMD 按 Charge 着色）。多帧 .xyz 可选帧，MPP/SDP 存 *MPP_SDP.txt*。例见 4.100.21.2/3。
- 输入 `cav`（主菜单直接输也可）：空腔直径。选定周围原子 + 球心初位（常用几何中心），算与最近 vdW 球相切半径；最速上升迭代调球心使半径最大（收敛判据位移<0.01 Å，步限 0.3 Å），直径即空腔直径（Bondi 半径）。多空腔：恰当选原子+初位（迭代自动移向最近空腔）。例见 4.100.21.4。详见 <http://sobereva.com/643>。

### 菜单路径

主功能100 → 子功能21（`size`/`dist`/`ring`/`MPP`/`cav` 或原子范围）。

### 输入要求

原子坐标（轨迹分析用多帧 .xyz）。

### 操作步骤（实例 4.100.21.1：alpha-cyclodextrin 直径与长宽高，*examples/alpha-cyclodextrin.pdb*）

```text
examples/alpha-cyclodextrin.pdb
100  // Other functions (Part 1)
21  // Calculate quantities that are purely based on geometry
size  // Calculate molecular diameter and length/width/height
```

```text
Farthest distance:   44(H )  ---  123(H ):    14.027 Angstrom
vdW radius of   44(H ): 1.200 Angstrom
vdW radius of  123(H ): 1.200 Angstrom
Diameter of the system:    16.427 Angstrom
Radius of the system:     8.213 Angstrom
Length of the three sides:    15.341    14.714     9.511 Angstrom
```

直径=14.027+2×1.2。选项 1 图形化包围盒（Ratio of atomic size=4.0 时原子球半径恰为 vdW 半径）；选项 2 导出旋转平移后 *new.pdb*（VMD `pbc box`）。*examples\principal_axes.tcl* 复制到 VMD 控制台显示主轴（红/蓝/绿）。另见 <http://sobereva.com/426>。

实例 4.100.21.2（[14]annulene 平面性，ωB97XD/def2-TZVP，中文版 <http://sobereva.com/618>）：

```text
examples[14]annulene.xyz  // It contains the optimized structure
MPP  // Enter the function of studying molecular planarity
1-14  // We only use all carbon atoms to determine the planarity. You can also simply input h to choose all non-hydrogen atoms
```

```text
Plane equation: A=   1.00000  B=  -0.00000  C=   0.00233  D=   0.00000

Deviation of atom    1(C ) to the plane:  -0.21768 Angstrom
Deviation of atom    2(C ) to the plane:   0.21768 Angstrom
Deviation of atom    3(C ) to the plane:   0.21430 Angstrom
Deviation of atom    4(C ) to the plane:  -0.21430 Angstrom
Deviation of atom    5(C ) to the plane:  -0.07768 Angstrom
Deviation of atom    6(C ) to the plane:   0.07768 Angstrom
Deviation of atom    7(C ) to the plane:  -0.04457 Angstrom
Deviation of atom    8(C ) to the plane:   0.04457 Angstrom
Deviation of atom    9(C ) to the plane:  -0.02456 Angstrom
Deviation of atom   10(C ) to the plane:   0.02456 Angstrom
Deviation of atom   11(C ) to the plane:   0.09971 Angstrom
Deviation of atom   12(C ) to the plane:  -0.09971 Angstrom
Deviation of atom   13(C ) to the plane:  -0.03585 Angstrom
Deviation of atom   14(C ) to the plane:   0.03585 Angstrom
Maximal positive deviation to the fitted plane is    2(C ):   0.21768 Angstrom
Maximal negative deviation to the fitted plane is    1(C ):  -0.21768 Angstrom

Molecular planarity parameter (MPP) is    0.127145 Angstrom
Span of deviation from plane (SDP) is    0.435354 Angstrom
```

MPP/SDP 均不小 → 有限平面性。导出 .pqr 图形化：

```text
y  // Let Multiwfn to export .pqr file containing d^s values
[Press ENTER button directly]  // Output to [14]annulene.pqr in current folder
```

VMD 载入，Representation 用 Charge 着色 + CPK，Trajectory 色标范围 −0.4~0.4，背景白：红/蓝分居拟合面两侧，色深偏离大。

实例 4.100.21.3（C18 MD 轨迹平面性演化，*examples\C18_MD_500.xyz*，501 帧，首帧全平面；全轨迹下载 <http://sobereva.com/multiwfn/extrafiles/C18-MD.xyz>；背景 *Chem. Asian J.*, **16**, 56 (2021)）：

```text
examples\C18_MD_500.xyz
MPP  // Enter the function of studying molecular planarity
a  // Choose all atoms
a  // Choose all frames
```

得 *MPP_SDP.txt*（帧号/MPP/SDP，Origin 画演化曲线）与 *ds.pqr*（每帧 $d^{\mathrm{s}}$）。VMD 载入 xyz + 复制 *ds.pqr*、*examples\scripts\ds.tcl* 到 VMD 安装目录，控制台 `source ds.tcl`，播放动画原子按 $d^{\mathrm{s}}$ 自动着色（默认色标 −0.4 蓝 ~ 0.4 红；演示 <http://sobereva.com/multiwfn/res/ds_color.mp4>，配合 RMSD 插件去整体运动更易看）。

实例 4.100.21.4（开口富勒烯空腔，*examples\open_fullerene.pdb*，中文版 <http://sobereva.com/643>）：

```text
open_fullerene.pdb
cav  // Enter the function for calculating cavity diameter
1,12-20,23-67,101  // Atoms in the fullerene part, they will be used to detect sphere radius
1  // Use the geometric center of the atoms inputted above as initial position of sphere center
1  // Allow automatic adjustment of sphere center to maximize sphere size
```

```text
 X/Y/Z of initial geometry center are    3.901518    3.594304   11.835946 Angstrom
 Initial sphere radius is    1.677086 Angstrom
[...ignored]
Step    5
 Current coordinate:    3.939857    3.615266   11.899052 Angstrom
 Gradient:        0.009072    0.022419    0.013652  Norm    0.027772
 Displacement:    0.002400    0.005932    0.003612  Norm    0.007348 Angstrom
 Goal: displacement norm <  0.01000000 Angstrom

 Converged after     5 iterations

 Final X/Y/Z of sphere center:    3.942257    3.621198   11.902664 Angstrom
 Radius is    1.707257 Angstrom
 Diameter is    3.414514 Angstrom
 Volume is   20.844205 Angstrom^3
```

VMD 验证命令（载入 pdb，CPK，Sphere Scale 0.7，控制台执行）：

```tcl
color Display Background white
draw material Transparent
draw color yellow
draw sphere {    3.942    3.621   11.903 } radius   1.707 resolution 100
```

黄色球即空腔（直径 3.414 Å）。不规则空腔、环内径、晶体空腔见博客 <http://sobereva.com/643>。

### 产出

几何中心/质心/回转半径/惯量/转动常数；直径与长宽高（+包围盒图/*new.pdb*）；碎片间距；环面积周长；MPP/SDP（+* MPP_SDP.txt*/.pqr 着色图）；空腔直径/体积（+VMD 球命令）。

### 来源

[3.100.21](../sec-3-100-other-functions-part-1.md#310021-基于几何信息计算特定原子的性质calculate-properties-based-on-geometry-information-for-specific-atoms)、[4.100.21](../sec-4-100-other-functions-part-1.md#410021-几何结构表征示例)。

## 子功能22：检测 π 轨道、设置占据数并计算 π 组成

### 说明

研究 π 电子的关键（*如* ELF-π）。强烈建议读 [*Theor. Chem. Acc.*, **139**, 25 (2020)](https://link.springer.com/article/10.1007%2Fs00214-019-2541-z)（算法详述+例子；引用 Multiwfn 外另引此文）。

离域轨道（MO/NO/NTO 等，所有原子在 XY/YZ/XZ 平面）：选 `0`，程序自动找分子平面，列出 π 轨道序号/占据数/能量；选项 1 置零 π 占据，选项 2 置零其余，选项 3 只考虑价 π，选项 4 清除除价 π 外占据。不严格平面体系的局域平面区类 π（如甲苯六元环）：单点前使环严格平行 XY，算完用主功能 6 选项 -4 删甲基 GTF，进子功能 2（原文如此）选 0，手动选 XY 平面 + 两容差，得三类 π 轨道。

定域轨道（LMO/NBO 等，须 Pipek-Mezey 定域；Foster-Boys 成香蕉键不可用）：选 `-1`，再选 `0` 检测并设占据数。算法：算轨道组成找贡献最大/次大原子 A/B；A 贡献>阈值（默认 85%，选项 1 改）视为单中心跳过；否则算探测点 0.7**R**_A+0.3**R**_B 与 0.3**R**_A+0.7**R**_B 处轨道密度 |φ|²（理想 π 沿键节面应为零；非平面 σ-π 混需容差，阈值默认 0.01 a.u.，选项 2 改）。选项 3 限定轨道范围；选项 `5` 设原子范围约束（如 `2,4-7,9` 只识别贡献前二原子皆在其中的轨道，可锁定共轭环）。组成默认 Mulliken+SCPA（占据 Mulliken、空 SCPA；绝不能带弥散函数，否则无意义；选项 `6` 可换 Hirshfeld/Becke——与弥散兼容但贵、有时误识空 π，因不忠实反映节面；组成计算详见 [3.10](../sec-3-10-orbital-composition-analysis.md)）。

π 组成：选 `-1` 界面下再选 `-1`（先检测 π LMO，再输入几何基函数完全相同的另一波函数文件路径），轨道 $i$ 的 π 组成为 $\Theta_i = 100\% \times \sum_j^{\pi\mathrm{LMO}} c_{j,i}^2$，$c_{j,i} = \langle j|i\rangle = \sum_\mu\sum_\nu C_{\mu,i}C_{\nu,j}\langle\chi_\mu|\chi_\nu\rangle$；输入阈值，只打印高于者。非限制 α/β 分别基于各自 π LMO 算；分析后内存波函数为新载入文件。选项 `3` 切换考虑轨道：默认 `Occupied localized orbitals`（只用占据 π LMO，算占据 MO/双正交化/NTO 组成；须先有占据 LMO）；`All localized orbitals`（占据+空 π LMO，算空 MO/NTO/双正交化/自然轨道组成；须同时有占据和空 LMO）。

弥散函数重要说明：自动检测 π 最好去弥散；坚持用则 (1) 定域界面选 `-6` → `3 Pipek-Mezey based on Becke population`（兼容但慢）；(2) 探测界面选 `6` 用 Hirshfeld/Becke 算组成（Mulliken+SCPA 有弥散时失效）。

### 菜单路径

主功能100 → 子功能22（`0` 离域 / `-1` 定域；`-1` 下 `0` 设占据 / `-1` 算他文件轨道 π 组成）。

### 输入要求

GTFs（离域情形）；基函数（定域情形）；原子坐标。

### 操作步骤（实例 4.100.22：环庚三烯 π 特征，*examples\cycloheptatriene.fch*）

探测 π LMO（先定域占据轨道）：

```text
examples\cycloheptatriene.fch
19  // Orbital localization
1  // Localize occupied orbitals
100  // Other functions (Part 1)
22  // Detect π orbitals
-1  // Current orbitals are in localized form
0  // Detect π LMOs under default settings and then set their occupation numbers
```

```text
Expected pi orbitals, occupation numbers and orbital energies (eV):
    23      2.000000     -8.361389
    24      2.000000     -6.762986
    25      2.000000     -5.798201
 Total number of pi orbitals:     3
 Total number of electrons in pi orbitals:    6.000000
```

选 2 置零其余占据 → 密度矩阵自动更新，后续分析（主功能 5 密度等值面 0.03、LOL 等值面 0.5）纯 π 贡献：C4-C6、C1-C2、C3-C5 强于 C1-C4、C2-C3。误把孤对 LMO 认成 π 时：主功能 0 检查占据轨道记下孤对号，主功能 6 子功能 26 置零其占据再做 LOL-π。Mayer 键级（做法见 4.9.1）：

```text
#    1:         1(C )    2(C )    0.70534437
#    2:         1(C )    4(C )    0.18472895
#    3:         1(C )    5(C )    0.10215925
#    4:         2(C )    3(C )    0.18472484
#    5:         2(C )    6(C )    0.10215398
#    6:         3(C )    5(C )    0.80861164
#    7:         4(C )    6(C )    0.80860020
#    8:         5(C )    6(C )    0.07556895
```

π 键级 C4-C6 > C1-C2 > C1-C4，与 ELF-π 一致（helicene LOL-π 0.55、选项 `5` 限中央两环的五 π LMO 密度图、多中心键级 LMO 下照常，见原文图）。

占据 MO π 组成（定域时自动导出 *new.fch* 存占据 LMO）：

```text
new.fch  // Load it to retrieve occupied LMOs
100  // Other functions (Part 1)
22  // Detect π orbitals
-1  // Current orbitals are in localized form
-1  // Detect π orbitals and then evaluate π composition for orbitals in another file
examples\cycloheptatriene.fch  // This file contains MOs

[Press ENTER button directly to use printing threshold of 50%]
```

```text
 Orbital    23 (Occ= 2.00000)   pi composition:  65.003%
 Orbital    24 (Occ= 2.00000)   pi composition:  84.466%
 Orbital    25 (Occ= 2.00000)   pi composition:  92.863%
```

之后内存为 cycloheptatriene.fch 轨道，主功能 0 可画 π MO。MO23 π 组成偏低原因：C6-C7/C5-C7 成键区 σ 特征 + H10/H11/H14 周围等值面；MO25 准 π 轨道。

空 MO π 组成（还需空 LMO）：回主菜单：

```text
19  // Orbital localization
2  // Localize both occupied and unoccupied orbitals
100  // Other functions (Part 1)
22  // Detect π orbitals
-1  // Current orbitals are in localized form
3  // Switch the LMOs in consideration to "all localized orbitals"
2  // Change the default density threshold for identifying π orbitals. Because current geometry is highly distorted, more loose density threshold must be adopted, otherwise you will find no unoccupied π LMO could be recognized
0.05  // A value much larger (looser) than the default threshold
-1  // Detect π orbitals and then evaluate π composition for orbitals in another file
```

识别出 6 个 π LMO：

```text
Expected pi orbitals, occupation numbers and orbital energies (eV):
   23      2.000000     -8.361389
   24      2.000000     -6.762986
   25      2.000000     -5.798201
   26      0.000000     -0.739482
   27      0.000000      0.770830
  110      0.000000     74.313859
```

```text
examples\cycloheptatriene.fch  // The file containing MOs

[Press ENTER button directly to use printing threshold of 50%]
```

```text
 Orbital    23 (Occ= 2.00000)   pi composition:  65.003%
 Orbital    24 (Occ= 2.00000)   pi composition:  84.466%
 Orbital    25 (Occ= 2.00000)   pi composition:  92.863%
 Orbital    26 (Occ= 0.00000)   pi composition:  84.033%
 Orbital    27 (Occ= 0.00000)   pi composition:  72.481%
 Orbital    29 (Occ= 0.00000)   pi composition:  57.811%
```

主功能 0 画 MO27（π 组成 72.5%）确以 π 为主。更多讨论见 <http://sobereva.com/432>。离域例另见 [4.5.3](../sec-4-5-generate-grid-data-and-view-isosurface-map.md#453-计算-elf-σ-和-elf-π-以研究苯的芳香性)（ELF-σ/π）、[4.4.9](../sec-4-4-output-and-plot-various-properties-in-a-plane.md#449-绘制卟啉的-lol-π-图以揭示有利的电子离域路径)（卟啉 LOL-π）。

### 产出

π 轨道序号/占据数/能量、占据数修改、他文件轨道 π 组成百分比。

### 来源

[3.100.22](../sec-3-100-other-functions-part-1.md#310022-检测π轨道设置占据数并计算π组成detect-π-orbitals-set-occupation-numbers-and-calculate-π-composition)、[4.100.22](../sec-4-100-other-functions-part-1.md#410022-分析非平面体系-non-planar-system的π电子-π-electron特征环庚三烯-cycloheptatriene)。

## 子功能23：拟合函数分布到原子值

### 说明

类似 ESP 电荷拟合（见 [3.9.10](../sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3910-chelpg-charges-from-electrostatic-potentials-using-a-grid-based-method-esp-拟合原子电荷-12)、[3.9.11](../sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3911-merz-kollmann-mk-esp-拟合原子电荷-13)），但被拟合实空间函数不限于 ESP（如表面平均局域电离能、Fukui 函数）。选项 1 选函数后在拟合点算值，最小二乘拟合到原子值：

$$
F(p_1, p_2 \cdots p_N) = \sum_i \left[ V(\mathbf{r}_i) - V'(\mathbf{r}_i) \right]^2
$$

$$
V'(\mathbf{r}_i) = \sum_A \frac{p_A}{r_{A,i}}
$$

误差：

$$
\begin{gathered} \mathrm{RMSE} = \sqrt{\frac{\sum_i \left[ V(\mathbf{r}_i) - V'(\mathbf{r}_i) \right]^2}{N}} \quad\quad \mathrm{RRMSE} = \sqrt{\frac{\sum_i \left[ V(\mathbf{r}_i) - V'(\mathbf{r}_i) \right]^2}{\sum_i V(\mathbf{r}_i)^2}} \end{gathered}
$$

默认拟合中心全在核上（选项 -2 从外部文件加额外中心，格式见 3.9.10）；默认拟合点同 Merz-Kollman（见 3.9.11），选项 3 层数、选项 2 面点密度、选项 4 每层 vdW 缩放（如两层 1.0/1.2）；选项 5 对总值 $\sum p_i$ 加约束（约束=净电荷 + ESP 函数 = MK 电荷）。选项 -1 从外部纯文本直接定义拟合点（格式见 3.9.10；首行点数写负值且文件含函数值时直接载入不再计算）。基于 ESP cube 算拟合电荷例见 <http://sobereva.com/wfnbbs/viewtopic.php?pid=1542> #4。

### 菜单路径

主功能100 → 子功能23。

### 输入要求

原子坐标（被拟合函数如 ESP/ALIE/Fukui 由 GTFs 算得）。

### 产出

原子拟合值 + RMSE/RRMSE。

### 来源

[3.100.23](../sec-3-100-other-functions-part-1.md#310023-拟合函数分布到原子值fit-function-distribution-to-atomic-value)。
