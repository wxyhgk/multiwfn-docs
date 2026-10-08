# 电子离域与芳香性分析 (Electron delocalization and aromaticity analyses) (25)

> Multiwfn manual, p.377–383.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.377 -->


使用本功能研究实际分子的例子见 4.24.5 节。

## 3.28 电子离域与芳香性分析 (Electron delocalization and aromaticity analyses) (25)

以下各节介绍了一些芳香性分析方法，而 Multiwfn 中的大多数电子离域与芳香性分析在其它节中介绍，概述见 4.A.3 节。

### 3.28.3 生成等化学屏蔽表面 (Generate iso-chemical shielding surfaces, ICSS) 及相关量 (related quantities)

理论 (Theory) 核独立化学屏蔽 (Nuclear independent chemical shielding, NICS) 通常在一些特殊点 (例如环中心) 处研究，在一些论文中通过在一条直线 (1D) 上或一个平面 (2D) 内扫描其值来研究 NICS。所谓等化学屏蔽表面 (iso-chemical shielding surface, ICSS) 实际上就是 NICS 负值的等值面，它清楚地展示了 NICS 在三维空间中的分布，因而给出了关于芳香性非常直观的图像。

本功能用于生成格点数据并可视化各向同性 ICSS、各向异性 ICSS、ICSSXX、ICSSYY 和 ICSSZZ，它们本质上分别对应于 NICS、NICSani、NICSXX、NICSYY 和 NICSZZ 负值的等值面。顺便说一下，在给定点，NICSani 定义为

ε3 - (ε1 + ε2)/2，其中 ε 表示磁屏蔽张量按从小到大排序的本征值 (即 ε3 是最大的那个)。

ICSS 的原始论文是 J. Chem. Soc. Perkin Trans. 2, 2001, 1893。而 ICSSani、ICSSXX、ICSSYY 和 ICSSZZ 是由我提出的。如果你在工作中使用了它们，请引用 Carbon, 165, 468 (2020)，这是我运用 ICSSZZ 的工作之一。我相信对于平面体系，ICSS 的分量形式一定比 ICSS 本身更有意义、更有用，正如 NICSZZ 比 NICS 有明显优势一样。ICSSani 有助于揭示不同区域 NICS 的各向异性特征。

用法 (Usage) Multiwfn 本身不能计算磁屏蔽张量，因此需要用 Gaussian 来完成。进行 ICSS 分析的一般步骤如下所示

(1) 为所研究体系准备一个 Gaussian 输入文件，必须明确指定 %chk。几何结构应该是已经优化过的。该文件中的关键词将用于准备 NMR 任务的 Gaussian 输入文件。例如，见 examples\ICSS\anthracene.gjf。

(2) 启动 Multiwfn 后，载入 .gjf 文件，然后进入主功能 (main function) 25 的子功能 (subfunction) 3。 (3) 按提示设置格点。注意，即使使用中等质量格点也可能相当耗时。因此对于中等大小体系一般推荐用低质量格点。

(4) 输入 n，即不跳过步骤 5。 (5) 在当前文件夹下生成了许多 Gaussian NMR 任务的输入文件，它们被命名为 NICS0001.gjf、NICS0002.gjf……建议手动检查其中一个，以确保格式和关键词正确。

在这些文件中，每个 Bq 原子对应一个格点。在 NMR 任务中 Gaussian 会输出每个 Bq 处以及每个原子核处的磁


<!-- p.378 -->



屏蔽张量。默认每个输入文件包含 8000 个原子 (真实原子 + Bq)，但这可以通过 `settings.ini` 中的 “NICSnptlim” 参数改变。之所以生成多个分开的文件而不是单个文件，是因为如果 Bq 原子数太多，由于内存消耗过大 Gaussian 无法正常运行，而且每次 Gaussian 运行的原子总数也有上限。如果你的物理内存很大，可以尝试把 “NICSnptlim” 设大一些，这可能降低 ICSS 分析的总体开销 (但 “NICSnptlim” 也不宜太大，例如 “NICSnptlim=10000” 的总计算耗时甚至高于 “NICSnptlim=1000”！)。

注意，对于 G09 D.01 和 E.01，由于在使用默认 Harris 初始猜测时内存分配有个 bug，你应该始终在模板 .gjf 文件的 route 部分加上 “guess=huckel”，否则必须把 NICSnptlim 设为很小的值 (例如 1000) 才能让 Gaussian 工作；在这种情况下 ICSS 计算的总体开销往往相当高。对于其它 Gaussian 版本，不应加该关键词。如果在指定 “guess=huckel” 时在 Link 401 模块出现错误，试用 “guess=core” 代替。对于 G16，不需要 guess 关键词。

(6) 运行上一步生成的所有 Gaussian 输入文件以得到输出文件。NICS0001.gjf 必须先于其它任何文件运行。最好保持 Multiwfn 运行 (如果你已经退出了，就重新启动 Multiwfn，并用完全相同的设置重复步骤 2 和 3，在步骤 4 输入 y)。

提示 (Hint)：你可以利用脚本 examples\runall.sh (用于 Linux) 或 examples\runall.bat (用于 Windows)，它调用 Gaussian 运行当前文件夹下所有 .gjf 文件，生成同名但后缀为 .out 的输出文件。

(7) 输入包含上一步得到的 Gaussian 输出文件的文件夹路径。然后 Multiwfn 会从该文件夹下的 NICS0001.out、NICS0002.out……中载入磁屏蔽张量。

(8) 选择你感兴趣的性质。 (9) 通过相应选项可视化等值面或把格点数据导出为 cube 文件。例如，如果你在步骤 8 选择了 “ZZ component”(ZZ 分量)，那么等值面和格点数据就对应于 ICSSZZ。你还可以选择 “-1 Load another ICSS form”(载入另一种 ICSS 形式) 来研究其它形式。

注意，如果这不是你第一次分析你的体系，而你手头已经有当前体系 NMR 任务的 Gaussian 输出文件，你可以从步骤 2 开始，并在步骤 4 输入 y，以跳过步骤 5 和 6。在这种情况下，步骤 3 选择的格点设置必须与当初生成 NMR 任务 Gaussian 输出文件时用的完全一致。

例子见 4.25.3 节。

### 3.28.4 获得非平面或倾斜体系的 NICSZZ 值 (Obtain NICSZZ value for non-planar or tilted system)

引言 (Introduction) 核独立化学位移 (Nucleus-independent chemical shift, NICS) 是非常流行的用于衡量芳香性的指标。在许多论文中，例如 Org. Lett., 8, 863 (2006)，已表明 NICS(0)ZZ 或 NICS(1)ZZ 是比最初定义的 NICS(目前称为 NICS(0))更好的指标。

对于完全平面体系，如果体系平面平行于 XY 平面，那么 NICS(0)ZZ 就是指环中心处磁屏蔽张量的 ZZ 分量。NICS(1)ZZ 与 NICS(0)ZZ 唯一的区别是计算点不是环中心，而是从环中心沿平面上方 (或下方) 1 Å 的点。注意，环中心的定义是高度任意的，最初的定义用几何中心，有人用质心，一些研究者推荐用 AIM 理论的环临界点 (ring critical point, RCP) 作为环中心，例如 WIREs Comput. Mol. Sci., 3, 105 (2013)。(我个人认为用 RCP 是最佳选择)

如果所关注的环是扭曲的、不是完全平面或倾斜的，NICSZZ 的计算就很困难，

<!-- p.379 -->


因为不能直接从量子化学程序的输出文件中获得垂直于平面方向的磁屏蔽张量分量。而且，对于 NICS(1)ZZ，很难恰当设置要计算的位置。本功能就是为解决这些困难而设计的。

在本功能中，垂直于给定环方向的磁屏蔽张量分量计算为 σ⊥=uTσu，其中 σ 是磁屏蔽张量，u 是垂直于环的单位列矢量，uT 是 u 的转置。

获得 NICS(1)ZZ 的步骤 (Steps for obtaining NICS(1)ZZ) 如果你想对非平面体系计算 NICS(1)ZZ，应该遵循以下步骤： (1) 用 Multiwfn 打开一个包含你的体系原子坐标的文件 (例如 .xyz/.pdb/.mol/.wfn/.mwfn/.fch/.molden……)

(2) 确定环中心。你可以用拓扑分析模块 (主功能 (main function) 2) 定位 RCP，或用主功能 (main function) 100 的子功能 (subfunction) 21 获得几何中心或质心。

(3) 进入主功能 (main function) 25 的子功能 (subfunction) 4 (即本功能)，输入你刚才得到的环中心，并输入一系列用于拟合环平面的原子的序号。通常输入的原子应该是所关注环中的全部原子。然后程序会输出从环中心算起在环平面上方和下方 1 Å 的点的坐标。

提示 1 (Hint 1)：Multiwfn 还会输出垂直于环平面的单位法矢量，利用它你可以很容易推导出用于计算例如 NICS(2)、NICS(3.5)……的位置。

提示 2 (Hint 2)：如果你只是想用几何中心，且选择环中全部原子来拟合平面，那么步骤 (2) 可以跳过，因为如屏幕提示中所说，当 Multiwfn 要求你输入环中心时若直接按 ENTER 键，它会自动确定为你选择的拟合环平面原子的几何中心。

(4) 用上一步得到的两个点中的任一个，用量子化学程序计算相应位置的磁屏蔽张量

(5) 按照你的量子化学程序的输出，在 Multiwfn 中输入磁屏蔽张量的全部组分。然后 Multiwfn 输出的 “The shielding value normal to the plane”(垂直于平面的屏蔽值) 的负值就是 NICS(1)ZZ。

注意，如果体系相对该平面不对称，实际上 NICS(1)ZZ 和 NICS(-1)ZZ 是不同的。要得到通常意义上的 NICS(1)ZZ，在合适时可以取它们的平均值。

获得 NICS(0)ZZ 的步骤 (Steps for obtaining NICS(0)ZZ) 计算 NICS(0)ZZ 的过程更简单： (1) 与上面所示步骤 1 相同 (2) 与上面所示步骤 2 相同 (3) 用步骤 (2) 得到的环中心，用量子化学程序计算该位置的磁屏蔽张量。

(4) 进入主功能 (main function) 25 的子功能 (subfunction) 4，输入环中心，并输入一系列用于拟合环平面的原子的序号。然后按照你的量子化学程序的输出输入磁屏蔽张量的全部组分。然后 Multiwfn 输出的 “The shielding value normal to the plane”(垂直于平面的屏蔽值) 的负值就是 NICS(0)ZZ。

有一篇博客文章说明了本功能：“Using Multiwfn to calculate NICS_ZZ of tilted and twisted rings”(用 Multiwfn 计算倾斜和扭曲环的 NICS_ZZ) http://sobereva.com/261 (中文)。

所需信息 (Information needed)：原子坐标 (Atom coordinates)

<!-- p.380 -->


### 3.28.6 计算 HOMA 和 Bird 芳香性指数 (Calculate HOMA and Bird aromaticity index)

HOMA 指数 (HOMA index) 谐振子芳香性度量 (Harmonic oscillator measure of aromaticity, HOMA) 是最流行的基于几何的衡量芳香性的指标。该量最初在 Tetrahedron Lett., 13, 3839 (1972) 中提出，随后广义形式在 J. Chem. Inf. Comput. Sci., 33, 70 (1993) 中给出。广义 HOMA 可写为 (注意 HOMA 公式已被大量论文错误引用)

,2ref,HOMA1()i j α= −− i ji RRN

其中 N 是所考虑原子的总数，j 表示与原子 i 相连的下一个原子，α 和 RRef 是原论文中对每种原子对预先计算的常数。如果 HOMA 等于 1，意味着每个键长都与最优值 Rref 完全相同，因而环是完全芳香的。而如果 HOMA 等于 0，意味着环是完全非芳香的。如果 HOMA 是显著的负值，则环表现出反芳香性特征。

HOMA 的发明人按以下方式发展了 HOMA 参数，详见 Chem. Inf. Comput. Sci., 33, 70 (1993)

$$\begin{aligned}&R_{ref}=(R_{s}+wR_{d})/(1+w)\\ &\alpha=\frac{2}{(R_{s}-R_{ref})^{2}+(R_{d}-R_{ref})^{2}}\\ \end{aligned}$$

<!-- formula-ocr: formula_p380_284.png 已替换为LaTeX, 原图保留备查 -->

其中 Rs 和 Rd 分别是单键和双键的实验键长。w=kd/ks，其中 ks 和 kd 分别是单键和双键的力常数。通常，w 假设为 2.0 (也有特殊情况，例如 BN 键 w=4.2)。例如，CO 键的 Rref 和 α 参数是基于甲酸中 C-O 和 C=O 键的实验长度并假设 w=2.0 推导的。

HOMA 可由主功能 (main function) 25 的子功能 (subfunction) 6 计算。当你选择选项 (option) 0 时，Multiwfn 会提示你输入局域体系中原子的序号，例如，2,3,4,5,6,7 (假设环中有六个原子。输入顺序必须与原子连接顺序一致)，然后 HOMA 值和每对原子的贡献会立即输出到屏幕上。例如，在 MP2/6-311+G** 下优化的噻吩，输出为

```text
        Atom pair         Contribution  Bond length(Angstrom)
   1(C )  --    2(C ):      -0.001852        1.382006
   2(C )  --    3(C ):      -0.056708        1.421170
   3(C )  --    4(C ):      -0.001852        1.382006
   4(C )  --    5(S ):      -0.023886        1.712627
   5(S )  --    1(C ):      -0.023886        1.712627
HOMA value is    0.891817
```

由于 0.891817 接近于 1，HOMA 分析表明噻吩具有显著芳香性。

内置 α 和 RRef 参数的来源如下所示：
- CC、CN、CO、CP、CS、NN、NO：Chem. Inf. Comput. Sci., 33, 70 (1993)
- BN：Tetrahedron, 54, 14913 (1998)
- BC：Struct. Chem., 23, 595 (2012)

<!-- p.381 -->


内置参数可由用户通过选项 (option) 1 修改或补充。

Bird 指数 (Bird index) Bird 指数 (Tetrahedron, 41, 1409 (1985)) 是另一种旨在衡量芳香性的基于几何的量，可由主功能 (main function) 25 的子功能 (subfunction) 6 的选项 (option) 2 计算。公式为

K100[1(/)]IV V=−

其中

$$V=\frac{100}{\overline{N}}\sqrt{\frac{\sum_{i}(N_{i.j}-\overline{N})^{2}}{n}}\quad N_{i.j}=\frac{a}{R_{i,j}}-b$$

<!-- formula-ocr: formula_p381_285.png 已替换为LaTeX, 原图保留备查 -->

在公式中，i 遍历环中所有键，j 表示与原子 i 相连的下一个原子。n 是所考虑键的总数。N 表示 Gordy 键级，𝑁̅ 是 N 值的平均值。Ri,j 是键长。a 和 b 分别是对每种键类型预定义的参数。VK 是预先确定的参考 V 值，对五元环和六元环分别为 35 和 33.2。Bird 指数越接近 100，芳香性越强。

可用的 a 和 b 参数包括 C-C、C-N、C-O、C-S、N-O 和 N-N，它们取自 Tetrahedron, 57, 5715 (2001)，B-N 参数取自 Tetrahedron, 54, 14913 (1998)。对于其它类型键用户应通过选项 (option) 3 提供相应参数。通过选项 (option) 4 用户可以调节或添加 VK 参数。

本功能的相应例子在 4.25.6 节给出。所需信息 (Information needed)：原子坐标 (Atom coordinates)

### 3.28.7 HOMAc 和 HOMER (HOMAc and HOMER)

HOMER 和 HOMAc 分别在 Phys. Chem. Chem. Phys., 25, 16763 (2023) 和 J.

Org. Chem., 90, 1297 (2025) 中提出。它们重新参数化了 Rref 和 α 参数，可用于含 CC、CN、CO、NN 键的环。

HOMER 是激发态芳香性谐振子模型 (Harmonic Oscillator Model of Excited-state aRomaticity) 的缩写。HOMER 旨在仅基于优化几何来表征 T1 态的芳香性，发现它与对 T1 态计算的 NICS(1)zz 指数有合理相关性；相比之下，HOMA 与 NICS(1)zz 几乎没有相关性。当然，HOMER 不能表征 Franck-Condon 点的 T1 芳香性，因为几何结构与 S0 相同。

HOMAc 旨在改善 HOMA 在确定 S0 基态芳香性方面的能力。确实，原论文中的比较表明它表现优于 HOMA。因此，推荐用 HOMAc 代替 HOMA。

需要注意的是，HOMAc 和 HOMER 的 Rref 参数按以下方式推导：它们对相应极小点处的原型 S0 和 T1 芳香性分子恰好为 1.0，

而 HOMAc 和 HOMER 的 α 参数进一步按以下方式确定：它们对相应极小点处的原型 S0 和 T1 反芳香性分子非常接近于 -1，

<!-- p.382 -->


分别地。HOMAc 和 HOMER 中的参数是从在非常昂贵的 CASPT2/cc-pVQZ 水平下优化的几何结构推导的，然而，这些指数对 DFT 优化的结构也 reasonably 适用。

HOMAc 和 HOMER 可分别通过主功能 (main function) 25 的子功能 (subfunction) 6a 和 6b 计算。用法与 HOMA 完全相同。

所需信息 (Information needed)：原子坐标 (Atom coordinates)

### 3.28.13 NICS-1D 扫描曲线图、积分 NICS (integral NICS, INICS) 和 FiPC-NICS (NICS-1D scan curve map, integral NICS (INICS) and FiPC-NICS)

背景 (Background) 众所周知，核独立化学位移 (nucleus-independent chemical shift, NICS) 是衡量芳香性非常有用的量。通常 NICS 在环中心或环中心上方/下方 1 Å 处计算。如果从环中心开始垂直于环扫描 NICS，显然可以得到关于芳香性丰富得多的信息。

如 J. Phys. Chem. A, 123, 3922 (2019) 中所提出，对 NICS 曲线积分是比只研究特定点 NICS 更可靠的确定芳香性的方法，该积分称为 INICS 指数。

FiPC-NICS 芳香性指数在 Inorg. Chem., 53, 3579 (2014) 中提出。任一点的 NICS 可看作面内分量 NICSin=(NICSXX+NICSYY)/3 与面外分量 NICSout=NICSZZ/3 之和。在 NICSin 等于 0 的上述扫描路径处的 NICSout 值定义为无面内分量 NICS (free of in-plane component NICS, FiPC-NICS)。因为 NICSin 主要由对应于 σ 键和孤对的定域电子贡献，FiPC-NICS 值，即完全不受面内分量污染的 NICS，被认为是比 NICS(1)ZZ 更严格的表征芳香性的指标。事实上，流行的 NICS(1)ZZ 是 FiPC-NICS 可接受的近似，因为在该论文中发现计算 FiPC-NICS 的距环中心距离离 1 Å 不远。此外，该论文表明，以 NICSin 和 NICSout 分别为 X 轴和 Y 轴的扫描数据曲线图的特征也有助于指认芳香性和反芳香性。

用法 (Usage) 本功能对应于主功能 (main function) 25 的子功能 (subfunction) 13。在本功能中，你可以非常容易地沿特定直线绘制 NICS 曲线图并得到 INICS 和 FiPC-NICS。需要以下步骤：

(1) 启动 Multiwfn，然后载入一个包含待研究体系结构信息的文件 (2) 进入主功能 (main function) 25 的子功能 (subfunction) 13 (3) 定义一条直线和均匀分布在该直线上的扫描点数 (4) 选择选项 (option) 1 以生成 Gaussian 程序的输入文件。你需要输入一个

Gaussian 模板文件的路径，该文件应对应于标准 NMR 任务，但坐标部分应替换为 [geometry]，见 examples\NICS_scan\template_NMR.gjf。例如。然后会在当前文件夹下生成 NICS_1D.gjf，你可以根据实际情况恰当修改

<!-- p.383 -->


关键词 (5) 手动用 Gaussian 运行 .gjf 文件 (6) 选择选项 (option) 2 并输入 Gaussian 输出文件的路径以载入它 (7) 选择感兴趣的分量。默认情况下，Multiwfn 提取的 NICS 数据是

磁屏蔽张量投影到扫描直线方向的分量的负值。你还可以选择提取各向同性、各向异性、XX/YY/ZZ 分量，或沿特定矢量方向的分量。 (8) 在新界面中，你可以绘制 NICS 曲线图，或将其保存为图像文件，或把

曲线数据导出为 .txt 文件。你还可以用该界面中的相应选项计算 INICS 或 FiPC-NICS 指数 (注意，只有当扫描路径平行于笛卡尔轴时才能计算 FiPC-NICS)。在步骤 (3) 中，直线可用两种方式指定：

- 手动指定两个端点的坐标。
- 输入一些原子的序号，将为它们拟合一个平面。然后分别指定相对这些原子的几何中心在平面上方和下方的距离。值得注意的是，如果恰当设置 Gaussian 模板文件，Multiwfn 能够绘制特定分子轨道贡献的 NICS

曲线，例如绘制 NICSσ,zz 和 NICSπ,zz 曲线。

例子见 4.25.13 节。

### 3.28.14 NICS-2D 扫描平面图 (NICS-2D scan plane map)

Multiwfn 能够轻松绘制非常漂亮的 NICS 平面图，需要以下步骤： (1) 启动 Multiwfn，然后载入一个包含待研究体系结构信息的文件

(2) 进入主功能 (main function) 25 的子功能 (subfunction) 14 (3) 定义绘图平面，设置与主功能 (main function) 4 完全相同 (4) 选择选项 (option) 1 以生成 Gaussian 程序的输入文件。你需要输入一个

Gaussian 模板文件的路径，该文件应对应于标准 NMR 任务，但坐标部分应替换为 [geometry]，见 examples\NICS_scan\template_NMR.gjf。例如。然后会在当前文件夹下生成 NICS_2D.gjf，你可以根据实际情况恰当修改关键词 (5) 手动用 Gaussian 运行 .gjf 文件 (6) 选择选项 (option) 2 并输入 Gaussian 输出文件的路径以载入它 (7) 选择感兴趣的 NICS 分量 (8) NICS 图会自动显示在屏幕上。关闭后，你可以在后处理菜单中调节绘图

设置并重新绘制。例子见 4.25.14 节。
