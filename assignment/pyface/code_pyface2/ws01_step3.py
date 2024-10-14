import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import tensorflow as tf
import cv2
import numpy as np
import csv
from facedetection import face_detection

print('Loading FaceNet Model')
facenet_model = tf.keras.models.load_model('facenet_keras_128.h5',compile=False)

csv_filename = 'dataset_face01.csv'

with open(csv_filename, 'r') as f:
    sample_data = list(csv.reader(f, delimiter=","))
    
print('Load dataset done')

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    
    ret, img = cap.read()
    img = cv2.flip(img,1)
    img2 = img.copy()
    
    (h, w) = img.shape[:2]

    face = face_detection(img)
    for (startX, startY, endX, endY) in face:
        cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 3)

        if startX > 0 and startY > 0 and endX < w and endY < h:
            imgcut = img2[startY:endY,startX:endX]
            face = cv2.resize(imgcut,(160,160))
            face = face.astype('float32')
            mean,std = face.mean(),face.std()
            face = (face-mean)/std
            face_test = np.expand_dims(face,axis=0)
            embedding = facenet_model.predict(face_test)
            face_embedding = embedding[0]

            keep_distance = []
            keep_name = []
            #print(len(sample_data))
            for i in range(len(sample_data)):
                sample_data = np.array(sample_data)
                #print(sample_data[0][0:128].astype('float32'))
                dataset = sample_data[i][0:128].astype('float32')
                name = sample_data[i][128]
                faces_distance = np.linalg.norm(face_embedding-dataset)
                keep_distance.append(faces_distance)
                keep_name.append(name)

            min_distance = np.argmin(keep_distance)             

            font = cv2.FONT_HERSHEY_SIMPLEX                
            if keep_distance[min_distance] < 5:  # สามารถปรับเปลี่ยนได้                  
                cv2.putText(img,keep_name[min_distance] + str(keep_distance[min_distance]),(startX, startY-10),font,1,(0,255,255),2)
                #cv2.putText(img,keep_name[min_distance],(startX, startY-10),font,1,(0,255,255),2)
            else:
                cv2.putText(img,str(keep_distance[min_distance]),(startX, startY-10),font,1,(0,255,255),2)

    cv2.imshow("img",img)      

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()






