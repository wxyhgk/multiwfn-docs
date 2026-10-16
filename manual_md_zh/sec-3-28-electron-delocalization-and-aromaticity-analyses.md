# **3.28 电子离域与芳香性分析 (25)**

以下各节介绍一些芳香性分析方法，而 Multiwfn 中的大多数电子离域与芳香性分析在其它章节介绍，概述见第 [4.A.3](sec-4-A-special-topics-and-advanced-tutorials.md#4a3-芳香性研究方法概述) 节。

## **3.28.3 生成等化学屏蔽表面 (ICSS) 及相关量**

### **理论**

核独立化学屏蔽 (NICS) 通常在某些特殊点（如环中心）研究，一些论文中通过沿一条线 (1D) 或在一个平面 (2D) 内扫描 NICS 值来研究 NICS。所谓等化学屏蔽表面 (ICSS) 实际上是 NICS 负值的等值面，它清晰地展示了 NICS 在三维空间中的分布，从而给出非常直观的芳香性图像。

本功能用于生成格点数据并可视化各向同性 ICSS、各向异性 ICSS、ICSS$_{XX}$、ICSS$_{YY}$ 和 ICSS$_{ZZ}$，它们本质上分别对应 NICS、NICS$_{ani}$、NICS$_{XX}$、NICS$_{YY}$ 和 NICS$_{ZZ}$ 负值的等值面。顺便说一下，在给定点，NICS$_{ani}$ 定义为 *ε*₃ - (*ε*₁ + *ε*₂)/2，其中 *ε* 表示磁屏蔽张量按从小到大排序的本征值（即 *ε*₃ 为最大者）。

ICSS 的原始论文是 *J. Chem. Soc. Perkin Trans.* 2, **2001**, 1893。而 ICSS$_{ani}$、ICSS$_{XX}$、ICSS$_{YY}$ 和 ICSS$_{ZZ}$ 由我提出。若在您的工作中使用了它们，请引用 *Carbon*, **165**, 468 (2020)，这是我运用 ICSS$_{ZZ}$ 的工作之一。我相信对于平面体系，ICSS 的分量形式一定比 ICSS 更有意义、更有用，正如 NICS$_{ZZ}$ 相对 NICS 有明显优势一样。ICSS$_{ani}$ 有助于揭示不同区域 NICS 的各向异性特征。

### **用法**

Multiwfn 自身不能计算磁屏蔽张量，需要用 Gaussian 来算。进行 ICSS 分析的一般步骤如下

- (1) 为所研究体系准备一个 Gaussian 输入文件，必须显式指定 %chk。几何结构应已优化好。此文件中的关键词将用于准备 NMR 任务的 Gaussian 输入文件。例如见 *examples\ICSS\anthracene.gjf*。

- (2) 启动 Multiwfn 后载入 .gjf 文件，然后进入主功能 25 的子功能 3。

- (3) 按提示设置格点。注意，即使使用中等质量格点也可能相当耗时。因此对中等大小体系一般推荐用低质量格点。

- (4) 输入 *n*，即不跳过第 5 步。

- (5) 在当前文件夹生成许多 Gaussian NMR 任务输入文件，命名为 *NICS0001.gjf*、*NICS0002.gjf*……建议手动检查其中一个，确保格式和关键词正确。

  > **注**
  >
  > 在这些文件中，每个 Bq 原子对应一个格点。在 NMR 任务中 Gaussian 会输出每个 Bq 处以及每个原子核处的磁屏蔽张量。默认每个输入文件含 8000 个原子（真实原子 + Bq），但可通过 *settings.ini* 中的 "NICSnptlim" 参数修改。之所以生成多个文件而不是单个文件，是因为若 Bq 原子数太多，Gaussian 会因内存消耗过大而无法正常运行，且每次 Gaussian 运行的原子总数有上限。若物理内存较大，可尝试将 "NICSnptlim" 设大一些，这可能降低 ICSS 分析的总代价（但 "NICSnptlim" 也不宜太大，例如……
  >
  > 注意，对于 G09 D.01 和 E.01，由于使用默认 Harris 初始猜测时内存分配有个 bug，应总在模板 .gjf 文件的 route 部分加上 "guess=huckel"，否则 NICSnptlim 必须设得很小（如 1000）Gaussian 才能工作；此时 ICSS 计算的总代价往往很高。对于其它 Gaussian 版本，不应加此关键词。若指定 "guess=huckel" 时在 Link 401 模块报错，改用 "guess=core"。对于 G16，不需要 guess 关键词。

- (6) 运行上一步生成的所有 Gaussian 输入文件以得到输出文件。*NICS0001.gjf* 必须先于其它文件运行。最好保持 Multiwfn 运行（若已退出，重启动 Multiwfn，用完全相同的设置重复第 2、3 步，并在第 4 步输入 *y*）。

  > **提示**
  >
  > 可利用脚本 *examples\runall.sh*（Linux）或 *examples\runall.bat*（Windows），它调用 Gaussian 运行当前文件夹中所有 .gjf 文件，生成同名但后缀为 .out 的输出文件。

- (7) 输入上一步所得 Gaussian 输出文件所在文件夹的路径。然后 Multiwfn 将从此文件夹中的 *NICS0001.out*、*NICS0002.out*……载入磁屏蔽张量。

- (8) 选择您感兴趣的性质。

- (9) 通过相应选项可视化等值面或将格点数据导出为 cube 文件。例如，若在第 8 步选了 "ZZ component"，则等值面和格点数据对应 ICSS$_{ZZ}$。也可选择 "-1 Load another ICSS form" 研究其它形式。

注意，若这不是您第一次分析该体系，且手头已有该体系 NMR 任务的 Gaussian 输出文件，可从第 2 步开始并在第 4 步输入 *y* 以跳过第 5、6 步。此时，第 3 步的格点设置必须与当初生成 NMR 任务 Gaussian 输出文件时用的完全一致。

例子见第 [4.25.3](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md#4253-研究苯的等化学屏蔽面-icss-和磁屏蔽分布) 节。

## **3.28.4 求非平面或倾斜体系的 NICS$_{ZZ}$ 值**

### **简介**

核独立化学位移 (NICS) 是很常用的衡量芳香性的指标。许多论文，如 *Org. Lett.*, **8**, 863 (2006) 表明，NICS(0)$_{ZZ}$ 或 NICS(1)$_{ZZ}$ 是比 NICS 原始定义（即现在所称的 NICS(0)）更好的指标。

对于严格平面体系，若体系平面平行于 XY 平面，则 NICS(0)$_{ZZ}$ 即环中心处磁屏蔽张量的 ZZ 分量。NICS(1)$_{ZZ}$ 与 NICS(0)$_{ZZ}$ 的唯一区别在于计算点不是环中心，而是环中心上方（或下方）平面外 1 Å 的点。注意，环中心的定义很任意，原始定义用几何中心，有人用质心，一些研究者推荐用 AIM 理论的环临界点 (RCP) 作环中心，如 *WIREs Comput. Mol. Sci.*, **3**, 105 (2013)。（我个人认为用 RCP 是最好的选择）

若感兴趣的环是扭曲的、非严格平面或倾斜的，NICS$_{ZZ}$ 的计算很困难，因为无法直接从量子化学程序输出文件中得到垂直于平面方向的磁屏蔽张量分量。而且对 NICS(1)$_{ZZ}$ 而言，难以恰当设定要计算的位置。本功能即为解决这些困难而设计。

在本功能中，给定环法向的磁屏蔽张量分量按 *σ*$_{\perp }$=**u**$^{T}$**σu** 计算，其中 **σ** 为磁屏蔽张量，**u** 为垂直于环的单位列向量，**u**$^{T}$ 为 **u** 的转置。

### **求 NICS(1)$_{ZZ}$ 的步骤**

若要计算非平面体系的 NICS(1)$_{ZZ}$，应按以下步骤：

- (1) 用 Multiwfn 打开含体系原子坐标的文件（如 .xyz/.pdb/.mol/.wfn/.mwfn/.fch/.molden……）

- (2) 确定环中心。可用拓扑分析模块（主功能 2）定位 RCP，或用主功能 100 的子功能 21 得到几何中心或质心。

- (3) 进入主功能 25 的子功能 4（即本功能），输入刚才得到的环中心，再输入一系列原子的序号以拟合环平面。通常输入的原子应为感兴趣环中的全部原子。然后会输出环中心上方和下方距环平面 1 Å 的点的坐标。

  > **提示 1**
  >
  > Multiwfn 还输出垂直于环平面的单位法向量，借此可容易导出如计算 NICS(2)、NICS(3.5)……所用的位置。

  > **提示 2**
  >
  > 若您只想用几何中心且拟合平面选用环中全部原子，可跳过第 (2) 步，因为如屏幕提示所述，当 Multiwfn 请您输入环中心时若直接按回车，则环中心自动定为拟合环平面所选原子的几何中心。

- (4) 用上一步得到的两个点之一，用量子化学程序计算相应位置的磁屏蔽张量

- (5) 按量子化学程序的输出在 Multiwfn 中输入磁屏蔽张量的所有分量。则 Multiwfn 输出的 "The shielding value normal to the plane" 的负值即 NICS(1)$_{ZZ}$。

注意，若体系相对平面不对称，实际上 NICS(1)$_{ZZ}$ 和 NICS(-1)$_{ZZ}$ 不同。要得到通常意义的 NICS(1)$_{ZZ}$，可在适当时取二者平均。

### **求 NICS(0)$_{ZZ}$ 的步骤**

计算 NICS(0)$_{ZZ}$ 时过程更简单：

- (1) 与上示第 1 步相同

- (2) 与上示第 2 步相同

- (3) 用第 (2) 步得到的环中心，用量子化学程序计算该位置的磁屏蔽张量。

- (4) 进入主功能 25 的子功能 4，输入环中心，再输入一系列原子的序号以拟合环平面。然后按量子化学程序的输出输入磁屏蔽张量的所有分量。则 Multiwfn 输出的 "The shielding value normal to the plane" 的负值即 NICS(0)$_{ZZ}$。

有一篇博客文章说明了本功能：“使用 Multiwfn 计算倾斜和扭曲环的 NICS_ZZ”<http://sobereva.com/261>（中文）。

> **所需信息**
>
> 原子坐标

## **3.28.6 计算 HOMA 和 Bird 芳香性指数**

### **HOMA 指数**

谐振子芳香性度量 (HOMA) 是最常用的基于几何的芳香性度量。该量最初在 *Tetrahedron Lett.*, **13**, 3839 (1972) 中提出，推广形式见 *J. Chem. Inf. Comput. Sci.*, **33**, 70 (1993)。推广的 HOMA 可写为（注意 HOMA 公式已被众多论文错误引用）

$$
\mathrm{HOMA}=1-\sum_i\frac{\alpha_{i,j}}{N}(R_{\mathrm{ref}}-R_{i,j})^2
$$

其中 $N$ 为所考虑原子的总数，$j$ 表示原子 *i* 的下一个原子，α 和 $R_{\mathrm{ref}}$ 为原论文中对每类原子对预先算好的常数。若 HOMA 等于 1，意味着每根键长都与最优值 $R_{\mathrm{ref}}$ 相同，环完全芳香。若 HOMA 等于 0，意味着环完全非芳香。若 HOMA 为显著负值，则环呈反芳香性特征。

HOMA 发明人按如下方式发展 HOMA 参数，详见 *Chem. Inf. Comput. Sci.*, **33**, 70 (1993)

$$
\begin{gathered}R_{\mathrm{ref}}=(R_{\mathrm{s}}+wR_{\mathrm{d}})/(1+w)\\\alpha=\frac{2}{(R_{\mathrm{s}}-R_{\mathrm{ref}})^2+(R_{\mathrm{d}}-R_{\mathrm{ref}})^2}\end{gathered}
$$

其中 $R_{\mathrm{s}}$ 和 $R_{\mathrm{d}}$ 分别为单键和双键的实验键长。$w$ = $k_{\mathrm{d}}$ / $k_{\mathrm{s}}$，其中 $k_{\mathrm{s}}$ 和 $k_{\mathrm{d}}$ 分别为单键和双键的力常数。通常假设 $w$ 为 2.0（也有特殊情况，如 BN 键 $w$ =4.2）。例如，CO 键的 $R_{\mathrm{ref}}$ 和 *α* 参数基于甲酸中 C-O 和 C=O 键的实验长度并假设 $w$ =2.0 导出。

HOMA 可用主功能 25 的子功能 6 计算。当选选项 0 时，Multiwfn 提示输入局域体系中原子的序号，例如 *2,3,4,5,6,7*（假设环中有六个原子。输入顺序必须与原子连接顺序一致），然后 HOMA 值和每对原子的贡献立即输出到屏幕。例如，在 MP2/6-311+G\*\* 下优化的噻吩，输出为

```text
        Atom pair         Contribution  Bond length(Angstrom)
   1(C )  --    2(C ):      -0.001852        1.382006
   2(C )  --    3(C ):      -0.056708        1.421170
   3(C )  --    4(C ):      -0.001852        1.382006
   4(C )  --    5(S ):      -0.023886        1.712627
   5(S )  --    1(C ):      -0.023886        1.712627
HOMA value is    0.891817
```

由于 0.891817 接近 1，HOMA 分析表明噻吩有突出的芳香性。

内置 *α* 和 $R_{\mathrm{ref}}$ 参数的来源如下：

- CC、CN、CO、CP、CS、NN、NO：*Chem. Inf. Comput. Sci.*, **33**, 70 (1993)

- BN：*Tetrahedron*, **54**, 14913 (1998)

- BC：*Struct. Chem.*, **23**, 595 (2012)

  内置参数可由用户经选项 1 修改或补充。

### **Bird 指数**

Bird 指数 (*Tetrahedron*, **41**, 1409 (1985)) 是另一种旨在度量芳香性的基于几何的量，可用主功能 25 子功能 6 的选项 2 计算。公式为

$$
\begin{gathered}I=100[1-(V/V_{\mathrm{K}})]\end{gathered}
$$

其中

$$
\begin{gathered}V=\frac{100}{\overline{N}}\sqrt{\frac{\sum_i(N_{i,j}-\overline{N})^2}{n}}\quad\quad N_{i,j}=\frac{a}{R_{i,j}}-b\end{gathered}
$$

公式中，$i$ 遍历环中所有键，$j$ 表示原子 *i* 的下一个原子。$n$ 为所考虑键的总数。$N$ 表示 Gordy 键级，$\bar{N}$ 为 $N$ 值的平均值。$R$ *$_{i,j}$* 为键长。$a$ 和 $b$ 分别为每类键的预定参数。$V_{\mathrm{K}}$ 为预定的参考 $V$，对五元和六元环其值分别为 35 和 33.2。Bird 指数越接近 100，芳香性越强。

可用的 $a$ 和 $b$ 参数包括 C-C、C-N、C-O、C-S、N-O 和 N-N，取自 *Tetrahedron*, **57**, 5715 (2001)，B-N 参数取自 *Tetrahedron*, **54**, 14913 (1998)。对其它键型用户应通过选项 3 提供相应参数。用选项 4 用户可调整或增加 $V_{\mathrm{K}}$ 参数。

本功能的相应例子见第 [4.25.6](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md#4256-计算菲的-homa-和-bird-芳香性指标) 节。

> **所需信息**
>
> 原子坐标

## **3.28.7 HOMAc 和 HOMER**

HOMER 和 HOMAc 分别在 *Phys. Chem. Chem. Phys.*, **25**, 16763 (2023) 和 *J. Org. Chem.*, **90**, 1297 (2025) 中提出。它们重新参数化了 $R_{\mathrm{ref}}$ 和 *α* 参数，可用于含 CC、CN、CO、NN 键的环。

HOMER 是 Harmonic Oscillator Model of Excited-state aRomaticity（激发态芳香性谐振子模型）的缩写。HOMER 旨在仅基于优化几何表征 T₁ 态芳香性，发现它与 T₁ 态计算的 NICS(1)$_{zz}$ 指数有合理相关性；相比之下，HOMA 与 NICS(1)$_{zz}$ 几乎无相关性。当然，HOMER 无法表征 Franck-Condon 点的 T₁ 芳香性，因为几何结构与 S₀ 相同。

HOMAc 旨在改善 HOMA 在判断 S₀ 基态芳香性上的能力。原论文中的比较确实表明它优于 HOMA。所以推荐用 HOMAc 代替 HOMA。

注意，HOMAc 和 HOMER 的 $R_{\mathrm{ref}}$ 参数按如下方式导出：在相应极小点处对原型 S₀ 和 T₁ 芳香分子恰为 1.0，而 HOMAc 和 HOMER 的 *α* 参数进一步按如下方式确定：对原型 S₀ 和 T₁ 反芳香分子在相应极小点处非常接近 -1。HOMAc 和 HOMER 的参数由极昂贵的 CASPT2/cc-pVQZ 级别优化的几何导出，但这些指数对 DFT 优化的结构也适用得不错。

HOMAc 和 HOMER 可分别经主功能 25 的子功能 6a 和 6b 计算。用法与 HOMA 完全相同。

> **所需信息**
>
> 原子坐标

## **3.28.13 NICS-1D 扫描曲线图、积分 NICS (INICS) 和 FiPC-NICS**

### **背景**

众所周知，核独立化学位移 (NICS) 是度量芳香性的很有用的量。通常在环中心或环中心上方/下方 1 Å 处计算 NICS。若从环中心出发垂直于环扫描 NICS，显然可得到关于芳香性的丰富得多的信息。

如 *J. Phys. Chem. A*, **123**, 3922 (2019) 所提，对 NICS 曲线积分比只研究特定点处的 NICS 是判断芳香性更可靠的方式，该积分称为 INICS 指数。

FiPC-NICS 芳香性指数在 *Inorg. Chem.*, **53**, 3579 (2014) 中提出。任一点的 NICS 可视为面内分量 NICS$_{in}$=(NICS$_{XX}$+NICS$_{YY}$)/3 与面外分量 NICS$_{out}$=NICS$_{ZZ}$/3 之和。前述扫描路径上 NICS$_{in}$ 等于 0 处的 NICS$_{out}$ 值定义为无面内分量 NICS (FiPC-NICS)。由于 NICS$_{in}$ 主要由对应 σ 键和孤对的定域电子贡献，FiPC-NICS 值即完全不受面内分量污染的 NICS，被认为是在表征芳香性上比 NICS(1)$_{ZZ}$ 更严格的指标。事实上，常用的 NICS(1)$_{ZZ}$ 是 FiPC-NICS 可接受的近似，因为在该论文中发现计算 FiPC-NICS 的点离环中心的距离离 1 Å 不远。此外，该论文表明，以 NICS$_{in}$ 和 NICS$_{out}$ 分别为 X、Y 轴的扫描数据曲线图的特征也有助于指认芳香性和反芳香性。

### **用法**

本功能对应主功能 25 的子功能 13。在本功能中，可很方便地沿特定线绘制 NICS 曲线图并得到 INICS 和 FiPC-NICS。所需步骤如下：

- (1) 启动 Multiwfn 并载入含待研究体系结构信息的文件

- (2) 进入主功能 25 的子功能 13

- (3) 定义一条线和均匀分布在线上的扫描点数

- (4) 选选项 1 生成 Gaussian 程序输入文件。需输入一个 Gaussian 模板文件的路径，该文件应对应标准 NMR 任务，但坐标部分替换为 \[geometry\]，例子见 *examples\NICS_scan\template_NMR.gjf*。然后在当前文件夹生成 *NICS_1D.gjf*，可按实际情况适当修改关键词

- (5) 手动用 Gaussian 运行该 .gjf 文件

- (6) 选选项 2 并输入 Gaussian 输出文件的路径以载入

- (7) 选择感兴趣的分量。默认 Multiwfn 提取的 NICS 数据是磁屏蔽张量投影到扫描线方向分量的负值。也可选择提取各向同性、各向异性、XX/YY/ZZ 分量，或特定矢量方向的分量。

- (8) 在新界面中可绘制 NICS 曲线图，或保存为图像文件，或将曲线数据导出为 .txt 文件。也可用此界面中相应选项计算 INICS 或 FiPC-NICS 指数（注意，仅当扫描路径平行于笛卡尔轴时才能计算 FiPC-NICS）。

在第 (3) 步中，线可用两种方式指定：

- (1) 手动指定两个端点的坐标。

- (2) 输入一些原子的序号，为它们拟合一个平面。然后分别指定相对原子几何中心在平面上方和下方的距离。

值得注意的是，若恰当设置 Gaussian 模板文件，Multiwfn 能绘制特定分子轨道贡献的 NICS 曲线，如绘制 NICS$_{σ,zz}$ 和 NICS$_{π,zz}$ 曲线。

例子见第 [4.25.13](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md#42513-绘制一维-nics-曲线计算积分-inics-和-fipc-nics-的例子) 节。

## **3.28.14 NICS-2D 扫描平面图**

Multiwfn 能很容易绘制漂亮的 NICS 平面图，所需步骤如下：

- (1) 启动 Multiwfn 并载入含待研究体系结构信息的文件

- (2) 进入主功能 25 的子功能 14

- (3) 定义作图平面，设置与主功能 4 完全相同

- (4) 选选项 1 生成 Gaussian 程序输入文件。需输入一个 Gaussian 模板文件的路径，该文件应对应标准 NMR 任务，但坐标部分替换为 \[geometry\]，例子见 *examples\NICS_scan\template_NMR.gjf*。然后在当前文件夹生成 *NICS_2D.gjf*，可按实际情况适当修改关键词

- (5) 手动用 Gaussian 运行该 .gjf 文件

- (6) 选选项 2 并输入 Gaussian 输出文件的路径以载入

- (7) 选择感兴趣的 NICS 分量

- (8) NICS 图自动显示在屏幕上。关闭后可在后处理菜单调整作图设置再重绘。

例子见第 [4.25.14](sec-4-25-examples-of-electron-delocalization-and-aromaticity-analyses.md#42514-绘制二维-nics-平面图的例子) 节。
