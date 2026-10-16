# **6.7 关于向 Multiwfn 提供 Fock/KS 矩阵**

Multiwfn 的一些功能，如轨道定域化（orbital localization）、双正交化（biorthogonalization）、ETS-NOCV 分析，可以计算所得新轨道的能量（*即* Fock 或 KS 算符的期望值），但这需要单电子有效哈密顿矩阵，即 Fock 或 Kohn-Sham (KS) 矩阵。此外，一些功能如绘制 COHP 也需要这类矩阵。该矩阵可由 Multiwfn 根据轨道能量、展开系数和重叠矩阵直接生成，你也可以让 Multiwfn 直接从文件载入该矩阵，以下文件是可接受的：

## **(1) 包含 Fock/KS 矩阵的纯文本文件**

在该文件中，矩阵元应以下三角形式记录，即文件结构应为（闭壳层情形）

$F(1,1)$ $F(2,1)$ $F(2,2)$ $F(3,1)$ $F(3,2)$ $F(3,3)$ ... $F(nbasis,nbasis)$

其中 *nbasis* 是基函数总数，**F** 为 Fock/KS 矩阵。对于非限制性开壳层情形，文件应包含 alpha 和 beta 的 Fock/KS 矩阵元（分别为 $F_a$ 和 $F_b$），均以下三角形式记录，即

$F_a(1,1)$ $F_a(2,1)$ $F_a(2,2)$ $F_a(3,1)$ $F_a(3,2)$ $F_a(3,3)$ ... $F_a(nbasis,nbasis)$\
$F_b(1,1)$ $F_b(2,1)$ $F_b(2,2)$ $F_b(3,1)$ $F_b(3,2)$ $F_b(3,3)$ ... $F_b(nbasis,nbasis)$

文件中数据的格式完全自由，只有数据个数是重要的。

Fock/KS 矩阵可从量子化学程序的输出文件中获得。例如，可在 Gaussian 中使用 *IOp(5/33=3)* 或在 GAMESS-US 中使用 *NPRINT=5* 关键词以在每个 SCF 循环中打印该矩阵，然后用自己的代码将最后一次打印的矩阵转换为上述格式。

值得注意的是，主功能 100 的子功能 17 能够根据当前轨道的能量和系数直接生成 Fock/KS 矩阵，并将该矩阵以上述格式导出到纯文本文件，细节见第 [3.100.17](sec-3-100-other-functions-part-1.md#310017-基于轨道能量和系数生成fockks矩阵generate-fockks-matrix-based-on-orbital-energies-and-coefficients) 节。因此，只要你有一个包含分子轨道的波函数文件，随时都可以得到载有 Fock/KS 矩阵的文件。

## **(2) NBO 程序的 .47 文件**

可让 Gaussian 产生 .47 文件，它是独立版 NBO 程序的输入文件。Multiwfn 能够直接从该文件的 \$FOCK 域读取 Fock/KS 矩阵。通过 Gaussian 生成 .47 文件很容易，只需运行如下的输入文件：

```text
# B3LYP/6-31G* pop=nboread

Title line

0 1
[Atom coordinates]

$NBO archive file=C:\MY_FILE $END
　
　
```

计算完成后将在 C: 目录下生成 *MY_FILE.47*，它载有 B3LYP/6-31G\* 水平的 Fock/KS 矩阵。

## **(3) ORCA 输出文件**

在 ORCA 输入文件中，若加入一行 *%output Print\[P_Iter_F\] 1*，则每个 SCF 循环的 Fock/KS 矩阵都会被打印，Multiwfn 将载入最后一次打印的矩阵，它对应于收敛波函数的矩阵。

## **(4) .mwfn 文件**

如第 [2.5](sec-2-5-input-files-and-wavefunction-types.md) 节以及我关于 mwfn 格式的介绍性论文，即 *ChemRxiv* (2020) DOI: [10.26434/chemrxiv.11872524](https://doi.org/10.26434/chemrxiv.11872524) 所述，.mwfn 文件能够携带 Fock/KS 矩阵。若文件中含有该矩阵，Multiwfn 可直接从这类文件载入 Fock/KS 矩阵。

## **(5) CP2K .csr 文件**

CP2K 能够将包括 KS 矩阵在内的各种矩阵导出到 .csr 文件。要导出 KS 矩阵，在 &FORCE_EVAL/&DFT 部分加入以下行

```text
&PRINT
  &KS_CSR_WRITE
    REAL_SPACE T
    UPPER_TRIANGULAR T
    THRESHOLD 0
  &END KS_CSR_WRITE
&END PRINT
```

任务完成后，你会在当前目录下发现已导出的包含 KS 矩阵的 .csr 文件。
