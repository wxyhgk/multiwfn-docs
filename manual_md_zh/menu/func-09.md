# 主功能9：键级分析

功能概述：主功能 9 提供十余种键级与成键强度描述符，覆盖经典 Mayer 键级（选项 1）、多中心键级 MCBO（选项 2/-2/-3）、Löwdin 基 Wiberg 键级（选项 3）、Mulliken 键级及分解（选项 4/5）、轨道占据微扰 Mayer 键级（选项 6）、模糊键级 FBO（选项 7）、拉普拉斯键级 LBO（选项 8）、NAO 基 Wiberg 键级分解（选项 9）、本征键强度指数 IBSI（选项 10）、AV1245/AVmin 大环芳香性指数（主功能 200 选项 19）与 AIM 盆间离域指数 DI（选项 12）。分析前可用选项 `-1` 定义片段 1 和 2，之后计算键级时会自动输出片段间总键级 $I_{RS}=\sum_{A\in R}\sum_{B\in S} I_{AB}$（多中心键级、微扰 Mayer 键级、Wiberg 分解除外）。

## 子功能 1：Mayer 键级

说明：原子 $A$ 与 $B$ 之间的 Mayer 键级（*Chem. Phys. Lett.*, **97**, 270 (1983)）为 $I_{AB}=2\sum_{a\in A}\sum_{b\in B}[(\mathbf{P}^{\alpha}\mathbf{S})_{ba}(\mathbf{P}^{\alpha}\mathbf{S})_{ab}+(\mathbf{P}^{\beta}\mathbf{S})_{ba}(\mathbf{P}^{\beta}\mathbf{S})_{ab}]$，限制性闭壳层简化为 $I_{AB}=\sum_{a\in A}\sum_{b\in B}(\mathbf{PS})_{ab}(\mathbf{PS})_{ba}$。单/双/三键分别接近 1.0/2.0/3.0。程序同时输出总价 $V_A$ 与自由价 $F_A$（闭壳层自由价恒为零，总价即键级之和）。开壳层分别输出 α、β 与总键级，另有混合密度矩阵的广义 Wiberg 总键级。对基组敏感，禁弥散函数；post-HF 波函数用相应密度矩阵按相同公式计算（*Chem. Phys. Lett.*, **544**, 83 (2012)）。

菜单路径：主功能 `9` → `1` → 输入原子序号对；`-1` 可预定义两片段并同时输出片段间总键级。

输入要求：含基函数信息的波函数文件（`.mwfn`/`.fch`/`.molden`/`.gms`）。

操作步骤：

```text
examples\CH3CONH2.fch
9  // Bond order analysis
1  // Calculate Mayer bond order
```

输出示例：

```text
Bond orders with absolute value >=  0.050000
#    1:         1(C )    2(H )    0.93802674
#    2:         1(C )    3(H )    0.93473972
#    3:         1(C )    4(H )    0.94494566
#    4:         1(C )    5(C )    0.96585484
#    5:         5(C )    6(O )    1.90392771
#    6:         5(C )    7(N )    1.11849509
#    7:         6(O )    7(N )    0.07620305
#    8:         7(N )    8(H )    0.83250273
#    9:         7(N )    9(H )    0.83869874
```

默认只打印键级绝对值 ≥0.05 的项（`settings.ini` 的 `bndordthres` 调节）。选 `y` 把完整键级矩阵导出到 `bndmat.txt`。GaussView 标注技巧：`9 → 1 → y` 导出 `bndmat.txt` → `0` 回主菜单 → `1000`（隐藏主功能）→ `13` 转为含键级信息的 `.gjf`，在 GaussView（≥6.0）中 Results→Bond Properties 着色/标注显示。

产出：大于阈值的键级表、原子总价/自由价、可选的完整键级矩阵 `bndmat.txt`（例：乙酰胺 C5–O6 为 1.90，接近双键）。

来源：[3.11.1](sec-3-11-bond-order-analysis.md#3111-mayer键级分析mayer-bond-order-analysis-1) · 实例 [4.9.1](sec-4-9-bond-order-analysis.md#491-乙酰胺的mayer键级与模糊键级分析)

## 子功能 2/-2/-3：多中心键级 MCBO

说明：MCBO 是 Mayer 键级向多中心情形的推广（*Struct. Chem.*, **1**, 423 (1990)），三/四/五/六中心定义分别为 $I_{ABC}=\sum(\mathbf{PS})_{ab}(\mathbf{PS})_{bc}(\mathbf{PS})_{ca}$ 等。不同中心数不可直接比较，应比较归一化值 $\mathrm{MCBO}^{1/n}$（负值时取 $-|\mathrm{MCBO}|^{1/n}$）。选项 2 为标准定义（原始基函数）；选项 -2 为 NAO 基定义（重叠矩阵为单位阵，公式简化为 $I=\sum P_{ab}P_{bc}\cdots P_{ka}$），基组稳定性好，有弥散函数时必须用 -2；选项 -3 为 Löwdin 正交化基下的隐藏选项。输入方向（A,B,C,D vs D,C,B,A）与排列都会影响结果：研究芳香性应按环连接顺序（顺/逆时针）输入；`settings.ini` 的 `iMCBOtype=1` 打印正反向平均值，`=2` 直接打印多中心指数 MCI。若只输 `-3`/`-4`/`-5`/`-6` 则自动搜索全部三/四/五/六中心键（仅打印大于阈值者）。明显为负的三中心键级意味着三中心四电子（3c-4e）相互作用（如 CO₂）。

菜单路径：主功能 `9` → `2`（标准）/ `-2`（NAO 基）/ `-3`（Löwdin 基，隐藏）→ 按连接顺序输入环原子序号。

输入要求：选项 2/-3 需含基函数的文件；选项 -2 需带 `DMNAO` 关键词的 NBO 输出文件（不可用 `.fch`）。Gaussian 输入示例：

```text
#p PBE1PBE/6-311G** pop=nboread

opted

0 1
 C                  0.00000000    1.38886900    0.00000000
... [ignored]
 H                 -2.14060700    1.23588000    0.00000000

$NBO DMNAO $END
```

操作步骤（Li₆ 边界三元环；菲边界六元环；NAO 基菲边界环）：

```text
examples\Li6.fch
9  // Bond order analysis
2  // Multi-center bond order analysis
1,3,4  // Indices of the atoms in the boundary three-member ring
```

```text
examples\phenanthrene.fch
9  // Bond order analysis
2  // Multi-center bond order analysis
1,2,3,4,5,6  // Indices of the atoms in the boundary ring. Note that the inputting order must be in consistency with atomic connectivity, namely inputting such as 1,3,5,6,4,2 will be meaningless
```

```text
examples\phenanthrene_DMNAO.out
9  // Bond order analysis
-2  // Multi-center bond order analysis in NAO basis
1,2,3,4,5,6  // Calculate six-center bond order for the boundary ring
```

产出：多中心键级与归一化值（例：Li₆ 边界环 0.1248 vs 中心环 0.0352，前者更稳定；菲边界环 0.0594 vs 中心环 0.0265，边界环芳香性更强；NAO 基菲边界环 0.0589，与标准结果一致）。

来源：[3.11.2](sec-3-11-bond-order-analysis.md#3112-多中心键级分析multi-center-bond-order-analysis-2--2--3) · 实例 [4.9.2](sec-4-9-bond-order-analysis.md#492-li₆团簇与菲的多中心键级分析)

## 子功能 3：Löwdin 基 Wiberg 键级

说明：Wiberg 键级 $I_{AB}=\sum_{a\in A}\sum_{b\in B} P_{ab}^2$（*Tetrahedron*, **24**, 1083 (1968) 脚注）原只适用于正交基的限制性闭壳层体系；Mayer 键级可视为其推广（正交归一基下两者完全相同）。本功能先做 Löwdin 正交化再做常规 Mayer 键级分析，对基组敏感性远小于 Mayer（小基组下两者接近），但倾向于高估极性键。NBO 程序的 Wiberg 键级是在 NAO 基（OWSO 正交化）下算的，与本功能结果不同；NAO 基 Wiberg 键级见 3.11.8 节。

菜单路径：主功能 `9` → `3`。

输入要求：含基函数信息的波函数文件。

操作步骤：在主功能 9 界面输入 `3`，按提示输入原子序号对即得结果；打印阈值同样由 `bndordthres` 控制。

产出：Löwdin 基下的 Wiberg 键级表。一般无特殊原因优先用 Mayer 键级。

来源：[3.11.3](sec-3-11-bond-order-analysis.md#3113-在löwdin正交化基löwdin-orthogonalized-basis下的wiberg键级wiberg-bond-order分析-3)

## 子功能 4/5：Mulliken 键级与分解

说明：Mulliken 键级是最早的键级定义：$I_{AB}=\sum_i\eta_i\sum_{a\in A}\sum_{b\in B}2C_{a,i}C_{b,i}S_{a,b}=2\sum_{a\in A}\sum_{b\in B} P_{a,b}S_{a,b}$。与经验键级一致性差，不建议定量描述成键强度，但正/负号是成键/反键的良好定性指标。独特优势是可精确分解为轨道贡献 $I_{AB}^i=\eta_i\sum_{a\in A}\sum_{b\in B}2C_{a,i}C_{b,i}S_{a,b}$，从而知道哪些轨道对特定成键有利或不利。

菜单路径：主功能 `9` → `4` 计算 / `5` 分解 → 输入两个原子序号。

输入要求：含基函数信息的波函数文件。

操作步骤（以 CH₃CONH₂ C–C 键为例，做 Mulliken 键级轨道分解）：

```text
examples\CH3CONH2.fch
9  // Bond order analysis
5  // Decompose Mulliken bond order
```

然后输入两个原子序号（如 C–C 键的原子对），逐轨道输出贡献值，正为成键、负为反键；结合等值面与占据数微扰 Mayer 键级交叉验证。

产出：Mulliken 键级及逐轨道贡献分解表。

来源：[3.11.4](sec-3-11-bond-order-analysis.md#3114-mulliken键级mulliken-bond-order分析4与分解5) · 实例 [4.9.5](sec-4-9-bond-order-analysis.md#495-研究ch₃conh₂中c-c键的mulliken键级的轨道贡献)

## 子功能 6：轨道占据微扰 Mayer 键级

说明：通过把特定轨道占据数设零后重算 Mayer 键级，得到该轨道对键级的贡献（*J. Chem. Theory Comput.*, **8**, 908 (2012)）。差值越负，该轨道存在对成键越有利。注意 Mayer 键级不是密度矩阵的线性函数，所有轨道贡献之和一般不等于总键级。等价的手动做法是用主功能 6 把特定轨道占据数设零再算 Mayer 键级，但轨道多时很繁琐。

菜单路径：主功能 `9` → `6` → 输入两个原子序号。

输入要求：含基函数信息的波函数文件。

操作步骤（接 4.9.1 乙酰胺 C5–O6 键之后）：在键级分析模块选 `6`，输入 `5,6`，输出每条占据轨道的微扰键级与 Variance（差值）。

产出：`Mayer bond order before orbital occupancy-perturbation` 及逐轨道 `Bond order`/`Variance` 表（例：轨道 14 的 Variance 最负，对 C5–O6 成键贡献最大，表现为强 π 成键）。

来源：[3.11.5](sec-3-11-bond-order-analysis.md#3115-轨道占据微扰mayer键级orbital-occupancy-perturbed-mayer-bond-order-6) · 实例 [4.9.1](sec-4-9-bond-order-analysis.md#491-乙酰胺的mayer键级与模糊键级分析)

## 子功能 7：模糊键级 FBO

说明：模糊键级（*Chem. Phys. Lett.*, **383**, 368 (2004)）：$B_{AB}=2\sum_{\mu\nu}[(\mathbf{P}^{\alpha}\mathbf{S}^A)_{\mu\nu}(\mathbf{P}^{\alpha}\mathbf{S}^B)_{\nu\mu}+(\alpha\to\beta)]$，其中 $S_{\mu\nu}^A=\int w_A(\mathbf{r})\chi_\mu^*(\mathbf{r})\chi_\nu(\mathbf{r})\mathrm{d}\mathbf{r}$。Multiwfn 用陡峭参数 $k=3$、修正 CSD 半径的 Becke 模糊原子空间。数值通常接近 Mayer 键级（尤其低极性键），但对基组变化稳健得多；本质上是在模糊原子空间中算的离域指数 DI。需做 Becke DFT 数值积分（默认 40 径向点 × 230 角向点，`settings.ini` 的 `radpot`/`sphpot` 可加密，需 `iautointgrid=0`），因而比 Mayer 键级耗时。

菜单路径：主功能 `9` → `7`。

输入要求：GTF + 原子坐标（`.wfn`/`.wfx` 亦可，不依赖基函数信息，兼容弥散函数）。

操作步骤：在键级分析菜单选 `7`，直接得全体系键级表。

产出：模糊键级表（例：乙酰胺 C5–O6 为 2.00，C5–N7 为 1.40，与 Mayer 相近；强极性键两者可能明显偏离）。

来源：[3.11.6](sec-3-11-bond-order-analysis.md#3116-模糊键级fuzzy-bond-order-7) · 实例 [4.9.1](sec-4-9-bond-order-analysis.md#491-乙酰胺的mayer键级与模糊键级分析)

## 子功能 8：拉普拉斯键级 LBO

说明：LBO（*J. Phys. Chem. A*, **117**, 3100 (2013)，<http://pubs.acs.org/doi/abs/10.1021/jp4010345>）是基于模糊重叠空间中电子密度拉普拉斯的共价键级：$L_{A,B}=-10\times\int_{\nabla^2\rho<0} w_A(\mathbf{r})w_B(\mathbf{r})\nabla^2\rho(\mathbf{r})\mathrm{d}\mathbf{r}$。模糊重叠空间中负 $\nabla^2\rho$ 积分越大，成键区电荷集中越强，共价成键越强。LBO 与键极性、键离解能、振动频率直接相关，对计算级别不敏感，原则上可用 X 射线衍射密度求 LBO。特别适合有机体系；不适合离子键（需更好的原子空间定义）与重原子（重于 Ar）间成键。

菜单路径：主功能 `9` → `8`。

输入要求：GTF + 原子坐标。

操作步骤：

```text
examples\ethane.wfn  // Optimized and produced at B3LYP/6-31G**
9  // Bond order analysis
8  // Laplacian bond order
```

产出：LBO 键级表（例：乙烷/乙烯/乙炔 C–C 的 LBO 为 1.060/2.023/2.767，比值 1:1.907:2.61，与 BDE 比 1:1.85:2.61 高度相关；C–H 强弱顺序乙炔 > 乙烯 > 乙烷与实验一致；水 O–H 为 0.638，反映强极性）。

来源：[3.11.7](sec-3-11-bond-order-analysis.md#3117-拉普拉斯键级laplacian-bond-order-8) · 实例 [4.9.3](sec-4-9-bond-order-analysis.md#493-计算laplacian键级lbo)

## 子功能 9：NAO 基 Wiberg 键级的原子轨道对分解

说明：Wiberg 键级 $I_{AB}=\sum_{a\in A}\sum_{b\in B} P_{ab}^2$ 是密度矩阵元平方的线性组合，可直接分解为基函数对贡献 $P_{ab}^2$。为使分解有充分物理意义，最好在 NAO 下进行（每个非 Rydberg NAO 唯一对应一个原子轨道），从而得到原子轨道尺度乃至壳层尺度（$\sum_{a\in i}\sum_{b\in j} P_{ab}^2$）的 Wiberg 键级分解。

菜单路径：主功能 `9` → `9` → 输入两个原子序号；输入 `-1` 定义两片段后给出片段间 Wiberg 键级的 NAO 壳贡献。

输入要求：含 NAO 密度矩阵信息的 NBO 输出文件（`DMNAO` 关键词），同 3.11.2 节选项 -2。

操作步骤（甲醛 C–O 键为例）：

```text
examples\H2CO_DMNAO.out
9  // Bond order analysis
9  // Decompose Wiberg bond order in NAO basis
```

然后输入 `1,4`，屏幕显示总 Wiberg 键级与不可忽略的 NAO 对/壳层对贡献（打印阈值由 `bndordthres` 控制）。

产出：NAO 对/壳层对贡献分解表与总 Wiberg 键级。

来源：[3.11.8](sec-3-11-bond-order-analysis.md#3118-将nao基nao-basis中的wiberg键级分解为原子轨道对贡献atomic-orbital-pair-contributions-9) · 实例 [4.9.4](sec-4-9-bond-order-analysis.md#494-甲醛在nao基组下的wiberg键级的分解分析)

## 子功能 10：本征键强度指数 IBSI

说明：IBSI（*J. Phys. Chem. A*, **124**, 1850 (2020)）用于量化化学键/弱相互作用强度：$\mathrm{IBSI}=[(1/d^2)\int\delta g^{\mathrm{pair}}\mathrm{d}\mathbf{r}]/[(1/d_{\mathrm{H}_2}^2)\int\delta g^{\mathrm{H}_2}\mathrm{d}\mathbf{r}]$，分子为两原子间原子对 $\delta g$ 指数积分，分母为平衡 H₂ 参考值。IBSI 与共价键强度适度正相关；过渡金属配位键量级明显小于共价键，弱相互作用更低，可用于区分相互作用类型。Multiwfn 支持 IGM-pro（默认，最接近原文；纯坐标文件即可）、IGMH（需波函数；默认）、mIGM 三种形式，结果差异大。

菜单路径：主功能 `9` → `10` → `0` 开始计算；`2` 切换 IGM 形式；`3` 限定局域区域；`4` 设 H₂ 参考值；`5` 设打印距离阈值（默认 3.5 Å）。

输入要求：IGM-pro/mIGM 只需原子坐标；IGMH 需 GTF。

操作步骤：进入子功能 10 后先选积分格点质量（IGM-pro 用 medium 已定量准确；IGMH/mIGM 要求精度时至少 high），选项 2 选 IGM 形式后选 `0` 开始计算。严格的 IGMH 参考值做法：载入 H₂ 波函数，把参考值设 1.0 后算 IBSI，所得结果用作实际分子的参考值。

产出：原子对距离、积分项与 IBSI 值表（IGMH 型与 BDE 线性相关好，IGM 型较差）。

来源：[3.11.9](sec-3-11-bond-order-analysis.md#3119-本征键强度指数intrinsic-bond-strength-index-ibsi-10) · 实例 [4.9.6](sec-4-9-bond-order-analysis.md#496-用本征键强度指数ibsi衡量化学键强度)

## 子功能 11（主功能 200-19）：AV1245 / AVmin 大环芳香性指数

说明：AV1245（*Phys. Chem. Chem. Phys.*, **18**, 11839 (2016)）是 MCBO 的近似，用于量化大环芳香性：对环上保持 1,2,4,5 位置关系的所有 4c-ESI 求平均（4c-ESI 由带全排列的多中心键级 $I^{\mathrm{perm}}$ 经 $\mathrm{ESI}=2I^{\mathrm{perm}}/(n-1)!$ 得到；4c 时除以 3）。值越大离域越强。AVmin（*J. Phys. Chem. C*, **121**, 27118 (2017)）取所有 4c-ESI 的最小绝对值，定量整条路径的最低共轭程度（瓶颈）。Multiwfn 按常规密度/重叠矩阵方式算（比原文 AIM 划分便宜，结果偏小）；无弥散时原始基与 NAO 基结果几乎相同，有弥散时必须用 NAO 版。

菜单路径：主功能 `200` → `19` → 按连接顺序输入环原子序号（先输 `d` 可任意顺序输入，由程序按连接性自动推测；环中任一原子与两个以上环原子相连时不可用 `d` 模式）。

输入要求：原子坐标 + 基函数；NAO 版需带 `DMNAO` 的 NBO 输出（此时 `d` 模式不可用）。

操作步骤：进入 `200 → 19`，按顺/逆时针连接顺序输入环原子序号，回车后输出 AV1245、各 4c-ESI 与 AVmin（呈现时常乘以 1000）。

产出：AV1245、各 4c-ESI、AVmin（例：菲局域环、卟啉大环路径的定量比较）。

来源：[3.11.10](sec-3-11-bond-order-analysis.md#31110-av1245指数av1245-index大环的近似多中心键级approximate-multi-center-bond-order-for-large-rings和avmin) · 实例 [4.9.11](sec-4-9-bond-order-analysis.md#4911-用av1245和avmin指数研究芳香性的例子)

## 子功能 12：AIM 盆间离域指数 DI

说明：在 AIM 原子盆（电子密度划分的盆）之间算的离域指数是对两原子共享电子对数的定量，也可视为键级的一种度量。非极性键时与 Mayer/FBO 非常接近，极性键会明显偏低。盆模块（主功能 17）也能算 DI，但最直接的是本专用功能（均匀网格 + 原子中心积分网格）。

菜单路径：主功能 `9` → `12` → 选择网格质量。

输入要求：原子坐标 + 基函数。

操作步骤：进入 `9 → 12`，按提示选网格质量（质量越好开销越高、结果越准），等待积分完成即得 AIM 盆间离域指数表。

产出：原子对间离域指数（极性键数值偏低属正常）。

来源：[3.11.12](sec-3-11-bond-order-analysis.md#31112-aim盆aim-basins之间的离域指数delocalization-index-di)
