import cv2
import numpy as np
from plantcv import plantcv as pcv
## 스켈레톤화 한 이미지로 노드를 찍은 이미지 출력## 
## 현재 노드를 찍은 이미지에서 노드의 좌표를 읽어 올 방법 고안중##  ## 2021 05. 해결
def findnode(img):
    pcv.params.debug="plot"
    
    ret,img=cv2.threshold(img,127,255,0)
    skeleton=pcv.morphology.skeletonize(mask=img)


    
    pcv.params.line_thickness=2
    

    branch_points_img=pcv.morphology.find_branch_pts(skel_img=skeleton,mask=None) ## 현재 pcv 함수에서 저절로 이미지가 뜨는데 이걸 찾아서 지워야함 (06.10)
                                                                                ## 
    return branch_points_img