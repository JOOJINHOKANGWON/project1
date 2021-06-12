
import numpy as np
import processing
import drawdraw
import cv2
import skeletonizefindnode
import colordetection
import skeletonize
import findxy
import checkparm
img1=cv2.imread('treemask.jpg') ## 연산을 할 사진을 불러옴. 
img2=img1.copy()
rois,a,b,c,d=drawdraw.startt(img1) ## 보낸 이미지에서 물체를 분할하기 위해 사용자가 임의로 영역을 잡음. 이는 후에 딥러닝으로 바꿀 예정



img4=skeletonize.skeleton(rois) ## findnode에서 이미지를 돌리기 위해서 스켈레톤화를 진행함

img5=skeletonizefindnode.findnode(img4) ## plantcv의 findnode 함수를 이용해서 가장 아래 브랜치를 구함
img6=np.array(img5) ##findxy에서 넘파이 배열을 필요로 하기 때문에 넘파이배열로 바꿔줌
xx,yy=findxy.find(img6) ## plantcv에서 findnode 돌린 이미지에서 가장 바깥 영역을 찾음
img18,img2,aa,bb,cc=processing.sobel(rois,img1,a,b,c,d,xx,yy) ## 영역분리 지금 엠보싱 연산으로 전체길이를 구했는데 이는 매우 부정확, plantcv의 findtip 으로 구하면 편할듯

img3,h,w=colordetection.tracking(img2) ## 색깔 마스크 찾는거 분홍색으로만 해놓음

checkparm.checkhow(h,w,aa,bb,cc)  ## 실제길이 파악
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.imshow('img4',img4)
cv2.imshow('img5',img5)
cv2.waitKey(0)


