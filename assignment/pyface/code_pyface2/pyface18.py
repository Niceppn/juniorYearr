import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
from facedetection import face_detection

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    
    ret, img = cap.read()
    img = cv2.flip(img,1)
    
    face = face_detection(img)
    for (startX, startY, endX, endY) in face:
        cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 3)

    cv2.imshow("img",img)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


