# 自适应自然密度划分（Adaptive natural density partitioning, AdNDP）

> Multiwfn manual, p.217–221.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.217 -->



所需信息：格点数据（正交与非正交格点都支持）


### 3.16.16 周期性复制格点数据（Duplicate grid data periodically）（20）

该功能用于沿第 1/2/3 盒子矢量把格点数据复制特定倍数，也可让 Multiwfn 同时复制原子。若当前格点数据的盒子信息与晶体的胞信息恰好重合，则经该功能可获得超胞对应的格点数据与结构。说明性应用见“用 Multiwfn 快速产生超胞的格点数据”（http://sobereva.com/770）。

所需信息：格点数据（正交与非正交格点都支持）


## 3.17 自适应自然密度划分（Adaptive natural density partitioning, AdNDP）


## 分析（analysis）（14）（接上）


### 3.17.1 理论（Theory）

Weinhold 等人发展的著名 NBO 分析可从密度矩阵恢复至多 3 中心 2 电子（3c-2e）轨道（如在 NBO 程序中用 "3cbond" 关键词）。Boldyrev 等人提出的自适应自然密度划分（AdNDP）（Phys. Chem. Chem. Phys., 10, 5207 (2008)）可视为 NBO 分析的自然延伸，旨在定位 N>3 中心的轨道。AdNDP 已广泛用于研究众多团簇体系的电子结构特征，搜索 "AdNDP" 可找到很多相关文献。

正则分子轨道（CMOs）一般高度离域，常缺乏化学意义；而 2c 或 3c NBO 高度定域，对高度共轭体系常需共振式描述（否则出现大的非 Lewis 成分，即当前体系不适合用单套 NBO 描绘），这与现代量子化学概念有些冲突，也掩盖了共轭体系中电子的离域本质。AdNDP 轨道无缝衔接了 CMOs 与 NBOs，AdNDP 成键图像避免了共振式描述，且总与分子的点群对称性一致。

AdNDP 产生多中心轨道的基本思想与 NBO 分析很相似，即在自然原子轨道（NAO）基下构建密度矩阵的合适子块再对角化，本征值与本征矢分别对应占据数与轨道波函数。例如，要产生原子 A、B、C、D 的全部可能 4 中心轨道，先取出相应子块再拼在一起：


<!-- p.218 -->



$$P^{(\boldsymbol{A},\boldsymbol{B},\boldsymbol{C},\boldsymbol{D})}=\left[\begin{matrix}{P_{\boldsymbol{A},\boldsymbol{A}}}&{P_{\boldsymbol{A},\boldsymbol{B}}}&{P_{\boldsymbol{A},\boldsymbol{C}}}&{P_{\boldsymbol{A},\boldsymbol{D}}}\\ {P_{\boldsymbol{B},\boldsymbol{A}}}&{P_{\boldsymbol{B},\boldsymbol{B}}}&{P_{\boldsymbol{B},\boldsymbol{C}}}&{P_{\boldsymbol{B},\boldsymbol{D}}}\\ {P_{\boldsymbol{C},\boldsymbol{A}}}&{P_{\boldsymbol{C},\boldsymbol{B}}}&{P_{\boldsymbol{C},\boldsymbol{C}}}&{P_{\boldsymbol{C},\boldsymbol{D}}}\\ {P_{\boldsymbol{D},\boldsymbol{A}}}&{P_{\boldsymbol{D},\boldsymbol{B}}}&{P_{\boldsymbol{D},\boldsymbol{C}}}&{P_{\boldsymbol{D},\boldsymbol{D}}}\\ \end{matrix}\right]$$

对 P(A,B,C,D) 对角化后，若一个或多个本征值超过预设阈值（通常设为接近 2.0，如 1.7），则相应轨道视为候选 4c-2e 键。完全相同的策略可用于产生更高中心数的轨道。

确实，一旦原子组合确定，AdNDP 的轨道产生过程很简单，但整个体系中最终 Nc-2e 轨道的搜索过程很复杂，需人工检查与操作。AdNDP 方法有很大任意性，不同人做的搜索过程最终可能得到不同的 AdNDP 图像，笔者认为这是当前 AdNDP 方法最严重的局限。因此，AdNDP 绝不是黑箱，用之前用户必须对 Multiwfn 中实现的 AdNDP 搜索过程有初步了解。

搜索前，core 型 NAO 的密度自动从密度矩阵中剔除，因为它们对成键没有贡献。之后依次搜索 1 中心轨道（孤对）、2 中心轨道、3 中心轨道、4 中心轨道……直到剩余密度（密度矩阵的迹）接近零。搜索可以是穷举的，即搜索 N 中心轨道时 Multiwfn 将构建并对角化 M!/(M-N)!/N! 个密度矩阵子块，其中 M 为总原子数。对大体系搜索过程可能很耗时乃至不可行，例如在 30 原子体系中穷举搜索 10 中心轨道需构建并对角化 30045015 个密度矩阵子块！在个人电脑上很难完成，此时必须用户主导搜索。在 Multiwfn 中可定义搜索列表，则穷举搜索只对搜索列表中的原子进行，从而大幅减少计算量。也可直接让 Multiwfn 对指定的原子组合构建并对角化密度矩阵子块。注意用户主导搜索对用户的技巧和经验要求相对较高。

N 中心轨道搜索完成后，得到候选 N 中心轨道列表。需从中挑出一些作为最终 N 中心 AdNDP 轨道。一般挑出占据数最高的一个或几个轨道。注意，由于有些密度同时被多个候选轨道共享，若一次直接挑出占据数最大的几个候选轨道，可能重复计数电子。为避免该问题，假设占据数最高的 K 个轨道明显与其它一些候选轨道重叠而这 K 个轨道之间没有明显重叠，应先挑出 K 个轨道为最终 AdNDP 轨道，随后 Multiwfn 自动从密度矩阵中耗尽它们的密度，再对剩余候选轨道重建并对角化相应密度矩阵子块以更新其形状与占据数。若仍有些候选轨道占据数接近 2.0，可考虑挑出它们，剩余轨道再更新。该过程可重复多次，直到没有占据数高的轨道。之后可


<!-- p.219 -->



开始搜索 N+1 中心轨道。

AdNDP 分析的一般要求是：最终剩余密度（对应 NBO 分析中的非 Lewis 成分）应尽可能低；每个 AdNDP 轨道的占据数应尽可能接近 2.0；AdNDP 轨道的中心数应尽可能少；所得轨道必须与分子对称性一致。

但搜索轨道和把候选轨道挑为 AdNDP 轨道没有唯一规则。例如，可在 3 中心轨道搜索完成前先搜索 5 中心轨道，也可在 2 中心轨道搜索完成后直接搜索 6 中心轨道。挑出候选轨道的顺序也不一定总按占据数大小。不同操作得到的最终 AdNDP 图像可能不同，AdNDP 分析怎么做很大程度上取决于用户自己。实际上，有些分子可能有两种乃至多种同样合理的 AdNDP 图像，有时难以判别哪种最好。笔者有信心说，已发表论文中的某些 AdNDP 图像不是最优的。用 AdNDP 方法的经验可在实践和阅读相关论文中逐渐丰富。

AdNDP 与 NBO 分析一样对基组质量很不敏感，对前几排主族元素 6-31G* 已足以产生准确结果。过度提高基组质量不会改善 AdNDP 分析结果，只会增加对角化步骤的计算负担，因为密度矩阵子块的大小直接由基组大小决定。

Multiwfn 提供求 AdNDP 轨道能量的功能。需提供包含原始基函数下 Fock（或 Kohn-Sham）矩阵的文件。Fock 矩阵可从 Gaussian 或其它程序的输出获得。AdNDP 轨道的能量为 AdNDP 轨道表示下 Fock 矩阵的相应对角元。具体地，Multiwfn 做如下表示变换：

TAdNDPAOAONAO==FC FCCXc

其中 FAO 为从用户提供文件载入的原始基函数下的 Fock 矩阵，C(r,i) 对应 AdNDP 轨道 i 中基函数 r 的系数。c(s,i) 对应 AdNDP 轨道 i 中 NAO s 的系数。XAONAO 为原始基函数与 NAO 之间的变换矩阵，即 X(t,s) 为 NAO s 中基函数 t 的系数。AdNDP 轨道 j 的能量就是 FAdNDP(j,j)，即 AdNDP 轨道波函数的 Fock 算符期望值。
### 3.17.2 输入文件（Input file）

含 NAO 基下密度矩阵（DMNAO）的 NBO 程序输出文件可用作 AdNDP 分析的输入文件。若还需可视化 AdNDP 轨道或把轨道导出为 cube 文件，须提供 .fch 文件，同时 NBO 输出文件中须有 NAO 与原始基函数之间的变换矩阵（AONAO）。

假设你是 Gaussian 用户，为获得包含 Multiwfn 做 AdNDP 分析与可视化所需全部信息的 Gaussian 输出文件，应在单点任务的 Gaussian 输入文件的 route 段写 pop=nboread 关键词，并在分子几何之后空一行写 \$NBO AONAO DMNAO \$END。再用 Gaussian 运行该输入文件，然后用 formchk 工具把 .chk 文件转为 .fch 格式。

Multiwfn


<!-- p.220 -->



启动时的初始输入文件应用 Gaussian 输出文件（不是 .fch 文件）。进入 AdNDP 模块后，Multiwfn 将从该文件载入 NAO 信息与 DMNAO 矩阵。若之后选相应选项可视化或导出轨道，将载入 AONAO 矩阵，程序将提示输入 .fch 文件的路径（若 .fch 在同一文件夹且与 Gaussian 输出文件同名，则 .fch 将自动载入）。

Multiwfn 也兼容独立 NBO 程序（GENNBO）的输出文件，当然须在 .47 文件的 $NBO 段加 DMNAO 关键词。这种情形无法可视化 AdNDP 轨道。

形式上 AdNDP 方法也适用于开壳层体系；当然占据数阈值应除以 2。进入 AdNDP 模块时，Multiwfn 会问用哪个密度矩阵，所谓总密度矩阵即 α 与 β 密度矩阵之和。

注意，若进入 AdNDP 模块后 Multiwfn 突然崩溃，而你用的基组含弥散函数，可试换不含弥散函数的基组。该问题由 NBO 3.1 模块的 bug 引起，即极少数情形若有弥散函数 DMNAO 输出可能略有问题。由于 AdNDP 分析对弥散函数很不敏感，去掉它们不会损失任何精度。

若要获得 AdNDP 轨道能量，须在纯文本文件中以下三角序列提供与当前体系同级别的 Fock 矩阵，即：F(1,1) F(2,1) F(2,2) F(3,1) F(3,2) F(3,3) ... F(nbasis,nbasis)，其中 nbasis 为基函数总数。格式自由。若是 Gaussian 用户，可在 \$NBO ... \$END 之间加 archive file=XXX 关键词，则在所得 XXX.47 文件中搜 \$FOCK，把 \$FOCK ... \$END 之间的全部数据复制到纯文本文件，该文件可直接用于向 Multiwfn 提供 Fock 矩阵（事实上，当文件名为 .47 后缀时 Multiwfn 也能自动定位并读取 \$FOCK 域）。


### 3.17.3 选项（Options）

AdNDP 模块涉及的全部选项介绍如下，某些情形有些选项不可见。若当前候选轨道列表非空，则菜单前屏幕总打印全部候选轨道（选选项 5 或 13 时除外），候选轨道序号按占据数确定。搜索列表中全部原子的剩余价电子数总打印在菜单上方，该值随把候选轨道挑为最终 AdNDP 轨道而逐渐减小。若该值很低（如低于 1.4），表明在搜索列表的原子间不大可能再找到新的 Nc-2e AdNDP 轨道。

-10 返回主菜单（-10 Return to main menu）：一旦选该选项，将返回主菜单，同时 AdNDP 分析的全部结果丢失。因此经选该选项再重进模块可重置 AdNDP 模块的状态。

-2 各种其它设置与功能（-2 Various other settings and functions）：该选项有几个不重要的子功能和设置。值得一提的是“设置打印的最大候选轨道数（Set maximum number of candidate orbitals to be printed）”选项，用于设定屏幕打印多少候选轨道，找到的候选很多时适当选阈值可避免过多输出。

-1 定义穷举搜索列表（-1 Define exhaustive search list）：在该选项中可定义搜索列表，穷举搜索（选项 2）只对搜索列表中的原子进行。该定义界面的全部命令都是自明的


<!-- p.221 -->



。注意默认搜索列表包括分子的全部原子。

0 挑出一些候选轨道并更新其它轨道的占据数（0 Pick out some candidate orbitals and update occupations of others）：用于从候选列表中挑出轨道进入实际 AdNDP 轨道列表。如屏幕提示所示，用户可输入要挑出的轨道序号。为方便，若用户只输入一个数，如 5，则占据数最大的 5 个候选轨道被挑出。之后，剩余候选轨道的本征矢（轨道形状）与本征值（占据数）如前所述更新。

1 对特定原子组合搜索轨道（1 Perform orbitals search for a specific atom combination）：用户需输入一些原子序号，如 3,4,5,8,9，则构建并对角化原子 3,4,5,8,9 的密度矩阵子块，所得全部本征矢加入候选轨道列表，同时此前全部候选轨道被清除。输入的原子数不限。

2 在搜索列表内穷举搜索 N 中心轨道（2 Perform exhaustive search of N-centers orbitals within the search list）：从搜索列表中穷举选出 N 个原子，假设搜索列表含 M 个原子，则共形成 M!/(M-N)!/N! 个原子组合。对每个组合构建并对角化相应密度矩阵子块，本征值大于用户定义阈值的全部本征矢加入候选轨道列表。旧候选轨道列表将被清空。

3 设定下次穷举搜索的中心数（3 Set the number of centers in the next exhaustive search）：即设定选项 2 中的值 N。N 中心轨道穷举搜索完成后，N 自动加一。

4 设定下次穷举搜索的占据数阈值（4 Set occupation threshold in the next exhaustive search）：即设定选项 2 中用的阈值。

5 显示 AdNDP 轨道信息（5 Show information of AdNDP orbitals）：打印全部已存 AdNDP 轨道的占据数与涉及的原子。

6 删除一些 AdNDP 轨道（6 Delete some AdNDP orbitals）：输入两数，如 i, j，则已存的第 i 到 j 个 AdNDP 轨道被删除。

7 可视化 AdNDP 轨道与分子几何（7 Visualize AdNDP orbitals and molecular geometry）：将提示输入相应 .fch 文件的路径，从该文件载入必要信息后弹出 GUI 窗口并显示分子几何。点击右下列表中的相应数字可绘制 AdNDP 轨道的等值面

8 可视化候选轨道与分子几何（8 Visualize candidate orbitals and molecular geometry）：类似选项 7，但用于可视化候选轨道的等值面。在把一些候选轨道挑为最终 AdNDP 轨道之前先可视化等值面很有用。

9 把一些 AdNDP 轨道导出为 Gaussian 型 cube 文件（9 Export some AdNDP orbitals to Gaussian-type cube files）：用户需选格点设置再输入序号范围，如 2-4，则 AdNDP 轨道 2、3、4 的波函数值将被计算并分别导出到当前文件夹的 AdNDPorb0002.cub、AdNDPorb0003.cub 与 AdNDPorb0004.cub。它们是 Gaussian 型 cube 文件，可被 VMD 等许多软件可视化。

10 把一些候选轨道导出为 Gaussian 型 cube 文件（10 Export some candidate orbitals to Gaussian-type cube files）：类似选项 9，但用于为候选轨道导出 cube 文件。

11/12 保存/载入当前密度矩阵与 AdNDP 轨道列表（11/12 Save/Load current density matrix and AdNDP orbital list）：选项 11 用于暂时保存内存中的当前密度矩阵与 AdNDP 轨道列表，当密度矩阵与 AdNDP 轨道列表改变后，可选选项 12 恢复此前状态。

13 显示搜索列表中原子上的剩余密度分布（13 Show residual density distributions on the atoms in the search list）：选该选项后，按当前
