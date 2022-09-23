import cv2
import numpy as np
def nothing(x):
    pass

cap = cv2.VideoCapture(1)
cv2.namedWindow("Trackbar")
cv2.createTrackbar("L-H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("L-S", "Trackbar", 68, 255, nothing)
cv2.createTrackbar("L-V", "Trackbar", 154, 255, nothing)
cv2.createTrackbar("U-H", "Trackbar", 180, 180, nothing)
cv2.createTrackbar("U-S", "Trackbar", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbar", 243, 180, nothing)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_s = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_h = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")



    lower_red = np.array([l-h, l_s, l_s])
    upper_red = np.array(u_h, u_h, u_v)

    mask = cv2.inRange(hsv, lower_red, upper_red)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)
    cv2.imshow("Frame", frame)
    cv2.imshow("MasK", masK)
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     for cnt in contours:
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            if area > 400:
                cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
                if len(approx) == 3:
                    cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
                elif len(approx) == 4:
                    cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
                elif 10 < len(approx) < 20:
                    cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))
    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release()
cap.destroyAllWindows()
