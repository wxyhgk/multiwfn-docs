# Multiwfn的文件（Files of Multiwfn）

> Multiwfn manual, p.34–40.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.34 -->



## 2.3 Multiwfn的文件（Files of Multiwfn）

解压Multiwfn压缩包后会看到以下文件，只有加粗的文件是运行Multiwfn所必需的：

- Multiwfn.exe（Windows）或Multiwfn（Linux/Mac OS）：Multiwfn的可执行文件。
- libiomp5md.dll（Windows）：Intel OpenMP Runtime库。
- `settings.ini`：记录了运行Multiwfn的所有详细参数，其中大多数无需经常修改。启动时，Multiwfn会先尝试在当前文件夹中查找并使用此文件，若当前文件夹中没有，则使用由“Multiwfnpath”环境变量定义的路径中的文件；若仍找不到，则使用默认设置。若通过命令行运行Multiwfn，还可通过“-set”参数直接指定此文件的位置，例如：Multiwfn test.wfn -set /sob/3.7/settings.ini。

`settings.ini`中所有参数的含义在本手册中没有系统说明，因为它们已有详细注释，本手册只提及重要的参数。建议通读`settings.ini`，找出对你有用的参数。

- “examples”文件夹：一些有用的文件、脚本以及第4章例子中涉及的文件。

- LICENSE.txt：所有用户必须遵守的条款。
- Multiwfn quick start.pdf：一份简短文档，让新用户能立即了解如何用Multiwfn完成非常常见的任务。

- How to cite Multiwfn.pdf：请按此文档正确引用Multiwfn。


## 2.4 并行实现（Parallel implementation）

Multiwfn中大多数耗时的代码已用OpenMP技术并行化。若你的CPU有多核，可从并行化中大大受益。要启用并行化，只需将`settings.ini`中的“nthreads”参数改为合适的数值。例如，你的计算机CPU有12个物理核心，那么通常应将“nthreads”改为12。

若在对非常大的体系进行并行计算时Multiwfn崩溃，请尝试增大`settings.ini`中的“ompstacksize”（Windows版）或增大环境变量OMP_STACKSIZE的值（Linux或Mac OS版）。


## 2.5 输入文件与波函数类型（Input files and wavefunction types）

Multiwfn支持的波函数类型包括限制性/非限制性单行列式波函数、限制性开壳层波函数和后HF波函数（自然轨道形式）。

支持角动量最高至h的Cartesian或球谐Gaussian函数。

Multiwfn对原子数/基函数数/GTF数/轨道数没有上限，实际上限仅取决于你计算机的可用内存。


<!-- p.35 -->


Multiwfn根据文件扩展名判断输入文件类型。注意不同功能需要不同类型的信息，应选择合适类型的输入文件，见下表。例如，Hirshfeld布居只需GTF表示的波函数，因此可用.mwfn/.fch/.molden/.gms/.31~.40/.wfn/.wfx文件作输入，而.pdb、.xyz、.mol等不携带任何波函数信息，故不能使用；相反，用promolecular近似生成RDG函数的格点数据只需原子坐标，因此所有支持的文件格式都可用（纯文本文件除外）。每种功能对信息类型的要求通常在第3章相应小节末尾以红色文字说明。

关于ghost原子：在下面所述的任何波函数格式中，都允许出现ghost原子（有基函数但无核电荷的点）。其元素序号应为0，若文件格式记录元素名，ghost原子元素名应为Bq。其核电荷由Multiwfn按常规方式从文件中载入，但原则上它们应为零，因为是ghost原子。

Multiwfn波函数文件（.mwfn）：该格式自Multiwfn 3.7起定义并支持，是最理想的波函数存储与交换格式。此文件以严格、简洁、紧凑且可扩展的格式记录了波函数分析所需全部信息。该格式的介绍与定义已在我的论文中详细描述：ChemRxiv (2020) DOI: 10.26434/chemrxiv.11872524。

AIM波函数文件（.wfn）：该格式最早由Bader的AIMPAC程序引入，目前被许多主流量子化学软件支持，如Gaussian、ORCA、GAMESS-US/UK、Firefly、Q-Chem和NWChem。.wfn文件中的信息包括原子坐标、元素、轨道能量、占据数、Cartesian型Gaussian函数（GTF）的展开系数。支持的GTF角动量最高至f。.wfn


| 文件格式（File Format） | GTFs | 基函数 | 原子坐标 | 网格数据 | 原子电荷 |
| --- | --- | --- | --- | --- | --- |
| .fch/.fchk/.chk | √ | √ | √ | × | × |
| .mwfn, .molden, .gbw, .gms | √ | √ | √ | × | × |
| NBO plot文件（.31至.40） | × | √ | √ | × | × |
| .wfn和.wfx | × | √ | √ | × | × |
| .pdb, .xyz, .mol/sdf, .mol2, .gro, .cif, .mop,<br/>Gaussian/ORCA输入/输出文件，<br/>CP2K输入/restart文件，POSCAR，<br/>Quantum ESPRESSO输入文件<br/>Turbomole coordination文件 | × | × | √ | × | × |
| .chg和.pqr | × | × | √ | × | √ |
| .cub/.cube<br/>CHGCAR/CHG/ELFCAR/LOCPOT | × | × | √ | √ | × |
| .vti, .grd, .dx | × | × | × | √ | × |
| 其它（纯文本文件） | × | × | × | × | × |

<!-- p.36 -->

文件中不含任何虚轨道。.wfn文件的生成方法见第4章开头。

注：虽然原始.wfn格式正式不支持g和h角动量的GTF，但若按以下方式记录g和h型GTF，Multiwfn也能识别：在“TYPE ASSIGNMENT”中21~35分别对应YZZZ、XYYY、XXYY、XYZZ、YZZZ、XYYZ、XXXX、XXXY、XZZZ、XXYZ、XXXZ、XXZZ、YYYY、YYYZ、ZZZZ；36~56分别对应ZZZZZ、YZZZZ、YYZZZ、YYYZZ、YYYYZ、YYYYY、XZZZZ、XYZZZ、XYYZZ、XYYYZ、XYYYY、XXZZZ、XXYZZ、XXYYZ、XXYYY、XXXZZ、XXXYZ、XXXYY、XXXXZ、XXXXY、XXXXX。此处所示顺序实际上也是Molden2AIM和Gaussian09自B.01版以来输出的.wfn所用的顺序。

AIM扩展波函数文件（.wfx）：这是作为.wfn扩展引入的格式，自B.01版起被Gaussian 09支持。相对于.wfn格式，.wfx支持更高的数据记录精度和无限高的GTF角动量。该格式最特殊之处是新增的电子密度函数（EDF）字段，即用多个GTF表示使用了有效核势（ECP）的波函数的内层芯电子密度。因此，对使用ECP的波函数做电子密度分析的结果与全电子波函数的结果几乎一致。目前Multiwfn中支持EDF的实空间函数包括：电子密度及其梯度和Laplacian、局域信息熵、约化密度梯度以及Sign(λ2(r))。同时电子密度及其Laplacian的拓扑分析也考虑EDF。注意EDF信息既不影响ESP，也不影响依赖波函数的实空间函数（如动能密度、ELF）。若想分析重元素的这些性质，应使用全电子基组，至少用小核ECP。目前EDF字段中唯一支持的GTF类型是S型（实际上S型已足以拟合内层密度，因为其近似球对称）。与.wfn一样，Multiwfn不允许.wfx文件中出现虚轨道。

Multiwfn内置了强大的EDF库，取自Wenli Zou开发的Molden2aim程序。只要输入文件含有GTF信息（例如.fch、.wfn、.molden、.gms……），Multiwfn总会自动从该库为使用ECP的原子载入EDF信息。只有当你用.wfx文件作输入且.wfx本身已含EDF字段时，才从.wfx文件而非EDF库载入EDF信息。详见附录4。

注意，尽管Gaussian之外的一些程序（如ORCA）也能生成.wfx文件，但这些.wfx文件无法提供EDF字段。

注意：对于某些版本的Gaussian（例如G09 B.01），我发现极少数情况下记录在.wfx中的EDF字段是有问题的，即EDF字段表示的电子数与ECP实际表示的芯电子数不等。为验证EDF字段是否正确，可用主功能（main function）100的子功能（subfunction）4对全空间总电子密度积分，若结果约等于总电子数（芯电子+价电子），则说明EDF字段正确。

Gaussian格式化checkpoint文件（.fch/.fchk）：Gaussian程序的checkpoint文件（.chk）可用Gaussian包中的formchk工具转为格式化checkpoint文件（.fch/.fchk）。.fch与.fchk没有区别。“fch”（“fchk”）是Windows（Linux）版formchk生成的默认扩展名。

若想让Multiwfn能直接载入.chk文件，必须将`settings.ini`中的“formchkpath”设为Gaussian包中formchk可执行文件的实际路径。此时Multiwfn会自动调用formchk将.chk文件转为.fch/fchk文件，若转换成功则载入.fch/fchk，载入完毕后自动删除。

.fch/.fchk比.wfn/.wfx文件含有更丰富的信息，记录了虚轨道波函数，同时为Multiwfn提供基函数信息。若想用.fch/.fchk文件作后HF波函数的载体，请仔细阅读第4章开头！


<!-- p.37 -->


由Q-Chem和PSI4生成的.fchk文件也可用作Multiwfn输入文件。（若.fchk文件由较旧版Q-Chem生成，必须将`settings.ini`中的“ifchprog”设为2。若你的Q-Chem版本等于或新于5.0，则无需此操作）。

Molden输入文件（.molden或.molden.input或molden.inp）：目前多种量子化学软件包，如Molpro、Molcas、ORCA、Q-Chem、CFour、Turbomole、PSI4、MRCC和NWChem，以及第一性原理程序CP2K，都能产生Molden可视化程序的输入文件。该类文件记录原子坐标、基组定义、所有占据和虚轨道的信息（包括基函数的展开系数、占据数、自旋、能量和对称性），同时没有仅对Molden专用的信息。因此，Molden输入文件实际上可视为交换波函数信息的标准通用文件格式。对Multiwfn而言，该类文件可提供原子坐标、基函数信息和GTF信息。

注意，很多程序产生的Molden输入文件很不标准！目前Multiwfn仅正式支持由Molpro、ORCA、xtb、Dalton、NWChem（仅球谐函数且关闭对称性时）、MRCC（仅球谐函数）、deMon2k、BDF、CP2K（仅球谐函数）生成的Molden输入文件。若你用的Molden输入文件由其它程序生成，分析结果可能正确也可能不正确，应先用附录5所述方法检查波函数是否被正确载入。

提示：Multiwfn完全支持经molden2aim工具标准化后的Molden输入文件（详见5.1节），该工具能正确识别由CFOUR、Molcas等许多其它量子化学程序生成的Molden输入文件。

.molden文件正式仅支持最高至g角动量的基函数。但主功能（main function）100的子功能（subfunction）2可生成含h函数的.molden文件，Multiwfn随后可正常载入。即使出现h函数，Multiwfn也能正常载入由ORCA和Dalton生成的.molden文件。

虽然Molden输入文件也支持Slater型轨道（STO），但Multiwfn只能利用记录Gaussian型基函数的Molden输入文件。

Molden格式的一个严重缺点是它不像wfn和fch等其它格式那样显式记录核电荷，因此使用ECP时依赖核电荷的结果（如静电势和原子电荷）会有问题。为解决此问题，Multiwfn将文件中的原子序号（即[Atoms]字段第三列）作为核电荷载入，因此若你手动将原子序号改为量子化学计算中显式表示的原子价电子数（相当于有效核电荷），结果即正确。若对此有疑问，请查看此帖：http://sobereva.com/wfnbbs/viewtopic.php?pid=721。或者，可在文件开头手动插入[Nval]字段以显式指定特定元素的价电子数；例如，以下几行要求Multiwfn将Na和Cl的价电子数分别设为9和7，其它元素保持不变。


```text
[Nval]
Na 9
Cl 7
```


<!-- p.38 -->


值得注意的是，若你使用ORCA >=6.0，则无需对molden文件做上述修改，因为ORCA导出的molden文件含有[Pseudo]字段，为使用ECP的原子提供了正确的核电荷，Multiwfn会自动载入（此时molden文件的标题行必须含有orca字样，以便Multiwfn能识别它由ORCA生成）。

用Molden输入文件作波函数载体的另一个明显缺点是该格式不如.mwfn和.fch紧凑。因此，对同一波函数，.molden文件的载入速度远慢于.mwfn和.fch。若需频繁分析.molden文件，建议用主功能（main function）100的子功能（subfunction）2将其转为.mwfn格式。

部分量子化学程序生成Molden输入文件的方法见第4章开头。若你是ORCA用户，不想手动通过ORCA中的orca_2mkl工具将.gbw文件转为Molden输入文件，可将`settings.ini`中的“orca_2mklpath”设为ORCA文件夹中orca_2mkl可执行文件的实际路径，Multiwfn即可直接载入.gbw文件。

PS：关于.molden格式的详细说明见Molden官网：https://www3.cmbi.umcn.nl/molden/molden_format.html。

GAMESS-US或Firefly输出文件（.gms）：若想用GAMESS-US或Firefly（原名PC-GAMESS）输出文件作输入文件，可将其扩展名改为.gms，Multiwfn即可正确识别。目前，我只能保证默认NPRINT选项下HF/DFT/TDDFT计算的输出文件能被Multiwfn正常载入。若点群不是C1，Multiwfn将无法处理该输出文件。

.gms的作用类似于.molden和.fch文件，即都提供原子坐标、GTF和基函数信息。

由于我不是有经验的Firefly用户，不能保证与Firefly输出文件的兼容性像GAMESS-US输出文件那样好。对前者我仅测试过DFT单点任务和TDDFT任务。

NBO程序的plot文件（.31~.40）：支持这些文件类型的主要目的是可视化PNAO/NAO/PNHO/NHO/PNBO/NBO/PNLMO/NLMO/MO（其轨道系数分别记录在.32~.40中），.31记录基函数信息。启动Multiwfn后，应先输入.31文件的路径，再输入.32~.40中某一个文件的路径（若文件名相同，为简便可只输入后缀）。

注意，NBO程序产生的所有类型轨道中，只有用NBO或NLMO计算实空间函数才有意义！

Protein Data Bank格式（.pdb）、.xyz、MDL Molfile（.mol/sdf）、.mol2：这些是记录原子坐标最广泛使用的格式。它们不携带任何波函数信息，但对只需原子坐标的功能，用这类文件作输入已足够。.mol和.mol2相对于.pdb和.xyz的一个优点是它们含有原子连接表，Multiwfn的少数功能需要它，例如EEM原子电荷的计算。若.xyz文件含多帧，只载入第一帧。

注意，Multiwfn支持的.mol文件是V2000版本，可记录的最大原子数和键数均为999。关于.mol格式的更多说明见https://en.wikipedia.org/wiki/Chemical_table_file。.sdf文件只是附加了额外信息的.mol文件的包装。


<!-- p.39 -->


在标准.xyz文件中，每个原子的名称即元素名。但基于某些分子动力学程序轨迹由VMD导出的.xyz文件用的是模拟中的原子名，此时Multiwfn不总能从原子名正确识别实际元素，因此Multiwfn中有特殊规则规避此问题：若与输入的.xyz文件同名的.pdb文件在同一文件夹中存在，则改用.pdb文件中的元素名（但若.pdb文件中某原子缺失元素名，Multiwfn仍会从.xyz文件中的原子名猜测元素）。

.pqr文件：该格式与.pdb格式很相似，但内容不同。在原子X/Y/Z坐标对应列之后，还有两列分别记录原子电荷和原子半径（这两列的小数位数不重要，各字段必须以空白符分隔）。该类文件可向Multiwfn提供原子信息和原子电荷信息。下面是水的.pqr文件示例。REMARK字段可用于记录注释，载入文件时会跳过。


```text
REMARK From file m1charges.out
REMARK ESP charges
ATOM      1 O    O 1     1       0.000   0.123   0.000 -0.680698  2.9000
ATOM      2 H    O 1     1       0.757  -0.490   0.000  0.340338  2.6000
ATOM      3 H    O 1     1      -0.757  -0.490   0.000  0.340361  2.6000
```

电荷文件（.chg）：这类纯文本文件可由Multiwfn的某些功能（如布居分析功能）生成，含有元素名（不超过两个字符）、原子坐标（前三列，以Å为单位）和电荷（第四列），用户可手动修改。该文件为自由格式，所有字段必须以空白符分隔。此文件可提供原子电荷信息，主要用途是基于原子电荷可视化静电势并在分子表面上分析它，也可用主功能（main function）7的子功能（subfunction）-2以.chg作输入评估基于原子电荷的静电相互作用能。载入.chg文件时，屏幕上会显示所有原子电荷之和以及用原子电荷计算的电偶极矩。

下面给出水分子的.chg文件示例：


```text
  O     0.000000    0.000000    0.119308   -0.301956
  H     0.000000    0.758953   -0.477232    0.150977
  H     0.000000   -0.758953   -0.477232    0.150977
```

.gro文件：GROMOS结构格式。该类文件最常用于GROMACS分子动力学程序。.gro文件只能为Multiwfn提供原子信息。注意由于该文件记录的是原子名而非元素，载入时Multiwfn会根据原子名和残基名自动猜测实际元素，但有时猜测的元素可能不正确，因此建议载入文件后检查打印的分子式。

.cif文件：这是记录晶体结构的标准格式。文件中必须显式给出对称操作，否则无法生成等价原子的位置。

Gaussian型cube文件（.cub或.cube）：这是最流行的体积数据格式，可由众多计算化学软件生成，能被大多数分子图形程序识别。该文件中可记录原子坐标、一套实空间函数的格点数据或多套分子轨道的格点数据。cube文件被


<!-- p.40 -->


载入Multiwfn后，可选主功能（main function）0可视化等值面，或用主功能（main function）13处理格点数据。

.vti、.dx和DMol3格点文件（.grd）.vti是“ParaView VTK Image Data”格式，可记录标量场和矢量场。该类文件可由例如GIMIC 2.0和ParaView程序生成。仅支持含ASCII型标量数据的.vti文件。简言之，该文件与.cub文件很相似，但没有原子信息。

.dx是例如VMD的Volmap插件可导出的体积数据格式。.grd文件是DMol3程序主要用的体积数据格式。.grd中不记录原子信息。

Gaussian输入文件（.gjf）、ORCA输入文件和MOPAC输入文件（.mop）：这些文件可向Multiwfn提供原子坐标信息以及α和β电子数信息。注意原子必须以Cartesian坐标记录。.gjf还可通过“Tv”字段向Multiwfn提供晶胞信息。

Gaussian和ORCA输出文件 Gaussian和ORCA输出文件可为Multiwfn提供原子信息。

- Gaussian输出文件：当settings.ini中的“iloadGaugeom”设为1（默认，载入input orientation）或2（载入standard orientation）时，Multiwfn将从该文件载入（最终）几何构型和电子数。

- ORCA输出文件：当settings.ini中的“iloadORCAgeom”设为1（默认）时，Multiwfn将从该文件载入（最终）几何构型。

CP2K输入和restart文件（.inp和.restart）：这些文件可向Multiwfn提供原子坐标信息和晶胞信息。注意原子必须以Å为单位的Cartesian坐标记录。

Quantum ESPRESSO输入（.inp或.in）：可向Multiwfn提供原子坐标信息和晶胞信息。仅支持ibrav=0。

Turbomole coordination文件：若纯文本文件的第一行为&coord，则将其作为Turbomole coordination文件载入。\$coord字段提供原子信息。若有\$periodic和$lattice，还提供晶胞信息。

VASP相关文件 以下文件与VASP程序相关。Multiwfn能载入它们，文件名必须包含相应字符串且没有.in或.inp扩展名。例如，要作为POSCAR载入，文件名可如POSCAR_Si8和MOF.POSCAR。

- POSCAR：VASP的输入文件之一，记录晶胞和原子信息。
- CHGCAR或CHG：该文件记录VASP产生的电子密度。自旋极化时，同时记录自旋密度

- ELFCAR：该文件记录VASP产生的ELF。自旋极化时，分别记录
