# **5.2 以静默模式运行 Multiwfn**

> **注记**
>
> 如果你能阅读中文，请改为阅读我的博客文章“Multiwfn 的命令行运行与批量运行方法的详细介绍”（<http://sobereva.com/612>）中的第 1 节和第 2 节，其中介绍了关于通过命令行运行 Multiwfn 的更详细信息，并给出和仔细讲解了许多示例脚本。

Multiwfn 以易用性为目标，因此被设计为交互式程序。不过，Multiwfn 也可以在静默模式（命令行模式）下运行，从而在运行过程中不需要按任何按键。下面我将介绍具体做法。

## **对于 Windows 用户**

例如，你想静默地得到 [4.4.1.1](sec-4-4-output-and-plot-various-properties-in-a-plane.md#441-绘制填充色图和等值线图的说明) 节中的图形，你需要先写一个输入流文件，内容如下（红色文字为注释）：

```text
4   ← Main function 4
1   ← Real space function 1
1   ← Color-filled map
   ← Space line, corresponding to press ENTER button once (use default grid setting)
2   ← XZ plane
0   ← Y=0
0   ← Option 0: save graph to current directory
```

假设该输入流文件命名为 *4.4.1.txt*，我已在 "examples" 目录中提供了此文件。现在将 *settings.ini* 中的 "isilent" 参数由 0 改为 1（或在命令行中添加 "-silent" 参数），这会使 Multiwfn 在运行过程中禁止自动显示任何图形或 GUI，否则你必须用鼠标点击按钮来关闭窗口。然后进入 Windows 的命令行环境（点击“开始”-“运行”并输入 "cmd"），运行：

`Multiwfn HCN.wfn < 4.4.1.txt > medinfo.txt`

这里假设 *Multiwfn.exe*、*4.4.1.txt* 和 *HCN.wfn* 都在当前目录下。几秒钟后，你会发现在当前目录下出现了图像文件。从 *medinfo.txt* 中可以找到 Multiwfn 输出的所有中间信息。

输入流文件中的内容是什么意思？答案是：输入流文件中每一行的文本正是你在交互模式下需要输入的内容。对照交互模式下屏幕上的提示来写一个新的输入流文件是非常容易的。符号 "\<" 和 "\>" 是重定向符，它们分别告诉 Multiwfn：*4.4.1.txt* 中的内容是输入流，而输出流应保存到 *medinfo.txt*。这种重定向机制不是由 Multiwfn 提供的，而是由操作系统提供的。注意输入流文件中没有给出输入文件名，因为它作为参数出现。

你可能已经注意到，当任务完成后，会出现如下的一些报错：

```text
forrtl: severe (24): end-of-file during read, unit -4, file CONIN$
Image              PC        Routine            Line        Source
Multiwfn.exe       00588F1A  Unknown               Unknown  Unknown
Multiwfn.exe       00586438  Unknown               Unknown  Unknown
Multiwfn.exe       00530B3A  Unknown               Unknown  Unknown
......
```

实际上它们并不是报错，因此你可以安全地忽略它们。不过，如果你确实想让 Multiwfn 优雅地退出以避免打印这些“报错”，你应当恰当地编写输入流文件，使得在最后一步于主功能菜单中输入命令 *q*。

另一个例子，假设你想保存 *COCl2.fch* 的轨道 1 至 3 的详细组成，只需创建一个内容如下的输入流文件 *orbana_1_3.in*：

```text
8  ← Orbital composition analysis
1  ← Mulliken method
1  ← Orbital 1
2  ← Orbital 2
3  ← Orbital 3
```

然后运行命令：`Multiwfn COCl2.fch < orbana_1_3.in > orbana_1_3.txt`。

注意，如果你在 Windows 环境下使用 PowerShell，由于不支持 "\<" 重定向符，你应改用 "Get-Content" 命令和管道功能。例如，上述命令应写为（假设 Multiwfn.exe 在当前文件夹中）：

```powershell
Get-Content orbana_1_3.in | ./Multiwfn.exe COCl2.fch > orbana_1_3.txt
```

## **对于 Linux / MacOS 用户**

如果你是 Linux 或 MacOS 用户，你不仅可以如上介绍的那样静默运行 Multiwfn，还可以利用 "echo" 命令来避免显式地写输入流文件。上一个例子等价地可以通过运行以下命令实现：

```bash
echo -e "8\n1\n1\n2\n3" | Multiwfn COCl2.fch > orbana_1_3.txt
```

每个 \n 意味着按一次回车键。

如果你更喜欢使用 shell 脚本，也可以在 shell 脚本文件中加入以下几行：

```bash
Multiwfn COCl2.fch > orbana_1_3.txt << EOF
8
1
1
2
3
EOF
```
