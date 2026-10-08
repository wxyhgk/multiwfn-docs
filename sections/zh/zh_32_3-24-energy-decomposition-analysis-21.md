# 能量分解分析 (21)

> Multiwfn manual, p.333–340.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.333 -->



得到。

要进行 amIGM 分析，你应提供记录分子动力学轨迹的多帧 .xyz 文件作为输入文件，然后进入主功能 20 (main function 20) 的子功能 -12 (subfunction -12)，然后像标准 mIGM/IGM 分析一样为 amIGM 分析定义片段，接着选择要考虑的帧范围，最后定义合适的计算格点数据的盒子。此后，将计算各种格点数据，并出现后处理菜单 (post-processing menu)。在该菜单中，你可将 𝛿𝑔̅inter 和平均 sign(λ2)ρ 的 cube 文件分别导出为 avgdg_inter.cub 和 avgsl2r.cub。有一个选项 (option) (-1) 可绘制这两个函数之间的散点图，这在 amIGM 分析中可能有用。你还可将平均 RDG（amIGM 分析的副产品）和 3.23.3 节提到的热涨落指数 (thermal fluctuation index，TFI) 导出为 cube 文件。

要绘制以平均 sign(λ2)ρ 着色的 𝛿𝑔̅inter 等值面图，你应将导出的 avgdg_inter.cub 和 avgsl2r.cub 以及 examples\aIGM.vmd 放到 VMD 文件夹，然后启动 VMD 并在 VMD 控制台窗口输入 source aIGM.vmd 命令以执行绘图脚本，你将立即看到 amIGM 图。

在后处理菜单 (post-processing menu) 中，你还可选择选项 (option) 8 以生成 𝛿𝑔inter 的标准差和 amIGM 的热涨落指数 (TFIamIGM) 的格点数据，其定义如下

$$\mathrm{TFI}^{\mathrm{amIGM}}(\mathbf{r})=\frac{s t d(\delta g^{\mathrm{inter}})(\mathbf{r})}{\delta g^{-\mathrm{inter}}(\mathbf{r})}$$

$$\mathrm{TFI}^{\mathrm{amIGM}}(\mathbf{r})=\frac{s t d(\delta g^{\mathrm{inter}})(\mathbf{r})}{\delta g^{-\mathrm{inter}}(\mathbf{r})}$$

其中 𝛿𝑔𝑖 inter 表示第 i 帧的 𝛿𝑔inter，N 表示所考虑帧的数目。通过以适当选择的颜色范围将 TFIamIGM 或 𝑠𝑡𝑑(𝛿𝑔inter) 映射到 𝛿𝑔̅inter 等值面上，可区分不同区域相互作用的稳定性。

amIGM 分析的例子见 4.20.13 节。

所需信息：多帧原子坐标


## 3.24 能量分解分析 (21)


### 3.24.1 基于分子力场的能量分解分析


### (EDA-FF)

能量分解分析 (energy decomposition analysis，EDA) 是揭示相互作用本质的重要方法。大多数 EDA 分析方法基于波函数，它们准确、严谨，结果有意义，但遗憾的是对大体系往往太昂贵。本模块专为基于经典分子力场 (force field，FF) 分析分子内和分子间弱相互作用而设计，该方法可称为 EDA-FF，计算

<!-- p.334 -->



代价对由数百原子组成的体系可忽略，甚至可应用于一万以上原子的体系。由于 FF 的限制，该模块显然不能用于讨论化学键相互作用的本质。本节中的“弱相互作用”一词指相隔三个以上化学键的原子间相互作用。

如果工作中使用了 EDA-FF 分析，请引用这篇文章，其中我简要描述了 EDA-FF 并用其研究了 cyclo[18]carbon 与石墨烯之间的相互作用：Mat. Sci. Eng. B, 273, 115425 (2021) DOI: 10.1016/j.mseb.2021.115425。

理论 有许多流行的分子体系 FF。弱相互作用的主要成分是范德华 (van der Waals，vdW) 相互作用和静电相互作用，大多数 FF 用成对势表示它们，如下所示。

·原子 A 和 B 之间的静电相互作用能（使用原子单位）：


$$E_{_{AB}}^{ele}=\frac{q_{_{A}}q_{_{B}}}{r_{_{AB}}}$$

<!-- formula-ocr: formula_p334_225.png 已替换为LaTeX, 原图保留备查 -->

其中 q 为原子电荷，rAB 为 A 与 B 之间的距离。

·原子 A 和 B 之间的 vdW 相互作用能：

EEE ABABAB disprepvdW +=

$$E_{_{AB}}^{\mathrm{vdW}}=E_{_{AB}}^{\mathrm{rep}}+E_{_{AB}}^{\mathrm{disp}}$$

其中 Erep 表示由 Pauli 排斥效应引起的排斥相互作用（也称为交换排斥），而 Edisp 为有吸引力的色散相互作用。εAB 是原子间 vdW 相互作用势的势阱深度，而 R0AB 为 vdW 非键距离。当 rAB=RAB0 时，相互作用能恰对应势阱深度。

参数 ε 和 R0 由 FF 提供，数值通常对每种原子类型定义。实际计算中使用的原子间参数通常按原子参数的几何平均或算术平均求得。例如，在 UFF 力场中，使用如下混合规则


$$E_{_{AB}}^{\mathrm{vdW}}=E_{_{AB}}^{\mathrm{rep}}+E_{_{AB}}^{\mathrm{disp}}$$

<!-- formula-ocr: formula_p334_226.png 已替换为LaTeX, 原图保留备查 -->

而对于 AMBER 和 GAFF 等其他 FF，定义了原子 ε 和 R*，所用混合规则为


$$E_{AB}^{\mathrm{rep}}=\varepsilon_{AB}\left(\frac{R_{AB}^{0}}{r_{AB}}\right)^{12}\quad E_{AB}^{\mathrm{disp}}=-2\varepsilon_{AB}\left(\frac{R_{AB}^{0}}{r_{AB}}\right)^{6}$$

<!-- formula-ocr: formula_p334_227.png 已替换为LaTeX, 原图保留备查 -->

其中 R* 称为原子非键半径或原子 vdW 半径。

给定原子间相互作用项，计算片段间相互作用能的各种物理分量很直接：


$$E_{IJ}^{\mathrm{ele}}=\sum_{A\in I}\sum_{B\in J}E_{AB}^{\mathrm{ele}}\qquad E_{IJ}^{\mathrm{rep}}=\sum_{A\in I}\sum_{B\in J}E_{AB}^{\mathrm{rep}}\qquad E_{IJ}^{\mathrm{disp}}=\sum_{A\in I}\sum_{B\in J}E_{AB}^{\mathrm{disp}}$$

<!-- formula-ocr: formula_p334_228.png 已替换为LaTeX, 原图保留备查 -->

本模块主要用于计算两个或多个用户定义片段之间的上述三项，同时可得到许多有用的量。

用法 使用本模块的基本步骤为：


<!-- p.335 -->



(1) 准备一个“分子列表”文件，其中包含“分子类型”文件的路径。详细描述见后。

(2) 载入含有整个体系几何信息的文件。显然，Multiwfn 支持的许多格式都可使用，例如 .xyz、.mol、.pdb、.fch 等等。

(3) 进入主功能 21 (main function 21) 的子功能 1 (subfunction 1)。(4) 用选项 (option) 3 载入分子列表文件。该步用于为每个原子指认原子电荷和类型。

(5) 用选项 (option) 2 定义片段。可定义无限多个片段，任何原子不应同时出现在两个或更多片段中。如果你想研究同一分子中两个片段之间的相互作用，这两个片段之间的任何原子对应相隔至少三个化学键（否则该相互作用将不再属于弱相互作用范畴）。注意步骤 (4) 和 (5) 的顺序可以互换。

(6) 选择选项 (option) 1 开始分析，然后每对片段之间的相互作用能分量以及原子贡献将被打印。分析前，如果你想检查电荷和类型是否已正确指认，可以选择选项 (option) 4。

计算前还有其他可选择的选项：·选项 (option) -1：用于选择计算中所用 FF。目前支持 AMBER99 & GAFF（默认）和 UFF，它们的区别在于计算中使用的内置原子 vdW 参数和混合规则不同。

·选项 (option) -2：该选项可选择计算静电相互作用时的算符。默认采用 1/r 算符，而用该选项可将其改为 1/r2。显然，基于 1/r2 计算的 Eele 随相互作用距离 r 的衰减比默认情形快得多，这就是一些研究采用这种简单策略以有效体现水环境的原因，因为众所周知水等极性溶剂由于其大介电常数可显著屏蔽静电相互作用强度。

·选项 (option) -3：如果你选择该选项一次以将状态切换为 "Yes"，则计算后，所有原子间相互作用能项包括其物理分量将被导出到当前文件夹的 interatm.txt 中。

·选项 (option) -4：在标准 .pqr 格式中，最后两列专用于存储原子 vdW 半径和原子电荷。如果你选择该选项一次以将状态切换为 "Yes"，则计算期间，atmint_tot.pqr、atmint_ele.pqr、atmint_rep.pqr、atmint_disp.pqr 和 atmint_vdW.pqr 将输出到当前文件夹，它们的最后一列分别记录原子对总、静电、排斥、色散和 vdW（即排斥 + 色散）相互作用能的贡献。在流行的 VMD 可视化程序中，你可以载入其中一个 .pqr 文件并按“原子电荷”数据给原子着色，则原子颜色将生动展示每个原子对相应种类相互作用能的贡献。

接下来，我介绍分子列表文件的书写规则。文件内容应如下所示：


```text
C:\mol1\phenol.txt 1
C:\mol2\H2O.txt 4
C:\HCl.txt 2
```

该示例文件意味着，在 Multiwfn 启动时载入的文件所记录的几何信息中，记录顺序为：一个 phenol 分子、四个 H2O 分子和两个 HCl 分子。这三个 .txt 文件含有相应分子的原子类型（区分大小写）和电荷。例如，下面是 C:\mol2\H2O.txt 的内容，记录了 H2O 分子中原子的信息，OW 和 HW 是 AMBER 力场的原子类型。


<!-- p.336 -->



Multiwfn 启动时载入的几何信息中，记录顺序为：一个 phenol 分子、四个 H2O 分子和两个 HCl 分子。这三个 .txt 文件含有相应分子的原子类型（区分大小写）和电荷。例如，下面是 C:\mol2\H2O.txt 的内容，记录了 H2O 分子中原子的信息，OW 和 HW 是 AMBER 力场的原子类型。


```text
OW -0.728713
HW  0.364427
HW  0.364286
```

第一列是对应于当前所选 FF 的原子类型，第二列对应原子电荷。注意该文件中的原子顺序必须与 Multiwfn 启动时载入的几何信息完全一致。如果分析中所用力场为 UFF，则该文件应只含原子电荷，因而应只有一列（因为对每种元素，所有相关原子类型共用相同的 UFF vdW 参数，因此用户无需定义原子类型）。

·关于原子类型：原子类型的详细描述可在相应力场的原始论文中找到。对于 AMBER，见 J. Am. Chem. Soc., 117, 5179 (1995) 的 Table 1。对于 GAFF，见 J. Comput. Chem., 25, 1157 (2004) 的 Table 1；你也可查阅 "examples\EDA\EDA_FF" 文件夹中的 AMBER99.txt 和 GAFF.txt 以了解原子类型描述。一般而言，你可根据当前体系中每个原子的实际化学环境手动找到合适的原子类型。然而，如果你觉得此过程麻烦，可用第三方程序帮助你识别原子类型并构建分子文件。例如，GaussView 可自动指认 AMBER 原子类型（进入 "Atom List"，点击带有大橙色 "M" 符号的图标，双击 "AMBER Type" 列头，选择 "File"-"Export Data"，然后提取对应 "AMBER Type" 列的数据），而 AmberTools 包中的 Antechamber 工具能够指认 GAFF 原子类型。注意 AMBER 和 GAFF 原子类型可在同一分子文件中混用，因为这两个力场彼此完全兼容，AMBER 和 GAFF 原子类型分别用大写和小写。

注：GaussView 指认的原子类型总是大写，然而，AMBER99 的某些原子类型为小写，如 Br。显然，你应在将文件载入 Multiwfn 前手动修改。如果你感到困惑，看看 examples\EDA\EDA_FF\AMBER99.txt。

·关于力场选择：对于有机类体系，通常我建议用 AMBER/GAFF 力场进行分析，结果应合理且有化学意义。事实上，由于 GAFF 的 vdW 参数直接继承自 AMBER，通常用 GAFF 和 AMBER 原子类型应无区别。显然，分析中所用几何应首先在合理水平下优化。不推荐用 UFF，因为我发现用 UFF 时，即使几何已用合适的量子化学方法充分优化，片段间总相互作用能通常为正，这是由于高估了 Erep。解决该问题的一种方法是用 UFF 自身优化的几何（许多程序可做到，如 Gaussian 和 OpenBabel），然而所得弱相互作用分子二聚体或多聚体的几何往往不太好。UFF 的独特优点是它几乎覆盖整个周期表。考虑到这点，我在 Multiwfn 中设计了一个技巧：如果你用 AMBER/GAFF，当原子类型写为 UF 时，将采用 UFF vdW 参数。该处理大大扩展了 AMBER 和 GAFF 的适用范围。


<!-- p.337 -->



·关于原子电荷选择：用于能量分解分析的原子电荷应能很好地再现分子 vdW 面周围的静电势 (electrostatic potential，ESP)。通常我建议用 CHELPG 原子电荷，它通过 ESP 拟合过程得到，可直接经 Multiwfn 计算，介绍见 3.9.10 节，例子见 4.7.1 节。注意若某类分子在当前体系中出现多次且构象显著不同，鉴于各单体的 ESP 拟合电荷可能彼此很不同，建议将这些复本视为不同种类的分子，以便分别指认原子电荷。若体系中某些单体太大而无法计算其 ESP 拟合原子电荷，你可改用 EEM 原子电荷，使用为再现 ESP 拟合电荷而拟合的参数，介绍见 3.9.15 节。EEM 电荷的计算代价对由数百原子组成的体系可忽略，因为计算完全基于分子几何信息和经验参数。

本模块的例子见 4.21.1 节。所需信息：原子坐标和含有原子电荷/类型的特殊文件


### 3.24.2 Shubin Liu 的能量分解

理论 在 J. Chem. Phys., 126, 244103 (2007) 中，作者 Shubin Liu 提出了一种能量分解思想，下文称为 EDA-SBL。在该方法中，总分子能量分解为

stericelectrostaticquantumEEEE=++

空间位阻项简单地是由 Weizsäcker 动能泛函得到的能量，对应于假设当前体系中电子为无相互作用玻色子时的精确动能：


$$E_{\mathrm{s t e r i c}}=T_{\mathrm{W}}=\left|\nabla\rho(\mathbf{r})\right|^{2}/\left[8\rho(\mathbf{r})\right]$$

<!-- formula-ocr: formula_p337_229.png 已替换为LaTeX, 原图保留备查 -->

静电项是体系中粒子所有经典 Coulomb 相互作用之和：

$$E_{\mathrm{e l e c t r o s t a t i c}}=E_{\mathrm{J}}+E_{\mathrm{N-E}}+E_{\mathrm{N-N}}=\iint\frac{\rho(\mathbf{r}_{1})\rho(\mathbf{r}_{2})}{r_{12}}\mathrm{d}\mathbf{r}_{1}\mathrm{d}\mathbf{r}_{2}-\int\rho(\mathbf{r})\sum_{A}\frac{Z_{A}}{|\mathbf{r}-\mathbf{R}_{A}|}\mathrm{d}\mathbf{r}+\sum_{A>B}\frac{Z_{A}Z_{B}}{R_{AB}}$$

最后，量子项是纯由量子效应引起的能量：

quantumPauliXCEEE=+

其中 EXC 为交换相关能，EPauli=TS-TW 为 Pauli 动能，其中 TS 表示无相互作用电子模型的总动能，可计算为所有占据分子轨道动能之和。Equantum 本质上体现了电子相关效应以及在无相互作用粒子假设下 Pauli 不相容原理对电子动能的影响。


<!-- p.338 -->



EDA-SBL 方法已在许多研究论文中使用，如下所示的论文，若你想了解该方法如何用于研究实际化学问题，建议阅读：J. Phys. Chem. A, 117, 962 (2013)，J. Chem. Phys., 133, 114110 (2010)，Phys. Chem. Chem. Phys., 17, 27052 (2015)，J. Phys. Chem. A, 119, 8216 (2015)，Chem. Phys. Lett., 687, 131 (2017)。

用法 Multiwfn 自身无法计算 EDA-SBL 方法中的所有项，Multiwfn 需要从 Gaussian 输出文件中读取相关信息。用 Gaussian 进行 EDA-SBL 分析的方法总结如下：

(1) 基于优化好的几何手动创建单点任务的特殊 Gaussian 输入文件

(2) 用 Gaussian 运行该输入文件，得到输出文件以及 fch/fchk 文件 (3) 启动 Multiwfn 并载入 fch/fchk 文件，然后进入主功能 21 (main function 21) 的子功能 2 (subfunction 2) (4) 输入 Gaussian 输出文件的路径 然后 Multiwfn 计算 Esteric 项，并打印 EDA-SBL 方法定义的所有三个能量分量。EDA-SBL 项中涉及的其他中间项也同时给出，如 Pauli 动能、核-电子 Coulomb 吸引能等等。

特殊 Gaussian 输入文件应符合如下格式，几何已用合适水平优化。


```text
%chk=H2O.chk
## B3LYP/6-31G* ExtraLinks=L608

Optimized water

0 1
O 0.00000000     0.00000000     0.11930801
H 0.00000000     0.75895306    -0.47723204
H 0.00000000    -0.75895306    -0.47723204

-5
```

DFT 泛函和基组可任意选择，必须指定 "ExtraLinks=L608" 以便 Gaussian 可将总能量分解为各种分量并打印到输出文件。计算后，所得 H2O.chk  usformchk 工具转换为 fch/fchk 文件。如你所见，输入文件末尾有一个值 "-5"，该值应根据你实际使用的 DFT 泛函指定，你可查阅 Gaussian IOp 参考中的 IOp(3/74) 找到对应值。常用杂化泛函的值为：

-73 (MN15) -58 (ωB97XD)、-55 (M06-2X)、-54 (M06)、-53 (M06L)、-40 (CAM-B3LYP)、-35 (TPSSh)、-13 (PBE0)、-5 (B3LYP)、-6 (B3PW91)、-3 (BHandHLYP)、402 (BLYP)、1009 (PBE)、2523 (TPSS)。

寻找当前 DFT 泛函对应 IOp(3/74) 值的另一种方法是做一个简单计算并查看输出文件开头自动显示的 IOp(3/74) 值，例如，用 B3LYP/6-31G* 水平的输出文件将含一行 "3/5=1,6=6,7=1,11=2,16=1,25=1,30=1,


<!-- p.339 -->



74=-5/1,2,3;"，显示 IOp(3/74) 为 -5。关于 ExtraLinks=L608 的更多解释可在 http://gaussian.com/faq1/ 找到。

对版本 ≤ G16 C.01 的 Gaussian 的重要注记：据 Gaussian 官方支持的回复，至少对 G16 C.01 或更老版本，ωB97XD 和 CAM-B3LYP 等长程校正泛函与 ExtraLinks=L608 不兼容。此外，为一致起见，如果你用 G16，还应在泛函序号后加值 "5" 以要求 Gaussian 对 ExtraLinks=L608 用“ultrafine”格点，因为自 G16 起“ultrafine”为默认 DFT 格点。例如，若需用 M06-2X，应写 -55 5 而非简单写 55。

EDA-SBL 分析的实际例子见 4.21.2 节。


### 3.24.3 SobEDA 与 sobEDAw 能量分解分析

基于色散校正密度泛函理论定义的 sobEDA 与 sobEDAw 能量分解分析非常稳健、高效、通用且易用，因此高度推荐使用！它们可用基于 Gaussian 和 Multiwfn 的 sobEDA.sh shell 脚本轻松进行。关于理论背景和示例应用的介绍请查看原始论文 J. Phys. Chem. A, 127, 7023 (2023)，非常详细的教程见 http://sobereva.com/soft/sobEDA_tutorial.zip。我的博客文章“Using sobEDA and sobEDAw methods to perform very accurate, fast, convenient and universal energy decomposition analysis”（http://sobereva.com/685，中文）含有额外讨论。


### 3.24.4 原子对色散能贡献的分析

理论 对 B3LYP 等描述色散相互作用能力为零的 DFT 泛函，著名的 DFT-D3 色散校正能可近似视为色散能。这点已在 J. Phys. Chem. A, 127, 7023 (2023) 中提出，并在 J. Chem. Theory Comput., 20, 1923 (2024) 中通过与 DLPNO-CCSD(T) 计算的色散能比较得到进一步确认。不考虑三体耦合项时，DFT-D3 的总色散校正能为每对原子间色散相互作用能之和。因此，原子 A 对体系色散能的贡献可

计算为 𝜀𝐴= (1/2) ∑𝜀𝐴,𝐵𝐵≠𝐴，其中 𝜀𝐴,𝐵 为原子 A 与 B 之间的 DFT-D3 色散校正能。片段对色散能的贡献简单地为其原子的贡献之和。两片段之间的色散相互作用能等于它们之间每对原子间色散相互作用能之和。

此外，J. Chem. Theory Comput., 20, 1923 (2024) 提出了色散能密度的思想，其定义为


$$\rho_{\mathrm{d i s p}}(\mathbf{r})=\left(\frac{\pi}{\alpha}\right)^{-3/2}\sum_{A}\varepsilon_{A}e^{-\alpha(\mathbf{r}-\mathbf{R}_{A})^{2}}$$

<!-- formula-ocr: formula_p339_230.png 已替换为LaTeX, 原图保留备查 -->

其中 α 通常取 0.5，RA 为原子 A 的坐标。本质上，𝜌disp 将原子对色散能的贡献展宽为 Gauss 函数以得到实空间函数，可图形展示。

某原子 A 在不同化学环境（如结构 m 和 n）中所贡献色散能之差记为 ∆𝜀𝐴。将上式中的 𝜀𝐴 替换为 ∆𝜀𝐴 即得 ∆𝜌disp 函数。若计算 ∆𝜌disp 所用核坐标对应结构 m，则 ∆𝜌disp 可用于给结构 m 的原子着色，或绘制

<!-- p.340 -->



为等值面并附加到结构图上，以突出对色散能变化贡献最大的区域。

上述信息对其他类型色散校正方案同样成立，如 DFT-D4，然而 Multiwfn 目前仅支持基于 DFT-D3 进行该分析。

功能 本模块中所有数据均基于以 B3LYP 拟合参数的 DFT-D3(BJ) 色散校正能计算。支持周期体系。

本模块的功能如下
- 计算当前体系原子对色散能的贡献：每个原子的值显示在屏幕上，并可导出名为 atomdisp.pqr 的文件，其中“charge”属性（文件中倒数第三列）对应原子对色散能的贡献。若将该文件载入 VMD 程序，可按“charge”属性给原子着色以直观展示原子贡献。

- 计算当前体系的色散密度：将被要求定义格点设置，然后计算色散密度的格点数据，接着可导出为当前文件夹中的 dispdens.cub。此后，你可用如 VMD 和 VESTA 载入并绘制色散密度的等值面。

- 计算当前体系与另一体系之间原子对色散能贡献之差：将被要求为当前体系定义片段（体系 A 的片段 i），然后被要求输入另一体系的文件路径并为其定义片段（体系 B 的片段 j）。两体系不一定对应同一体系，但两片段必须有相同原子数和相同原子顺序。此后，Multiwfn 将依次打印体系 B 的总色散能然后是体系 A 的总色散能。然后打印片段 i 中原子对体系 A 色散能的贡献与片段 j 中原子对体系 B 色散能的贡献之差，并可导出 diffatomdisp.pqr，其“charge”属性对应此差值。

- 计算当前体系与另一体系之间的色散密度差。与上一功能类似，但计算 ∆𝜌disp 的格点数据并导出为当前文件夹中的 dispdensdiff.cub。

- 计算片段对色散能的贡献
- 计算两片段之间的色散相互作用能

用法 本模块对应主功能 21 (main function 21) 的子功能 4 (subfunction 4)。输入文件必须含原子信息，如 xyz、pdb、mol2、gjf、fch、mwfn，全面介绍见 2.5 节。若输入文件含晶胞信息，则计算视为周期性。

该功能需要 Tian Lu 修改的 Grimme's dftd3 程序，可在 http://sobereva.com/soft/dftd3_TLmod.zip 下载，内含修改的源代码、预编译 Windows 版可执行文件 (dftd3.exe)、预编译 Linux 版可执行文件 (dftd3)。在启动 Multiwfn 前应将 `settings.ini` 中的“dftd3path”设为 dftd3 可执行文件的实际路径，以便 Multiwfn 可调用 dftd3。在 Linux 环境下，别忘了用“chmod”为 dftd3 添加可执行权限。
