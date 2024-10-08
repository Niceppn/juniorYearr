import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    
    ret, img = cap.read()
    img = cv2.flip(img,1)          

    key = cv2.waitKey(1) & 0xFF
    
    font = cv2.FONT_HERSHEY_SIMPLEX    
    cv2.putText(img,str(key),(20,200),font,3,(255,255,0),5) #BGR
    cv2.putText(img,chr(key),(20,300),font,3,(0,255,255),5) #BGR
    
    cv2.imshow("img",img)
    
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


