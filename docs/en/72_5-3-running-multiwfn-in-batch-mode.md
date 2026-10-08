# 5.3 Running Multiwfn in batch mode

> Multiwfn manual, p.1144–1145. Images: `../imgs/`.

---

<!-- p.1144 -->

Content orbana_1_3.in | ./Multiwfn.exe COCl2.fch > orbana_1_3.txt

For Linux / MacOS users If you are a Linux or Mac OS user, you can not only run Multiwfn silently as introduced above, but also make use of "echo" command to avoid explicitly writing an input stream file. The last example can be equivalently realized by running this command:


```text
echo -e "8\n1\n1\n2\n3" | Multiwfn COCl2.fch > orbana_1_3.txt
```

Each \n means pressing ENTER button once.

If you prefer to use shell script, you can also add below lines into your shell script file:


```text
Multiwfn COCl2.fch > orbana_1_3.txt << EOF
8
1
1
2
3
EOF
```


### 5.3 Running Multiwfn in batch mode

Note: If you can read Chinese, please read Sections 3 and 4 of my blog article “Detailed introduction to the command line running and batch running methods of Multiwfn” (http://sobereva.com/612) instead, in which more detailed information about using shell script to run Multiwfn to automatically process batch of files is introduced, and some illustrative scripts are given and carefully explained.

If you are familiar with writing shell scripts and you have carefully read last section, you must have already known how to use Multiwfn to process a batch of files, it is indeed very easy. I will briefly introduce this point in this section.

For Windows users

- Example 1 Assume that you want to generate .cub files of ELF for these input files: ultravox.wfn, chinaski.fch, strawberry_egg.wfn, you can create a plain text file named batchrun.bat (the suffix must be .bat, while file name is arbitrary) with the following content:


```text
Multiwfn ultravox.wfn < genELFcub.txt > null
move ELF.cub ultravox.cub
Multiwfn chinaski.fch < genELFcub.txt > null
move ELF.cub chinaski.cub
Multiwfn strawberry_egg.wfn < genELFcub.txt > null
move ELF.cub strawberry_egg.cub
del null
```

where genELFcub.txt is input stream file for generating ELF cube file, it is a plain text file having the content below

5  Main function 5, calculate grid data

9  Real space function 9, namely ELF

2  Option 2: Medium-quality grid

2  Option 2: Exporting cube file in current directory


<!-- p.1145 -->

Put all of aforementioned files into a folder containing Multiwfn.exe, then double click the icon "batchrun.bat" or input command batchrun in command line window, the task will start and the three ELF cube files will be generated in current folder sequentially.

- Example 2 Shell script is very useful and powerful, it can automate a lot of repetitive work. As a simple example, you want to generate ELF .cub file for all .wfn files in current folder, and hope that the name of the resulting .cub files are [Input_file_name]_ELF.cub, then you can write a .bat file with the following content


```text
for /f %%i in ('dir *.wfn /b') do (
Multiwfn %%i < genELFcub.txt > null
rename ELF.cub %%~ni_ELF.cub
)
```

Run the .bat file, the .cub files will yield in turn. Assume that one of input files is yoshiko.wfn, the corresponding resulting .cub file will be yoshiko_ELF.cub.

For Linux users Similarly, you can run Multiwfn under Linux environment in batch mode and write script to significantly make your research easier. To realize the aforementioned example 1 under Linux, you can create a file runthree.sh with the following content (assume that you have properly installed Multiwfn as mentioned in Section 2.1.2 and thus you can directly invoke Multiwfn by Multiwfn command)


```text
Multiwfn ultravox.wfn < genELFcub.txt > null
mv ELF.cub ultravox.cub
Multiwfn chinaski.fch < genELFcub.txt > null
mv ELF.cub chinaski.cub
Multiwfn strawberry_egg.wfn < genELFcub.txt > null
mv ELF.cub strawberry_egg.cub
rm null
```

Put the runthree.sh and all input files in current folder, run this command: chmod +x ./runthree.sh;./runthree.sh, then the calculation will start. (The chmod +x command is used to add executable permission, it may not be necessary for certain cases)

To realize the aforementioned example 2 under Linux, you should create a shell script file with the content below and then run it


```text
#!/bin/bash
for inf in *.wfn
do
echo Running ${inf} ...
Multiwfn ${inf} < genELFcub.txt > /dev/null
mv ELF.cub ${inf//.wfn}_ELF.cub
done
```

The shell environment of Linux platform is much more powerful than Windows. The examples\scripts\gjf2xyz.sh is a Bash shell script that converts all .gjf files in current folder to .xyz
