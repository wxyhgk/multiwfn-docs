# 前言与输入文件的生成

> Multiwfn manual, p.458–460.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.458 -->




## 4 教程与实例


## 前言与输入文件的生成

欢迎使用 Multiwfn！如果你还没有阅读本手册第 2 页的“ALL USERS MUST READ”，请先阅读。如果你在使用 Multiwfn 过程中遇到任何问题，欢迎在 Multiwfn 论坛发帖求助。

在开始之前，我首先向你展示如何生成各种输入文件。注意 Multiwfn 中的不同功能需要不同类型的输入文件，详见 2.5 节。简而言之，对于任何仅基于实空间函数的分析，你都可以使用 .wfn 或 .wfx 作为输入文件。然而，许多功能需要基函数信息，在这种情况下你必须使用 .mwfn、.fch/fchk、.molden 或 .gms 文件作为输入文件。由于这些文件比 .wfn/wfx 文件包含更丰富的信息（即基函数和虚轨道），原则上对于任何需要 .wfn/wfx 文件作为输入文件的功能，你也可以改用 .mwfn/fch/molden/gms。而 Multiwfn 中的少数功能（例如 AdNDP 和 ICSS 分析）依赖一些特殊文件，这些情况下对输入文件的要求已在第 3 章相应小节中明确说明。

生成 .wfn 和 .wfx 文件

- Gaussian：在路线节（route section）中写入 out=wfn，在分子坐标节之后留一空行，并写入 .wfn 文件的目标路径，例如 C:\otoboku\H2O.wfn（可参考“examples”文件夹中的 H2O.gjf），然后运行该文件。若任务正常结束，H2O.wfn 将出现在“C:\otoboku”文件夹中。

如果你想在 Gaussian 中生成 .wfx 文件（自 G09 B.01 起支持），只需在路线节中写 out=wfx 而不是 out=wfn。

如果你在 Gaussian 中使用 MCSCF，为了将自然轨道生成并导出到 .wfn 中，还应使用 pop=no 关键词。如果你使用的 Gaussian 早于 G09 C.01，请仔细阅读以下信息：

若理论方法为 post-HF 类型，还必须在路线节中添加“density”关键词以使用当前密度，否则输出到 .wfn 文件中的仍将是 HF 轨道。如果你使用 TDDFT 或 CIS 并想导出对应激发态波函数的自然轨道，同样需要指定“density”关键词。

对于基于非限制 HF 参考态的 CCD/CCSD、QCISD 或 MP2/3、MP4SDQ 任务，只有同时指定“pop=NOAB”关键词时，才会将自然自旋轨道而非空间自然轨道保存到 .wfn 文件中。Gaussian 的 TD、CI 和 MCSCF 任务不能产生自然自旋轨道。

如果你使用的 Gaussian 早于 G09 B.01，注意存在一个严重 bug，若你的任务为限制性开壳层（ROHF 和 RODFT），.wfn 文件中单占据轨道的占据数将被错误地写为 2.0，你必须用文本编辑器打开该文件，找到最后一处“OCC NO =”，然后手动将其后的值改为 1.0000000。

- GAMESS-US：在 \$CONTRL 节中添加 AIMPAC=.TRUE.。任务结束后，在由 \$SCR 环境变量定义的目录（参见 rungms 脚本）中生成的 .dat 文件将包含与 .wfn 文件格式相同的波函数信息，提取“----- TOP OF INPUT FILE FOR BADER'S AIMPAC PROGRAM -----”与“----- END OF INPUT FILE FOR BADER'S AIMPAC PROGRAM -----”之间的内容，并保存为带“.wfn”后缀的新文件。

- ORCA：只需在输入文件中使用 aim 关键词即可生成 .wfn 和 .wfx 文件，或使用命令 orca_2aim XXX 将 XXX.gbw 转换为 XXX.wfn 和 XXX.wfx。至少对于


<!-- p.459 -->



ORCA 4.1，当使用 ECP 时无法生成 .wfn 和 .wfx 文件。作为 Multiwfn 的输入文件，始终更推荐使用 .molden 文件。

至于在其他量子化学软件中输出 .wfn 文件的方法，请查阅相应手册。

生成 .fch 文件

- Gaussian：先运行一个例如带“%chk=test.chk”的 Gaussian 任务以产生二进制 checkpoint 文件 test.chk 文件，再运行命令 formchk test.chk 将 test.chk 转换为 test.fch。

注：.fch 与 .fchk 格式没有区别。前者与后者分别是 Windows 版和 Linux 版 Gaussian 的格式化 checkpoint 文件的默认扩展名。你可以将二者中的任一种作为 Multiwfn 的输入文件。

进行 post-HF 任务时，Gaussian .fch 文件中默认记录的轨道和占据数都是 HF 的，因此 Multiwfn 分析结果与 HF 相同。类似地，在默认情况下，基于 TDDFT 任务产生的 .fch 文件的分析结果与基态 DFT 波函数相同。要分析 post-HF 波函数或 TDDFT 激发态波函数，应使用相应级别的自然轨道（NOs）进行分析，有两种方法可以得到它们：

(1) 利用主功能 200（main function 200）的子功能 16（subfunction 16）让 Multiwfn 生成自然轨道（或自旋自然轨道，自然自旋轨道）。详见 3.200.16 节。该方法非常方便，推荐使用。

(2) 让 Gaussian 将自然轨道写入 .fch 文件。应先用“density”关键词进行 post-HF 或 TDDFT 任务，然后仅用路线节中的“guess (save,only,naturalorbitals) chkbasis”重新运行该任务。注意 Gaussian 会把轨道占据数填入 .fch 文件中的轨道能量字段，因此应在 .fch 文件第一行写入“saveNO”，以让 Multiwfn 知晓该行为。若你进行的是开壳层 post-HF 计算，即使经过上述过程也无法将自然自旋轨道正确存入 .fch 文件。一般而言，我强烈推荐使用 .wfn/.wfx 文件查看自然轨道并对 post-HF 波函数进行实空间函数分析。

对于 MCSCF 计算，应载入生成的 .fch 文件，并用主功能 200 的子功能 16 生成包含 MCSCF 级别 NOs 的 .molden 文件，再将此 .molden 文件作为输入文件。由于 MCSCF 的 alpha 与 beta 轨道不能分别生成，对于自旋多重度大于 1 的体系，必须手动打开 .fch 文件，将“Number of beta electrons”设为与“Number of alpha electrons”相同的值，以使 Multiwfn 识别出输入文件中只有一套轨道。

- Q-Chem：在 $rem 字段中写入 GUI 2，任务结束后，你将在当前文件夹中找到生成的 .fchk 文件。注意若你使用的是相当旧的版本（可能 ≤5.0）的 Q-Chem，在将 .fchk 文件载入 Multiwfn 之前，必须将 `settings.ini` 中的“ifchprog”设为 2。

- PSI4：目前最新版（非旧版）PSI4 产生的 .fchk 文件与 Multiwfn 兼容。examples\psi4_fch.inp 是在 B3LYP/6-31G** 级别生成 .fchk 文件的示例文件。在 4.A.8 节中，我还展示了如何基于 PSI4 的 .fchk 文件分析 post-HF 波函数。

生成 .molden 文件
- ORCA：使用命令 orca_2mkl XX -molden 将 XX.gbw 转换为 Molden 输入文件

XX.molden.input。你无需再手动将后缀从 .molden.input 改为 .molden，因为前者同样可被 Multiwfn 识别。你也可以将 `settings.ini` 中的“orca_2mklpath”设为 ORCA 文件夹中 orca_2mkl 可执行文件的实际路径，


<!-- p.460 -->



则 Multiwfn 将能直接载入 .gbw 文件。
- Molpro：在输入文件最后一行添加诸如 put,molden,ltwd.molden 的语句，计算结束后将产生 Molden

输入文件 ltwd.molden。
- Dalton：计算结束时程序会自动输出 .molden 文件。该文件

为 .tar.gz 包中的 molden.inp。此文件可直接载入，无需更改后缀。
- NWChem：示例输入文件为 examples\NWChem_molden.nw。运行

后，.molden 文件将生成在当前文件夹中。注意必须使用球谐基函数（即“spherical”关键词），且当体系具有点群对称性时必须使用“noautosym”关键词。
- MRCC：一旦计算正常结束，当前

文件夹中将生成名为 MOLDEN 的文件。然后重命名使其具有 .molden 后缀。4.A.8 节中给出了一个例子。
- xtb：运行带“--molden”选项的 xtb，则当前文件夹中将生成 molden.input。
- 其他程序：请查阅相应手册。

当使用赝势且需要做与核电荷有关的一些分析时，别忘了手动将 .molden 文件中的原子序号改为核电荷，详见 2.5 节。

注：目前仅正式支持由 Molpro、ORCA、xtb、Dalton、NWChem、MRCC、deMon2k、BDF 程序生成的 Molden 输入文件。若文件由其他程序生成，结果可能正确也可能不正确，因为众多程序产生的文件不规范或存在问题。幸运的是，molden2aim 工具能够处理更广泛程序产生的 Molden 输入文件，并输出标准化的 Molden 输入文件，该文件随后即可用作 Multiwfn 输入文件。详见 5.1 节。

生成 .gms 文件 GAMESS-US 和 Firefly（旧称 PC-GAMESS）输出文件也可用作 Multiwfn 输入文件，需将其后缀改为 .gms 以便 Multiwfn 识别。目前，我只能保证以默认 NPRINT 选项进行 HF/DFT 计算的输出文件可被 Multiwfn 正常载入。GAMESS-US 的输入与输出文件示例分别作为 GAMESS_US.inp 和 UKS_cc-pVDZ.gms 提供在 examples 文件夹中。

现在开始吧！注意 4.x 节中的例子与主功能 x 相关，因此你可以快速找到所需的例子。4.A 节包括专题与高级教程，其中可能涉及多个功能和一些高级技巧，例如研究芳香性和弱相互作用。这些例子中涉及的几乎所有文件都可在“examples”文件夹中找到。// 之后的所有文字均为注释，不应作为命令输入。本章教程仅涵盖 Multiwfn 的基本应用，若想了解更多功能和更多选项的用法，请阅读第 3 章相应小节，并尝试例子中未提到的选项。

对于大多数例子，我采用 .fch 或 .wfn 作为输入文件格式，但这绝不意味着这些功能只能接受这两种格式！如果你已读过 2.5 节，一定知道如何为不同功能恰当选择输入文件格式。

PS1：若想分析高于 CCSD 级别的波函数，建议阅读 4.A.8 节，你将需要 ORCA、PSI4 或 MRCC 程序。

PS2：在第 4 章中，涉及我的许多中文博客文章，它们常包含扩展讨论和更多例子。若你读不懂中文，可尝试使用 Google 翻译（例如，可安装名为“Google translator for Firefox”的 Mozilla Firefox 插件。成功安装后，你会在 Firefox 工具栏中发现一个“T”图标。现在打开
