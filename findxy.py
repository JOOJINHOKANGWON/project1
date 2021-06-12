import numpy as np

def find(img6):  ### findnode에서 넘긴 이미지에서 함수가 노드라고 인식한 점들의 좌표를 리스트에 저장
    print(img6)
    sum=0
    xx=[]
    yy=[]
    rows,cols=img6.shape[:2]
    for row in range(rows):
        for col in range(cols):
            if img6[row,col] ==0:
                continue
            yy.append(row)
            xx.append(col)
            sum+=1
    return xx,yy
        