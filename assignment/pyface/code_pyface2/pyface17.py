import cv2
from facedetection import face_detection

cap = cv2.VideoCapture('face_m1.mp4')
#cap = cv2.VideoCapture('face_m2.mp4')

while True:
    ret, img = cap.read()
    
    key = cv2.waitKey(10) & 0xFF 
    if (key == ord('q')) or (ret == False):
        break

    face = face_detection(img)
    for (startX, startY, endX, endY) in face:
        cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 3)

    cv2.imshow('img',img) 

cv2.destroyAllWindows()
cap.release()
