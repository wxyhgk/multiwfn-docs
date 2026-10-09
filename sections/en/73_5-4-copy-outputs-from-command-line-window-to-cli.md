# 5.4 Copy outputs from command-line window to clipboard

> Multiwfn manual, p.1146–1146. Images: `../imgs/`.

---

<!-- p.1146 -->

file with same name, please check the script to understand how it works. If you are unable to understand the content, just Google shell scripting.

An additional example of shell script is given below, which calculates MPP index (see Section 3.100.21) for all .mol2 file in current folder:


```text
#!/bin/bash
for filename in `ls *.mol2`
do
echo calculating $filename ...
echo -e "MPP\na\nn\nq" | Multiwfn $filename | grep "Molecular planarity parameter (MPP)"
done
```

By the way, it is noteworthy that via sed command in Linux you can easily modify content of

`settings.ini` in your script. For example, to replace "iuserfunc=□0" by "iuserfunc=□30", you can input below command


```text
sed -i 's/iuserfunc=../iuserfunc= 30/g' settings.ini
```

Substantially and flexibly employing shell scripts can automate many more kinds of analyses than those shown above. For example, in Section 4.18.6 I illustrated that with a simple script, natural transition orbitals (NTOs) of all selected excited states can be yielded and exported to various files in one run.


### 5.4 Copy outputs from command-line window to clipboard

Sometimes the output of Multiwfn in command-line windows needs to be stored permanently or loaded to third-part softwares via plain text file. Here I describe how to copy these outputs to Windows clipboard.

If you are using Windows 11, you just need to hold “ALT” key and use left mouse button to drag a rectangle region in the window, then press ENTER button, the content in the region will be copied to clipboard.

If you are using older Windows version, you need to follow the steps shown below. Assuming that you want to copy Hessian matrix of electron density.
