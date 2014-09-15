#Ionic Strength Dependence of Peptide-RNA Interactions

####Software that will be needed:  
[Click here for Git](http://git-scm.com/)  
[Click here for APBS & PDB2PQR](http://www.poissonboltzmann.org/)  
[Click here for Python](https://www.python.org/)
**Note that this is written using Python 2.7  
[Click here for Matplotlib](http://matplotlib.org/)

#####After downloading Git, it is useful to set it to your path so you don't have to change your command prompt to the directory containing git.exe. Make sure you pick one of the files (there could be multiple) that says exactly "git.exe", not like "git-add-exe".

1. Go into "My Computer" and in the upper right corner and search for git.exe: 
![](http://i60.tinypic.com/2qc08xl.jpg)
<img
    style="width: 640px; height: 480px;" 
    src="http://i60.tinypic.com/2qc08xl.jpg">  

2. Right click the file that comes up and select "Open file location" (should be near the bottom of the tab that comes up)  
![](http://i61.tinypic.com/vcw4yv.jpg)  

3. Copy the path which should look something like this:
![](http://i59.tinypic.com/5angox.jpg)

4. Open the start menu and right click "Computer" and left click properties.  
![](http://i57.tinypic.com/1zxtyet.jpg)

5. Click on "Advanced system settings" which should be in the top left corner.  
![](http://i58.tinypic.com/1zc1tg8.jpg)

6. Under the "Advanced" tab, click "Environment Variables". (Should be in the bottom right)  

7. Make sure "PATH" is selected and click "Edit..."  
![](http://i57.tinypic.com/2llleue.jpg)

8. Go to the far right, add a semi-colon (if one does not already exist), paste the path you copied (step 2) and click ok.  
![](http://i60.tinypic.com/26425oj.jpg)

#####In order to obtain the needed files (input files, pqr, pdb, etc.) now you have to [clone the repository from github](https://github.com/Electrostatics/apbs-pdb2pqr) 
 
1. Type "**git clone http://github.com/electrostatics/apbs-pdb2pqr.git**" into your command prompt (this may take a while).
![](http://i57.tinypic.com/vinneh.jpg)  
<img
    style="width: 640px; height: 250px;" 
    src="http://i57.tinypic.com/vinneh.jpg">  
If you are still at all confused how to fork a repository you can [use this practice example](https://help.github.com/articles/fork-a-repo) to learn how.

2. Now, find the "template.in" file in the "**apbs-pdb2pqr/apbs/examples/protein-rna**" folder that you just cloned, if you don't know where it is you can search your computer again for the "apbs-pdb2pqr" folder (use the "**dir**" command in order to see what files are in the current "directory" (folder)).  
![](http://i61.tinypic.com/2n8btyt.jpg)  
<img
    style="width: 640px; height: 320px;" 
    src="http://i61.tinypic.com/2n8btyt.jpg">  
(use "__cd directoryname__" to change to the wanted directory, you can repeat using dir and cd in order to get to the place you are looking for)
![](http://i60.tinypic.com/9uymo4.jpg)
<img
    style="width: 640px; height: 320px;" 
    src="http://i60.tinypic.com/9uymo4.jpg">

3. Save the file as "template.txt" 

4. Save python to your path (see the git.exe example but search for python.exe this time)

5. Save the following python script (in my case I saved as apbs_dx.py):
####Python Script (windows):
	from subprocess import call

	my_list = (0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.225, 0.275, 0.325, 0.4, 0.5, 0.6, 0.7, 0.8)
		with open("template.txt", "r") as temp:  
		template_text = temp.read()

	for item in my_list:  
		input_txt = template_text.replace("IONSTR",str(item))  
		file_name = "apbs-" + str(item) + ".in"  
		print "Creating file now:", file_name  
		with open(file_name, "w") as temp:  
			temp.write(input_txt)
		call(["apbs", "apbs-" + str(item) + ".in"])

	with open("dxmath.txt", "r") as temp:
		template_2_text = temp.read()

	for item in my_list:
		input_2_txt = template_2_text.replace("IONSTR",str(item))
		file_2_name = "dxmath-" + str(item) + ".in"
		print "Creating file_2 now:", file_2_name
		with open(file_2_name, "w") as temp:
			temp.write(input_2_txt)
		call(["dxmath", "dxmath-" + str(item) + ".in"])

1. Run this script from your command prompt by typing "**python apbs_dx.py >> output.txt**" (change apbs_dx.py to whatever you named the above script). When it is running nothing will show up, but when it is done, there will be a new line.
![](http://i59.tinypic.com/2gsoqbc.jpg)
<img
    style="width: 640px; height: 400px;" 
    src="http://i59.tinypic.com/2gsoqbc.jpg">

2. The "**python**" tells the computer to use python.exe to run the input. It takes "**apbs_dx.py**" as your input.  

3. Furthermore the double greater than symbol "**>>**" tells your cmd to take the things that would normally be printed into the command prompt into a file called "**output.txt**".

4. Open the output.txt file with your favorite text editor (This tutorial is using notepad ++), hit "**ctrl f**" and search for "Global net ELEC energy", copy the numbers and paste them into another file.
![](http://i60.tinypic.com/besv1h.jpg)
<img
    style="width: 640px; height: 480px;" 
    src="http://i60.tinypic.com/besv1h.jpg">

###Python Script (unix)
	my_list = (0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.225, 0.275, 0.325, 0.4, 0.5, 0.6, 0.7, 0.8)
		with open("template.txt", "r") as temp:  
		template_text = temp.read()

	for item in my_list:  
		input_txt = template_text.replace("IONSTR",str(item))  
		file_name = "apbs-" + str(item) + ".in"  
		print "Creating file now:", file_name  
		with open(file_name, "w") as temp:  
			temp.write(input_txt)

	with open("dxmath.txt", "r") as temp:
		template_2_text = temp.read()

	for item in my_list:
		input_2_txt = template_2_text.replace("IONSTR",str(item))
		file_2_name = "dxmath-" + str(item) + ".in"
		print "Creating file_2 now:", file_2_name
		with open(file_2_name, "w") as temp:
			temp.write(input_2_txt)

Run this script by typing "**python apbs_dx.py**". It will poop out all the apbs-ionconcentration.in files and dxmath-ionconcentration.in files that you need.

![](http://i57.tinypic.com/okzaqb.jpg)
<img 
    style="width: 640px; height: 400px;" 
    src="http://i57.tinypic.com/okzaqb.jpg">  
###Bash Script (unix)
	#!/bin/bash
	# Usage: remove all utility bills pdf file password 
	shopt -s nullglob

	for f in apbs-*.in
		do
			echo "Running apbs on $f" 
			apbs $f	
	done		
	for f in dxmath-*.in
		do
			echo "Running dxmath on - $f"   
			dxmath $f		
	done

1. Save the bash scipt (my name was run\_apdx\_files.sh). Run it by typing "**./run_apdx_files.sh | tee  output.txt**". This will feed all the input files from the python (unix) script through apbs and dxmath. It will make a "tee pipe" by both printing the results to both the command line and the output.txt file.
![](http://i62.tinypic.com/2rcyhxy.jpg)
<img 
    style="width: 640px; height: 400px;" 
    src="http://i62.tinypic.com/2rcyhxy.jpg">

2. After this command, run "**grep "Global net ELEC energy" output.txt | tee output_2.txt**". This will search output.txt for the string "Global net ELEC energy" and output the lines which contain the phrase to a file called output\_2.txt.
![](http://i60.tinypic.com/dvij43.jpg)
<img 
    style="width: 640px; height: 400px;" 
    src="http://i60.tinypic.com/dvij43.jpg">  

###Formatting Results
1. Take the numbers you printed/copied into a new file and change the format so that there is no E+XYZ (it is the same as multiplying by 10^XYZ). The numbers should look like this:
![](http://i58.tinypic.com/5d1evs.jpg)
<img 
    style="width: 640px; height: 480px;" 
    src="http://i58.tinypic.com/5d1evs.jpg">  

2. In your command prompt type python.exe which will open the python [Read-Eval-Print-Loop (REPL)](http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop).

3. In this prompt type "**import matplotlib.pyplot as plt**"

4. Next type "**plt.plot([0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.225, 0.25, 0.275, 0.3, 0.325, 0.4, 0.5, 0.6, 0.7, 0.8], [86.74, 96.07, 101.15, 104.61, 107.22, 109.31, 111.04, 113.81, 114.94, 115.96, 116.88, 117.72, 119.85, 122.06, 123.81, 125.24, 126.43], 'ro')**" (ro will print red circles where the data points are).

5. Now type "**plt.axis([0,0.8, 80, 130])**" (xmin, xmax, ymin, ymax).

6. Finally by typing "**plt.show()**" you will get the graph to appear.
![](http://i57.tinypic.com/10i9saa.jpg)
<img 
    style="width: 640px; height: 840px;" 
    src="http://i57.tinypic.com/10i9saa.jpg">

7. To get the blue line to appear with the red dots, hit the up arrow a few times until the plt.plot command comes up. Now switch the 'ro' with a 'b' and press enter (or retype the plt.plot command with this change). Finally type plt.show() to get the final graph to print out.

##Molecular Modeling
PyMol: 
  
1. Open "**PyMOL + Tcl-Tk GUI**". Using the window at the top, find the directory containing the files that were just pooped out by the python/bash scripts. Once you find the file type "**load qdens-diff-0.225.dx**".  
![](http://i61.tinypic.com/e7xdf7.jpg)
<img 
    style="width: 640px; height: 160px;" 
    src="http://i61.tinypic.com/e7xdf7.jpg">

2. Your "PyMol Viewer" should now show this: 
![](http://i60.tinypic.com/kci5c8.jpg)
<img 
    style="width: 640px; height: 480px;" 
    src="http://i60.tinypic.com/kci5c8.jpg">

3. Click the "qdens-diff-0.225 tab on the right so that it turns the same color as the all button (this means it's on). This should show the outline of a rectangular prism (these correspond to dime values which are used to run apbs). Click the "**S** (show)" next to qdens and click show everything.
![](http://i61.tinypic.com/2rw8dib.jpg)
<img 
    style="width: 640px; height: 480px;" 
    src="http://i61.tinypic.com/2rw8dib.jpg">

4. Now load the pqr file into the PyMol Viewer from the Pymol prompt again. "**load  model_outNB.pqr**"

5. Under the "**S**" for the new model you just loaded hit show cartoon and ribbon. Hit "**H**(hide)" lines and now you should have a picture like this:
![](http://i59.tinypic.com/281801l.jpg)
<img 
    style="width: 640px; height: 480px;" 
    src="http://i59.tinypic.com/281801l.jpg">  

VMD:

1. Open VMD 1.9.1 (or what ever version you have). From the VMD Main window hit "**File -> New Molecule**". A "**Molecule File Browser**" window should come up.

2. Hit 'Browse...'    

3. Open the "**qdens-diff-0.225.dx**" file and hit 'Load'   
Your window should look somemthing like this:
![](http://i62.tinypic.com/210nc78.jpg)
<img 
    style="width: 640px; height: 360px;" 
    src="http://i62.tinypic.com/210nc78.jpg">  
(If "Load" doesn't work, make sure the file type is correct under "Determine file type")

3. Now load another new molecule (model_outNB.pqr) and you should have something like this (zoomed in a little with the scroll on a 3 button mouse):  
![](http://i61.tinypic.com/352pycp.jpg)

4. Under the "Graphics" tab hit "Representations". A "Graphical Representations"  tab should come up.  
![](http://i59.tinypic.com/nwa7tv.jpg)  
Click the "Rep" that has "Style" "Lines" and change the "Drawing Method" from "Lines" to "New Cartoon". Click "Coloring Method" and change to "ResType". This will color the protein alpha helix such that each amino acid will be a different color based on whether it is non-polar, basic, acidic, or polar (white, blue, red, and green respectively).

5. Now change the Isosurface representation. Draw (bottom right) should be "Solid Surface" instead of "Points". The "Material should also be changed from "Opaque" to "Transparent".

6. Now the representation should look like this:  
![](http://i57.tinypic.com/ayayq8.jpg)
