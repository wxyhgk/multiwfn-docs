# 2.1 Install

> Multiwfn manual, p.31–32. Images: `../imgs/`.

---

<!-- p.31 -->


## 2  General information


## 2.1 Install


### 2.1.1 Windows version

What you need to do is just uncompressing the program package, then you can start to use by double-clicking the icon.

A few functions in Multiwfn rely on Gaussian, if you need to carry out these analyses, you need to setup environment variables for Gaussian manually, see Appendix 1.

It is strongly suggested to set "nthreads" in `settings.ini` to actual number of CPU physical cores of your machine, so that all computing power of your CPU could be utilized during calculation. See Section 2.4 for more detail.

If you want to make Multiwfn able to directly open .chk file produced by Gaussian, set "formchkpath" in `settings.ini` to actual path of formchk executable file in Gaussian package.


### 2.1.2 Linux version

Note: Chinese version of this section is my blog article “Chinese instructions for installing Multiwfn under Linux” (http://sobereva.com/688).

- Uncompress the Multiwfn binary package
- Make sure that you have installed motif package, which provides libXm.so.4, full version of Multiwfn cannot boot up without this file. The motif is freely available at https://motif.ics.com/motif/downloads. If you are a CentOS or Red Hat Linux user and have not installed motif, you can directly run yum install motif to install it; alternatively, you can download corresponding rpm package (e.g. motif-2.3.4-1.x86_64.rpm) and manually install it; If you are an Ubuntu user, run sudo apt-get install libxm4 libgl1 to install it, or download deb package (e.g. libmotif4_2.3.4-1_amd64.deb) and manually install it.

- Add below lines to ~/.bashrc file (using e.g. vi ~/.bashrc command)


```text
export OMP_STACKSIZE=1000M
ulimit -s unlimited
```

These lines remove limitation on stacksize memory, and define stacksize of 1000MB for each OpenMP thread during parallel calculations, see Section 2.4 for detail.

Note: If ulimit -s unlimited does not work properly on your system, try to use ulimit -Sn unlimited instead.

- Run cat /proc/sys/kernel/shmmax to check if the size of SysV shared memory segments is large enough (unit is in bytes); if the value is too small, Multiwfn may crash when analyzing big wavefunction. To enlarge the size, for example you can add kernel.shmmax = 5000000000 to /etc/sysctl.conf and reboot system, then the upper limit will be enlarged to about 5GB.

- Assume that you are using Bash shell, and you have decompressed the Multiwfn package as “/sob/Multiwfn_3.6_bin_Linux” folder, you should add below lines into ~/.bashrc file:


```text
export Multiwfnpath=/sob/Multiwfn_3.6_bin_Linux
export PATH=$PATH:/sob/Multiwfn_3.6_bin_Linux
```


<!-- p.32 -->

- Run below command to add executable permission to Multiwfn executable file:


```text
chmod +x /sob/Multiwfn_3.6_bin_Linux/Multiwfn
```

- Configure the `settings.ini` file in Multiwfn folder in the same way as described in last Section. After re-entering the terminal, you can boot up Multiwfn anywhere by simply running Multiwfn command.

If you use Multiwfn via remote connection to a server with text-only mode, and you find Multiwfn get stuck by about two seconds after loading input file, please add export DISPLAY=":0" to your ~/.bashrc file.

Linux version of Multiwfn works well on CentOS 6/7/8, Rocky Linux 9 and Ubuntu 12/14/16/22. I cannot guarantee that the program is completely compatible with all other Linux distributions. If system prompts you that some dynamical link libraries (.so files) are missing when booting up Multiwfn, please try to find and install the packages which contain the corresponding .so files.

If you encounter difficulty when running/compiling Multiwfn due to missing or incompatibility of some graphics related library files, and meantime you do not need any visualization function of Multiwfn, you can run/compile Multiwfn without GUI supported, all functions irrelevant to GUI and map plotting will still work normally. Please check “COMPLIATION_METHOD.txt” in source code package on how to compile this special version, the pre-compiled executable file of this version can also be downloaded from Multiwfn website (termed as "noGUI" version).


### 2.1.3 Mac OS version

As I am not a MacOS user, there is no MacOS release of Multiwfn. If you want to compile Multiwfn on MacOS, please check https://github.com/digital-chemistry-laboratory/multiwfn-mac-build. If you can read Chinese, see http://bbs.keinsci.com/thread-46059-1-1.html.

After compilation of Multiwfn, you should do following steps (but I cannot guarantee that the first two steps below still work for latest version of MacOS):

(1) Add the following line to your .profile file (e.g. /Users/sob/.profile) to make them take effect automatically, then reboot your terminal. If the .profile is nonexistent, you should create it manually.


```text
export OMP_STACKSIZE=64000000
```

OMP_STACKSIZE defines stacksize (in bytes) for each thread in parallel implementation, see Section 2.4 for detail.

(2) Run sysctl -a|grep shmmax to check if the size of SysV shared memory segments is large enough (unit is in bytes), if the value is too small, Multiwfn may crashes when analyzing big wavefunction. In order to enlarge the size, you should edit or create the file /etc/sysctl.conf, and add kern.sysv.shmmax = 512000000 to it and reboot system, then the upper limit will be enlarged to about 512MB.

(3) Set Multiwfnpath environment variable if needed, see point 5 of Section 2.1.2. (4) Configure the `settings.ini` file in the same way as described in Section 2.1.1. An alternative method of running Multiwfn on MacOS was provided by a Multiwfn user Maciej Spiegel:

First of all, a user should download the newest version of Unofficial Wineskin (https://github.com/Gcenx/WineskinServer/releases/tag/V1.8.4). After that, run it, update the wrapper version and download one of the most recent engines. These are WS11WineCX64Bit19.0.1-1 (for 64bit system) or WS11WineCX19.0.1-1 (for 32bit system). Finally, one should create new wrapper and use Windows GUI installer.
