# 主功能25：电子离域与芳香性分析

本主功能汇集若干芳香性分析方法：等化学屏蔽表面（ICSS）三维格点生成、非平面/倾斜体系 NICS_ZZ 求值、HOMA/Bird/HOMAc/HOMER 几何指数、NICS-1D 扫描曲线与 INICS/FiPC-NICS 积分、一维/二维 NICS 平面图。Multiwfn 自身不能算磁屏蔽张量，凡涉及 NICS/ICSS 都需 Gaussian 做 NMR 任务。本功能只要求原子坐标的那些子功能（HOMA/Bird 等）用任意含坐标文件即可。

Multiwfn 中大多数电子离域与芳香性分析在其它章节，概述见 [4.A.3](../sec-4-A-special-topics-and-advanced-tutorials.md#4a3-芳香性研究方法概述)。理论与实例来源：[3.28](../sec-3-28-electron-delocalization-and-aromaticity-analyses.md)、[4.25](../sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md)。相关博文：<http://sobereva.com/216>（ICSS）、<http://sobereva.com/261>（倾斜/扭曲环 NICS_ZZ）、<http://sobereva.com/681>（一维 NICS）、<http://sobereva.com/682>（二维 NICS）、<http://sobereva.com/724>（FiPC-NICS）。

## 子功能3：生成等化学屏蔽表面（ICSS）及相关量

### 说明

等化学屏蔽表面（ICSS）即 NICS 负值的等值面，展示 NICS 三维分布，给出直观芳香性图像。本功能生成各向同性 ICSS、各向异性 ICSS、ICSS_XX、ICSS_YY、ICSS_ZZ 格点，分别对应 NICS、NICS_ani、NICS_XX、NICS_YY、NICS_ZZ 负值的等值面。NICS_ani 定义为 *ε*₃ − (*ε*₁ + *ε*₂)/2（*ε* 为磁屏蔽张量本征值从小到大排序）。ICSS 原始论文 *J. Chem. Soc. Perkin Trans.* 2, **2001**, 1893；ICSS_ani/XX/YY/ZZ 由开发者提出，用到请引用 *Carbon*, **165**, 468 (2020)。对平面体系分量形式（尤其 ICSS_ZZ）比总 ICSS 更有意义，正如 NICS_ZZ 优于 NICS。

### 菜单路径

主功能25 → 子功能3。

### 输入要求

Gaussian 输入模板 .gjf（几何已优化，必须显式指定 %chk；其中的关键词将用于 NMR 任务，如 *examples\ICSS\anthracene.gjf*）＋ 运行所得 NMR 输出文件。

### 操作步骤

- (1) 为所研究体系准备 Gaussian 输入文件，必须显式指定 %chk，几何结构应已优化好。
- (2) 启动 Multiwfn 后载入 .gjf 文件，然后进入主功能 25 的子功能 3。
- (3) 按提示设置格点。注意，即使中等质量格点也可能相当耗时，对中等大小体系一般推荐低质量格点。
- (4) 输入 `n`，即不跳过第 5 步。
- (5) 在当前文件夹生成许多 Gaussian NMR 输入文件（*NICS0001.gjf*、*NICS0002.gjf*……），建议手动检查一个确保格式关键词正确。每个 Bq 对应一个格点；默认每个文件 8000 原子（真实+Bq），可调 *settings.ini* 中 `NICSnptlim`。Bq 太多 Gaussian 会因内存过大失败且有原子总数上限；内存大可调大 `NICSnptlim` 以降低总代价。G09 D.01/E.01 须在模板 route 加 `guess=huckel`（Link401 报错改 `guess=core`），否则 NICSnptlim 须很小（如 1000）；G16 不需要 guess。
- (6) 运行所有输入文件得输出（*NICS0001.gjf* 必须先运行；可用 *examples\runall.sh* / *runall.bat* 批量跑，生成同名 .out）。最好保持 Multiwfn 运行（若退出，用完全相同设置重复 2、3 步，第 4 步输入 `y`）。
- (7) 输入输出文件所在文件夹路径，Multiwfn 从 *NICS0001.out*、*NICS0002.out*……载入磁屏蔽张量。
- (8) 选择感兴趣的性质。
- (9) 可视化等值面或导出 cube（如第 8 步选 ZZ 则对应 ICSS_ZZ；选 `-1 Load another ICSS form` 可研究其它形式）。

若已有该体系 NMR 输出：从第 2 步开始，第 4 步输入 `y` 跳过 5、6 步，但第 3 步格点必须与当初完全一致。

### 实例：苯的 ICSS_ZZ 与磁屏蔽分布（4.25.3）

苯平面在 XY 面。模板 *examples\ICSS\benzene.gjf*（几何已优化）。启动 Multiwfn：

```text
examples\ICSS\benzene.gjf  // Note that molecular plane is in XY plane
25  // Electron delocalization and aromaticity analyses
3  // Generate grid data of ICSS or related quantities
1  // Low-quality grid, magnetic shielding tensor at 130910 points will be calculated by Gaussian later. Using "medium-quality grid" could result in smoother maps, but the calculation will be much more expensive. Note that the default extension distance is 12 Bohr, which is usually large enough
n  // Do not skip the step of generating Gaussian input file, because this is the first time we carry out analysis and thus currently we do not have Gaussian input/output files in hand
```

生成 *NICS0001.gjf*~*NICS0017.gjf*，用 Gaussian 运行（*NICS0001.gjf* 先跑；输出可下载 <http://sobereva.com/multiwfn/extrafiles/benzene_ICSS.rar>）。常见失败原因：(1) %mem 太小；(2) `NICSnptlim` 太大。

假设输出在 `C:\benzene`，输入 `C:\benzene\NICS`，选 `5: ZZ component`，得 ICSS_ZZ 格点。选项 1 可视化（ICSS_ZZ = 2.0 ppm：绿色等值面覆盖环上下区域 → 强芳香性；蓝色在外侧 → 退屏蔽；C-H 键也被绿面覆盖 → σ 局域环电流）；选项 2 导出 *ICSSZZ.cub*；选项 -1 换其它形式。

已有输出时直接研究：

```text
examples\ICSS\benzene.gjf
25  // Electron delocalization and aromaticity analyses
3  // Generate grid data of ICSS or related quantities
1  // Low-quality grid
y  // Skip generating Gaussian input files and thus directly load Gaussian output files
C:\benzene\NICS
5  // Study ICSS_ZZ
```

格点设置必须与生成时完全一致，否则加载失败。

绘制 YZ 平面（X=0，穿过 C4-H10 和 C1-H7）填色图：设 *settings.ini* 中 `iuserfunc` = -3（B 样条插值 cube 格点），新开 Multiwfn：

```text
ICSSZZ.cub
4  // Plot plane map
100  //User-defined function, which now corresponds to the function interpolated by the grid data of ICSSZZ.cub via B-spline algorithm
1  // Color-filled map
[Press Enter button]
0  // Set extension distance of the plot
8  // 8 Bohr
3  // YZ plane
0  // X=0
```

关图后微调：

```text
4  // Show atom labels
3  // Blue
1  // Change lower and upper limit of color scale
-60,60
2  // Enable showing contour lines
-2  // Set label interval in X, Y and color scale axes
3,3,10
19  // Set color transition
8  // Blue-White-Red
-1  // Replot the map
```

环中心屏蔽 Z 分量为正但远小于环上下（只有 π 芳香性、无 σ 全局离域）。

磁屏蔽曲线（垂直环穿过环中心、±8 Bohr）：选 -5 回主菜单后输入：

```text
3  // Plot curve map
100  // User-defined function
2  // Input coordinate of two points to define a line
0,0,-8,0,0,8  // The line starts from 8 Bohr below and above the ring center
```

选 `6` 找极值：

```text
Maximum X (Bohr):    6.122667  Value:    0.28936394E+02
Minimum X (Bohr):    8.000000  Value:    0.13254245E+02
Maximum X (Bohr):    9.882667  Value:    0.28937419E+02
```

ICSS_ZZ 最大 28.9 ppm 在环上下 1.88 Bohr（0.995 Å）；环中心仅 13.2 ppm。注意格点延伸仅 12 Bohr，插值作图范围不宜太大，超出点值为 0。

由 ICSS_ZZ 直接得 NICS(0)_ZZ/NICS(1)_ZZ（NICS = −ICSS）：确保 `iuserfunc` = -3，启动：

```text
ICSSZZ.cub
1  // Calculate function values at a point
0,0,1  // The point 1 Å above the ring center
2  // The inputted position is in Å
```

自定义函数值 28.9 → NICS(1)_ZZ = −28.9 ppm。

练习体系在 *examples\ICSS*（azulene、cyclobutadiene、cycloheptatriene、porphyrin、propane、pyracylene），详见博文 <http://sobereva.com/216>。

### 产出

ICSS 各形式格点（等值面可视化 / 导出 .cub）；基于插值可进一步画平面图、曲线图、求 NICS(0/1)_ZZ。

### 来源

[3.28.3](../sec-3-28-electron-delocalization-and-aromaticity-analyses.md#3283-生成等化学屏蔽表面-icss-及相关量)、[4.25.3](../sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md#4253-研究苯的等化学屏蔽面-icss-和磁屏蔽分布)。

## 子功能4：求非平面或倾斜体系的 NICS_ZZ 值

### 说明

NICS(0)_ZZ 或 NICS(1)_ZZ 比原始 NICS 更好（*Org. Lett.*, **8**, 863 (2006)）。平面体系 NICS(0)_ZZ 即环中心磁屏蔽 ZZ 分量（平面平行 XY 时）；NICS(1)_ZZ 为环中心上/下方平面外 1 Å 处的值。环中心可用几何中心、质心，推荐 AIM 环临界点（RCP）（*WIREs Comput. Mol. Sci.*, **3**, 105 (2013)）。

扭曲/倾斜环无法直接从程序输出得法向分量，本功能按 *σ*⊥=**u**ᵀ**σu**（**u** 为环法向单位列向量）计算，并给出 NICS(1) 所需的 1 Å 上下方点坐标。

### 菜单路径

主功能25 → 子功能4。

### 输入要求

含原子坐标的文件（.xyz/.pdb/.mol/.wfn/.mwfn/.fch/.molden 等）＋ 环中心（可由主功能 2 的 RCP 或主功能 100 子功能 21 的几何中心/质心得到）＋ 量子化学程序算得的磁屏蔽张量。

### 操作步骤（NICS(1)_ZZ）

- (1) 用 Multiwfn 打开含坐标的文件。
- (2) 确定环中心（拓扑模块主功能 2 定 RCP，或主功能 100 子功能 21 得几何中心/质心）。
- (3) 进主功能 25 子功能 4，输入环中心，再输入拟合环平面的原子序号（通常为该环全部原子）。输出环平面上下 1 Å 两点坐标（还输出法向量，可推 NICS(2)、NICS(3.5)…位置；若只要几何中心且用环全部原子拟合，第 2 步可跳过——被问环中心时直接回车即自动用拟合原子的几何中心）。
- (4) 用上步两点之一，以量子化学程序计算该处磁屏蔽张量。
- (5) 按程序输出输入磁屏蔽张量全部分量。输出的 `The shielding value normal to the plane` 的负值即 NICS(1)_ZZ（体系相对平面不对称时 NICS(1)_ZZ ≠ NICS(−1)_ZZ，可取平均）。

NICS(0)_ZZ 更简单：(1)(2) 同上；(3) 直接用环中心算磁屏蔽张量；(4) 进子功能 4 输入环中心 + 拟合原子 + 张量分量，法向屏蔽值负值即 NICS(0)_ZZ。

### 产出

环平面法向量、1 Å 上下方点坐标、法向屏蔽值（负值即 NICS_ZZ）。

### 来源

[3.28.4](../sec-3-28-electron-delocalization-and-aromaticity-analyses.md#3284-求非平面或倾斜体系的-nics_zz-值)。另见博客“使用 Multiwfn 计算倾斜和扭曲环的 NICS_ZZ”<http://sobereva.com/261>。

## 子功能6：计算 HOMA 和 Bird 芳香性指数

### 说明

HOMA（*Tetrahedron Lett.*, **13**, 3839 (1972)；推广形式 *J. Chem. Inf. Comput. Sci.*, **33**, 70 (1993)，注意众多论文误引公式）：

$$
\mathrm{HOMA}=1-\sum_i\frac{\alpha_{i,j}}{N}(R_{\mathrm{ref}}-R_{i,j})^2
$$

$$
\begin{gathered}R_{\mathrm{ref}}=(R_{\mathrm{s}}+wR_{\mathrm{d}})/(1+w)\\\alpha=\frac{2}{(R_{\mathrm{s}}-R_{\mathrm{ref}})^2+(R_{\mathrm{d}}-R_{\mathrm{ref}})^2}\end{gathered}
$$

$N$ 为环原子总数，$j$ 为原子 $i$ 的下一原子；$R_s$、$R_d$ 为单/双键实验键长，$w=k_d/k_s$（通常 2.0，BN 键 4.2）。HOMA=1 完全芳香，0 完全非芳香，显著负值反芳香。内置参数：CC、CN、CO、CP、CS、NN、NO（*Chem. Inf. Comput. Sci.*, **33**, 70 (1993)）；BN（*Tetrahedron*, **54**, 14913 (1998)）；BC（*Struct. Chem.*, **23**, 595 (2012)），可经选项 1 修改/补充。

Bird 指数（*Tetrahedron*, **41**, 1409 (1985)）：

$$
\begin{gathered}I=100[1-(V/V_{\mathrm{K}})]\end{gathered}
$$

$$
V=\frac{100}{\overline{N}}\sqrt{\frac{\sum_i(N_{i,j}-\overline{N})^2}{n}}\quad\quad N_{i,j}=\frac{a}{R_{i,j}}-b
$$

$i$ 遍历环键，$n$ 为键总数，$N$ 为 Gordy 键级，$V_K$ 五/六元环分别为 35/33.2。越接近 100 芳香性越强。$a$、$b$ 参数：C-C、C-N、C-O、C-S、N-O、N-N（*Tetrahedron*, **57**, 5715 (2001)），B-N（*Tetrahedron*, **54**, 14913 (1998)），其它键经选项 3 提供，$V_K$ 经选项 4 调整/增加。

### 菜单路径

主功能25 → 子功能6。选项 0 算 HOMA（选项 1 改参数），选项 2 算 Bird（选项 3/4 提供键参数/调 VK）。

### 输入要求

仅原子坐标（任意含坐标文件）。

### 操作步骤

进入子功能 6，选 0（HOMA）或 2（Bird），按连接顺序输入环原子序号（如 `2,3,4,5,6,7`），即得指数与每对原子贡献。MP2/6-311+G** 噻吩示例输出：

```text
        Atom pair         Contribution  Bond length(Angstrom)
   1(C )  --    2(C ):      -0.001852        1.382006
   2(C )  --    3(C ):      -0.056708        1.421170
   3(C )  --    4(C ):      -0.001852        1.382006
   4(C )  --    5(S ):      -0.023886        1.712627
   5(S )  --    1(C ):      -0.023886        1.712627
HOMA value is    0.891817
```

0.891817 接近 1 → 突出芳香性。

### 实例：菲的 HOMA 和 Bird（4.25.6）

几何 B3LYP/6-31G* 优化。启动：

```text
examples/phenanthrene.pdb
25  // Electron delocalization and aromaticity analyses
6  // Calculate HOMA and Bird aromaticity index
0  // Start the calculation
```

先看默认参数（*J. Chem. Inf. Comput. Sci.*, **33**, 70 (1993)），可选项 1 修改。输入中间环 `3,4,8,9,10,7`（须按连接顺序）：

```text
        Atom pair         Contribution  Bond length(Angstrom)
   3(C )  --    4(C ):      -0.065698        1.427111
   4(C )  --    8(C ):      -0.210455        1.458000
   8(C )  --    9(C ):      -0.065698        1.427111
   9(C )  --   10(C ):      -0.096016        1.435282
  10(C )  --    7(C ):      -0.033673        1.360000
   7(C )  --    3(C ):      -0.096016        1.435282
HOMA value is    0.432442
```

C4-C8 偏离理想键长 1.388 最显著。边缘环 `8,15,14,13,11,9` 得 0.855126 → 边缘环芳香性更强。选项 2 算 Bird 同样边缘环更接近 100。

### 产出

HOMA 值（越近 1 越芳香）与每键贡献；Bird 指数（越近 100 越芳香）。

### 来源

[3.28.6](../sec-3-28-electron-delocalization-and-aromaticity-analyses.md#3286-计算-homa-和-bird-芳香性指数)、[4.25.6](../sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md#4256-计算菲的-homa-和-bird-芳香性指标)。

## 子功能6a/6b：HOMAc 和 HOMER

### 说明

HOMER（*Phys. Chem. Chem. Phys.*, **25**, 16763 (2023)）针对 T₁ 态重新参数化 $R_{\mathrm{ref}}$ 和 *α*（仅 CC、CN、CO、NN 键），与 T₁ 的 NICS(1)_zz 合理相关（HOMA 几乎无相关）；无法表征 Franck-Condon 点 T₁（几何与 S₀ 相同）。HOMAc（*J. Org. Chem.*, **90**, 1297 (2025)）改善 S₀ 基态判断，推荐代替 HOMA。参数由 CASPT2/cc-pVQZ 优化几何导出，但对 DFT 几何也适用。

### 菜单路径

主功能25 → 子功能 6a（HOMAc）/ 6b（HOMER），用法与 HOMA 完全相同。

### 输入要求

仅原子坐标。

### 产出

HOMAc/HOMER 指数（判读同 HOMA）。

### 来源

[3.28.7](../sec-3-28-electron-delocalization-and-aromaticity-analyses.md#3287-homac-和-homer)。

## 子功能13：NICS-1D 扫描曲线图、积分 NICS（INICS）与 FiPC-NICS

### 说明

沿垂直于环的线扫描 NICS 比单点含信息得多。对 NICS 曲线积分（INICS，*J. Phys. Chem. A*, **123**, 3922 (2019)）比单点更可靠。FiPC-NICS（*Inorg. Chem.*, **53**, 3579 (2014)）：任一点 NICS = 面内 NICS_in=(NICS_XX+NICS_YY)/3 + 面外 NICS_out=NICS_ZZ/3；扫描线上 NICS_in=0 处的 NICS_out 即 FiPC-NICS（不受面内污染，比 NICS(1)_ZZ 更严格；常用 NICS(1)_ZZ 是其可接受近似）。

### 菜单路径

主功能25 → 子功能13。

### 输入要求

含结构信息的文件 ＋ Gaussian NMR 模板文件（坐标处替换为 `[geometry]`，如 *examples\NICS_scan\template_NMR.gjf*）。

### 操作步骤

- (1) 启动 Multiwfn 并载入结构文件。
- (2) 进主功能 25 子功能 13。
- (3) 定义扫描线 + 线上均匀扫描点数。两种定线方式：① 手动指定两端点坐标；② 输入原子序号拟合平面，再指定相对几何中心在平面上下方距离。
- (4) 选选项 1，输入 Gaussian 模板路径（标准 NMR 任务，坐标为 `[geometry]`），当前文件夹生成 *NICS_1D.gjf*（可按需改关键词）。
- (5) 手动用 Gaussian 运行。
- (6) 选选项 2，输入输出路径载入。
- (7) 选感兴趣分量（默认磁屏蔽张量投影到扫描线方向分量的负值；可选各向同性/各向异性/XX/YY/ZZ/特定矢量方向）。
- (8) 新界面绘 NICS 曲线（可存图/导出 .txt），或算 INICS、FiPC-NICS（FiPC-NICS 要求扫描线平行于笛卡尔轴）。恰当设置模板（如 `nmr=csgt iop(10/93=2)` 指定 MO）可画特定轨道贡献曲线（如 NICS_σ,zz、NICS_π,zz）。

### 实例 1：infinitene 的 NICS_ZZ 曲线（4.25.13.1）

*examples\NICS_scan\infinitene.pdb*（PBE0/6-31G* 优化），扫描高亮环：垂直拟合平面、从几何中心指向外侧：

```text
examples\NICS_scan\infinitene.pdb  //You can also use any other file format containing structure information, similarly hereinafter
25  //Electron delocalization and aromaticity analyses
13  //NICS-1D scan curve map, integral NICS (INICS) and FiPC-NICS
2  //The two end points of scanning line are above and below the center of a plane fitted for specific atoms, and the line perpendicularly passes through their center
35-37,68-69,71  //Using these atoms (highlighted in the map above) to define a fitting plane
[Press ENTER button directly]  //The center is chosen as geometric center of the selected atoms (in this step you may also input coordinate of other type of center, such as the ring critical point obtained by topology analysis module of Multiwfn)
10  //An end point of the scanning line is above 10 Å of the fitting plane from the center
0  //Another end point is below 0 Å of the fitting plane from the center, namely the scan will start from the ring center
```

得 *NICS_1D.gjf*（GaussView 可见 Bq 均匀分布扫描线上）。改基组 6-31G* 后运行（输入输出见 *examples\NICS_1D\infinitene_NICS_1D.gjf/.out*）。载入：

```text
2  //Load Gaussian output file of NICS-1D scanning
examples\NICS_scan\infinitene_NICS_1D.out  //Gaussian output file
```

选项 -1 可选分量（默认垂直拟合平面分量 = NICS_ZZ）。选 1 绘曲线（选 -3 可水平翻转）：环芳香（1 Å 处明显为负）。屏幕积分：

```text
Integral of NICS component:    -96.19 ppm*Angstrom
```

选项 5 求极值：

```text
Minimum X (Angstrom):    1.111111  Value:   -0.29469963E+02
Totally found    1 minima,    0 maxima
```

### 实例 2：苯的 NICS_σ,ZZ 与 NICS_π,ZZ 曲线（4.25.13.2）

*examples\NICS_scan\benzene.pdb*（B3LYP/6-31G*，XY 平面 Z=0）：

```text
examples\NICS_scan\benzene.pdb  //Benzene optimized at B3LYP/6-31G* level, the molecule is lying at XY plane of Z=0
25  //Electron delocalization and aromaticity analyses
13  //NICS-1D scan curve map, integral NICS (INICS) and FiPC-NICS
2  //The two end points of scanning line are above and below the center of a plane fitted for specific atoms, and the line perpendicularly passes through their center
1-6  //Using all carbon atoms in this system to define a fitting plane
[Press ENTER button directly]  //The center is chosen as geometric center of the selected atoms
10  //An end point of the scanning line is above 10 Å of the fitting plane from the center
10  //Another end point is below 10 Å of the fitting plane from the center
```

模板要求只算 MO 17,20,21（π-MO）贡献，须 `nmr=csgt iop(10/93=2)`：

```text
#p b3lyp/6-31+G* nmr=csgt iop(10/93=2)

template file

  0  1
[geometry]

AICD.txt

17,20,21

　
```

运行 *NICS_1D.gjf*（输出 *examples\NICS_scan\benzene-pi_NICS_1D.out*；*AICD.txt* 无用可删）。载入：

```text
2  //Load Gaussian output file of NICS-1D scanning
examples\NICS_scan\benzene-pi_NICS_1D.out  //Gaussian output file
1  //Plot NICS curve map, which corresponds to NICS_π,ZZ in present case
```

X=0 为环中心。NICS_σ,ZZ 同法（模板指定 σ MO，见 *examples\NICS_scan\template_NMR_benzene-sigma.gjf*）。*C5H5-.pdb*、*C7H7+.pdb* 同法；界面选项 `3` 导出曲线数据，Origin 合画。σ 电子只影响环中心附近；NICS_π,ZZ 积分：苯 −142.45、C₅H₅⁻ −134.85、C₇H₇⁺ −145.02 ppm⋅Å → π 芳香性 C₇H₇⁺ ≥ 苯 > C₅H₅⁻。

### 实例 3：苯的 FiPC-NICS（4.25.13.3）

```text
examples\NICS_scan\benzene.pdb  //Benzene optimized at B3LYP/6-31G* level, the molecule is lying at XY plane of Z=0
25  //Electron delocalization and aromaticity analyses
13  //NICS-1D scan curve map, integral NICS (INICS) and FiPC-NICS
2  //The two end points of scanning line are above and below the center of a plane fitted for specific atoms, and the line perpendicularly passes through their center
1-6  //Using all carbon atoms in this system to define a fitting plane
[Press ENTER button directly]  //The center is chosen as geometric center of the selected atoms
0  //An end point of the scanning line is 0 Å from the center
10  //Another end point is 10 Å from the center
200  //200 points used in NICS scan
1  // Generate Gaussian input file for NICS-1D scanning
examples\NICS_scan\template_NMR.gjf  //Gaussian template file corresponding NMR calculation at B3LYP/6-31+G* level
```

*NICS_1D.gjf* 改名 *benzene_NICS_1D_0to10.gjf* 运行（输出已提供），载入：

```text
2  // Load Gaussian output file of NICS-1D scanning
examples\NICS_scan\benzene_NICS_1D_0to10.out  //Gaussian output file
6  //Calculate FiPC-NICS
```

```text
FiPC-NICS is   -9.332247 ppm, at   1.179 Angstrom
```

环上 1.179 Å 处 NICS_in 消失，NICS_out = −9.33 ppm（原文献 PBE0/6-311++G** 为 −9.59 ppm @1.18 Å）。同时导出 *FiPC-NICS.txt*（取最后两列 NICS_in/NICS_out 作 X/Y 散点连线图，与原文图 1 一致）。

### 产出

NICS 曲线（存图/导出 .txt）、INICS 积分、FiPC-NICS 值与 *FiPC-NICS.txt*。

### 来源

[3.28.13](../sec-3-28-electron-delocalization-and-aromaticity-analyses.md#32813-nics-1d-扫描曲线图积分-nics-inics-和-fipc-nics)、[4.25.13](../sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md#42513-绘制一维-nics-曲线计算积分-inics-和-fipc-nics-的例子)。

## 子功能14：NICS-2D 扫描平面图

### 说明

绘制漂亮的 NICS 平面图。只关心平面/曲线时优先用子功能 13/14，比三维 ICSS 便宜得多。注意 NICS 与 ICSS 仅差一个符号；此处 NICS_ZZ 指垂直于所关注平面的分量，Z 不总对应 Z 轴。

### 菜单路径

主功能25 → 子功能14。

### 输入要求

结构文件 ＋ Gaussian NMR 模板（含 `[geometry]` 占位）。

### 操作步骤

- (1) 启动载入结构文件；(2) 进主功能 25 子功能 14；(3) 定义作图平面（与主功能 4 完全相同）；(4) 选 1，输入模板路径，生成 *NICS_2D.gjf*（按需改关键词）；(5) Gaussian 运行；(6) 选 2 载入输出；(7) 选 NICS 分量；(8) 图自动显示，关闭后可在后处理菜单调设置重绘。

### 实例 1：coronene 上方 1 Å 的 NICS_ZZ 平面图（4.25.14.1）

*examples\NICS_scan\coronene.pdb*（B3LYP/6-31G*，XY 平面 Z=0）：

```text
examples\NICS_scan\coronene.pdb
25  //Electron delocalization and aromaticity analyses
14  //NICS-2D scan plane map
1  //Color-filled map
[Press ENTER button directly]  //Using default number of grid points (100*100)
0  //Set extension distance
1  // 1 Bohr
1  //XY plane
1a  //Z = 1Å
1  //Gaussian input file for NICS-2D scanning
examples\NICS_scan\template_NMR.gjf  //Template input file of NMR task of Gaussian, which is used to generate Gaussian input file for NICS-2D scan. [geometry] line in this file will be replaced with coordinates of scanning points, while other parts are kept unchanged
NICS_2D.gjf has been generated in current folder, you can properly modify it according to actual situation. Run it by Gaussian, the output file is examples\NICS_scan\coronene_NICS_2D.out.
```

载入：

```text
2  //Load Gaussian output file of NICS-2D scanning
examples\NICS_scan\coronene_NICS_2D.out
5  //Taking ZZ Cartesian component. Since the molecule is exactly in XY plane, the resulting NICS will correspond to NICS_ZZ in common sense (i.e. the component normal to ring plane)
```

屏幕最小/最大值：

```text
The minimum of data:  -43.3034000000000
The maximum of data:   11.3487000000000
```

关图后微调：

```text
4  //Enable showing atom labels
1  //Red
8  //Enable showing bonds
14  //Brown
17  //Set distance threshold for showing atom labels
5  //5 Bohr
y  //Show labels of the atoms that beyond the threshold by light font
1  //Set lower&upper limit of color scale
-45,45
-8  //Change length unit of the graph to Angstrom
-2  //Set label intervals in X, Y, and color scale axes
2,2,10
2  //Enable showing contour lines
3  //Change contour line setting
8  //Generate contour value by arithmetic progression
-50,5,21  //Starting value, step, and total number
y  //Removing existing contour lines. Then the contour values will be -50,-45,-40...40,45,50
1  //Save setting and return
-1  //Replot
```

外圈 1 Å 上方 NICS_ZZ 更负 → 外圈芳香性强于内环。

### 实例 2：N(phenyl)₃ 苯环上方 1 Å 平面图（4.25.14.2，倾斜环）

```text
examples\NICS_scan\N(phenyl)3.pdb  //Structure optimized at B3LYP/6-31G* level
25  //Electron delocalization and aromaticity analyses
14  //NICS-2D scan plane map
1  //Color-filled map
[Press ENTER button directly]  //Using default number of grid points (100*100)
8  //The plotting plane is above or below the plane consisting of specific atoms
23,24,26,30,28,25  //Atoms in the ring of interest
```

记下拟合平面单位法向量：

```text
The unit normal vector is    0.33076524    0.57300118    0.74984265
```

```text
1  //The plotting plane is parallel to the fitting plane and at 1 Å above it. Negative value means below it
6  //Length of the plotting plane (a square region) is set to 6 Å
```

屏幕给出 VMD 绘图平面验证命令：

```tcl
draw triangle {   2.495   2.581  -1.739} {  -1.211  -0.235   2.047} {   6.776  -1.451  -0.547}
draw triangle {  -1.211  -0.235   2.047} {   6.776  -1.451  -0.547} {   3.070  -4.266   3.239}
draw material Transparent
```

载入 pdb 到 VMD 运行上三条命令即见绘图区域。然后：

```text
1  //Generate Gaussian input file for NICS-2D scanning
examples\NICS_scan\template_NMR.gjf  //Template file of Gaussian for NMR task
```

改基组 6-31G* 运行（输出 *examples\NICS_scan\N(phenyl)3_NICS_2D.out*），载入：

```text
2  //Load Gaussian output file of NICS-2D scanning
examples\NICS_scan\N(phenyl)3_NICS_2D.out
0  //Take the NICS component along specific direction
0.33076524    0.57300118    0.74984265  //The unit normal vector shown by Multiwfn earlier
```

调绘图设置（参考主功能 4 例子；颜色 Yellow-Orange-Black，范围 [−34,0]）即得漂亮平面图：环上方 1 Å NICS_ZZ 明显为负 → 芳香；环内侧屏蔽略强于中心。

### 产出

NICS 平面填色图（自动显示，后处理菜单可重调重绘）。

### 来源

[3.28.14](../sec-3-28-electron-delocalization-and-aromaticity-analyses.md#32814-nics-2d-扫描平面图)、[4.25.14](../sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md#42514-绘制二维-nics-平面图的例子)。
