import cv2
import numpy as np

def sobel(img,imgreal,a,b,c,d,xxx,yyy):
    img18=img.copy()
    img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,img3=cv2.threshold(img2,0,255,cv2.THRESH_OTSU)
    g_aa=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    edge_embossing=cv2.filter2D(img3,-1,g_aa)
    retval3,labels3,stats3,centroids3=cv2.connectedComponentsWithStats(edge_embossing)
    ptx=[]
    pty=[]
    pth=[]
    ptw=[]
    for i in range(1,retval3):
        
        (x,y,w,h,area)=stats3[i]
        ptx.append(x)
        pty.append(y)
        pth.append(h)
        ptw.append(w)
        xmin,xmax=min(ptx),max(ptx)
        ymin,ymax=min(pty),max(pty)
        wmin,wmax=min(ptw),max(ptw)
        hmin,hmax=min(pth),max(pth)
        
    nodexmax=max(xxx)  ## 가장 낮은 노드의 x 좌표
    number1=np.argmax(xxx)
    nodeymax=max(yyy)  ## 가장 낮은 노드의 y 좌표
    number2=np.argmax(yyy)
    nodexmin=min(xxx)  
    nodeymin=min(yyy)  
    roi=img3[xmin:xmax+wmax,ymin:ymax+hmax]
    
    print(number1,number2,"number")
    print(xmax,ymax,xmin,ymin)
    cv2.rectangle(imgreal,(c+xmin,a+ymin),(c+nodexmax,a+ymax),(0,0,255),thickness=3)   ##전체높이 영역 바운딩
    cv2.rectangle(imgreal,(c+xmin,a+ymin),(c+nodexmax,a+nodeymax),(255,0,0),thickness=2)  ##수관높이 영역 바운딩
    cv2.rectangle(imgreal,(c+xmin,a+nodeymax),(c+nodexmax,a+ymax),(0,255,0)) ##수간높이 영역 바운딩
    return img18,imgreal,nodexmax-xmin,ymax-ymin,ymax-nodeymax

