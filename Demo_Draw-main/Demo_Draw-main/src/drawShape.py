import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy import ndimage
from PIL import Image

importPhotoFile = "../photo/demo"
savePhotoFile = "../photo/result"

width = 500
height = 500

rectangleWidth = 150
rectangleHeight = 150

color = (255, 140, 0)

list_draw = []

canvas = np.zeros((width, height, 3), np.uint8)

def draw_poly(
    image,
    pts,
    is_closed=True,
    color_bgr=[255, 0, 0],
    size=0.01,  # 1%
    line_type=cv.LINE_AA,
    is_copy=True,
):
    assert size > 0

    image = image.copy() if is_copy else image  # copy/clone a new image

    # calculate thickness
    h, w = image.shape[:2]
    if size > 0:
        short_edge = min(h, w)
        thickness = int(short_edge * size)
        thickness = 1 if thickness <= 0 else thickness
    else:
        thickness = -1

    # calc x,y in absolute coord
    new_pts = []
    for x, y in pts:
        new_pts.append((int(x * w), int(y * h)))

    cv.polylines(
        img=image,
        pts=[np.int32(new_pts)],
        isClosed=is_closed,
        color=color_bgr,
        thickness=thickness,
        lineType=line_type,
        shift=0,
    )
    return image


rectangleBox = cv.rectangle(
    canvas,
    ((int)(width / 2 - rectangleWidth), (int)(height / 2 - rectangleHeight)),
    ((int)(width / 2 + rectangleWidth), (int)(height / 2 + rectangleHeight)),
    color,
    3,
)

draw_poly(
    image=canvas,
    pts=[(0.5, 0.1), (0.1, 0.5), (0.5, 0.9), (0.9, 0.5), (0.5, 0.1)],
    is_closed=False,
    color_bgr=color,
    size=0.009,  # 1%
    is_copy=False,
)
cv.rectangle(
    canvas,
    (
        (int)(width / 2 - (rectangleWidth - 90)),
        (int)(height / 2 - (rectangleHeight - 90)),
    ),
    (
        (int)(width / 2 + (rectangleWidth - 90)),
        (int)(height / 2 + (rectangleHeight - 90)),
    ),
    color,
    3,
)
draw_poly(
    image=canvas,
    pts=[(0.5, 0.33), (0.33, 0.5), (0.5, 0.67), (0.67, 0.5), (0.5, 0.33)],
    is_closed=False,
    color_bgr=color,
    size=0.009,  # 1%
    is_copy=False,
)
cv.line(
    canvas,
    (
        (int)(width / 2 - (rectangleWidth - 50)),
        (int)(height / 2 - (rectangleHeight - 50)),
    ),
    (
        (int)(width / 2 + (rectangleWidth - 50)),
        (int)(height / 2 + (rectangleHeight - 50)),
    ),
    color = color,
    thickness = 5
)
cv.line(
    canvas,
    (
        (int)(width / 2 + 100),
        (int)(height / 2 - 100),
    ),
    (
        (int)(width / 2 - 100),
        (int)(height / 2 + 100),
    ),
    color = color,
    thickness = 5
)
cv.line(
    canvas,
    (
        (int)(width / 2 - rectangleWidth),
        (int)(height / 2 + 0),
    ),
    (
        (int)(width / 2 + rectangleWidth),
        (int)(height / 2 + 0),
    ),
    color = color,
    thickness = 5
)
cv.line(
    canvas,
    (
        (int)(width / 2 + 0),
        (int)(height / 2 - rectangleHeight),
    ),
    (
        (int)(width / 2 + 0),
        (int)(height / 2 + rectangleHeight),
    ),
    color = color,
    thickness = 5
)

cv.putText(canvas, "Nguyen Tan Phap", (110 , 490), fontFace = cv.FONT_HERSHEY_PLAIN, fontScale = 2,  color = color, thickness = 3)

# show image
cv.imshow("Display window", canvas)

while True:
    k = cv.waitKey(1)
    if k == ord("q"):
        break

cv.destroyAllWindows()
