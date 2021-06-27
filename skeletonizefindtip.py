## 후에 추가할 예정 (06.10)

import cv2
from plantcv import plantcv as pcv

def findtips(img):
    pcv.params.debug="plot"
    
    ret,img=cv2.threshold(img,127,255,0)
    skeleton=pcv.morphology.skeletonize(mask=img)
    

    pcv.params.line_thickness=3


    tips_img=pcv.morphology.find_tips(skel_img=skeleton)
    
    return tips_img