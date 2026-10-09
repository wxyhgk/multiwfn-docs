# 图形格式与图像尺寸（Graphic formats and image size）

> Multiwfn manual, p.70–76.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.70 -->



## 2.8 图形格式与图像尺寸（Graphic formats and image size）

Multiwfn支持许多主流图形格式，包括：1 Postscript (ps) 2 Encapsulated postscript (eps) 3 Portable document format (pdf) 4 Windows metafile format (wmf) 5 Graphics interchange format (gif) 6 TIFF (tiff) 7 Portable network graphics (png) 8 Windows bitmap format (bmp) 9 Scalable vector graphics (svg) Multiwfn导出的图片的图形格式由`settings.ini`中的“graphformat”参数控制，可将此参数设为上面括号中的文本，默认格式为“png”。

曲线图的图像高和宽由`settings.ini`中的“graph1Dsize”参数控制。“graph2Dsize”负责二维数据绘图（填充色图、等高线图、浮雕图等）。“graph3Dsize”负责三维数据绘图（等值面图、分子结构图等）。

提示1：若图形主要由线条组成，如等高线图和曲线图，最佳格式为pdf和svg。但若需将结果图嵌入Office，通常应用wmf格式。

提示2：若想使导出图像文件的背景透明，请看此视频说明：https://youtu.be/E7lAGac3aDM。


## 2.9 周期体系的分析（Analysis of periodic systems）

Multiwfn能处理周期体系，细节将在本节给出。要分析周期体系的波函数，既可用量子化学程序产生的团簇模型波函数，也可用CP2K程序产生的周期波函数，分别见2.9.1节和2.9.2节所述。Multiwfn中有许多分析与波函数无关，对周期体系应用它们的特别注意见2.9.3节。

### 2.9.1 基于团簇模型波函数的波函数分析

可将晶体原胞扩展为大超胞，再从超胞中截取团簇。基于此团簇，可用任何量子化学程序做优化或单点任务，再像往常一样在Multiwfn中分析所得波函数。当然，为最小化有限团簇尺寸带来的人为边界效应，团簇应足够大。若不确定最小可接受尺寸，可对结果做相对团簇尺寸的收敛测试。重要的是，团簇边界原子的电子结构不应纳入讨论，因为不可避免的边界效应使其必然无意义。

若晶体结构由X射线衍射实验确定，应始终对氢位置做优化，因为X射线衍射通常不能准确定位氢。

若原子位置由实验以满意的分辨率确定，应忽略重原子（即非氢原子）的几何优化。但若想研究表面反应或吸附，或研究晶体内部反应，应冻结边界重原子以模拟体相环境，同时优化团簇中心区域以体现反应或吸附对几何的影响。

有四种常见晶体类型，评论如下：

- 分子晶体：这是最简单的情况。4.12.6节示例了如何从尿素晶体中截取尿素团簇，可仿此构建其它团簇。用团簇模型分析分子晶体波函数的好例子是J. Comput. Chem., 33, 580 (2012)图6，其中对基于B3LYP/6-31G**波函数的尿素团簇做了约化密度梯度分析。另一例子：“基于背景电荷计算晶体环境中分子的吸收光谱”（http://sobereva.com/579）。

- 金属晶体：利用此模型的例子见我的博客文章：“基于团簇模型用量子化学程序计算金属表面吸附”（http://sobereva.com/540）。不建议用团簇模型研究d区和f区金属，因为相应团簇的自洽场很难收敛，且易收敛到不稳定波函数。

- 共价晶体：石墨烯和金刚石是典型例子，应以氢饱和边界原子以避免悬挂键，否则当前体系的电子结构高度人为。当然，所加氢的位置应优化。好例子是Mater. Sci. Eng. B, 273, 115425 (2021) DOI: 10.1016/j.mseb.2021.115425，用Multiwfn研究了cyclo[18]carbon与石墨烯片段的相互作用。

- 离子或半离子晶体：NaCl和TiO2是典型情形。此类晶体需特别注意以正确处理边界效应。通常应用嵌入团簇模型，如下所述。首先确定合适尺寸的量子化学处理区域（称QM区域）。区域越大，结果常越好，但越贵。QM区域周围应加数层处于晶格位点的点电荷作背景电荷，以模拟QM原子与环境原子的静电相互作用。环境原子的点电荷值可选氧化态，而有更好但更复杂的方式经迭代过程确定，见Inorg. Chem., 58, 9303 (2019)。此外，紧邻QM区域的一层环境原子应加相应元素的有效核势（ECP，不带基函数），称为capped ECP (cECP)，此很薄的区域被视为缓冲区域。缓冲区域的存在是为避免电子从QM区域向邻近点电荷的正Coulomb奇点溢出，当QM区域带负电时非常重要。关于上述嵌入团簇模型见Inorg. Chem., 58, 9303 (2019)和J. Chem. Theory Comput., 16, 6950 (2020)，前篇论文的SI提供了ORCA输入文件示例。另见Surface Sci., 471, 21


<!-- p.71 -->


结果相对团簇尺寸。若晶体结构由X射线衍射实验确定，应始终优化氢的位置，因为X射线衍射通常无法准确定出氢。

若原子位置由实验以满意分辨率确定，应忽略重原子（即非氢原子）的几何优化。但若想研究表面反应或吸附，或研究晶体内部反应，应冻结边界重原子以模拟体相环境，同时优化团簇中心区域以体现反应或吸附对几何的影响。

有四种常见晶体类型，评论如下（接上页，此段为原文重复排版，此处保留译文以保持页标记对应）：

- 分子晶体、金属晶体、共价晶体、离子/半离子晶体的处理同前所述，嵌入团簇模型需QM区域、外围点电荷背景与capped ECP缓冲层，详见Inorg. Chem., 58, 9303 (2019)、J. Chem. Theory Comput., 16, 6950 (2020)及Surface Sci., 471, 21

<!-- p.72 -->


(2001)的另一应用。注意避免电子溢出问题的另一种方式是用Gaussian电荷分布表示环境原子，称为静电势的Gaussian展开（GEEP），CP2K的QM/MM处理支持，见J. Chem. Theory Comput., 1, 1176 (2005)。

### 2.9.2 基于周期波函数的波函数分析

要直接用Multiwfn分析周期波函数，应使用免费高效的CP2K程序（https://www.cp2k.org）对周期体系做计算，细节如下。目前除CP2K外Multiwfn不支持其它第一性原理程序。Gaussian程序周期计算产生的.fch/fchk文件也被完全支持，但无实用价值，因为Gaussian中的周期计算极慢。

### 2.9.2.1 生成.molden波函数文件

注：关于此话题的更多信息与讨论，见“用CP2K产生供Multiwfn用的molden格式波函数文件”（http://sobereva.com/651，中文）

CP2K导出的.molden文件可用作Multiwfn输入文件。为生成它，应在输入文件的$DFT字段中加入以下内容


```text
    &PRINT
      &MO_MOLDEN
        NDIGITS 9
      &END MO_MOLDEN
    &END PRINT
```

计算后将在当前文件夹得到.molden文件。

·CP2K ≥ 2026.2用户 若体系周期性，还在&MO_MOLDEN字段中插入WRITE_CELL T，要求CP2K将晶胞信息以[Cell]字段写入.molden文件。

若用赝势，还插入WRITE_PSEUDO T，要求CP2K将每个原子的实际价电子数以[Pseudo]字段写入.molden文件。

·CP2K < 2026.2用户 应编辑文件以手动在文件开头加入晶胞信息，例如


```text
[Molden Format]
[Cell]
7.13358000    0.00000000    0.00000000
0.00000000    7.13358000    0.00000000
0.00000000    0.00000000    7.13358000
 [Atoms] AU
 C        1       4       0.000000       0.000000       0.000000
 C        2       4       1.685064       1.685064       1.685064
 C        3       4       0.000000       3.370128       3.370128
```


<!-- p.73 -->



```text
...ignored
```

高亮的三行分别对应晶胞的三平移矢量（亦称晶胞矢量），以Å为单位。支持任何类型晶胞，晶胞不一定正交。

为方便，也可用晶胞长度（a、b、c）和晶胞角（α、β、γ）表示晶胞信息。例如，以下内容定义a = 15 Å、b = 13 Å、c = 18.5 Å、α = 90°、β = 90°、γ = 121.3°。


```text
[Cell]
15 13 18.5 90 90 121.3
```

此外，若不想修改.molden文件，也可在文本文件中提供晶胞信息（三行三晶胞矢量，或一行六晶胞参数），命名为[Cell].txt并放在当前文件夹。当.molden文件中找不到[Cell]而当前文件夹检测到[Cell].txt时，Multiwfn会问是否从中载入晶胞信息。

若用了赝势，建议将原子的元素序号改为实际价电子数，以便研究电子密度及其导数时自动用适当的电子密度函数（EDF）表示内层芯电子密度（详见附录4），Multiwfn也能正确计算原子电荷，这就是上例中“C”后的第二项由元素序号（6）改为4的原因。若觉得逐个修改每个原子太麻烦，可用[Nval]字段手动指定特定元素的价电子数，例如


```text
...ignored
0.00000000    7.13358000    0.00000000
0.00000000    0.00000000    7.13358000
[Nval]
C 4
O 6
 [Atoms] AU
...ignored
```

生成金刚石2×2超胞.molden文件的CP2K输入文件示例已提供为examples\PBC\CP2K_diamond_2x2_DZVP-MOLOPT.inp。

### 2.9.2.2 分析周期波函数可用的功能

目前Multiwfn中正式支持周期波函数的功能有限，以下功能已测试，发现对周期体系工作良好，其它功能可能正常也可能不正常。未来更多功能将正式支持周期波函数。

- 查看轨道（主功能（main function）0）
- 计算某点性质（主功能（main function）1）
- 拓扑分析（主功能（main function）2）
- 对实空间函数绘制曲线图（主功能（main function）3），包括promolecular和deformation（变形）性质

- 对实空间函数绘制平面图（主功能（main function）4），包括promolecular和


<!-- p.74 -->


deformation（变形）性质

- 计算格点数据并对实空间函数绘制等值面图（主功能（main function）5），包括promolecular和deformation（变形）性质。注意非正交晶胞时，等值面图在Multiwfn中不能正确绘制，但可将格点数据导出为cube文件再在VMD和VESTA中可视化

- 原子电荷与布居分析：Hirshfeld、Hirshfeld-I、MBIS、CM5、1.2*CM5、Mulliken布居、Löwdin布居、各种修正Mulliken布居、PEOE (Gasteiger)、EEM和AIM（经盆分析模块）

- 用Mulliken、Stout-Politzer、SCPA和Hirshfeld方法的轨道成分分析，包括显示片段贡献（主功能（main function）8中的子功能（subfunctions）1-6）

- 计算氧化态的LOBA/mLOBA方法
- 键级分析：Mayer键级、Wiberg键级、Mulliken键级及其分解分析、轨道占据微扰Mayer键级、fuzzy键级

- 电子离域与芳香性分析：多中心键级、HOMA、HOMAc、HOMER、Bird、AV1245

- 绘制TDOS、PDOS、OPDOS、LDOS、MO-PDOS和COHP（主功能（main function）10）
- 电荷分解分析（CDA）
- 用Mulliken或Löwdin布居的Pipek-Mezey轨道定域（主功能（main function）19）

- 弱相互作用的可视化分析（IGMH、mIGM、amIGM、aIGM、IGM、IRI、NCI、aNCI、DORI）。

- 电子激发分析：电子-空穴分析（hole和electron分布、transition密度和transition偶极矩密度、与质心无关的各种指标包括ghost-hunter指数）、IFCT分析、NTO分析、产生并导出transition密度矩阵、计算Mulliken原子transition电荷、产生激发态自然轨道、“检查、修改并导出激发的组态系数”、打印所有激发态的主要MO跃迁、CTS分析

- 模糊原子空间分析：在模糊原子空间中对实空间函数积分、计算AOM、计算LI、DI、片段LI、IFDI、PDI、FLU、FLU-π、CLRK、PLR。支持Hirshfeld、Hirshfeld-I和MBIS划分。

- 其它：在全空间积分函数；双正交化；NAdO和BOD分析 静电势（ESP）分析尚不支持！因为Multiwfn无法基于波函数信息直接计算ESP。

### 2.9.2.3 分析周期波函数的相关参数

`settings.ini`中有一些与周期波函数和结构分析相关的参数，如下。注意对非正交晶胞，上面提到的X、Y、Z实际指第一、第二、第三维度。

- ifdoPBCxyz：其三个值分别控制在输入文件提供晶胞信息时X、Y、Z是否考虑周期性。例如，若“ifdoPBCxyz”设为1,1,0，则Z方向的周期性被完全忽略。

- PBCnxnynz：其三个值分别控制X、Y、Z考虑多少邻近镜像。例如，若“PBCnxnynz”设为1,1,1，则计算中考虑相对当前晶胞所有方向+1和-1邻近镜像晶胞。“当前晶胞”指所考虑位置或原子所在的晶胞。默认


<!-- p.75 -->


1,1,1通常合适，无特殊理由不应更改。原则上，增大该值会使结果更准确但显著增加代价。

- expcutoff_PBC：为降低计算实空间函数时指数项的代价，若发现exp(x)的x小于此参数，则跳过计算。默认值为速度与准确性的良好平衡。显然，增大此参数会使结果变差但降低代价。

关于研究一维和二维体系的注：若想研究平行于XY平面的二维体系，高度建议将“ifdoPBCxyz”设为1,1,0，则不考虑Z方向周期性，计算代价也降低。类似，对Z方向周期的一维体系，建议将“ifdoPBCxyz”设为0,0,1。

关于CP2K计算的非常重要注：Multiwfn不考虑k点采样，即CP2K计算只应包含gamma点。因此，晶胞尺寸应足够大以避免需考虑k点采样。

若晶胞很小，例如金刚石的常规晶胞，尺寸约3.5 Å，最好将上述“PBCnxnynz”参数设为2,2,2，否则结果略不准确。

若你想用的分析方法与弥散函数不兼容，如Mayer键级和Mulliken布居分析，绝不应使用含强弥散特征基函数的基组，否则结果非物理。据我测试，DZVP-GTH通常不可接受，而MOLOPT-SR-GTH系列基组是好的选择。

### 2.9.3 周期体系的其它分析

Multiwfn中有些功能与波函数无关，只需原子信息或格点数据，如独立梯度模型（IGM）分析、promolecular近似下的约化密度梯度（RDG）分析、Hirshfeld表面分析、配位数计算。此时，可用CP2K、Quantum ESPREESO、Abinit和VASP等任何第一性原理程序优化晶体或表面，再将所得几何转为Multiwfn支持的任何文件格式（例如.xyz、.pdb、.mol2）作输入文件。

目前，这类功能中只有少数显式支持考虑周期边界条件（PBC），如下（换言之，其它功能简单将当前体系视为孤立体系）：

- 可视化几何与格点数据（主功能（main function）0）
- 处理格点数据（主功能（main function）13），包括绘制（局域）积分曲线
- 基于promolecular密度的RDG/NCI分析、独立梯度模型（IGM）、修正IGM (mIGM)、平均IGM (aIGM)、平均mIGM (amIGM)

- 范德华势分析（主功能（main function）20的子功能（subfunction）6）
- 色散能的原子贡献与色散密度分析（3.24.4节）
- 评估原子间连接性与原子配位数（主


<!-- p.76 -->


功能（main function）100的子功能（subfunction）9）

- 计算空腔直径（见3.100.21节所述）
- 对多孔体系可视化自由区域并计算自由体积（主功能（main function）300的子功能（subfunction）1）

- 绘制分子表面距离投影图（主功能（main function）300的子功能（subfunction）8）
- 域分析（主功能（main function）200的子功能（subfunction）14）
- 计算键长/键级交替（BLA/BOA）（主功能（main function）200的子功能（subfunction）9）注意上节提到的“ifdoPBCxyz”参数也影响周期体系的几何分析结果。

### 2.9.4 可向Multiwfn提供晶胞信息的文件

为在上述功能中显式考虑PBC，需要晶胞信息。以下文件可向Multiwfn提供晶胞信息

- .cif文件
- 按2.9.2节修改的CP2K产生的.molden文件
- 含“Ndim”字段且Ndim>0的.mwfn文件
- 含“CRYST1”字段的.pdb和.pqr文件
- GROMACS/GROMOS程序的.gro文件
- 含“@<TRIPOS>CRYSIN”字段的.mol2文件
- 含“Tv”（平移矢量）信息的Gaussian输入文件
- Gaussian PBC计算产生的.fch/fchk文件
- CP2K输入文件或restart文件
- VASP程序的POSCAR、CHGCAR、CHG、ELFCAR、LOCPOT文件
- .xyz文件。原始格式没有记录晶胞信息的字段，但可在该文件第二行手动加入晶胞信息以向Multiwfn提供晶胞信息。例如，第二行以下内容定义三平移矢量为（7.426 0.0 0.0）、（-3.66 6.40 0.0）和（0.0 0.0 10.0）Å：


```text
Tv_1: 7.426 0.0 0.0 Tv_2: -3.66 6.40 0.0 Tv_3: 0.0 0.0 10.0
```

或者，在第二行可用与扩展xyz格式（“Lattice”标签）相同的方式记录晶胞信息，例如


```text
Lattice="7.426 0.0 0.0 -3.66 6.40 0.0 0.0 0.0 10.0"
```

- .wfn文件。原始格式没有记录晶胞信息的字段，但可在文件末尾手动加入如下晶胞信息。该字段含三晶胞矢量，格式与上述CP2K文件中[Cell]字段相同，单位为Å。


```text
[Cell]
 9.901    0.0     0.0
-4.879   8.534   0.0
 0.0    0.0    10.0
```

若有晶胞信息，主功能（main function）100的子功能（subfunction）2导出的这些文件也携带晶胞信息：.mwfn、.molden、.pdb、.pqr、.xyz、.fch、.gjf、.wfn、CP2K输入文件。

## Multiwfn

> 结构显示、点/线/面性质输出、波函数检查、布居分析、轨道成分、键级、DOS、光谱

> 英文原文见同目录 `03_功能3.2-3.13.md`｜图片目录：`../mw_imgs/`

---
