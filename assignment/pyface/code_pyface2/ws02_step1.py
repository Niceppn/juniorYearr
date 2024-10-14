import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('clip_video.avi', fourcc,30.0,(640,480))

rec = False
while cap.isOpened():
    ret, img = cap.read()
    img = cv2.flip(img,1)
    
    dt = time.localtime()
    DD = ("{:02d}".format(dt[2])+'/'+"{:02d}".format(dt[1])+'/'+"{:02d}".format(dt[0]))
    TT = ("{:02d}".format(dt[3])+':'+"{:02d}".format(dt[4])+':'+"{:02d}".format(dt[5]))

    cv2.putText(img,DD,(100,50),font,1,(0,255,0),3)
    cv2.putText(img,TT,(350,50),font,1,(0,255,255),3)
    cv2.circle(img,(600,40),15,(255,255,255),-1)
    
    key = cv2.waitKey(1)
    
    if key == ord('s'):
        rec = True
        print("Start Recording")
        
    if rec == True:
        cv2.circle(img,(600,40),15,(0,0,255),-1)
        out.write(img)

    cv2.imshow('img', img)
    
    if key == ord('q'):
        print("Exit")
        break

cap.release()
out.release()
cv2.destroyAllWindows()

