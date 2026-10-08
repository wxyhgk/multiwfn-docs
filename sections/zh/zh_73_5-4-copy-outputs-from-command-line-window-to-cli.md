# 从命令行窗口复制输出到剪贴板

> Multiwfn manual, p.1146–1146.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.1146 -->



文件，请查看该脚本以了解其工作原理。如果你看不懂其中的内容，就 Google 一下 shell 脚本。

下面给出 shell 脚本的另一个例子，它计算当前文件夹中所有 .mol2 文件的 MPP 指数（见 3.100.21 节）：


```text
#!/bin/bash
for filename in `ls *.mol2`
do
echo calculating $filename ...
echo -e "MPP\na\nn\nq" | Multiwfn $filename | grep "Molecular planarity parameter (MPP)"
done
```

顺便一提，值得注意的是，通过 Linux 中的 sed 命令你可以在脚本中轻松修改 `settings.ini` 的内容。例如，要把“iuserfunc= 0”替换为“iuserfunc= 30”，你可以输入以下命令


```text
sed -i 's/iuserfunc=../iuserfunc= 30/g' settings.ini
```

灵活而充分地运用 shell 脚本，可以自动完成比上述例子多得多的分析。例如，在 4.18.6 节我说明了用一个简单脚本，一次运行即可得到并导出所有选定激发态的自然跃迁轨道（NTO）到各种文件。


### 5.4 从命令行窗口复制输出到剪贴板

有时需要将 Multiwfn 在命令行窗口中的输出永久保存，或通过纯文本文件载入第三方软件。这里我介绍如何把这些输出复制到 Windows 剪贴板。

如果你使用 Windows 11，只需按住“ALT”键并用鼠标左键在窗口中拖出一个矩形区域，然后按回车(ENTER)键，该区域中的内容就会被复制到剪贴板。

如果你使用较老版本的 Windows，需按下面所示步骤操作。假设你要复制电子密度的 Hessian 矩阵。
