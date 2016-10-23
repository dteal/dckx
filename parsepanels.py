from PIL import Image, ImageStat
import argparse
import cv2
import os
import sys

os.chdir("/home/wangbri/Desktop/imgsplice/splitpanels")
os.chmod("/home/wangbri/Desktop/imgsplice/splitpanels",0777)

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True, help = "path to query image")
args = vars(ap.parse_args())


img = cv2.imread(args["query"])
height, width, channels = img.copy().shape
if height > 3 * width or height > 400:
	os.remove(args["query"])

im = Image.open(args["query"])

stat = ImageStat.Stat(im)
min = stat.extrema[0]
max = stat.extrema[1]

if min == max:
	os.chmod(args["query"])
	os.remove(args["query"])

