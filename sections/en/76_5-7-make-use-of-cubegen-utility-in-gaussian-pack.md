# 5.7 Make use of cubegen utility in Gaussian package to reduce computational time of electrostatic potential analyses

> Multiwfn manual, p.1149–1149. Images: `../imgs/`.

---

<!-- p.1149 -->


### 5.7 Make use of cubegen utility in Gaussian package to reduce computational time of electrostatic potential analyses



When number of your CPU cores is very limited (less than 10), calculation speed of ESP by internal code of Multiwfn is not as fast as the cubegen utility in Gaussian package. In this circumstance, you can allow Multiwfn to invoke cubegen to calculate ESP data to reduce the overall time-consuming. Even if you have large number of CPU cores, if you need to calculate grid data of ESP (e.g. using main function 5), the time cost by internal ESP code of Multiwfn is still higher compared to allowing Multiwfn to invoke cubegen.

The way of making use of cubegen during analyses of ESP is rather easy: Set "cubegenpath" parameter in `settings.ini` file to actual path of cubegen executable file (For example, "D:\study\G16W\cubegen.exe" in Windows platform or "/sob/g16/cubegen" in Linux platform). Then if you use .fch/fchk/chk file as input file of Multiwfn, cubegen will be automatically invoked by Multiwfn at the right time to calculate ESP data.

Availability Below cases and functions currently support invoking cubegen to evaluate ESP: ·Plotting curve map of ESP (main function 3) ·Plotting plane map of ESP (main function 4) ·All functions that request grid data of ESP (e.g. using main function 5 to evaluate grid data of ESP, using main function 17 to perform basin analysis for ESP, using subfunction 14 of main function 200 to perform domain analysis for ESP)

·Calculating ESP fitting atomic charges such as CHELPG, MK and RESP (via corresponding subfunctions in main function 7)

·Calculating TrEsp charges (see Section 4.A.9 on how to do this) ·Quantitative molecular surface analysis with ESP as mapped function (main function 12) Although many other functions in Multiwfn also need ESP information, they do not support utilizing cubegen because only very few numbers of points are needed to be calculated.

Even if you are not a Gaussian user, as long as the quantum chemistry program you used can produce .mwfn or .molden file, or you are using GAMESS-US/Firefly, you can also benefits from cubegen, because by subfunction 2 of main function 100, Multiwfn can convert the loaded .mwfn/.molden/.gms file to .fch file. Then, if you use the .fch file as input file, cubegen can be invoked during ESP calculation. It is worth to note that the examples/scripts/gbw2fch.sh is a Bash shell script that converts all .gbw files of ORCA to .fch file by automatically invoking orca_2mkl in ORCA package and Multiwfn command.

Notes ·The wavefunction invoked by cubegen used for evaluating ESP comes from density matrix in .fch/fchk file. This file may contain more than one density matrices, by default the SCF density matrix is used. The type of density matrix employed can be chosen by "cubegendenstype" parameter in `settings.ini`. For example, if a .fch file was produced via "# MP2/cc-pVTZ density" keyword, then
