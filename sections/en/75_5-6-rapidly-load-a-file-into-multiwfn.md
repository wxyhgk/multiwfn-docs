# 5.6 Rapidly load a file into Multiwfn

> Multiwfn manual, p.1148–1148. Images: `../imgs/`.

---

<!-- p.1148 -->

steps below.

Boot up Multiwfn, click title of the window by right mouse button, click "Properties", select "Layout" page, you will find the default buffer size of the window is 300 (see the screenshot below), that means only up to 300 lines can be recorded in the window, which is obviously too small. Change the value to a larger value, for example 9999, and then click OK button. After that you will find the window capable of recording much more output (If the complete output still cannot be recorded, enlarge buffer size again).

The buffer size setting is saved permanently in system, you needn’t set this value again next time you boot up Multiwfn.

For Linux and Mac OS, you can also find a similar option used to set buffer size of terminal.


### 5.6 Rapidly load a file into Multiwfn

Probably sometimes you feel inputting the path of input file is troublesome, especially when the path is very long. Below I provide you with some tricks, which make this step much easier.

If you want to rapidly load a file into Multiwfn without inputting its path, you can boot up Multiwfn and then directly drag the icon of the file into the Multiwfn command-line window.

In Windows platform, an even simpler method is directly dragging the file onto the icon of Multiwfn.exe, then the file will be automatically loaded into Multiwfn. Notice that in this situation, the "current folder" is the position of the input file.

If directly inputting letter o, the file that last time loaded will be loaded again, whose path is recorded as "lastfile" variable in `settings.ini` file.

Assume that the file you last time loaded is C:\sob\lover\K-ON\Mio.wfn, and this time you want to load C:\sob\lover\K-ON\Azusa.wfn, you can simply input ?azusa.wfn, namely the path of the folder last time involved can be replace with a question mark.


![](../imgs/p1148_621.png)
