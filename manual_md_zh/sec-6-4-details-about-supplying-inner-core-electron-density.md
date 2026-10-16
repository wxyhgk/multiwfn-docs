# **6.4 关于为涉及赝势的波函数补充内层电子密度的细节**

在第 [2.5](sec-2-5-input-files-and-wavefunction-types.md) 节中，已经介绍了电子密度函数（electron density function，EDF）的特征与含义。EDF 信息用于表示被赝势（pseudopotential）取代的内层电子密度，使得对于涉及赝势的波函数，那些纯粹基于电子密度的波函数分析结果几乎可以与全电子波函数完全一致。

当你使用的输入文件包含 GTF 信息，同时部分原子使用了赝势时，Multiwfn 会自动从内置的 EDF 库中找到这些原子合适的 GTF 信息。内置 EDF 库由 Wenli Zou 及其合作者开发，最初作为 Molden2aim 程序（<https://github.com/zorkzou/Molden2AIM>）的一部分发布。该 EDF 库质量相当好，优于 Gaussian 程序产生的 .wfx 文件中所含的 EDF 字段。该 EDF 库覆盖整个元素周期表，直至序号 120。对于大多数元素，它同时包含大核与小核赝势的 EDF 信息。开发者关于该库的一些说明可见 <http://bbs.keinsci.com/thread-5354-1-1.html> 以及 *J. Comput. Chem.*, **39**, 1697 (2018)。如果你不希望 Multiwfn 自动从该库读取 EDF 信息，可将 *settings.ini* 中的 "isupplyEDF" 设为 0。

如第 [2.5](sec-2-5-input-files-and-wavefunction-types.md) 节所述，Gaussian 产生的 .wfx 文件在使用赝势时直接携带 EDF 字段。当使用这类文件作为输入时，Multiwfn 默认从该 .wfx 文件的 EDF 字段读取 EDF 信息，而不是从内置 EDF 库读取。如果你不希望 Multiwfn 从该文件读取 EDF 信息，而希望从内置 EDF 库读取，可将 *settings.ini* 中的 "readEDF" 从 1 改为 0。

值得注意的是，Multiwfn 还允许从 Gaussian 产生的原子 .wfx 文件读取 EDF 信息，而不使用 Multiwfn 的内置 EDF 库（该功能很少有用，因为如上所述，Multiwfn 内置 EDF 库的质量优于 Gaussian 内嵌的 EDF 库）。下面给出一个例子：

*examples\Pt(NH3)2Cl2.wfn* 是对应于 Pt(NH₃)₂Cl₂ 的文件，其中 Pt 和 Cl 使用 Lanl2 赝势及与其配套的 Lanl2DZ 基组，其它原子使用 6-31G\*。*examples\Pt_lanl2.wfx* 和 *examples\Cl_lanl2.wfx* 是由 Gaussian 09 产生的 Pt 和 Cl 原子 .wfx 文件，其中同样使用了 Lanl2，因此它们的 EDF 字段表示被 Lanl2 取代的 Pt 和 Cl 的内层电子密度。

为了在分析 *Pt(NH3)2Cl2.wfn* 时从原子 .wfx 文件借用 EDF 信息，首先需要将 *settings.ini* 中的 "isupplyEDF" 参数设为 1。然后启动 Multiwfn 并输入以下命令

```text
examples\Pt(NH3)2Cl2.wfn
Pt   // Load EDF information for element Pt
examples\Pt_lanl2.wfx   // Take EDF information of Pt from this file
Cl   // Load EDF information for element Cl
examples\Cl_lanl2.wfx   // Take EDF information of Cl from this file
q   // We have finished, exit
```

现在就可以像往常一样进行波函数分析。但最好先做一些测试，以检查内层电子密度是否已被正确表示，例如，我们在全空间对电子密度积分

```text
100   // 100 Other functions (Part1)
4   // Integrate a function over the whole space
1   // Electron density
```

结果为 132.00，即 Pt(NH₃)₂Cl₂ 应有的总电子数。假设我们没有载入 EDF 信息，则结果为 52.00，即 Pt(NH₃)₂Cl₂ 的价电子数。

注意，你也可以直接输入原子序号而不是元素名，例如，输入 *4,8-10,11* 表示选择当前体系中的原子 4、8、9、10、11。当然，每次选择的原子必须对应相同的元素和相同的赝势。

准备原子 .wfx 文件是用户的责任。由于赝势和元素的种类太多，显然，我无法为你提供全部文件。
