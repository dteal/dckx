# dckx

* Dreadfully Creative Klaxon Xylophone
* Deeply Concerning Knews eXceptor
* Daleks Can be Killed by X-rays
* Don't Care, Keep Xeroxing
* Dainty Cute Kittens are Xenial

...is the news aggregator of the future! Tired of boring world news? Can't
get enough programmer humor? Read your *Times* headlines in XKCD panels!

![comic generated by "Star Wars"](https://raw.githubusercontent.com/dteal/dckx/master/output/star_wars.png)

##Usage

This program requires Python 3 with Pillow and nltk (including the nltk
corpus) installed.

Run dckx.py with command line arguments. Said arguments, forming, ostensibly,
a headline, will be elucidatingly reinterpreted via XKCD conglomeration. That
is, you will be given a superb image pieced together from hand-picked
out-of-context singular panels removed from their native comic.

For example, "python dckx.py star wars" could create the above image. The
left panel must be part of an XKCD comic that references stars, and the right,
one that references wars.

##Preprocessing

In order to run, dckx has a large precollated library of source material.
The materials consists of webscraped XKCD graphics, caption text, and
executive summaries drawn from explainxkcd.com. The database generation code,
in modular form, is in getxkcd.py, parser.py, and contourtest.py.

	Program: getxkcd.py
	Input: (none)
	Output:
		image files in /originals/, e.g., dckx/originals/971.png
		summary text in /originals/, e.g., dckx/original/971_transcript.txt
		list of comic numbers in /originals/index.txt

	Program: parser.py
	Input: (none)
	Output:
		image files in /originals/, e.g., dckx/originals/971.png
		summary text in /originals/, e.g., dckx/original/971_summary.txt
		list of comic numbers in /originals/index.txt

	Program: contourtest.py
	Requirements: OpenCV
	Input: (none)
	Output:
		image files in /originals/, e.g., dckx/originals/971.png
		summary text in /originals/, e.g., dckx/original/971_transcript.txt
		list of comic numbers in /originals/index.txt

##Postprocessing

Input is tokenized by dckx.py, then fed into search.py, which uses
several techniques to match each token to a proper comic panel. These
panels are recombined in an output comic, which is displayed for the
user's convenience.

##Authorship

dckx was authored by Annie, Brian, Daniel, Kevin, and Zach during HackTX 2016.

