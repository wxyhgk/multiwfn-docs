# **6.3 内建原子密度的细节**

一些分析，如 Hirshfeld/ADCH 布居分析和 Hirshfeld 轨道成分分析，需要原子密度。虽然如第 [3.7.3](sec-3-7-custom-operation-promolecular-and-deformation-properties.md#373-原子波函数的生成-generation-of-atomic-wavefunctions) 节所示，原子密度可以基于原子的 .wfn 文件计算，但过程稍显复杂，即必须先准备好所需元素的 .wfn 文件并做球平均。为了简化这些分析任务，Multiwfn 提供了一套内建原子密度（从 H 到 Lr 均可用），可直接选择使用。

这些内建原子密度是在原子基态下以很高精度的计算水平得到的，并已做了球平均（许多原子基态的密度分布并非球对称）。序号 \<=18 的主族元素在 B3LYP/cc-pVQZ 水平下计算，序号 \>18 的在 B3LYP/ANO-RCC 水平下计算（Ca 除外，用的是 UGBS，因为 EMSL 网站上的 Ca 的 ANO-RCC 是错的，至少在我构建这些密度时是错的）。过渡金属在 HF/UGBS 水平下计算。镧系和锕系在 B3LYP/SARC-DKH 水平下计算（U 和 Np 除外，对它们用 ROHF 代替 B3LYP，因为 DFT 无法给出它们正确的基态构型）。对于所有比 Ar 重的元素，都采用 DKH2 方法考虑标量相对论效应。除非另有说明，开壳层体系均用非限制开壳层形式处理。

原子密度以径向点的形式记录在 *atmraddens.f90* 中，径向点的位置用第二类 Gauss-Chebyshev 方法生成，所有元素的点分布完全相同。任意一点的原子密度基于这些点用拉格朗日插值方法求得。

如果你想用自己计算的原子密度替换某个元素的内建原子密度，在启动 Multiwfn 并载入相应原子的波函数文件后，在主功能 100 中选择子功能 10（一个隐藏选项），Multiwfn 会计算径向电子密度并将结果输出到当前文件夹的 *sphavgval.txt* 中。你可以直接将该文件中的 Fortran 代码复制到 *atmraddens.f90* 的相应位置。
