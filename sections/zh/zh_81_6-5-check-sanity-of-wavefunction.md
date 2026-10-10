# 检查波函数的合理性(Check sanity of wavefunction)

> Multiwfn manual, p.1157–1157.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.1157 -->



为了在Pt(NH3)2Cl2.wfn的分析中借用原子.wfx文件中的EDF信息，首先我们需要将`settings.ini`中的“isupplyEDF”参数设为1。然后启动Multiwfn并输入以下命令

examples\Pt(NH3)2Cl2.wfn Pt // 载入元素Pt的EDF信息(load EDF information for element Pt) examples\Pt_lanl2.wfx // 从该文件获取Pt的EDF信息(take EDF information of Pt from this file) Cl // 载入元素Cl的EDF信息(load EDF information for element Cl) examples\Cl_lanl2.wfx // 从该文件获取Cl的EDF信息(take EDF information of Cl from this file) q // 我们已完成，退出(we have finished, exit)现在我们可以像往常一样进行波函数分析。但最好先进行一些测试以检查内层芯电子密度是否已被正确表示，例如，我们在全空间对电子密度积分

!!! terminal "Multiwfn 交互"

    - **100** — 100 其他功能（第一部分）(Other functions (Part1))
    - **4** — 在全空间对函数积分(Integrate a function over the whole space)
    - **1** — 电子密度(Electron density)结果为132.00，即Pt(NH3)2Cl2预期的总电子数。假设我们没有载入EDF信息，则结果将为52.00，这只是Pt(NH3)2Cl2的价电子数。

注意你也可以直接输入原子序号而不是元素名，例如，输入4,8-10,11表示选择当前体系中的原子4,8,9,10,11。当然，你每次选择的原子必须对应于相同元素和相同赝势。

准备原子.wfx文件是用户的责任。由于赝势和元素的种类太多，显然，我无法为你提供所有文件。


### 6.5 检查波函数的合理性(Check sanity of wavefunction)

由各种量子化学程序生成的Multiwfn输入文件并不总是标准的。例如，许多程序产生的.molden文件在内容或格式上有问题。将它们输入Multiwfn后，若你想确认波函数是否已被正确载入，有两种有用的检查合理性的方法：

(1)进入主功能100并选择子功能4，然后选择电子密度。如果电子密度在全空间的积分非常接近实际电子数，则该波函数可直接使用。

(2)进入主功能1000（隐藏功能）并选择子功能100。该功能将检查所有轨道归一化条件的满足情况，并向你显示与1和整数的最大偏差。如果这两个最大偏差都明显大于零，则输入文件必定存在严重问题；如果其中任何一个非常接近于零，则输入文件应与Multiwfn完全兼容。因为如果输入的波函数文件包含基函数信息，在Multiwfn中相对于GTF和基函数的轨道系数都可用，在这种情况下该功能会要求你选择检查哪种轨道系数（当然，两者都应满足归一化条件）。
