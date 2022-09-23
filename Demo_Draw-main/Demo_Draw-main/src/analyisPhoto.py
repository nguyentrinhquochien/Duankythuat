import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import matplotlib
import pathlib

importPhotoFile = '../photo/demo'
savePhotoFile = '../photo/result'
rows = 2
cols = 4
img_arr = []
count_img = 0
num_image = 8

def img_change(image, index):
    image = cv.imread(image)
    height, width, channels = image.shape
    if(index == 0):
        color = (0, 255, 0)
        line_thickness = 5
        image = cv.line(image, (0, 0), (width, height), color, thickness = line_thickness)
    elif (index == 1):
        color = color = (0, 255, 0)
        line_thickness = 10
        center_x, center_y = 0.45, 0.5
        radius = 150
        coorX, coorY = int(center_x * width), int(center_y * height)
        image = cv.circle(image, (coorX, coorY), radius, line_thickness)
    return image

for i in range(num_image):
    img_arr.append(img_change(importPhotoFile + "/charset.png", index = i))

fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(15,15))

for i in range(rows):
    for j in range(cols):   
        if(count_img < num_image):     
            axes[i, j].imshow(img_arr[count_img])
            count_img += 1
        else: 
            count_img = 0

plt.show()
