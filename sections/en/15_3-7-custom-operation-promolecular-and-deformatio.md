# 3.7 Custom operation, promolecular and deformation properties (options 0, -1, -2 in main functions 3, 4, 5)

> Multiwfn manual, p.97–99. Images: `../imgs/`.

---

<!-- p.97 -->

grid data to .cub file in current directory. By selecting option 3 the grid data will be exported to plain text file output.txt in current directory. Using option 4 you can set isovalue without entering GUI window and dragging slide bar, it is useful for batch process and in command-line environment. With options 5~8, you can perform addition, subtraction, multiplication and division operations on the grid data, respectively; after that, you may use option 10 to restore to original grid data.

If you only want to visualize isosurface of a specific fragment, you can select option 9 in post-processing menu, then input indices of the atoms in this fragment. After that, Hirshfeld weight of the fragment will be calculated at every grid, which will then be multiplied to the original grid data. Via this manner, value of the grid points far from the fragment will be zero, and thus will not be shown in isosurface map.

Special case: Calculate data for a set of arbitrarily distributed points If you want to use Multiwfn to calculate real space function value for a set of points (maybe arbitrarily distributed), in the interface for setting up grid, you should choose "100 Load a set of points from external file" and then input the path of the plain text file recording the points. In the file the first line should be the number of points recorded, and followed by X/Y/Z coordinates of all points. For example,


```text
1902
   -3.3790050   -2.0484700    0.0274117
   -3.3844930   -1.9472468   -0.2500274
   -3.4064601   -1.9221635   -0.1287148
   -3.4118258   -1.9232203   -0.0003350
   -3.4059106   -1.9218280    0.1351179
....
```

The coordinates must be given in Bohr. The format is in free format, and can have more than four columns of data, but the columns after the fourth one will be simply ignored.

Multiwfn will load coordinates of the points from this file, and then calculate function value for them. Finally, the X/Y/Z coordinate and function value of all points will be outputted to a plain text file, whose path is specified by users.

Information needed: Atom coordinates, GTFs (depends on the choice of real space function)


## 3.7 Custom operation, promolecular and deformation properties (options 0, -1, -2 in main functions 3, 4, 5)




### 3.7.1 Custom operation for multiple wavefunctions (0)

In main functions 3, 4 and 5, there is a subfunction that allows you to set custom operation for

multiple wavefunctions. Supported operators include + (add), − (minus), * (multiply), / (divide), there is no upper limit of the number of wavefunctions involved in custom operation. For example, if the first loaded wavefunction after booting up Multiwfn is a.wfn, then in the setting step of custom operation you inputted 2 (viz. there are two wavefunctions will be put into “custom operation list”


<!-- p.98 -->

and thus will be operated with a.wfn in turn), then you inputted -,b.wfn and *,c.wfn, the property finally you get will be [(property of a.wfn) - (property of b.wfn)] * (property of c.wfn). If you are confused, you can consult the example in Sections 4.5.4 and 4.5.5.

Sometimes the molecular structure in the first loaded file and that in the subsequently loaded files are not identical, the grid points you set will be for the first loaded file, all of the other files will share the same grid setting.

Avoid using custom operation in conjunction with main functions -4, -3 and 6, otherwise you may get absurd result.


### 3.7.2 Promolecular and deformation properties (-1, -2)

If you selected subfunction -1 in main functions 3, 4 or 5 before choosing a property (viz. a real space function), what you finally get will be promolecular property. Promolecular property is the superposition property of atoms in their free-states

$$P^{\mathrm{pro}}(\mathbf{r})=\sum_{A}P_{A}^{\mathrm{free}}(\mathbf{r}-\mathbf{R}_{A})$$

If the property you chose is electron density, then the promolecular property is generally referred to as promolecular density

$$P^{\mathrm{pro}}(\mathbf{r})=\sum_{A}P_{A}^{\mathrm{free}}(\mathbf{r}-\mathbf{R}_{A})$$

This is an artificial density that corresponds to the state when the molecule has formed but the density has not relaxed.

Deformation property is the difference between actual property and promolecular property of a molecule under the same geometry


$$P^{\mathrm{def}}\left(\mathbf{r}\right)=P^{\mathrm{mol}}\left(\mathbf{r}\right)-P^{\mathrm{pro}}\left(\mathbf{r}\right)$$

<!-- formula-ocr: formula_p98_043.png 已替换为LaTeX, 原图保留备查 -->

If the property is chosen as electron density, then the deformation property is generally called deformation density or known as electronic bonding charge distributions (BCD), which is very useful for analyzing charge transfer and bonding nature. Application example of deformation density can be found from my paper Acta Phys. -Chim. Sin., 34, 503 (2018) and Angew. Chem. Int. Ed., 137, e202504895 (2025) DOI: 10.1002/anie.202504895.


### 3.7.3 Generation of atomic wavefunctions

Evaluation of promolecular and deformation properties and some functions in Multiwfn request atomic wavefunction files, such as calculating Hirshfeld, VDD and ADCH charges, fuzzy atomic space analysis and orbital composition analysis based on Hirshfeld partition, etc. The process of generating atomic .wfn files are exactly the same.

After you select subfunctions -1 or -2 to study promolecular and deformation properties, Multiwfn checks whether .wfn files of all elements involved in present system have been presented in “atomwfn” subdirectory of current directory, if not, Multiwfn automatically invokes Gaussian to generate the missing element .wfn files and sphericalizes their densities. If the path of Gaussian executable file (“gaupath” parameter in `settings.ini`) is incorrect or has not been defined, Multiwfn


<!-- p.99 -->

will ask you to input the path of Gaussian executable file. The basis set for generating the element wavefunctions can be arbitrarily set by user, however it is suggested to use the same basis set as the molecular wavefunction.

The newly generated element wavefunction files or those taken from “atomwfn” directory are stored in “wfntmp” subdirectory in current directory. They will be translated to actual position of the atoms in present system, meanwhile atomic indices will be added to the .wfn filename (e.g. "Cr 30.wfn"). These are the files that will directly be used to calculate promolecular and deformation properties.

Details and skills If you want to avoid the step of generating element wavefunctions every time, you can move the .wfn files that without number suffix (such as C .wfn) from “wfntmp” directory to “atomwfn” directory (if “atomwfn” directory is non-existing, build it yourself), next time if Multiwfn detected that all needed element .wfn files have already been presented in “atomwfn” folder, then Multiwfn will directly use them. Multiwfn only invokes Gaussian to calculate the missing element .wfn files.

“atomwfn” subdirectory in “examples” directory contains element wavefunction files of all first four rows, they were generated under 6-31G*, and they have been sphericalized. If you want to use them, simply copy the "atomwfn" directory to current folder.

There is a quick way to generate all first four-rows element wavefunction files: the file “examples\genatmwfn.pdb” contains all first four-rows atoms, load it into Multiwfn and generate promolecular property, after the calculation of element wavefunctions is finished, copy the .wfn files that without suffix in “wfntmp” directory to “atomwfn” directory.

If your system involves elements heavier than Kr, Multiwfn is unable to generate atom wavefunction files by invoking Gaussian and sphericalize their density automatically; in that cases you have to calculate and sphericalize atom wavefunctions manually, and then put them into “atomwfn” directory, Multiwfn will directly use them.

The default theoretical method for generating wavefunction for main group elements in first four-rows (index from 1 to 20 and 31 to 36) is ROHF, for the transition metals in the fourth row, UB3LYP is used. In general, the promolecular and deformation properties are insensitive to theoretical method. If you want to specify theoretical method yourself, you can input theoretical method and basis set at the same time with slash as separator, for example BLYP/6-311G*. Do not add “RO” or “U” prefix since they will be added automatically. If error occurs during generation of atom wavefunctions, please check Gaussian input and output files in “wfntmp” directory carefully.

Notice that the maximum character length of the path of .wfn file permitted by Gaussian is only 60! The path will be truncated and cause error if the length exceeded this threshold. So do not put Multiwfn in the directory with too long path!


### 3.7.4 Sphericalization of atom wavefunction

The main purpose of Multiwfn supporting promolecular and deformation property is for generating promolecular and deformation density, however, electron density of most elements in free and ground state is not in spherical symmetry, hence will lead to orientation dependence problem. To tackle it, atomic electron density must be sphericalized. However, there is no unique way to do this. In Multiwfn, atom electron density is sphericalized by modifying atom wavefunction artificially, here I describe the detail. If you want to skip the sphericalization step, simply set the “ispheratm” in `settings.ini` to 0.
