import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
from facedetection import face_detection

cap = cv2.VideoCapture(0)

count = 1

while(cap.isOpened()):
    
    ret, img = cap.read()
    img = cv2.flip(img,1)
    img2 = img.copy()

    (h, w) = img.shape[:2]
    
    face = face_detection(img)
    for (startX, startY, endX, endY) in face:
        cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 3)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            if startX > 0 and startY > 0 and endX < w and endY < h:
                filesave = str(count)+".jpg"
                imgcut = img2[startY:endY,startX:endX]
                cv2.imwrite(filesave,imgcut)
                count = count + 1
                print(filesave)
                
    cv2.imshow("img",img) 
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


