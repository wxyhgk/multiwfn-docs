# 实空间函数（Real space functions）

> Multiwfn manual, p.41–53.英文原文见同名 English 章节。 Images: `../imgs/`.

---

<!-- p.41 -->


α和β电子的ELF。

- LOCPOT：该文件记录VASP产生的一个电子感受到的外势。自旋极化时，分别记录α和β电子的势。若LVHAR=.TRUE.，该势对应静电势的负值；而若LVHAR=.FALSE.，它对应“分子中作用于一个电子的势”（PAEM，见2.7节）。

纯文本文件：该文件类型仅用于特殊功能，如绘制DOS图、绘制光谱、生成带初猜的Gaussian输入文件。见相应小节的说明。


## 2.6 实空间函数（Real space functions）

本手册中的“实空间函数”指变量为当前体系三维空间坐标的函数。实空间函数分析是Multiwfn最重要的功能之一，支持的实空间函数列表如下。所有波函数均假设为实型，所有单位均为原子单位（a.u.）。

注意，为加快计算，特别对大体系，在计算指数函数时（少数实空间函数除外，如12、14和16），若指数小于-40，则跳过该次计算。默认截断值足够安全，即使定量分析也不会造成可察觉的精度损失，也可禁用此处理或调整截断，见`settings.ini`中的“expcutoff”。

1 电子密度（Electron density）


$$\rho(\mathbf{r})=\sum_{i}\eta_{i}\left|\varphi_{i}(\mathbf{r})\right|^{2}=\sum_{i}\eta_{i}\left|\sum_{\mu}C_{\mu,i}\chi_{\mu}(\mathbf{r})\right|^{2}$$

<!-- formula-ocr: formula_p41_001.png 已替换为LaTeX, 原图保留备查 -->

其中ηi为轨道i的占据数，φ为轨道波函数，χ为基函数。C为系数矩阵，第i行第j列的元素对应轨道j相对基函数i的展开系数。电子密度的原子单位可显式写为1/Bohr3（对应6.74833/Å3，因为1 Bohr = 0.529177Å）。

当输入文件不含GTF信息时，该函数将按promolecular密度计算，即简单叠加体系中所有原子的内置球平均自由态原子密度得到的近似分子电子密度。内置原子密度如何得到见附录3。

值得注意的是，价电子密度的分布特征比电子密度信息量大得多，此点在我的工作Acta Phys. -Chim. Sin., 34, 503 (2018) DOI: 10.3866/pku.Whxb201709252中有充分讨论。

2 电子密度的梯度模（Gradient norm of electron density）


$$\left|\nabla\rho(\mathbf{r})\right|=\sqrt{\left(\frac{\partial\rho(\mathbf{r})}{\partial x}\right)^{2}+\left(\frac{\partial\rho(\mathbf{r})}{\partial y}\right)^{2}+\left(\frac{\partial\rho(\mathbf{r})}{\partial z}\right)^{2}}$$

<!-- formula-ocr: formula_p41_002.png 已替换为LaTeX, 原图保留备查 -->


<!-- p.42 -->


3 电子密度的Laplacian（Laplacian of electron density）


$$\nabla^{2}\rho(\mathbf{r})=\frac{\partial^{2}\rho(\mathbf{r})}{\partial x^{2}}+\frac{\partial^{2}\rho(\mathbf{r})}{\partial y^{2}}+\frac{\partial^{2}\rho(\mathbf{r})}{\partial z^{2}}$$

<!-- formula-ocr: formula_p42_003.png 已替换为LaTeX, 原图保留备查 -->

该函数的正值和负值分别对应电子密度局域 depleted（耗尽）和局域 concentrated（聚集）。Bader及许多其它研究者已建立∇2𝜌与价层电子对互斥（VSEPR）模型、化学键类型、电子定域性和化学反应性之间的关系。

注意，在其它一些程序如AIMALL和AIM2000中，电子密度的Laplacian定义为（−1/4）∇2𝜌，与Multiwfn给出的值相差-1/4因子。

若`settings.ini`中的“laplfac”设为非默认值1.0之外的其它值，∇2𝜌将乘以该值。

Multiwfn输出的∇2𝜌为原子单位，可显式写为1 Bohr-5（对应24.09874 Å-5，因为1 Bohr = 0.529177 Å）。

4 轨道波函数的值（Value of orbital wavefunction）；44 轨道概率密度（Orbital probability density）它们分别定义为


$$\varphi_{i}(\mathbf{r})=\sum_{\mu}C_{\mu,i}\chi_{\mu}(\mathbf{r})$$

<!-- formula-ocr: formula_p42_004.png 已替换为LaTeX, 原图保留备查 -->

从函数列表中选择这些函数时，会提示输入感兴趣轨道的序号。

5 电子自旋密度（Electron spin density）自旋密度定义为alpha与beta密度之差


$$\rho^{s}(\mathbf{r})=\rho^{\alpha}(\mathbf{r})-\rho^{\beta}(\mathbf{r})$$

<!-- formula-ocr: formula_p42_005.png 已替换为LaTeX, 原图保留备查 -->

若`settings.ini`中的“ipolarpara”设为1，则返回自旋极化参数函数而非自旋密度


$$\zeta(\mathbf{r})=\frac{\rho^{\alpha}(\mathbf{r})-\rho^{\beta}(\mathbf{r})}{\rho^{\alpha}(\mathbf{r})+\rho^{\beta}(\mathbf{r})}$$

<!-- formula-ocr: formula_p42_006.png 已替换为LaTeX, 原图保留备查 -->

ζ的绝对值从零到1，对应局域区域从非极化到完全极化。

6 Hamilton动能密度K(r)（Hamiltonian kinetic energy density K(r)）动能密度不是唯一定义的，因为由不同定义计算的动能密度积分都可恢复动能算符$\langle\varphi|-(1/2)\nabla^{2}|\varphi\rangle$的期望值。常用定义之一是


<!-- p.43 -->



$$K(\mathbf{r})=-\frac{1}{2}\sum_{i}\eta_{i}\varphi_{i}^{*}(\mathbf{r})\nabla^{2}\varphi_{i}(\mathbf{r})$$

<!-- formula-ocr: formula_p43_007.png 已替换为LaTeX, 原图保留备查 -->

7 Lagrange动能密度G(r)（Lagrangian kinetic energy density G(r)）相对K(r)，下面给出的局域动能定义处处保证为正，因此物理意义更清楚，也更常用。G(r)也称为正定动能密度。

$$G(\mathbf{r})=\frac{1}{2}\sum_{i}\eta_{i}\left|\nabla\varphi_{i}(\mathbf{r})\right|^{2}=\frac{1}{2}\sum_{i}\eta_{i}\left\{\left(\frac{\partial\varphi_{i}(\mathbf{r})}{\partial x}\right)^{2}+\left(\frac{\partial\varphi_{i}(\mathbf{r})}{\partial y}\right)^{2}+\left(\frac{\partial\varphi_{i}(\mathbf{r})}{\partial z}\right)^{2}\right\}$$


K(r)与G(r)通过电子密度的Laplacian直接关联


$$\nabla^{2}\rho(\mathbf{r})/4=G(\mathbf{r})-K(\mathbf{r})$$

<!-- formula-ocr: formula_p43_008.png 已替换为LaTeX, 原图保留备查 -->

8 来自核/原子电荷的静电势（Electrostatic potential from nuclear / atomic charges）


$$V_{\mathrm{nuc}}(\mathbf{r})=\sum_{A}\frac{Z_{A}}{\left|\mathbf{r}-\mathbf{R}_{A}\right|}$$

<!-- formula-ocr: formula_p43_009.png 已替换为LaTeX, 原图保留备查 -->

其中RA和ZA分别表示原子A的位置矢量和核电荷。若用赝势，则Z为显式表达的电子数。当用.chg文件作输入时，Z代表文件中记录的原子电荷（第四列），此时Vnu有助于分析精确静电势与原子电荷再现的静电势之差。

注意，在核位置处该函数为无穷大，可能引起程序中的数值问题，因此在这些情况下该函数恒返回1000而非无穷大。

9 电子定域函数（ELF）（Electron localization function (ELF)）区域中电子定域性越大，电子运动被束缚在其中的可能性越大。若电子完全定域，则可与外部电子区分。Bader发现电子定域性大的区域必有大幅值的Fermi hole积分。但Fermi hole是六维函数，难以直观研究。Becke和Edgecombe注意到球平均的同自旋条件对概率与Fermi hole直接相关，进而在论文J. Chem. Phys., 92, 5397 (1990)中建议了电子定域函数（ELF）。Angew. Chem. Int. Ed., 137, e202504895 (2025) DOI: 10.1002/anie.202504895是一篇很好的综述，阐明了ELF在解读电子结构中的巨大实用价值，Theoretical Aspects of Chemical Reactivity (2007)第5章提供了更多信息。

Multiwfn采用的ELF是由我推广到自旋极化体系的形式，见我的论文Acta Phys. -Chim. Sin., 27, 2786 (2011)。


<!-- p.44 -->



$$\mathrm{ELF}(\mathbf{r})=\frac{1}{1+[\boldsymbol{D}(\mathbf{r})/\boldsymbol{D}_{0}(\mathbf{r})]^{2}}$$

<!-- formula-ocr: formula_p44_010.png 已替换为LaTeX, 原图保留备查 -->

其中


$$D(\mathbf{r})=\frac{1}{2}\sum_{i}\eta_{i}\big|\nabla\varphi_{i}(\mathbf{r})\big|^{2}-\frac{1}{8}\Biggl[\frac{\big|\nabla\rho_{\alpha}(\mathbf{r})\big|^{2}}{\rho_{\alpha}(\mathbf{r})}+\frac{\big|\nabla\rho_{\beta}(\mathbf{r})\big|^{2}}{\rho_{\beta}(\mathbf{r})}\Biggr]$$
$$D_{0}(\mathbf{r})=\frac{3}{10}(6\pi^{2})^{2/3}[\rho_{\alpha}(\mathbf{r})^{5/3}+\rho_{\beta}(\mathbf{r})^{5/3}]$$

<!-- formula-ocr: formula_p44_011.png 已替换为LaTeX, 原图保留备查 -->

D 3/53/53/220 3)( rrr += ])()([)6(10 ρρπ βα

$$\mathrm{ELF}(\mathbf{r})=\frac{1}{1+[\boldsymbol{D}(\mathbf{r})/\boldsymbol{D}_{0}(\mathbf{r})]^{2}}$$


$$D(\mathbf{r})=\frac{1}{2}\sum_{i}\eta_{i}\left|\nabla\varphi_{i}(\mathbf{r})\right|^{2}-\frac{1}{8}\frac{\left|\nabla\rho(\mathbf{r})\right|^{2}}{\rho(\mathbf{r})}$$
$$D_{0}(\mathbf{r})=(3/10)(3\pi^{2})^{2/3}\rho(\mathbf{r})^{5/3}$$

<!-- formula-ocr: formula_p44_012.png 已替换为LaTeX, 原图保留备查 -->

Savin等人从动能角度重新解释了ELF，见Angew. Chem. Int. Ed. Engl., 31, 187 (1992)，这使ELF对Kohn-Sham DFT波函数甚至多组态波函数也有意义。D(r)的第一项可视为KS-DFT理论定义的非相互作用电子体系的精确动能密度，即

$$\mathrm{ELF}(\mathbf{r})=\frac{1}{1+[\boldsymbol{D}(\mathbf{r})/\boldsymbol{D}_{0}(\mathbf{r})]^{2}}$$


$$\mathrm{ELF}(\mathbf{r})=\frac{1}{1+[\boldsymbol{D}(\mathbf{r})/\boldsymbol{D}_{0}(\mathbf{r})]^{2}}$$

由Pauli排斥引起的能量密度，称为Pauli动能密度。D0(r)

可解释为Thomas-Fermi动能密度τTF，即非相互作用均匀电子气的精确动能密度。由于D0(r)作为参考引入ELF，ELF揭示的实际是相对定域程度。

ELF取值范围为[0,1]。大的ELF值意味着电子高度定域，表明存在共价键、孤对或原子的内层。ELF已广泛用于各种体系，如有机和无机小分子、原子晶体、配位化合物、团簇，以及不同问题，如揭示原子壳层结构、化学键分类、验证电荷移键、研究芳香性。

顺便说一下：有人质疑Multiwfn对多组态波函数的ELF实现。下面几段是我在电子邮件中对一位Multiwfn用户的答复，论证了Multiwfn所用上述ELF定义的合理性：

需注意ELF有不同解释，或有不同推导方式。最初Becke等人基于HF波函数的平均Fermi hole推导ELF，因此原始形式的ELF与MP2、CASSCF、CCSD等多组态波函数不兼容（甚至严格说对DFT波函数也不适用！）。我注意到有人沿Becke最初思路将ELF推广到多组态波函数，但相当复杂且难实现，故Multiwfn未采用。

相反，对多组态波函数，Multiwfn如手册2.6节所述简单基于其自然轨道计算ELF。我认为这绝非错误，而是物理上合理的。在Angew. Chem. Int. Ed. Engl., 31, 187 (1992)中，Savin等人从动能角度重新解释了ELF的物理意义，这为只要动能密度可用就可对任何波函数计算ELF铺平了道路。沿此观点，ELF表达式中涉及的三种动能密度均基于自然轨道计算。尽管此实现的结果与上述（即基于多组态波函数严格推导的Fermi hole）不完全相同，但也是严格且物理上有意义的。

简言之，对多组态波函数，ELF的实现不是唯一的，取决于如何看待ELF。

注意ELF有一个缺陷，有时r超出分子边界时，D(r)比D0(r)下降更快，ELF达到1（完全定域）。为克服此问题，Multiwfn自动给D(r)加一个极小值10-5，此处理几乎不影响感兴趣区域的ELF值。也可将`settings.ini`中的“ELF_addminimal”改为0以禁用此处理。

Tsirelson和Stash在Chem. Phys. Lett., 351, 142 (2002)中提出了近似版ELF，其中D(r)中的实际动能项用Kirzhnits型二阶梯度展开代替，即


$$(1/2)\sum_{i}\eta_{i}\left|\nabla\varphi_{i}(\mathbf{r})\right|^{2}\approx\tau_{\mathrm{T F}}(\mathbf{r})+(1/72)\left|\nabla\rho(\mathbf{r})\right|^{2}/\rho(\mathbf{r})+(1/6)\nabla^{2}\rho(\mathbf{r})$$

<!-- formula-ocr: formula_p45_013.png 已替换为LaTeX, 原图保留备查 -->


从而ELF完全不依赖波函数，可用于分析X射线衍射数据的电子密度。当然，Tsirelson的ELF也可用于分析量子化学计算的电子密度，但因动能项引入近似而不如Becke定义的ELF好，不过一般仍可恢复定性结论。若想用Tsirelson定义的ELF，将`settings.ini`中的“ELFLOL_type”由0改为1。


<!-- p.45 -->


若“ELFLOL_type”设为2，将使用另一种形式：


$$\frac{1}{1+D(\mathbf{r})/D_{0}(\mathbf{r})}$$

<!-- formula-ocr: formula_p45_014.png 已替换为LaTeX, 原图保留备查 -->

与ELF密切相关的实空间函数是SCI指数，对识别强共价键非常有用，见2.7节用户自定义函数37的介绍。

10 定域轨道定位器（LOL）（Localized orbital locator (LOL)）这是另一个类似ELF的定位高定域区域的函数，由Schmider和Becke在论文J. Mol. Struct. (THEOCHEM), 527, 51 (2000)中定义：


$$\mathrm{LOL}(\mathbf{r})=\frac{\tau(\mathbf{r})}{1+\tau(\mathbf{r})}$$

<!-- formula-ocr: formula_p45_015.png 已替换为LaTeX, 原图保留备查 -->

其中


$$\tau(\mathbf{r})=\frac{D_{0}(\mathbf{r})}{(1/2)\sum_{i}\eta_{i}\left|\nabla\varphi_{i}(\mathbf{r})\right|^{2}}$$

<!-- formula-ocr: formula_p45_016.png 已替换为LaTeX, 原图保留备查 -->


自旋极化体系和闭壳层体系的D0(r)定义与ELF中相同。

LOL与ELF表达式相似。实际上，LOL与ELF突出的化学重要区域一般定性可比。强烈建议阅读我的综述Angew. Chem. Int. Ed., 137, e202504895 (2025) DOI: 10.1002/anie.202504895，其中例证了LOL的重要实用价值。显然，LOL


<!-- p.46 -->


可像ELF一样从动能角度解释，但LOL也可从定域轨道角度解释。小的（大的）LOL值通常出现在定域轨道的边界（内部）区域，因为该处轨道波函数的梯度大（小）。LOL取值范围与ELF相同，即[0,1]。

Multiwfn也支持Tsirelson和Stash定义的近似版LOL（Acta. Cryst., B58, 780 (2002)），即LOL中的实际动能项用二阶梯度展开代替，如同他们对ELF所做的。将“ELFLOL_type”设为1即可激活此Tsirelson版LOL。

出于特殊原因，若`settings.ini`中的“ELFLOL_type”由0改为2，将使用另一种形式：21LOL( ) +r 1 [1/ ( )]τ= r。

11 局域信息熵（Local information entropy）信息熵是对信息的量化，该理论由Shannon在其噪声信道信息传输研究中提出，如今应用已大幅扩展到其它领域，包括理论化学。例如，Aslangul等尝试通过最小化信息熵将双原子和三原子分子划分为互不相交的空间（Adv. Quantum Chem., 6, 93 (1972)），Parr等讨论了信息熵与原子划分及分子相似性的关系（J. Phys. Chem. A, 109, 3957 (2005)），Noorizadeh和Shakerzadeh建议用信息熵研究芳香性（Phys. Chem. Chem. Phys., 12, 4742 (2010)）。对归一化连续概率函数的Shannon信息熵公式为


$$V_{\mathrm{ESP}}(\mathbf{r})=V_{\mathrm{nuc}}(\mathbf{r})+V_{\mathrm{ele}}(\mathbf{r})=\sum_{A}\frac{Z_{A}}{\left|\mathbf{r}-\mathbf{R}_{A}\right|}-\int\frac{\rho(\mathbf{r}^{\prime})}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|}\mathrm{d}\mathbf{r}^{\prime}$$

<!-- formula-ocr: formula_p46_017.png 已替换为LaTeX, 原图保留备查 -->

对化学体系，若将P(x)换为ρ(r)/N，则被积函数可称为电子的局域信息熵

$$V_{\mathrm{ESP}}(\mathbf{r})=V_{\mathrm{nuc}}(\mathbf{r})+V_{\mathrm{ele}}(\mathbf{r})=\sum_{A}\frac{Z_{A}}{\left|\mathbf{r}-\mathbf{R}_{A}\right|}-\int\frac{\rho(\mathbf{r}^{\prime})}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|}\mathrm{d}\mathbf{r}^{\prime}$$

其中N为当前体系总电子数。对该函数在全空间积分即得信息熵。

12 总静电势（ESP）（Total electrostatic potential (ESP)）

$$V_{\mathrm{ESP}}(\mathbf{r})=V_{\mathrm{nuc}}(\mathbf{r})+V_{\mathrm{ele}}(\mathbf{r})=\sum_{A}\frac{Z_{A}}{\left|\mathbf{r}-\mathbf{R}_{A}\right|}-\int\frac{\rho(\mathbf{r}^{\prime})}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|}\mathrm{d}\mathbf{r}^{\prime}$$

其中Z为核电荷，指标A遍历所有原子。若用赝势，则ZA为显式表示的电子数。ESP的原子单位（a.u.）为Hartree/e，其中e

为元电荷。其它常用单位有eV/e和kcal/(mol·e)，但为简便，在Multiwfn中分别打印为eV和kcal/mol。以eV/e为单位的值等于以SI单位（J/C）表示的值。

该函数衡量置于r处的单位点电荷与当前体系在不考虑电荷极化和转移时的静电相互作用能。正（负）


<!-- p.47 -->


值意味着当前位置由核（电子）电荷主导。分子静电势（ESP）长期广泛用于预测亲核和亲电位点。在研究氢键、卤键、分子识别和芳香体系分子间相互作用方面也很有价值。此外，基于统计分析，Murray等发现了一套称为GIPF的函数，见J. Mol. Struct. (THEOCHEM), 307, 55，将分子表面ESP与宏观性质联系起来。关于ESP有许多综述，建议感兴趣读者参阅WIREs Comput. Mol. Sci., 1, 153 (2011)、Theor. Chem. Acc., 108, 134 (2002)、Chemical Reactivity Theory-A Density Functional View第17章、Encyclopedia of Computational Chemistry中“Electrostatic Potentials: Chemical Applications”条目（第912页）以及Reviews in Computational Chemistry vol.2第7章。

顺便说一下，若只想得到电子贡献的静电势，即Vele(r)，可用第14个用户自定义函数。若想在计算VESP(r)时略去特定核的贡献，用第39个用户自定义函数。详见2.7节相应条目。

注1：目前Multiwfn内部有两套计算ESP的代码，可用`settings.ini`中的“iESPcode”选择。iESPcode=1对应Tian Lu编写的旧而慢的代码，iESPcode=2（默认）对应基于Jun Zhang的LIBRETA电子排斥积分库的新的快速代码。此外，在许多分析中，若你用.fch/fchk作输入文件且机器上装有Gaussian，可让Multiwfn调用Gaussian包中的cubegen工具计算ESP，若你的CPU核数少于10，速度甚至比“iESPcode=2”更快，详见5.7节。

注2：Multiwfn中有些功能会修改轨道占据。例如，可用主功能（main function）6的子功能（subfunction）26手动修改特定轨道的占据数。只有用内部代码“iESPcode=1”计算的ESP才直接反映占据修改的影响。用“iESPcode=2”时，为在ESP计算中体现修改的影响，应先将修改后的波函数导出为.wfn/wfx/molden/mwfn（经主功能（main function）100的子功能（subfunction）2），然后重启Multiwfn并载入该文件。

13 约化密度梯度（RDG）（Reduced density gradient (RDG)）

RDG与sign(λ2)ρ是揭示弱相互作用区域非常重要的一对函数，在NCI方法中联合使用，详见J. Am. Chem. Soc., 132, 6498 (2010)，应用例子见3.23.1节。RDG定义为


$$\mathrm{RDG}(\mathbf{r})=\frac{1}{2(3\pi^{2})^{1/3}}\frac{\left|\nabla\rho(\mathbf{r})\right|}{\rho(\mathbf{r})^{4/3}}$$

<!-- formula-ocr: formula_p47_018.png 已替换为LaTeX, 原图保留备查 -->

注意`settings.ini`中有参数“RDG_maxrho”，若设为x，则电子密度大于x处的RDG函数将被设为任意大值（100.0）。该机制可在观察弱相互作用区域等值面时屏蔽不感兴趣的区域。默认x为0.05，将该参数设为零可取消此处理。

14 promolecular近似下的约化密度梯度（RDG）弱相互作用对大分子的构象、蛋白与配体的结合模式有重要影响；但对如此 huge（巨大）体系由从头算重现电子密度并计算RDG的格点数据总是太耗时。幸运的是，发现promolecular密度下的弱相互作用分析仍合理。promolecular密度简单由自由态原子的电子密度叠加构造，因而可


<!-- p.48 -->


极快地计算

$$\rho^{\mathrm{p r o}}(\mathbf{r})=\sum_{A}\rho_{A}^{\mathrm{f r e e,f i t}}(\mathbf{r}-\mathbf{R}_{A})$$

free,fit(𝐫)为预拟合的原子A的球平均电子密度。H~Lr的原子密度为Multiwfn内置数据，其中H~Ar数据取自J. Am. Chem. Soc., 132, 6498 (2010)的补充材料，其它元素的数据按附录3所述计算。对重于Lr的元素目前无promolecular近似。其中𝜌𝐴

为效率考虑，若H、C、N或O原子对某点函数值的贡献小于0.00001，则不计算该贡献，对巨大体系此处理可提高数倍效率且结果几乎不受影响。也可将`settings.ini`中的“atomdenscut”设为0以禁用此处理。

`settings.ini`中的参数“RDGprodens_maxrho”是promolecular近似下“RDG_maxrho”的对应物。

15 sign(λ2)ρ


$$\Omega(\mathbf{r})=sign[\lambda_{2}(\mathbf{r})]\rho(\mathbf{r})$$

<!-- formula-ocr: formula_p48_019.png 已替换为LaTeX, 原图保留备查 -->

其中sign[λ2(r)]表示位置r处电子密度Hessian矩阵第二大本征值的符号。

16 promolecular近似下的sign(λ2)ρ 计算sign[λ2(r)]所用的实际电子密度用promolecular电子密度近似，见实空间函数14的说明。

17 交换相关密度、相关hole与相关因子（Exchange-correlation density, correlation hole and correlation factor）这些函数涉及高级课题，为阐明其物理意义并避免多种论文所用符号的混淆，我认为值得用更多篇幅介绍理论背景。更详细的讨论请参阅A Chemist's Guide to Density Functional Theory 2ed第2章和Methods of molecular quantum mechanics (2ed, McWeeny)第5章。


> **用法（Usage）**

**理论基础（Theoretical basis）**
对密度（Pair density）定义为


$$\pi(\mathbf{r}_{1},\mathbf{r}_{2})=N(N-1)\int\int\cdots\int\left|\Psi(\mathbf{x}_{1},\mathbf{x}_{2}\ldots\mathbf{x}_{N})\right|^{2}\mathrm{d}\sigma_{1}\mathrm{d}\sigma_{2}\mathrm{d}\mathbf{x}_{3}\mathrm{d}\mathbf{x}_{4}\ldots\mathrm{d}\mathbf{x}_{N}$$

其中Ψ为体系波函数，r为空间坐标，σ为自旋坐标，x为空自旋坐标。对密度表示在r1处找到一个电子同时在r2处找到另一个电子的概率，不论自旋类型。若对全空间对对密度双重积分，将得到N(N-1)，反映当前体系有N(N-1)个电子对的本质。显然，对密度可分解为不同自旋类型电子对的贡献


$$\mathbf{r}$$

<!-- formula-ocr: formula_p48_020.png 已替换为LaTeX, 原图保留备查 -->

若电子运动完全相互独立，则在r1处找到自旋σ1的电子同时在r2处找到自旋σ2的电子的概率密度应简单为


<!-- p.49 -->


$$f_{\mathrm{XC}}^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})=\frac{h_{\mathrm{XC}}^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})}{\rho^{\sigma_{2}}(\mathbf{r}_{2})}=\frac{\Gamma_{\mathrm{XC}}^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})}{\rho^{\sigma_{1}}(\mathbf{r}_{1})\rho^{\sigma_{2}}(\mathbf{r}_{2})}$$

运动是相关的。对密度因此应用交换相关密度Г修正

1212121212XC12( ,)( )( )( ,)σσσσσσπρρ=+ Γr rrrr r

若已知自旋σ1的电子出现在r1，则在r2处找到自旋σ2的另一电子的概率称为条件概率（此函数也称Lennard-Jones函数）


$$\pi^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})=\rho^{\sigma_{1}}(\mathbf{r}_{1})\rho^{\sigma_{2}}(\mathbf{r}_{2})+\Gamma_{\mathrm{X C}}^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})$$

<!-- formula-ocr: formula_p49_021.png 已替换为LaTeX, 原图保留备查 -->

相关hole揭示了当自旋σ1的电子出现在r1时，由于电子相关效应在r2处找到自旋σ2的另一电子的概率降低


$$h_{\mathrm{XC}}^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})=\frac{\Gamma_{XC}^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})}{\rho^{\sigma_{1}}(\mathbf{r}_{1})}=\Omega^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})-\rho^{\sigma_{2}}(\mathbf{r}_{2})=\frac{\pi^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})}{\rho^{\sigma_{1}}(\mathbf{r}_{1})}-\rho^{\sigma_{2}}(\mathbf{r}_{2})$$

<!-- formula-ocr: formula_p49_022.png 已替换为LaTeX, 原图保留备查 -->

相关因子是与相关hole密切相关的函数


$$f_{\mathrm{XC}}^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})=\frac{h_{\mathrm{XC}}^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})}{\rho^{\sigma_{2}}(\mathbf{r}_{2})}=\frac{\Gamma_{\mathrm{XC}}^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})}{\rho^{\sigma_{1}}(\mathbf{r}_{1})\rho^{\sigma_{2}}(\mathbf{r}_{2})}$$

<!-- formula-ocr: formula_p49_023.png 已替换为LaTeX, 原图保留备查 -->

 collectively（总体上），可写出

$$f_{\mathrm{XC}}^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})=\frac{h_{\mathrm{XC}}^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})}{\rho^{\sigma_{2}}(\mathbf{r}_{2})}=\frac{\Gamma_{\mathrm{XC}}^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})}{\rho^{\sigma_{1}}(\mathbf{r}_{1})\rho^{\sigma_{2}}(\mathbf{r}_{2})}$$

ГXC可分解为交换相关（亦称Fermi相关）部分ГX与Coulomb相关部分ГC之和，因此hXC可直接分解为交换hole hX（亦称Fermi hole）与Coulomb hole hC。同理，fXC可分解为fX和fC


$$\pi^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})=\rho^{\sigma_{1}}(\mathbf{r}_{1})\rho^{\sigma_{2}}(\mathbf{r}_{2})+\rho^{\sigma_{1}}(\mathbf{r}_{1})h_{\mathrm{X C}}^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})=\rho^{\sigma_{1}}(\mathbf{r}_{1})\rho^{\sigma_{2}}(\mathbf{r}_{2})\left[1+f_{\mathrm{X C}}^{\sigma_{1}\sigma_{2}}(\mathbf{r}_{1},\mathbf{r}_{2})\right]$$

<!-- formula-ocr: formula_p49_024.png 已替换为LaTeX, 原图保留备查 -->

Fermi相关只存在于同自旋电子之间；而Coulomb相关存在于任意两电子之间。Fermi相关远比Coulomb相关重要，即使在Hartree-Fock水平，由于Slater行列式的反对称要求，Fermi相关总能很好表示，而Coulomb完全被忽略。只有后HF波函数能同时体现Fermi与Coulomb相关效应。通常我们只关注Fermi hole而忽略Coulomb hole。易证hX在全空间积分为精确等于-1，因此Fermi相关完美避免了可能导致体系能量显著升高的自配对问题；而hC积分为零，这主要是Coulomb相关对体系能量影响较小的原因。

在只考虑交换相关或Coulomb相关时，也相当容易得到对密度和条件概率。


<!-- p.50 -->


对自旋σ的电子，不论另一电子自旋，总的π、Ω、ГXC（或ГX、ГC）与hXC（或hX、hC）可定义为


$$\Gamma_{\mathrm{XC}}^{\sigma,\mathrm{tot}}(\mathbf{r}_{1},\mathbf{r}_{2})=\Gamma_{\mathrm{XC}}^{\sigma\alpha}(\mathbf{r}_{1},\mathbf{r}_{2})+\Gamma_{\mathrm{XC}}^{\sigma\beta}(\mathbf{r}_{1},\mathbf{r}_{2})$$

<!-- formula-ocr: formula_p50_025.png 已替换为LaTeX, 原图保留备查 -->


> **用法（Usage）**

**技术方面（Technical aspects）**


对单行列式波函数，α电子的交换相关密度可显式写为

$$\Gamma_{\mathrm{X C}}^{\alpha,\mathrm{tot}}(\mathbf{r}_{1},\mathbf{r}_{2})=\Gamma_{\mathrm{X C}}^{\alpha\alpha}(\mathbf{r}_{1},\mathbf{r}_{2})=-\sum_{i\in\alpha}^{\mathrm{o c c}}\sum_{j\in\alpha}^{\mathrm{o c c}}\varphi_{i}^{*}(\mathbf{r}_{1})\varphi_{j}^{*}(\mathbf{r}_{2})\varphi_{j}(\mathbf{r}_{1})\varphi_{i}(\mathbf{r}_{2})$$

$$\begin{aligned}\Gamma_{\mathrm{C,approx}}^{\alpha,\mathrm{tot}}(\mathbf{r}_{1},\mathbf{r}_{2})&=\Gamma_{\mathrm{XC,approx}}^{\alpha,\mathrm{tot}}(\mathbf{r}_{1},\mathbf{r}_{2})-\Gamma_{\mathrm{X,approx}}^{\alpha\alpha}(\mathbf{r}_{1},\mathbf{r}_{2})\\&=\sum_{i\in\alpha}\sum_{j\in\alpha}[(\eta_{i}\eta_{j}-\sqrt{\eta_{i}\eta_{j}})\varphi_{i}^{*}(\mathbf{r}_{1})\varphi_{j}^{*}(\mathbf{r}_{2})\varphi_{j}(\mathbf{r}_{1})\varphi_{i}(\mathbf{r}_{2})]\end{aligned}$$

对β电子，只需将α换为β，下同。

对后HF波函数，精确计算对密度需二粒子密度矩阵（2PDM）。不幸的是，2PDM很难获得，包括Gaussian在内的主流量子化学软件包都不能直接输出。在Multiwfn中，后HF波函数的交换相关密度用自然轨道形式近似计算。注意近似方法不唯一，见J. Chem. Theory Comput., 6, 2736 (2010)的讨论。其中最流行、由Müller最早推导的形式目前在Multiwfn中实现如下。见Phys. Lett. A, 105, 446 (1984)，另见Mol. Phys., 100, 401 (2002)的广泛讨论（特别是方程32）。

$$\Gamma_{\mathrm{XC,approx}}^{\alpha,\mathrm{tot}}(\mathbf{r}_{1},\mathbf{r}_{2})=-\sum_{i\in\alpha}\sum_{j\in\alpha}\sqrt{\eta_{i}\eta_{j}}\varphi_{i}^{*}(\mathbf{r}_{1})\varphi_{j}^{*}(\mathbf{r}_{2})\varphi_{j}(\mathbf{r}_{1})\varphi_{i}(\mathbf{r}_{2})$$

α,tot退化为单行列式形式。so ΓXC,approx 显然，若自然自旋轨道占据数为整数（0或1），则ΓXC,approx α,tot可视为计算

交换相关密度的一般形式。注意后HF波函数已考虑非同自旋电子间的Coulomb相关，但无法分离ΓXC,approx αα和

$$\Gamma_{\mathrm{XC},\mathrm{approx}}^{\alpha,\mathrm{tot}}$$

后HF波函数的纯交换部分Г可近似计算如下（当然，αβ电子对间无交换相关）

$$\Gamma_{\mathrm{XC,approx}}^{\alpha,\mathrm{tot}}(\mathbf{r}_{1},\mathbf{r}_{2})=-\sum_{i\in\alpha}\sum_{j\in\alpha}\sqrt{\eta_{i}\eta_{j}}\varphi_{i}^{*}(\mathbf{r}_{1})\varphi_{j}^{*}(\mathbf{r}_{2})\varphi_{j}(\mathbf{r}_{1})\varphi_{i}(\mathbf{r}_{2})$$

因此纯Coulomb部分Г可计算为（包括αα和αβ对贡献）

$$\Gamma_{\mathrm{XC},\mathrm{approx}}^{\alpha,\mathrm{tot}}$$


$$\Gamma_{\mathrm{X C}}^{\alpha,\mathrm{tot}}(\mathbf{r}_{1},\mathbf{r}_{2})=\Gamma_{\mathrm{X C}}^{\alpha\alpha}(\mathbf{r}_{1},\mathbf{r}_{2})=-\sum_{i\in\alpha}^{\mathrm{o c c}}\sum_{j\in\alpha}^{\mathrm{o c c}}\varphi_{i}^{*}(\mathbf{r}_{1})\varphi_{j}^{*}(\mathbf{r}_{2})\varphi_{j}(\mathbf{r}_{1})\varphi_{i}(\mathbf{r}_{2})$$

<!-- formula-ocr: formula_p50_026.png 已替换为LaTeX, 原图保留备查 -->


<!-- p.51 -->


既然已有计算ГXC项的显式表达式，根据它们与ГXC的关系可容易算出前面介绍的其它量。回顾


$$\rho^{\sigma}(\mathbf{r})=\sum_{i\in\sigma}\eta_{i}\left|\varphi_{i}(\mathbf{r})\right|^{2}$$

<!-- formula-ocr: formula_p51_027.png 已替换为LaTeX, 原图保留备查 -->

附言：可证ΓXC,approx α,tot(𝐫1, 𝐫2)也精确满足对r2在全空间积分为−𝜌α(𝐫1)的要求。但一般，对ΓX,approx α,tot(𝐫1,𝐫2)与ΓC,approx α,tot(𝐫1, 𝐫2)对r2在全空间积分偏离精确形式ΓX α,tot与α,tot和ΓC的基本性质−𝜌α(𝐫1)和零，


> **用法（Usage）** — 在Multiwfn中，r1视为参考点，r2视为变量，定义参考点坐标只需在启动前修改`settings.ini`中的“refxyz”。

`settings.ini`中的“paircorrtype”参数控制计算Г时考虑哪类相关效应。由于相关hole与相关因子基于Г计算，此设置也影响它们。对单行列式波函数，=1与=3等价，=2无意义，因为Coulomb相关被完全忽略。

=1：只考虑交换相关 =2：只考虑Coulomb相关 =3：同时考虑交换与Coulomb相关 “pairfunctype”参数控制实空间函数17计算哪个函数和哪个自旋，见下，括号中为单行列式

波函数情形。当然，对闭壳层体系，α自旋结果与β自旋完全相同。注意，后HF波函数的相关因子无定义。

$$\Gamma_{\mathrm{XC,approx}}^{\alpha,\mathrm{tot}}(\mathbf{r}_{1},\mathbf{r}_{2})$$

$$\Gamma_{\mathrm{XC,approx}}^{\alpha,\mathrm{tot}}(\mathbf{r}_{1},\mathbf{r}_{2})$$

交换相关。该量可解释为r1处β电子在r2处引起的Fermi hole。

18 平均局域电离能（Average local ionization energy）平均局域电离能写作（Can. J. Chem., 68, 1440 (1990)）


$$\bar{I}(\mathbf{r})=\frac{\displaystyle\sum_{i}\rho_{i}(\mathbf{r})\mid\varepsilon_{i}\mid}{\rho(\mathbf{r})}$$

<!-- formula-ocr: formula_p51_028.png 已替换为LaTeX, 原图保留备查 -->

其中ρi(r)和εi分别为第i个分子轨道的电子密度函数和轨道能量。Hartree-Fock和B3LYP等典型DFT泛函都适合计算𝐼̅。𝐼̅值越低表明该点电子束缚越弱。𝐼̅用途广泛，例如揭示原子壳层结构、衡量电负性、预测pKa、量化局域极化率和硬度，但最重要的可能是


<!-- p.52 -->


预测亲电或自由基进攻的反应位点。已证明vdW表面上𝐼̅的极小值是揭示哪些原子更可能是亲电或自由基进攻优先位点的良好指标。𝐼̅还有许多潜在用途有待进一步发掘。Politzer等给出了𝐼̅的优秀综述，见J. Mol. Model., 16, 1731 (2010)和Theoretical Aspects of Chemical Reactivity (2007)第8章。

由于𝐼̅依赖轨道能量，而后HF波函数的轨道能量无定义，因此用后HF波函数时，𝐼̅处处输出为零。

若`settings.ini`中的参数“iALIEdecomp”设为1，在主功能（main function）1中不仅输出𝐼̅，还输出每个占据MO的贡献，MO i的贡献定义为


$$\overline{I}_{i}(\mathbf{r})=\frac{\rho_{i}(\mathbf{r})\mid\varepsilon_{i}\mid}{\rho(\mathbf{r})}$$

<!-- formula-ocr: formula_p52_029.png 已替换为LaTeX, 原图保留备查 -->

19 源函数（Source function）源函数由Bader和Gatti提出，见Chem. Phys. Lett., 287, 233 (1998)。


$$\rho(\mathbf{r})=\int S F(\mathbf{r},\mathbf{r}^{\prime})\mathrm{d}\mathbf{r}^{\prime}$$

<!-- formula-ocr: formula_p52_030.png 已替换为LaTeX, 原图保留备查 -->

可证

其中r'遍及全空间。此方程表明SF(r,r')表示r'处电子Laplacian对r处电子密度的影响。若r'处电子聚集（即Laplacian为负，也表明势能主导动能），则r'为r处电子密度的源；反之，若r'处电子 depleted（耗尽），则r'使r处电子密度减小。若将上式积分范围限制在局域区域Ω得到值S(r,Ω)，则S(r,Ω)/ρ(r)×100%可视为区域Ω对r处电子密度的贡献。源函数有许多用途，用于讨论成键问题时，通常取键临界点为r。Gatti在Struct. & Bond., 147, 193 (2010)中对源函数的理论背景与应用给出了非常全面的综述。

在Multiwfn中，源函数有两种模式：（1）若`settings.ini`中的“srcfuncmode”设为1，则r'视为变量，r视为固定的参考点，其坐标由`settings.ini`中的“refxyz”决定。这是默认模式，有助于研究各处电子Laplacian对特定点的影响；（2）若“srcfuncmode”设为2，则r为变量而r'为参考点，有助于研究特定点电子Laplacian对各处的影响。

当r=r'时，为避免数值问题该函数返回−∇2ρ(r')/0.001。

20、21 电子离域范围函数EDR(r;d)与轨道重叠距离函数D(r)（Electron delocalization range function EDR(r;d) and orbital overlap distance function D(r)）

本节内容及EDR(r;d)和D(r)的全部分析代码由Arshad Mehmood慷慨贡献，后经Tian Lu略作调整。


<!-- p.53 -->


电子离域范围函数EDR(r;d)（J. Chem. Phys., 141, 144104 (2014); J. Chem. Theory Comput., 12, 3185 (2016); Angew. Chem. Int. Ed., 56, 6878 (2017)）量化了波函数中r点电子占据尺寸为d的轨道瓣的程度。EDR(r;d）由

非局域单粒子约化密度矩阵（1-RDM）（, ')( ) ( ')iiγηφφ= r rrr

构建为


$$\begin{aligned}&EDR(\mathbf{r};d)=\int g_{d}(\mathbf{r},\mathbf{r}^{\prime})\gamma(\mathbf{r},\mathbf{r}^{\prime})d\mathbf{r}^{\prime}\\&g_{d}(\mathbf{r},\mathbf{r}^{\prime})=\left(\frac{2}{\pi d^{2}}\right)^{3/4}\rho^{-1/2}(\mathbf{r})\exp\left(-\frac{|\mathbf{r}-\mathbf{r}^{\prime}|^{2}}{d^{2}}\right)\\ \end{aligned}$$

<!-- formula-ocr: formula_p53_031.png 已替换为LaTeX, 原图保留备查 -->

$$\begin{aligned}&EDR(\mathbf{r};d)=\int g_{d}(\mathbf{r},\mathbf{r}^{\prime})\gamma(\mathbf{r},\mathbf{r}^{\prime})d\mathbf{r}^{\prime}\\&g_{d}(\mathbf{r},\mathbf{r}^{\prime})=\left(\frac{2}{\pi d^{2}}\right)^{3/4}\rho^{-1/2}(\mathbf{r})\exp\left(-\frac{|\mathbf{r}-\mathbf{r}^{\prime}|^{2}}{d^{2}}\right)\\ \end{aligned}$$

其中ρ(r)为r点电子密度。前置因子保证EDR在-1至+1之间。Multiwfn实现在格点上对单一全局输入的距离d计算EDR。4.5.6节给出了示例。

每点轨道重叠距离函数D(r)=argmaxdEDR(r;d)对应使EDR(r;d)最大的距离d。小的D(r)的紧凑、化学“硬”区域与大的D(r)的弥散、化学“软”区域得以区分。价电子D(r)的原子平均补充了原子部分电荷的信息。密度等值面上D(r)的图及此类表面的定量分析补充了分子静电势。Multiwfn实现在距离格点di上计算EDR(r;di)，再用三点数值拟合找最大值。4.5.7节和4.12.8节给出了计算示例。

22、23 独立梯度模型（IGM）方法定义的δg函数 δg函数在独立梯度模型（IGM）方法原始论文（Phys. Chem. Chem. Phys., 19, 17928 (2017)）中定义如下：

$$\delta g(\mathbf{r})=g^{\mathrm{I G M}}(\mathbf{r})-g(\mathbf{r})=\left|\sum_{A}\mathrm{a b s}[\nabla\rho_{A}(\mathbf{r})]\right|-\left|\sum_{A}\nabla\rho_{A}(\mathbf{r})\right|$$

其中ρA代表原子A的原子密度，abs()算子使三个梯度分量各取绝对值。具体，Multiwfn支持两种计算δg的方式：

- 实空间函数22：对应promolecular近似下计算的δg，即ρA对应孤立态原子A的球形密度，此时输入文件只需提供几何信息，因为原子密度为Multiwfn内置数据（详见附录3）。

- 实空间函数23：对应基于实际分子电子密度Hirshfeld划分计算的δg，因此输入文件必须提供波函数。该定义由我在J. Comput. Chem., 43, 539 (2022)中提出。此时ρA定义为wAρ，其中ρ为按常规方式计算的分子电子密度，wA为原子A的Hirshfeld权重函数（定义见3.9.1节）。

弱相互作用区域键临界点处的δg函数值与相互作用强度密切相关。该函数也可绘制为平面图或等值面图以揭示所有成键区域。IGM方法的详细介绍见3.23.5节，若想研究特定两 fragment（片段）或多片段间的弱相互作用，应用本节所述函数。
