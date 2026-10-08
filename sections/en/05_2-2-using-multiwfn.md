# 2.2 Using Multiwfn

> Multiwfn manual, p.33–33. Images: `../imgs/`.

---

<!-- p.33 -->


## 2.2 Using Multiwfn

Using Multiwfn is very easy, by simply reading the prompts shown on screen, you will know what should input next. If you get stuck, please read corresponding section carefully in Chapter 3 or corresponding tutorials in Chapter 4.

In Windows, usually Multiwfn is booted up by directly double-clicking the icon of the executable file, then you should input the path of the file to be loaded. You can also boot up Multiwfn via command line, and the same time the path of input file may be also given, for example you can run Multiwfn /sob/test.wfn.

If the input file is in current directory, you can input file name without the path of directory. If the input file is just the one that last time used, you can simply input the letter o after entering Multiwfn (the path of the input file successfully read at last time was recorded in `settings.ini`). If the input file is in the same folder as the one last time used, for convenience the path can be replaced by symbol ?. For example, last time you loaded C:\sob\wives\K-ON\Mio.wfn, this time you can simply input ?Azusa.fch to load C:\sob\wives\K-ON\Azusa.fch. If you preferred to choose input file in GUI window, you can directly press ENTER button after entering Multiwfn, then a GUI window will be shown for selecting input file.

You can press CTRL+C or click “×” button at right-top of Multiwfn window any time to exit Multiwfn, but a more graceful way of exiting Multiwfn is inputting q in main menu. When graphical window is showing on screen, you can click “RETURN” button to close the window, if there is no such button, clicking right mouse button on the graph to close it.

If you want to load another file into Multiwfn, you can reboot Multiwfn or start a new Multiwfn instance. Alternatively, in main menu you can input r to initialize Multiwfn and load a new file, at the meantime the `settings.ini` will also be reloaded. However, please note that the safest way of loading a new file is rebooting Multiwfn.

Multiwfn can also run via silent mode instead of interactive mode, by which users do not need to press any keyboard button during running. This is useful for batch processing, please consult Sections 5.2 and 5.3.

Supported arguments For convenience, there are a few arguments that may be added when running Multiwfn via command line:

- -nt: Number of threads for parallel calculation
- -uf: Index of user-defined function
- -silent: Run Multiwfn in silent mode
- -set: Path of `settings.ini` For example,

Multiwfn COCl2.fch -nt 36 -set /sob/tmp/settings.ini -silent The priorities of these arguments are higher than those in `settings.ini`. If `settings.ini` cannot be found when Multiwfn boots up, these arguments will not take effect and only the default parameters will be used.
