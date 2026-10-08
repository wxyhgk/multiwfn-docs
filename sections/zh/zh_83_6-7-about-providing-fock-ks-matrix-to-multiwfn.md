# 关于向Multiwfn提供Fock/KS矩阵(About providing Fock/KS matrix to Multiwfn)

> Multiwfn manual, p.1159–1161.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.1159 -->



交换相关泛函，它也被Multiwfn用于许多波函数分析功能中，例如，计算Hirshfeld电荷和ADCH电荷、模糊原子空间分析（主功能15）等。

通过主功能1000的子功能93（隐藏功能），你可以将Becke算法的积分点导出到当前文件夹下的intpt.txt中。导出后各列的含义将在屏幕上明确显示。积分点的数量由`settings.ini`中的“radpot”和“sphpot”决定。角向格点的位置和权重由Lebedev方法决定，而径向格点的位置和权重由第二类Gauss-Chebyshev方法决定。

进入该功能后，Multiwfn会询问你是否同时输出Becke积分权重。如果你输入y，权重将被计算并一起输出。

所需信息(Information needed)：原子坐标

### 6.6.4 使轨道等同于基函数(Make orbitals equivalent to basis functions)

该功能是主功能1000的子功能15。通过该功能，你可以使轨道等同于基函数，轨道序号将对应于基函数序号。使用该功能后，你可以使用主功能0可视化基函数的等值面以了解它们的空间分布，你也可以使用主功能3和4分别为基函数绘制曲线图和平面图。

所需信息(Information needed)：基函数

### 6.6.5 生成前分子波函数(Generating promolecular wavefunction)

如果你想生成前分子波函数，从而可以研究各种前分子性质，你可以使用Multiwfn中专为此目的设的特殊功能：你应首先在启动时载入当前体系的实际波函数文件，然后进入主功能1000的子功能17。Multiwfn将为当前体系中的所有原子准备.wfn文件，情况与第3.7.3节(Section 3.7.3)中描述的完全相同。注意用于原子波函数文件的基组必须与用于当前体系实际波函数的基组完全相同。在成功生成前分子波函数后，如果你选择y，内存中的波函数信息将对应于前分子波函数。这意味着，例如，如果你通过主功能5中的常规步骤计算ELF格点数据，你最终将获得对应于前分子状态的ELF格点数据。


### 6.7 关于向Multiwfn提供Fock/KS矩阵(About providing Fock/KS matrix to Multiwfn)

Multiwfn的某些功能，如轨道定域化、双正交化以及ETS-NOCV分析，可以求得所得到新轨道的能量（即Fock或KS算符的期待值），然而这需要单电子有效Hamilton矩阵，即Fock或Kohn-Sham (KS)矩阵。此外，一些功能如绘制COHP需要这类矩阵。该矩阵可由Multiwfn基于轨道能量、展开系数和重叠矩阵直接生成，


<!-- p.1160 -->



然而你也可以让Multiwfn直接从文件载入该矩阵，以下文件可接受：

(1)包含Fock/KS矩阵的纯文本文件(Plain text file containing Fock/KS matrix)在该文件中，矩阵元应以下三角形式(lower-triangular form)记录，即文件结构应为（闭壳层情形）

F(1,1) F(2,1) F(2,2) F(3,1) F(3,2) F(3,3) ... F(nbasis,nbasis)其中nbasis为基函数总数，F为Fock/KS矩阵。对于非限制开壳层情形，文件应包含alpha和beta Fock/KS矩阵元（分别为Fa和Fb），以下三角形式记录，即

Fa(1,1) Fa(2,1) Fa(2,2) Fa(3,1) Fa(3,2) Fa(3,3) ... Fa(nbasis,nbasis) Fb(1,1) Fb(2,1) Fb(2,2) Fb(3,1) Fb(3,2) Fb(3,3) ... Fb(nbasis,nbasis)文件中数据的格式完全自由，只有数据个数是重要的。

Fock/KS矩阵可从量子化学程序的输出文件中获得。例如，你可以在Gaussian中使用IOp(5/33=3)或在GAMESS-US中使用NPRINT=5关键词在每个SCF循环中打印矩阵，然后你可以用自己的代码将最后一次打印的矩阵转换为上述格式。

值得注意的是，主功能100的子功能17能够基于当前轨道的能量和系数直接生成Fock/KS矩阵，并将矩阵以上述格式导出到纯文本文件，详见第3.100.17节(Section 3.100.17)。因此，只要你有包含分子轨道的波函数文件，你随时都可以获得带有Fock/KS矩阵的文件。

(2)NBO程序的.47文件(.47 file of NBO code)你可以让Gaussian产生.47文件，该文件是独立版NBO程序的输入文件。Multiwfn能够直接从该文件中的$FOCK字段读取Fock/KS矩阵。通过Gaussian生成.47文件很容易，只需运行如下输入文件：


```text
## B3LYP/6-31G* pop=nboread

Title line

0 1
[Atom coordinates]

$NBO archive file=C:\MY_FILE $END
```

然后一旦计算完成，将在C:\文件夹下生成MY_FILE.47，它带有B3LYP/6-31G*水平的Fock/KS矩阵。

(3)ORCA输出文件(ORCA output file)在ORCA输入文件中，如果你添加一行%output Print[P_Iter_F] 1，则每个SCF循环的Fock/KS矩阵都将被打印，Multiwfn将载入最后一次打印的矩阵，它对应于收敛波函数的矩阵。

(4).mwfn文件(.mwfn file)如第2.5节(Section 2.5)和我关于mwfn格式的介绍性论文，即ChemRxiv (2020) DOI: 10.26434/chemrxiv.11872524中所述，.mwfn文件能够带有Fock/KS矩阵。如果该类文件中


<!-- p.1161 -->



有该矩阵，Multiwfn可直接从这类文件载入Fock/KS矩阵。

(5)CP2K .csr文件(CP2K .csr file)CP2K能够将包括KS矩阵在内的各种矩阵导出到.csr文件。为了导出KS矩阵，在&FORCE_EVAL/&DFT节中添加以下行


```text
&PRINT
  &KS_CSR_WRITE
    REAL_SPACE T
    UPPER_TRIANGULAR T
    THRESHOLD 0
  &END KS_CSR_WRITE
&END PRINT
```

任务完成后，你将在当前文件夹下发现已导出包含KS矩阵的.csr文件。
