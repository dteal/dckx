# dckx

* Dreadfully Creative Klaxon Xylophone
* Deeply Concerning Knews eXceptor
* Daleks Can be Killed by X-rays
* Don't Care, Keep Xeroxing
* Dainty Cute Kittens are Xenial

...is the news aggregator of the future! Tired of boring world news? Can't
get enough programmer humor? Read your *Times* headlines in XKCD panels!

##Preprocessing

Daniel: program to download XKCD images and Explain XKCD text to numbered
PNG and text files, respectively.

	Program: getxkcd.py
	Input: (none)
	Output:
		image files in /originals/, e.g., dckx/originals/971.png
		summary text in /originals/, e.g., dckx/original/971_summary.txt
		list of comic numbers in /originals/index.txt

Brian: program to take each png comic and output individual panels as
separate images (and the number of images).

Zach: program to take each text file from Explain XKCD and the number of
panels, and to output a text file containing relevant text for each panel.

	Program: parser.py
	Input: Nothing, it's a script
	Output: A folder full of newly formatted files

##Postprocessing

Kevin: program that takes input from user and ends up with a number of panels
needed and relevant text to describe each panel.

	Program: ui.py

Annie: program that matches a bit of text to the most relevant panel
description.

	Program: search.py, implements search() function.
	Input:
		Input word (str)
		Num results (int)
	Output:
		List of num strs that match images, e.g., ['1_1','4_1']
	

