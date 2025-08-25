import pickle
import math

import cv2
import numpy as np
from cv2 import BORDER_CONSTANT
from cv2 import BORDER_DEFAULT


image = cv2.imread("Screenshot_1.jpg")
# print(image.shape)
# image = cv2.copyMakeBorder(image, 40, 40, 40, 40, BORDER_CONSTANT)
gray = cv2.cvtColor(image[15:-15, 15:-15], cv2.COLOR_BGR2GRAY)
height, width = gray.shape

cells = 15
startleft = 0
startup = 0
dh = height//cells
dw = width//cells

for i in range(cells):
    for j in range(cells):
        cropim = gray[startup:startup+dh, startleft:startleft+dw]
        cv2.imwrite(f"photo/img{i*cells + j}.jpg", cropim)
        startleft += dw
    startup += dh
    startleft = 0


# dst = cv2.Canny(gray, 25, 100, None, 3)

# ret, thresh = cv2.threshold(gray, 127, 255, 0)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cnt = contours[5]
# im = cv2.drawContours(image, [cnt], 0, (0,255,0), 3)


cv2.imshow("Scrabble board", gray)
cv2.waitKey(0)