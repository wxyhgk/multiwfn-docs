# 6.6 Special functions

> Multiwfn manual, p.1158–1158. Images: `../imgs/`.

---

<!-- p.1158 -->


### 6.6 Special functions

There are some special functions in Multiwfn, they are mainly used for debugging, special purposes, and some of them are requested by some Multiwfn users. Here a few of them are mentioned.

6.6.1 Add Bq atoms at specific positions

Sometimes we want to highlight special positions on a 3D map, for example, the reference point, centroid position of a real space function, the position used to plot local DOS and so on. To realize this, you can enter main function 1000, select subfunction 12, and manually input the X, Y, Z coordinate of the Bq atoms (ghost atoms) to be added. You can add arbitrary number of Bq atoms. Once all Bq atoms have been added, input q to return. Then in the GUI showing 3D molecular structure you will see the Bq atoms, which are displayed as cyan spheres. It is worth to note that in the main function 0, you can choose showing or not showing labels of Bq atoms by selecting corresponding term in "Other settings" - "Set atomic label type".

6.6.2 Calculate nuclear attractive energy between a fragment and an orbital

You can use this function by entering subfunction 90 of main function 1000 (hidden in main menu). This function calculates attractive energy between all nuclei in a user-defined fragment and an orbital, namely:

$$E_{\mathrm{M O}i-\mathrm{f r a g}}=\left\langle\varphi_{i}\right|\sum_{A\in\mathrm{f r a g}}\frac{Z_{A}}{\left|\mathbf{r}-\mathbf{R}_{A}\right|}\left|\varphi_{i}\right\rangle\equiv\int\left|\varphi_{i}(\mathbf{r})\right|^{2}\sum_{A\in\mathrm{f r a g}}\frac{Z_{A}}{\left|\mathbf{r}-\mathbf{R}_{A}\right|}\mathrm{d}\mathbf{r}$$

During the calculation, the atomic contributions to the result are outputted in turn, for example, below output


```text
Processing center     2(H )   /     3
Accumulated value:       -8.3269642826  Current center:       -0.0629848533
```

means

$$E_{\mathrm{M O}i-\mathrm{f r a g}}^{\mathrm{2H}}=\int w_{2\mathrm{H}}(\mathbf{r})\left|\varphi_{i}(\mathbf{r})\right|^{2}\sum_{A\in\mathrm{f r a g}}\frac{Z_{A}}{\left|\mathbf{r}-\mathbf{R}_{A}\right|}\mathrm{d}\mathbf{r}=-0.06298$$

where w2H(r) is atomic weighting function of 2H atom defined by Becke's partition.

The integral is evaluated by Becke's multi-center integration method, therefore the "radpot" and "sphpot" in `settings.ini` affect integral accuracy. Commonly the default value is accurate enough. Note that, as shown in above formula, the occupation number of orbital is not taken into account in the calculation.

Information needed: GTFs, atom coordinates

6.6.3 Output Becke's integration points

The Becke's multi-center numerical integration algorithm proposed in J. Chem. Phys., 88, 2547 (1988) has been employed by almost all popular quantum chemistry programs to integrate
