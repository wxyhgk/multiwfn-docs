# 5.8 Some tips on achieving ideal drawing quality

> Multiwfn manual, p.1150–1151. Images: `../imgs/`.

---

<!-- p.1150 -->

the file will contain both SCF density matrix and MP2 density matrix. If you want to calculate ESP at MP2 level by means of cubegen, you should change the value of "cubegendenstype" from the default "SCF" to "MP2".

·When you are dealing with very large .fch/fchk file, running cubegen via Multiwfn may be failed. Commonly, this is because the memory to be allocated by cubegen exceeded default upper limit. To solve this problem, you can run for example export GAUSS_MEMDEF=4GB in you console before performing your analysis, in this case the limit of memory will be increased to 4GB, which is absolutely large enough.

·This feature is fully compatible with the cubegen in Gaussian 09 and 16 packages. For cubegen in Gaussian 16, the number of CPU cores assigned for cubegen is identical to the "nthreads" parameter in `settings.ini` file. However, since parallel implementation of cubegen in Gaussian 09 seems buggy, only one CPU core will be employed for it. Multiwfn judges whether it is G09 or G16 cubegen by checking if there is "g16" or "G16" string in the "cubegenpath".

·Even though you have modified current wavefunction via some functions of Multiwfn, e.g. using subfunction 26 of main function 6 to manually change orbital occupation numbers, the ESP calculated by cubegen still corresponds to the original wavefunction, since the density matrix in the input file was not modified. If you indeed want to calculate ESP based on modified wavefunction via cubegen, you should first use subfunction 2 of main function 100 to export .fch file, the SCF density matrix in this file will correspond to the density matrix constructed by current wavefunction, and thus then you can use this .fch file as input file to carry out ESP analyses.

Why Multiwfn crashes when invoking cubegen? If Multiwfn crashes when (or after) invoking cubegen, there are three common reasons: (1) The .fch/fchk file is problematic or inappropriate, for example:

- The file does not contain wavefunction information (e.g. the one produced by ONIOM task with forcefield as low method)

- The file contains wavefunction but does not contain density matrix of expected type. For example, you require cubegen to deal with MP2 density matrix, but current file only contains SCF density matrix

- The file is corrupted. For example, incomplete file transfer, formchk does not work normally (2) The wavefunction is quite large but you did not properly define the "GAUSS_MEMDEF". (3) The cubegen is too old to be compatible with the fch/fchk file, you need to upgrade the Gaussian.

The outputted information of cubegen is dumped to nouseout file in current folder. If you are confused why the invoked cubegen cannot run normally, you can try to manually examine this file.


### 5.8 Some tips on achieving ideal drawing quality

Many functions of Multiwfn involve plotting graph, below are some suggestions for getting ideal drawing quality:

- Do not take screenshot, but use an option like "save picture" or "export graphical file" to generate the image file. This is particularly important for Linux system, because the quality of the graph shown on the screen is often poor. The effect of image file is independent of platform.


<!-- p.1151 -->

- If the graph to be plotted only consists of texts, straight lines and curves, it is strongly suggested to change "graphformat" in `settings.ini` to a vector format, such as .pdf and .svg (see Section 2.8 for detail), because in this case the texts and lines look very smooth, the graph can be losslessly scaled, and meantime the file size is very small. Since vector format is not directly supported by many applications programs, you can then manually convert the image file from vector format to pixel format.

- When the graph contains gradient colors, such as isosurface map, color-filled map and so on, the default .png format is the best choice. In order to make the axes, texts and outlines of objects as smooth as possible, I suggest save the image file with large size (see Section 2.8 on how to change size), then use advanced image editor such as Photoshop, or Irfanview (my favourite image viewer) to shrink the graph to the size you actually need, in this process the resample will be done automatically, anti-aliasing effect can thus be equivalently realized. By the way, before choosing the option used to generate image file, I suggest properly zooming to make the system fill the entire drawing area as much as possible.

- Please always pay attention to all options in the menu, Multiwfn has many options to control plotting parameters, graph quality under default settings may be significantly improved by properly using corresponding options. In addition, in `settings.ini` file there are many parameters controlling plotting effect, I suggest you briefly check comment of each parameter in this file to find the ones you often need to change.

- For plotting isosurface map, use relatively high quality of grid (i.e. relatively small grid spacing, or equivalently, relatively high number of grid points) to generate grid data. If lighting effect is not satisfactory, in the menu bar of the GUI for showing isosurface, use "Set lighting" in "Other settings" to adjust lightings. In addition, using VMD to plot this kind of map can get much better rendering effect, see Section 4.A.14 for related introduction and example.

- Use VMD plotting script whenever possible. For example, as illustrated in Section 4.2.5, using VMD to plot paths and critical points can yield much better effect than directly plotting them in the GUI window of topology module of Multiwfn; as also introduced in Section 4.A.14, via VMD plotting script very ideal isosurface map of grid data can be obtained via merely a few steps
