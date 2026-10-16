# **2.3 Multiwfn 的文件**

解压 Multiwfn 程序包后你会看到以下文件，只有加粗的文件是运行 Multiwfn 必不可少的：

- **Multiwfn.exe**（Windows）或 **Multiwfn**（Linux/MacOS）：Multiwfn 的可执行文件。
- **libiomp5md.dll**（Windows）：Intel OpenMP 运行时库 (Runtime library)。
- **settings.ini**：运行 Multiwfn 的所有详细参数都记录在这里，其中大多数不需要经常修改。启动时，Multiwfn 会先尝试在当前文件夹中寻找并使用该文件；如果当前文件夹中没有，则使用 "Multiwfnpath" 环境变量所定义路径下的文件；如果仍然找不到，则使用默认设置。如果你通过命令行运行 Multiwfn，也可通过 "-set" 参数直接指定该文件的位置，例如：`Multiwfn test.wfn -set /sob/3.7/settings.ini`。

  *settings.ini* 中所有参数的含义在本手册中没有系统地说明，因为文件中已有详细注释，本手册只会提到其中重要的参数。建议你通读一遍 *settings.ini*，找出对你有用的参数。

- “examples”文件夹：一些有用的文件、脚本，以及[第 4 章](4-tutorials-and-examples.md)例子中涉及的文件。
- *LICENSE.txt*：所有用户必须遵守的条款。
- *Multiwfn quick start.pdf*：一份简短文档，让新用户能立刻了解如何用 Multiwfn 完成很常见的任务。
- *How to cite Multiwfn.pdf*：请按此文档的要求正确引用 Multiwfn。
