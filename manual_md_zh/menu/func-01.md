# 主功能1：在某一点输出所有性质

功能概述：输入一点坐标或一原子序号，Multiwfn 支持的全部实空间函数在该点（或相应核位置）处的值一次打印到屏幕，同时输出指定函数（默认电子密度）的梯度各分量与 Hessian 矩阵；若指定函数为电子密度，还输出应力张量及其本征值/本征向量、应力张量刚度与极化率。可用 `f?` 切换被研究的函数、`o?` 切换输出波函数值的轨道、`d` 做轨道贡献分解。仅含坐标的文件（如 `.pdb`）只输出基于 promolecular 密度的有限函数。ESP 计算最贵，不需要时可将 `settings.ini` 的 `ishowptESP` 设为 0 跳过。

## 子功能/选项：在给定点输出全部实空间性质

说明：以三重态水为例，输入点坐标与单位后，一次输出密度、ELF、LOL、ESP、梯度、Hessian 本征值等全部信息（单位除注明外均为 a.u.，科学记数法如 `0.6307272576E-02` 即 0.006307272576）。`Corr. hole` 与 `Source function` 行中 `ref` 为参考点位置，由 `settings.ini` 的 `refxyz` 决定。

菜单路径：主菜单 → `1`（在某一点输出所有性质）→ 输入坐标

输入要求：GTFs（依所选函数而定）+ 原子坐标；仅坐标文件只输出 promolecular 密度的有限函数。

操作步骤（原始格式）：

```text
examples\H2O_m3ub3lyp.wfn
1  // Main function function 1, show properties at a point
0.2,2.1,2  // X, Y, Z coordinate of the point
1  // The unit of inputted coordinate is Bohr
```

输出摘录（原始格式）：

```text
Note: Unless otherwise specified, all units are in a.u.
 Density of all electrons:  0.4598301528E-02
 Density of Alpha electrons:  0.2861566387E-02
 Density of Beta electrons:  0.1736735141E-02
 Spin density of electrons:  0.1124831246E-02
 Lagrangian kinetic energy G(r):  0.3365319167E-02
 G(r) in X,Y,Z:  0.1342141336E-03  0.1888713104E-02  0.1342391929E-02
 Hamiltonian kinetic energy K(r):  0.1088761528E-03
 Potential energy density V(r): -0.3474195320E-02
 Energy density E(r) or H(r): -0.1088761528E-03
 Laplacian of electron density:  0.1302577206E-01
 Electron localization function (ELF):  0.1998328717E+00
 Localized orbital locator (LOL):  0.1008002781E+00
 Local information entropy:  0.3533635333E-02
 Interaction region indicator (IRI):  0.3583198766E+01
 Reduced density gradient (RDG):  0.2033111359E+01
 Reduced density gradient with promolecular approximation:  0.2294831921E+01
 Sign(lambda2)*rho: -0.4598301528E-02
 Sign(lambda2)*rho with promolecular approximation: -0.3918852312E-02
 Corr. hole for alpha, ref.:   0.00000   0.00000   0.00000 : -0.1251859403E-03
 Source function, ref.:   0.00000   0.00000   0.00000 : -0.3565867942E-03
 Wavefunction value for orbital       1 :  0.1536978161E-03
 Average local ionization energy (ALIE):  0.4664637535E+00
 van der Waals potential (probe atom: C ):  0.5566195299E+04 kcal/mol
 Delta-g (under promolecular approximation):  0.3210501179E-03
 Delta-g (under Hirshfeld partition):  0.2394976411E-03
 User-defined real space function:  0.1000000000E+01
 ESP from nuclear charges:  0.3453377860E+01
 ESP from electrons: -0.3439063818E+01
 Total ESP:  0.1431404144E-01 a.u. ( 0.3895049E+00 eV, 0.8982204E+01 kcal/mol)
```

电子密度梯度/Hessian 部分（原始格式）：

```text
 Note: The following information is for electron density

 Components of gradient in x/y/z are:
 -0.7919856828E-03 -0.6903543769E-02 -0.6651181972E-02
 Norm of gradient is:  0.9618959378E-02

 Components of Laplacian in x/y/z are:
 -0.3809549089E-02  0.1052804857E-01  0.6307272576E-02
 Total:  0.1302577206E-01

 Hessian matrix:
 -0.3809549089E-02  0.1394394193E-02  0.1197923973E-02
  0.1394394193E-02  0.1052804857E-01  0.1008387143E-01
  0.1197923973E-02  0.1008387143E-01  0.6307272576E-02
 Eigenvalues of Hessian: -0.3959672207E-02 -0.1883455778E-02  0.1886890004E-01
 Eigenvectors (columns) of Hessian:
  0.9964397434E+00 -0.2418531975E-01  0.8076452238E-01
 -0.4735415689E-01  0.6320255930E+00  0.7734993430E+00
 -0.6975257409E-01 -0.7745700228E+00  0.6286301443E+00
 Determinant of Hessian:  0.1407217564E-06
 Ellipticity of electron density:    1.102344
 eta index:    0.209852
 Stiffness:    0.099818

 Stress tensor:
 -0.1220815539E-02  0.1483611490E-04  0.1618000275E-04
  0.1483611490E-04 -0.1145414066E-02  0.3494514646E-04
  0.1618000275E-04  0.3494514646E-04 -0.1107965714E-02
 Eigenvalues of stress tensor: -0.1224514565E-02 -0.1166013495E-02 -0.1083667260E-02
 Eigenvectors (columns) of stress tensor:
 -0.9852173517E+00  0.7263017197E-01  0.1551503399E+00
  0.1433520595E+00  0.8453962002E+00  0.5145439259E+00
  0.9379209402E-01 -0.5291787248E+00  0.8433106903E+00
 Stress tensor stiffness:    1.129973
 Stress tensor polarizability:    0.884977
```

继续输入其它坐标可算下一点；输入 `q` 返回上级菜单。

产出：该点全部实空间函数值 + 电子密度梯度/Hessian/椭率/eta 指数/刚度 + 应力张量及本征值/刚度/极化率。

来源链接：[3.3](sec-3-3-outputting-all-properties-at-a-point.md) · [4.1.1](sec-4-1-calculate-properties-at-a-point.md)

## 子功能/选项：切换被研究函数（f?）、切换轨道（o?）、列出全部函数（allf）

说明：默认输出波函数值对应轨道 1，梯度/Laplacian/Hessian 针对电子密度。用 `f?` 指定函数（如 `f9` 选 ELF、`f10` 选 ELF 后续量全针对 ELF），`allf` 列出全部可用函数；用 `o?` 选轨道（如 `o4` 选第 4 轨、`o6` 选第 6 轨）。

菜单路径：主功能 `1` 内联命令：`f?` / `o?` / `allf`

输入要求：同上。

操作步骤（原始格式）：

```text
o6
f10
allf
```

产出：后续梯度/Hessian/本征值全部针对新选函数；波函数值行切换到新选轨道。

来源链接：[3.3](sec-3-3-outputting-all-properties-at-a-point.md) · [4.1.1](sec-4-1-calculate-properties-at-a-point.md)

## 子功能/选项：核位置取值（aN）与轨道贡献分解（d）

说明：输入 `aN` 直接取第 N 个原子核位置（如 `a1` 取原子 1 核位置），免去手输坐标，并可读“扣除自身核贡献的 ESP”。输入 `d` 把给定点实空间函数值分解为轨道贡献：每次将除轨道 $i$ 外全部占据置零再常规计算，注意非线性函数（如 ELF）各轨道贡献之和可不等于全轨道结果。

菜单路径：主功能 `1` 内联命令：`aN` / `d`

输入要求：同上；ESP 核位置分析建议 MP2/aug-cc-pVDZ 以上、post-HF 加 `density`。

操作步骤（原始格式）：

```text
a1  // Nuclear position of atom 1
a5
d
```

产出：核位置处全部性质；或各轨道对该点函数值的贡献百分比。

来源链接：[3.3](sec-3-3-outputting-all-properties-at-a-point.md)

## 子功能/选项：核位置 ESP 评估静电主导相互作用能（H₂O···HF 实例）

说明：基于核位置 ESP 定义 $\Delta\Delta V_{\mathrm{n}}=\Delta V_{\mathrm{n-D}}-\Delta V_{\mathrm{n-A}}=(V_{\mathrm{n-D'}}-V_{\mathrm{n-D}})-(V_{\mathrm{n-A'}}-V_{\mathrm{n-A}})$，其中 $V_{\mathrm{n-D'}}$ 为复合物中给体核位置扣除自身核贡献的 ESP，$V_{\mathrm{n-D}}$ 为单体中同一量的值（受体类同），再代入 $E_{\mathrm{nb}}=-89.2857\times\Delta\Delta V_{\mathrm{n}}-0.125$ 预测相互作用能。拟合级别须与原文一致（MP4(SDQ)/aug-cc-pVTZ，`examples\Vn` 下 `.wfn`；旧版 G09 做 post-HF 必须加 `density`；G09/G16 MP4 取不到密度故用 MP4(SDQ)）。实际研究可用 MP2/aug-cc-pVDZ 近似（本体系 0.0939 a.u. vs 0.0933 a.u.，成本减半）。

菜单路径：主功能 `1` → `aN` 读“扣除自身核贡献的 ESP”（复合物与单体各算一次）

输入要求：复合物 + 各单体 `.wfn`（MP2/aug-cc-pVDZ 以上，post-HF 加 `density`）；H₂O 中 O 为原子 1，HF 中 H 为原子 2。

操作步骤（原始格式）：

```text
examples\Vn\H2O-HF.wfn
1  // Calculate properties at a point
a1  // Nuclear position of atom 1
```

```text
Total ESP without contribution from nuclear charge of atom     1:
-0.2228775074E+02 a.u. ( -0.6064805E+03 eV, -0.1398579E+05 kcal/mol)
```

上即 $V_{\mathrm{n-D'}}=-22.2877$ a.u.；再输入 `a5` 得 $V_{\mathrm{n-A'}}=-0.9608$ a.u.。再分别算单体：

```text
?H2O.wfn  // The symbol ? means the folder of the file we last time loaded
1
a1  // In H2O.wfn oxygen is atom 1
```

```text
?HF.wfn
1
a2  // In HF.wfn hydrogen is atom 2
```

得 $V_{\mathrm{n-D}}=-22.3339$ a.u.，$V_{\mathrm{n-A}}=-0.9136$ a.u.，故

$$
E_{\mathrm{nb}}=-89.2857\times\Delta\Delta V_{\mathrm{n}}-0.125
$$

$$
\Delta\Delta V_{\mathrm{n}}=\Delta V_{\mathrm{n-D}}-\Delta V_{\mathrm{n-A}}=\left( V_{\mathrm{n-D'}}-V_{\mathrm{n-D}} \right)-\left( V_{\mathrm{n-A'}}-V_{\mathrm{n-A}} \right)
$$

$\Delta\Delta V_{\mathrm{n}}=-22.2877-(-22.3339)-[-0.9608-(-0.9136)]=0.0462+0.0472=0.0933$ a.u.，预测 $E_{\mathrm{nb}}=-89.2857\times0.0933-0.125=-8.45$ kcal/mol，与 Counterpoise 精确值 $-8.31$ kcal/mol 接近。

产出：四个核位置 ESP 值、$\Delta\Delta V_{\mathrm{n}}$ 与预测相互作用能。

来源链接：[4.1.2](sec-4-1-calculate-properties-at-a-point.md)
