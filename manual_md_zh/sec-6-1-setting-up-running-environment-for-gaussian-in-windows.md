# **6.1 在 Windows 下为 Gaussian 设置运行环境**

Multiwfn 的某些功能可以直接调用 Gaussian（前提是 *settings.ini* 中的 "gaupath" 已设为 Gaussian 可执行文件的实际路径）。为了使 Windows 版 Gaussian 在这种情况下能正常运行，必须定义 "GAUSS_EXEDIR" 环境变量，否则会出现"No executable for file l1.exe"错误，Gaussian 运行会失败，因为 Gaussian 不知道去哪里找 l1.exe 可执行文件。下面是设置该环境变量的步骤。

- (1) Windows XP 用户：进入"Control panel"-"System properties"-"Advanced"

- (2) Windows 7 用户：进入"Control panel"-"System"-"Advanced system setting"-"Advanced"

- (3) Windows 10 用户：在开始按钮上点击鼠标右键，进入"Control panel"-"System"-"Advanced system setting"-"Advanced"

然后点击 "Environment variables" 按钮，再点击 "New" 按钮（在 "User variables" 框中），变量名输入 *GAUSS_EXEDIR*，变量值输入 Gaussian 的安装目录（例如 *D:\study\g16w\\*，假设 *g16.exe* 在该文件夹中）。

另外，非常重要的一点是，在 Windows 环境下当 Multiwfn 调用 Gaussian 时，Gaussian 会在当前文件夹而不是在 Gaussian 临时文件夹中寻找 *Default.Rou*。因此，如果 *Default.Rou* 中有重要设置，例如默认使用的 CPU 核心数，你应将该文件复制到当前文件夹，以使这些设置在计算中生效。
