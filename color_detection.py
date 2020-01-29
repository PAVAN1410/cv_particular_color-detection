#for blue color approx values are below
#(93,51,51)
#(130,255,255)
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
def nothing(x):
    pass
cv2.namedWindow('Tracking')
cv2.createTrackbar("lh","Tracking",0,255,nothing)
cv2.createTrackbar("ls","Tracking",0,255,nothing)
cv2.createTrackbar("lv","Tracking",0,255,nothing)
cv2.createTrackbar("uh","Tracking",255,255,nothing)
cv2.createTrackbar("us","Tracking",255,255,nothing)
cv2.createTrackbar("uv","Tracking",255,255,nothing)
while True:        
   #frame=cv2.imread(r'C:\Users\smarties.png') for still picture
    _,frame=cap.read(0)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos('lh','Tracking')
    ls=cv2.getTrackbarPos('ls','Tracking')
    lv=cv2.getTrackbarPos('lv','Tracking')
    uh=cv2.getTrackbarPos('uh','Tracking')
    us=cv2.getTrackbarPos('us','Tracking')
    uv=cv2.getTrackbarPos('uv','Tracking')
    
    l_b=np.array([lh,ls,lv])
    u_p=np.array([uh,us,uv])
    mask=cv2.inRange(hsv,l_b,u_p)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(1)
    if k==ord('a'):
        break
cap.release()
cv2.destroyAllWindows()                 
