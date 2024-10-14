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
            embedding = facenet_model.predict(face_test,verbose=0)
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

            keep_distance = np.array(keep_distance)
            keep_name = np.array(keep_name)
            #print(keep_distance)
            #print(keep_name)
            name_unique = np.unique(keep_name)
            keep_name_dist = []
            for i in name_unique:
                name_dist = np.where(keep_name==i,keep_distance,0)
                name_num = len(np.nonzero(name_dist)[0])
                #print(sum(name_dist)/name_num)
                #print(name_num)
                keep_name_dist.append(sum(name_dist)/name_num)
            #print(keep_name_dist)
            min_keep_name_dist = np.argmin(keep_name_dist)
            min_name_unique = name_unique[min_keep_name_dist]
            #print(min_keep_name_dist)
            #print(min_name_unique)

            font = cv2.FONT_HERSHEY_SIMPLEX
            distance = int(np.min(keep_name_dist)*100)/100
            if distance < 7:                    
                cv2.putText(img,min_name_unique + ' ' + str(distance),(startX, startY-10),font,1,(255,255,0),2)
            else:
                pass
                #cv2.putText(img,str(distance),(startX, startY-10),font,1,(0,0,255),2)

    cv2.imshow("img",img)      

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()






