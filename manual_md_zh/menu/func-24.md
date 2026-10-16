# 主功能24：（超）极化率分析

本主功能是研究极化率（polarizability）与超极化率（hyperpolarizability）的一系列子功能的集合，涵盖解析 Gaussian `polar` 任务输出、态求和（SOS）方法计算、两/三能级模型分析、（超）极化率密度以及单位球与矢量表示可视化。计算（超）极化率时基组必须带足量弥散函数，否则结果不可靠。原子极化率另可通过模糊空间分析模块计算，见 `sec-3-18` 第 3.18.12 节。

理论与实例来源：[3.27](../sec-3-27-hyperpolarizability-analysis.md)、[4.24](../sec-4-24-examples-of-hyperpolarizability-analyses.md)。更多讨论见博文 <http://sobereva.com/231>（解析输出）、<http://sobereva.com/232>（SOS）、<http://sobereva.com/305>（极化率密度）、<http://sobereva.com/547>（单位球表示）、<http://sobereva.com/512>（二/三能级模型）、<http://sobereva.com/683>（极化率密度实例）。

## 子功能1：解析 Gaussian 的（超）极化率任务输出并计算相关量

### 说明

Gaussian 的（超）极化率任务（`polar` 关键词）输出难以理解，本功能用于解析这些输出，并以更易读的格式打印，同时输出一些与（超）极化率相关的量。目前正式兼容 Gaussian 09 与 16。

体系能量可写成对均匀外电场 **F** 的 Taylor 展开：

$$
\begin{gathered} E(\mathbf{F}) = E(\mathbf{0}) + \left.\frac{\partial E}{\partial \mathbf{F}}\right|_{\mathbf{F} = 0} \mathbf{F} + \frac{1}{2}\left.\frac{\partial^2 E}{\partial \mathbf{F}^2}\right|_{\mathbf{F} = 0} \mathbf{F}^2 + \frac{1}{6}\left.\frac{\partial^3 E}{\partial \mathbf{F}^3}\right|_{\mathbf{F} = 0} \mathbf{F}^3 + \frac{1}{24}\left.\frac{\partial^4 E}{\partial \mathbf{F}^4}\right|_{\mathbf{F} = 0} \mathbf{F}^4 + \dots \\ \equiv E(\mathbf{0}) - \boldsymbol{\mu}_0 \mathbf{F} - \frac{1}{2}\boldsymbol{\alpha}\mathbf{F}^2 - \frac{1}{6}\boldsymbol{\beta}\mathbf{F}^3 - \frac{1}{24}\boldsymbol{\gamma}\mathbf{F}^4 - \frac{1}{120}\boldsymbol{\delta}\mathbf{F}^5 - \frac{1}{720}\boldsymbol{\epsilon}\mathbf{F}^6 \dots \end{gathered}
$$

$$
\boldsymbol{\mu}_0 = -\left.\frac{\partial E}{\partial \mathbf{F}}\right|_{\mathbf{F} = 0} \quad\quad \boldsymbol{\alpha} = -\left.\frac{\partial^2 E}{\partial \mathbf{F}^2}\right|_{\mathbf{F} = 0} \quad\quad \boldsymbol{\beta} = -\left.\frac{\partial^3 E}{\partial \mathbf{F}^3}\right|_{\mathbf{F} = 0} \quad\quad \boldsymbol{\gamma} = -\left.\frac{\partial^4 E}{\partial \mathbf{F}^4}\right|_{\mathbf{F} = 0}
$$

其中 **µ**₀ 为永久偶极矩（矢量）；**α** 为极化率（二阶张量）；**β** 为第一超极化率（三阶张量，即二阶非线性光学响应系数）；**γ** 为第二超极化率（四阶张量，即三阶 NLO 系数）。**F** 为零频率时称为静态（超）极化率，非零频率时为动态（超）极化率。

各向同性平均极化率：

$$
\langle \alpha \rangle = \mathrm{Tr}(\boldsymbol{\alpha})/3 = (\alpha_{xx} + \alpha_{yy} + \alpha_{zz})/3
$$

极化率各向异性定义 2（最常用，见 *J. Chem. Phys.*, **98**, 3022 (1993)）：

$$
\Delta\alpha = \sqrt{[(\alpha_{xx} - \alpha_{yy})^2 + (\alpha_{xx} - \alpha_{zz})^2 + (\alpha_{yy} - \alpha_{zz})^2]/2}
$$

**β** 沿笛卡尔轴的值与大小：

$$
\beta_i = (1/3)\sum_j (\beta_{iij} + \beta_{jii} + \beta_{jij}) \quad\quad i, j = \{x, y, z\}
$$

$$
\beta_{\mathrm{tot}} = \sqrt{\beta_x^2 + \beta_y^2 + \beta_z^2}
$$

$$
\beta_{\mathrm{prj}} = \sum_i \frac{\mu_i\beta_i}{|\boldsymbol{\mu}|} \quad\quad \beta_{\parallel} = (3/5)\beta_{\mathrm{prj}}
$$

静态情形：$\beta_x = \beta_{xxx} + \beta_{xyy} + \beta_{xzz}$，$\beta_y = \beta_{yxx} + \beta_{yyy} + \beta_{yzz}$，$\beta_z = \beta_{zxx} + \beta_{zyy} + \beta_{zzz}$。

**γ** 的 $i$ 分量与平均值（定义 1 更常用，等价于 γ$_{||}$）：

$$
\gamma_i = (1/15)\sum_j (\gamma_{ijji} + \gamma_{ijij} + \gamma_{iijj}) \quad\quad i, j = \{x, y, z\}
$$

$$
\begin{aligned}\mathrm{def\ 1:} \quad \langle \gamma \rangle &= \gamma_x + \gamma_y + \gamma_z\\\mathrm{def\ 2:} \quad \langle \gamma \rangle &= (1/5)(\gamma_{xxxx} + \gamma_{yyyy} + \gamma_{zzzz} + \gamma_{xxyy} + \gamma_{xxzz} + \gamma_{yyzz} + \gamma_{yyxx} + \gamma_{zzxx} + \gamma_{zzyy})\end{aligned}
$$

超 Rayleigh 散射（HRS）与退偏比（DR）：

$$
\beta_{\mathrm{HRS}}(-2\omega; \omega, \omega) = \sqrt{\left\langle \beta_{ZZZ}^2 \right\rangle + \left\langle \beta_{XZZ}^2 \right\rangle}
$$

$$
\mathrm{DR} = \frac{\left\langle \beta_{ZZZ}^2 \right\rangle}{\left\langle \beta_{XZZ}^2 \right\rangle}
$$

$$
\begin{aligned}\left| \beta_{J = 1} \right| &= \sqrt{6\left\langle \beta_{ZZZ}^2 \right\rangle - 9\left\langle \beta_{XZZ}^2 \right\rangle}\\\left| \beta_{J = 3} \right| &= \sqrt{\frac{1}{2}\left( -7\left\langle \beta_{ZZZ}^2 \right\rangle + 63\left\langle \beta_{XZZ}^2 \right\rangle \right)}\end{aligned}
$$

（⟨β²⟩ 的完整取向平均展开式很长，见原文档第 3.27.1 节，此处从略。）

### 菜单路径

主功能24（超极化率）→ 子功能1（解析 Gaussian 的 polar 任务输出）。

### 输入要求

Gaussian `polar` 任务输出文件，输入文件中必须指定 **#P**，否则 Multiwfn 无法正确解析。频率相关计算需在分子几何之后空一行给出外电场频率（例如 `0.05 0.07 0.1` 或 `532 nm 680 nm`），并用 `CPHF=RdFreq`（只算 **β**(-ω;ω,0)）或 `polar=DCSHG`（同时算 **β**(-ω;ω,0) 与 **β**(-2ω;ω,ω)）。

### 操作步骤

进入本功能后，按 Gaussian 计算的实际情况选择以下选项之一（所有选项都打印极化率；只有选项 1、3、5 还打印第一超极化率，只有 7 还打印第二超极化率）：

- (1) `polar` 关键词 + 支持解析三阶导数的方法（HF/DFT/半经验方法）
- (2) `polar` 关键词 + 支持解析二阶导数的方法（例如 MP2）
- (3) `polar=Cubic` 关键词 + 支持解析二阶导数的方法
- (4) `polar` 关键词 + 支持解析一阶导数的方法（CISD、QCISD、CCSD、MP3、MP4(SDQ) 等）
- (5) `polar=DoubleNumer`（等价于 `Polar=EnOnly`）关键词 + 支持解析一阶导数的方法
- (6) `polar` 关键词 + 仅支持能量计算的方法（CCSD(T)、QCISD(T)、MP4(SDTQ)、MP5 等）
- (7) `polar=gamma` 关键词 + 支持解析三阶导数的方法（HF/DFT/半经验方法）

辅助选项：选项 `-1` 切换“解析频率相关结果”（对选项 1 与 7，选后可再选解析哪个频率；解析 **β**(-2ω;ω,ω) 必须用 `polar=DCSHG`）；选项 `-3` 选择输出单位（原子单位、SI、esu）；选项 `-4` 在解析后导出张量 txt 文件（供子功能 5 用）。

单位换算：*α* (1 a.u.) = *α*' (0.14818470 Å³)（极化率体积）。

|     |        | SI                    | esu                |
|-----|--------|-----------------------|--------------------|
| *µ* | 1 a.u. | 8.47835×10⁻³⁰ C m     | 2.54175 ×10⁻¹⁸ esu |
| *α* | 1 a.u. | 1.6488×10⁻⁴¹ C²m²J⁻¹  | 1.4819×10⁻²⁵ esu   |
| *β* | 1 a.u. | 3.20636×10⁻⁵³ C³m³J⁻² | 8.63922×10⁻³³ esu  |
| *γ* | 1 a.u. | 6.23538×10⁻⁶⁵ C⁴m⁴J⁻³ | 5.03670×10⁻⁴⁰ esu  |

众所周知 Gaussian 输出的所有超极化率分量符号都是错的，应乘以 -1，Multiwfn 已自动处理。

### 实例：解析 NH₃ 的静态（超）极化率（4.24.1）

`examples\polar` 文件夹中 *NH3_polar_static.out*（PBE0/aug-cc-pVTZ，弥散函数不可少）。启动 Multiwfn 并输入：

```text
examples\polar\NH3_polar_static.out
24  // (Hyper)polarizability analysis
1  // Parse (hyper)polarizability task of Gaussian
1  // Start parsing. We select option 1 because third-order derivative of current level (normal DFT functional) is supported by Gaussian
```

屏幕输出：

```text
Dipole moment:
 X,Y,Z=    0.000000    0.000000   -0.596558   Norm=    0.596558

 Static polarizability:
 XX=       13.692700
 XY=        0.000000
 YY=       13.693300
 XZ=        0.000000
 YZ=       -0.000334
 ZZ=       15.323600
 Isotropic average polarizability:       14.236533
 Isotropic average polarizability volume:       2.109636 Angstrom^3
 Polarizability anisotropy (definition 1):        1.630600
 Polarizability anisotropy (definition 2):        1.630600
 Eigenvalues of polarizability tensor:     13.69270     13.69330     15.32360
 Polarizability anisotropy (definition 3):        1.630600

 Note: It is well known that the sign of hyperpolarizability of Gaussian 09/16 s
hould be inverted, the outputs shown below have already been corrected

 Static first hyperpolarizability:
 XXX=        0.000000
 XXY=       12.903200
 XYY=        0.000000
 YYY=      -12.900200
 XXZ=        9.617100
 XYZ=        0.000000
 YYZ=        9.564710
 XZZ=        0.000000
 YZZ=        0.016285
 ZZZ=       26.613200

 Beta_X=        0.00000  Beta_Y=        0.01929  Beta_Z=       45.79501
 Magnitude of first hyperpolarizability:       45.795014
 Projection of beta on dipole moment:      -45.795010
 Beta ||     :      -27.477006
 Beta ||(z)  :       27.477006
 Beta _|_(z) :        9.159002
```

### 实例：解析频率相关（超）极化率与 HRS（4.24.1）

```text
examples\polar\NH3_polar_dynamic.out
24  // (Hyper)polarizability analysis
1  // Parse (hyper)polarizability task of Gaussian
-1  // Let Multiwfn load frequency-dependent (hyper)polarizability
1  // Start parsing
```

Multiwfn 检测到三套数据：

```text
       1   w=    0.000000 (     Static    )
       2   w=    0.065600 (      695.04nm )
       3   w=    0.071900 (      634.14nm )
```

输入 `2` 加载 0.0656 a.u. 数据。之后选择超极化率类型：

```text
1: Beta(-w;w,0)   2: Beta(-2w;w,w)
Note: Option 2 is meaningless if "DCSHG" keyword was not used
```

选 2（输入文件用了 `polar=DCSHG`）解析 β(-2w;w,w)，同时打印 HRS 相关量：

```text
<beta_ZZZ^2>:  8.12843560E+02
<beta_XZZ^2>:  1.45318790E+02
Hyper-Rayleigh scattering (beta_HRS):        30.954
Depolarization ratio (DR):   5.594
|<beta J=1>|:        59.743
|<beta J=3>|:        41.624
Nonlinear anisotropy parameter (rho):   0.697
Dipolar contribution to beta, phi_beta(J=1):     0.589
Octupolar contribution to beta, phi_beta(J=3):   0.411
< (beta_ZXZ+beta_ZZX)^2 - 2*betaZZZ*betaZXX >:  2.04387968E+02
```

之后输入 `y` 再输入初始角度（如 -180），生成 *HRS_angle.txt*（偏振角 -180°~179°、步长 1° 的散射强度），可用 Origin 画极坐标图（示例 *examples\polar\HRS_angle.opj*）。

### 实例：解析第二超极化率 γ（4.24.1）

示例输入 *examples\polar\NH3_gamma.gjf*（`polar=gamma`，末尾指定 532 nm 和 680 nm 两个频率）。解析 532 nm 处 γ(-2w;w,w,0)：

```text
examples\polar\NH3_gamma.out
24  // (Hyper)polarizability analysis
1  // Parse (hyper)polarizability task of Gaussian
-1  // Let Multiwfn load frequency-dependent (hyper)polarizability
7  // This option is specific for parsing polarizability and second hyperpolarizability
3  // 532 nm
```

再选 2 解析 gamma(-2w;w,w,0)，输出：

```text
 XXXX=    3.966470E+03
 YXXX=    0.000000E+00
 ZXXX=    8.493370E-05
 XYXX=XXYX=    0.000000E+00
[...ignored]
 ZZZZ=    3.204030E+04

 Magnitude of gamma:      1.067181E+04
 X component of gamma:    2.134993E+03
 Y component of gamma:    2.134897E+03
 Z component of gamma:    1.023580E+04
 Average of gamma (definition 1), gamma ||:    1.450569E+04
 Average of gamma (definition 2):    1.461464E+04
 gamma _|_:    4.653651E+03
```

注意 γ 分量对应输入取向（α 与 β 对应标准取向）。想解析 gamma(0;0,0,0)，解析前不要选 -1。

### 产出

屏幕打印偶极矩、α/β/γ 各分量与各向同性平均、各向异性、βₓ/βᵧ/βz、βtot、βprj、β∥、HRS、DR、J=1/3 分量等；SHG 型 β 可扫描 I(ΨV) 输出 *HRS_angle.txt*；选项 -4 导出 *alpha.txt*/*beta.txt*/*gamma.txt*。

### 来源

[3.27.1](../sec-3-27-hyperpolarizability-analysis.md#3271-解析-gaussian-的超极化率任务输出并计算相关量)、[4.24.1](../sec-4-24-examples-of-hyperpolarizability-analyses.md#4241-解析-gaussian-polar-任务的输出文件得到-超极化率并计算相关量)。

## 子功能2：用态求和（SOS）方法计算（超）极化率

### 说明

SOS 方法基于 Orr 与 Ward 思想（显式方程见 *J. Chem. Phys.*, **99**, 3738 (1993)），原则上对所有激发态求和（实际 60–120 个低能态通常已够）。它比解析导数法慢，当导数法可用时一般不推荐；优点是可分别给出不同态的贡献，且手头已有跃迁偶极矩时可快速算不同频率处的值。

α 与 β 的 SOS 方程（原子单位）：

$$
\begin{gathered}\alpha_{AB}(-\omega;\omega)=\sum_{i\ne 0}\left[\frac{\mu_{0i}^{A}\mu_{i0}^{B}}{\Delta_{i}-\omega}+\frac{\mu_{0i}^{B}\mu_{i0}^{A}}{\Delta_{i}+\omega}\right]=\hat{P}[A(-\omega),B(\omega)]\sum_{i\ne 0}\frac{\mu_{0i}^{A}\mu_{i0}^{B}}{\Delta_{i}-\omega}\end{gathered}
$$

$$
\begin{gathered}\beta_{ABC}(-\omega_{\sigma};\omega_{1},\omega_{2})=\hat{P}[A(-\omega_{\sigma}),B(\omega_{1}),C(\omega_{2})]\sum_{i\ne 0}\sum_{j\ne 0}\frac{\mu_{0i}^{A}\overline{\mu_{ij}^{B}}\mu_{j0}^{C}}{(\Delta_{i}-\omega_{\sigma})(\Delta_{j}-\omega_{2})}\end{gathered}
$$

γ、δ 的 SOS 方程见原文档第 3.27.2.1 节。

### 菜单路径

主功能24 → 子功能2（SOS 方法）。

### 输入要求

两种输入文件：(1) 含所有相关态激发能与跃迁偶极矩的纯文本文件（可算 α、β、γ、δ；格式如下，可由 3.21.5 功能基于 Gaussian 或其他程序激发任务输出生成；只算极化率时只需 `1 1` 行之前内容且态数写成负数）；(2) CIS/TDHF/TDDFT/ZINDO 的 Gaussian 输出文件（只算极化率，态数要足够大，建议 `#P`）。

```text
2      // The number of excited states
1  1.1        // Excited state 1, its index and excitation energy (eV)
2  3.2
0 0  0.845 0.2 0.4    // Electric dipole moment of ground in X,Y,Z (a.u.)
0 1  0.231 0.3 0.7    // Transition dipole moment between ground and excited state 1
0 2  0.112 0.564 0.21
1 1  0.021 0.465 0.0    // Electric dipole moment of excited state 1
1 2  0.001 0.3 0.11     // Transition dipole moment between excited states 1 and 2
2 2  0.432 0.14 0.42
```

SOS 模块中单位均为原子单位。

### 操作步骤

- 选项 1~4：分别计算给定频率处 α、β、γ、δ。输入每个外电场频率（可为负，如算 β(-(0.25-0.32);0.25,-0.32) 输入 `0.25,-0.32`；默认原子单位，加后缀 `nm` 可以 nm 输入，如 `182.25,-142.385 nm`）。算 γ/δ 时会提示输入考虑的态数目。
- 选项 5~7：研究 α、β、γ 随态数目的变化（α/β 从 1 到全部态步长 1；γ 可自定义终值步长），结果输出到当前目录纯文本文件。
- 选项 15~17：研究 α、β、γ 随频率的变化。α 输入初值/终值/步长；β/γ 写纯文本文件、每行一对（组）频率，例如研究 γ(-0;0,ω,-ω)、ω 从 0 到 0.2 a.u. 步长 0.02：

```text
0.0  0.0  0.0
0.0  0.02  -0.02
0.0  0.04  -0.04
...[ignored]
0.0  0.2  -0.2
```

- 选项 19：同时扫描 β(-(ω₁+ω₂);ω₁,ω₂) 的 ω₁ 与 ω₂，输入各自起止与步数，结果输出纯文本文件，可画 relief 图（单光子共振/和频/差频/光整流特征分析见 *ACS Appl. Nano Mater.*, **2**, 1648 (2019)）。

### 实例：SOS 计算 NH₃ 的 α、β、γ（4.24.2.1）

先用 Gaussian 跑 *examples\NH3_SOS.gjf*（CIS，150 态，def2-TZVPPD，`IOp(9/40=5)` 很重要；TDHF/TDDFT 也可），formchk 得 *NH3_SOS.fch*。生成 *SOS.txt*：

```text
C:\NH3_SOS.fch
18  // Electron excitation analysis module
5  // Calculate transition dipole moments and dipole moment for all excited states
C:\NH3_SOS.out
3  // Generate SOS.txt
```

重启 Multiwfn 并输入：

```text
SOS.txt
24  // (Hyper)polarizability analysis
2  // Study (hyper)polarizability by sum-over-states (SOS) method
```

静态极化率：选 1，输入 `0`，得各向同性平均 14.59（实验 14.56，*Mol. Phys.*, **33**, 1155）：

```text
             1              2              3
 1      14.610682       0.000000       0.000000
 2       0.000000      14.610682       0.000000
 3       0.000000       0.000000      14.552483
Isotropic average polarizability:      14.591283
Isotropic average polarizability volume:       2.162205 Angstrom^3
Polarizability anisotropy (definition 1):       0.058199
Eigenvalues:      14.552483      14.610682      14.610682
Polarizability anisotropy (definition 2):       0.029100
```

动态极化率 α(-ω;ω)：再选 1，输入 `0.0719`，动态平均约 14.86。

静态第一超极化率：选 2，输入 `0,0`，β∥(0;0,0) = -38.98（接近 CCSD(T) 高精度值 -34.3）。动态 β(-2ω;ω,ω)：再选 2，输入 `0.0656, 0.0656`，β∥ = -49.69（实验 -48.9±1.2）。

第二超极化率：选 3，输入 `0,0,0`，再输入态数 `150`，γ 平均值 928.74（γ 准确计算通常需 d-aug-cc-pVTZ 级基组）。

收敛性检验：选 6，输入 `0,0`，得 *beta_n.txt*/*beta_n_comp.txt*（n=100 处基本收敛，70 态定性正确）。选项 5/7 类似检验 α/γ。

频率扫描：写频率对文件（每行一对 ω₁,ω₂，本例 ω₂=0）：

```text
0.00  0
0.01  0
0.02  0
...
0.5   0
```

选 16，输入文件路径，得 *beta_w.txt*/*beta_w_comp.txt*。双频扫描：

```text
19
-0.6,0.6,100  // Lower limit, upper limit and number of steps of ω_1 (in a.u.)
-0.6,0.6,100  // Lower limit, upper limit and number of steps of ω_2 (in a.u.)
```

### 产出

各阶（超）极化率张量及各向异性、大小、轴向分量；收敛/频率扫描纯文本文件供 Origin 等作图。

### 来源

[3.27.2.1](../sec-3-27-hyperpolarizability-analysis.md#32721-超极化率的计算)、[4.24.2.1](../sec-4-24-examples-of-hyperpolarizability-analyses.md#42421-计算-nh₃-的极化率和超极化率)。

## 子功能2选项20：两能级与三能级模型分析

### 说明

β 的 SOS 表达式可分解为单个激发态贡献与交叉项之和：

$$
\beta_{ZZZ}^{\mathrm{SOS}}=\sum_{i}6\frac{(\mu_{0i}^{Z})^{2}\Delta\mu_{i}^{Z}}{\Delta_{i}^{2}}+\sum_{i}\sum_{j>i}12\frac{\mu_{0i}^{Z}\mu_{0j}^{Z}\mu_{ij}^{Z}}{\Delta_{i}\Delta_{j}}
$$

**两能级模型**（基态 + 一个关键态，通常为跃迁偶极矩 Z 分量大的最低激发态）：

$$
\beta_{ZZZ}^{\mathrm{SOS}}\approx 6\frac{(\mu_{0i}^{Z})^{2}\Delta\mu_{i}^{Z}}{\Delta_{i}^{2}}
$$

等价振子强度形式：$\beta_{ZZZ}^{\mathrm{SOS}}=9\Delta\mu_{i}^{Z}f_{i}^{Z}/\Delta_{i}^{3}$，其中 $f_{i}^{Z}=(2/3)\Delta_{i}(\mu_{0i}^{Z})^{2}$。比较 Δμ、f、Δ 三项即可分析不同体系 β 差异来源。

**三能级模型**（两个近简并关键态 i、j 都不可忽略时）：

$$
\beta_{ZZZ}^{\mathrm{SOS}}=6\frac{(\mu_{0i}^{Z})^{2}\Delta\mu_{i}^{Z}}{\Delta_{i}^{2}}+12\frac{\mu_{0i}^{Z}\mu_{0j}^{Z}\mu_{ij}^{Z}}{\Delta_{i}\Delta_{j}}+6\frac{(\mu_{0j}^{Z})^{2}\Delta\mu_{j}^{Z}}{\Delta_{j}^{2}}
$$

适用条件：(1) 只有一个 β 分量主导；(2) 一个（两能级）或两个（三能级）激发态贡献远大于其余。给体-π-受体体系通常满足。

### 菜单路径

主功能24 → 子功能2 → 子选项 20。

### 输入要求

与 SOS 计算第一超极化率完全相同的输入文件（*SOS.txt*）。

### 操作步骤

进入选项 20 后：只输入一个激发态序号 → 两能级分析；输入两个序号 → 三能级分析；输入范围（如 `1-20`）→ 范围内每个态逐个做两能级分析。

### 实例：NH₂-biphenyl-NO₂ 的 β 分析（4.24.2.2）

*examples\excit\D-pi-A.fchk* + *D-pi-A.out*（CAM-B3LYP/6-31G(d)，5 个单重态；给体-π-受体沿 X 轴，故只看 βXXX）。准备输入：

```text
examples\excit\D-pi-A.fchk
18  // Electron excitation analysis module
5  // Calculate transition dipole moments and dipole moment for all excited states
examples\excit\D-pi-A.out
3  // Generate SOS.txt, which contains all information needed by the two- or three-level analysis
```

重启 Multiwfn：

```text
SOS.txt
24  // (Hyper)polarizability analysis
2 // Study (hyper)polarizability by sum-over-states (SOS) method
20  // Two- or three-level model analysis of β
```

Multiwfn 打印各态关键信息：

```text
Excitation energy (E), transition electric dipole moment between ground state and excited state, and variation of dipole moment of excited states w.r.t. ground state
                  Trans. dipole moment (a.u.)        Var. dipole moment (a.u.)
 State   E(eV)     X       Y       Z      Tot        X       Y       Z      Tot
    1   3.9069   0.444  -0.000  -0.002   0.444    -1.010  -0.001   0.001   1.010
    2   4.0624   2.528  -0.003  -0.007   2.528     6.563  -0.015  -0.047   6.501
    3   4.4166  -0.003  -0.002  -0.023   0.024    -1.081   0.002   0.002   1.077
    4   4.7912   0.001   0.341  -0.013   0.341     1.845  -0.006  -0.015   1.823
    5   4.8872  -0.004   0.192  -0.171   0.257     0.993  -0.019  -0.049   0.925
```

态 2 跃迁偶极矩与偶极矩变化远大于他态 → 关键态。输入 `1-5` 逐个两能级分析：

```text
beta evaluated by two-level model: (a.u.)
 #    1: XXX=       -58.05  YYY=        -0.00  ZZZ=         0.00  Norm=        58.05
 #    2: XXX=     11289.12  YYY=        -0.00  ZZZ=        -0.00  Norm=     11289.12
 #    3: XXX=        -0.00  YYY=         0.00  ZZZ=         0.00  Norm=         0.00
 #    4: XXX=         0.00  YYY=        -0.15  ZZZ=        -0.00  Norm=         0.15
 #    5: XXX=         0.00  YYY=        -0.13  ZZZ=        -0.27  Norm=         0.30
```

看态 2 细节：

```text
20  // Two or three-level model analysis of β
2  // Select excited state 2 for two-level model analysis
```

```text
 Excited state     2
 Excitation energy    0.149290 a.u.    4.0624 eV
 Transition dipole moment (a.u.)
 X=    2.527776  Y=   -0.003088  Z=   -0.007328  Total=    2.527789
 Oscillator strength
 X=    0.635943  Y=    0.000001  Z=    0.000005  Total=    0.635949
 Variation of dipole moment (a.u.)
 X=    6.562899  Y=   -0.015345  Z=   -0.046710  Total=    6.563083

 beta evaluated by two-level model: (a.u.)
 XXX=    11289.1185  YYY=       -0.0000  ZZZ=       -0.0007  Norm=    11289.1185
```

三能级分析：

```text
20  // Perform two- or three-level model analysis of β again
1,2  // Choose excited states 1 and 2 for the three-level model analysis
```

```text
 Transition dipole moment between states     1 to     2: (a.u.)
 X=    1.475397  Y=   -0.001634  Z=   -0.008677  Total=    1.475423
 Individual contribution of excited state     1 to beta: (a.u.)
 XXX=      -58.0482  YYY=       -0.0000  ZZZ=        0.0000  Norm=       58.0482
 Individual contribution of excited state     2 to beta: (a.u.)
 XXX=    11289.1185  YYY=       -0.0000  ZZZ=       -0.0007  Norm=    11289.1185
 Coupling contribution of the two excited states to beta: (a.u.)
 XXX=      927.8987  YYY=       -0.0000  ZZZ=       -0.0001  Norm=      927.8987

 beta evaluated by three-level model: (a.u.)
 XXX=    12158.9690  YYY=       -0.0000  ZZZ=       -0.0007  Norm=    12158.9690
```

态 1 单独贡献与耦合项均可忽略 → 两能级模型已足够。

提示：激发任务输出含大量态时，可设 *settings.ini* 中 `maxloadexc`（如 5）只加载前几个态以加速 *SOS.txt* 生成。

### 产出

关键态的跃迁偶极矩、偶极矩差、振子强度、激发能及各项对 β 的分解，便于跨体系比较。

### 来源

[3.27.2.2](../sec-3-27-hyperpolarizability-analysis.md#32722-超极化率的两能级与三能级模型分析)、[4.24.2.2](../sec-4-24-examples-of-hyperpolarizability-analyses.md#42422-对-nh₂-biphenyl-no₂-的第一超极化率做二能级和三能级模型分析)。

## 子功能3：（超）极化率密度分析

### 说明

电子密度对电场的 Taylor 展开：

$$
\begin{gathered}\rho(\mathbf{r},\mathbf{F})=\rho^{(0)}(\mathbf{r})+\rho^{(1)}(\mathbf{r})\mathbf{F}+(1/2)\rho^{(2)}(\mathbf{r})\mathbf{F}^2+(1/6)\rho^{(3)}(\mathbf{r})\mathbf{F}^3+\dots\\\rho^{(1)}(\mathbf{r})=\left.\frac{\partial \rho(\mathbf{r})}{\partial \mathbf{F}}\right|_{\mathbf{F}=0}\quad\quad\rho^{(2)}(\mathbf{r})=\left.\frac{\partial^2 \rho(\mathbf{r})}{\partial \mathbf{F}^2}\right|_{\mathbf{F}=0}\quad\quad\rho^{(3)}(\mathbf{r})=\left.\frac{\partial^3 \rho(\mathbf{r})}{\partial \mathbf{F}^3}\right|_{\mathbf{F}=0}\end{gathered}
$$

$$
\begin{gathered}\boldsymbol{\mu}_0=\int-\rho^{(0)}(\mathbf{r})\mathbf{r}\,\mathrm{d}\mathbf{r}\quad\quad\boldsymbol{\alpha}=\int-\rho^{(1)}(\mathbf{r})\mathbf{r}\,\mathrm{d}\mathbf{r}\\\boldsymbol{\beta}=\int-\rho^{(2)}(\mathbf{r})\mathbf{r}\,\mathrm{d}\mathbf{r}\quad\quad\boldsymbol{\gamma}=\int-\rho^{(3)}(\mathbf{r})\mathbf{r}\,\mathrm{d}\mathbf{r}\end{gathered}
$$

**ρ**⁽¹⁾ 为极化率密度，**ρ**⁽²⁾、**ρ**⁽³⁾ 为第一、第二超极化率密度。有限差分求法（步长经验取 0.003 a.u.）：

$$
\rho_{zzz}^{(3)}=\frac{\rho(2F^z)-2\rho(F^z)+2\rho(-F^z)-\rho(-2F^z)}{2(F^z)^3}
$$

$$
\begin{gathered}\rho_z^{(1)}=\frac{\rho(F^z)-\rho(-F^z)}{2F^z}\\\boldsymbol{\gamma}_{zz}=\int-\rho_z^{(1)}(\mathbf{r})z\,\mathrm{d}\mathbf{r}\end{gathered}
$$

$$
\begin{gathered}\rho_{zz}^{(2)}=\frac{\rho(F^z)-2\rho(0)+\rho(-F^z)}{(F^z)^2}\\\boldsymbol{\beta}_{zzz}=\int-\rho_{zz}^{(2)}(\mathbf{r})z\,\mathrm{d}\mathbf{r}\end{gathered}
$$

$-z\rho_{zzz}^{(3)}(\mathbf{r})$ 为点 **r** 对 γZZZZ 的贡献（依赖原点选取），而 ρ 本身与原点无关，二者都有研究价值。用此功能建议引用 *J. Comput. Chem.*, **38**, 1574 (2017)。

### 菜单路径

主功能24 → 子功能3。

### 输入要求

含原子信息的文件（.xyz/.pdb/.mwfn/.fch 等）＋ 不同外电场下的 .wfx 文件（由本功能选项 1 生成 Gaussian 输入、手动运行得到）。

### 操作步骤

- (1) 启动 Multiwfn 并加载原子信息文件。
- (2) 进入主功能 24 的子功能 3。
- (3) 选择希望研究的量（极化率密度 / 第一 / 第二超极化率密度及其空间贡献）。
- (4) 选择方向（X/Y/Z）。
- (5) 选选项 1 生成不同外电场下单点计算的 Gaussian 输入文件（默认 PBE0/aug-cc-pVTZ，可手动改关键词；有限场 0.003 a.u.；`nosymm` 防重取向）。
- (6) 手动用 Gaussian 运行 .gjf，生成 .wfx 文件。
- (7) 选选项 2 加载 .wfx 文件。
- (8) 计算格点数据（可视化等值面 / 导出 .cub / 绘平面图）。空间贡献格点导出 .cub 后可进一步做原子/片段贡献分析。

分子取向提示：真正感兴趣的往往是沿偶极矩方向的分量，应先重取向使偶极矩平行于某笛卡尔轴（如 Z）。加载波函数后输入：

```text
300  //Other function (Part 3)
7  //Geometry operation on the present system
7  //Make electric dipole moment parallel to a vector or Cartesian axis
3  //Parallel to Z axis
-1  //Output system to .xyz file
```

导出的 .xyz 即为本功能输入文件。

### 实例：H₂CO 的第二超极化率密度（4.24.3）

C=O 沿 Z 轴，研究 ρzzz⁽³⁾ 与 -zρzzz⁽³⁾。先用 Gaussian 常规 γ 任务（*examples\polar\polardens\gamma.gjf*，PBE0/aug-cc-pVTZ）得 γZZZZ = 3092.1 a.u. 作参照。准备工作：

```text
examples\polar\polardens\H2CO.xyz  //Multiwfn will load the geometry from this file, which contains the same coordinate as gamma.gjf
24  //(Hyper)polarizability analysis
3  //(Hyper)polarizability density analysis
3  //Study second hyperpolarizability density and spatial contribution to second hyperpolarizability
3  //Z direction
1  //Generate Gaussian input files of single point task under different external electric fields
[Press ENTER button directly]  //Use 0 and 1 as net charge and spin multiplicity, respectively
```

生成 *Z-2.gjf*、*Z-1.gjf*、*Z+1.gjf*、*Z+2.gjf*（Z+2 对应 +0.006 a.u.）。用 Gaussian 运行得四个 .wfx，然后：

```text
2  //Load .wfx files of single point task under different external electric fields
[Press ENTER button directly]  //Assume that the .wfx files are in current folder
```

可视化 ρzzz⁽³⁾ 等值面：

```text
1  //Generate grid data of second hyperpolarizability density
2  //Medium-quality grid
1  //Visualize isosurface map
```

等值面 0.5。再看空间贡献：关 GUI 后输入：

```text
0  //Return
2  //Generate grid data of spatial contribution to second hyperpolarizability
2  //Medium-quality grid
```

格点积分 3008.2 a.u. ≈ 3092.1 a.u.（更高质量格点 + 更大延伸距离会更接近）。选 2 可视化，等值面 2：绿色（蓝色）区对 γZZZZ 正（负）贡献；价层区基本为负、分子两端显著为正且占优，故 γZZZZ 为明显正值。

绘制 YZ 平面图：

```text
3  //Plot plane map of second hyperpolarizability density
1  //Color-filled map
[Press ENTER button directly]  //Use the default 200*200 grid points
3  //YZ plane
0  //X=0
3  //YZ plane
0  //X=0
```

微调（蓝-白-红色过渡、删小等值线、显原子标签/键、色标 -6~6）：

```text
19  //Set color transition
8  //Blue-White-Red
2  //Enable showing contour lines
3  //Change contour line setting
4  //Delete some contour lines (we only want to keep contour lines with relatively large value in this example)
32-37
4  //Delete some contour lines
1-6
1  //Save setting and return
4  //Enable showing atom labels and reference point
12  //Dark green
8  //Enable showing bonds
14  //Brown
1  //Set lower & upper limits
-6,6
-1  //Replot
```

选 `-5` 回主菜单后，用选项 4 类似绘制 -zρzzz⁽³⁾ 平面图。

原子贡献：选项 2 生成空间贡献格点后选 `2` 导出 *grid.cub*（直接回车用默认名）。设 *settings.ini* 中 `iuserfunc` = -1，重启载入 *grid.cub*：

```text
15  //Fuzzy atomic space analysis
1  //Integrate a real space function in every atomic space
100  //User-defined function
```

```text
  Atomic space        Value                % of sum            % of sum abs
    1(C )           28.87467715             0.962679             0.962679
    2(H )          950.91673574            31.703459            31.703459
    3(H )          949.91946330            31.670210            31.670210
    4(O )         1069.69915961            35.663652            35.663652
Summing up above values:       2999.41003579
Summing up absolute value of above values:       2999.41003579
```

两 H 与 O 为主要贡献；总和 2999.4 a.u. ≈ 3092.1 a.u.。

### 产出

（超）极化率密度与空间贡献的平面图/等值面/.cub；原子或片段贡献定量分解。

### 来源

[3.27.3](../sec-3-27-hyperpolarizability-analysis.md#3273-研究超极化率密度)、[4.24.3](../sec-4-24-examples-of-hyperpolarizability-analyses.md#4243-研究-超极化率密度的例子)。

## 子功能5：通过单位球与矢量表示可视化（超）极化率

### 说明

有效偶极矢量（*θ*、*φ* 为球极坐标，**e** 为球面外法向单位矢量）：

$$
\boldsymbol{\beta}^{\mathrm{eff}}(\theta,\phi)=\boldsymbol{\beta}\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)
$$

$$
\beta_i^{\mathrm{eff}}=\sum_j\sum_k\beta_{i,j,k}e_ke_j\quad\quad i,j,k=\{x,y,z\}
$$

$$
\begin{gathered}\boldsymbol{\alpha}^{\mathrm{eff}}(\theta,\phi)=\boldsymbol{\alpha}\cdot\mathbf{e}(\theta,\phi)\\\boldsymbol{\gamma}^{\mathrm{eff}}(\theta,\phi)=\boldsymbol{\gamma}\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\cdot\mathbf{e}(\theta,\phi)\end{gathered}
$$

球面每顶点绘制 **β**ᵉᶠᶠ 即得单位球表示：箭头取向/长度反映沿该方向施加两束电场组合引起的诱导偶极矩方向/大小。

矢量表示：**β** 画 (*β*ₓ,*β*ᵧ,*β*z) 箭头，其中 $\beta_i=(1/3)\sum_j(\beta_{ijj}+\beta_{jji}+\beta_{jij})$；**α** 沿 X/Y/Z 画双向箭头，长度 $\alpha_x = \alpha_{xx} + \alpha_{xy} + \alpha_{xz}$ 等；**γ** 类似，$\gamma_i=(1/15)\sum_j(\gamma_{ijji}+\gamma_{ijij}+\gamma_{iijj})$。矢量表示简洁但丢失各向异性特征。

张量分量 Fortran 顺序：极化率 ((**α**(i,j),j=1,3),i=1,3)；一阶 (((**β**(i,j,k),k=1,3),j=1,3),i=1,3)；二阶 ((((**γ**(i,j,k,l),l=1,3),k=1,3),j=1,3),i=1,3)，指标 $i$ 循环最慢。例如 **α** 文件：

```text
 3.62370000E+001   XX
-2.20999000E+000   XY
 0.00000000E+000   XZ
-2.20999000E+000   YX
 3.91836000E+001   YY
 0.00000000E+000   YZ
 0.00000000E+000   ZX
 0.00000000E+000   ZY
 2.54054000E+001   ZZ
```

### 菜单路径

主功能24 → 子功能5。选项 `-8` 可切换“最长箭头定长”（便于比较大小不同的体系）；选项 1/2/3 分别做 α/β/γ。

### 输入要求

含原子信息的文件（定球半径，如 .xyz/.pdb/.fch）＋ 张量文件 *alpha.txt*/*beta.txt*/*gamma.txt*（由子功能 1 选项 `-4` 导出，或手动按 Fortran 顺序准备）。

### 操作步骤

启动后载入原子信息文件 → 进子功能 5 → 调箭头参数（自明）→ 选 1/2/3 自动加载对应 txt（须在当前目录）→ 得 *alpha/beta/gamma.tcl*（单位球）与 *alpha/beta/gamma_vec.tcl*（矢量）→ VMD 中 `source` 运行。

### 实例：CH₃NHCHO 的 SHG 型 β（4.24.5.1）

*examples\polar\CH3NHCHO\polar.gjf*（`#P HF/6-311++g(d,p) polar=DCSHG CPHF=rdfreq`，末尾 `450nm 1030nm`，必须 #P）。解析并导出：

```text
examples\polar\CH3NHCHO\polar.out
24  // (Hyper)polarizability analysis
1  // Parse "polar" task of Gaussian. PS: If you are not familiar with this function, please check Section 3.27.1 for introduction and 4.24.1 for example
-1  // Request Multiwfn to parse dynamic (hyper)polarizability
-4  // Request Multiwfn to export parsed (hyper)polarizability as .txt file
1  // Start parsing (hyper)polarizability
2  // As shown on screen, the second option corresponds to 1030 nm case
2  // Load SHG form of β
n  // Do not perform analysis related to hyper-Rayleigh scattering
```

得 *alpha.txt*、*beta.txt*。设 *settings.ini* 中 `iloadGaugeom` = 2（从 Gaussian 输出以标准取向加载坐标），重启：

```text
examples\polar\CH3NHCHO\polar.out
24 // (Hyper)polarizability analysis
5  // Visualize (hyper)polarizability via unit sphere and vector representations
```

选 2 → 得 *beta.tcl*、*beta_vec.tcl*。导出结构供 VMD 显示：

```text
0  // Exit current function
0  // Return to main menu
100  // Other function (Part 1)
2  // Generate new file
1  // Export current geometry as .pdb file
CH3NHCHO.pdb
```

VMD 中依次 `source beta.tcl`、`source beta_vec.tcl`，载入 pdb 并设 CPK 显示即得单位球图（与 *J. Comput. Chem.*, **32**, 1128 (2011) 图 2(e) 一致）。球上小箭头为缩放 **β**ᵉᶠᶠ（按长度着色：最短蓝、最长红、居中白）；大绿箭头为矢量表示 (*β*ₓ,*β*ᵧ,*β*z)，方向与球上箭头矢量和基本一致。

### 实例：环[18]碳的 α 与 γ（4.24.5.2）

*examples\polar\C18\gamma.gif*…（`gamma.gjf`，LPol-ds 基组，静态，末尾频率 0.0；几何 ωB97XD/def2-TZVP）。提取：

```text
examples\polar\C18\gamma.out  // Output file of aforementioned input file
24  // (Hyper)polarizability analysis
1  // Parse "polar" task of Gaussian
-4  // Request Multiwfn to export parsed (hyper)polarizability as .txt file
7  // Start parsing α and γ
```

得 *alpha.txt*、*gamma.txt*，然后：

```text
0  // Exit current function
5  // Visualize (hyper)polarizability via unit sphere and vector representations
-3  // Change scale factor of length of the arrows on sphere surface
0.005  // This value is smaller than default, since α of cyclo[18]carbon is fairly large. If default value is used, you will find the arrows are too long
-5  // Change length scale factor for the arrow of vector representation
0.01
1  // Perform unit sphere representation analysis of α. Since alpha.txt already exists in current folder, α tensor is automatically loaded from it
```

VMD 运行 *alpha.tcl*、*alpha_vec.tcl*（结构 .pdb 同上一例导出）：环面内 α 大（392 a.u.）、垂直环方向小（98 a.u.）。γ 类似：

```text
-3  // Change scale factor of length of the arrows on sphere
1E-5  // This value is significantly smaller than default one, since magnitude of γ is quite large
-5  // Change length scale factor for the arrow of vector representation
0.00005
1  // Perform unit sphere representation analysis of γ. Since gamma.txt already exists in current folder, γ tensor is automatically loaded from it
```

注意子功能 1 解析的 **γ** 对应输入取向（α、β 对应标准取向），载入 VMD 的结构必须对应输入取向：设 `iloadGaugeom` = 1，重启后输入：

```text
examples\polar\C18\gamma.out  // Geometry in input orientation will be loaded from this file
100  // Other function (Part 1)
2  // Generate new file
1  // Export current geometry as .pdb file
C18.pdb
```

### 产出

*alpha/beta/gamma.tcl*（单位球 VMD 脚本）与 *alpha/beta/gamma_vec.tcl*（矢量表示脚本）。

### 来源

[3.27.5](../sec-3-27-hyperpolarizability-analysis.md#3275-通过单位球与矢量表示可视化超极化率)、[4.24.5](../sec-4-24-examples-of-hyperpolarizability-analyses.md#4245-用单位球表示直观研究-超极化率的例子)。
