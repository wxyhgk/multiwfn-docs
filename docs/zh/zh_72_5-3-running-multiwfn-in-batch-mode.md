# 在批处理模式下运行 Multiwfn

> Multiwfn manual, p.1144–1145.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.1144 -->



Content orbana_1_3.in | ./Multiwfn.exe COCl2.fch > orbana_1_3.txt

对于 Linux / MacOS 用户 如果你是 Linux 或 Mac OS 用户，你不仅可以如上所述静默运行 Multiwfn，还可以利用“echo”命令来避免显式编写输入流文件。上一个例子可用运行以下命令等价实现：


```text
echo -e "8\n1\n1\n2\n3" | Multiwfn COCl2.fch > orbana_1_3.txt
```

每个 \n 意味着按一次回车(ENTER)键。

如果你更喜欢用 shell 脚本，你也可以在 shell 脚本文件中加入以下几行：


```text
Multiwfn COCl2.fch > orbana_1_3.txt << EOF
8
1
1
2
3
EOF
```


### 5.3 在批处理模式下运行 Multiwfn

注：如果你能读中文，请改读我的博客文章“Multiwfn 的命令行运行与批量运行方法详细介绍”（http://sobereva.com/612）中的第 3、4 节，其中介绍了更多关于用 shell 脚本运行 Multiwfn 以自动批量处理文件的信息，并给出和仔细讲解了一些示例脚本。

如果你熟悉编写 shell 脚本且已仔细阅读上一节，你一定已经知道如何用 Multiwfn 批量处理文件，这确实非常容易。我将在本节简要介绍这一点。

对于 Windows 用户

- 例 1 假设你想为这些输入文件生成 ELF 的 .cub 文件：ultravox.wfn、chinaski.fch、strawberry_egg.wfn，你可以创建一个名为 batchrun.bat 的纯文本文件（后缀必须为 .bat，文件名任意），内容如下：


```text
Multiwfn ultravox.wfn < genELFcub.txt > null
move ELF.cub ultravox.cub
Multiwfn chinaski.fch < genELFcub.txt > null
move ELF.cub chinaski.cub
Multiwfn strawberry_egg.wfn < genELFcub.txt > null
move ELF.cub strawberry_egg.cub
del null
```

其中 genELFcub.txt 是用于生成 ELF cube 文件的输入流文件，它是内容如下的纯文本文件

5  主功能 5，计算格点数据

9  实空间函数 9，即 ELF

2  选项 2：中等质量格点

2  选项 2：在当前目录导出 cube 文件


<!-- p.1145 -->



把上述所有文件放到含有 Multiwfn.exe 的文件夹中，然后双击“batchrun.bat”图标或在命令行窗口中输入命令 batchrun，任务就会开始，三个 ELF cube 文件将依次在当前文件夹中生成。

- 例 2 Shell 脚本非常有用且强大，可以自动完成大量重复工作。举一个简单例子，你想为当前文件夹中的所有 .wfn 文件生成 ELF 的 .cub 文件，并希望结果 .cub 文件名为 [输入文件名]_ELF.cub，那么你可以写一个 .bat 文件，内容如下


```text
for /f %%i in ('dir *.wfn /b') do (
Multiwfn %%i < genELFcub.txt > null
rename ELF.cub %%~ni_ELF.cub
)
```

运行该 .bat 文件，.cub 文件将依次生成。假设其中一个输入文件为 yoshiko.wfn，则对应的结果 .cub 文件为 yoshiko_ELF.cub。

对于 Linux 用户 类似地，你可以在 Linux 环境下以批处理模式运行 Multiwfn，编写脚本会让你的研究轻松很多。要在 Linux 下实现上述例 1，你可以创建一个文件 runthree.sh，内容如下（假设你已如 2.1.2 节所述正确安装了 Multiwfn，因而可直接用 Multiwfn 命令调用 Multiwfn）


```text
Multiwfn ultravox.wfn < genELFcub.txt > null
mv ELF.cub ultravox.cub
Multiwfn chinaski.fch < genELFcub.txt > null
mv ELF.cub chinaski.cub
Multiwfn strawberry_egg.wfn < genELFcub.txt > null
mv ELF.cub strawberry_egg.cub
rm null
```

把 runthree.sh 和所有输入文件放在当前文件夹中，运行该命令：chmod +x ./runthree.sh;./runthree.sh，然后计算就会开始。（chmod +x 命令用于添加可执行权限，在某些情况下可能不需要）

要在 Linux 下实现上述例 2，你应创建一个内容如下的 shell 脚本文件然后运行它


```text
#!/bin/bash
for inf in *.wfn
do
echo Running ${inf} ...
Multiwfn ${inf} < genELFcub.txt > /dev/null
mv ELF.cub ${inf//.wfn}_ELF.cub
done
```

Linux 平台的 shell 环境比 Windows 强大得多。examples\scripts\gjf2xyz.sh 是一个 Bash shell 脚本，可将当前文件夹中的所有 .gjf 文件转换为同名的 .xyz
