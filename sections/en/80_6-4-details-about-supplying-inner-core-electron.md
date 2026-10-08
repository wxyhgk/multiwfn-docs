# 6.4 Details about supplying inner-core electron density for the wavefunctions involving pseudopotential

> Multiwfn manual, p.1156–1156. Images: `../imgs/`.

---

<!-- p.1156 -->

Chebyshev method was used to generate the position of radial points, and the point distribution is identical for all elements. The atomic density at any point is evaluated in terms of Lagrange interpolation method based on the points.

If you want to replace built-in atomic density of an element with that calculated yourself, after booting up Multiwfn and loading corresponding atom wavefunction file, select subfunction 10 in main function 100 (a hidden option), then Multiwfn will calculate radial electron density and output the result to sphavgval.txt in current folder. You can directly copy the Fortran codes in this file into corresponding field of atmraddens.f90.


### 6.4 Details about supplying inner-core electron density for the wavefunctions involving pseudopotential



In Section 2.5, the characteristics and the meaning of electron density function (EDF) have been introduced. EDF information is used to represent the inner-core density replaced by pseudopotential, so that for the wavefunctions involving pseudopotential, the result of the wavefunction analyses that purely based on electron density can be almost exactly identical to full-electron wavefunction.

When the input file you used contains GTF information, and meantime some atoms utilized pseudopotential, Multiwfn automatically finds proper GTF information from built-in EDF library for these atoms. The built-in EDF library was developed by Wenli Zou and coworkers, it was originally released as a part of Molden2aim program (https://github.com/zorkzou/Molden2AIM). The quality of this EDF library is quite good, and is better than the EDF field contained in the .wfx file produced by Gaussian program. This EDF library covers the entire periodic table, up to index of 120. For most elements, it contains both EDF information for large and small core pseudopotentials. Some descriptions about this library posted by its developer can be found in http://bbs.keinsci.com/thread-5354-1-1.html as well as J. Comput. Chem., 39, 1697 (2018). If you do not want Multiwfn to read EDF information from this library automatically, set "isupplyEDF" in `settings.ini` to 0.

As mentioned in Section 2.5, the .wfx file produced by Gaussian directly carries EDF field when pseudopotential is used. When this kind of file is used as input, Multiwfn by default reads EDF information from EDF field of this .wfx file rather than from the built-in EDF library. If you do not want Multiwfn to read EDF information from this file but from the built-in EDF library, you can change "readEDF" in `settings.ini` from 1 to 0.

It is noteworthy that Multiwfn also allows reading EDF information from atomic .wfx file produced by Gaussian rather than from the built-in EDF library of Multiwfn (This feature is rarely useful, since as mentioned above, the quality of the built-in EDF library in Multiwfn is better than the EDF library embedded in Gaussian). An example is provided as below:

examples\Pt(NH3)2Cl2.wfn is a file corresponding to Pt(NH3)2Cl2, Lanl2 pseudopotential accompanied by Lanl2DZ basis set is used for Pt and Cl, while 6-31G* is used for other atoms. examples\Pt_lanl2.wfx and examples\Cl_lanl2.wfx are the Pt and Cl atomic .wfx files produced by Gaussian 09, in which Lanl2 is also used, therefore their EDF fields represent the inner-core electron density of Pt and Cl replaced by Lanl2.
