# **3.17 自适应自然密度划分 (Adaptive natural density partitioning, AdNDP) 分析 (14)**

## **3.17.1 理论**

由 Weinhold 等人发展的著名 NBO 分析能够从密度矩阵中还原出最多 3 中心 2 电子 (3c-2e) 轨道 (例如在 NBO 程序中使用 "3cbond" 关键词)。自适应自然密度划分 (Adaptive natural density partitioning, AdNDP) 由 Boldyrev 等人提出 (*Phys. Chem. Chem. Phys.*, **10**, 5207 (2008))，可视为 NBO 分析的自然推广，旨在定位 $N>3$ 中心轨道。AdNDP 已被广泛用于研究各类团簇体系的电子结构特征，在网上搜索 "AdNDP" 即可找到大量相关文献。

正则分子轨道 (Canonical molecular orbital, CMO) 通常高度离域，往往缺乏明确的化学意义；而 2 中心或 3 中心 NBO 则相当定域，对于高度共轭体系常常需要共振式描述 (否则会出现很大的非 Lewis 成分，这意味着当前体系不适合用单一一套 NBO 来描绘)，这在某种程度上与现代量子化学概念相冲突，并掩盖了共轭体系中电子离域的本质。AdNDP 轨道在 CMO 与 NBO 之间架起了无缝桥梁，AdNDP 成键图像避免了共振式描述，且始终与分子的点群对称性一致。

AdNDP 生成多中心轨道的基本思想与 NBO 分析非常相似，即在自然原子轨道 (natural atomic orbital, NAO) 基下构造密度矩阵的适当子块并将其对角化，特征值和特征向量分别对应占据数和轨道波函数。例如，若要为原子 A、B、C、D 生成所有可能的 4 中心轨道，首先取出相应的子块并将它们组合在一起：

$$
P^{(A,B,C,D)}=\begin{bmatrix}P_{A,A}&P_{A,B}&P_{A,C}&P_{A,D}\\ P_{B,A}&P_{B,B}&P_{B,C}&P_{B,D}\\ P_{C,A}&P_{C,B}&P_{C,C}&P_{C,D}\\ P_{D,A}&P_{D,B}&P_{D,C}&P_{D,D}\end{bmatrix}
$$

对 $P^{(A,B,C,D)}$ 对角化后，若一个或多个特征值超过预设阈值 (通常设为接近 2.0 的值，例如 1.7)，则相应的轨道将被视为候选的 4c-2e 键。完全相同的策略可用于生成中心数更高的轨道。

事实上，一旦原子组合确定，AdNDP 的轨道生成过程相当简单，但整个体系中最终 *N*c-2e 轨道的搜索过程很复杂，需要人工检查和操作。AdNDP 方法存在较大的任意性，不同的人执行搜索过程最终可能得到不同的 AdNDP 图像，我认为这是当前 AdNDP 方法最严重的局限。因此，AdNDP 绝不是一个黑箱，在使用它之前，用户必须对 Multiwfn 中实现的 AdNDP 搜索过程有初步了解。

在搜索之前，来自核型 NAO 的密度会自动从密度矩阵中剔除，因为它们对成键没有贡献。此后，将依次搜索 1 中心轨道 (孤对电子)、2 中心轨道、3 中心轨道、4 中心轨道……直到剩余密度 (密度矩阵的迹) 接近于零。搜索可以是穷举式的，即在搜索 *N* 中心轨道时，Multiwfn 将构造并对角化 M!/(M-N)!/N! 个密度矩阵子块，其中 *M* 为原子总数。所有占据数大于阈值的轨道都将被加入候选轨道列表。对于大体系，搜索过程可能非常耗时甚至不可行，例如，穷举……

一旦 *N* 中心轨道的搜索完成，我们将得到一个包含候选 *N* 中心轨道的列表。我们需要从中挑选出一些作为最终的 *N* 中心 AdNDP 轨道。通常，占据数最高的一个或多个轨道会被挑选出来。注意，由于某些密度同时被多个候选轨道共享，若一次性直接挑选出占据数最大的几个候选轨道，电子可能会被重复计数。为避免这一问题，假设占据数最高的 *K* 个轨道明显与其他一些候选轨道重叠，而这 *K* 个轨道之间没有明显重叠，我们应先挑选出这 *K* 个轨道作为最终的 AdNDP 轨道，然后 Multi……

AdNDP 分析的一般要求是：最终剩余密度 (对应于 NBO 分析中的非 Lewis 成分) 应尽可能低；每个 AdNDP 轨道的占据数应尽可能接近 2.0；AdNDP 轨道的中心数应尽可能少；所得轨道必须与分子对称性一致。

然而，关于如何搜索轨道以及如何从候选轨道中挑选 AdNDP 轨道，并没有唯一的规则。例如，可以在完成 3 中心轨道搜索之前先搜索 5 中心轨道，也可以直接在 2 中心轨道搜索完成后搜索 6 中心轨道。从候选轨道中挑选的顺序也不一定总是按照占据数的大小。不同操作得到的最终 AdNDP 图像可能不同，如何进行 AdNDP 分析很大程度上取决于用户自己。实际上，某些分子可能有两种甚至更多同样合理的 AdNDP 图像，有时很难判断哪种图像最好。我有信心说……

AdNDP 与 NBO 分析一样，对基组质量非常不敏感，对于前几行的主族元素，6-31G\* 已足以给出准确结果。过度提高基组质量并不会改善 AdNDP 分析结果，只会增加对角化步骤的计算负担，因为密度矩阵子块的大小直接由基组大小决定。

Multiwfn 提供了计算 AdNDP 轨道能量的功能。用户需要提供一个包含在原始基函数下 Fock (或 Kohn-Sham) 矩阵的文件。Fock 矩阵可从 Gaussian 或其他程序的输出中获得。AdNDP 轨道的能量即为 Fock 矩阵在 AdNDP 轨道表象下的相应对角元。具体地，Multiwfn 执行如下表象变换：

$$
\mathbf{F}_{\mathrm{AdNDP}}=\mathbf{C}^{\mathrm{T}}\mathbf{F}_{\mathrm{AO}}\mathbf{C}\qquad\mathbf{C}=\mathbf{X}_{\mathrm{AONAO}}\mathbf{c}
$$

其中 $F_{\mathrm{AO}}$ 为从用户提供文件中读取的原始基函数下的 Fock 矩阵，*C*(*r*,*i*) 对应 AdNDP 轨道 *i* 中基函数 *r* 的系数，*c*(*s*,*i*) 对应 AdNDP 轨道 *i* 中 NAO *s* 的系数，$X_{\mathrm{AONAO}}$ 为原始基函数与 NAO 之间的变换矩阵，即 X(*t*,*s*) 为 NAO s 中基函数 *t* 的系数。AdNDP 轨道 *j* 的能量即为 $F_{\mathrm{AdNDP}}$ (*j*,*j*)，也就是 AdNDP 轨道波函数的 Fock 算符期望值。

## **3.17.2 输入文件**

包含 NAO 基下密度矩阵 (DMNAO) 的 NBO 程序输出文件可用作 AdNDP 分析的输入文件。若还需要可视化 AdNDP 轨道或将轨道导出为 cube 文件，则必须提供 .fch 文件，同时 NBO 输出文件中必须包含 NAO 与原始基函数之间的变换矩阵 (AONAO)。

假设你是 Gaussian 用户，为了得到包含 Multiwfn 进行 AdNDP 分析和可视化所需全部信息的一个 Gaussian 输出文件，应在 Gaussian 输入文件的任务路线部分写上 *pop=nboread* 关键词，并在分子几何构型之后空一行写上 *\$NBO AONAO DMNAO \$END*。然后用 Gaussian 运行该输入文件，再用 formchk 工具将 .chk 文件转换为 .fch 格式。

Multiwfn 启动时的初始输入文件应使用 Gaussian 输出文件 (而不是 .fch 文件)。进入 AdNDP 模块后，Multiwfn 将从该文件中读取 NAO 信息和 DMNAO 矩阵。若随后选择可视化或导出轨道的相应选项，将读取 AONAO 矩阵，程序会提示输入 .fch 文件的路径 (若 .fch 与 Gaussian 输出文件在同一目录且同名，则 .fch 会被自动加载)。

Multiwfn 也兼容独立 NBO 程序 (GENNBO) 的输出文件，当然你必须在 .47 文件的 \$NBO 部分添加 *DMNAO* 关键词。这种情况下无法可视化 AdNDP 轨道。

形式上，AdNDP 方法同样适用于开壳层体系；当然，占据数阈值应除以 2。进入 AdNDP 模块时，Multiwfn 会询问应使用哪个密度矩阵，所谓的总密度矩阵即 alpha 与 beta 密度矩阵之和。

注意，若进入 AdNDP 模块后 Multiwfn 突然崩溃，而所用基组包含弥散函数，可以尝试换用不含弥散函数的基组。该问题是由 NBO 3.1 模块的程序错误引起的，即在极少数情况下，若存在弥散函数，DMNAO 输出可能略有问题。由于 AdNDP 分析对弥散函数相当不敏感，去掉它们不会损失任何精度，是安全的。

若要获得 AdNDP 轨道能量，必须在一个纯文本文件中以下三角序列提供与当前体系、相同计算水平相应的 Fock 矩阵，即：*F*(1,1) *F*(2,1) *F*(2,2) *F*(3,1) *F*(3,2) *F*(3,3) ... *F*(*nbasis*,*nbasis*)，其中 *nbasis* 为基函数总数。格式是自由的。若你是 Gaussian 用户，可在 \$NBO ... \$END 之间添加 *archive file=XXX* 关键词，然后在生成的 XXX.47 文件中搜索 \$FOCK，将 \$FOCK ... \$END 之间的所有数据复制到一个纯文本文件，该文件即可直接用于向 Multiwfn 提供 Fock 矩阵 (事实上，当文件后缀为 .47 时，Multiwfn 也能自动定位并读取其中的 \$FOCK 字段)。

## **3.17.3 选项**

下面介绍 AdNDP 模块涉及的所有选项，在某些情况下部分选项不可见。若当前候选轨道列表非空，则在菜单之前总会将所有候选轨道打印在屏幕上 (选择选项 5 或 13 时除外)，候选轨道序号按占据数确定。搜索列表中所有原子的剩余价电子数始终打印在菜单上方，该数值随着候选轨道被逐个挑选为最终 AdNDP 轨道而逐渐减小。若该值很低 (例如低于 1.4)，则表明在搜索列表中的原子之间很可能无法再找到新的 *N*c-2e AdNDP 轨道。

**-10 Return to main menu**：选择此选项后将返回主菜单，同时 AdNDP 分析的所有结果都将丢失。因此可通过选择此选项再重新进入模块来重置 AdNDP 模块的状态。

**-2 Various other settings and functions**：该选项包含若干不太重要的子功能和设置。其中值得一提的是 "Set maximum number of candidate orbitals to be printed"，用于设置在屏幕上打印多少个候选轨道，当找到的候选轨道数量很大时，适当选择该阈值可避免过多输出。

**-1 Define exhaustive search list**：在此选项中可定义一个搜索列表，穷举搜索 (选项 2) 将只应用于搜索列表中的原子。该定义界面中的所有命令都是自解释的。注意默认搜索列表包含分子的全部原子。

**0 Pick out some candidate orbitals and update occupations of others**：用于从候选列表中挑选轨道进入实际 AdNDP 轨道列表。如屏幕提示所示，用户可输入要挑选的轨道序号。为方便起见，若用户只输入一个数字，例如 *5*，则占据数最大的 5 个候选轨道将被挑选出来。此后，其余候选轨道的特征向量 (轨道形状) 和特征值 (占据数) 将如前所述进行更新。

**1 Perform orbitals search for a specific atom combination**：用户需输入一些原子的序号，例如 3,4,5,8,9，则将构造原子 3、4、5、8、9 的密度矩阵子块并对角化，所得全部特征向量将被加入候选轨道列表，同时所有此前的候选轨道将被清除。输入的原子数没有限制。

**2 Perform exhaustive search of N-centers orbitals within the search list**：以穷举方式从搜索列表中选出 *N* 个原子，假设搜索列表包含 *M* 个原子，则共形成 *M*!/(*M*-*N*)!/*N*! 种原子组合。对每种组合，构造相应的密度矩阵子块并对角化，所有特征值大于用户定义阈值的特征向量将被加入候选轨道列表。旧的候选轨道列表将被清空。

**3 Set the number of centers in the next exhaustive search**：即设置选项 2 中的数值 *N*。一旦 *N* 中心轨道的穷举搜索完成，*N* 将自动加一。

**4 Set occupation threshold in the next exhaustive search**：即设置选项 2 中使用的阈值。

**5 Show information of AdNDP orbitals**：打印所有已保存 AdNDP 轨道的占据数和涉及的原子。

**6 Delete some AdNDP orbitals**：输入两个数字，例如 *i*、*j*，则已保存的 AdNDP 轨道中从 *i* 到 *j* 的轨道将被删除。

**7 Visualize AdNDP orbitals and molecular geometry**：将提示输入相应的 .fch 文件路径，从该文件读取必要信息后，会弹出 GUI 窗口并显示分子几何构型。点击右下列表中的相应编号即可绘制 AdNDP 轨道的等值面

**8 Visualize candidate orbitals and molecular geometry**：类似于选项 7，但用于可视化候选轨道的等值面。在将某些候选轨道挑选为最终 AdNDP 轨道之前，先可视化其等值面是很有用的。

**9 Export some AdNDP orbitals to Gaussian-type cube files**：用户需选择格点设置并输入序号范围，例如 *2*-*4*，则 AdNDP 轨道 2、3、4 的波函数值将被计算并分别导出为当前目录下的 *AdNDPorb0002.cub*、*AdNDPorb0003.cub* 和 *AdNDPorb0004.cub*。它们是 Gaussian 型 cube 文件，可用 VMD 等许多软件可视化。

**10 Export some candidate orbitals to Gaussian-type cube files**：类似于选项 9，但用于为候选轨道导出 cube 文件。

**11/12 Save/Load current density matrix and AdNDP orbital list**：选项 11 用于将内存中当前的密度矩阵和 AdNDP 轨道列表临时保存，当密度矩阵和 AdNDP 轨道列表发生变化后，可选择选项 12 恢复到此前状态。

**13 Show residual density distributions on the atoms in the search list**：选择此选项后，将根据当前密度矩阵计算搜索列表中每个原子的布居数并打印出来。若某些相邻原子具有较大的布居数，表明在这些原子上可能出现高占据数的多中心轨道；而布居数低的原子在后续搜索过程中通常可以忽略。因此该选项对建立用户主导的搜索非常有帮助。

**14 Export AdNDP orbitals to .mwfn file:** 通过此选项，所有已挑选的 AdNDP 轨道将被导出为当前目录下的 *AdNDP.mwfn* (关于 .mwfn 格式的介绍见 [2.5](sec-2-5-input-files-and-wavefunction-types.md) 节)。以该文件为输入文件，可对 AdNDP 轨道进行各种分析 (例如通过主功能 8 做轨道成分分析，通过主功能 4 绘制平面图)。注意，若有 *N* 个基函数且已挑选出 *M* 个 AdNDP 轨道，则 *AdNDP.mwfn* 中的前 *M* 个轨道对应 AdNDP 轨道，而该文件中的其余 *N*-*M* 个轨道没有意义，可直接忽略。

**15 Evaluate and output composition of AdNDP orbitals:** 该选项用于按自然原子轨道 (NAO) 方法计算已挑选 AdNDP 轨道的轨道成分，该方法已在 [3.10.4](sec-3-10-orbital-composition-analysis.md#3104-用自然原子轨道方法做轨道成分分析-7) 节介绍过。

**16 Evaluate and output energy of AdNDP orbitals**：该功能用于计算已挑选 AdNDP 轨道的能量。Multiwfn 会提示输入包含原始基函数下 Fock 矩阵的文件路径，矩阵元应按下三角序列记录，包含 \$FOCK 字段的 NBO .47 文件也可直接用作输入文件。经过简单的变换后，轨道能量即被输出。

AdNDP 分析相对复杂，不是黑箱，在用该模块分析自己的体系之前，请先学习 [4.14](sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md) 节中的例子。

> **Information needed**
>
> NBO output file (with AONAO DMNAO keywords), .fch file (only needed when visualizing and exporting cube file for AdNDP orbitals, or exporting AdNDP orbitals as .mwfn file), plain text file (containing Fock matrix. Only needed if you want to gain orbital energies)
