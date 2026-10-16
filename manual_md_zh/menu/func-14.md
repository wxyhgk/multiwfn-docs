# 主功能14：自适应自然密度划分（AdNDP）分析

功能概述：AdNDP 是 NBO 的推广，在 NAO 基下构造密度矩阵子块并对角化，特征值/特征向量即占据数/轨道波函数，可定位 $N>3$ 中心 2 电子轨道，在 CMO 与 NBO 间架起桥梁，避免共振式描述且与点群对称性一致。流程为依次搜索 1c→2c→3c…轨道（穷举或用户指定组合），占据数超阈值者入候选列表，再挑选为最终轨道并耗竭密度更新其余候选，要求剩余密度接近零、占据数接近 2.0、中心数尽量少。AdNDP 对基组不敏感，强烈不建议用弥散函数。

## 子功能：指定原子组合搜索轨道（选项 1）

说明：输入原子序号，构造该原子组合的密度子块并对角化，所得全部特征向量加入候选列表（清空旧列表）。适合用户导向搜索，如在指定环片段上找 6c-2e 轨道。

菜单路径：主功能14 → 选项1 → 输入原子序号（如 3,4,5,8,9 或 1-6）

输入要求：含 DMNAO 的 NBO 输出（Gaussian 路线加 pop=nboread，几何后加 $NBO AONAO DMNAO $END）；Multiwfn 启动时载入 .out 而非 .fch。

操作步骤（原始格式，菲边缘环 6c-2e 搜索）：

```text
examples\AdNDP\phenanthrene.out  // 启动 Multiwfn 时载入
14  // AdNDP analysis
1  // Perform orbitals search for a specific atom combination
1-6  // Search in the fragment of atoms 1,2,3,4,5,6
```

```text
...ignored
 #   5 Occ: 0.2157 Atom:   1C    2C    3C    4C    5C    6C
 #   4 Occ: 0.2998 Atom:   1C    2C    3C    4C    5C    6C
 #   3 Occ: 1.8214 Atom:   1C    2C    3C    4C    5C    6C
 #   2 Occ: 1.9850 Atom:   1C    2C    3C    4C    5C    6C
 #   1 Occ: 2.0000 Atom:   1C    2C    3C    4C    5C    6C
```

产出：候选轨道列表（序号按占据数排序），占据≈2 即理想 nc-2e 键；配合选项 13 看剩余布居定搜索范围，配合 -1 定搜索列表＋选项 3 定中心数可达同样效果。

来源：[3.17.2 输入文件](../sec-3-17-adaptive-natural-density-partitioning-analysis.md)、[3.17.3 选项 1](../sec-3-17-adaptive-natural-density-partitioning-analysis.md)、[4.14.3 菲的用户导向搜索](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)

## 子功能：穷举 N 中心轨道搜索（选项 2，配合 3、4、-1）

说明：遍历搜索列表（默认全部分子原子，可用 -1 改为片段）全部 C(M,N) 组合，构造子块对角化，占据数超阈值（选项 4 设，默认接近 2.0）者入候选；搜索完成后 N 自动加一（选项 3 可直接设 N 跳过低中心数）。

菜单路径：主功能14 → -1（定义穷举搜索列表，clean 清空、a 加原子、x 保存）→ 3（设下次搜索中心数 N）→ 4（设占据阈值）→ 2（穷举搜索）

输入要求：含 DMNAO 的 NBO 输出。

操作步骤（原始格式，Li5+ 逐级搜索）：载入 examples\AdNDP\Li5+.out → 主功能14 → 选项 2 搜 1c（空）→ 选项 2 搜 2c（空）→ 选项 2 搜 3c（空）→ 选项 2 搜 4c，得：

```text
#   2 Occ:  1.9966  Atom:   1Li   2Li   3Li   4Li
#   1 Occ:  1.9966  Atom:   1Li   2Li   3Li   5Li
```

操作步骤（原始格式，Au20 大团簇）：

```text
Au20.out  // Generated at B3PW91/Lanl2DZ level based on optimized geometry
14  // AdNDP analysis
2  // Search 1-center AdNDP orbitals. 100 candidates are found, whose occupation numbers are very close to 2.0 and thus can be picked out
0  // Pick out orbitals
100  // Pick out all 100 candidate orbitals
2  // Perform exhaustive search of 2-centers orbitals. Nothing can be found
2  // Perform exhaustive search of 3-centers orbitals. Again nothing can be found
2  // Perform exhaustive search of 4-centers orbitals. Now you can see four candidates with 1.84 e and six candidates with 1.7589 e
0  // Pick out orbitals
4  // Pick out first four orbitals. The remaining orbitals now have occupancy of 1.6913, which, although is not quite high, it is still worth to be picked out in current circumstance
0  // Pick out orbitals
6  // Pick out remaining six orbitals.
```

产出：候选轨道列表；剩余价电子数（菜单上方，低于 ~1.4 即难再找到新 nc-2e 轨道）；选项 11/12 存取当前状态防取错。

来源：[3.17.3 选项 2/3/4/-1](../sec-3-17-adaptive-natural-density-partitioning-analysis.md)、[4.14.1 Li5+](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)、[4.14.4 Au20](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)

## 子功能：从候选挑选 AdNDP 轨道（选项 0，配合 5、6、11、12、13）

说明：按序号或取前 K 个挑入最终轨道并耗竭密度更新其余候选；为避免重复计数，应分批取出（先取无共享原子的，再取其余）；选项 5 打印已取列表，6 删除，13 看各原子剩余布居，11/12 存取状态。

菜单路径：主功能14 → 选项0 → 输入序号或个数（如 2 取前 2 个）→ 选项5（查看已取）→ 选项13（剩余布居指导下一步）

输入要求：非空候选列表。

操作步骤（原始格式，B11− 分步取轨）：载入 B11-.out＋B11-.fch（HF/STO-3G 已够）→ 选项 2 搜 2c → 选项 0 输入 3 取前三（密度扣除后其余占据下降）→ 选项 0 输入 4 取前四 → 取出剩下两个；再选项 2 搜 3c，依次取出 2 个、1 个、2 个（最高仅 1.41 不再取）；选项 2 搜 4c（最高 1.71 不取）→ 搜 5c 取前 2（1.89）→ 搜 6c（最高 1.84 不取）→ 搜 7c 取最高（1.90）；剩余价电子 1.34（<2）结束。最终 9 个 2c＋5 个 3c＋2 个 5c＋1 个 7c，选项 5 输出：

```text
#    1 Occ:  1.9942 Atom:   2B    3B
#    2 Occ:  1.9871 Atom:   8B   10B
#    3 Occ:  1.9871 Atom:   9B   11B
#    4 Occ:  1.9750 Atom:   2B    6B
#    5 Occ:  1.9750 Atom:   3B    5B
#    6 Occ:  1.9556 Atom:   7B    9B
#    7 Occ:  1.9556 Atom:   7B    8B
#    8 Occ:  1.9337 Atom:   6B   10B
#    9 Occ:  1.9337 Atom:   5B   11B
#   10 Occ:  1.8673 Atom:   4B    9B   11B
#   11 Occ:  1.8673 Atom:   1B    8B   10B
#   12 Occ:  1.8533 Atom:   1B    4B    7B
#   13 Occ:  1.8451 Atom:   3B    4B    5B
#   14 Occ:  1.8451 Atom:   1B    2B    6B
#   15 Occ:  1.8908 Atom:   1B    2B    6B    8B   10B
#   16 Occ:  1.8908 Atom:   3B    4B    5B    9B   11B
#   17 Occ:  1.9036 Atom:   2B    3B    5B    6B    7B    8B    9B
Total occupation number in above orbitals:   32.6607
```

产出：最终 AdNDP 轨道列表；残余电子即非 Lewis 电子。

来源：[3.17.3 选项 0/5/6/11/12/13](../sec-3-17-adaptive-natural-density-partitioning-analysis.md)、[4.14.2 B11−](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)

## 子功能：可视化与导出 cube（选项 7、8、9、10）

说明：选项 7/8 在 GUI 按编号绘制 AdNDP/候选轨道等值面（挑前先看候选形状）；选项 9/10 选序号范围输出 AdNDPorbXXXX.cub，可用 VMD 显示或批量绘制。

菜单路径：主功能14 → 7（可视化 AdNDP 轨道，需 .fch 提供基组）→ 8（可视化候选轨道）→ 9（导出 AdNDP 轨道 cube：格点质量 → 序号范围）→ 10（导出候选轨道 cube）

输入要求：NBO 输出＋同名 .fch（含 AONAO；同目录同名自动加载）。

操作步骤（原始格式，导出 B11− 全部轨道）：选项 9 → Medium-quality grid → 输入 1-17，得 AdNDPorb0001.cub～AdNDPorb0017.cub。

操作步骤（原始格式，导出 Au20 的 4c 轨道）：

```text
9  // Export cube file of picked AdNDP orbitals
2  // Medium-quality grid, which is adequate for producing smooth orbital isosurface for present system
101-110  // The index range of the picked 4c-orbitals
```

VMD 批量绘制（原始格式）：编辑 examples\AdNDP\plotAdNDP.vmd，把 `set name "D:\\CM\\my_program\\Multiwfn\\AdNDPorb$idx.cub"` 改为实际路径，确保 set istart/set iend 为 1 和 17，把全部内容粘入 VMD 命令窗口；VMD 主窗口每条目一轨道，双击 D 显隐，载入 B11-.xyz 以 CPK 叠加结构。

产出：AdNDP.mwfn 供后续分析之外的 cube 文件与 GUI 等值面图。

来源：[3.17.3 选项 7/8/9/10](../sec-3-17-adaptive-natural-density-partitioning-analysis.md)、[4.14.1](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)、[4.14.2 VMD 脚本](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)、[4.14.4](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)

## 子功能：导出 .mwfn、算成分、算能量（选项 14、15、16）

说明：选项 14 把已取轨道导出 AdNDP.mwfn（前 M 个轨道有意义，可做常规组成/平面分析）；选项 15 用 NAO 法直接算指定轨道成分；选项 16 用 Fock 矩阵（文本下三角或 .47 的 $FOCK）算轨道能量（Fock 期望值）。

菜单路径：主功能14 → 14（导出 AdNDP.mwfn）→ 15（NAO 法成分：输入轨道号）→ 16（轨道能量：输入 Fock 文件/.47 路径）

输入要求：NBO 输出（能量另需 Fock 矩阵文本或 .47；成分的 NAO 法需 NBO 信息）。

操作步骤（原始格式，Li5+ 轨道能量）：把 Li5+.gjf 复制为 Li5+_47.gjf，末行改为 $NBO archive file=C:\Li5+ $END，Gaussian 运行得 C:\Li5+.47；AdNDP 界面选 16 → 输入 Li5+.47 路径，得：

```text
Energy of picked AdNDP orbitals:
Orbital:     1  Energy (a.u./eV):   -0.325776     -8.8648
Orbital:     2  Energy (a.u./eV):   -0.325776     -8.8648
```

操作步骤（原始格式，菲 31 号轨道 NAO 成分）：选项 15 → 输入 31，得：

```text
    NAO#   Center   Label      Type    Composition
      67    8(C )    px       Val( 2p)     2.247%
      76    9(C )    px       Val( 2p)     1.929%
      94   11(C )    px       Val( 2p)    13.276%
     105   13(C )    px       Val( 2p)    32.846%
     114   14(C )    px       Val( 2p)    34.484%
     123   15(C )    px       Val( 2p)    15.204%
```

产出：AdNDP.mwfn；NAO 成分表（如菲 6c-2e 轨道纯由 px 价 NAO 组成）；各轨道能量（等价轨道简并）。

来源：[3.17.3 选项 14/15/16](../sec-3-17-adaptive-natural-density-partitioning-analysis.md)、[4.14.1 能量](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)、[4.14.3 能量与组成](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)

## 实例条目

- Li5+ 两个 4c-2e 穷举搜索：选项 2 逐级搜 1c→4c → 选项 0 取出 → 选项 5 看列表；剩余价电子 0.020 停止。来源：[4.14.1](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)
- AdNDP 轨道能量（Li5+ / 菲）：选项 16 → 输入 .47 路径；等价轨道能量简并。来源：[4.14.1](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)、[4.14.3](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)
- B11− 分步取轨（9 个 2c＋5 个 3c＋2 个 5c＋1 个 7c）：分批取出防重复计数，占据<1.9 不取；残余 1.34 即非 Lewis 电子。来源：[4.14.2](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)
- VMD 脚本同时绘制一批 AdNDP 轨道：选项 9 导出 cube → 编辑 plotAdNDP.vmd → 粘入 VMD。来源：[4.14.2](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)
- 菲用户导向搜索（两侧 6c-2e 芳香环）：选项 2 取 C–H/C–C σ 与中央 π 后 → 选项 13 定范围 → 选项 1 片段搜索 → 取高占据轨道；每侧 3 个占据≈2 的 6c-2e π 轨道。来源：[4.14.3](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)
- Au20 大团簇（100 个 1c＋10 个 4c）：搜 1c 全取 → 2c/3c 无 → 搜 4c 取前 4 再取后 6 → 选项 9 导出 101–110。来源：[4.14.4](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)
- AdNDP 轨道组成分析：选项 15（NAO 法）或选项 14（导出 .mwfn 后按 4.8 做常规分析）。来源：[4.14.3](../sec-4-14-adaptive-natural-density-partitioning-adndp-analysis.md)
