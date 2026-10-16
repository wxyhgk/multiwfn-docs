# **5.7 利用 Gaussian 软件包中的 cubegen 工具以减少计算耗时**

当你的 CPU 核心数非常有限（少于 10 个）时，Multiwfn 内部代码计算静电势 (ESP, electrostatic potential) 的速度不如 Gaussian 软件包中的 cubegen 工具快。在这种情况下，你可以让 Multiwfn 调用 cubegen 来计算 ESP 数据，以减少总耗时。即使你拥有大量 CPU 核心，如果需要计算 ESP 的格点数据 (*e.g.* 使用主功能 5)，Multiwfn 内部 ESP 代码的时间开销仍然高于让 Multiwfn 调用 cubegen。

在 ESP 分析过程中利用 cubegen 的方法非常简单：将 *settings.ini* 文件中的 "cubegenpath" 参数设为 cubegen 可执行文件的实际路径（例如 Windows 平台下的 "D:\study\G16W\cubegen.exe"，或 Linux 平台下的 "/sob/g16/cubegen"）。之后如果你使用 .fch/fchk/chk 文件作为 Multiwfn 的输入文件，cubegen 就会在恰当的时机被 Multiwfn 自动调用以计算 ESP 数据。

## **可用范围**

目前以下情形和功能支持调用 cubegen 计算 ESP：

- 绘制 ESP 的曲线图（主功能 3）

- 绘制 ESP 的平面图（主功能 4）

- 所有需要 ESP 格点数据的功能（*e.g.* 使用主功能 5 计算 ESP 的格点数据，使用主功能 17 对 ESP 做盆分析 (basin analysis)，使用主功能 200 的子功能 14 对 ESP 做域分析 (domain analysis)）

- 计算 ESP 拟合原子电荷，如 CHELPG、MK 和 RESP（通过主功能 7 中相应的子功能）

- 计算 TrEsp 电荷（具体做法参见[4.A.9](sec-4-A-special-topics-and-advanced-tutorials.md#4a9-计算tresp由静电势得到的跃迁电荷电荷并分析激子耦合)节）

- 以 ESP 作为映射函数的分子表面定量分析 (Quantitative molecular surface analysis)（主功能 12）

虽然 Multiwfn 中还有许多其它功能也需要 ESP 信息，但它们不支持调用 cubegen，因为只需要计算极少数格点的 ESP。

即使你不是 Gaussian 用户，只要你使用的量子化学程序能够产生 .mwfn 或 .molden 文件，或者你使用的是 GAMESS-US/Firefly，你同样可以受益于 cubegen，因为通过主功能 100 的子功能 2，Multiwfn 可以把载入的 .mwfn/.molden/.gms 文件转换为 .fch 文件。然后，如果你使用该 .fch 文件作为输入文件，在 ESP 计算过程中就可以调用 cubegen。值得注意的是，*examples/scripts/gbw2fch.sh* 是一个 Bash shell 脚本，它通过自动调用 ORCA 软件包中的 *orca_2mkl* 和 *Multiwfn* 命令，把所有 ORCA 的 .gbw 文件转换为 .fch 文件。

## **注意事项**

- cubegen 调用以计算 ESP 所用的波函数来自 .fch/fchk 文件中的密度矩阵。该文件可能包含不止一个密度矩阵，默认使用 SCF 密度矩阵。所采用的密度矩阵类型可通过 *settings.ini* 中的 "cubegendenstype" 参数选择。例如，如果一个 .fch 文件是通过 "# MP2/cc-pVTZ density" 关键词产生的，那么该文件将同时包含 SCF 密度矩阵和 MP2 密度矩阵。如果你想借助 cubegen 在 MP2 水平下计算 ESP，就应当把 "cubegendenstype" 的值从默认的 "SCF" 改为 "MP2"。

- 当处理非常大的 .fch/fchk 文件时，通过 Multiwfn 运行 cubegen 可能会失败。通常这是因为 cubegen 需要分配的内存超过了默认上限。要解决这个问题，可以在进行分析之前先在终端中运行例如 `export GAUSS_MEMDEF=4GB`，此时内存上限会被提高到 4GB，这绝对足够大了。

- 该功能与 Gaussian 09 和 16 软件包中的 cubegen 完全兼容。对于 Gaussian 16 的 cubegen，分配给 cubegen 的 CPU 核心数与 *settings.ini* 文件中的 "nthreads" 参数相同。然而，由于 Gaussian 09 中 cubegen 的并行实现似乎有 bug，对它只会使用一个 CPU 核心。Multiwfn 通过检查 "cubegenpath" 中是否存在 "g16" 或 "G16" 字符串来判断是 G09 还是 G16 的 cubegen。

- 即使你已经通过 Multiwfn 的某些功能修改了当前波函数，*e.g.* 使用主功能 6 的子功能 26 手动改变轨道占据数，cubegen 计算出的 ESP 仍然对应于原始波函数，因为输入文件中的密度矩阵并未被修改。如果你确实想基于修改后的波函数通过 cubegen 计算 ESP，应当先使用主功能 100 的子功能 2 导出 .fch 文件，该文件中 SCF 密度矩阵将对应于由当前波函数构建的密度矩阵，这样就可以用这个 .fch 文件作为输入文件进行 ESP 分析。

## **为什么调用 cubegen 时 Multiwfn 会崩溃？**

如果 Multiwfn 在调用 cubegen 时（或调用之后）崩溃，常见有三种原因：

\(1\) .fch/fchk 文件有问题或不合适，例如：

- 该文件不含波函数信息（*e.g.* 以力场为低层方法做 ONIOM 任务产生的文件）

- 文件包含波函数，但不含预期类型的密度矩阵。例如，你要求 cubegen 处理 MP2 密度矩阵，但当前文件只含 SCF 密度矩阵

- 文件已损坏。例如，文件传输不完整，formchk 未正常工作

\(2\) 波函数相当大，但你没有正确定义 "GAUSS_MEMDEF"。

\(3\) cubegen 太旧，与 fch/fchk 文件不兼容，需要升级 Gaussian。

cubegen 输出的信息被转存到当前文件夹下的 *nouseout* 文件中。如果你不清楚被调用的 cubegen 为何无法正常运行，可以尝试手动查看该文件。
