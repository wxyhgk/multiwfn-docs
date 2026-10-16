# **2.4 并行实现**

Multiwfn 中最耗时的代码大多已用 OpenMP 技术实现并行。如果你的 CPU 有多个核心，并行化会带来很大收益。要启用并行，只需把 *settings.ini* 中的“nthreads”参数改为合适的数值。例如，你的计算机 CPU 有 12 个物理核心，那么通常应把“nthreads”改为 12。

如果在对很大的体系进行并行计算时 Multiwfn 崩溃，请尝试增大 *settings.ini* 中的“ompstacksize”（Windows 版），或增大环境变量 OMP_STACKSIZE 的值（Linux 或 MacOS 版）。
