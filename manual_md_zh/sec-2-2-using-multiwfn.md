# **2.2 使用 Multiwfn**

使用 Multiwfn 非常简单，只需按照屏幕上显示的提示操作，你就会知道下一步该输入什么。如果你卡住了，请仔细阅读[第 3 章](3-functions.md)中的相应章节，或[第 4 章](4-tutorials-and-examples.md)中的相应教程。

在 Windows 下，通常直接双击可执行文件的图标即可启动 Multiwfn，然后输入待加载文件的路径。你也可以通过命令行启动 Multiwfn，同时还可以直接给出输入文件的路径，例如可以运行 `Multiwfn /sob/test.wfn`。

如果输入文件就在当前目录下，可以只输入文件名而不带目录路径。如果输入文件恰好是上次用过的文件，进入 Multiwfn 后只需输入字母 *o* 即可（上次成功读取的输入文件路径记录在 *settings.ini* 中）。如果输入文件与上次用过的文件在同一文件夹下，为方便起见，可用符号 *?* 代替路径。例如，上次你加载的是 *C:\sob\wives\K-ON\Mio.wfn*，这次只需输入 *?Azusa.fch* 即可加载 *C:\sob\wives\K-ON\Azusa.fch*。如果你希望在图形界面窗口中选择输入文件，进入 Multiwfn 后直接按回车键，随后会弹出用于选择输入文件的图形窗口。

你可以随时按 CTRL+C 或点击 Multiwfn 窗口右上角的“×”按钮退出 Multiwfn，但更优雅的退出方式是在主菜单中输入 *q*。当图形窗口显示在屏幕上时，可以点击“RETURN”按钮关闭窗口；如果没有这个按钮，则在图形上点击鼠标右键即可关闭。

如果你想把另一个文件载入 Multiwfn，可以重启 Multiwfn 或再启动一个新的 Multiwfn 实例。也可以在主菜单中输入 *r* 来初始化 Multiwfn 并加载新文件，同时 *settings.ini* 也会被重新加载。但请注意，最稳妥的加载新文件的方式是重启 Multiwfn。

Multiwfn 也可以通过静默模式 (silent mode) 而非交互模式运行，用户在运行过程中无需按任何键盘按键。这对批量处理很有用，请参阅[5.2](sec-5-2-running-multiwfn-in-silent-mode.md) 和 [5.3](sec-5-3-running-multiwfn-in-batch-mode.md) 节。

## **支持的命令行参数**

为方便起见，通过命令行运行 Multiwfn 时可以附加以下几个参数：

- -nt：并行计算的线程数
- -uf：用户自定义函数 (user-defined function) 的编号
- -silent：以静默模式运行 Multiwfn
- -set：*settings.ini* 的路径

例如：

```bash
Multiwfn COCl2.fch -nt 36 -set /sob/tmp/settings.ini -silent
```

这些参数的优先级高于 *settings.ini* 中的设置。如果 Multiwfn 启动时找不到 *settings.ini*，这些参数将不起作用，只会使用默认参数。
