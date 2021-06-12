import cv2
import numpy as np

def tracking(cap1):
    
    
        
    lower_blue=np.array([100,30,220])
    upper_blue=np.array([255,255,255])

        
    frame23=cap1
        
    hsv=cv2.cvtColor(frame23,cv2.COLOR_BGR2HSV)
    blue_range=cv2.inRange(hsv,lower_blue,upper_blue)    ## 마스크 영역 분할 >> 위의 lower_blue, upper_blue 사이의 값을 제외하고는 전부 0으로 찍힘
    
    
            
    blue_result=blue_range
    
    __ ,contours1,_=cv2.findContours(blue_result,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours1:
        (x,y,w,h)=cv2.boundingRect(contour)
        if w<20:      ## 작게 잡히는 노이즈를 제거
            continue
        if h<20:      ##  위와 같음
            continue
        checkxx=w     ## 실제 길이를 구하기위해 checkparm에서 사용 할 마스크 너비
        checkyy=h     ## 실제 길이를 구하기위해 checkparm에서 사용 할 마스크 높이
        cv2.rectangle(cap1,pt1=(x,y),pt2=(x+w,y+h),color=(255,0,255),thickness=1) ##분홍색 마스크 영역을 바운딩함

        
    return cap1,checkyy,checkxx