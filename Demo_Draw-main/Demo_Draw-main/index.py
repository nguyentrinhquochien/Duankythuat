#Write a program to calculate the sum of 2 number
import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("./Hinh-nen-cute-1.jpg"))
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)
