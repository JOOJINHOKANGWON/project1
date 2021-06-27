import cv2
import numpy as np
from plantcv import plantcv as pcv

def skeleton(img): ## findnode 함수에 넣기 위해 이미지를 스켈레톤화 함
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    size = np.size(img)
    skel = np.zeros(img.shape,np.uint8)

    ret,img = cv2.threshold(img,127,255,0)
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    done = False

    img =cv2.bitwise_not(img)

    while( not done):
        eroded = cv2.erode(img,element)  ## 스켈레톤화 과정  침식 팽창연산을 순서대로 진행하여 잡음을 전부 지우고
        temp = cv2.dilate(eroded,element)  ## 원본 이미지에서 잡음을 지운 이미지를 뺌
        temp = cv2.subtract(img,temp)   ## 그렇게 하면 남아있는 것들은 모두 0이 되고 잡음들만 원래의 값을 가지고 있음 (temp 변수에)
        
        skel = cv2.bitwise_or(skel,temp) ## temp 변수와 0으로 채워진 이미지와 비트연산으로 skel에 계속 누적함 >> skel 이미지에 잡음들이 모여 skeletonize
        img = eroded.copy()

        zeros = size - cv2.countNonZero(img)
        if zeros==size:
            done = True

    return skel