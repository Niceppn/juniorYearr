import cv2
from facedetection import face_detection

img = cv2.imread("face1.jpg")
#img = cv2.imread("face2.jpg")
#img = cv2.imread("face3.jpg")

face = face_detection(img)

for (startX, startY, endX, endY) in face:
    cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,str(len(face)),(20,250),font,3,(255,255,0),10) 
      
cv2.imshow("img",img)

cv2.waitKey()
cv2.destroyAllWindows()
