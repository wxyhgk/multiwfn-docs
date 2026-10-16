# **2.5 输入文件与波函数类型**

Multiwfn 支持的波函数 (wavefunction) 类型包括限制性/非限制性单行列式波函数、限制性开壳层波函数和 post-HF 波函数（自然轨道形式）。

支持角动量高达 *h* 的笛卡尔型或球谐型高斯函数。

Multiwfn 对原子数/基函数 (basis functions) 数/GTF 数/轨道数没有上限，实际上限只取决于你计算机的可用内存。

Multiwfn 根据文件扩展名判断输入文件类型。注意不同功能需要不同类型的信息，应选择合适类型的输入文件，见下表。例如，Hirshfeld 布居 (population) 分析用 GTF 表示的波函数就足够了，因此可用 .mwfn/.fch/.molden/.gms/.31\~.40/.wfn/.wfx 文件作输入，而 .pdb、.xyz、.mol 等不携带任何波函数信息，不能使用；相反，用 promolecular 近似产生 RDG 函数的格点数据只需要原子坐标，因此所有支持的文件格式都可用（纯文本文件除外）。每个功能对信息类型的要求通常在[第 3 章](3-functions.md)的功能介绍中说明，或……

<table style="width: auto; margin-left: auto; margin-right: auto;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th rowspan="2" style="text-align: center;">File Format</th>
<th colspan="5" style="text-align: center;">Provided information types</th>
</tr>
<tr>
<th style="text-align: center;">Basis functions</th>
<th style="text-align: center;">GTFs</th>
<th style="text-align: center;">Atom coordinates</th>
<th style="text-align: center;">Grid data</th>
<th style="text-align: center;">Atomic charges</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">.fch/.fchk/.chk</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
</tr>
<tr>
<td style="text-align: center;">.mwfn, .molden, .gbw, .gms</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
</tr>
<tr>
<td style="text-align: center;">NBOplot file (.31 to .40)</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
</tr>
<tr>
<td style="text-align: center;">.wfn and .wfx</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
</tr>
<tr>
<td style="text-align: center;">.pdb, .xyz, .mol/sdf, .mol2, .gro, .cif, .mop,<br />
Gaussian/ORCA input/output file,<br />
CP2K input/restart file, POSCAR, Quantum ESPRESSO input file<br />
Turbomole coordination file</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
</tr>
<tr>
<td style="text-align: center;">.chg and .pqr</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">√</td>
</tr>
<tr>
<td style="text-align: center;">.cub/.cube<br />
CHGCAR/CHG/ELFCAR/LOCPOT</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">×</td>
</tr>
<tr>
<td style="text-align: center;">.vti, .grd, .dx</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">×</td>
</tr>
<tr>
<td style="text-align: center;">Others (plain text file)</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
</tr>
</tbody>
</table>

> **关于幽灵原子 (ghost atom)**
>
> 在下面介绍的任何波函数格式中，都允许出现幽灵原子（带基函数但没有核电荷的点）。它们的元素序号应为 0，如果文件格式记录元素名，幽灵原子的元素名应为 Bq。Multiwfn 按常规方式从文件中读取它们的核电荷，但它们作为幽灵原子，核电荷原则上应为零。

**Multiwfn 波函数文件 (.mwfn)：**该格式自 Multiwfn 3.7 起定义并支持，是用于波函数存储和交换的最理想格式。该文件以严格、简洁、紧凑且可扩展的格式记录了波函数分析所需的全部信息。该格式的介绍和定义已在我的论文中详细描述：*ChemRxiv* (2020) DOI: [10.26434/chemrxiv.11872524](https://doi.org/10.26434/chemrxiv.11872524)。

**AIM 波函数文件 (.wfn)：**该格式最初由 Bader 的 AIMPAC 程序引入，目前被许多主流量子化学软件支持，如 Gaussian、ORCA、GAMESS-US/UK、Firefly、Q-Chem 和 NWChem。.wfn 文件中的信息包括原子坐标、元素、轨道能量、占据数、笛卡尔型高斯型函数 (GTF) 的展开系数。GTF 支持的角动量高达 *f*。wfn 文件不含任何虚轨道。.wfn 文件的产生方法在[第 4 章](4-tutorials-and-examples.md)开头有说明。

> **注**
>
> 虽然原始 .wfn 格式正式不支持角动量为 g 和 h 的 GTF，但如果 g 和 h 型 GTF 按以下方式记录，Multiwfn 也能够识别："TYPE ASSIGNMENT" 中的 21\~35 分别对应 YZZZ、XYYY、XXYY、XYZZ、YZZZ、XYYZ、XXXX、XXXY、XZZZ、XXYZ、XXXZ、XXZZ、YYYY、YYYZ、ZZZZ；36\~56 分别对应 ZZZZZ、YZZZZ、YYZZZ、YYYZZ、YYYYZ、YYYYY、XZZZZ、XYZZZ、XYYZZ、XYYYZ、XYYYY、XXZZZ、XXYZZ、XXYYZ、XXYYY、XXXZZ、XXXYZ、XXXYY、XXXXZ、XXXXY、XXXXX。这里所示的顺序实际上也是 Molden2AIM 和自 B.01 起的 Gaussian09 输出的 .wfn 所用的顺序。

**AIM 扩展波函数文件 (.wfx)：**这是作为 .wfn 扩展而引入的格式，自 B.01 修订版起被 Gaussian 09 支持。相对于 .wfn 格式，.wfx 支持更高的数据记录精度和无限高的 GTF 角动量。该格式最特殊之处是新增的电子密度函数 (EDF) 段，即用多个 GTF 来表示使用了有效核势 (ECP) 的波函数的内层芯电子密度。因此，对使用 ECP 的波函数做电子密度分析的结果与全电子波函数的结果几乎一致。目前 Multiwfn 中支持 EDF 的实空间函数 (real space functions) 包括：电子密度及其梯度和 Laplacian、局域信息熵 (local information entropy)、约化密度梯度 (reduced density gradient) 以及 *Sign*(*λ*₂(**r**))。同时电子密度及其 Laplacian 的拓扑分析也考虑了 EDF。**注意 EDF 信息既不影响 ESP，也不影响依赖波函数的实空间函数（*例如*动能密度、ELF）。如果你想分析重元素的这些性质，应使用全电子基组，至少用小核 ECP**。目前 EDF 段中唯一支持的 GTF 类型是 S 型（实际上 S 型足以拟合内层密度，因为内层密度近似球对称）。与 .wfn 一样，Multiwfn 不允许 .wfx 文件中出现虚轨道。

Multiwfn 内置了强大的 EDF 库，取自 Wenli Zou 开发的 Molden2aim 程序。**只要输入文件含有 GTF 信息（例如 .fch、.wfn、.molden、.gms……），Multiwfn 总是自动从该库为使用 ECP 的原子加载 EDF 信息**。只有当你用 .wfx 文件作输入且 .wfx 本身已含有 EDF 段时，才会从 .wfx 文件而非 EDF 库加载 EDF 信息。更多细节见[附录 4](sec-6-4-details-about-supplying-inner-core-electron-density.md)。

注意，虽然 Gaussian 之外的一些程序也能产生 .wfx 文件（*例如* ORCA），但这些 .wfx 文件无法提供 EDF 段。

> **注意**
>
> 对于某些版本的 Gaussian（*例如* G09 B.01），我发现极少数情况下 .wfx 中记录的 EDF 段是有问题的，即 EDF 段表示的电子数与 ECP 实际对应的芯电子数不等。为了验证 EDF 段是否正确，可用主功能 100 的子功能 4 求全空间电子密度的积分，若结果约等于总电子数（芯电子+价电子），则说明 EDF 段正确。

**Gaussian 格式化 checkpoint 文件 (.fch/.fchk)：**Gaussian 程序的 checkpoint 文件 (.chk) 可通过 Gaussian 包中的 *formchk* 工具转换为格式化 checkpoint 文件 (.fch/.fchk)。.fch 与 .fchk 没有区别，"fch"（"fchk"）是 Windows（Linux）版 *formchk* 生成的默认扩展名。

如果你想让 Multiwfn 能直接加载 .chk 文件，必须把 *settings.ini* 中的 "formchkpath" 设为 Gaussian 包中 formchk 可执行文件的实际路径。此时 Multiwfn 会自动调用 formchk 把 .chk 文件转换为 .fch/fchk 文件，若转换成功则加载 .fch/fchk，加载完毕后自动删除。

.fch/.fchk 比 .wfn/.wfx 文件含有更丰富的信息，还记录了虚轨道波函数，同时为 Multiwfn 提供基函数信息。如果你想用 .fch/.fchk 文件作为 post-HF 波函数的载体，请仔细阅读[第 4 章](4-tutorials-and-examples.md)开头！

Q-Chem 和 PSI4 产生的 .fchk 文件也可用作 Multiwfn 的输入文件。（如果 .fchk 文件是由较老版本的 Q-Chem 产生的，必须把 *settings.ini* 中的“ifchprog”设为 2；若你的 Q-Chem 版本等于或新于 5.0，则不需要这样做）。

**Molden 输入文件 (.molden 或 .molden.input 或 molden.inp)：**目前 Molpro、Molcas、ORCA、Q-Chem、CFour、Turbomole、PSI4、MRCC 和 NWChem 等多种量子化学软件，以及第一性原理程序 CP2K，都能产生 Molden 可视化程序的输入文件。这类文件记录原子坐标、基组定义、全部占据和虚轨道的信息（包括基函数的展开系数、占据数、自旋、能量和对称性），同时没有只针对 Molden 的信息。所以实际上 Molden 输入文件可视为交换波函数信息的标准通用文件格式。对 Multiwfn 而言，这类文件可提供原子坐标、基函数信息和 GTF 信息。

注意很多程序产生的 Molden 输入文件很不规范！**目前 Multiwfn 只正式支持由 Molpro、ORCA、xtb、Dalton、NWChem（仅球谐函数且关闭对称性时）、MRCC（仅球谐函数时）、deMon2k、BDF、CP2K（仅球谐函数时）产生的 Molden 输入文件**。如果你用的 Molden 输入文件由其它程序产生，分析结果可能正确也可能不正确，应先用[附录 5](sec-6-5-check-sanity-of-wavefunction.md)中介绍的方法检查波函数是否被正确加载。

> **提示**
>
> Multiwfn 完全支持经 molden2aim 工具标准化后的 Molden 输入文件（细节见 [5.1](sec-5-1-make-multiwfn-support-more-quantum-chemistry-programs.md) 节），该工具能正确识别许多其它量子化学程序（如 CFOUR 和 Molcas）产生的 Molden 输入文件。

.molden 文件正式只支持高达 g 角动量的基函数。不过主功能 100 的子功能 2 可产生含 *h* 函数的 .molden 文件，Multiwfn 随后可正常加载。即使出现 *h* 函数，Multiwfn 也能正常加载 ORCA 和 Dalton 产生的 .molden 文件。

虽然 Molden 输入文件也支持 Slater 型轨道 (STO)，但 Multiwfn 只能利用记录高斯型基函数的 Molden 输入文件。

Molden 格式的一个严重缺点是它不像 wfn 和 fch 等其它格式那样显式记录核电荷，因此使用 ECP 时依赖核电荷的结果（*例如*静电势 (electrostatic potential) 和原子电荷）会有问题。为解决此问题，Multiwfn 把文件中的原子序号（即 \[Atoms\] 段第三列）当作核电荷加载，因此若你手动把原子序号改为量子化学计算中显式表示的原子价电子数（相当于有效核电荷），结果就是正确的。如果你对此感到困惑，请看这个帖子：<http://sobereva.com/wfnbbs/viewtopic.php?pid=721>。或者，你可以在文件开头手动插入 \[Nval\] 段来显式指定特定元素的价电子数；例如，下面几行要求 Multiwfn 把 Na 和 Cl 的价电子数分别设为 9 和 7，而其它元素保持不变。

```text
[Nval]
Na 9
Cl 7
```

值得注意的是，如果你用的是 ORCA >=6.0，不需要对 molden 文件做上述修改，因为 ORCA 导出的 molden 文件含有 \[Pseudo\] 段，给出了带 ECP 原子的正确核电荷，Multiwfn 会自动加载（此时 molden 文件的标题行必须含有 *orca* 字样，Multiwfn 才能认出它是由 ORCA 产生的）。

用 Molden 输入文件作波函数载体的另一个明显缺点是该格式不如 .mwfn 和 .fch 紧凑。因此对同一波函数，.molden 文件的加载速度比 .mwfn 和 .fch 慢得多。所以，如果需要频繁分析一个 .molden 文件，建议用主功能 100 的子功能 2 把它转换为 .mwfn 格式。

一些量子化学程序产生 Molden 输入文件的方法在[第 4 章](4-tutorials-and-examples.md)开头有介绍。如果你是 ORCA 用户，不想经 ORCA 中的 orca_2mkl 工具手动把 .gbw 文件转换为 Molden 输入文件，可把 *settings.ini* 中的 "orca_2mklpath" 设为 ORCA 文件夹中 orca_2mkl 可执行文件的实际路径，这样 Multiwfn 就能直接加载 .gbw 文件。

> **PS**
>
> 关于 .molden 格式的详细说明可在 Molden 官网找到：<https://www3.cmbi.umcn.nl/molden/molden_format.html>。

**GAMESS-US 或 Firefly 输出文件 (.gms)：**如果想用 GAMESS-US 或 Firefly（原名 PC-GAMESS）的输出文件作输入文件，可把其扩展名改为 .gms，Multiwfn 就能正确识别。目前我只能保证用默认 NPRINT 选项的 HF/DFT/TDDFT 计算的输出文件能被 Multiwfn 正常加载。如果点群不是 C1，Multiwfn 将无法处理该输出文件。

.gms 的作用类似于 .molden 和 .fch 文件，*即*它们都提供原子坐标、GTF 和基函数信息。

> **注**
>
> 由于我不是经验丰富的 Firefly 用户，不能保证对 Firefly 输出文件的兼容性与 GAMESS-US 输出文件一样好。对前者我只测试过 DFT 单点任务和 TDDFT 任务。

**NBO 程序的绘图文件 (.31\~.40)：**支持这些文件类型的主要目的是可视化 PNAO/NAO/PNHO/NHO/PNBO/NBO/PNLMO/NLMO/MO（它们的轨道系数分别记录在 .32\~.40 中），.31 记录基函数信息。启动 Multiwfn 后，应先输入 .31 文件的路径，再输入 .32\~.40 其中之一的路径（为简便，若文件名相同可只输入后缀）。

注意 NBO 程序产生的各类轨道中，只有用 NBO 或 NLMO 计算实空间函数才有意义！

**Protein data bank 格式 (.pdb)、.xyz、MDL Molfile (.mol/sdf)、.mol2：**这些是记录原子坐标最常用的格式。它们不携带任何波函数信息，但对只需要原子坐标的功能来说，用这类文件作输入就足够了。.mol 和 .mol2 相对于 .pdb 和 .xyz 的一个优点是它们含有原子连接表，一些 Multiwfn 功能需要它，*例如* EEM 原子电荷的计算。如果 .xyz 文件含有多个构象帧，只加载第一帧。

注意 Multiwfn 支持的 .mol 文件是 V2000 版，能记录的原子数和键数上限都是 999。关于 .mol 格式的更多说明可在 <https://en.wikipedia.org/wiki/Chemical_table_file> 找到。.sdf 文件只是带附加信息的 .mol 文件的外包装。

> **注**
>
> 在标准的 .xyz 文件中，每个原子的名称就是元素名。但 VMD 基于某些分子动力学程序轨迹导出的 .xyz 文件用的是模拟中的原子名，此时 Multiwfn 不总能从原子名正确识别实际元素，因此 Multiwfn 中有专门规则来规避此问题：如果与输入的 .xyz 文件同名的 .pdb 文件在同一文件夹下存在，就改用 .pdb 文件中的元素名（但若某原子在 .pdb 文件中缺失元素名，Multiwfn 仍会从 .xyz 文件的原子名猜测元素）。

**.pqr 文件：**该格式与 .pdb 格式很相似，但内容不同。在原子 X/Y/Z 坐标对应列之后，还有两列分别记录原子电荷和原子半径（这两列的小数位数不重要，各字段必须以空白分隔）。这类文件可为 Multiwfn 提供原子信息和原子电荷信息。下面是水的 .pqr 文件示例。REMARK 段可用于记录注释，加载文件时会跳过。

```text
REMARK From file m1charges.out
REMARK ESP charges
ATOM      1 O    O 1     1       0.000   0.123   0.000 -0.680698  2.9000
ATOM      2 H    O 1     1       0.757  -0.490   0.000  0.340338  2.6000
ATOM      3 H    O 1     1      -0.757  -0.490   0.000  0.340361  2.6000
```

**电荷文件 (.chg)：**这种纯文本文件可由 Multiwfn 的一些功能（*例如*布居分析功能）产生，含有元素名（不超过两个字符）、原子坐标（前三列，单位为 Å）和电荷（第四列），用户可手动修改。该文件是自由格式，所有字段必须以空白分隔。该文件可提供原子电荷信息，主要用途是基于原子电荷在分子表面上可视化静电势并分析之，也可用主功能 7 的子功能 -2 以 .chg 作输入文件计算基于原子电荷的静电相互作用能。加载 .chg 文件时，屏幕上会显示全部原子电荷之和，以及用原子电荷算得的电偶极矩。

下面给出水分子的 .chg 文件示例：

```text
  O     0.000000    0.000000    0.119308   -0.301956
  H     0.000000    0.758953   -0.477232    0.150977
  H     0.000000   -0.758953   -0.477232    0.150977
```

**.gro 文件：**GROMOS 结构格式。这类文件最常用于 GROMACS 分子动力学程序。.gro 文件只能为 Multiwfn 提供原子信息。注意该文件记录的是原子名而非元素，加载时 Multiwfn 会根据原子名和残基名自动猜测实际元素。但有时猜测的元素可能是错的，因此建议加载文件后检查打印的分子式。

**.cif 文件：**这是记录晶体结构的标准格式。文件中必须显式给出对称操作，否则无法生成等效原子的位置。

**Gaussian-type cube 文件 (.cub 或 .cube)：**这是最流行的体积数据格式，可由众多计算化学软件产生，能被大多数分子图形程序识别。该文件中可记录原子坐标、一套实空间函数的格点数据或多套分子轨道的格点数据。把 cube 文件载入 Multiwfn 后，可选主功能 0 可视化等值面，或用主功能 13 处理格点数据。

**.vti、.dx 和 DMol3 格点文件 (.grd)**

.vti 是 "ParaView VTK Image Data" 格式，可记录标量场和矢量场。这类文件可由*例如* GIMIC 2.0 和 ParaView 程序产生。只支持含 ASCII 型标量数据的 .vti 文件。简单说，该文件与 .cub 文件很相似，只是不含原子信息。

.dx 是可由*例如* VMD 的 Volmap 插件导出的体积数据格式。

.grd 文件是 DMol3 程序主要用的体积数据格式，不记录原子信息。

**Gaussian 输入文件 (.gjf)、ORCA 输入文件和 MOPAC 输入文件 (.mop)：**这些文件可为 Multiwfn 提供原子坐标信息以及 α 和 β 电子数信息。注意原子必须用笛卡尔坐标记录。.gjf 还可经“Tv”字段为 Multiwfn 提供晶胞信息。

**Gaussian 和 ORCA 输出文件**

Gaussian 和 ORCA 输出文件可为 Multiwfn 提供原子信息。

- Gaussian 输出文件：当 *settings.ini* 中的 "iloadGaugeom" 设为 1（默认，加载输入取向）或 2（加载标准取向）时，Multiwfn 会从该文件加载（最终）几何和电子数。
- ORCA 输出文件：当 *settings.ini* 中的 "iloadORCAgeom" 设为 1（默认）时，Multiwfn 会从该文件加载（最终）几何。

**CP2K 输入和 restart 文件 (.inp 和 .restart)：**这些文件可为 Multiwfn 提供原子坐标信息和晶胞信息。注意原子必须用 Å 为单位的笛卡尔坐标记录。

**Quantum ESPRESSO 输入 (.inp 或 .in)：**可为 Multiwfn 提供原子坐标信息和晶胞信息。只支持 ibrav=0。

**Turbomole coordination 文件：**若纯文本文件的第一行为 &coord，就会被当作 Turbomole coordination 文件加载。*\$coord* 段提供原子信息。若有 *\$periodic* 和 *\$lattice*，还会提供晶胞信息。

**VASP 相关文件**

以下文件与 VASP 程序相关。Multiwfn 能加载它们，文件名必须含有相应字符串且没有 .in 或 .inp 扩展名。例如，要把一个文件当作 POSCAR 加载，文件名可以是 POSCAR_Si8 和 MOF.POSCAR。

- POSCAR：VASP 的输入文件之一，记录晶胞和原子信息。
- CHGCAR 或 CHG：该文件记录 VASP 产生的电子密度。自旋极化时还同时记录自旋密度
- ELFCAR：该文件记录 VASP 产生的 ELF。自旋极化时分别记录 α 和 β 电子的 ELF。
- LOCPOT：该文件记录 VASP 产生的一个电子感受到的外势。自旋极化时分别记录 α 和 β 电子的势。若 LVHAR=.TRUE.，该势对应静电势的负值；而若 LVHAR=.FALSE.，它对应“分子中一个电子感受到的势”（PAEM，见 [2.7](sec-2-7-user-defined-real-space-function.md) 节）。

**纯文本文件：**该文件类型只用于特殊功能，如绘制 DOS 图、绘制光谱、产生带初猜的 Gaussian 输入文件。见相应章节的说明。
