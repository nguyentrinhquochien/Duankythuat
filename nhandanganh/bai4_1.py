import argparse
import imutils
import cv2

count = 0

class ShapeDetector:
	def __init__(self):
		pass
	def detect(self, c):
		# initialize the shape name and approximate the contour
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        # if the shape is a triangle, it will have 3 vertices
		if len(approx) == 3:
			shape = "Tam Giac"
		# if the shape has 4 vertices, it is either a square or
		# a rectangle
		elif len(approx) == 4:
			# compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)
			# a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
			shape = "Hinh Vuong" if ar >= 0.95 and ar <= 1.05 else "Chu Nhat"
		# if the shape is a pentagon, it will have 5 vertices
		elif len(approx) == 5:
			shape = "Ngu Giac"
		# otherwise, we assume the shape is a circle
		else:
			shape = "Hinh Tron"
		# return the name of the shape
		return shape

image = cv2.imread(cv2.samples.findFile("./shape.jpg"))
# resized = imutils.resize(image, width=300)
ratio = image.shape[0] / image.shape[0]

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()
# loop over the contours
for index, c in enumerate(cnts):
    # compute the center of the contour
    if(index != 0):
        M = cv2.moments(c)
        count += 1
        # print(M)  
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        # draw the contour and center of the shape on the image
        shape = sd.detect(c)
        # multiply the contour (x, y)-coordinates by the resize ratio,
        # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")

        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(image, "center", (cX - 20, cY - 20),
        	cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(image, shape, (cX + 10, cY + 10), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (255, 255, 255), 2)
        # show the image

cv2.putText(image, "Number for shape: " + str(count), (30, 30),
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)
