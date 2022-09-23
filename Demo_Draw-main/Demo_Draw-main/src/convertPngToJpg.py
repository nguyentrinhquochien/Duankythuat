import cv2 as cv
import sys
from datetime import datetime

importPhotoFile = 'photo/demo'
savePhotoFile = 'photo/result'

# img = cv.imread(cv.samples.findFile(importPhotoFile + "/charset.png")) 
img = cv.imread(cv.samples.findFile(importPhotoFile + "/charset.png"), cv.IMREAD_GRAYSCALE) # convert file image to grayscale color

# if file not found
if img is None:
    sys.exit("Could not read the image.")

# show image
cv.imshow("Display window", img)

while True:
    k = cv.waitKey(0)
    if k == ord("s"):
        dt = datetime.now()
        ts = datetime.timestamp(dt)
        temp = savePhotoFile + '/' + str(round(ts)) + "-charset.jpg"
        cv.imwrite(temp, img)
    elif k == ord("q"):
        break
