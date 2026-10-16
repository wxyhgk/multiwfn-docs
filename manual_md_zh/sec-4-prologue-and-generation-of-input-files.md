# **序言与输入文件的生成**

欢迎使用 Multiwfn！如果你还没有阅读本手册第 2 页上的 "ALL USERS MUST READ"，请先阅读它。如果你在用 Multiwfn 时遇到任何问题，请尽管在 Multiwfn 论坛上发帖。

在开始之前，我首先向你展示如何生成各种输入文件。

注意 Multiwfn 中不同的功能需要不同类型的输入文件，见 [2.5](sec-2-5-input-files-and-wavefunction-types.md) 节的说明。简单地说，对于任何仅基于实空间函数（real space function）的分析，你都可以使用 .wfn 或 .wfx 作为输入文件。然而，许多功能需要基函数信息，在这些情况下你必须使用 .mwfn、.fch/fchk、.molden 或 .gms 文件作为输入文件。由于这些文件比 .wfn/wfx 文件包含更丰富的信息（即基函数和虚轨道），原则上对于任何需要 .wfn/wfx 文件作为输入文件的功能，你也可以改用 .mwfn/fch/molden/gms。Multiwfn 中的少数功能（例如 AdNDP 和 ICSS 分析）依赖于一些特殊文件，这些情况下对输入文件的要求在[第 3 章](3-functions.md)相应章节中已明确指出。

## **生成 .wfn 和 .wfx 文件**

- Gaussian：在 route section（任务关键词行）中写 *out=wfn*，在分子坐标部分之后留一空行并写上 .wfn 文件的目标路径，例如 *C:\otoboku\H2O.wfn*（可参考 "examples" 文件夹中的 *H2O.gjf*），然后运行此文件。若任务正常结束，*H2O.wfn* 将出现在 "C:\otoboku" 文件夹中。

  若想在 Gaussian 中生成 .wfx 文件（自 G09 B.01 起支持），只需在 route section 中写 *out=wfx* 而不是 *out=wfn*。

  若你在 Gaussian 中使用 MCSCF，为了将自然轨道生成并导出到 .wfn，还应使用 *pop=no* 关键词。若你用的 Gaussian 早于 G09 C.01，请仔细阅读以下信息：

  > **注记**
  >
  > 若理论方法为 post-HF 类型，你还必须在 route section 中添加 "density" 关键词以使用当前密度，否则输出到 .wfn 文件中的仍将是 HF 轨道。若你使用 TDDFT 或 CIS，并且想导出与激发态波函数对应的自然轨道，你同样需要指定 "density" 关键词。
  >
  > 对于基于非限制性 HF 参考态的 CCD/CCSD、QCISD 或 MP2/3、MP4SDQ 任务，只有同时指定了 "pop=NOAB" 关键词，保存到 .wfn 文件中的才是自然自旋轨道而不是空间自然轨道。Gaussian 的 TD、CI 和 MCSCF 任务不能产生自然自旋轨道。
  >
  > 若你用的 Gaussian 早于 G09 B.01，注意存在一个严重的 bug，若你的任务是限制性开壳层（ROHF 和 RODFT），.wfn 文件中单占据轨道的占据数将被错误地写成 2.0，你必须用文本编辑器打开该文件，找到最后一处 "OCC NO ="，然后手动将其后的值改为 1.0000000。

- GAMESS-US：在 \$CONTRL 部分添加 *AIMPAC=.TRUE.*。任务结束后，在 \$SCR 环境变量定义的目录（见 *rungms* 脚本）中生成的 .dat 文件将包含与 .wfn 文件格式相同的波函数信息，提取 "----- TOP OF INPUT FILE FOR BADER'S AIMPAC PROGRAM -----" 与 "----- END OF INPUT FILE FOR BADER'S AIMPAC PROGRAM -----" 之间的内容，保存为带有 ".wfn" 后缀的新文件。

- ORCA：只需在输入文件中使用 *aim* 关键词，或使用命令 *orca_2aim XXX* 将 *XXX.gbw* 转换成 *XXX.wfn* 和 *XXX.wfx*，即可生成 .wfn 和 .wfx 文件。至少对于 ORCA 4.1，当使用 ECP（有效核芯势）时无法生成 .wfn 和 .wfx 文件。作为 Multiwfn 的输入文件，总是更推荐使用 .molden 文件。

关于在其它量子化学软件中输出 .wfn 文件的方法，请查阅相应的手册。

## **生成 .fch 文件**

- Gaussian：首先运行 Gaussian 任务，例如用 "%chk=test.chk" 得到二进制 checkpoint 文件 *test.chk*，然后运行命令 `formchk test.chk` 将 *test.chk* 转换为 *test.fch*。

  > **注记**
  >
  > .fch 和 .fchk 格式没有区别。前者和后者分别是 Windows 版和 Linux 版 Gaussian 的 formatted checkpoint 文件的默认扩展名。你可以用其中任意一种作为 Multiwfn 的输入文件。

  当做 post-HF 任务时，Gaussian .fch 文件中默认记录的轨道和占据数是 HF 的，因此 Multiwfn 的分析结果与 HF 相同。类似地，在默认情况下，基于 TDDFT 任务产生的 .fch 文件的分析结果与基态 DFT 波函数相同。要对 post-HF 波函数或 TDDFT 激发态波函数做分析，应当使用相应级别的自然轨道 (NO, natural orbital) 进行分析，有两种得到它们的方法：

  - （1）用主功能 200 的子功能 16 使 Multiwfn 生成自然轨道（或自旋自然轨道、自旋自然轨道，natural spin orbital、spin natural orbital）。细节见 [3.200.16](sec-3-200-other-functions-part-2.md#320016-基于-fchfchk-文件中的密度矩阵生成自然轨道自然自旋轨道-nso-和自旋自然轨道-sno) 节。这种方式非常方便，推荐使用。
  - （2）使 Gaussian 将自然轨道写入 .fch 文件。你应先带着 "density" 关键词做 post-HF 或 TDDFT 任务，然后仅以 route section 中的 "guess (save,only,naturalorbitals) chkbasis" 重跑该任务。注意 Gaussian 把轨道占据数填到了 .fch 文件的轨道能量字段中，因此你应在 .fch 文件的第一行写上 "saveNO"，以让 Multiwfn 知道这一情况。当心，若你做的是开壳层 post-HF 计算，即使经过上述过程也无法将自然自旋轨道正确存入 .fch 文件。一般来说，我强烈推荐对 post-HF 波函数使用 .wfn/.wfx 文件来查看自然轨道和分析实空间函数。

  对于 MCSCF 计算，你应载入生成的 .fch 文件，用主功能 200 的子功能 16 生成包含 MCSCF 级别自然轨道的 .molden 文件，然后用该 .molden 文件作为输入文件。由于对 MCSCF 无法分别生成 alpha 和 beta 轨道，对于自旋多重度大于 1 的体系，你必须手动打开 .fch 文件，将 "Number of beta electrons" 设为与 "Number of alpha electrons" 相同的值，以使 Multiwfn 认为输入文件中只有一套轨道。

- Q-Chem：在 \$rem 字段中写 *GUI 2*，任务结束后，你将在当前文件夹中找到生成的 .fchk 文件。当心，若你用的 Q-Chem 版本相当老（可能 ≤5.0），在将 .fchk 文件载入 Multiwfn 之前，必须将 *settings.ini* 中的 "ifchprog" 设为 2。

- PSI4：当前最新版（而非更老的版本）PSI4 产生的 .fchk 文件与 Multiwfn 兼容。*examples\psi4_fch.inp* 是一个在 B3LYP/6-31G\*\* 级别生成 .fchk 文件的示例文件。在 [4.A.8](sec-4-A-special-topics-and-advanced-tutorials.md#4a8-分析高于ccsd水平的波函数) 节中，我还展示了如何基于 PSI4 的 .fchk 文件分析 post-HF 波函数。

## **生成 .molden 文件**

- （1）ORCA：用命令 `orca_2mkl XX -molden` 将 *XX.gbw* 转换为 Molden 输入文件 *XX.molden.input*。你不需要再手动将后缀由 .molden.input 改为 .molden，因为前者同样能被 Multiwfn 识别。你也可以将 *settings.ini* 中的 "orca_2mklpath" 设为 ORCA 文件夹中 orca_2mkl 可执行文件的实际路径，这样 Multiwfn 就能直接载入 .gbw 文件。

- （2）Molpro：在输入文件最后一行添加诸如 *put,molden,ltwd.molden* 的内容，计算结束后即产生 Molden 输入文件 *ltwd.molden*。

- （3）Dalton：计算结束后程序自动输出 .molden 文件。该文件是 .tar.gz 包中的 *molden.inp*，可直接载入而无需改后缀。

- （4）NWChem：示例输入文件见 *examples\NWChem_molden.nw*。运行它之后，当前文件夹中即生成 .molden 文件。注意必须使用球谐基函数（即 "spherical" 关键词），且当体系具有点群对称性时必须使用 "noautosym" 关键词。

- （5）MRCC：计算正常结束后，当前文件夹中将生成一个名为 *MOLDEN* 的文件，然后改名使其具有 .molden 后缀。示例见 [4.A.8](sec-4-A-special-topics-and-advanced-tutorials.md#4a8-分析高于ccsd水平的波函数) 节。

- （6）xtb：以 "--molden" 选项运行 xtb，当前文件夹中即生成 *molden.input*。

- （7）其它程序：请查阅相应的手册。

当使用了赝势并且你需要做一些与核电荷有关的分析时，不要忘记手动将 .molden 文件中的原子序号改为核电荷，细节见 [2.5](sec-2-5-input-files-and-wavefunction-types.md) 节。

> **注记**
>
> 目前，只有 Molpro、ORCA、xtb、Dalton、NWChem、MRCC、deMon2k、BDF 程序生成的 Molden 输入文件是被正式支持的。若文件由其它程序生成，结果可能正确也可能不正确，因为众多程序产生的文件不标准或有问题。幸运的是，molden2aim 工具能够处理更广泛程序产生的 Molden 输入文件，并输出标准化的 Molden 输入文件，之后即可用作 Multiwfn 输入文件。细节见 [5.1](sec-5-1-make-multiwfn-support-more-quantum-chemistry-programs.md) 节。

## **生成 .gms 文件**

GAMESS-US 和 Firefly（旧名为 PC-GAMESS）的输出文件也可用作 Multiwfn 输入文件，你需要将其后缀改为 .gms 以使 Multiwfn 能识别。目前，我只能保证以默认 NPRINT 选项做 HF/DFT 计算的输出文件能被 Multiwfn 正常载入。GAMESS-US 的输入和输出文件示例分别见 examples 文件夹中的 *GAMESS_US.inp* 和 *UKS_cc-pVDZ.gms*。

现在开始吧！注意 *4.x* 节中的例子与主功能 *x* 相关，因此你可以快速找到所需的例子。[4.A](sec-4-A-special-topics-and-advanced-tutorials.md) 节包括专题和高级教程，其中可能涉及不止一个功能和一些高级技巧，例如研究芳香性和弱相互作用。这些例子中用到的几乎所有文件都可以在 "examples" 文件夹中找到。// 之后的所有文字都是注释，不应作为命令输入。本章的教程只覆盖 Multiwfn 的基本应用，若想了解更多功能和更多选项的用法，请阅读[第 3 章](3-functions.md)中的相应章节并试用例子中未提及的选项。
对于大多数例子，我以 .fch 或 .wfn 作为输入文件的格式，但**这绝不意味着这些功能只能接受这两种格式**！若你已读过 [2.5](sec-2-5-input-files-and-wavefunction-types.md) 节，你一定知道如何针对不同功能恰当地选择输入文件的格式。

PS1：若想分析高于 CCSD 级别的波函数，建议阅读 [4.A.8](sec-4-A-special-topics-and-advanced-tutorials.md#4a8-分析高于ccsd水平的波函数) 节，你将需要 ORCA、PSI4 或 MRCC 程序。

PS2：在第 4 章中，涉及许多我用中文写的博客文章，它们常包含扩展讨论和更多例子。若你看不懂中文，可以尝试用谷歌翻译（例如，你可以安装名为 "Google translator for Firefox" 的 Mozilla Firefox 插件。安装成功后，你会在 Firefox 工具栏中发现一个 "T" 图标。现在打开所需的网页链接，点击 "T" 图标，即可看到所需语言的全文）。

PS3：若你能阅读中文，阅读以下三篇文章将非常有帮助：“Multiwfn 上手小贴士”（<http://sobereva.com/167>）、“Multiwfn FAQ”（<http://sobereva.com/452>）和“多功能波函数分析程序 Multiwfn 的意义、功能与用途”（<http://sobereva.com/184>）。
