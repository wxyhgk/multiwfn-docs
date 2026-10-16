# 主功能22：概念密度泛函理论（CDFT）分析

功能概述：主功能 22 一站式计算 CDFT 框架下几乎所有常用量：选项 1 生成 N/N±1（可选 N−2、N±p/q）态 Gaussian/ORCA 输入；选项 2 自动算整体指数（电离势、亲和势、电负性、硬度、软度、亲电/亲核指数）与 Hirshfeld 凝聚量并存 CDFT.txt；选项 3/9 分别算 Fukui 函数/对偶描述符与 Fukui 势/对偶描述符势格点；选项 10 算键对偶描述符；选项 4–7 算轨道加权量；选项 −3/子功能 12 处理（准）简并与开壳层；选项 8 算超离域性；子功能 11 算对偶离域描述符。

## 选项 1：CDFT 输入文件生成（Gaussian / ORCA）

说明：为 N、N+1、N−1 态（需 ω_cubic/ε 时再加 N−2；简并时为 N、N+p、N−q，另需 N±1 求 IP/EA）生成单点输入；几何取载入文件的 N 态优化几何。混合基组时当前目录备 basis.txt（含 gen/genecp 定义），内容自动追加到 .gjf 末尾。大有机体系建议 B3LYP/6-31G*。

菜单路径：主功能 22 → 选项 1（ORCA 版先经选项 −2 切换到 ORCA）。

输入要求：任意含目标体系原子信息的文件。

操作步骤（苯酚，Gaussian 默认 B3LYP/6-31G*）：

```text
examples\phenol.xyz
22  // Calculate various quantities in conceptual density functional theory
1  // Generate .wfn files for N, N+1 and N-1 electrons states
[Press ENTER button directly]  // The generated .gjf files will correspond to single point task at B3LYP/6-31G* level
[Press ENTER button directly]  // Use default charge and spin multiplicity, namely 0 1 for N state, -1 2 for N+1 state, and 1 2 for N-1 state
```

生成 N.gjf、N+1.gjf、N−1.gjf；Gaussian 跑完得 N.wfn、N+1.wfn、N−1.wfn（或 settings.ini 设 gaupath 后输入 y 让 Multiwfn 直接调用；ORCA 版设 orcapath，生成 N.inp、N−1.inp、N+1.inp）。

产出：各态 .gjf/.inp 与 .wfn 文件。

来源链接：[3.25.2](sec-3-25-conceptual-density-functional-theory-analysis.md)、[4.22.1](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md)。

## 选项 2：整体指数与凝聚量自动计算

说明：自动算 Hirshfeld 电荷并输出电离势/亲和势 $I_1 = E(N-1)-E(N)$、$A = E(N)-E(N+1)$、电负性 χ=(I₁+A)/2、化学势 μ=−χ、硬度 η=I₁−A、软度 S=1/η、亲电性 ω=μ²/(2η)、亲核性 $N_{\mathrm{Nu}} = E_{\mathrm{HOMO}}(\mathrm{Nu})-E_{\mathrm{HOMO}}$(TCE)（模块内 TCE 的 HOMO 取 B3LYP/6-31G* 的 −0.335198 Hartree；非此级别应自算修正）、凝聚 Fukui $f_A^+$/$f_A^-$/$f_A^0$、对偶描述符、凝聚局域软度/亲电/亲核/超软度、相对亲电/亲核性到 CDFT.txt。选项 −1 切 Yes 后再加 N−2 态可得 $I_2$、ω_cubic、ε 及其凝聚值。

菜单路径：主功能 22 → 选项 2（需 ω_cubic/ε 先选项 −1 切 Yes；选项 1 备 N/N+1/N−1/N−2 的 .wfn）。

输入要求：N/N+1/N−1（算 ω_cubic/ε 再加 N−2）态 .wfn/.wfx/.fch/.mwfn，几何相同；缺文件时手动输路径。

操作步骤（苯酚，已有三态 .wfn 后选 2）：输出 CDFT.txt（examples\CDFT.txt），含：

```text
 Hirshfeld charges, condensed Fukui functions and condensed dual descriptors
 Units used below are "e" (elementary charge)
     Atom     q(N)    q(N+1)   q(N-1)     f-       f+       f0      CDD
     1(C )  -0.0587  -0.1185   0.0852   0.1439   0.0598   0.1018  -0.0841
     2(C )  -0.0390  -0.1674   0.0268   0.0658   0.1284   0.0971   0.0626
     3(C )  -0.0597  -0.1873   0.0319   0.0916   0.1276   0.1096   0.0360
...[ignored]

 Condensed local electrophilicity/nucleophilicity index (e*eV)
     Atom              Electrophilicity          Nucleophilicity
     1(C )                  0.02576                  0.45535
     2(C )                  0.05533                  0.20827
     3(C )                  0.05496                  0.28982
...[ignored]

Condensed local softness (e/Hartree), relative electrophilicity/nucleophilicity (dimensionless) and condensed local hyper-softness (e/Hartree^2)
     Atom         s-          s+          s0        s+/s-       s-/s+       s(2)
     1(C )      0.3761      0.1562      0.2661      0.4154      2.4075     -0.5746
     2(C )      0.1720      0.3355      0.2538      1.9501      0.5128      0.4271
     3(C )      0.2392      0.3333      0.2863      1.3933      0.7177      0.2459
...[ignored]

 E(N):     -307.464860 Hartree
 E(N+1):     -307.383614 Hartree
 E(N-1):     -307.163438 Hartree
 E_HOMO(N):     -0.218913 Hartree,   -5.9569 eV
 E_HOMO(N+1):    0.161297 Hartree,    4.3891 eV
 E_HOMO(N-1):   -0.464864 Hartree,  -12.6496 eV
 First vertical IP:     0.301421 Hartree,    8.2021 eV
 First vertical EA:    -0.081246 Hartree,   -2.2108 eV
 Mulliken electronegativity:     0.110088 Hartree,    2.9956 eV
 Chemical potential:            -0.110088 Hartree,   -2.9956 eV
 Hardness (=fundamental gap):    0.382667 Hartree,   10.4129 eV
 Softness:      2.613235 Hartree^-1,    0.0960 eV^-1
 Softness^2:    6.828998 Hartree^-2,    0.0092 eV^-2
 Electrophilicity index:    0.015835 Hartree,    0.4309 eV
 Nucleophilicity index:     0.116285 Hartree,    3.1643 eV
```

注：涉 N+1 能量的量（EA、电负性）用弥散函数才准，建议至少 6-311+G*。

操作步骤（ω_cubic 与 ε，需 N−2 态）：

```text
-1  // Toggle calculating ω_cubic and ε
1  // Generate .wfn files for N, N+1, N-1, N-2 electronic states
[Press ENTER button directly]  // Use B3LYP/6-31G* level
[Press ENTER button directly]  // Use default charge and spin multiplicity, namely 0 1 for N state, -1 2 for N+1 state, 1 2 for N-1 state, 2 1 for N-2 state
```

跑完四个 .gjf 得 N.wfn、N+1.wfn、N−1.wfn、N−2.wfn 后选 2，CDFT.txt 新增：

```text
Cubic electrophilicity index (w_cubic):    0.021716 Hartree,    0.5909 eV
Electrophilic descriptor (epsilon):        0.080522 Hartree,    2.1911 eV
```

产出：CDFT.txt（含整体与原子指数；ω_cubic/ε 版另含 I₂ 与凝聚局域 ω_cubic）。

来源链接：[3.25.1](sec-3-25-conceptual-density-functional-theory-analysis.md)、[3.25.2](sec-3-25-conceptual-density-functional-theory-analysis.md)、[4.22.1](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md)。

## 选项 3：Fukui 函数与对偶描述符格点

说明：算 $f^+$/$f^-$/$f^0$ 与对偶描述符 Δf 格点，可视化等值面或导出 cube；乘整体软度即得局域软度 $s=Sf$；选项 −1 设缩放因子（如输软度 2.613235 即得局域软度；输 softness² 6.828998 再导出对偶描述符即得局域超软度）。

菜单路径：主功能 22 → 选项 3。

输入要求：N/N+1/N−1 态波函数文件（几何相同）。

操作步骤（苯酚 Medium 格点 + 局域量导出）：

```text
3  // Calculate grid data of Fukui function, dual descriptor and related functions
2  // Medium-quality grid
```

可视化 $f$ 与 Δf（等值面 0.007 a.u.）。导出局域亲电指数：选项 −1 输 0.4309（eV 单位全局亲电指数），再选 5 导出 scaled f+（f+.cub，eV/Bohr³）。导出局域超软度：选项 −1 输 6.828998（Hartree⁻² 单位 softness²），再选 5 导出 scaled DD（DD.cub，a.u.）。

操作步骤（C₆₀ 简并情形局域超软度/局域软度）：

```text
3  // Calculate grid data of Fukui function, dual descriptor and related functions
-10  // Set extension distance
6  // 6 Bohr, which is slightly larger than the default one to avoid isosurface truncation at box boundary when isovalue is set to a small value
3  // Since C_60 is not small, we use high-quality grid to guarantee that grid spacing will not be too large and thus leading to poor isosurface map
-1  // Set the scale factor to various grid data
21.514996  // Square of softness in Hartree^-2
8  // Export grid data of scaled dual descriptor as DD.cub in current folder
```

```text
-1  // Set the scale factor to various grid data
4.638426  // Softness in Hartree^-1
6  // Export grid data of scaled f- as f-.cub in current folder
```

产出：$f$ / Δf / $s$ / 局域超软度等值面与 .cub 文件。

来源链接：[3.25.2](sec-3-25-conceptual-density-functional-theory-analysis.md)、[4.22.1](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md)。

## 选项 9：Fukui 势与对偶描述符势

说明：算 ${V}_{f^+}$/${V}_{f^-}$（各态 ESP 差，如 ${V}_{f^-} = V_{N-1}^{\mathrm{ESP}}-V_{N}^{\mathrm{ESP}}$）与 $DDP = V_{f^+}-V_{f^-}$ 格点；${V}_{f^+}$ 越正越易亲核反应，${V}_{f^-}$ 越正越易亲电反应，DDP 正/负分别易亲核/亲电。ESP 格点开销大，宜用稀疏格点。

菜单路径：主功能 22 → 选项 9。

输入要求：N/N+1/N−1 态波函数文件。

操作步骤（马来酸酐，M06-2X/6-311++G(d,p) 复现文献）：

```text
examples\maleic_anhydride.xyz  //Geometry was optimized at M06-2X/6-311++G(d,p) level
22  // Conceptual DFT (CDFT) analysis
1  // Generate .wfn files for N, N+1, N-1 electrons states
M062X/6-311++G(d,p)  // Keywords of Gaussian to perform single point calculations
[Press ENTER button]  // Use (0 1), (-1 2) and (1 2) for N, N+1 and N-1 states
y  // Invoke Gaussian to calculate the three states (assume that you have properly set “gaupath” in settings.ini)
9  // Calculate grid data of Fukui potential and dual descriptor potential
1  // Because calculating ESP grid data is relatively expensive, so here we choose to use low-quality grid
```

产出：${V}_{f^+}$、${V}_{f^-}$、DDP 等值面图（DDP 绿色处如 C4/C5 最易亲电攻击）。

来源链接：[3.25.1](sec-3-25-conceptual-density-functional-theory-analysis.md)、[4.22.4](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md)。

## 选项 10：键对偶描述符 BDD

说明：键 $A$–$B$ 的 ${BDD}_{A,B}={f}_{A,B}^{+}-{f}_{A,B}^{-}$，${f}_{A,B}^{+}=P(N+1)-P(N)$、${f}_{A,B}^{-}=P(N)-P(N-1)$，P 取 Hirshfeld 模糊键级；负为亲核键、正为亲电键。支持简并情形（先选项 −3 设 p/q）。

菜单路径：主功能 22 → 选项 10。

输入要求：各电子态 .wfn 文件（由选项 1 生成输入后计算得到）。

操作步骤（丙烯腈）：

```text
22  // Conceptual DFT (CDFT) analysis
1  // Generate .wfn files for N, N+1, N-1 electrons states
[Press ENTER button directly]  // The generated .gjf files will correspond to single point task at B3LYP/6-31G* level
[Press ENTER button directly]  // Use default charge and spin multiplicity, namely 0 1 for N state, -1 2 for N+1 state, and 1 2 for N-1 state
```

跑完 N.gjf、N−1.gjf、N+1.gjf 得三态 .wfn 后选 10，依次载入各态算模糊键级并有限差分，输出如：

```text
10 most negative BDD values:
    1(C )     3(C ):    -0.562
    6(C )     7(N ):    -0.365
    3(C )     7(N ):    -0.029
    2(H )     3(C ):    -0.009
    1(C )     4(H ):    -0.008
    1(C )     5(H ):    -0.008
    4(H )     7(N ):    -0.001
    4(H )     5(H ):    -0.000
    5(H )     7(N ):    -0.000
    2(H )     4(H ):     0.000

10 most positive BDD values:
    1(C )     6(C ):     0.312
    1(C )     7(N ):     0.166
    3(C )     6(C ):     0.064
    3(C )     5(H ):     0.016
    3(C )     4(H ):     0.016
    2(H )     6(C ):     0.006
    2(H )     7(N ):     0.004
    5(H )     6(C ):     0.003
    4(H )     6(C ):     0.003
    1(C )     2(H ):     0.001
```

C1–C3 最亲核、C1–C6 最亲电（不直接成键的对忽略）。选 y 导出 BDD.txt（按原子序）与 BDD_sorted.txt（按数值排序）。

产出：各键 BDD 值 + BDD.txt / BDD_sorted.txt。

来源链接：[3.25.1](sec-3-25-conceptual-density-functional-theory-analysis.md)、[4.22.5](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md)。

## 选项 4–7：轨道加权 Fukui 函数与对偶描述符

说明：以前线轨道高斯权重混合近简并轨道，$f_w^\pm$/$f_w^0$/$\Delta f_w$ 分布符合分子对称性，解决简并体系反应位点预测。Δ 初猜 0.1 Hartree。选项 4 设 Δ；选项 5 查前 10 权重；选项 6 算 Hirshfeld 凝聚值；选项 7 算格点并可视化/导出 cube。Δf_w 对应自定义函数 98，可作平面图与表面极值分析。

菜单路径：主功能 22 → 选项 4（设 Δ）→ 选项 5（查权重）→ 选项 6（凝聚值）/ 选项 7（格点）。

输入要求：闭壳层单行列式文件（.mwfn/.fch/.molden/.gms；算虚轨道参与量时不用弥散函数）。

操作步骤（C₆₀）：

```text
C60.fch
22  // Calculate various quantities in conceptual density functional theory
```

```text
7  // Calculate grid data of OW Fukui function and OW dual descriptor
2  // Medium quality
```

等值面取 0.0003 a.u.；[6,6] 键上方 Δf_w 最负，最易亲电攻击。选项 5 输出如：

```text
 10 Highest weights in orbital-weighted f+
 Orbital   181 (LUMO  )   Weight:  12.47 %   E_diff:     1.752 eV
 Orbital   182 (LUMO+1)   Weight:  12.47 %   E_diff:     1.752 eV
 Orbital   183 (LUMO+2)   Weight:  12.47 %   E_diff:     1.752 eV
 Orbital   184 (LUMO+3)   Weight:   6.32 %   E_diff:     2.847 eV
 Orbital   185 (LUMO+4)   Weight:   6.32 %   E_diff:     2.847 eV
 Orbital   186 (LUMO+5)   Weight:   6.32 %   E_diff:     2.847 eV
 Orbital   187 (LUMO+6)   Weight:   4.70 %   E_diff:     3.207 eV
 Orbital   188 (LUMO+7)   Weight:   4.70 %   E_diff:     3.207 eV
 Orbital   189 (LUMO+8)   Weight:   4.70 %   E_diff:     3.207 eV
 10 Highest weights in orbital-weighted f-
 Orbital   180 (HOMO  )   Weight:   9.06 %   E_diff:    -1.752 eV
 Orbital   179 (HOMO-1)   Weight:   9.06 %   E_diff:    -1.752 eV
 Orbital   178 (HOMO-2)   Weight:   9.06 %   E_diff:    -1.752 eV
 Orbital   177 (HOMO-3)   Weight:   9.06 %   E_diff:    -1.752 eV
 Orbital   176 (HOMO-4)   Weight:   9.06 %   E_diff:    -1.752 eV
 Orbital   175 (HOMO-5)   Weight:   5.02 %   E_diff:    -2.728 eV
 Orbital   174 (HOMO-6)   Weight:   5.02 %   E_diff:    -2.728 eV
 Orbital   173 (HOMO-7)   Weight:   5.02 %   E_diff:    -2.728 eV
 Orbital   172 (HOMO-8)   Weight:   5.02 %   E_diff:    -2.728 eV
 Orbital   171 (HOMO-9)   Weight:   5.02 %   E_diff:    -2.728 eV
```

环[18]碳 Δf_w 平面图（settings.ini 设 iuserfunc=98）：

```text
C18.fchk
4  // Plot plane map
100  // User-defined real space function, which now corresponds to ∆f_w
1  // Color-filled map
[Press ENTER button to use default grid setting]
1  // XY plane
0  // Z=0
```

产出：${f}_{w}$ / $\Delta f_w$ 等值面、权重表、凝聚值、cube（如 OW_DD.cub）。

来源链接：[3.25.3](sec-3-25-conceptual-density-functional-theory-analysis.md)、[4.22.2](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md)。

## 选项 −3：基于电子密度的（准）简并 Fukui 函数（闭壳层）

说明：直接基于电子密度、考虑弛豫的 $f_Q^\pm = (\rho_{N+p}-\rho_N)/p$、$(\rho_N-\rho_{N-q})/q$ 及 Δf_Q；p/q 按前线轨道能量差判定（差 < 0.01 eV 视简并），态多重度通常取 p+1/q+1。非简并时退化为普通 $f$/Δf。

菜单路径：主功能 22 → 选项 −3（设 FMO 简并度 p/q）→ 选项 1（生成输入）→ 选项 2/3。

输入要求：N、N+p、N−q（及 N±1 求 IP/EA）态波函数文件。

操作步骤（苯，p=q=2）：

```text
examples\benzene.fch
22  // Calculate various quantities in conceptual density functional theory
-3  // Set degree of frontier molecular orbital degeneracy
```

屏幕列 10 个最低非占据轨道（如 LUMO/LUMO+1 皆 0.100 eV）输 2；再列 10 个最高占据轨道（如 HOMO/HOMO−1 皆 −6.720 eV）输 2。然后：

```text
1  // Single point input files of Gaussian for generating .wfn files for N, N+2, N-2 states will be prepared (If you are an ORCA user, you can choose option -2 to change to ORCA program before selecting this option)
[Press ENTER button]  //Use the default B3LYP/6-31G* level for single point calculation
[Press ENTER button]  //As mentioned in prompt, pressing ENTER button directly will use net charge and spin multiplicity of (0 1), (-2 3) and (2 3) for the N, N+2 and N-2 states, respectively. These combinations are reasonable for present case
```

N+1/N−1 不需则两次回车跳过；跑完得 N.wfn、N+2.wfn、N−2.wfn 后：

```text
3  // Calculate grid data of Fukui function and dual descriptor (if N.wfn, N+2.wfn and N-2.wfn are not present in current folder, Multiwfn will ask you to input path of wavefunction files of the three states)
2  // Medium-quality grid
2  // Visualize isosurface of f^-
```

等值面 0.005 a.u.，$f^- = (\rho_N-\rho_{N-2})/2$ 符合分子对称性。注意：$f^+$ 宜用 ωB97XD 等长程校正泛函 + 无弥散 3-zeta 基（如 6-311G*），B3LYP + 弥散基因自相互作用误差致阴离子过度弥散。

操作步骤（C₆₀，ωB97XD/6-311G*，p=3/q=5 自动判定）：

```text
C60_wB97XD_opt.fchk
22  // Calculate various quantities in conceptual density functional theory
-3  // Set degree of frontier molecular orbital degeneracy
[Press ENTER button directly]  // Use automatically determined LUMO degeneracy of 3
[Press ENTER button directly]  // Use automatically determined HOMO degeneracy of 5
1  // Generate .wfn files for various electrons states
wB97XD/6-311G* symm=loose scf=conver=7  // Keywords for performing single point task of Gaussian. The “symm=loose” ensures that Gaussian will utilize I_h point group of C_60 to greatly reduce cost. “scf=conver=7” slightly loosens SCF convergence threshold to make it easier to reach
-1,2  // Net charge and spin multiplicity of N+1 state
1,2  // Net charge and spin multiplicity of N-1 state
```

得 N/N−1/N+1/N−3/N+5 的 .wfn 后选项 2 算量（Softness 4.638426 Hartree⁻¹，Softness² 21.514996 Hartree⁻²），再选项 3 导出局域超软度/局域软度（见选项 3 节命令）。

产出：考虑简并的 $f_Q$/Δf_Q 等值面与局域性质。

来源链接：[3.25.4](sec-3-25-conceptual-density-functional-theory-analysis.md)、[4.22.3](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md)。

## 子功能 12：开壳层 Fukui 函数与对偶描述符

说明：按自旋数变化类型（ΔN_S<0 / >0 / ≈0）分别计算 $f^+$/$f^-$/对偶描述符格点并可视化或导出 .cub；原则上 $\Delta f_{\Delta N_S\approx 0}$ 最理想。

菜单路径：主功能 22 → 子功能 12 → 选项 1（设简并度）→ 选项 2（生成输入）→ 选项 3（格点）。

输入要求：含基函数与全部轨道的波函数文件。

操作步骤（O₂，HOMO/LUMO 简并，LUMO(α)=1、HOMO(α)=2、LUMO(β)=2、HOMO(β)=2）：

```text
examples\O2.fch  // Wavefunction file of ground state O_2 at B3LYP/6-31G* level
22  // Calculate various quantities in conceptual density functional theory
12  // Calculate Fukui function and dual descriptor based on formalism of conceptual spin-polarized DFT
1  // Set degeneracy of frontier molecular orbitals
[Press ENTER button directly]  // Use suggested degeneracy of LUMO(α)
[Press ENTER button directly]  // Use suggested degeneracy of HOMO(α)
[Press ENTER button directly]  // Use suggested degeneracy of LUMO(β)
[Press ENTER button directly]  // Use suggested degeneracy of HOMO(β)
```

```text
[Press ENTER button directly]  // Use suggested degeneracy of HOMO(β)
```

```text
2  //Generate .wfn files for various electrons states
[Press ENTER button directly]  // Use the default B3LYP/6-31G* as computational level for generating Gaussian input files
```

生成 state0_3.gjf、state−1_4.gjf、state−2_1.gjf、state2_1.gjf、state2_5.gjf，跑完得各态 .wfn 后选 3（Medium 格点），后处理如选 7 画 $\Delta f_{\Delta N_S<0}$（等值面 0.0005 a.u.）。

产出：各 ΔN_S 形式的 Fukui/对偶描述符等值面与 .cub。

来源链接：[3.25.4](sec-3-25-conceptual-density-functional-theory-analysis.md)、[4.22.3](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md)。

## 选项 8：亲核/亲电超离域性

说明：基于 Hirshfeld 轨道组成（与弥散函数兼容）：$D^{\mathrm{N}}(A)=2\sum_i^{\mathrm{unocc}}\Theta_{A,i}/(\alpha-\varepsilon_i)$、$D^{\mathrm{E}}(A)=2\sum_i^{\mathrm{occ}}\Theta_{A,i}/(\varepsilon_i-\alpha)$，另有不含 α 的 $D^{\mathrm{N0}}$/$D^{\mathrm{E0}}$；均为负值。

菜单路径：主功能 22 → 选项 8。

输入要求：闭壳层单行列式文件（.mwfn/.fch/.molden/.gms；算 D_N 时不用弥散函数）。

操作步骤：载入输入文件后进主功能 22 选 8，直接打印各原子 $D_N$/$D_E$/$D_{N0}$/$D_{E0}$（examples\oxirane.fchk 示例）：

```text
    Atom             D_N                D_E              D_N_0             D_E_0
    1(C )        -26.56182        -10.85916        -35.92863         -8.75591
    2(C )        -26.56182        -10.85916        -35.92863         -8.75591
    3(O )        -20.09086        -19.14131        -25.62598        -14.71454
    4(H )        -10.19410         -2.66387        -14.52037         -2.13024
    5(H )        -10.19410         -2.66387        -14.52037         -2.13024
    6(H )        -10.19410         -2.66387        -14.52037         -2.13024
    7(H )        -10.19410         -2.66387        -14.52037         -2.13024

Sum of D_N:        -113.99092 /Hartree
Sum of D_E:         -51.51513 /Hartree
Sum of D_N_0:      -155.56471 /Hartree
Sum of D_E_0:       -40.74734 /Hartree
```

产出：各原子超离域性列表。

来源链接：[3.25.5](sec-3-25-conceptual-density-functional-theory-analysis.md)。

## 子功能 11：对偶离域描述符 DDD

说明：定量离域指数对得失电子响应的不对称性：输出 $f^+$/$f^-$/$f^{(1)}$/$g^+$/$g^-$/$f^{(2)}$；闭壳层、冻结轨道近似，只需 N 态波函数。注意本实现 $g^-$ 为原文表 2 值的两倍才是正确值（严格按原文 Eq.29 应加倍）。

菜单路径：主功能 22 → 子功能 11 → 选项 1（AIM 划分）/ 选项 2（Hirshfeld 划分）/ 选项 3（载入已有 AOM；模糊/盆模块导 AOM 前 settings.ini 设 ispecial=3）。

输入要求：闭壳层含基函数波函数文件（.fch/.molden 等）。

操作步骤（氨基苯，Hirshfeld 划分，1–6 键）：

```text
aminobenzene_DDD.fch  // The file in the compressed package mentioned above
22  // Conceptual DFT (CDFT) analysis
11  // Calculate dual delocalization descriptor (DDD)
2  // Calculate AOM via Hirshfeld partition
```

输入 `1,6` 得：

```text
Result of    1(C )   --    6(C )
f-:      0.067452
f+:      0.026544
g-:      0.017868
g+:      0.011229
f(1):   -0.040907
f(2):   -0.056481
```

产出：指定键的 DDD 各分量。

来源链接：[3.25.6](sec-3-25-conceptual-density-functional-theory-analysis.md)、[4.22.6](sec-4-22-examples-of-conceptual-density-functional-theory-cdft-analysis.md)。
