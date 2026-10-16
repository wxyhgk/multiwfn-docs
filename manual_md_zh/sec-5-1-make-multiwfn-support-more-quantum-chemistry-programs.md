# **5.1 使 Multiwfn 支持更多的量子化学程序**

虽然目前 Multiwfn 可以直接接受 Molden 输入文件 (.molden) 作为输入文件，但只有少数程序生成的文件是被正式支持的（见第 [2.5](sec-2-5-input-files-and-wavefunction-types.md) 节中的相关说明）。如果 Molden 输入文件是由其它程序生成的，那么分析结果可能是错误的。对于这些情况，你可以使用 Wenli Zou 编写的 Molden2aim 程序 (<https://github.com/zorkzou/Molden2AIM>) 来生成标准化的 Molden 输入文件。

使用 Molden2aim 很简单。首先将 Molden 输入文件（例如 *ltwd.molden*）移动到 *molden2aim.exe* 所在的目录，然后恰当地修改其设置文件 *m2a.ini*，接着启动 Molden2aim 并按照提示输入命令，最后你将得到 *ltwd_new.molden*（标准化的 Molden 输入文件），还可能得到其它文件（.wfn、.wfx 等）。

在 Multiwfn 和 Molden2aim 输出的 .wfn 文件中，轨道自旋类型通过 \$MOSPIN 字段显式写在 wfn 文件末尾，该信息会被 Multiwfn 自动载入。

Molden2aim 可以输出角动量高达 *g* 的高斯型基函数 (GTF)。虽然 *g* 型 GTF 并非 wfn 格式原本定义的内容，但这些 *g* 型 GTF 同样可以被 Multiwfn 正确识别和载入。

Molden2aim 输出的 wfn 文件中的 "charge" 字段是元素在元素周期表中的序号，而不是有效核电荷，即使使用了有效核芯势 (ECP, effective core potential) 也是如此。这种处理方式与 Gaussian 输出的 wfn 文件不一致，在 Gaussian 的文件中，当使用 ECP 时 "charge" 为有效核电荷（例如在 Lanl2DZ 下 Au 的 "charge" 为 19.0）。因此，如果使用了 ECP 并且你想计算静电势，不要忘记将 Molden2aim 输出的 wfn 文件中的 "charge" 字段修改为有效核电荷。
