# 利用 Gaussian 软件包中的 cubegen 工具

> Multiwfn manual, p.1149–1149.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.1149 -->




### 5.7 利用 Gaussian 软件包中的 cubegen 工具


### 减少静电势分析的计算耗时

当你的 CPU 核数很少（少于 10）时，Multiwfn 内部代码计算 ESP 的速度不如 Gaussian 软件包中的 cubegen 工具快。在这种情况下，你可以让 Multiwfn 调用 cubegen 来计算 ESP 数据，以减少总耗时。即使你有大量 CPU 核，如果你需要计算 ESP 的格点数据（例如用主功能 5），Multiwfn 内部 ESP 代码的耗时仍高于让 Multiwfn 调用 cubegen。

在 ESP 分析中利用 cubegen 的方法非常简单：把 `settings.ini` 文件中的“cubegenpath”参数设为 cubegen 可执行文件的实际路径（例如 Windows 平台下的“D:\study\G16W\cubegen.exe”或 Linux 平台下的“/sob/g16/cubegen”）。然后如果你用 .fch/fchk/chk 文件作为 Multiwfn 的输入文件，cubegen 就会在恰当时机被 Multiwfn 自动调用以计算 ESP 数据。

可用性 以下情况和功能目前支持调用 cubegen 计算 ESP：·绘制 ESP 的曲线图（主功能 3）·绘制 ESP 的平面图（主功能 4）·所有需要 ESP 格点数据的功能（例如用主功能 5 计算 ESP 的格点数据，用主功能 17 对 ESP 做盆分析，用主功能 200 的子功能 14 对 ESP 做域分析）

·计算 ESP 拟合原子电荷如 CHELPG、MK 和 RESP（通过主功能 7 中的相应子功能）

·计算 TrEsp 电荷（见 4.A.9 节了解如何操作）·以 ESP 为映射函数的定量分子表面分析（主功能 12）尽管 Multiwfn 中许多其它功能也需要 ESP 信息，但它们不支持利用 cubegen，因为只需计算很少数量的点。

即使你不是 Gaussian 用户，只要你用的量子化学程序能产生 .mwfn 或 .molden 文件，或者你用的是 GAMESS-US/Firefly，你也能从 cubegen 获益，因为通过主功能 100 的子功能 2，Multiwfn 可把载入的 .mwfn/.molden/.gms 文件转换为 .fch 文件。然后，若你用该 .fch 文件作输入文件，就能在 ESP 计算中调用 cubegen。值得注意的是，examples/scripts/gbw2fch.sh 是一个 Bash shell 脚本，它通过自动调用 ORCA 软件包中的 orca_2mkl 和 Multiwfn 命令，把所有 ORCA 的 .gbw 文件转换为 .fch 文件。

注 ·被 cubegen 调用以计算 ESP 的波函数来自 .fch/fchk 文件中的密度矩阵。该文件可能含有不止一个密度矩阵，默认使用 SCF 密度矩阵。所用的密度矩阵类型可通过 `settings.ini` 中的“cubegendenstype”参数选择。例如，若 .fch 文件是通过“# MP2/cc-pVTZ density”关键词产生的，则
