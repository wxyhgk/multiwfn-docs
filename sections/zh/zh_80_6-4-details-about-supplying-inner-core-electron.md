# 关于为涉及赝势的波函数补充内层芯电子密度的细节(Details about supplying inner-core electron density for

> Multiwfn manual, p.1156–1156.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.1156 -->



Chebyshev方法用于生成径向点的位置，所有元素的点分布都相同。任意点处的原子密度基于这些点用Lagrange插值方法求得。

如果你想用自己计算的密度替换某元素的内建原子密度，在启动Multiwfn并载入相应原子波函数文件后，选择主功能100中的子功能10（隐藏选项），然后Multiwfn将计算径向电子密度并将结果输出到当前文件夹下的sphavgval.txt中。你可以直接将该文件中的Fortran代码复制到atmraddens.f90的相应字段中。


### 6.4 关于为涉及赝势的波函数补充内层芯电子密度的细节(Details about supplying inner-core electron density for


### 涉及赝势的波函数(the wavefunctions involving pseudopotential))

在第2.5节(Section 2.5)中，已介绍了电子密度函数(EDF)的特征和含义。EDF信息用于表示被赝势取代的内芯密度，从而对于涉及赝势的波函数，纯粹基于电子密度的波函数分析结果几乎可以与全电子波函数完全相同。

当你使用的输入文件包含GTF信息，同时一些原子使用了赝势，Multiwfn会自动从内建EDF库中找到合适的GTF信息用于这些原子。内建EDF库由Wenli Zou及其合作者开发，最初作为Molden2aim程序的一部分发布（https://github.com/zorkzou/Molden2AIM）。该EDF库质量相当好，比Gaussian程序产生的.wfx文件中包含的EDF字段更好。该EDF库覆盖整个周期表，直至序号120。对于大多数元素，它同时包含大核和小核赝势的EDF信息。开发者关于该库的一些说明可在http://bbs.keinsci.com/thread-5354-1-1.html以及J. Comput. Chem., 39, 1697 (2018)中找到。如果你不想让Multiwfn自动从该库读取EDF信息，将`settings.ini`中的“isupplyEDF”设为0即可。

如第2.5节(Section 2.5)所述，当使用赝势时，Gaussian产生的.wfx文件直接带有EDF字段。当使用这类文件作为输入时，Multiwfn默认从该.wfx文件的EDF字段而不是从内建EDF库读取EDF信息。如果你不想让Multiwfn从该文件而是想从内建EDF库读取EDF信息，你可以将`settings.ini`中的“readEDF”从1改为0。

值得注意的是，Multiwfn还允许从Gaussian产生的原子.wfx文件而不是从Multiwfn的内建EDF库读取EDF信息（该功能很少有用，因为如上所述，Multiwfn内建EDF库的质量比Gaussian内嵌的EDF库更好）。下面提供一个例子：

examples\Pt(NH3)2Cl2.wfn是对应于Pt(NH3)2Cl2的文件，对Pt和Cl使用Lanl2赝势及Lanl2DZ基组，其他原子使用6-31G*。examples\Pt_lanl2.wfx和examples\Cl_lanl2.wfx是Gaussian 09产生的Pt和Cl原子.wfx文件，其中同样使用Lanl2，因此它们的EDF字段代表被Lanl2取代的Pt和Cl的内层芯电子密度。
