---
layout: examples
title: Compiled Tutorial
permalink: /examples/comp_tut/
---

<script src="dist/js/bind-polyfill.js"></script>
<script src="dist/js/smooth-scroll.js"></script>



<a name="topcall"></a>
#Table of Contents:


* [VMD Tutorials](#vmd)
	* [How to get a 3-D protein structure](#3dprot)
	* [How to find a Ligand](#ligand)
	* [How to find a Residue](#residue)
	* [How to Mutate a Protein](#mutate)
* [PDB2PQR Tutorial](#PDB2PQR)
	* [Introduction to PDB2PQR](#IntroPDB)
	* [Downloading a PDB or PQR file for Offline APBS](#Download)
* [APBS Tutorial](#APBS)
	* [Introduction to APBS](#IntroAPBS)
	* [How to run a protein through APBS (online)](#OnlineAPBS)
	* [Setting up your computer for APBS](#SetupAPBS)
	* [How to run APBS from the command line](#CMDAPBS)
	* [Dime Value Problems](#Dimes)
* [APBS and Visualization](#APBSvis)
	* [PyMol](#PyMol)
	* [VMD](#VMD)
* [Precursor Requirements](#)
	* [Download VMD](http://www.ks.uiuc.edu/Research/vmd/)
	* [Download Pymol](http://www.pymol.org/)
	* [Download APBS and PDB2PQR](http://www.poissonboltzmann.org/docs/downloads/)
	* [Download Git](http://git-scm.com/)  
	* [Download Python](https://www.python.org/) (*This is written using Python 2.7 )
	* [Download Matplotlib](http://matplotlib.org/)

<a data-scroll href="#vmd">vmd</a>
...
<span id="bazinga">Bazinga!</span>

## VMD

<a name="3dprot"></a>
### How to get a 3-D protein structure 

1. Go to desired Protein Page [(pic)](http://oi60.tinypic.com/2zs8xti.jpg)

2. On the right hand corner, hit the "download files" option  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_1.png)  
<img src="https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_1.png?url=https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_1_big.png" class="dg-picture-zoom">

3. Now, select desired file type. For this tutorial, the PBD File (TEXT) was selected  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_2.png)  
Once you click the file, download should start immediately. Save the file in desired location.

4. Next, open up VMD  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_3.png)

5. Click ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_4.png), then click "new molecule" A Molecule File Browser will pop up as such  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_5.png)  

6. Click "Browse...", and then click and open saved Protein file. 
Go below to "Determine File Type", and click file type, which in this case, is PDB
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_6.png)
Click the "Load" button, and your saved protein will load in the VMD window as a 3-D protein structure

[Click here to return to the top of the page](#topcall)
<hr/>

<a name="ligand"></a>
######How to find a Ligand

1. First, your 3-D protein structure should be loaded
on the VMD Main window, click 
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_7.png), and then click 
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_8.png)

2. Next, the Graphical Representations Window will open  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_9.png)

3. Under 
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_10.png), delete the text "all" and enter "resname (insert name of desired compound here)"

4. Hit 
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_11.png)
and the chosen ligand will appear

[Click here to return to the top of the page](#topcall)
<hr/>
<a name="residue"></a>
######How to find a Residue

1. First, your 3-D protein structure should be loaded
on the VMD Main window, click 
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_12.png), and then click 
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_13.png)

2. Next, the Graphical Representations Window will open  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_14.png)

3. Under ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_15.png), delete the text "all" and enter "resid (insert residue number)" to find the desired residue number

4. Hit ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_16.png)and the chosen residue will appear

[Click here to return to the top of the page](#topcall)
<hr/>
<a name="mutate"></a>
######How to Mutate a Protein

1.  First, one must take their pdb file (taken from pdb.org) and convert it into a psf file. This is done by hitting ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_17.png) in the VMD main window, then ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_18.png), and finally ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_19.png). You will this on your screen:  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_20.png)
\*For this example, we'll use the pdb protein 1JLB.

2. Molecule simply names the molecule you want to make into a psf file. ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_21.png) is the name of your soon-to-be psf file; change it if you wish. Then hit ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_22.png)  

3. For the next section, keep automatic settings and hit ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_23.png) 

4. For the next section as well, keep automatic settings and hit ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_24.png)

5. When the following window pops up, click "ok"
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_25.png)

6. If, perhaps an error window pops up:  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_26.png)  
simply click ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_27.png) and the error messages will clear. However this may jeopardize the quality of the mutated protein. 

7. Click ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_28.png), and then you will have the psf file saved in your files. 

8. Now we can go on to really mutating our residue. Hit ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_29.png) in the VMD main window, then ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_30.png), and finally![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_31.png). Then, the following window will open:  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_32.png)  

9. Upload the psf and pdb files of your protein. For the field marked MUTATED, retype the name you wish your mutated file to be called.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_33.png) refers to the original residue your target residue was  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_34.png) is the residue number  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_35.png) is the amino acid of your desired mutation.  
An example of the procedure, is if you wanted to change a wild type HIV-1 Reverse Transcriptase Tyrosin to Cysteine, then ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_36.png) would be TYR, ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_37.png) would be 181, and ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_38.png) would be CYS  
You do not have to check the ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_39.png) in order to mutate your residue.  

10. Finally, click ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_40.png)  
The mutated protein will now appear in your VMD window 

[Click here to return to the top of the page](#topcall)
<a name="PDB2PQR"></a>
##PDB2PQR

<a name="IntroPDB"></a>
######Introduction to PDB2PQR

[Use the online pdb2pqr website to run pdb2pqr](http://nbcr-222.ucsd.edu/pdb2pqr_1.9.0/) (changes file from pdb to the pqr format, this adds missing hydrogens, adds some missing heavy atoms, and optimizes the protein structure among other things)

First, go to the PDB2PQR website above. You should already have a selected protein form pdb.org in mind.
_(My example will be using the protein 2HNY)_

Since I want my file to be compatible with VMD, for the both settings named "Pick a forcefield to use:" and "Pick an output naming scheme to use", choose the option CHARMM (PARSE works as well). 

* To run with apbs, you need to change the setting in pdb2pqr to  
 _Insert white spaces between atom name and residue name, between x and y, and between y and z_

* With PDB2PQR, unfortunately the program deletes any stray ligands that are in the molecule, which means to mutate accordingly a MOL2 file must be taken (which most are available at the ZINC database website). 

An interesting thing to keep in mind whilst using pdb2pqr:
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_41.jpg)

[Click here to return to the top of the page](#topcall)
<a name="Download"></a>
######Downloading a PDB or PQR file for Offline APBS 

1. After running PDB2PQR from the website, click on the file under "Input Files" labeled something like "14084693082.pdb" (the number will be different but it will have a .pdb ending). This should start a download   
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_42.jpg)  
**\*(It is useful to rename the file to 1FAS.pdb because it gets confusing when you have many different strings of numbers for different proteins)**

2. If the link didn't download, right click on this link and click "Save link as..." and save the file where you want to be able to find it.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_43.jpg)  
**\*(You should rename this file too)**

3. Now you should download the same numbered file under "Output files" (mine is called 1408469302.pqr). This time you cannot click on it (as it will just bring up the a webpage with all the information in the file. You must right click and "Save link as..." this time. Also make sure the downloaded file ends in a .pqr but once again the number will not be the same as the one in this picture.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_44.jpg)

[Click here to return to the top of the page](#topcall)
<a name="APBS"></a>
##APBS

<a name="IntroAPBS"></a>
######Introduction to APBS

APBS is a useful tool to find the electrostatic field of a protein. Certain components need to be in place for APBS to work including _white spaces must be in place_  

<a name="OnlineAPBS"></a>
######How to run a protein through APBS (online)

The steps follow the same steps in making a PDB2PQR protein model structure, except for a small difference. 

1. When making the PDB2PQR, check the option for allowing the program to have an APBS option, and in addition adding the insert white space link in the options, like so: 
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_45.png)  

2. Then, click submit, and it will take you to the page for the PDB2PQR runned protein. On the bottom of the page, click ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_46.jpg) and wait until APBS is done running.  

3. Then download the .dx.gz file, and that is the end of your APBS session.

\* Note: Unzipping the .dx.gz file can be done using any unzipping program 

[Click here to return to the top of the page](#topcall)
<a name="SetupAPBS"></a>
######Setting up your computer for APBS

*DISCLAIMER: THIS IS FOR WINDOWS USERS ONLY (?)

In order to run APBS using command line, you will need to first download the APBS binary from http://sourceforge.net/projects/apbs/ as well as download the newest python version 2 release (https://www.python.org/download/releases/2.7.2/  as of 8/8/2014). 

Why use the command line? It gives the user much more power over executable functions, immediately unzips the file, and is quite simple to use. 

1. First, in order to run APBS at all, you need to make a directory connecting APBS to the command line. 
To do so, go to the start menu, and right click on 'computer' The following should open:  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_47.png)  

2. Click on properties, and the following should open:  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_48.png)  

3. Click on 'Advanced System Settings' ; the computer will ask you if you want to change settings. Click yes, and then the system properties window will open.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_49.png)  

4. Click 
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_50.png), and another window will pop up.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_51.png)  

5. This is where you'll write your path. Click on the 
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_52.png) to create a new path.  

6. TO make the directory, simply copy and paste  
**C:\Python27\;C:\Python27\Scripts;C:\Util\pdb2pqr-windows-bin-1.9.0;C:\apbs\bin**  
and click ok. 

You can now run APBS!

[Click here to return to the top of the page](#topcall)
<a name="CMDAPBS"></a>
######How to run APBS from the command line

####DISCALIMER: THIS TUTORIAL IS USING A WINDOWS COMPUTER AND WINDOWS COMMAND PROMPT

1. First, before running APBS through the command line, you must make sure your desired protein files are in the same folder as the apbs command prompt. If APBS downloaded correctly, it should be in your C drive (![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_53.png)) when you open "computer" from your start menu. 

2. Click on the APBS folder, and in the APBS folder make a new folder for all your proteins; please label the folder accordingly, and remember the name of the folder. 

3. It is important to remember, that when putting protein files in the folder, you need to put both the PQR as well as the corresponding IN file. PQR and IN files can both be obtained from the PDB2PQR webserver.   
(A PQR file is the information about the protein, whereas the IN file is a command file that tells APBS how to calculate the electrostatic fields. The In file is unique to one PQR file (as it specifies its commands to only one PQR file) and also holds other information such as dimensions and calculation specifications. Both files are needed to run APBS)  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_54.png)
_An example of the pdb2pqr webserver and the pqr and in files_

4. Now that the folders are set up, you can open the command line. To open up the start menu, type in cmd.exe and open the command prompt; this is the command line execution for APBS.
The command prompt should look something similar to this:  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_55.png)  

5. Of course, our PQR and IN files are not in this location, so we'll have to go back to our C:\ drive, then to our APBS Folder, then to our designated protein folder. To do so, in the command prompt hit "space", cd, "space", .., then enter. Your command prompt should look like the following:  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_56.png)  
As you can see, this makes our prompt go up one directory. To go to the C:\ drive, type in the same command, and hit "enter"  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_57.png)  

6. Now, type "space", "cd", "space", "apbs" and hit "enter". You are now in your APBS folder. To get to your folder of proteins, type in "cd", "space", then type in the first letter of your folder name and hit "tab" until your folder name pops up. Then hit "enter"   
(_What the tab key does is find all files that start with the letters you have typed, for example, if you typed "i", then tab, the command prompt would go down, alphabetically, all your files in the folder that start with "i"_)  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_58.png)  

7. Now that you are in your folder with your PQR and IN files, using the tab shortkey (as mentioned above), type the first letter of your 
desired IN file. This is very important; apbs does not need the PQR file, it needs the IN file to operate.  
Once you find your IN file, hit enter and APBS will run its calculations and save a DX file (File containing electrostatic fields coordinates) in your folder. 

You are done running APBS!

[Click here to return to the top of the page](#topcall)
<a name="APBSvis"></a>
##APBS and Visualization

<a name="PyMol"></a>
######PyMol

[The needed protein for this PyMol tutorial](http://www.rcsb.org/pdb/explore/explore.do?structureId=1fas) (1FAS a.k.a Fasciculin-1).  Fasciculin-1 is an acetylcholinesterase (this compound ends the communication between muscle cells) inhibitor found in the venom of the green mamba. This allows the action potential to go uncurbed which causes small involuntary muscle contractions (it paralyzes the injected subject).

To set up the molecule follow the **"Introduction to PDB2PQR"** instructions above.

1. Open the PQR file you are going to be using so you can edit it, and go down to where all the **"HETATM"** are (these should all be HOH which is water). Select them all and delete them. Save the file.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_59.jpg)
It should look something like this:  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_60.jpg)

2.  Load the newly saved PQR file you had into PyMOL (File → Open...) and choose your favorite graphical representation of the molecular structure (often the easiest to view is "showing (**S**)" the cartoon representation and "hiding (**H**)" lines). 
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_61.jpg)
 
3. Next go to the Plugin tab and open APBS Tools... (where ... is a number referring to the  version). In the window that comes up, click "Use another PQR" and then "Choose Externally Generated PQR:".   
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_62.jpg)

4. Now find the file that you created using the webserver and click ok.    
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_63.jpg)

5. Go into "My Computer" and in the upper right corner and type in apbs.exe and press enter (to search for it).   
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_64.jpg)

6. Once you find the file, left click on it once to select it, then right click and go to open file location.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_65.jpg)

7. Click on the white space in the top of window.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_66.jpg)

8. When the path is highlighted blue, Right click on it,  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_67.jpg)

9. And hit Copy (to copy the file path).    
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_68.jpg)

10. Paste this link into the "APBS binary location" on the "Program Locations" tab of "PyMol APBS Tools".  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_69.jpg)

11. Now add "**\apbs.exe**" after "\bin" in order to finish off the path to the APBS executable. If the path to an apbs.exe executable is correct, the line should no longer be highlighted red.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_70.jpg)

12. Now repeat steps 4 through 10 but with **psize.py** and **pdb2pqr.exe** (if they are not already in place). The end product should look like this:  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_71.jpg)

13. Now hit "Set grid", and "Run APBS".  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_72.jpg)

14. Now you should go to the visualization tab, and hit "Show" under "Molecular surface", "Positive Isosurface", and "Negative Isosurface".  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_73.jpg)  

15. A visualization in the "PyMol Viewer" window should appear and look something like this:
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_74.jpg)  

16. \*\*\* By changing the values for" Low, High, and Contour (kT/e), you can increase the range of concentrations you can see (larger values means more white space and less dark red/blue, as well as less isosurface).    
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_75.jpg)  

17. To get the changes to show you need to hit the "Update button" after changing the values.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_75.jpg)  
Using values of 5, this is the picture that appears (common isovalues are 1,5,10):  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_76.jpg)  

18. **If a picture like this**   
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_77.jpg)  
**or this appears,**   
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_78.jpg)  
**you didn't properly delete/save the water molecules which causes small highly charged areas**

19. To get field lines to appear, under the Visualization(1) tab hit "Show"  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_79.jpg)  
The picture should look somewhat similar to this:  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_80.jpg)  

[Click here to return to the top of the page](#topcall)
<a name="VMD"></a>
######VMD

[The needed protein for this VMD tutorial](http://www.rcsb.org/pdb/explore/explore.do?pdbId=1MYK) (1MYK a.k.a Hyperstable Arc Repressor Mutant PL8). An arc repressor is a small protein that acts as a transcription factor. This is a mutant that has the Proline-8 (in location 8) replaced by a Leucine. This creates enhanced stability due to an extra hydrogen bond, but also decreases the affinity of the molecule to bind to DNA.

In order to set up the molecule, follow the same instructions as **"Introduction to PDB2PQR"** but replace the shown molecule with 1MYK.

1. Open the downloaded PQR file and go to the bottom where the "HETATMs" are listed. There should be the 3 parts of a water molecule (labeled HOH). Delete these.
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_81.jpg)
You should end up with the following:
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_82.jpg)

2. Open up VMD, and under the **VMD Main** tab, click "File" -> "New Molecule".  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_83.jpg)

3. Under "Molecule File Browser",  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_84.jpg)  
Hit ![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_85.jpg)  
Open the "**1MYK.pqr**" file and hit Load (make sure the file type under "Determine file type:" is correct after hitting load, it should be PQR)  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_86.jpg)  

4. Under "Extensions", select "Analysis" and "APBS Electrostatics"  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_87.jpg)  

5. Under "APBS Tools" click "Edit" and then "Settings"  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_88.jpg)  

6. Under the APBS Tools "Settings" tab, hit Browse under "APBS Location". Input the location to an apbs.exe (apbs executable).  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_89.jpg) 
 
7. Click on "Computer" on the left sidebar and in the top right corner type "apbs.exe" and hit enter to search for apbs.exe.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_90.jpg)  

8. Click on one of the "apbs.exe", right click and go down to "Open file location"  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_91.jpg)  

9. Click on the "apbs.exe" and click "Open".  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_92.jpg)  

10. For "Working Directory" browse over to the file that contains the PQR file (1MYK.pqr) you downloaded and saved previously. Hit "Ok" once you found the file.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_93.jpg)   

11. Click OK on the "Settings" page  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_94.jpg)  

12. Click on the "0" and hit "Edit".  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_95.jpg)  

13. If you need to change the APBS settings you would do it on this page; however, the defaults are usually fine except for the most highly charged molecules (Elec stands for electrostatics). Hit Ok when you are done.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_96.jpg)  

14. Now hit "Run APBS". In the "APBSRun: Load APBS Maps" window click "Load files into top molecule" and click "Ok"  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_97.jpg)  

15. Under the "VMD Main" tab, go to "Graphics" and hit "Representations".  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_98.jpg)  

16. Select the current "rep" and under "Drawing Method" select "NewCartoon". Under "Coloring Method" select "ResType (colors based on type of residue: non-polar, basic, acidic, polar are white, blue, red, and green respectively)"  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_99.jpg)  
The current picture should look something like this:  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_100.jpg)

17. Now hit "Create rep" and select the new rep.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_101.jpg)  
Change the "Coloring Method" of this one to "ColorID" (the value of this should be 0).  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_102.jpg)  
Now change the "Drawing Method" to "Isosurface". Change the material to "Transparent", the "Draw" to "Solid Surface", and the "Isovalue" to 1.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_103.jpg)  

18. Repeat step 17 but with a ColorID of 1 and an Isovalue of -1 (red for a negative charge is standard because oxygen is typically modeled as red while blue is standard for a positive charge because nitrogen is modeled as blue). The display window should now look something like this:  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_104.jpg)  

19. If you want to visualize surface potentials (instead of isosurfaces), under the "Graphical Representations" window change the coloring method for both reps that are "Isosurface" under the "Style" title to "Surf".  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_105.jpg)  

20. Also change the "Coloring Method" to "Volume" and the Material to "Opaque" for both reps.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_106.jpg)

21. Under the "Trajectory" tab  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_107.jpg)  
Change the "Color Scale Data Range:" values to -10 and 10 and hit set (do this for both Surf reps).  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_108.jpg)

22. Now the display should have a solid red/blue/white surface that looks like this:  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_109.jpg)  

23. By keeping the "Coloring Method" as "Volume", but changing the "Drawing Method" to "FieldLines" you can visualize the local intensity of electric fields.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_110.jpg)  

24. Change the "Size" to 2, "GradientMag" to approximately 8.30, "Min Length" to 1.00, and "Max Length" is approximately 200.  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_111.jpg)  

25. The final representation should now look like the following:  
![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_112.jpg)  

[Click here to return to the top of the page](#topcall)
<a name="Dimes"></a>
##DIME VALUE PROBLEMS

When running APBS, DIME values may become a problem that keeps apbs electrostatic calculations from running. In order to check DIME values, you need to check the .in file for DIME values. One can change the DIME values of an APBS file by going through a text editor and manually changing the dime values. 

![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_113.png) 

The picture above shows a sample .in file, which can be obtained after running PDB2PQR on the desired protein. 

Dime values are the dimensions for the XYZ grid for the protein. Each  grid point requires about 160B of memory, and to get the total number if grid points the x,y,z grid elements are multiplied. The multi-grid solver iterates over all of these elements to find the electrostatic potential at each of those locations. If the dimensions are too large, the computer will have a memory problem and will be unable to calculate the electrostatic fields, such as:

![](https://raw.githubusercontent.com/PEMIfolder/github.io-PEMIfolder/master/Tutorial_pics_in_order/Tutorial_pic_114.png)

In order to work around this issue, you must manually change the DIME values to a smaller size. For the HIV-1 RT, I changed the DIME values to 129, which allowed APBS to run as normal and calculate a .dx file. 

Choosing the appropriate DIME value will fix the memory problems that may occur. The reason problems with DIME values may be too big is when PDB2PQR calculates the input file, it measures DIME values based on the size of the protein. For example,with HIV-1, it is protein with 2 chains of 400+ residues, and so the DIME values are unnecessarily large. 
  
To expand on DIME values, since a computer only knows about 1s and 0s convention is used to encode and decode values to the bits and bytes in memory; this is often called a type system.  An 8 bit byte has eight slots for a bit (1 or 0); therefore, if you are only considering positive numbers, it may hold a value between 0 (00000000) and 2^8 – 1  (11111111) which is 255 (though 2^8 is 256, and we have to subtract one because '0' takes up a slot).

To represent negative numbers, APBS uses the two's compliment encoding. This means if the left-most bit is a 1, then the number is negative, and so we invert the bits (change 0's to 1's and 1's to 0's), add 1, and read the value.  As an example, below is a table that shows the values of  just four bits (a nibble) that are decoded as unsigned and signed (using two's compliment) integers:

0000 = 0  :  0
0001 = 1  :  1
0010 = 2  :  2
0011 = 3  :  3
1101 = 13 : -3
1110 = 14 : -2
1111 = 15 : -1 


The problem is that APBS used a signed integer in the 1.4 release to store the total number of elements.  If the total got bigger than 2^(n-1) - 1, where n is the width of the integer (in our case a 32 bit wide int so 2^(n-1) = 2,147,483,648) then the number "overflowed" and looked like a negative number.  

In the new APBS release, this was fixed by using an unsigned type that is as big as the machine can support, generally a 64 bit number.

[For extra information on signed integers and overflow click HERE](http://en.wikipedia.org/wiki/Two's_complement)

[Click here to return to the top of the page](#topcall)

<script>
    smoothScroll.init();
<<<<<<< HEAD
</script>
=======
</script>
>>>>>>> origin/master
