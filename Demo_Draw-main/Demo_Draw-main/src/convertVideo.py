import cv2 as cv
import time

importVideoFile = '../video/demo'
saveVideoFile = '../video/result'

cap = cv.VideoCapture(importVideoFile + '/gaixinh.mp4')

width= int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps= int(cap.get(cv.CAP_PROP_FPS))

dotFile = 'mkv'

#define codec for video you want to save
fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter(saveVideoFile + '/output.' + dotFile, fourcc, fps, (width, height)) 

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imshow('frame', frame)
    time.sleep(0.025)
    # frame = cv.flip(frame, 0)
    # out.write(frame)
    if cv.waitKey(1) == ord('q'): # wait if you press key q so exit program
        break

out.release()
cap.release()
cv.destroyAllWindows()
