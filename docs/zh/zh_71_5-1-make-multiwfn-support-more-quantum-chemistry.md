# 使 Multiwfn 支持更多的量子化学

> Multiwfn manual, p.1142–1143.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.1142 -->




## 5 技巧(Skills)


### 5.1 使 Multiwfn 支持更多的量子化学


### 程序

尽管目前 Multiwfn 能够直接接受 Molden 输入文件（.molden）作为输入文件，但只有少数程序生成的文件是正式支持的（见 2.5 节的相关说明）。如果 Molden 输入文件是由其它程序生成的，则分析结果可能不正确。对于这些情况，你可以用 Wenli Zou 编写的 Molden2aim 程序（https://github.com/zorkzou/Molden2AIM）来产生标准化的 Molden 输入文件。

使用 Molden2aim 很简单。首先把 Molden 输入文件（例如 ltwd.molden）移动到 molden2aim.exe 所在的目录，然后适当修改其设置文件 m2a.ini，接着启动 Molden2aim 并按其提示输入命令，最后你会得到 ltwd_new.molden（标准化的 Molden 输入文件），还可能得到其它文件（.wfn、.wfx 等）。

在 Multiwfn 和 Molden2aim 导出的 .wfn 文件中，轨道自旋类型在 wfn 文件末尾通过 $MOSPIN 字段明确写出，该信息会被 Multiwfn 自动加载。

Molden2aim 可输出角动量高达 g 的 GTF。虽然 g 型 GTF 原本没有在 wfn 格式中定义，但这些 g 型 GTF 也能被正确识别并载入 Multiwfn。

Molden2aim 输出的 wfn 文件中的“charge”字段是元素在周期表中的序号，而不是有效核电荷，即使使用了有效核势（ECP）。这种处理与 Gaussian 输出的 wfn 文件不一致，在 Gaussian 的文件中当使用 ECP 时“charge”为有效核电荷（例如 Au 在 Lanl2DZ 下的“charge”为 19.0）。因此，如果使用了 ECP 且你想计算静电势，别忘了把 Molden2aim 输出的 wfn 文件中的“charge”字段修改为有效核电荷。


### 5.2 在静默模式下运行 Multiwfn

注：如果你能读中文，请改读我的博客文章“Multiwfn 的命令行运行与批量运行方法详细介绍”（http://sobereva.com/612）中的第 1、2 节，其中介绍了更多关于通过命令行运行 Multiwfn 的详细信息，并给出和仔细讲解了许多示例脚本。

Multiwfn 以易用为目标，因此被设计为交互式程序。尽管如此，Multiwfn 也可在静默模式（命令行模式）下运行，这样运行期间你无需按任何按钮。这里我将介绍如何做到。

对于 Windows 用户 例如，你想静默地得到 4.4.1 节例子中的图，你需要先写一个输入流文件，内容为（红色文字为注释）：

4 ← 主功能 4


<!-- p.1143 -->



1 ← 实空间函数 1

1 ← 填充色图

← 空行，对应按一次回车(ENTER)键（使用默认格点设置）

2 ← XZ 平面

0 ← Y=0

0 ← 选项 0：将图形保存到当前目录 假设该输入流文件名为 4.4.1.txt，我已在“examples”目录中提供了该文件。现在把 `settings.ini` 中的“isilent”参数由 0 改为 1（或在命令行中加“-silent”参数），这会使 Multiwfn 在运行期间禁止自动显示任何图形或 GUI，否则你必须用鼠标点击按钮来关闭窗口。然后进入 Windows 的命令行环境（点击“开始(Start)”—“运行(run)”并输入“cmd”）并运行：

Multiwfn HCN.wfn < 4.4.1.txt > medinfo.txt 这里假设 Multiwfn.exe、4.4.1.txt 和 HCN.wfn 都在当前目录。几秒后，你会发现当前目录中出现了图像文件。从 medinfo.txt 中你可以找到 Multiwfn 输出的所有中间信息。

输入流文件中的内容是什么意思？答案是：输入流文件中每一行的文本正是你在交互模式下需要输入的内容。跟随交互模式下屏幕上的提示，写一个新的输入流文件非常容易。符号“<”和“>”是重定向运算符，它们分别告诉 Multiwfn 以 4.4.1.txt 中的内容为输入流，而输出流应存到 medinfo.txt。这种重定向机制不是由 Multiwfn 提供的，而是由操作系统提供的。注意输入流文件中没有给出输入文件名，因为它作为参数出现。

你可能已注意到，任务完成后会出现如下一些错误：


```text
forrtl: severe (24): end-of-file during read, unit -4, file CONIN$
Image              PC        Routine            Line        Source
Multiwfn.exe       00588F1A  Unknown               Unknown  Unknown
Multiwfn.exe       00586438  Unknown               Unknown  Unknown
Multiwfn.exe       00530B3A  Unknown               Unknown  Unknown
......
```

实际上它们不是错误，因此你可以放心忽略。不过，如果你确实想优雅地退出 Multiwfn 以避免打印这些“错误”，你应正确编写输入流文件，以便在最后一步于主功能菜单中输入命令 q。

另一个例子，假设你想保存 COCl2.fch 的轨道 1 至 3 的详细组成，只需创建一个输入流文件 orbana_1_3.in，内容如下：

8 ← 轨道组成分析

1 ← Mulliken 方法

1 ← 轨道 1

2 ← 轨道 2

3 ← 轨道 3 然后运行命令：Multiwfn COCl2.fch < orbana_1_3.in > orbana_1_3.txt。

注意，如果你在 Windows 环境中使用 PowerShell，由于不支持“<”重定向运算符，你应改用“Get-Content”命令和管道功能。例如，上述命令应写为（假设 Multiwfn.exe 在当前文件夹中）：Get-
