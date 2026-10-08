# 扩展过渡态-化学价自然轨道 (ETS-NOCV) 分析 (23) (Extended Transition State - Natural Orbitals for Chemical Valence (ETS-NOCV) analysis (23))

> Multiwfn manual, p.354–360.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.354 -->



例子见 4.22.6 节。


## 3.26 扩展过渡态-化学价自然轨道 (ETS-NOCV) 分析 (23) (Extended Transition State - Natural Orbitals for Chemical Valence (ETS-NOCV) analysis (23))

扩展过渡态-化学价自然轨道 (ETS-NOCV) 方法由 Ziegler 等在 J. Chem. Theory Comput., 5, 962 (2009) 中提出，它是 J. Phys. Chem. A, 112, 1933 (2008) 中提出的 NOCV 方法与 Theor. Chim. Acta, 46, 1 (1977) 中 ETS 思想的结合。ETS-NOCV 已被广泛用于研究片段间的化学键与弱相互作用。简言之，ETS-NOCV 使人能通过对相互作用所致密度矩阵变化的可视化分解分析，深入洞察片段间相互作用。

我将先在 3.26.1 节尽可能清晰详细地介绍 ETS-NOCV 理论，然后在 3.26.2 节提及 Multiwfn 中该分析的一些实现细节。在 3.26.3 节我将描述 Multiwfn 中 ETS-NOCV 模块的功能与用法。ETS-NOCV 分析的应用例子见 4.23 节。


### 3.26.1 理论 (Theory)

Multiwfn 中的 ETS-NOCV 分析支持任意数目的片段。但为简单起见，我在下面介绍 ETS-NOCV 理论时只涉及两个片段。

片段间相互作用能的物理分量 我先回顾片段间相互作用能的物理分量，这是理解 ETS-NOCV 的重要预备知识。

片段 A 与 B 之间因片段间相互作用引起的总能量变化可表示为（下述片段处于复合物结构中，故组合过程中因片段结构扭曲引起的形变能在此不考虑）：

0 + ∆𝐸Pauli + ∆𝐸orb 其中 EAB 为复合物电子能量，EA 与 EB 分别为 A 与 B 在复合物几何下的电子能量。四个物理分量定义如下 ∆𝐸int = 𝐸𝐴𝐵−𝐸𝐴−𝐸𝐵= ∆𝐸els + ∆𝐸XC

- ∆𝐸els：片段间静电相互作用能。按 A 与 B 原始波函数 (Ψ𝐴 与 Ψ𝐵) 之间的经典 Coulomb 相互作用能计算。

0：从 Ψ𝐴 与 Ψ𝐵 组合为 Ψ𝐴Ψ𝐵 过程中交换-相关 (XC) 能量的变化。它也计入片段间色散相互作用，因为色散效应本质上是片段间 Coulomb 相关。

- ∆𝐸XC

- ∆𝐸Pauli：两片段电子间 Pauli 排斥引起的能量升高。也称为交换-排斥项。

- ∆𝐸orb：因片段轨道混合引起的轨道相互作用能，计入极化效应（占据与未占据轨道的片段内混合）与电荷转移效应（占据与未占据轨道的片段间混合）。


<!-- p.355 -->



具体而言，ΔEPauli 表示为

0 ] −𝐸[Ψ𝐴Ψ𝐵] 其中 E[ ] 表示复合物的能量泛函。Ψ𝐴 与 Ψ𝐵 为 A 与 B 的原始波函数。Ψ𝐴Ψ𝐵 可称为前分子 (promolecular) 波函数，它是 Ψ𝐴 与 Ψ𝐵 的 Hartree 积，简单对应于由 A 与 B 全部占据轨道直接构建的 Slater 行列式。Ψ𝐴𝐵 0 记为冻结态 (frozen state) 波函数，定义为 Ψ𝐴 与 Ψ𝐵 的反对称积；具体而言，它对应于由 A 与 B 全部占据轨道构建的 Slater 行列式，且在这些轨道间采用了 Löwdin 正交化使彼此正交。冻结态可视为源于如下事实的人为中间态：当两片段组合在一起形成全同粒子体系时，所有电子轨道必须构成正交集，或一片段的占据轨道必须与另一片段的占据轨道正交以遵守 Pauli 不相容原理。片段间 Löwdin 正交化给原始片段轨道带来额外节面，这一现象显然使轨道动能 ∆𝐸Pauli = 𝐸[Ψ𝐴𝐵

增加，这正是 ΔEPauli 必为正值并起去稳定化作用的主要原因。

ΔEorb 表示为

0 ] 其中 Ψ𝐴𝐵 为 SCF 收敛后所得的实际复合物波函数。由 Ψ𝐴𝐵 0 到 Ψ𝐴𝐵 的变化源于片段内与片段间轨道混合（也称轨道弛豫）。ΔEorb 总为负项，因而稳定复合物。ETS-NOCV 方法聚焦于对 ΔEorb 项获得深入化学洞察。∆𝐸orb = 𝐸[Ψ𝐴𝐵] −𝐸[Ψ𝐴𝐵

总之，上述各项可整理为如下关系

𝐸𝐴 iso + 𝐸𝐵 iso Δ𝐸prep→ 𝐸𝐴[Ψ𝐴] + 𝐸𝐵[Ψ𝐵] 0→ 𝐸[Ψ𝐴Ψ𝐵] Δ𝐸els+Δ𝐸XC Δ𝐸Pauli→ 𝐸[Ψ𝐴𝐵 0 ] Δ𝐸orb→ 𝐸[Ψ𝐴𝐵]

其中 ΔEprep 称为准备能 (preparation energy)，它包括片段 A 与 B 从孤立几何到复合物几何的扭曲能，也包括其

电子态从最稳定态到参考态 A 与 B 的能量变化（例如，用 ETS-NOCV 研究 H2Ge=GeH2 的双键，合理的片段参考态应为三重态，但 GeH2 在孤立状态下的最稳定态为单重态。该差异应

计入 ΔEprep）。显然片段参考态的选择影响 ETS-NOCV 分析结果，而在某些情形下它在一定程度上是任意的。

坦率地说，在我看来，上述普遍接受的相互作用能划分并非完全严格。因为在复合物波函数由

前分子（参考）态 AB 到实际态 AB 的转变过程中，静电相互作用能与交换-相关能量必定也显著变化，因此 ΔEorb 项不应被视为仅反映轨道混合效应对相互作用能的贡献。

0 + ∆𝐸Pauli 在文献中有时为讨论方便称为空间位阻项 (steric term) ΔEsteric。Multiwfn 不能直接计算它或其分量，但你可 ∆𝐸els + ∆𝐸XC

用 Gaussian 结合 Multiwfn 计算 ΔEsteric，见 3.100.8 节。ΔEprep 可直接用任重量子化学程序手动计算。

NOCV 理论 首先，我们看化学价自然轨道 (NOCV) 理论。两片段间的轨道相互作用导致密度矩阵差


<!-- p.356 -->



0 ] 其中 P 与 P0 分别为实际复合物态与冻结态的密度矩阵；它们可基于相应态占据轨道的系数矩阵容易产生。∆𝐏orb = 𝐏−𝐏0 = 𝐏[Ψ𝐴𝐵] −𝐏[Ψ𝐴𝐵

NOCV 方法对角化 ∆𝐏orb 以求其本征值与本征矢，即有如下关系（矩阵在 Löwdin 正交化基函数下表示）

∆𝐏orb𝐂NOCV = 𝐂NOCV𝐯 其中 CNOCV 为 NOCV 轨道的系数矩阵，其每一列对应一个 NOCV 轨道相对 Löwdin 正交化基函数的展开系数。v 为对角矩阵，vi,i 对应第 i 个 NOCV 轨道的本征值。也可说 NOCV 轨道是密度矩阵差算符的本征函数，即

∆𝑃̂orb𝜑𝑖= 𝑣𝑖𝜑𝑖 注意 NOCV 轨道数 (N) 等于基函数数。因此，通常 N 很大，但只有很少 NOCV 轨道具有显著大小的本征值，分析时应关注它们。

轨道相互作用导致电子密度变化，可表示为“轨道形变密度 (orbital deformation density)”

0 ] ∆𝜌orb 可分解为各 NOCV 密度 {𝑣𝑖𝜑𝑖 ∆𝜌orb(𝐫) = 𝜌(𝐫) −𝜌0(𝐫) = 𝜌[Ψ𝐴𝐵] −𝜌[Ψ𝐴𝐵 2}


$$\Delta\rho^{\mathrm{o r b}}(\mathbf{r})=\sum_{i=1}^{N}v_{i}\varphi_{i}^{2}(\mathbf{r})$$

<!-- formula-ocr: formula_p356_250.png 已替换为LaTeX, 原图保留备查 -->

由于 ∆𝐏orb 是在一组正交基下表示的无迹矩阵，NOCV 轨道的一个值得注意的特征是它们成对出现，即若本征值由最

正到最负排序，则 vN+1-i = −vi。为简单起见，后文将 N+1−i 简写为 −i。于是，∆𝜌orb 也可分解为 NOCV 对贡献以便于分析讨论


$$\Delta\rho^{\mathrm{o r b}}(\mathbf{r})=\sum_{i=1}^{N/2}v_{i}\varphi_{i}^{2}(\mathbf{r})+v_{-i}\varphi_{-i}^{2}(\mathbf{r})=\sum_{i=1}^{N/2}v_{i}[\varphi_{i}^{2}(\mathbf{r})-\varphi_{-i}^{2}(\mathbf{r})]$$

<!-- formula-ocr: formula_p356_251.png 已替换为LaTeX, 原图保留备查 -->

显然，NOCV 分析使我们能从 NOCV 轨道或密度的角度细致考察轨道形变密度，以更好地理解轨道相互作用的本质。

ETS 与 ETS-NOCV 理论 扩展过渡态 (ETS) 理论表明


$$\Delta E_{\mathrm{orb}}=\mathrm{Tr}\big(\Delta\mathbf{P}^{\mathrm{orb}}\mathbf{F}^{\mathrm{TS}}\big)=\sum_{\mu}^{N}\sum_{\nu}^{N}\Delta P_{\mu\nu}^{\mathrm{orb}}F_{\mu\nu}^{\mathrm{TS}}$$

<!-- formula-ocr: formula_p356_252.png 已替换为LaTeX, 原图保留备查 -->

∆𝐸orb = Tr(Δ𝐏orb𝐅TS) = ∑∑∆𝑃𝜇𝜈orb𝐹𝜇𝜈TS

其中 μ 与 ν 为 Löwdin 正交化基函数的指标。FTS 为所谓扩展过渡态 Fock 矩阵（KS-DFT 情形下为 Kohn-Sham 矩阵），即用 Ψ𝐴𝐵 与 Ψ𝐴𝐵 0 的平均构建的 Fock 矩阵。注意此处的“扩展过渡态”与通常意义的过渡态很不同，在当前语境下它指 Ψ𝐴𝐵 与 Ψ𝐴𝐵 0 中点处的人为电子结构，其中轨道相互作用仅发生了一半。

ETS-NOCV 理论表明


<!-- p.357 -->




$$\Delta E_{\mathrm{orb}}=\sum_{i=1}^{N}\Delta E_{i}^{\mathrm{orb}}=\sum_{i=1}^{N}\nu_{i}\tilde{F}_{i,i}^{\mathrm{TS}}$$

<!-- formula-ocr: formula_p357_253.png 已替换为LaTeX, 原图保留备查 -->

其中 i 为 NOCV 指标，𝐹̃𝑖,𝑖 TS 为 NOCV 基下 Fock 矩阵的第 i 个对角元

轨道；换言之，它对应于用 𝐹̂TS 算符估计的第 i 个 NOCV 轨道能量，即 𝐹̃𝑖,𝑖 TS = ⟨𝜑𝑖|𝐹̂TS|𝜑𝑖⟩。同样，由于 NOCV 轨道成对，∆𝐸orb 可分解为 NOCV 对的贡献


$$\Delta E_{\mathrm{orb}}=\sum_{i=1}^{N/2}v_{i}\big[\tilde{F}_{i,i}^{\mathrm{TS}}-\tilde{F}_{-i,-i}^{\mathrm{TS}}\big]$$

<!-- formula-ocr: formula_p357_254.png 已替换为LaTeX, 原图保留备查 -->

由能量贡献，我们可判断哪些 NOCV 对在轨道相互作用中起主要作用，进而着重分析其特征。本征值或能量很小的 NOCV 对在讨论时可忽略。

形变密度 最后，三类形变密度总结如下，它们涉及 Multiwfn 中的 ETS-NOCV 分析，注意 ρ、ρ0、ρA 与 ρB 分别对应 Ψ𝐴𝐵、Ψ𝐴𝐵 0、Ψ𝐴 与 Ψ𝐵 的电子密度。

Pauli 形变密度：

∆𝜌Pauli(𝐫) = 𝜌0(𝐫) −[𝜌𝐴(𝐫) + 𝜌𝐵(𝐫)] 轨道形变密度：

∆𝜌orb(𝐫) = 𝜌(𝐫) −𝜌0(𝐫) 总形变密度：


$$\Delta\rho(\mathbf{r})=\Delta\rho^{\mathrm{o r b}}(\mathbf{r})+\Delta\rho^{\mathrm{P a u l i}}(\mathbf{r})=\rho(\mathbf{r})-[\rho_{A}(\mathbf{r})+\rho_{B}(\mathbf{r})]$$

<!-- formula-ocr: formula_p357_255.png 已替换为LaTeX, 原图保留备查 -->


### 3.26.2 实现细节 (Implementation details)

特征 (Features) Multiwfn 中的 ETS-NOCV 模块具有如下功能：

- 计算 NOCV 轨道波函数、本征值与能量
- 可视化 NOCV 轨道并导出相应 cube 文件
- 计算 NOCV 对对 ΔEorb 的能量贡献
- 可视化 NOCV 对密度并导出相应 cube 文件
- 用 SCPA 方法计算 NOCV 对与轨道的组成
- 可视化前分子 (promolecular)、冻结态 (frozen state) 与实际复合物轨道
- 可视化 ΔρPauli、Δρorb 和 Δρ 等值面 ETS-NOCV 模块支持定义任意数目的片段。若你定义了 M 个片段，则 ETS-NOCV 将分析全部 M 个片段之间的总相互作用。

仅 Hartree-Fock 与 Kohn-Sham DFT 波函数受支持。多组态波函数如 coupled-cluster、CASSCF 与 double-hybrid 泛函波函数不受支持。

仅限制性闭壳层或非限制性开壳层波函数可接受。限制性开壳层波函数不受支持。

<!-- p.358 -->


如果配合物是开壳层，或者任一片段是开壳层，ETS-NOCV分析将自动以开壳层形式进行。在这种情况下，alpha和beta NOCV轨道被独立求解，其能量分别用alpha和beta Fock矩阵来估计。

Multiwfn中的NOCV轨道能量并非按上文所述标准ETS-NOCV方法的严格方式计算！这是因为ETS-NOCV分析中的FTS目前在Multiwfn中还无法获得。在ETS-NOCV模块的后处理菜单中，你可以选择载入一个包含量子化学程序输出的配合物实际Fock矩阵的文件，或者也可以选择让Multiwfn基于输入文件中记录的轨道能量和系数通过F=SCEC-1关系直接生成配合物的实际Fock矩阵，然后例如第i个NOCV轨道能量将被计算为⟨𝜑𝑖|𝐹̂|𝜑𝑖⟩，其中𝐹̂是与载入或生成的Fock矩阵相对应的Fock算符。根据我与一些已发表的ETS-NOCV数据以及ORCA程序结果的比较，用这种近似方式基于𝐹̂计算得到的NOCV能量与基于𝐹̂TS得到的严格意义上的NOCV能量接近（特别是弱相互作用情形），至少这种差异不会定性地影响你对主导NOCV轨道/对的识别。注意由于这一差别，Multiwfn给出的所有NOCV轨道或轨道对能量之和并不严格等于ΔEorb。

输入文件 你需要提供配合物以及每个片段的波函数文件。文件应包含基函数信息，例如你可以使用.fch、.mwfn、.molden等；但不能使用.wfn和.wfx，因为它们不包含基函数信息。如果你对此有疑问，见第2.5节。

要为一个体系准备ETS-NOCV分析所需的波函数文件，通常应按以下步骤进行

(1) 首先用你喜欢的量子化学程序优化配合物的几何结构，同时获得配合物的波函数文件

(2) 从优化后的配合物中提取每个片段的坐标，然后将其保存为单点任务的输入文件。如果你使用Gaussian，不要忘记加上nosymm关键词，以避免计算过程中发生自动重定向。

(3) 运行每个片段的输入文件以获得它们的波函数文件。显然，片段的计算水平必须与配合物完全相同。如果没有特殊理由，使用弥散函数不仅完全没有必要，而且不建议使用。通常，使用3-zeta基组如def2-TZVP已完全足够，而使用2-zeta基组如6-31G*和def2-SVP对定性研究也已足够。

在按照在ETS-NOCV模块中载入片段的顺序排列每个片段中的原子后，原子的顺序必须与配合物中的顺序一致。显然，这要求片段文件中的原子顺序必须与配合物中的相同，且每个片段的原子在配合物中必须连续出现。

通常，应避免使用隐式溶剂化模型，它会使情况复杂得多。


<!-- p.359 -->




### 3.26.3 用法(Usage)

使用ETS-NOCV模块的一般过程是：(1) 启动Multiwfn，并载入配合物的波函数文件 (2) 进入主功能23 (3) 输入片段数 (4) 输入每个片段波函数文件的文件路径。载入顺序应与片段在配合物中出现的顺序一致

注意，若发现某个片段为非限制开壳层，还会询问你是否选择翻转自旋(flip spin)。如果你选择y，则alpha和beta轨道的波函数和占据数将被交换。你应恰当设置自旋翻转，使所有片段的alpha(beta)电子数之和与配合物的相同。

(5) 此时NOCV轨道波函数和本征值已计算完毕，NOCV已自动配对。从屏幕上的NOCV信息中，你可以直接找到NOCV对序号和相应的NOCV序号及其本征值。目前NOCV能量尚未计算。

之后会出现后处理菜单，你可根据需要选择相应选项，简述如下。

如果你想再次查看NOCV信息，选择“0 打印NOCV信息(0 Print NOCV information)”。默认NOCV本征值的打印阈值为0.001，本征值绝对值小于此阈值的NOCV将不显示，以避免输出过长。你可通过“-3 设置NOCV本征值打印阈值(-3 Set printing threshold of NOCV eigenvalues)”手动更改阈值。

要获得NOCV能量，你需要选择“-1 载入Fock/KS矩阵并计算NOCV轨道能量(-1 Load Fock/KS matrix and evaluate NOCV orbital energies)”以载入包含当前配合物在相同水平下计算的Fock矩阵的文件（详见本手册附录7），或选择“-2 生成Fock/KS矩阵并计算NOCV轨道能量(-2 Generate Fock/KS matrix and evaluate NOCV orbital energies)”以基于配合物波函数文件（即启动Multiwfn后载入的文件）中分子轨道能量和系数生成当前配合物的Fock矩阵。然后Multiwfn将计算NOCV能量，并在屏幕上显示带有能量的NOCV信息。

“1 显示NOCV轨道等值面(1 Show isosurface of NOCV orbitals)”用于可视化NOCV轨道。选择此选项后，为方便用户，屏幕上会显示NOCV信息，并出现一个GUI窗口，你可从窗口右下角列表中选择相应的NOCV轨道，也可直接在窗口右下角文本框中输入想要查看的NOCV轨道序号。

“2 显示NOCV对密度等值面(2 Show isosurface of NOCV pair density)”用于直观查看NOCV对的密度。选择后，为方便用户，屏幕上会显示NOCV信息，然后你可输入感兴趣的NOCV对序号。例如，若接着输入6，则将计算𝑣6[𝜑6 2 (𝐫)]的格点数据并在GUI窗口中显示其等值面图。需要特别注意的是，你可以输入一串对序号以获得它们的总密度；例如，若输入2,4-6,9，则将计算∑𝑣𝑖[𝜑𝑖 2 (𝐫)]𝑖=2,4,5,6,9的格点数据并绘制等值面。若总共有例如50个NOCV而你输入1-50，则格点数据2(𝐫) −𝜑−6 2(𝐫) −𝜑−𝑖

将恰好对应于轨道形变密度Δρorb。此外，值得注意的是，对于开壳层情形，alpha和beta自旋的对序号是不同的（如屏幕所示），因此你可以输入恰当的序号以查看特定的alpha和beta NOCV对之和。

若想可视化上文提到的ΔρPauli、Δρorb和Δρ，可分别选择


<!-- p.360 -->



“3 显示Pauli形变密度等值面(3 Show isosurface of Pauli deformation density)”、“4 显示轨道形变密度等值面(4 Show isosurface of orbital deformation density)”

和“5 显示总形变密度等值面(5 Show isosurface of total deformation density)”。ΔρPauli可让你生动理解由于Pauli排斥，片段间区域的电子如何被排斥。Δρorb使你能图形化地考察由于共价相互作用形成导致的片段间电子聚集，或由于片段的占据轨道与其它片段的空轨道混合导致的片段间电子转移。Δρ恰好是ΔρPauli与Δρorb之和，事实上它也可利用主功能5的自定义操作功能（第3.7.1节）计算得到。

NOCV轨道、NOCV对、ΔρPauli、Δρorb和Δρ的格点数据也可导出为.cub文件，以便你在第三方可视化软件中进行可视化，只需选择选项6~10中相应的一项即可。

当选择选项2至8以可视化或导出各种密度时，若你尚未通过“-5 设置计算各种密度所用的格点(-5 Set grid for calculation of various densities)”定义格点设置，将自动提示你先设置格点。下次则无需再设置格点，但你仍可随时通过选项-5更改格点设置。

0和Ψ𝐴𝐵见第3.26.1节，你可分别选择“11 可视化前分子轨道(11 Visualize promolecular orbitals)”、“12 可视化冻结态轨道(12 Visualize frozen state orbitals)”和“13 可视化实际配合物轨道(13 Visualize actual complex orbitals)”来可视化相应轨道的等值面。Ψ𝐴Ψ𝐵的轨道即片段波函数文件中的轨道，Ψ𝐴𝐵的轨道即配合物波函数文件中的轨道。通过比较Ψ𝐴𝐵 0中的轨道与Ψ𝐴Ψ𝐵中的轨道，你可以考察片段电子间的Pauli排斥（通过前文提到的Löwdin正交化实现）如何使占据的片段分子轨道发生形变。若等值面值已设得足够小，你将能观察到由于Löwdin正交化导致的Ψ𝐴𝐵 0片段轨道上额外的节面。注意在Multiwfn的ETS-NOCV分析中正交化不作用于空轨道，因此Ψ𝐴𝐵 0与Ψ𝐴Ψ𝐵中的空轨道完全相同。研究NOCV对及其相应NOCV轨道的组成在你想更好地理解其本质时往往有用。若选择选项“14 计算NOCV轨道和对的组成(14 Calculate composition of NOCV orbitals and pairs)”，将被要求选择一个NOCV对，然后每个基函数、壳层、角动量和原子对该NOCV对及相应NOCV轨道的贡献将打印在屏幕上。NOCV轨道组成用第3.10.3节提到的SCPA方法计算。NOCV对组成按𝑣𝑖Θ𝑖+ 𝑣𝑗Θ𝑗计算，若你对Ψ𝐴Ψ𝐵、Ψ𝐴𝐵的占据轨道感兴趣

其中i和j是配对的两个NOCV轨道的序号，𝑣𝑗= −𝑣𝑖，Θ是用SCPA方法计算的轨道组成。此选项在研究电子转移时很有用。例如，若用此选项发现原子A和B对NOCV对1的贡献分别为34.12%和-20.53%，则意味着由于NOCV对1表征的相互作用，原子A得到了0.3412个电子而原子B失去了0.2053个电子。注意绝不要使用弥散函数，因为SCPA方法与弥散函数不兼容。若你确实不得不用弥散函数，在完成ETS-NOCV分析后，你应返回主菜单（此时内存中的轨道为NOCV轨道），然后用主功能8通过例如Hirshfeld或Becke方法计算轨道组成，这在存在弥散函数时仍能正常工作。

选项“-6 手动定义NOCV对与轨道的对应关系(-6 Manually define correspondence between NOCV pairs and orbitals)”有时很有用。Multiwfn按本征值排序的NOCV轨道自动构建NOCV对。对于对称体系（例如线性体系Ne...BeO），某些NOCV轨道可能
