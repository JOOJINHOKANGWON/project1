
maskrealh=20  ## 실제 마스크 높이
maskrealw=20  ## 실제 마스크 너비
def checkhow(h,w,aa,bb,cc):

    print('aavv',h)  ## 마스크 높이 픽셀값
    print(w)  ## 마스크 너비 픽셀값
    print(aa) ## 나무 폭
    print(bb) ## 나무 전체높이
    print(cc) ## 나무 수간높이

    realh=maskrealh/h ## 실제 길이를 마스크 픽셀길이로 나눠서 1픽셀당 실제 길이를 realh라는 변수로 잡음
    realw=maskrealw/w ## 위와 똑같음 realw는 1픽셀당 실제 너비
    print(realh,realw)

    totalh=realh*bb  ##전체높이
    totalw=realw*aa  ## 전체 폭
    smh=realh*cc     ## 수간높이
    sgh=totalh-smh   ## 수관높이
    print(totalh,totalw,smh,sgh)