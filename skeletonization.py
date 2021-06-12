import cv2
import numpy as np


img=cv2.imread('horse2.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
    cv2.THRESH_BINARY,7,-3)

img2=img.copy()

rows,cols=img.shape[:2]
black=np.zeros((rows,cols),np.uint8)

element=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
temp=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,element)
eroded=cv2.erode(img,element,iterations=1)
skel=cv2.bitwise_or(black,temp)
img=eroded.copy()


cv2.imshow('as',img2)
cv2.imshow('imgskel',skel)
cv2.imshow('img',img)
cv2.waitKey(0)


