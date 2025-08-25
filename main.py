import pickle

import cv2
# import imutils as im
# import cvzone
# import numpy as np

def rescale(frame, scale=0.4):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    new_metrics = (width, height)

    return cv2.resize(frame, new_metrics)

with open("points", "rb") as f:
    point_list = pickle.load(f)

w, h = 110, 100
img = rescale(cv2.imread("img.jpg"))

for j in range(15):
    for ind in range(15):
        x, y = 45+ind*45, 10+j*35
        cropim = img[y:y+35, (x-2*ind):x+(40-ind)]
        # cropim = im.resize(cropim, width=28, height=28)
        cv2.imshow("Image", cropim)
        cv2.waitKey(500)
        cv2.imwrite("testimg.jpg", cropim)