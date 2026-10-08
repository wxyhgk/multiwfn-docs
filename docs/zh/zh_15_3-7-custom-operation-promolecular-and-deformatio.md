# 自定义操作、promolecular 与 deformation 性质（主功能 3、4、5 中的选项 0、-1、-2）

> Multiwfn manual, p.97–99.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.97 -->


格点数据至当前目录下的 .cub 文件。选择选项 3 则格点数据将导出至当前目录下的纯文本文件 output.txt。使用选项 4 无需进入 GUI 窗口拖动滑动条即可设置等值面数值，适用于批处理和命令行环境。利用选项 5~8，可分别对格点数据进行加、减、乘、除运算；之后，可使用选项 10 恢复至原始格点数据。

若只想可视化特定片段的等值面，可在后处理菜单中选择选项 9，然后输入该片段中原子的序号。此后，将在每个格点计算该片段的 Hirshfeld 权重，并乘到原始格点数据上。如此，远离该片段的格点的值将为零，从而不会显示在等值面图中。

特殊情形：为一组任意分布的点计算数据 若想用 Multiwfn 为一组点（可能任意分布）计算实空间函数值，在设置格点的界面中应选择“100 从外部文件载入一组点(Load a set of points from external file)”并输入记录这些点的纯文本文件的路径。文件中第一行应为所记录点的数目，其后为所有点的 X/Y/Z 坐标。例如，

```text
1902
   -3.3790050   -2.0484700    0.0274117
   -3.3844930   -1.9472468   -0.2500274
   -3.4064601   -1.9221635   -0.1287148
   -3.4118258   -1.9232203   -0.0003350
   -3.4059106   -1.9218280    0.1351179
....
```

坐标必须以 Bohr 为单位给出。格式为自由格式，可有多于四列的数据，但第四列之后的列将被直接忽略。

Multiwfn 将从该文件载入点的坐标，然后为它们计算函数值。最后，所有点的 X/Y/Z 坐标和函数值将被输出至纯文本文件，其路径由用户指定。

所需信息：原子坐标、GTFs（取决于实空间函数的选择）

## 3.7 自定义操作、promolecular 与 deformation 性质（主功能 3、4、5 中的选项 0、-1、-2）

### 3.7.1 多波函数的自定义操作 (0)

在主功能 3、4 和 5 中，有一个子功能允许为多个波函数设置自定义操作。支持的运算符包括 +（加）、−（减）、*（乘）、/（除），参与自定义操作的波函数数目没有上限。例如，若启动 Multiwfn 后载入的第一个波函数为 a.wfn，然后在自定义操作设置步骤中输入 2（即有两个波函数将被放入“自定义操作列表(custom operation list)”

<!-- p.98 -->


并从而依次与 a.wfn 进行运算），接着输入 -,b.wfn 和 *,c.wfn，则最终得到的性质将为 [(a.wfn 的性质) - (b.wfn 的性质)] * (c.wfn 的性质)。若感到困惑，可参阅 4.5.4 和 4.5.5 节的例子。

有时首次载入文件中的分子结构与随后载入文件中的不完全相同，你设置的格点是针对首次载入文件的，所有其他文件将共用相同的格点设置。

避免将自定义操作与主功能 -4、-3 和 6 联用，否则可能得到荒谬的结果。

### 3.7.2 Promolecular 与 deformation 性质 (-1, -2)

若在选择性质（即实空间函数）之前在主功能 3、4 或 5 中选择子功能 -1，则最终得到的是 promolecular 性质。Promolecular 性质是处于自由状态的原子的性质叠加

$$P^{\mathrm{pro}}(\mathbf{r})=\sum_{A}P_{A}^{\mathrm{free}}(\mathbf{r}-\mathbf{R}_{A})$$

若所选性质为电子密度，则 promolecular 性质一般称为 promolecular 密度

$$P^{\mathrm{pro}}(\mathbf{r})=\sum_{A}P_{A}^{\mathrm{free}}(\mathbf{r}-\mathbf{R}_{A})$$

这是一种人为的密度，对应于分子已形成但密度尚未弛豫时的状态。

Deformation 性质是相同几何下分子的实际性质与 promolecular 性质之差

$$P^{\mathrm{def}}\left(\mathbf{r}\right)=P^{\mathrm{mol}}\left(\mathbf{r}\right)-P^{\mathrm{pro}}\left(\mathbf{r}\right)$$

<!-- formula-ocr: formula_p98_043.png 已替换为LaTeX, 原图保留备查 -->

若性质选为电子密度，则 deformation 性质一般称为 deformation 密度或称电子成键电荷分布（BCD），对分析电荷转移和成键本质非常有用。Deformation 密度的应用例子可参见我的论文 Acta Phys. -Chim. Sin., 34, 503 (2018) 和 Angew. Chem. Int. Ed., 137, e202504895 (2025) DOI: 10.1002/anie.202504895。

### 3.7.3 原子波函数的生成

计算 promolecular 与 deformation 性质以及 Multiwfn 中的某些功能需要原子波函数文件，如计算 Hirshfeld、VDD 和 ADCH 电荷、模糊原子空间分析以及基于 Hirshfeld 划分的轨道成分分析等。生成原子 .wfn 文件的过程完全相同。

在选择子功能 -1 或 -2 研究 promolecular 与 deformation 性质后，Multiwfn 会检查当前目录的“atomwfn”子目录中是否已存在当前体系所涉及所有元素的 .wfn 文件，若没有，Multiwfn 会自动调用 Gaussian 生成缺失元素的 .wfn 文件并将其密度球化。若 Gaussian 可执行文件的路径（`settings.ini` 中的“gaupath”参数）不正确或未定义，Multiwfn

<!-- p.99 -->


将要求输入 Gaussian 可执行文件的路径。生成元素波函数的基组可由用户任意设置，但建议使用与分子波函数相同的基组。

新生成的元素波函数文件或从“atomwfn”目录取用的文件存放在当前目录的“wfntmp”子目录中。它们将被平移至当前体系中原子的实际位置，同时原子序号将被加到 .wfn 文件名中（如 "Cr 30.wfn"）。这些是直接用于计算 promolecular 与 deformation 性质的文件。

细节与技巧 若想避免每次都生成元素波函数，可将“wfntmp”目录中不带数字后缀的 .wfn 文件（如 C .wfn）移至“atomwfn”目录（若“atomwfn”目录不存在，请自行创建），下次若 Multiwfn 检测到“atomwfn”文件夹中已存在所有需要的元素 .wfn 文件，则将直接使用它们。Multiwfn 仅调用 Gaussian 计算缺失的元素 .wfn 文件。

“examples”目录下的“atomwfn”子目录包含前四周期所有元素的波函数文件，它们在 6-31G* 下生成，且已被球化。若想使用它们，只需将 "atomwfn" 目录复制到当前文件夹。

有一种快速生成前四周期所有元素波函数文件的方法：“examples\genatmwfn.pdb”文件包含前四周期的所有原子，将其载入 Multiwfn 并生成 promolecular 性质，待元素波函数计算完成后，将“wfntmp”目录中不带后缀的 .wfn 文件复制到“atomwfn”目录。

若你的体系涉及比 Kr 更重的元素，Multiwfn 无法通过调用 Gaussian 自动生成原子波函数文件并球化其密度；此时必须手动计算并球化原子波函数，然后放入“atomwfn”目录，Multiwfn 将直接使用它们。

为前四周期的主族元素（序号 1 至 20 及 31 至 36）生成波函数的默认理论方法为 ROHF，对于第四周期的过渡金属，使用 UB3LYP。一般而言，promolecular 与 deformation 性质对理论方法不敏感。若想自行指定理论方法，可同时输入理论方法和基组，以斜线分隔，例如 BLYP/6-311G*。不要加“RO”或“U”前缀，因为它们会被自动添加。若生成原子波函数时出错，请仔细检查“wfntmp”目录中的 Gaussian 输入与输出文件。

注意，Gaussian 允许的 .wfn 文件路径最大字符长度仅为 60！若长度超过此阈值，路径将被截断并导致错误。因此不要把 Multiwfn 放在路径过长的目录中！

### 3.7.4 原子波函数的球化

Multiwfn 支持 promolecular 与 deformation 性质的主要目的是生成 promolecular 与 deformation 密度，然而，大多数元素在自由基态下的电子密度不具球对称性，从而会导致取向依赖问题。为解决它，必须将原子电子密度球化。但球化没有唯一的方法。在 Multiwfn 中，通过人为修改原子波函数使原子电子密度球化，此处我描述其细节。若想跳过球化步骤，只需将 `settings.ini` 中的“ispheratm”设为 0。
