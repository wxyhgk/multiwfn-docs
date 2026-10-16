# 主功能21：能量分解分析

功能概述：主功能 21 提供四类能量分解：子功能 1 的 EDA-FF（基于分子力场的片段间静电/排斥/色散分解，适用于数百至上万原子）；子功能 2 的 Shubin Liu 能量分解（需 Gaussian 输出 + .fch）；sobEDA / sobEDAw（外部 sobEDA.sh 脚本，作者强烈推荐，通用稳健）；子功能 4 的原子对色散能贡献分析（基于 DFT-D3(BJ)，支持周期体系与两体系差值、色散密度）。

## 子功能 1：EDA-FF 能量分解

说明：基于经典力场把片段间相互作用分解为静电、排斥（交换排斥）、色散三项：

$$
E_{IJ}^{\mathrm{ele}}=\sum_{A\in I}\sum_{B\in J}E_{AB}^{\mathrm{ele}}\qquad E_{IJ}^{\mathrm{rep}}=\sum_{A\in I}\sum_{B\in J}E_{AB}^{\mathrm{rep}}\qquad E_{IJ}^{\mathrm{disp}}=\sum_{A\in I}\sum_{B\in J}E_{AB}^{\mathrm{disp}}
$$

注意“弱相互作用”指相隔三个以上化学键的原子间作用，不能用于化学键本质讨论。力场默认 AMBER99 & GAFF（选项 −1 可换 UFF；一般不建议 UFF，易高估排斥致总能量为正）。静电算符默认 1/r（选项 −2 可改 1/r² 以有效体现水屏蔽）。选项 −3 输出原子对明细 interatm.txt；选项 −4 输出按能量贡献着色的 .pqr（atmint_tot/ele/rep/disp/vdW.pqr，按 charge 着色）。

菜单路径：主功能 21 → 子功能 1。

输入要求：体系几何文件（.xyz/.mol/.pdb/.fch 等）+ 分子列表文件（记录各分子类型文件路径与数目）+ 分子类型文件（原子类型 + 电荷；UFF 只需电荷一列）。电荷建议 ESP 拟合电荷（CHELPG/MK，主功能 7 子功能 12/13；大体系可用 EEM，主功能 7 子功能 17）。原子类型：AMBER 见 *J. Am. Chem. Soc.*, **117**, 5179 (1995) 表 1；GAFF 见 *J. Comput. Chem.*, **25**, 1157 (2004) 表 1；`examples\EDA\EDA_FF` 下 AMBER99.txt/GAFF.txt 可查；UF 类型写作 UF 即用 UFF 参数。

操作步骤（水二聚体）：分子列表 mollist.txt 内容为：

```text
water.txt 2
```

分子类型 water.txt 内容为：

```text
OW -0.737121
HW  0.368560
HW  0.368560
```

启动 Multiwfn 并输入：

```text
dimer.mol  // The file containing dimer structure information (you can also use other formats containing the geometry information as input file, such as the .fch file produced during optimization task of the dimer)
21  // Energy decomposition analysis
1  // Energy decomposition analysis based on forcefield
3  // Load atom types and atomic charges
mollist.txt  // The actual path of the molecular list file. At this point, the program read atom types and charges from the water.txt and assign them to the two water molecules in the current system
2  // Define fragments
2  // Two fragments will be defined
1-3  // The atomic indices of the fragment 1
4-6  // The atomic indices of the fragment 2
```

选项 4 检查电荷/类型指派，选项 1 开始计算。输出（kJ/mol）：

```text
Contribution of each atom in defined fragments to overall interfragment interac
tion energies:
 Atom    1(O )   Elec:   12.53  Rep:    3.85  Disp:   -2.21  Total:   14.17
 Atom    2(H )   Elec:   -6.24  Rep:    0.00  Disp:    0.00  Total:   -6.24
 Atom    3(H )   Elec:  -16.87  Rep:    0.00  Disp:    0.00  Total:  -16.87
 Atom    4(O )   Elec:  -23.52  Rep:    3.85  Disp:   -2.21  Total:  -21.88
 Atom    5(H )   Elec:    6.47  Rep:    0.00  Disp:    0.00  Total:    6.47
 Atom    6(H )   Elec:    6.47  Rep:    0.00  Disp:    0.00  Total:    6.47

 Interaction energy components between all fragments:
                         Electrostatic   Repulsive   Dispersion     Total
 Frag   1 -- Frag   2:       -21.15         7.71        -4.43       -17.87
```

操作步骤（C3GC 三聚体，三个片段）：

```text
C3GC.pdb
21  // Energy decomposition analysis
1  // EDA-FF
3  // Load atom types and charges
mollist.txt  // Input actual path of mollist.txt
2  // Define fragments
3  // Three fragments will be defined
1-13  // Atom indices in fragment 1, namely cytosine (C)
14-29  // Atom indices in fragment 2, namely guanine (G)
30-101  // Atom indices in fragment 3, namely C3
```

输出：

```text
                         Electrostatic   Repulsion   Dispersion     Total
 Frag   1 -- Frag   2:      -120.98        60.26       -45.54      -106.27
 Frag   1 -- Frag   3:         1.88        44.86       -94.69       -47.95
 Frag   2 -- Frag   3:         0.71        62.08      -132.62       -69.84
```

重定义两片段（GC 对 vs C3）再算：

```text
2  // Redefine fragments
2  // Two fragments will be defined
1-29  // Fragment 1, the GC base pair
30-101  // Fragment 2, the C3 part
1  // Start the EDA-FF calculation
```

产出：每对片段的静电/排斥/色散/总量（kJ/mol）及原子贡献；interatm.txt（原子对距离与分量）；.pqr 文件供 VMD 按 charge 着色。

来源链接：[3.24.1](sec-3-24-energy-decomposition-analysis.md)、[4.21.1](sec-4-21-energy-decomposition-analysis.md)。

## 子功能 2：Shubin Liu 能量分解（EDA-SBL）

说明：总能量分解为 $E=E_{\mathrm{steric}}+E_{\mathrm{electrostatic}}+E_{\mathrm{quantum}}$，其中 $E_{\mathrm{steric}}=T_{\mathrm{W}}=|\nabla\rho|^{2}/[8\rho]$，$E_{\mathrm{quantum}}=E_{\mathrm{Pauli}}+E_{\mathrm{XC}}$。Multiwfn 读 Gaussian 输出相关量并算位阻项，同时打印 Pauli 动能等中间量。

菜单路径：主功能 21 → 子功能 2。

输入要求：.fch/.fchk + 含 `ExtraLinks=L608` 分解量的 Gaussian 输出。输入文件末尾按泛函写 IOp(3/74) 值：−73 (MN15)、−58 (ωB97XD)、−55 (M06-2X)、−54 (M06)、−53 (M06L)、−40 (CAM-B3LYP)、−35 (TPSSh)、−13 (PBE0)、−5 (B3LYP)、−6 (B3PW91)、−3 (BHandHLYP)、402 (BLYP)、1009 (PBE)、2523 (TPSS)；G16 用 ultrafine 格点时序号后加 5（如 −55 5）。

操作步骤（先准备特殊 Gaussian 输入，乙烷 staggered 为例）：

```text
%chk=H2O.chk
# B3LYP/6-31G* ExtraLinks=L608

Optimized water

0 1
O 0.00000000     0.00000000     0.11930801
H 0.00000000     0.75895306    -0.47723204
H 0.00000000    -0.75895306    -0.47723204

-5
```

Gaussian 算完后 formchk 转 .fch，启动 Multiwfn 并输入：

```text
examples\EDA\EDA_SBL\ethane_staggered.fch
21  // Energy decomposition analysis
2  // Shubin Liu's energy decomposition
examples\EDA\EDA_SBL\ethane_staggered.out
```

输出：

```text
 E_steric:              64.213411 Hartree
 E_electrostatic:     -146.114859 Hartree
 E_quantum:              2.037465 Hartree

 E_total:              -79.863983 Hartree
```

对 eclipsed 重复上述流程，两构象差值（kJ/mol）：ΔE_tot 11.2、ΔE_steric 15.3、ΔE_electrostatic 18.5、ΔE_quantum −22.7，位垒主要来自空间位阻与静电，量子项抵消。

产出：三项能量分量 + Pauli 动能等中间量。

来源链接：[3.24.2](sec-3-24-energy-decomposition-analysis.md)、[4.21.2](sec-4-21-energy-decomposition-analysis.md)。

## sobEDA / sobEDAw 能量分解（外部脚本）

说明：基于色散校正 DFT 的稳健、高效、通用、易用的能量分解，作者强烈推荐。无主功能菜单入口，用 sobEDA.sh 脚本配合 Gaussian + Multiwfn 运行。

菜单路径：主功能 21 之外（sobEDA.sh 脚本）。

输入要求：Gaussian 算的复合物与片段能量文件（见 sobEDA 教程）。

操作步骤：按 `sobEDA_tutorial.zip`（<http://sobereva.com/soft/sobEDA_tutorial.zip>）流程运行脚本；理论见 *J. Phys. Chem. A*, **127**, 7023 (2023)；讨论见 <http://sobereva.com/685>。

产出：sobEDA / sobEDAw 分解结果（详见教程）。

来源链接：[3.24.3](sec-3-24-energy-decomposition-analysis.md)、[4.21.3](sec-4-21-energy-decomposition-analysis.md)。

## 子功能 4：原子对色散能贡献分析

说明：基于以 B3LYP 拟合参数的 DFT-D3(BJ) 色散校正能：原子贡献 ${\varepsilon}_{A}=(1/2)\sum_{B\ne A}{\varepsilon}_{A,B}$；色散密度

$$
{\rho}_{\mathrm{disp}}\left( \mathbf{r} \right)={\left( \frac{\pi}{\alpha} \right)}^{-3/2}\sum_{A} {\varepsilon}_{A}{e}^{-\alpha{(\mathbf{r}-{\mathbf{R}}_{A})}^{2}}
$$

（α 通常 0.5）；支持两体系差值 Δε_A / Δρ_disp、片段对贡献、两片段间色散作用能；支持周期体系。需经 Tian Lu 修改的 dftd3 程序（<http://sobereva.com/soft/dftd3_TLmod.zip>），`settings.ini` 中 `dftd3path` 指向可执行文件（Linux 下 chmod +x）。

菜单路径：主功能 21 → 子功能 4。

输入要求：原子信息文件（.xyz/.pdb/.mol2/.gjf/.fch/.mwfn；含晶胞信息即按周期体系算）。两体系差值比较时感兴趣原子数与顺序必须一致。

操作步骤（6-helicene 原子贡献 + 色散密度 + 片段间作用能）：

```text
examples\helicene.xyz  // Structure file of 6-helicene
21  // Energy decomposition analysis
4  // Analysis of atomic contribution to dispersion energy
1  // Calculate atomic contributions to dispersion energy for current system
```

屏幕输出总色散 −74.468 kcal/mol 及各原子贡献；输入 y 导出 atomdisp.pqr（VMD 按 charge 着色，色标 −5.0~5.0）。选项 2 算色散密度（选 Medium-quality grid），导出 dispdens.cub（kcal/mol/Bohr³）。选项 6 算两片段间色散作用能，如输入 `17-22` 再输入 `11-12,23-26` 得 −2.809 kcal/mol。

操作步骤（Actos 卷曲 vs 线型构象差值）：

```text
examples\Actos_curly.xyz
21  // Energy decomposition analysis
4  // Analysis of atomic contribution to dispersion energy
3  // Calculate difference of atomic contributions to dispersion energy between current and another systems
[Press ENTER button]  // All atoms in the present system (Actos_curly.xyz) are of interest
examples\Actos_linear.xyz
[Press ENTER button]  // All atoms in Actos_curly.xyz are of interest
```

输入 y 导出 diffatomdisp.pqr（坐标同 curly，charge 为 curly−linear 差值）。色散密度差值：

```text
4  // Calculate dispersion density difference between current and another system
[Press ENTER button]  //All atoms in the present system (Actos_curly.xyz) are of interest
examples\Actos_linear.xyz  // Another system
```

操作步骤（沸石–甲苯周期体系差值）：

```text
examples\zeolite-mol.cif
21  // Energy decomposition analysis
4  // Analysis of atomic contribution to dispersion energy
3  // Calculate difference of atomic contributions to dispersion energy between current and another systems
1-216  // The atoms of interest are those of the zeolite moiety (first 216 atoms) in the current system (zeolite-mol.cif)
examples\zeolite.cif  // Another system
[Press ENTER button directly]  // The atoms of interest are all 216 atoms in zeolite.cif, which also correspond to atoms 1-216 in zeolite-mol.cif
y  // Export diffatomdisp.pqr in current folder
```

产出：总色散能、各原子贡献（屏幕 + atomdisp.pqr）、dispdens.cub、差值 diffatomdisp.pqr / dispdensdiff.cub、片段对/片段间色散作用能。

来源链接：[3.24.4](sec-3-24-energy-decomposition-analysis.md)、[4.21.4](sec-4-21-energy-decomposition-analysis.md)。
