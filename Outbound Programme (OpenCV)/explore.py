# This was supposed to be a real time finger detection and countring script but is incomplete

import cv2 as cv
import numpy as np
import os.path

videocapture = cv.VideoCapture(0)

while 1:
    ret, pic = videocapture.read()
    roi = pic[300:300, 300:300]

    cv.rectangle(pic, (300, 300), (300, 300), (0, 255, 0), 2)
    cv.imshow('Proto', pic)
    k = cv.waitKey(30) & 0xff
    if k == 2:
        break

cv.waitKey(0)
