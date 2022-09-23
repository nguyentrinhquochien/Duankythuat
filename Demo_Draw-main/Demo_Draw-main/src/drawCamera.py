# import the opencv library
import cv2 as cv

# define a video capture object
vid = cv.VideoCapture(0)
color = (255, 140, 0)
width = int(vid.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv.CAP_PROP_FRAME_HEIGHT))
axesLength = (100, 50)
angle = 0
startAngle = 0
endAngle = 360

if not vid.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = vid.read()
    cv.line(img=frame, pt1=(50, 50), pt2=(100, 100), color=(255, 0, 0), thickness=6, lineType=5, shift=0)
    cv.line(img=frame, pt1=(100, 100), pt2=(150, 20), color=(255, 0, 0), thickness=6, lineType=5, shift=0)
    cv.line(img=frame, pt1=(150, 20), pt2=(200, 100), color=(255, 0, 0), thickness=6, lineType=5, shift=0)
    cv.line(img=frame, pt1=(200,100), pt2=(250, 20), color=(255, 0, 0), thickness=6, lineType=5, shift=0)
    cv.line(img=frame, pt1=(250, 20), pt2=(300, 100), color=(255, 0, 0), thickness=6, lineType=5, shift=0)
    cv.putText(frame, "Nguyen Trinh Quoc Hien", (150 , 400), fontFace = cv.FONT_HERSHEY_PLAIN, fontScale = 2,  color = color, thickness = 3)
    
    cv.imshow("Display window", frame)
    
    k = cv.waitKey(1)
    if k == ord("q"):
        break

vid.release()

cv.destroyAllWindows()
