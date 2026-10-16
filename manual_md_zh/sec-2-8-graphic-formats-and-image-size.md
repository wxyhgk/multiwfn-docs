# **2.8 图形格式与图像尺寸**

Multiwfn 支持许多主流图形格式，包括：

1.  Postscript (ps)

2.  Encapsulated postscript (eps)

3.  Portable document format (pdf)

4.  Windows metafile format (wmf)

5.  Graphics interchange format (gif)

6.  TIFF (tiff)

7.  Portable network graphics (png)

8.  Windows bitmap format (bmp)

9.  Scalable vector graphics (svg)

Multiwfn 导出的图片的图形格式由 *settings.ini* 中的 "graphformat" 参数控制，你可以将该参数设为上面括号中所列的文本，默认格式为 "png"。

对于曲线图，图像文件的高度和宽度由 *settings.ini* 中的 "graph1Dsize" 参数控制。"graph2Dsize" 负责二维数据作图（颜色填充图、等值线图、浮雕图等）。"graph3Dsize" 负责三维数据作图（等值面图、分子结构图等）。

**提示 1**：如果图形主要由线条组成，例如等值线图和曲线图，最佳格式是 pdf 和 svg。但如果你需要将所得图形嵌入到 Office 中，通常应使用 wmf 格式。

**提示 2**：如果你想让导出的图像文件的背景透明，请看此视频说明：<https://youtu.be/E7lAGac3aDM>。
