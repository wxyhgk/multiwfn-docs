# 轨道定域分析（Orbital localization analysis）（19）

> Multiwfn manual, p.305–309.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.305 -->



例子见 4.18.18 节。


## 3.22 轨道定域分析（Orbital localization analysis）（19）

轨道定域的理论（Theory of orbital localization） 正则分子轨道（CMOs）常呈强离域特征，从而不传达关于化学键的有用信息。定域 MO 有很多方式，最流行的有 Foster-Boys (FB) 定域、Edmiston–Ruedenberg (ER) 定域与 Pipek–Mezey (PM) 定域。NBO 程序支持的 NLMO 方法也是一种轨道定域算法。这些方法所得轨道称为定域分子轨道（LMOs）。LMOs 与 CMOs 都是正交归一集且维数相同，可经幺正变换相互转换。

FB 是最老的轨道定域方法；见 Rev. Mod. Phys., 32, 300 (1960)。该方法最小化下量，从而全部轨道的空间分布范围尽量窄

$$\left\langle\Omega\right\rangle_{\mathrm{B o y s}}=\sum_{i}\iint\rho_{i}(\mathbf{r}_{1})(\mathbf{r}_{1}-\mathbf{r}_{2})^{2}\rho_{i}(\mathbf{r}_{2})\mathrm{d}\mathbf{r}_{1}\mathrm{d}\mathbf{r}_{2}\quad\rho_{i}=\mid\varphi_{i}\mid^{2}$$

FB 方法很流行且广泛用，所以 Multiwfn 支持。

Rev. Mod. Phys., 35, 457 (1963) 提出的 ER 定域也是著名方法，它经由最大化下量（轨道自排斥积分）定域轨道


$$\left\langle\Omega\right\rangle_{\mathrm{E R}}=\sum_{i}\iint\rho_{i}(\mathbf{r}_{1})\frac{1}{\left|\mathbf{r}_{1}-\mathbf{r}_{2}\right|}\rho_{i}(\mathbf{r}_{2})\mathrm{d}\mathbf{r}_{1}\mathrm{d}\mathbf{r}_{2}$$

<!-- formula-ocr: formula_p305_212.png 已替换为LaTeX, 原图保留备查 -->

ER 方法很不受待见，因为它需求电子积分的求值，很复杂；而且积分从 AO 基到 MO 基的变换很贵。虽然少数论文中有人认为 ER 方法物理意义更好且经由引入 resolution-of-identity 技术可大幅降低计算代价，笔者从不认为有任何令人信服的理由用 ER 方法代替 FB，所以 Multiwfn 不支持 ER 方法。

最流行的轨道定域方法是 PM。PM 定域的本质是最大化下量，从而全部轨道的分布范围尽量收缩


$$p_{A}^{i}$$

<!-- formula-ocr: formula_p305_213.png 已替换为LaTeX, 原图保留备查 -->

iA

在 PM 方法的原文 J. Chem. Phys., 90, 4916 (1989) 中，pAi 对应 MO i 中原子 A 的 Mulliken 布居。而在 J. Chem. Theory Comput., 10, 642 (2014) 中指出，其它布居方法如 Löwdin、Hirshfeld、Becke、AIM 也可与 PM 联用并获得合理结果。目前 Multiwfn 支持基于 Mulliken、Löwdin、Becke 布居的 PM 方法。

算法细节（Algorithm details） 若对轨道定域方法的实现细节不感兴趣，可放心跳过本部分。


<!-- p.306 -->



上述量的最大化或最小化可用 Jacob sweep 算法完成，它用于轨道定域方法的原文且至今仍普遍使用。该方法效率低于后来发展的复杂方法如 unitary optimization 与 trust region；但 Jacob sweep 很简单且对多数情形很好用，尤其只需定域占据轨道时，因此 Multiwfn 用该算法。

基于各种布居方法的 PM 定域的工作方程基本相同，见 J. Comput. Chem., 14, 736 (1993) Eq. 9，它们只在项 Q 的定义上不同，Jacob sweep 每次迭代对每轨道对都需算它。

对基于 Mulliken 布居的 PM 定域（PM-Mulliken 方法），轨道 i 与 j 对原子 A 的项 Q 为


$$\begin{array}{r}{Q_{A}^{i j}=\frac{1}{2}\displaystyle\sum_{\mu\in A}\displaystyle\sum_{v}[C_{v i}C_{\mu j}+C_{\mu i}C_{v j}]S_{\mu v}}\end{array}$$

<!-- formula-ocr: formula_p306_214.png 已替换为LaTeX, 原图保留备查 -->

其中 μ 与 ν 对应基函数序号，后者循环全部基函数。

对 PM-Löwdin 方法，因基函数已用 Löwdin 对称正交化，项 Q 简化为 ijAijAQC Cμμμ∈= 

PM-Löwdin 似乎比 PM-Mulliken 便宜得多；但若编程得当，两方法的代价本质相同，因为 PM-Mulliken 情形的 Q 可重写为


$$Q_{A}^{i j}=\frac{1}{2}\sum_{\mu\in A}[C_{\mu j}(\mathbf{S C})_{\mu i}+C_{\mu i}(\mathbf{S C})_{\mu j}]$$

<!-- formula-ocr: formula_p306_215.png 已替换为LaTeX, 原图保留备查 -->

若 Jacob sweep 前算好 SC 矩阵存于内存并在迭代中频繁更新，对序号 ν 的求和可完全忽略。事实上，因为 Löwdin 方法的对称对角化步骤对大体系耗时，PM-Mulliken 的总代价一般低于 PM-Löwdin。

在 PM-Becke，即基于 Becke 布居的 PM 定域（见 3.9.8 节）中，Q 写为


$$\boldsymbol{Q}_{A}^{ij}=\boldsymbol{\mathbf{c}}_{i}^{\mathrm{T}}\boldsymbol{\mathbf{S}}^{A}\boldsymbol{\mathbf{c}}_{j}$$

<!-- formula-ocr: formula_p306_216.png 已替换为LaTeX, 原图保留备查 -->

其中 SA 为原子 A 处基函数间的原子重叠矩阵，wA(r) 为原子 A 的 Becke 权重

函数，χ 为基函数，ci 表示轨道 i 展开系数的列阵。PM-Becke 方法的代价高，尤其对大体系，这不仅因为用数值积分算全部原子的原子重叠矩阵很耗时，而且整个定域过程中 Q 项算很多次而每次都涉及贵的矩阵乘法。

关于 FB 方法，因它涉及偶极矩积分从 AO 到 MO 基的变换，需大量算术运算，它比 PM-Mulliken 与 PM-Löwdin 贵，但代价显著低于 PM-Becke。

该用哪种轨道定域方法？（Which orbital localization method should I use?） 一般推荐用 PM-Mulliken 与 PM-Löwdin，因为其结果通常满意且代价很低。但当有大量弥散函数时


<!-- p.307 -->



这些方法可能（但不总是）失效，众所周知弥散函数严重破坏 Löwdin 与 Mulliken 布居的意义。

若需用 PM 方法而弥散函数对表示当前体系的电子结构可有可无（如阴离子或被强外电场严重极化的中性分子），应改用更稳健但贵得多的 PM-Becke 方法。

FB 定域也与弥散函数兼容，且不如 PM-

Becke 贵。但 FB 方法定域的轨道不像 PM 轨道保持 σ-π 分离特征，如双键表示为两个香蕉轨道，这与常见化学直觉有些矛盾，若不在乎这点可用 FB 方法。

轨道定域模块的用法（Usage of orbital localization module） 输入文件须含基函数信息，因此可用如 .mwfn、.fch、.molden 或 .gms 作输入文件。该功能只对限制与非限制 SCF 波函数有效。

由于 PM-Mulliken 方法稳健且代价很低，它选为 Multiwfn 的默认轨道定域方法。若要换其它方法，用选项“-6 设置定域方法（-6 Set localization method）”。

在界面中，可用选项 1 选择只定域占据 MO，或用选项 2 定域占据与未占据 MO（两套轨道分别定域，即占据与未占据轨道间不允许混合）。对非限制波函数，α 与 β 部分分别处理。用选项 3 可定域特定的 MO 子集；换言之，定域中只允许特定的 MO 混合。该功能可实现特殊目的，如选合适的 MO 以在某区域获得完全或半定域的 MO。

轨道定域为迭代过程，从而应设定收敛判据与最大循环数。默认值一般合适，不需修改。迭代中打印收敛状态，对全部定域方法，

2()iAiAPp= 的变化用于判断收敛。

一旦定域收敛，算全部所得 LMO 的轨道成分并打印 LMO 的主要特征。默认用稳健的 Hirshfeld 方法求轨道成分（细节见 3.9 节），但也可在轨道定域前经选项“-9 设置算轨道成分的方法（-9 Set the method for calculating orbital composition）”换其它方法。

最后，LMOs 导出到当前文件夹的 new.fch，Multiwfn 自动载入它，之后可以各种方式分析定域轨道；如用主功能 0 绘制为等值面或用主功能 8 做轨道成分分析。若不想让 Multiwfn 自动载入新产生的 new.fch，可选选项 -3 一次以切换状态。

做轨道定域分析的提示（Hints on performing orbital localization analysis） 在 Multiwfn 中，PM-Löwdin 与 PM-Mulliken 方法的代价正比于 Norb2Nbas，而 FB 的代价正比于 Norb2Nbas2，其中 Norb 与 Nbas 分别为要定域的轨道数与基函数数。显然，FB 贵得多。


<!-- p.308 -->



PM-Becke 方法对中等基组的中等体系（如 6-31G* 基组的 C60）已极其贵，所以大体系绝不要考虑用它。

收敛通常对未占据轨道比占据轨道难，对大体系比小体系难，对 FB 方法比 PM 方法难。

无特殊理由时，只需定域占据轨道，因为只有占据轨道携带关于电子结构的有意义信息。定域未占据轨道比定域占据轨道耗时得多，因为用扩展基组时未占据轨道数常很高。一般地，经 PM-Mulliken/Löwdin 方法，对中等基组含至多 200 原子的体系占据轨道可很容易定域。而对 FB，一般该工作只能对含至多 100 原子的体系实现。

若要降低定域占据轨道的代价，可选 "-5 是否也定域 core 轨道（-5 If also localizing core orbitals）"一次以把状态从默认 "Yes" 切为 "No"。一般地，价轨道与 core 轨道间的混合很弱，因此定域价轨道时忽略内层 core 轨道安全。但极少数情形，忽略内层 core 轨道可能导致收敛困难。

PM-Mulliken 与 PM-Löwdin 方法在 Multiwfn 中没有并行，因为笔者发现并行不明显提高速度有时还使收敛更难。FB 方法完全并行，从而用多核 CPU 将显著降低计算代价。

2-zeta 加极化函数质量的基组（如 6-31G* 与 def2-SVP）对轨道定域分析完全足够，用更大的基组从不带来可察觉的更好结果。

专题 1：求 LMO 能量（Special topic 1: Evaluating LMO energies） 尽管 LMO 不是 Fock 算符的本征函数，其能量可求为 Fock 算符的期望，可经由矩阵方程解得。具体地，LMO 基下的 Fock 矩阵可获得为

CFCFAOTLMO =

其中 FAO 为原始基函数下的 Fock 矩阵，C(μ,i) 对应 LMO i 中基函数 μ 的系数。LMO i 的能量就是对角元 FLMO(i,i)。

若要这样获得 LMOs 的能量，应在开始轨道定域前选选项“-4 是否算并打印轨道能量（-4 If calculating and print orbital energies）”。再可用两种方式提供 FAO：(1) 基于 MO 的能量与系数矩阵经 FAO=SCEC-1 关系产生 (2) 输入含 FAO 的文件的路径，再载入矩阵，细节见本手册附录 7。

专题 2：揭示 LMOs 的中心（Special topic 2: Revealing center of LMOs） 为方便捕捉所产生 LMOs 的基本分布特征，Multiwfn 能算 LMOs 的中心位置并作为 Bq 原子（鬼原子）加入当前体系，从而可用主功能 0 方便地可视化它们。LMO 的中心求为下式

iiiφφ=Rr

其中 r 为坐标矢量。

要产生 LMO 中心，应选“-8 是否算 LMOs 的中心位置与偶极矩（-8 If calculating center position and dipole


<!-- p.309 -->



moment of LMOs）”一次以把状态切为“Yes”。再产生 LMOs、导出 .fch 并重载后，LMOs 的中心位置将被求出并作为 Bq 原子加入。LMO 中心的坐标以及 LMO 序号与 Bq 序号的对应将输出到当前文件夹的 LMOcen.txt，同时主功能 0 的设置将设为显示 LMO 中心的最佳状态（如 4.19.1 节所示）。由于新加的 Bq 原子没有伴随的基函数，当前波函数不应再做波函数分析，否则 Multiwfn 可能崩溃或结果完全无意义。

注意若有多重键且用 PM 定域算法，同一键的 σ-LMO 与 π-LMO 的中心对应的 Bq 原子

可能重叠。该问题可用 FB 算法代替避免，因为 FB 把多重键表示为多个香蕉 LMOs，其中心位置明显不同。
专题 3：占据 LMOs 的偶极矩分析（Special topic 3: Dipole moment analysis for occupied LMOs） 一旦“-8 是否算 LMOs 的中心位置与偶极矩（-8 If calculating center position and dipole moment of LMOs）”已切为“Yes”，做完轨道定域后，将被要求选择是否也对占据 LMOs 做偶极矩分析。若输入 y，则得到 LMOdip.txt，其中含全部占据 LMOs 的偶极矩分析结果。为使你正确理解输出，下面描述细节。

某占据 LMO 的电子对整个体系偶极矩的贡献为


$$\mathbf{D}_{i}=\left\langle\boldsymbol{\varphi}_{i}\middle|-\mathbf{r}\middle|\boldsymbol{\varphi}_{i}\right\rangle$$

<!-- formula-ocr: formula_p309_217.png 已替换为LaTeX, 原图保留备查 -->

全部 LMOs 的该矢量输出为 LMOdip.txt 文件中的“全部占据 LMOs 对体系偶极矩的贡献（Contributions of all occupied LMOs to system dipole moment）”。

但该量不能直接用于衡量 LMO 的极性。给定 r = (r-rc)+rc，其中 rc 为固定点，上量可重写为下式

$$\mathbf{D}_{i}=\left\langle\varphi_{i}\left|-(\mathbf{r}-\mathbf{r}_{\mathrm{c}}^{i})\right|\varphi_{i}\right\rangle-\left\langle\varphi_{i}\left|\mathbf{r}_{\mathrm{c}}^{i}\right|\varphi_{i}\right\rangle=-\left\langle\varphi_{i}\left|\mathbf{r}-\mathbf{r}_{\mathrm{c}}^{i}\right|\varphi_{i}\right\rangle-\mathbf{r}_{\mathrm{c}}^{i}\left\langle\varphi_{i}\left|\varphi_{i}\right|\varphi_{i}\right\rangle=-\left\langle\varphi_{i}\left|\mathbf{r}-\mathbf{r}_{\mathrm{c}}^{i}\right|\varphi_{i}\right\rangle-\mathbf{r}_{\mathrm{c}}^{i}$$

可定义量 di，它衡量轨道相对 rc 的偶极矩：

cciiiiiiφφ= −−=+drrDr

若对某轨道适当选 rc，则 di 可能反映 LMO 的极性。

对每个识别为单中心 LMO，rc 自动设为对该 LMO 贡献最大的原子的位置。因此，di 表示 LMO 电子分布质心相对核位置的偏离。这些 {d} 打印为 LMOdip.txt 中的“单中心轨道偶极矩 (a.u.)（Single-center orbital dipole moments (a.u.)）”。

对每个识别为双中心 LMO，假设贡献最大的两原子为 A 与 B，rc 设为

RRRRRR=+++rrr c BAABABAB

其中 rA 与 RA 分别为原子 A 的核位置与共价半径。原子 B 类似。rc 位于成键区中心，因此 di 展示 LMO 电子分布质心相对 rc 的偏离，能揭示键极性。这些 {d} 打印为 LMOdip.txt 中的“双中心轨道偶极矩 (a.u.)（Two-center orbital dipole moments (a.u.)）”。

## Multiwfn

> 弱作用可视化、能量分解、CDFT、ETS-NOCV、超极化率、离域与芳香性、其它功能

> 英文原文见同目录 `05_功能3.23-3.300.md`｜图片目录：`../mw_imgs/`

---
