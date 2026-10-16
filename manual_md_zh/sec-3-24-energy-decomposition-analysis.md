# **3.24 能量分解分析 (21)**

## **3.24.1 基于分子力场 (force field, FF) 的能量分解分析 (EDA-FF)**

能量分解分析 (energy decomposition analysis, EDA) 是揭示相互作用本质的重要方法。大多数 EDA 分析方法基于波函数，它们准确、严谨，结果有意义，但遗憾的是对于大体系往往过于昂贵。本模块用于基于经典分子力场 (force field, FF) 分析分子内和分子间弱相互作用 (weak interaction)，该方法可称为 EDA-FF，对于由数百个原子组成的体系计算代价可以忽略，甚至可用于一万个原子以上的体系。由于力场的局限，本模块显然不能用于讨论化学键相互作用的本质。本节中的“弱相互作用”一词指相隔三个以上化学键的原子间相互作用。

若在工作中使用了 EDA-FF 分析，请引用本文，我在其中简要描述了 EDA-FF 并将其用于研究环[18]碳与石墨烯之间的相互作用：*Mat. Sci. Eng. B*, **273**, 115425 (2021) DOI: [10.1016/j.mseb.2021.115425](https://doi.org/10.1016/j.mseb.2021.115425)。

### **理论**

分子体系有许多流行的力场。弱相互作用的主要成分是范德华 (van der Waals, vdW) 相互作用和静电相互作用，大多数力场用对势表示它们，如下所示。

- 原子 *A* 与 *B* 之间的静电相互作用能（采用原子单位）：

  
$$
E_{AB}^{\mathrm{ele}}=\frac{q_{A}q_{B}}{r_{AB}}
$$

  其中 $q$ 为原子电荷，$r_{\mathrm{AB}}$ 为 *A* 与 *B* 之间的距离。

- 原子 *A* 与 *B* 之间的 vdW 相互作用能：

  
$$
\begin{gathered}E_{AB}^{\mathrm{vdW}}=E_{AB}^{\mathrm{rep}}+E_{AB}^{\mathrm{disp}}\\ E_{AB}^{\mathrm{rep}}=\varepsilon_{AB}\left(\frac{R_{AB}^{0}}{r_{AB}}\right)^{12}\qquad E_{AB}^{\mathrm{disp}}=-2\varepsilon_{AB}\left(\frac{R_{AB}^{0}}{r_{AB}}\right)^{6}\end{gathered}
$$

  其中 $E^{\mathrm{rep}}$ 表示由 Pauli 排斥效应引起的排斥相互作用（亦称交换排斥 (exchange-repulsion)），而 $E^{\mathrm{disp}}$ 为有吸引力的色散相互作用。$ε_{AB}$ 为原子间 vdW 相互作用势的势阱深度，而 $R^0$ *$_{AB}$* 为 vdW 非键距离。当 $r$ *$_{AB}$*= $R$ *$_{AB}$*⁰ 时，相互作用能恰好对应势阱深度。

  参数 *ε* 与 $R^0$ 由力场提供，其取值通常对每种原子类型定义。实际计算中使用的原子间参数通常取原子参数的几何平均或算术平均。例如，UFF 力场使用如下混合规则

  
$$
\varepsilon_{AB}=\sqrt{\varepsilon_{A}\varepsilon_{B}}\qquad R_{AB}^{0}=\sqrt{R_{A}^{0}R_{B}^{0}}
$$

  而对于 AMBER、GAFF 等其他力场，定义的是原子的 *ε* 与 $R^{*}$，所用混合规则为

  
$$
\varepsilon_{AB}=\sqrt{\varepsilon_{A}\varepsilon_{B}}\qquad R_{AB}^{0}=R_{A}^{*}+R_{B}^{*}
$$

  其中 $R^{*}$ 称为原子非键半径或原子 vdW 半径。

给定原子间相互作用项后，计算片段间相互作用能的各物理分量是直接的：

$$
E_{IJ}^{\mathrm{ele}}=\sum_{A\in I}\sum_{B\in J}E_{AB}^{\mathrm{ele}}\qquad E_{IJ}^{\mathrm{rep}}=\sum_{A\in I}\sum_{B\in J}E_{AB}^{\mathrm{rep}}\qquad E_{IJ}^{\mathrm{disp}}=\sum_{A\in I}\sum_{B\in J}E_{AB}^{\mathrm{disp}}
$$

本模块主要用于计算两个或多个用户定义片段之间的上述三项，还可同时得到许多有用的量。

### **用法**

使用本模块的基本步骤为：

- (1) 准备一个“分子列表”文件，其中包含“分子类型”文件的路径。详细描述见后。

- (2) 载入一个包含整个体系几何信息的文件。显然，Multiwfn 支持的许多格式都可使用，例如 .xyz、.mol、.pdb、.fch 等。

- (3) 进入主功能 21 的子功能 1。

- (4) 用选项 3 载入分子列表文件。该步骤用于为每个原子指派原子电荷和类型。

- (5) 用选项 2 定义片段。可定义任意多个片段，任何原子不得同时出现在两个或多个片段中。若要研究同一分子中两个片段之间的相互作用，两片段之间的任何原子对应相隔至少三个化学键（否则相互作用将不再属于弱相互作用的范畴）。注意步骤 (4) 和 (5) 的顺序可以交换。

- (6) 选择选项 1 开始分析，然后将打印每对片段之间的相互作用能分量以及原子贡献。在分析之前，若想检查电荷和类型是否已正确指派，可选择选项 4。

在计算之前还可选择其他选项：

- 选项 -1：用于选择计算中采用的力场。目前支持 AMBER99 & GAFF（默认）和 UFF，区别在于内置的原子 vdW 参数和计算中使用的混合规则不同。

- 选项 -2：可选择计算静电相互作用时的算符。默认采用 1/ $r$ 算符，使用该选项可将其改为 1/ $r^2$。显然，基于 1/ $r^2$ 计算的 $E^{\mathrm{ele}}$ 随相互作用距离 $r$ 的衰减比默认情形快得多，这也是一些研究采用这一简单策略来有效体现水环境的原因，因为众所周知，水等极性溶剂介电常数很大，可显著屏蔽静电相互作用强度。

- 选项 -3：若选择一次将状态切换为“Yes”，则计算结束后所有原子间相互作用能项及其物理分量将导出到当前文件夹的 *interatm.txt* 中。

- 选项 -4：在标准 .pqr 格式中，最后两列专门用于存储原子 vdW 半径和原子电荷。若选择一次将状态切换为“Yes”，则计算过程中将在当前文件夹输出 *atmint_tot.pqr*、*atmint_ele.pqr*、*atmint_rep.pqr*、*atmint_disp.pqr* 和 *atmint_vdW.pqr*，其最后一列分别记录原子对总、静电、排斥、色散和 vdW（*即*排斥 + 色散）相互作用能的贡献。在流行的 VMD 可视化程序中，可载入其中一个 .pqr 文件并按“原子电荷”数据对原子着色，原子颜色将生动展示每个原子对相应相互作用能的贡献。

下面介绍分子列表文件的书写规则。文件内容应如下所示：

```text
C:\mol1\phenol.txt 1
C:\mol2\H2O.txt 4
C:\HCl.txt 2
```

该示例文件表明，在 Multiwfn 启动时载入的文件所提供的几何信息中，记录顺序为：一个苯酚分子、四个 H₂O 分子和两个 HCl 分子。三个 .txt 文件包含相应分子的原子类型（区分大小写）和电荷。例如，下面是 *C:\mol2\H2O.txt* 的内容，记录 H₂O 分子中原子的信息，OW 和 HW 为 AMBER 力场的原子类型。

```text
OW -0.728713
HW  0.364427
HW  0.364286
```

第一列是与当前所选力场对应的原子类型，第二列对应原子电荷。注意该文件中的原子顺序必须与 Multiwfn 启动时载入的几何信息完全一致。若分析采用的力场为 UFF，则该文件只需包含原子电荷，即只有一列（因为对每种元素，所有相关原子类型共用相同的 UFF vdW 参数，用户无需定义原子类型）。

- **关于原子类型**：原子类型的详细描述见相应力场的原始论文。AMBER 见 *J. Am. Chem. Soc.*, **117**, 5179 (1995) 表 1；GAFF 见 *J. Comput. Chem.*, **25**, 1157 (2004) 表 1；也可查阅 "examples\EDA\EDA_FF" 文件夹中的 *AMBER99.txt* 和 *GAFF.txt* 了解原子类型的描述。一般可根据各原子在当前体系中的实际化学环境手动确定合适的原子类型。若觉得此过程麻烦，可借助第三方程序帮助指认原子类型并构建分子文件。例如，GaussView 可自动指派 AMBER 原子类型（进入 "Atom List"，点击带大橙色 "M" 标志的图标，双击 "AMBER Type" 列的表头，选择 "File"-"Export Data"，再提取 "AMBER Type" 列对应的数据），而 AmberTools 包中的 Antechamber 工具可指派 GAFF 原子类型。注意 AMBER 与 GAFF 原子类型可在同一分子文件中混用，因为这两种力场完全兼容，AMBER 与 GAFF 原子类型分别使用大写和小写。

  > **注**
  >
  > GaussView 指派的原子类型恒为大写，但 AMBER99 的某些原子类型为小写，*如* Br。显然，在载入 Multiwfn 之前应手动修改。若有困惑，可查看 *examples\EDA\EDA_FF\AMBER99.txt*。

- **力场的选择**：对于有机体系，通常建议使用 AMBER/GAFF 力场进行分析，结果应合理且有化学意义。事实上，由于 GAFF 的 vdW 参数直接继承自 AMBER，使用 GAFF 与 AMBER 原子类型通常没有差别。显然，分析所用几何应先在合理水平下优化。一般不建议使用 UFF，因为我发现采用 UFF 时，即使几何已用合适的量子化学方法充分优化，片段间总相互作用能通常也为正，这是由于高估了 $E^{\mathrm{rep}}$。解决该问题的一种办法是使用 UFF 本身优化的几何（Gaussian、OpenBabel 等许多程序都可做到），但弱相互作用分子二聚体或多聚体的所得几何往往不太好。UFF 的独特优势在于几乎覆盖整个周期表。考虑到这一点，我在 Multiwfn 中设计了一个技巧：若使用 AMBER/GAFF，当原子类型写作 *UF* 时将采用 UFF vdW 参数。该处理极大地扩展了 AMBER 与 GAFF 的适用范围。

- **原子电荷的选择**：能量分解分析所用原子电荷应能很好地复现分子 vdW 表面周围的静电势 (ESP)。通常建议使用 CHELPG 原子电荷，它通过 ESP 拟合得到，可直接用 Multiwfn 计算，介绍见[3.9.10 节](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3910-chelpg-charges-from-electrostatic-potentials-using-a-grid-based-method-esp-拟合原子电荷-12)，例子见[4.7.1 节](sec-4-7-population-analysis-and-atomic-charge-calculation.md#471-计算三氟化氯的hirshfeld和chelpg原子电荷以及片段电荷)。注意若某类分子在当前体系中出现多次且构象显著不同，鉴于各单体的 ESP 拟合电荷可能彼此相差很大，建议将这些重复体视为不同种类的分子，以便分别指派原子电荷。若体系中某些单体太大而无法计算其 ESP 拟合原子电荷，可改用 EEM 原子电荷，其参数为复现 ESP 拟合电荷而拟合，介绍见[3.9.15 节](sec-3-9-population-analysis-and-calculation-of-atomic-charges.md#3915-电负性均衡方法-eem-原子电荷-17)。EEM 电荷的计算代价对于由数百个原子组成的体系可以忽略，因为计算完全基于分子几何信息和经验参数。

本模块的例子见[4.21.1 节](sec-4-21-energy-decomposition-analysis.md#4211-基于力场的能量分解分析-eda-ff示例)。

> **所需信息**
>
> 原子坐标及含原子电荷/类型的特殊文件

## **3.24.2 Shubin Liu 能量分解**

### **理论**

在 *J. Chem. Phys.*, **126**, 244103 (2007) 中，作者 Shubin Liu 提出了能量分解的思想，下文称之为 EDA-SBL。该方法中，分子总能量分解为

$$
E=E_{\mathrm{steric}}+E_{\mathrm{electrostatic}}+E_{\mathrm{quantum}}
$$

空间位阻项即由 Weizsäcker 动能泛函导出的能量，对应当前体系中电子为无相互作用玻色子假设下的精确动能：

$$
E_{\mathrm{steric}}=T_{\mathrm{W}}=\left|\nabla\rho(\mathbf{r})\right|^{2}/\left[8\rho(\mathbf{r})\right]
$$

静电项为体系中粒子间所有经典库仑相互作用之和：

$$
E_{\mathrm{electrostatic}}=E_{\mathrm{J}}+E_{\mathrm{N-E}}+E_{\mathrm{N-N}}=\int\int\frac{\rho(\mathbf{r}_{1})\rho(\mathbf{r}_{2})}{r_{12}}\mathrm{d}\mathbf{r}_{1}\mathrm{d}\mathbf{r}_{2}-\int\rho(\mathbf{r})\sum_{A}\frac{Z_{A}}{\left|\mathbf{r}-\mathbf{R}_{A}\right|}\mathrm{d}\mathbf{r}+\sum_{A>B}\frac{Z_{A}Z_{B}}{R_{AB}}
$$

最后，量子项为纯粹由量子效应引起的能量：

$$
E_{\mathrm{quantum}}=E_{\mathrm{Pauli}}+E_{\mathrm{XC}}
$$

其中 $E_{\mathrm{XC}}$ 为交换相关能，$E_{\mathrm{Pauli}}=T_{\mathrm{S}}-T_{\mathrm{W}}$ 为 Pauli 动能，其中 $T_{\mathrm{S}}$ 表示无相互作用电子模型的总动能，可计算为所有占据分子轨道动能之和。$E_{\mathrm{quantum}}$ 本质上体现电子相关效应以及无相互作用粒子假设下 Pauli 不相容原理对电子动能的影响。

EDA-SBL 方法已用于许多研究论文，如下所列，若想了解该方法如何用于研究实际化学问题，建议阅读：*J. Phys. Chem. A*, **117**, 962 (2013)，*J. Chem. Phys.*, **133**, 114110 (2010)，*Phys. Chem. Chem. Phys.*, **17**, 27052 (2015)，*J. Phys. Chem. A*, **119**, 8216 (2015)，*Chem. Phys. Lett.*, **687**, 131 (2017)。

### **用法**

Multiwfn 自身无法计算 EDA-SBL 方法中的所有项，Multiwfn 需从 Gaussian 输出文件中读取相关信息。用 Gaussian 进行 EDA-SBL 分析的方法总结如下：

- (1) 基于优化好的几何手动创建单点任务的特殊 Gaussian 输入文件

- (2) 用 Gaussian 运行该输入文件，得到输出文件以及 fch/fchk 文件

- (3) 启动 Multiwfn 并载入 fch/fchk 文件，然后进入主功能 21 的子功能 2

- (4) 输入 Gaussian 输出文件的路径

然后 Multiwfn 计算 $E_{\mathrm{steric}}$ 项，并打印 EDA-SBL 方法定义的全部三个能量分量。同时还给出 EDA-SBL 各项涉及的其他中间项，如 Pauli 动能、核-电子库仑吸引能等。

特殊 Gaussian 输入文件应符合如下格式，几何已用合适水平优化。

```text
%chk=H2O.chk
# B3LYP/6-31G* ExtraLinks=L608

Optimized water

0 1
O 0.00000000     0.00000000     0.11930801
H 0.00000000     0.75895306    -0.47723204
H 0.00000000    -0.75895306    -0.47723204

-5
　
　
```

DFT 泛函和基组可任意选择，必须指定 "ExtraLinks=L608"，以便 Gaussian 将总能量分解为各分量并打印到输出文件。计算后，所得 *H2O.chk* 应用 formchk 工具转换为 fch/fchk 文件。如所见，输入文件末尾有一个值 "-5"，该值应根据实际使用的 DFT 泛函指定，可查阅 Gaussian IOp 手册中的 IOp(3/74) 找到对应值。常用杂化泛函的值为：-73 (MN15)、-58 (ωB97XD)、-55 (M06-2X)、-54 (M06)、-53 (M06L)、-40 (CAM-B3LYP)、-35 (TPSSh)、-13 (PBE0)、-5 (B3LYP)、-6 (B3PW91)、-3 (BHandHLYP)、402 (BLYP)、1009 (PBE)、2523 (TPSS)。

> **注**
>
> 找到当前 DFT 泛函对应的 IOp(3/74) 值的另一办法是做一个简单计算，查看输出文件开头自动显示的 IOp(3/74) 值，例如，使用 B3LYP/6-31G\* 水平的输出文件将包含一行 "3/5=1,6=6,7=1,11=2,16=1,25=1,30=1, 74=-5/1,2,3;"，表明 IOp(3/74) 为 -5。关于 ExtraLinks=L608 的更多说明见 <http://gaussian.com/faq1/>。
>
> 对版本 ≤ G16 C.01 的 Gaussian 的重要提示：据 Gaussian 官方支持的回复，至少对于 G16 C.01 或更早版本，ωB97XD、CAM-B3LYP 等长程校正泛函与 ExtraLinks=L608 不兼容。另外，为一致起见，若使用 G16，还应在泛函序号后加值 "5"，要求 Gaussian 对 ExtraLinks=L608 使用“ultrafine”格点，因为自 G16 起“ultrafine”为默认 DFT 格点。例如，若需使用 M06-2X，应写 *-55 5* 而非简单写 *55*。

EDA-SBL 分析的实例见[4.21.2 节](sec-4-21-energy-decomposition-analysis.md#4212-乙烷旋转位垒的-shubin-liu-能量分解分析)。

## **3.24.3 SobEDA 与 sobEDAw 能量分解分析**

基于色散校正密度泛函理论定义的 sobEDA 与 sobEDAw 能量分解分析非常稳健、高效、通用且易用，因此**强烈推荐使用**！它们可用基于 Gaussian 和 Multiwfn 的 *sobEDA.sh* 脚本轻松进行。理论背景和示例应用的介绍请查阅原始论文 *J. Phys. Chem. A*, **127**, 7023 (2023)，另有非常详细的教程：<http://sobereva.com/soft/sobEDA_tutorial.zip>。我的博客文章“Using sobEDA and sobEDAw methods to perform very accurate, fast, convenient and universal energy decomposition analysis”（<http://sobereva.com/685>，中文）包含更多讨论。

## **3.24.4 原子对色散能贡献的分析**

### **理论**

对于 B3LYP 等描述色散相互作用能力为零的 DFT 泛函，著名的 DFT-D3 色散校正能可近似视为色散能。该观点已在 *J. Phys. Chem. A*, **127**, 7023 (2023) 中提出，并在 *J. Chem. Theory Comput.*, **20**, 1923 (2024) 中通过与 DLPNO-CCSD(T) 计算的色散能比较得到进一步证实。不考虑三体耦合项时，DFT-D3 总色散校正能为每对原子间色散相互作用能之和。因此，体系中原子 *A* 对色散能的贡献可计算为 ${\varepsilon}_{A}^{}=(1/2)\sum_{B\neq A} {\varepsilon}_{A,B}^{}$，其中 ${\varepsilon}_{A,B}^{}$ 为原子 *A* 与 $B$ 之间的 DFT-D3 色散校正能。片段对色散能的贡献即其原子贡献之和。两个片段间的色散相互作用能等于它们之间每对原子间色散相互作用能之和。

此外，*J. Chem. Theory Comput.*, **20**, 1923 (2024) 提出了色散密度的思想，定义为

$$
{\rho}_{\mathrm{disp}}\left( \mathbf{r} \right)={\left( \frac{\pi}{\alpha} \right)}^{-3/2}\sum_{A} {\varepsilon}_{A}{e}^{-\alpha{(\mathbf{r}-{\mathbf{R}}_{A})}^{2}}
$$

其中 α 通常取 0.5，**R***$_{A}$* 为原子 *A* 的坐标。本质上，${\rho}_{\mathrm{disp}}$ 将原子对色散能的贡献展宽为高斯函数，得到实空间函数，可图形化展示。

处在不同化学环境（如结构 $m$ 与 $n$）的某原子 *A* 所贡献色散能之差记为 $\Delta {\varepsilon}_{A}$。将上式中的 ${\varepsilon}_{A}$ 替换为 $\Delta {\varepsilon}_{A}$ 即得 $\Delta {\rho}_{\mathrm{disp}}$ 函数。若计算 $\Delta {\rho}_{\mathrm{disp}}$ 所用核坐标对应结构 $m$，则 $\Delta {\rho}_{\mathrm{disp}}$ 可用于对结构 $m$ 的原子着色，或绘制等值面 (isosurface) 并叠加到结构图上，以突出对色散能变化贡献最大的区域。

上述信息对其他类型的色散校正方案（如 DFT-D4）同样成立，但 Multiwfn 目前仅支持基于 DFT-D3 进行该分析。

### **功能**

本模块所有数据均基于以 B3LYP 拟合参数的 DFT-D3(BJ) 色散校正能计算。支持周期体系。

本模块的功能如下

- 计算当前体系原子对色散能的贡献：各原子的值显示在屏幕上，可导出名为 *atomdisp.pqr* 的文件，其中“charge”属性（文件倒数第三列）对应原子对色散能的贡献。若将该文件载入 VMD 程序，可按“charge”属性对原子着色，直观展示原子贡献。

- 计算当前体系的色散密度：将要求定义格点设置，然后计算色散密度的格点数据 (grid data)，可导出为当前文件夹中的 *dispdens.cub*。之后可用 VMD、VESTA 等载入并绘制色散密度的等值面。

- 计算当前体系与另一体系原子对色散能贡献之差：将要求为当前体系定义一个片段（体系 *A* 的片段 *i*），再要求输入另一体系的文件路径并为其定义一个片段（体系 *B* 的片段 *j*）。两体系不一定对应同一体系，但两片段必须原子数相同且原子顺序一致。之后，Multiwfn 将依次打印体系 *B* 再打印体系 *A* 的总色散能。然后打印片段 *i* 中原子对体系 *A* 色散能的贡献与片段 *j* 中原子对体系 *B* 色散能的贡献之差，并可导出 *diffatomdisp.pqr*，其“charge”属性对应此差值。

- 计算当前体系与另一体系的色散密度差。与上一功能类似，但计算 $\Delta {\rho}_{\mathrm{disp}}$ 的格点数据并导出为当前文件夹中的 *dispdensdiff.cub*。

- 计算片段对色散能的贡献

- 计算两个片段间的色散相互作用能

### **用法**

本模块对应主功能 21 的子功能 4。

输入文件须包含原子信息，如 xyz、pdb、mol2、gjf、fch、mwfn，全面介绍见[2.5 节](sec-2-5-input-files-and-wavefunction-types.md)。若输入文件含晶胞信息，则计算视为周期体系。

该功能需要经 Tian Lu 修改的 Grimme dftd3 程序，可下载：<http://sobereva.com/soft/dftd3_TLmod.zip>，内含修改后的源代码、预编译 Windows 版可执行文件（*dftd3.exe*）、预编译 Linux 版可执行文件（*dftd3*）。在启动 Multiwfn 之前，应将 *settings.ini* 中的“dftd3path”设为 dftd3 可执行文件的实际路径，以便 Multiwfn 调用 dftd3。在 Linux 环境下，别忘了用“chmod”为 *dftd3* 添加可执行权限。

该分析的例子见[4.21.4 节](sec-4-21-energy-decomposition-analysis.md#4214-原子对色散能贡献分析示例)。
