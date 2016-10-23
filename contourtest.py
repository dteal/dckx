from skimage import exposure
import numpy as np
import argparse
import cv2

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

im2, contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
largestPanel = None

for c in contours:
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)

	if len(approx) == 4:
		largestPanel = approx
		break

cv2.drawContours(image, [largestPanel], -1, (0, 255, 0), 3)
cv2.imshow("contour", image)
cv2.waitKey(0)
