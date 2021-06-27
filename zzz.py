import cv2
import numpy as np
def skeleton(img): 
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    size = np.size(img)
    skel = np.zeros(img.shape,np.uint8)

    _,img = cv2.threshold(img,127,255,0)
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    done = False

    img =cv2.bitwise_not(img)
    

    while( not done):
        eroded = cv2.erode(img,element)  
        temp = cv2.dilate(eroded,element) 
        temp = cv2.subtract(img,temp)   
        skel = cv2.bitwise_or(skel,temp) 
        img = eroded.copy()

        zeros = size - cv2.countNonZero(img)
        if zeros==size:
            done = True

    return skel