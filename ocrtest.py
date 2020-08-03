import pytesseract as tes
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#add a comment line

img = cv.imread(r'e:\cv\brakeSystem_Sub.PNG')
img_sub = img[650:690,620:740]

_ , img_sub = cv.threshold(img_sub,80,255,cv.THRESH_BINARY)

kernel = np.array([[1,1],[1,1]],np.uint8)

img_erosion = cv.erode(img_sub, kernel, iterations=2)


#need to integrate FCA work here.

#to import and integrate FCA work.

