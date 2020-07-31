import pytesseract as tes
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread(r'e:\cv\brakeSystem_Sub.PNG')
img_sub = img[650:690,620:740]

_ , img_sub = cv.threshold(img_sub,80,255,cv.THRESH_BINARY)

kernel = np.ones((3,3),np.uint8)

img_erosion = cv.erode(img_sub,kernel)



