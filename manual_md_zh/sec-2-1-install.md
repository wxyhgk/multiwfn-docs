# **2.1 安装**

## **2.1.1 Windows 版**

你需要做的只是解压程序包，然后双击图标即可开始使用。

Multiwfn 中的少数功能依赖于 Gaussian，如果需要进行这些分析，你需要手动为 Gaussian 设置环境变量，见[附录 1](sec-6-1-setting-up-running-environment-for-gaussian-in-windows.md)。

强烈建议把 *settings.ini* 中的 "nthreads" 设为你机器 CPU 物理核心的实际数目，这样在计算过程中才能利用 CPU 的全部算力。更多细节见 [2.4](sec-2-4-parallel-implementation.md) 节。

如果你想让 Multiwfn 能直接打开 Gaussian 产生的 .chk 文件，请把 *settings.ini* 中的 "formchkpath" 设为 Gaussian 包中 formchk 可执行文件的实际路径。

## **2.1.2 Linux 版**

> **注**
>
> 本节的中文版是我的博客文章“Multiwfn 在 Linux 下的安装中文说明”（<http://sobereva.com/688>）。

- 解压 Multiwfn 二进制包
- 确保已安装 motif 包，它提供 libXm.so.4，没有该文件，完整版 Multiwfn 无法启动。motif 可从 <https://motif.ics.com/motif/downloads> 免费获取。如果你是 CentOS 或 Red Hat Linux 用户且尚未安装 motif，可直接运行 `yum install motif` 安装；也可以下载相应的 rpm 包（*例如* motif-2.3.4-1.x86_64.rpm）手动安装；如果你是 Ubuntu 用户，运行 `sudo apt-get install libxm4 libgl1` 安装，或下载 deb 包（*例如* libmotif4_2.3.4-1_amd64.deb）手动安装。
- 在 *\~/.bashrc* 文件中加入以下几行（可用*例如* `vi \~/.bashrc` 命令编辑）

  ```bash
  export OMP_STACKSIZE=1000M
  ulimit -s unlimited
  ```

  这几行解除了栈内存 (stacksize memory) 的限制，并为并行计算中每个 OpenMP 线程定义了 1000MB 的栈大小，细节见 [2.4](sec-2-4-parallel-implementation.md) 节。

  > **注**
  >
  > 如果 `ulimit -s unlimited` 在你的系统上不能正常工作，请改用 `ulimit -Sn unlimited`。
- 运行 `cat /proc/sys/kernel/shmmax` 检查 SysV 共享内存段 (shared memory segments) 的大小是否足够大（单位为字节）；如果数值太小，分析大波函数时 Multiwfn 可能崩溃。要增大上限，例如可在 */etc/sysctl.conf* 中加入 *kernel.shmmax = 5000000000* 并重启系统，上限就会增大到约 5GB。
- 假设你使用 Bash shell，并且已把 Multiwfn 程序包解压为“/sob/Multiwfn_3.6_bin_Linux”文件夹，应在 *\~/.bashrc* 文件中加入以下几行：

  ```bash
  export Multiwfnpath=/sob/Multiwfn_3.6_bin_Linux
  export PATH=$PATH:/sob/Multiwfn_3.6_bin_Linux
  ```
- 运行以下命令，给 Multiwfn 可执行文件加上可执行权限：

  ```bash
  chmod +x /sob/Multiwfn_3.6_bin_Linux/Multiwfn
  ```
- 按上一节所述的同样方式配置 Multiwfn 文件夹中的 *settings.ini* 文件

  重新进入终端后，在任何位置只需运行 *Multiwfn* 命令即可启动 Multiwfn。

  如果你通过远程连接以纯文本模式在服务器上使用 Multiwfn，发现载入输入文件后 Multiwfn 卡住约两秒钟，请在 *\~/.bashrc* 文件中加入 `export DISPLAY=":0"`。

> **注**
>
> Linux 版 Multiwfn 在 CentOS 6/7/8、Rocky Linux 9 和 Ubuntu 12/14/16/22 上运行良好。我不能保证该程序与所有其它 Linux 发行版完全兼容。如果启动 Multiwfn 时系统提示缺少某些动态链接库（.so 文件），请尝试找到并安装包含相应 .so 文件的软件包。
>
> 如果由于缺少某些图形相关的库文件或不兼容而在运行/编译 Multiwfn 时遇到困难，而同时你又不需要 Multiwfn 的任何可视化功能，可以运行/编译不支持 GUI 的 Multiwfn，与 GUI 和绘图无关的所有功能仍可正常工作。关于如何编译这个特殊版本，请查看源代码包中的“COMPLIATION_METHOD.txt”，该版本的预编译可执行文件也可从 Multiwfn 官网下载（称为 "noGUI" 版）。

## **2.1.3 MacOS 版**

由于我不是 MacOS 用户，没有发布 MacOS 版 Multiwfn。如果你想在 MacOS 上编译 Multiwfn，请查看 <https://github.com/digital-chemistry-laboratory/multiwfn-mac-build>。如果你能读中文，可看 <http://bbs.keinsci.com/thread-46059-1-1.html>。

编译完 Multiwfn 后，应执行以下步骤（但我不能保证下面前两步对最新版 MacOS 依然有效）：

- (1) 在你的 .profile 文件（*例如* */Users/sob/.profile*）中加入下面一行，使其自动生效，然后重启终端。如果 .profile 不存在，应手动创建。

  ```bash
  export OMP_STACKSIZE=64000000
  ```

  OMP_STACKSIZE 定义了并行实现中每个线程的栈大小（单位为字节），细节见 [2.4](sec-2-4-parallel-implementation.md) 节。

- (2) 运行 `sysctl -a|grep shmmax` 检查 SysV 共享内存段的大小是否足够大（单位为字节），如果数值太小，分析大波函数时 Multiwfn 可能崩溃。为了增大上限，应编辑或创建 */etc/sysctl.conf* 文件，在其中加入 *kern.sysv.shmmax = 512000000* 并重启系统，上限就会增大到约 512MB。
- (3) 如有需要，设置 *Multiwfnpath* 环境变量，见 [2.1.2](#212-linux-版) 节第 5 点。
- (4) 按 [2.1.1](#211-windows-版) 节所述的同样方式配置 *settings.ini* 文件。

一位 Multiwfn 用户 Maciej Spiegel 提供了在 MacOS 上运行 Multiwfn 的另一种方法：

首先，用户应下载最新版 Unofficial Wineskin（<https://github.com/Gcenx/WineskinServer/releases/tag/V1.8.4>）。之后运行它，更新 wrapper 版本并下载最新引擎之一，即 WS11WineCX64Bit19.0.1-1（64 位系统）或 WS11WineCX19.0.1-1（32 位系统）。最后，新建一个 wrapper 并使用 Windows 版图形界面安装程序。
