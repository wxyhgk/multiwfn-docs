# **3.26 扩展过渡态-化学价自然轨道 (Extended Transition State - Natural Orbitals for Chemical Valence, ETS-NOCV) 分析**

扩展过渡态-化学价自然轨道 (Extended Transition State - Natural Orbitals for Chemical Valence, ETS-NOCV) 方法 (ETS-NOCV 方法)由 Ziegler 等人在 *J. Chem. Theory Comput.*, **5**, 962 (2009) 中提出，它是 *J. Phys. Chem. A*, **112**, 1933 (2008) 中提出的 NOCV 方法与 *Theor. Chim. Acta*, **46**, 1 (1977) 中提出的 ETS 思想的结合。ETS-NOCV 已被广泛用于研究化学键以及片段之间的弱相互作用 (weak interaction)。简单地说，ETS-NOCV 通过对相互作用引起的密度矩阵变化作可视化分解分析，使人们能够深入理解片段间相互作用。

我将首先在第 [3.26.1](#3261-理论) 节中尽可能清晰、详细地介绍 ETS-NOCV 的理论，然后在第 [3.26.2](#3262-实现细节) 节中提及 Multiwfn 中该分析的一些实现细节。在第 [3.26.3](#3263-用法) 节我将描述 Multiwfn 中 ETS-NOCV 模块的功能和用法。ETS-NOCV 分析的应用示例见第 [4.23](sec-4-23-examples-of-ets-nocv-analysis.md) 节。

## **3.26.1 理论**

Multiwfn 中的 ETS-NOCV 分析支持任意数目的片段。但为简单起见，下面介绍 ETS-NOCV 理论时只涉及两个片段。

### **片段间相互作用能的物理分量**

我先回顾片段间相互作用能的物理分量，这是理解 ETS-NOCV 的重要预备知识。

片段 *A* 与 $B$ 之间因片段间相互作用引起的总能量变化可表示为（下文提到的片段均处于复合物结构中，因此此处不考虑组合过程中因片段结构畸变引起的变形能）：

$$
\Delta {E}_{\mathrm{int}}={E}_{AB}-{E}_{A}-{E}_{B}=\Delta {E}_{\mathrm{els}}+\Delta {E}_{\mathrm{XC}}^{0}+\Delta {E}_{\mathrm{Pauli}}+\Delta {E}_{\mathrm{orb}}
$$

其中 $E$ *$_{AB}$* 为复合物电子能量，$E$ *$_{A}$* 和 $E$ *$_{B}$* 为 $A$ 和 $B$ 在复合物几何结构下的电子能量。这四个物理分量定义如下

- $\Delta {E}_{\mathrm{els}}$ ：片段间静电相互作用能。它按 A 与 B 原始波函数（ ${\Psi}_{A}$ 和 ${\Psi}_{B}$ ）之间的经典库仑相互作用能计算。

- $\Delta {E}_{\mathrm{XC}}^{0}$ ：从 ${\Psi}_{A}$ 和 ${\Psi}_{B}$ 组合成 ${\Psi}_{A}{\Psi}_{B}$ 过程中交换-相关 (XC) 能量的变化。由于色散效应本质上是片段间库仑相关，它也包含了片段间色散相互作用。

- $\Delta {E}_{\mathrm{Pauli}}$ ：因两片段电子间 Pauli 排斥引起的能量升高。它也被称为交换-排斥项。

- $\Delta {E}_{\mathrm{orb}}$ ：因片段轨道混合引起的轨道相互作用能，它包括极化效应（占据轨道与非占据轨道的片段内混合）和电荷转移效应（占据轨道与非占据轨道的片段间混合）。

  具体地，Δ $E_{\mathrm{Pauli}}$ 可表示为

  
$$
\Delta {E}_{\mathrm{Pauli}}=E\left[ {\Psi}_{AB}^{0} \right]-E\left[ {\Psi}_{A}{\Psi}_{B} \right]
$$

  其中 $E[\,]$ 表示复合物的能量泛函。 ${\Psi}_{A}$ 和 ${\Psi}_{B}$ 为 $A$ 和 $B$ 的原始波函数。 ${\Psi}_{A}{\Psi}_{B}$ 可称为*前分子 (promolecular)*波函数，它是 ${\Psi}_{A}$ 和 ${\Psi}_{B}$ 的 Hartree 乘积，简单对应于由 $A$ 和 $B$ 的全部占据轨道直接构造的 Slater 行列式。 ${\Psi}_{AB}^{0}$ 记为*冻结态 (frozen state)*波函数，它定义为 ${\Psi}_{A}$ 和 ${\Psi}_{B}$ 的反对称乘积；具体地，它对应于由 $A$ 和 $B$ 的全部占据轨道构造的 Slater 行列式，并已在这些轨道之间采用 Löwdin 正交归一化使它们彼此正交归一。冻结态可视为一种人为的中间态，它来源于：当两个片段组合在一起形成全同粒子体系时，所有电子轨道必须构成正交归一集，或者说一个片段的占据轨道必须与另一片段的占据轨道正交以遵守 Pauli 不相容原理。片段间的 Löwdin 正交归一化给原始片段轨道带来了额外的节点面，这一现象显然使轨道动能升高，这正是 Δ $E_{\mathrm{Pauli}}$ 必为正值并起去稳定化作用的主要原因。

  Δ $E_{\mathrm{orb}}$ 可表示为

  
$$
\Delta {E}_{\mathrm{orb}}=E\left[ {\Psi}_{AB} \right]-E\left[ {\Psi}_{AB}^{0} \right]
$$

  其中 ${\Psi}_{AB}$ 为自洽场 (SCF) 收敛后得到的复合物实际波函数。从 ${\Psi}_{AB}^{0}$ 到 ${\Psi}_{AB}$ 的变化源于片段内和片段间的轨道混合（也称为轨道弛豫）。Δ $E_{\mathrm{orb}}$ 恒为负项，因而稳定复合物。ETS-NOCV 方法着重于对 Δ $E_{\mathrm{orb}}$ 项给出深入的化学理解。

总之，上述各项可整理为如下关系

$$
{E}_{A}^{\mathrm{iso}}+{E}_{B}^{\mathrm{iso}}\xrightarrow{\Delta{E}_{\mathrm{prep}}}{E}_{A}\left[ {\Psi}_{A} \right]+{E}_{B}\left[ {\Psi}_{B} \right]\xrightarrow{\Delta{E}_{\mathrm{els}}+\Delta{E}_{\mathrm{XC}}^{0}}E[{\Psi}_{A}{\Psi}_{B}]\xrightarrow{{\Delta E}_{\mathrm{Pauli}}}E[{\Psi}_{AB}^{0}]\xrightarrow{{\Delta E}_{\mathrm{orb}}}E[{\Psi}_{AB}]
$$

其中 Δ $E_{\mathrm{prep}}$ 称为制备能，它包括片段 *A* 和 $B$ 从孤立几何结构到复合物几何结构的畸变能，还包括它们的电子态从最稳定态到参考态 Ψ*$_{A}$* 和 Ψ*$_{B}$* 的能量变化（例如，用 ETS-NOCV 研究 H₂Ge=GeH₂ 的双键时，合理的片段参考态应为三重态，而 GeH₂ 在孤立状态下的最稳定态为单重态，这一差别应计入 Δ $E_{\mathrm{prep}}$ ）。显然片段参考态的选择会影响 ETS-NOCV 分析结果，而在某些情况下这种选择多少有些任意性。

坦率地说，在我看来，上述广为接受的相互作用能划分并不完全严格。因为在复合物波函数从前分子（参考）态 Ψ*$_{A}$*Ψ*$_{B}$* 到实际态 Ψ*$_{AB}$* 的转变过程中，静电相互作用能和交换-相关能也必然显著变化，因此 Δ $E_{\mathrm{orb}}$ 项不应被视为仅反映轨道混合效应对相互作用能的贡献。

文献中为讨论方便，有时把 $\Delta {E}_{\mathrm{els}}+\Delta {E}_{\mathrm{XC}}^{0}+\Delta {E}_{\mathrm{Pauli}}$ 称为空间位阻项 Δ $E_{\mathrm{steric}}$ 。Multiwfn 无法直接计算它或其分量，但你可以用 Gaussian 结合 Multiwfn 计算 Δ $E_{\mathrm{steric}}$ ，见第 [3.100.8](sec-3-100-other-functions-part-1.md#31008-生成以碎片波函数组合为初猜的gaussian输入文件generate-gaussian-input-file-with-initial-guess-combined-from-fragment-wavefunctions) 节。Δ $E_{\mathrm{prep}}$ 可直接用任何量子化学程序手工计算。

### **NOCV 理论**

首先，我们看化学价自然轨道 (natural orbitals for chemical valence, NOCV)理论。两片段间的轨道相互作用导致密度矩阵差

$$
\Delta {\mathbf{P}}^{\mathrm{orb}}=\mathbf{P}-{\mathbf{P}}^{0}=\mathbf{P}\left[ {\Psi}_{AB} \right]-\mathbf{P}\left[ {\Psi}_{AB}^{0} \right]
$$

其中 **P** 和 **P**⁰ 分别为复合物实际态和冻结态的密度矩阵；它们可基于相应状态下占据轨道的系数矩阵很容易地生成。NOCV 方法对角化 $\Delta {\mathbf{P}}^{\mathrm{orb}}$ 以求其本征值和本征矢量，即有如下关系（矩阵表示在 Löwdin 正交归一化的基函数下）

$$
\Delta {\mathbf{P}}^{\mathrm{orb}}{\mathbf{C}}^{\mathrm{NOCV}}={\mathbf{C}}^{\mathrm{NOCV}}\mathbf{v}
$$

其中 **C**$^{NOCV}$ 为 NOCV 轨道的系数矩阵，它的每一列对应一个 NOCV 轨道相对 Löwdin 正交归一化基函数的展开系数。**v** 为对角矩阵，$v$ *$_{i,i}$* 对应第 $i$ 个 NOCV 轨道的本征值。也可以说 NOCV 轨道是密度矩阵差算符的本征函数，即

$$
\Delta {\hat{P}}^{\mathrm{orb}}{\varphi}_{i}={v}_{i}{\varphi}_{i}
$$

注意 NOCV 轨道的数目（ $N$ ）等于基函数数目。因此，通常 $N$ 很大，但只有很少的 NOCV 轨道具有显著量级的本征值，分析时应关注这些轨道。

轨道相互作用导致电子密度变化，可表示为"轨道变形密度 (deformation density)"

$$
\Delta {\rho}^{\mathrm{orb}}\left( \mathbf{r} \right)=\rho\left( \mathbf{r} \right)-{\rho}^{0}\left( \mathbf{r} \right)=\rho\left[ {\Psi}_{AB} \right]-\rho\left[ {\Psi}_{AB}^{0} \right]
$$

$\Delta {\rho}^{\mathrm{orb}}$ 可分解为各个 NOCV 密度 { ${v}_{i}{\varphi}_{i}^{2}$ } 的贡献

$$
\Delta {\rho}^{\mathrm{orb}}\left( \mathbf{r} \right)=\sum_{i=1}^{N} {v}_{i}{\varphi}_{i}^{2}\left( \mathbf{r} \right)
$$

因为 $\Delta {\mathbf{P}}^{\mathrm{orb}}$ 是在一组正交归一基下表示的无迹矩阵，NOCV 轨道的一个显著特征是它们成对出现，即若将本征值从最正到最负排序，则 $v$ *$_{N+1-i}$* = − $v$ *$_{i}$*。为简单起见，后文将 $N+1-i$ 简写为 − $i$ 。于是，为便于分析和讨论，$\Delta {\rho}^{\mathrm{orb}}$ 也可分解为 NOCV 对的贡献

$$
\Delta {\rho}^{\mathrm{orb}}\left( \mathbf{r} \right)=\sum_{i=1}^{N/2} {v}_{i}{\varphi}_{i}^{2}\left( \mathbf{r} \right)+{{v}_{-i}\varphi}_{-i}^{2}\left( \mathbf{r} \right)=\sum_{i=1}^{N/2} {v}_{i}\left[ {\varphi}_{i}^{2}\left( \mathbf{r} \right)-{\varphi}_{-i}^{2}\left( \mathbf{r} \right) \right]
$$

显然，NOCV 分析使我们能从 NOCV 轨道或密度的角度审视轨道变形密度的细节，从而更好地理解轨道相互作用的本质。

### **ETS 与 ETS-NOCV 理论**

扩展过渡态 (ETS) 理论表明

$$
\Delta {E}_{\mathrm{orb}}=\mathrm{Tr}\left( \Delta{\mathbf{P}}^{\mathrm{orb}}{\mathbf{F}}^{\mathrm{TS}} \right)=\sum_{\mu}^{N} \sum_{\nu}^{N} \Delta {P}_{\mu\nu}^{\mathrm{orb}}{F}_{\mu\nu}^{\mathrm{TS}}
$$

其中 *µ* 和 *ν* 为 Löwdin 正交归一化基函数的指标。**F**$^{TS}$ 是所谓的扩展过渡态 Fock 矩阵（KS-DFT 情形下为 Kohn-Sham 矩阵），它是用 ${\Psi}_{AB}$ 和 ${\Psi}_{AB}^{0}$ 的平均构造的 Fock 矩阵。注意此处的"扩展过渡态"与通常意义的过渡态很不相同，在此处它指介于 ${\Psi}_{AB}$ 与 ${\Psi}_{AB}^{0}$ 之间的中点处的人为电子结构，此时轨道相互作用只发生了一半。

ETS-NOCV 理论表明

$$
\Delta {E}_{\mathrm{orb}}=\sum_{i=1}^{N} \Delta {E}_{i}^{\mathrm{orb}}=\sum_{i=1}^{N} {\nu}_{i}{\tilde{F}}_{i,i}^{\mathrm{TS}}
$$

其中 $i$ 为 NOCV 的指标，${\tilde{F}}_{i,i}^{\mathrm{TS}}$ 为 NOCV 轨道基下 Fock 矩阵的第 $i$ 个对角元；换句话说，它对应于用 ${\hat{F}}^{\mathrm{TS}}$ 算符估计的第 $i$ 个 NOCV 轨道的能量，即 ${\tilde{F}}_{i,i}^{\mathrm{TS}}=\left\langle {\varphi}_{i}\middle|{\hat{F}}^{\mathrm{TS}}\middle|{\varphi}_{i} \right\rangle$ 。

同样，因为 NOCV 轨道是成对的，$\Delta {E}_{\mathrm{orb}}$ 可分解为 NOCV 对的贡献

$$
\Delta {E}_{\mathrm{orb}}=\sum_{i=1}^{N/2} {v}_{i}\left[ {\tilde{F}}_{i,i}^{\mathrm{TS}}-{\tilde{F}}_{-i,-i}^{\mathrm{TS}} \right]
$$

从能量贡献中，我们可以判断哪些 NOCV 对在轨道相互作用中起主要作用，进而着重分析它们的特征。本征值或能量很小的 NOCV 对在讨论时可忽略。

### **变形密度**

最后，下面总结三种变形密度，它们涉及 Multiwfn 中的 ETS-NOCV 分析，注意 *ρ*、*ρ*⁰、$ρ_{A}$ 和 $ρ_{B}$ 分别对应 ${\Psi}_{AB}$ 、${\Psi}_{AB}^{0}$ 、${\Psi}_{A}$ 和 ${\Psi}_{B}$ 的电子密度。

Pauli 变形密度：

$$
\Delta {\rho}^{\mathrm{Pauli}}\left( \mathbf{r} \right)={\rho}^{0}\left( \mathbf{r} \right)-[{\rho}_{A}\left( \mathbf{r} \right)+{\rho}_{B}\left( \mathbf{r} \right)]
$$

轨道变形密度：

$$
\Delta {\rho}^{\mathrm{orb}}\left( \mathbf{r} \right)=\rho\left( \mathbf{r} \right)-{\rho}^{0}\left( \mathbf{r} \right)
$$

总变形密度：

$$
\Delta \rho\left( \mathbf{r} \right)=\Delta {\rho}^{\mathrm{orb}}\left( \mathbf{r} \right)+\Delta {\rho}^{\mathrm{Pauli}}\left( \mathbf{r} \right)=\rho\left( \mathbf{r} \right)-[{\rho}_{A}\left( \mathbf{r} \right)+{\rho}_{B}\left( \mathbf{r} \right)]
$$

## **3.26.2 实现细节**

### **功能特点**

Multiwfn 中的 ETS-NOCV 模块具有以下功能：

- 计算 NOCV 轨道波函数、本征值和能量

- 可视化 NOCV 轨道并导出相应的 cube 文件

- 计算 NOCV 对对 Δ $E_{\mathrm{orb}}$ 的能量贡献

- 可视化 NOCV 对密度并导出相应的 cube 文件

- 用 SCPA 方法计算 NOCV 对和轨道的组成

- 可视化前分子态、冻结态和复合物实际态轨道

- 可视化 Δ*ρ*$^{Pauli}$、Δ*ρ*$^{orb}$ 和 Δ*ρ* 等值面

  ETS-NOCV 模块支持定义任意数目的片段。若你定义了 $M$ 个片段，则 ETS-NOCV 将分析全部 $M$ 个片段之间的总相互作用。

  仅支持 Hartree-Fock 和 Kohn-Sham DFT 波函数。不支持耦合簇、CASSCF、双杂化泛函等多组态波函数。

  仅接受限制性闭壳层或非限制性开壳层波函数。不支持限制性开壳层波函数。

  若复合物为开壳层，或任一片段为开壳层，ETS-NOCV 分析将自动以开壳层形式进行。此时 alpha 和 beta NOCV 轨道分别独立求解，其能量分别用 alpha 和 beta Fock 矩阵估计。

  **Multiwfn 中 NOCV 轨道的能量并非按上述标准 ETS-NOCV 方法的严格方式计算！**这是因为 ETS-NOCV 分析中的 **F**$^{TS}$ 在 Multiwfn 中目前无法得到。在 ETS-NOCV 模块的后处理菜单中，你可以选择载入一个文件中由量子化学程序输出的复合物实际 Fock 矩阵，也可以选择让 Multiwfn 根据输入文件中记录的轨道能量和系数经由 **F**=**SCEC**⁻¹ 关系直接生成复合物的实际 Fock 矩阵，然后例如第 $i$ 个 NOCV 轨道的能量将按 $\left\langle {\varphi}_{i}\middle|\hat{F}\middle|{\varphi}_{i} \right\rangle$ 计算，其中 $\hat{F}$ 为与载入或生成的 Fock 矩阵对应的 Fock 算符。根据我与一些已发表的 ETS-NOCV 数据以及 ORCA 程序结果的比较，这种用 $\hat{F}$ 近似计算的 NOCV 能量与基于 ${\hat{F}}^{\mathrm{TS}}$ 的严格意义 NOCV 能量接近（特别是弱相互作用情形），至少这种差别不会定性地影响你对主导 NOCV 轨道/对的判断。注意由于这一差别，Multiwfn 给出的全部 NOCV 轨道或 NOCV 对的能量之和并不严格等于 Δ $E_{\mathrm{orb}}$ 。

### **输入文件**

你需要提供复合物的波函数文件以及每个片段的波函数文件。文件应包含基函数信息，例如你可以使用 .fch、.mwfn、.molden 等；但不能使用 .wfn 和 .wfx，因为它们不含基函数信息。若有疑惑，见第 [2.5](sec-2-5-input-files-and-wavefunction-types.md) 节。

为一个体系准备 ETS-NOCV 分析所需的波函数文件，通常应按以下步骤操作

- (1) 先用你喜欢的量子化学程序优化复合物的几何结构，同时得到复合物的波函数文件

- (2) 从优化好的复合物中抽取每个片段的坐标，然后保存为单点任务的输入文件。若你使用 Gaussian，别忘了加 *nosymm* 关键词以避免计算中自动重定向。

- (3) 运行每个片段的输入文件以得到它们的波函数文件。

显然，片段的计算水平必须与复合物完全相同。

若无特殊理由，使用弥散函数不仅完全没有必要，而且不提倡。通常，使用 def2-TZVP 这类 3-zeta 基组绝对足够，而使用 6-31G\* 和 def2-SVP 这类 2-zeta 基组对定性研究也足够。

按在 ETS-NOCV 模块中载入片段的顺序排列好每个片段中的原子后，原子的顺序必须与复合物中的一致。显然，这要求片段文件中的原子顺序与复合物中的相同，且每个片段的原子在复合物中必须连续出现。

通常应避免使用隐式溶剂化模型，它会使情况复杂得多。

## **3.26.3 用法**

使用 ETS-NOCV 模块的一般流程为：

- (1) 启动 Multiwfn，载入复合物的波函数文件

- (2) 进入主功能 23

- (3) 输入片段数目

- (4) 输入每个片段的波函数文件路径。载入顺序应与片段在复合物中出现的顺序一致

  > **注**
  >
  > 若发现某片段为非限制性开壳层，还会询问你是否翻转自旋。若你选择 *y*，则 alpha 和 beta 轨道的波函数和占据数将被交换。你应恰当设置自旋翻转，使所有片段的 alpha (beta) 电子数之和与复合物的相同。

- (5) 现在计算 NOCV 轨道波函数和本征值，NOCV 自动配对。从屏幕上的 NOCV 信息中，你可直接找到 NOCV 对指标以及相应的 NOCV 指标和它们的本征值。目前尚未计算 NOCV 能量。

之后出现后处理菜单，你可按需要选择相应选项，简述如下。

若想再次查看 NOCV 信息，选择"0 Print NOCV information"。默认 NOCV 本征值的打印阈值为 0.001，本征值绝对值小于此阈值的 NOCV 不显示，以免输出过长。你可用"-3 Set printing threshold of NOCV eigenvalues"手工改变阈值。

要得到 NOCV 能量，需选择"-1 Load Fock/KS matrix and evaluate NOCV orbital energies"以载入一个包含当前复合物在相同水平下计算的 Fock 矩阵的文件（细节见本手册[附录 7](sec-6-7-about-providing-fock-ks-matrix-to-multiwfn.md)），或选择"-2 Generate Fock/KS matrix and evaluate NOCV orbital energies"以基于复合物波函数文件（即启动 Multiwfn 后载入的文件）中分子轨道的能量和系数生成当前复合物的 Fock 矩阵（*即*上述文件）。然后 Multiwfn 将计算 NOCV 能量，并在屏幕上显示带能量的 NOCV 信息。

"1 Show isosurface of NOCV orbitals"用于可视化 NOCV 轨道。选择此选项后，为方便起见屏幕上会显示 NOCV 信息，并出现一个 GUI 窗口，你可从窗口右下角的列表中选择相应的 NOCV 轨道，也可直接在窗口右下角的文本框中输入想查看的 NOCV 轨道的指标。

"2 Show isosurface of NOCV pair density"用于直观查看 NOCV 对的密度。选择后，为方便起见屏幕上会显示 NOCV 信息，然后你可输入感兴趣的 NOCV 对指标。例如，若接着输入 *6*，则将计算 ${v}_{6}\left[ {\varphi}_{6}^{2}\left( \mathbf{r} \right)-{\varphi}_{-6}^{2}\left( \mathbf{r} \right) \right]$ 的格点数据并在 GUI 窗口中显示其等值面图。重要的是，你可输入一串对指标以得到它们的总密度；例如，若输入 *2,4-6,9*，则将计算 $\sum_{i=2,4,5,6,9} {v}_{i}\left[ {\varphi}_{i}^{2}\left( \mathbf{r} \right)-{\varphi}_{-i}^{2}\left( \mathbf{r} \right) \right]$ 的格点数据并绘制为等值面。若总共有*例如* 50 个 NOCV 而你输入 *1-50*，则格点数据就简单对应于轨道变形密度 Δ*ρ*$^{orb}$。另外值得注意的是，对于开壳层情形，alpha 和 beta 自旋的对指标不同（如屏幕所示），因此你可输入恰当的指标以查看特定的 alpha 与 beta NOCV 对之和。

若想可视化上述 Δ*ρ*$^{Pauli}$、Δ*ρ*$^{orb}$ 和 Δ*ρ*，可分别选择"3 Show isosurface of Pauli deformation density"、"4 Show isosurface of orbital deformation density"和"5 Show isosurface of total deformation density"。Δ*ρ*$^{Pauli}$ 使你能生动理解电子在片段间区域如何因 Pauli 排斥而被排开。Δ*ρ*$^{orb}$ 使你能图形化地考察因共价相互作用形成导致的片段间电子聚集，或因某片段的占据轨道与其它片段的非占据轨道混合导致的片段间电子转移。Δ*ρ* 即 Δ*ρ*$^{Pauli}$ 与 Δ*ρ*$^{orb}$ 之和，事实上它也可用主功能 5 的自定义操作功能计算（第 [3.7.1](sec-3-7-custom-operation-promolecular-and-deformation-properties.md#371-多个波函数的自定义操作-custom-operation-for-multiple-wavefunctions0) 节）。

NOCV 轨道、NOCV 对、Δ*ρ*$^{Pauli}$、Δ*ρ*$^{orb}$ 和 Δ*ρ* 的格点数据也可导出为 .cub 文件，以便在第三方可视化软件中可视化，只需选择选项 6\~10 中相应的一项。

用选项 2 至 8 可视化或导出各种密度时，若你尚未通过"-5 Set grid for calculation of various densities"定义格点设置，将自动要求你先设置格点。下次无需再设格点，但你仍可随时经由选项 -5 改变格点设置。

若你对第 [3.26.1](#3261-理论) 节中提到的 ${\Psi}_{A}{\Psi}_{B}$ 、${\Psi}_{AB}^{0}$ 和 ${\Psi}_{AB}$ 的占据轨道感兴趣，可分别选择"11 Visualize promolecular orbitals"、"12 Visualize frozen state orbitals"和"13 Visualize actual complex orbitals"以可视化相应轨道的等值面。 ${\Psi}_{A}{\Psi}_{B}$ 的轨道即片段波函数文件中的轨道， ${\Psi}_{AB}$ 的轨道即复合物波函数文件中的轨道。通过比较 ${\Psi}_{AB}^{0}$ 中的轨道与 ${\Psi}_{A}{\Psi}_{B}$ 中的轨道，你可考察片段电子间的 Pauli 排斥（如前所述经由 Löwdin 正交归一化实现）如何使占据的片段分子轨道变形。若等值面值已设得足够小，你将能在 ${\Psi}_{AB}^{0}$ 的片段轨道上观察到 Löwdin 正交归一化造成的额外节点面。注意 Multiwfn 的 ETS-NOCV 分析中正交归一化不施加于非占据轨道，因此 ${\Psi}_{AB}^{0}$ 与 ${\Psi}_{A}{\Psi}_{B}$ 中的非占据轨道完全相同。

当你想更好地理解 NOCV 对及其相应 NOCV 轨道的本质时，研究它们的组成常有帮助。若选择选项"14 Calculate composition of NOCV orbitals and pairs"，将被要求选择一个 NOCV 对，然后每个基函数、壳层、角动量和原子对该 NOCV 对及相应 NOCV 轨道的贡献将打印在屏幕上。NOCV 轨道的组成用第 [3.10.3](sec-3-10-orbital-composition-analysis.md#3103-用-mullikenstout-politzer-和-scpa-方法输出片段-1-的成分和片段间成分-4-5-6) 节提到的 SCPA 方法计算。NOCV 对的组成按 ${v}_{i}{\Theta}_{i}+{v}_{j}{\Theta}_{j}$ 计算，其中 $i$ 和 $j$ 为配对的两个 NOCV 轨道的指标，${v}_{j}=-{v}_{i}$ ，Θ 为 SCPA 方法计算的轨道组成。此选项在研究电子转移时有用。例如，若用此选项发现原子 *A* 和 $B$ 对 NOCV 对 1 的贡献分别为 34.12% 和 -20.53%，意味着原子 *A* 得到了 0.3412 个电子而原子 *B* 失去了 0.2053 个电子，这是 NOCV 对 1 所表征的相互作用导致的。注意绝不能使用弥散函数，因为 SCPA 方法与它们不兼容。若你确实不得不用弥散函数，在做完 ETS-NOCV 分析后，应回到主菜单（此时内存中的轨道为 NOCV 轨道）再用主功能 8 经由*例如* Hirshfeld 或 Becke 方法计算轨道组成，这些方法在有弥散函数时也能正常工作。

选项"-6 Manually define correspondence between NOCV pairs and orbitals"有时有用。Multiwfn 按 NOCV 轨道本征值排序自动构造 NOCV 对。对于对称体系（*例如*直线型体系 Ne...BeO），某些 NOCV 轨道可能简并，即具有完全相同的本征值；此时它们的顺序（指标）是任意的，自动确定的 NOCV 对与轨道的对应关系可能不符合预期。此时你可用选项 -6 选择一个 NOCV 对，然后手工输入该对应当对应的两个轨道的指标。此选项可多次使用以重定义多个 NOCV 对。

ETS-NOCV 分析的丰富示例见第 [4.23](sec-4-23-examples-of-ets-nocv-analysis.md) 节。
