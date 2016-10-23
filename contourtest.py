from skimage import exposure
import numpy as np
import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True, help = "path to query image")
args = vars(ap.parse_args())

image = cv2.imread(args["query"])
orig = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)

#cv2.imshow("canny", edged)
#cv2.waitKey(0)

im2, contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
largestPanel = None


contourArray = []
#badContoursArray = []
for c in contours:
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	#print(cv2.contourArea(c))
	#if(cv2.contourArea(c) < 20000:
	#	badContours.append(approx)

	##if 
	if len(approx) == 4:
		contourArray.append(approx)
		#largestPanel = approx
		#break

mask = np.zeros_like(image)
cv2.drawContours(mask, contourArray, -1, [255, 255, 255], -1)

#ret,thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
#cv2.imshow("contour", image)
#cv2.waitKey(0)

out = np.zeros_like(image)
out[mask == [255, 255, 255]] = image[mask == [255, 255, 255]]
#cv2.drawContours(image, contourArray, -1, (0, 255, 0), 3)
#cv2.imshow("contour", out)
#cv2.waitKey(0)

##ROI - region of interest

##specifies directory to output panels
os.chdir("/home/wangbri/Desktop/imgsplice/splitpanels")

filename = args["query"]

if filename.endswith('.png'):
	filename = filename[:-4]

panelCnt = 1;
for c in contours:
	##excludes files smaller than typical xkcd panel
	if cv2.contourArea(c) > 20000:
		##sets bounding rectangle
		x, y, width, height = cv2.boundingRect(c)
		roi = orig[y:y+height, x:x+width]
		cv2.imwrite(filename + "_" + str(panelCnt)+".png", roi)
		panelCnt += 1

