# Multiwfn的使用（Using Multiwfn）

> Multiwfn manual, p.33–33.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.33 -->



## 2.2 Multiwfn的使用（Using Multiwfn）

使用Multiwfn非常简单，只需阅读屏幕上显示的提示，就能知道下一步该输入什么。若遇到困难，请仔细阅读第3章中的相应小节或第4章中的相应教程。

在Windows下，通常双击可执行文件图标即可启动Multiwfn，然后输入待载入文件的路径。也可通过命令行启动Multiwfn，同时还可给出输入文件的路径，例如可运行Multiwfn /sob/test.wfn。

若输入文件在当前目录下，可只输入文件名而不带目录路径。若输入文件正是上次使用的那个，进入Multiwfn后只需输入字母o即可（上次成功读取的输入文件路径记录在`settings.ini`中）。若输入文件与上次使用的文件在同一文件夹中，为方便可用符号?代替路径。例如，上次载入的是C:\sob\wives\K-ON\Mio.wfn，这次只需输入?Azusa.fch即可载入C:\sob\wives\K-ON\Azusa.fch。若希望在GUI窗口中选择输入文件，进入Multiwfn后直接按回车键（ENTER），随后会弹出用于选择输入文件的GUI窗口。

可随时按CTRL+C或点击Multiwfn窗口右上角的“×”按钮退出Multiwfn，但更优雅的退出方式是在主菜单（main menu）中输入q。当图形窗口显示在屏幕上时，可点击“RETURN”按钮关闭窗口，若没有该按钮，则在图形上点击鼠标右键关闭。

若想向Multiwfn中载入另一个文件，可重启Multiwfn或启动一个新的Multiwfn实例。或者，也可在主菜单（main menu）中输入r以初始化Multiwfn并载入新文件，同时`settings.ini`也会被重新载入。但请注意，最稳妥的载入新文件方式是重启Multiwfn。

Multiwfn也可通过静默模式（silent mode）而非交互模式运行，用户在运行过程中无需按任何键盘按键。这对批处理很有用，请参阅5.2节和5.3节。

支持的命令行参数（Supported arguments）。为方便起见，通过命令行运行Multiwfn时可附加以下参数：

- -nt：并行计算的线程数
- -uf：用户自定义函数的序号
- -silent：以静默模式运行Multiwfn
- -set：settings.ini的路径。例如：

Multiwfn COCl2.fch -nt 36 -set /sob/tmp/settings.ini -silent 这些参数的优先级高于`settings.ini`中的设置。若Multiwfn启动时找不到`settings.ini`，这些参数将不起作用，只使用默认参数。
