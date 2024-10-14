import os
import tensorflow as tf
import cv2
import numpy as np
from csv import writer

print('Loading FaceNet Model')
facenet_model = tf.keras.models.load_model('facenet_keras_128.h5',compile=False)

csv_filename = 'dataset_face01.csv'
with open(csv_filename,'w',encoding='UTF8',newline='') as f:
    writer_f = writer(f)
    f.close()

c_path = os.getcwd()
#print(c_path)

dataset_folder = 'dataset_face01'

dataset_path = os.path.join(c_path,dataset_folder)
#print(dataset_path)

file_list = []

for (root, dirs, file) in os.walk(dataset_path):
    for f in file:
        if '.jpg' in f:
            file_list.append(os.path.abspath(os.path.join(root, f)))
            #print(root)

for i in file_list:
    print(i)
    face = cv2.imread(i)
    
    face = cv2.resize(face,(160,160))
    
    face = face.astype('float32')
    
    mean,std = face.mean(),face.std()
    face = (face-mean)/std
    
    face_test = np.expand_dims(face,axis=0)
    embedding = facenet_model.predict(face_test)
    
    face_embedding = embedding[0]

    name = os.path.basename(os.path.dirname(i))
    face_embedding = face_embedding.tolist() + [name]

    with open(csv_filename,'a',encoding='UTF8',newline='') as f:
        writer_f = writer(f)
        writer_f.writerow(face_embedding)
        f.close()
