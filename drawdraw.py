import cv2
import numpy as np
import copy

ptsx=[]
ptsy=[]                  
isDragging = False            
count=0
markerId = 1   
# 화면 출력
colors = [] 
rois=[]
a,b,c,d=0,0,0,0
rows,cols=0,0
def onMouse(event, x, y, flags,img):
    marker=[]
    global a,b,c,d
    global isDragging, count ,ptsx , ptsy, rois
    if event==cv2.EVENT_LBUTTONDOWN:
        isDragging=True
        
    elif event==cv2.EVENT_MOUSEMOVE:
        if isDragging:
            cv2.circle(img,(x,y),2,color=(255,255,255),thickness=2)
            cv2.imshow('watershed',img)

    elif event==cv2.EVENT_LBUTTONUP:
        isDragging=False
        ptsx.append(x)
        ptsy.append(y)
        print(ptsx)#
        print(ptsy)        #
        a=min(ptsx)#
        b=max(ptsx)#                   점으로 찍은 네 좌표를 취합해서
        c=min(ptsy)#                  직사각형을 그림
        d=max(ptsy)
        count=count +1#
        print(count)#
        if count==4:#
            rois=img[c:d,a:b]#
            cv2.imwrite('rois.png',rois)
            print(c,d,a,b)
            key=cv2.waitKey(0) &0xFF
            if key=='i':
                cv2.destroyAllWindows()



    

def startt(img):
    global count
    global rows,cols
    global a,b,c,d
    rows, cols = img.shape[:2]
    

    
    pure=np.zeros((3,3))

    cv2.imshow('watershed', img)
    while True:
        cv2.setMouseCallback('watershed', onMouse,img)
        cv2.waitKey(0)
        if count==4:
            break
    return rois,a,b,c,d
    

