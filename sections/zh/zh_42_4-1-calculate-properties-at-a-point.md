# 计算某点处的性质

> Multiwfn manual, p.468–471.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.468 -->




## 4.1 计算某点处的性质


### 4.1.1 显示三重态水在给定点处的所有性质

本例 illustrate 如何为三重态水计算给定点处的多种实空间函数。启动 Multiwfn 并输入以下命令

!!! terminal "Multiwfn 交互"

    - **examples\H2O_m3ub3lyp.wfn 1** — 主功能 1，显示某点处的性质
    - **0.2,2.1,2** — 该点的 X、Y、Z 坐标
    - **1** — 输入坐标的单位为 Bohr 此时 Multiwfn 支持的所有实空间函数在该点处的值连同电子密度梯度/Laplacian 分量、Hessian 矩阵及其本征值/本征向量一并打印。若不能完全理解输出，请仔细阅读 2.6 与 2.7 节，输出中的所有术语都有非常详细的描述。


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
```


<!-- p.469 -->




```text
 Total ESP:  0.1431404144E-01 a.u. ( 0.3895049E+00 eV, 0.8982204E+01 kcal/mol)

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

所有数据均以科学计数法表示，E 之后的值为指数，例如 0.6307272576E-02 对应 0.006307272576。

在“Corr. hole (correlation hole)（相关洞）”与“Source function（源函数）”行中，所谓“ref”为参考点位置，由 `settings.ini` 中的“refxyz”参数决定。

默认输出的波函数值对应轨道 1，可输入例如 o6 以选择轨道 6。


<!-- p.470 -->



默认情况下，梯度与 Laplacian 分量以及 Hessian 及其本征值/本征向量均为针对电子密度的。可输入诸如 f10 以选择序号为 10 的实空间函数（即 ELF），之后所有这些量均为针对 ELF 的。若想查询所有可用实空间函数的序号，输入 allf。

可继续输入其他坐标，当想返回上一级菜单时，输入 q；若想退出程序，按“CTRL+C”键或直接关闭命令行窗口。


### 4.1.2 计算核位置处的 ESP 以评估 H2O∙∙∙HF 的相互作用强度

这是一个高级例子，若对弱相互作用不感兴趣，可跳过本节。

在 J. Phys. Chem. A, 118, 1697 (2014) 中，Mohan 与 Suresh 研究了一批以静电为主的相互作用体系，包括氢键、卤键与双氢键，它们都属于电子给体-受体相互作用，其中给体指富电子片段（Lewis 碱），而受体为缺电子片段（Lewis 酸）。他们拟合出一条 surprisingly 好的

直线方程，将 ΔΔVn 指数与各类相互作用的相互作用能（Enb）关联起来，R2 高达 0.9762。其结果可总结为下图

对于以静电为主的复合物，假设我们能得到 ΔΔVn，则根据上图所示方程，可轻松预测相互作用能为


$$E_{\mathrm{n b}}=-89.2857\times\Delta\Delta V_{\mathrm{n}}-0.125$$

<!-- formula-ocr: formula_p470_336.png 已替换为LaTeX, 原图保留备查 -->

ΔΔVn 基于核位置处的 ESP 定义为

$$\Delta\Delta V_{\mathrm{n}}=\Delta V_{\mathrm{n-D}}-\Delta V_{\mathrm{n-A}}=(V_{\mathrm{n-D^{\prime}}}-V_{\mathrm{n-D}})-(V_{\mathrm{n-A^{\prime}}}-V_{\mathrm{n-A}})$$

其中 Vn-D' 为复合物环境中给体原子核位置处的 ESP，但忽略该给体原子核的贡献。Vn-D 与 Vn-

D' 的唯一区别在于前者在单体状态下计算，因此 ΔVn-D = Vn-D' - Vn-D 可视为


![](../imgs/p470_081.png)

<!-- p.471 -->



由于另一分子的存在而引起的给体原子核位置处 ESP 的变化，它直接反映分子间相互作用的强度。Vn-A' 与 Vn-A 的定义与 Vn-D'、Vn-D 完全相同，只是针对受体原子计算。

本例中，我们计算 H2O∙∙∙HF 的 ΔΔVn，并检验基于 ΔΔVn 预测的相互作用能是否真的接近精确计算的相互作用能。在此复合物中 H2O 的氧为电子给体原子，HF 的氢为电子受体原子。由于 Mohan 与 Suresh 给出的方程是针对特定计算级别拟合的，为恰当使用其方程，这里采用的计算级别与他们完全相同。下面使用的 .wfn 文件在 MP2/6-311++G** 优化几何下以 MP4(SDQ)/aug-cc-pVTZ 级别产生，这些 .wfn 文件与相应的 Gaussian 输入文件可在“examples\Vn”文件夹中找到。

注意若使用较旧版本的 G09 且采用 post-HF 方法，“density”关键词不可或缺，否则生成的 .wfn 文件中的密度将对应 Hartree-Fock 密度。此外，在 G09 与 G16 中，MP4 级别无法产生密度，因此我们改用 MP4(SDQ) 关键词（MP4 关键词默认为 MP4(SDTQ），比 MP4(SDQ）更精确但昂贵得多）。

首先，我们计算 Vn-A' 与 Vn-D'。启动 Multiwfn 并输入 examples\Vn\H2O-HF.wfn 1 // 计算某点处的性质 a1 // 原子 1 的核位置 从输出中可见


```text
Total ESP without contribution from nuclear charge of atom     1:
-0.2228775074E+02 a.u. ( -0.6064805E+03 eV, -0.1398579E+05 kcal/mol)
```

即 Vn-D' 为 -22.2877 a.u.。再输入 a5，可发现 Vn-A' 为 -0.9608 a.u.。

接下来计算 Vn-D。重新启动 Multiwfn 并输入以下命令 ?H2O.wfn // 符号 ? 表示上次载入文件所在文件夹 1 a1 // H2O.wfn 中氧为原子 1 发现 Vn-D 为 -22.3339 a.u.。再计算 Vn-A。重启 Multiwfn 并输入

?HF.wfn 1 a2 // HF.wfn 中氢为原子 2 发现 Vn-A 为 -0.9136 a.u.。

于是 ΔΔVn 为 -22.2877-(-22.3339) - [-0.9608-(-0.9136)] = 0.0462 + 0.0472 = 0.0933 a.u.。用前面提到的方程，相互作用能可近似预测为

-89.2857×0.0933-0.125 = -8.45 kcal/mol，该值与 Mohan 与 Suresh 在 MP4/aug-cc-pVTZ 级别加 Counterpoise 校正得到的精确相互作用能（-8.31 kcal/mol）相当接近。

即使对如本例研究的小复合物，在 MP4(SDQ)/aug-cc-pVTZ 下产生波函数也相当耗时，因此找到一个能显著节省计算时间又不牺牲太多精度的计算级别很重要。对当前体系，基于 MP2/6-311++G** 几何，我尝试用几个级别评估 ΔΔVn：

B3LYP/6-311+G**: 0.1021 a.u. MP2/cc-pVTZ: 0.1052 a.u. MP2/aug-cc-pVTZ: 0.0955 a.u. B3LYP/aug-cc-pVTZ: 0.0985 a.u. MP2/aug-cc-pVDZ: 0.0939 a.u. B3LYP/aug-cc-pVDZ: 0.0980 a.u. 在 MP2/aug-cc-pVDZ 下产生的 ΔΔVn（0.0939）与我们上面在 MP4(SDQ)/aug-cc-pVTZ 下得到的值（0.0933）非常接近，而计算开销降低了两倍。因此，在实际研究中，
