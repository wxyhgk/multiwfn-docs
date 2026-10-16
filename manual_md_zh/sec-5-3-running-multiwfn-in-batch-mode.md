# **5.3 以批处理模式运行 Multiwfn**

> **注记**
>
> 如果你能阅读中文，请改为阅读我的博客文章“Multiwfn 的命令行运行与批量运行方法的详细介绍”（<http://sobereva.com/612>）中的第 3 节和第 4 节，其中介绍了关于使用 shell 脚本运行 Multiwfn 以自动批量处理文件的更详细信息，并给出和仔细讲解了一些示例脚本。

如果你熟悉 shell 脚本的编写，并且已经认真读过上一节，你一定已经知道如何用 Multiwfn 批量处理文件，这确实非常容易。本节将简要介绍这一点。

## **对于 Windows 用户**

### **例 1**

假设你想为以下输入文件生成 ELF 的 .cub 文件：*ultravox.wfn*、*chinaski.fch*、*strawberry_egg.wfn*，你可以创建一个名为 *batchrun.bat* 的纯文本文件（后缀必须为 .bat，文件名任意），内容如下：

```bat
Multiwfn ultravox.wfn < genELFcub.txt > null
move ELF.cub ultravox.cub
Multiwfn chinaski.fch < genELFcub.txt > null
move ELF.cub chinaski.cub
Multiwfn strawberry_egg.wfn < genELFcub.txt > null
move ELF.cub strawberry_egg.cub
del null
```

其中 *genELFcub.txt* 是用于生成 ELF cube 文件的输入流文件，它是一个内容如下的纯文本文件

```text
5   ← Main function 5, calculate grid data
9   ← Real space function 9, namely ELF
2   ← Option 2: Medium-quality grid
2   ← Option 2: Exporting cube file in current directory
```

将上述所有文件放入含有 *Multiwfn.exe* 的文件夹，然后双击 "batchrun.bat" 图标或在命令行窗口中输入命令 *batchrun*，任务即开始，三个 ELF cube 文件将依次在当前文件夹中生成。

### **例 2**

Shell 脚本非常有用且强大，可以自动完成大量重复性工作。举一个简单的例子，你想为当前文件夹中的所有 .wfn 文件生成 ELF 的 .cub 文件，并希望生成的 .cub 文件名为 *\[输入文件名\]\_ELF.cub*，那么你可以写一个内容如下的 .bat 文件

```bat
for /f %%i in ('dir *.wfn /b') do (
Multiwfn %%i < genELFcub.txt > null
rename ELF.cub %%~ni_ELF.cub
)
```

运行该 .bat 文件，.cub 文件将依次生成。假设其中一个输入文件为 *yoshiko.wfn*，相应的结果 .cub 文件将为 *yoshiko_ELF.cub*。

## **对于 Linux 用户**

类似地，你可以在 Linux 环境下以批处理模式运行 Multiwfn，编写脚本会让你的研究显著更轻松。要在 Linux 下实现上述例 1，你可以创建一个内容如下的文件 *runthree.sh*（假设你已如 [2.1.2](sec-2-1-install.md#212-linux-版) 节所述正确安装了 Multiwfn，因而可以直接用 *Multiwfn* 命令调用 Multiwfn）

```bash
Multiwfn ultravox.wfn < genELFcub.txt > null
mv ELF.cub ultravox.cub
Multiwfn chinaski.fch < genELFcub.txt > null
mv ELF.cub chinaski.cub
Multiwfn strawberry_egg.wfn < genELFcub.txt > null
mv ELF.cub strawberry_egg.cub
rm null
```

将 *runthree.sh* 和所有输入文件放在当前文件夹中，运行命令：`chmod +x ./runthree.sh;./runthree.sh`，计算即开始。（`chmod +x` 命令用于添加可执行权限，在某些情况下可能不是必需的）

要在 Linux 下实现上述例 2，你应创建一个内容如下的 shell 脚本文件然后运行它

```bash
#!/bin/bash
for inf in *.wfn
do
echo Running ${inf} ...
Multiwfn ${inf} < genELFcub.txt > /dev/null
mv ELF.cub ${inf//.wfn}_ELF.cub
done
```

Linux 平台的 shell 环境比 Windows 强大得多。*examples\scripts\gjf2xyz.sh* 是一个将当前文件夹中所有 .gjf 文件转换为同名 .xyz 文件的 Bash shell 脚本，请查看该脚本以了解其工作原理。如果你无法理解其内容，只需上网搜索 shell 脚本教程即可。

下面再给出一个 shell 脚本的例子，它计算当前文件夹中所有 .mol2 文件的 MPP 指数（见 [3.100.21](sec-3-100-other-functions-part-1.md#310021-基于几何信息计算特定原子的性质calculate-properties-based-on-geometry-information-for-specific-atoms) 节）：

```bash
#!/bin/bash
for filename in `ls *.mol2`
do
echo calculating $filename ...
echo -e "MPP\na\nn\nq" | Multiwfn $filename | grep "Molecular planarity parameter (MPP)"
done
```

顺便值得一提的是，通过 Linux 中的 *sed* 命令，你可以在脚本中轻松修改 *settings.ini* 的内容。例如，要将 "iuserfunc= 0" 替换为 "iuserfunc= 30"，可以输入以下命令

```bash
sed -i 's/iuserfunc=../iuserfunc= 30/g' settings.ini
```

实质性地、灵活地使用 shell 脚本可以自动完成比上面展示的更多种类的分析。例如，在 [4.18.6](sec-4-18-electron-excitation-analysis.md#4186-产生并分析尿嘧啶的自然跃迁轨道-nto) 节中，我展示了用一个简单的脚本，如何在一次运行中生成并导出所有选定激发态的自然跃迁轨道 (NTO, natural transition orbital) 到各种文件。
