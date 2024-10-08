import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2

cap = cv2.VideoCapture(0)

frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) #640
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) #480
fps = cap.get(cv2.CAP_PROP_FPS) #30

print('frame_width = ',frame_width)
print('frame_height = ',frame_height)
print('fps = ',fps)

while(cap.isOpened()):
    
    ret, img = cap.read()
    img = cv2.flip(img,1)

    cv2.imshow("img",img)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("testsave.jpg",img)
        print(img.shape)
        break

cap.release()
cv2.destroyAllWindows()


