# 安装（Install）

> Multiwfn manual, p.31–32.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.31 -->



## 2  基本信息（General information）


## 2.1 安装（Install）


### 2.1.1 Windows版本（Windows version）

你只需要解压程序压缩包，然后双击图标即可开始使用。

Multiwfn中的少数功能依赖于Gaussian，如果需要进行这些分析，需手动设置Gaussian的环境变量，见附录1。

强烈建议将`settings.ini`中的“nthreads”设为你机器CPU物理核心的实际数量，以便在计算中充分利用CPU的全部算力。详见2.4节。

如果你希望Multiwfn能直接打开Gaussian产生的.chk文件，请将`settings.ini`中的“formchkpath”设为Gaussian程序包中formchk可执行文件的实际路径。


### 2.1.2 Linux版本（Linux version）

注：本节的中文版是我的博客文章“Linux下安装Multiwfn的中文说明”（http://sobereva.com/688）。

- 解压Multiwfn二进制包
- 确保已安装motif包，它提供libXm.so.4，没有该文件完整版Multiwfn无法启动。motif可从https://motif.ics.com/motif/downloads免费获取。如果你是CentOS或Red Hat Linux用户且尚未安装motif，可直接运行yum install motif进行安装；或者下载相应的rpm包（例如motif-2.3.4-1.x86_64.rpm）手动安装；如果你是Ubuntu用户，运行sudo apt-get install libxm4 libgl1进行安装，或下载deb包（例如libmotif4_2.3.4-1_amd64.deb）手动安装。

- 向~/.bashrc文件中添加以下几行（例如用vi ~/.bashrc命令）


```text
export OMP_STACKSIZE=1000M
ulimit -s unlimited
```

这几行解除了对stacksize内存的限制，并为并行计算中每个OpenMP线程定义了1000MB的stacksize，详见2.4节。

注：若ulimit -s unlimited在你的系统上不能正常工作，请改用ulimit -Sn unlimited。

- 运行cat /proc/sys/kernel/shmmax检查SysV共享内存段的大小是否足够大（单位为字节）；若数值太小，分析大波函数时Multiwfn可能会崩溃。若要扩大上限，例如可在/etc/sysctl.conf中加入kernel.shmmax = 5000000000并重启系统，上限将被扩大到约5GB。

- 假设你使用Bash shell，并已将Multiwfn压缩包解压为“/sob/Multiwfn_3.6_bin_Linux”文件夹，应向~/.bashrc文件中加入以下几行：


```text
export Multiwfnpath=/sob/Multiwfn_3.6_bin_Linux
export PATH=$PATH:/sob/Multiwfn_3.6_bin_Linux
```


<!-- p.32 -->


- 运行以下命令给Multiwfn可执行文件添加可执行权限：


```text
chmod +x /sob/Multiwfn_3.6_bin_Linux/Multiwfn
```

- 用与上一节所述相同的方式配置Multiwfn文件夹中的settings.ini文件。重新进入终端后，在任何位置只需运行Multiwfn命令即可启动Multiwfn。

如果你通过远程连接以纯文本模式在服务器上使用Multiwfn，发现载入输入文件后Multiwfn卡住约两秒钟，请向你的~/.bashrc文件中加入export DISPLAY=":0"。

Linux版Multiwfn在CentOS 6/7/8、Rocky Linux 9和Ubuntu 12/14/16/22上运行良好。我不能保证该程序与所有其它Linux发行版完全兼容。启动Multiwfn时若系统提示缺少某些动态链接库（.so文件），请尝试查找并安装包含相应.so文件的软件包。

若因缺少某些图形相关库文件或其不兼容而在运行/编译Multiwfn时遇到困难，而你又不需要Multiwfn的任何可视化功能，可以运行/编译不支持GUI的Multiwfn，所有与GUI和绘图无关的功能仍可正常工作。关于如何编译此特殊版本，请查看源代码包中的“COMPLIATION_METHOD.txt”，此版本的预编译可执行文件也可从Multiwfn网站下载（称为“noGUI”版本）。


### 2.1.3 Mac OS版本（Mac OS version）

由于我不是MacOS用户，因此没有Multiwfn的MacOS发行版。若想在MacOS上编译Multiwfn，请查看https://github.com/digital-chemistry-laboratory/multiwfn-mac-build。若能阅读中文，见http://bbs.keinsci.com/thread-46059-1-1.html。

编译完Multiwfn后，应执行以下步骤（但我不能保证下面前两步对最新版MacOS仍然有效）：

（1）向你的.profile文件（例如/Users/sob/.profile）中加入以下一行以使其自动生效，然后重启终端。若.profile不存在，应手动创建。


```text
export OMP_STACKSIZE=64000000
```

OMP_STACKSIZE定义了并行实现中每个线程的stacksize（以字节为单位），详见2.4节。

（2）运行sysctl -a|grep shmmax检查SysV共享内存段的大小是否足够大（单位为字节），若数值太小，分析大波函数时Multiwfn可能会崩溃。为了扩大上限，应编辑或创建文件/etc/sysctl.conf，向其中加入kern.sysv.shmmax = 512000000并重启系统，上限将被扩大到约512MB。

（3）如有需要设置Multiwfnpath环境变量，见2.1.2节第5点。（4）用与2.1.1节所述相同的方式配置`settings.ini`文件。Multiwfn用户Maciej Spiegel提供了另一种在MacOS上运行Multiwfn的方法：

首先，用户应下载最新版Unofficial Wineskin（https://github.com/Gcenx/WineskinServer/releases/tag/V1.8.4）。之后运行它，更新wrapper版本并下载最新引擎之一，即WS11WineCX64Bit19.0.1-1（用于64位系统）或WS11WineCX19.0.1-1（用于32位系统）。最后，应创建新的wrapper并使用Windows GUI安装程序。
