import sys
import threading
import time

import cv2
import os
import face_recognition
import numpy as np
class Camera():
    def __init__(self, path='registered', tolerance=0.45, develop=False):
        self.develop = develop
        self.path = path
        self.tolerance = tolerance
        self.classNames = []
        self.encoded_face_train = self.imgRead() # 인코딩된 훈련 데이터 저장.
        self.cap  = cv2.VideoCapture(0)
        print(f'name : {self.classNames}')
    def imgRead(self):
        images = []
        mylist = os.listdir(self.path)
        for cl in mylist:
            curImg = cv2.imread(f'{self.path}/{cl}')
            images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])

        encodeList = self.findEncodings(images)
        return encodeList
    # 훈련 데이터를 인코딩하고 함수에 저장.
    def findEncodings(self, images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encoded_face = face_recognition.face_encodings(img)[0]
            encodeList.append(encoded_face)
        return encodeList
    def getData(self):
        success, frame = self.cap.read()
        img = cv2.resize(frame, (0,0), None, 0.25,0.25)  # 인식 부분에만 크기를 1/4로 조정. (초당 프레임 향상 효과)
        faces_in_frame = face_recognition.face_locations(img)
        encoded_faces = face_recognition.face_encodings(img, faces_in_frame)

        name = self.getName(faces_in_frame , encoded_faces)
        if name != '':
            if name == 'Unknown':
                self.drow(frame, name, faces_in_frame, 'red')
            else:
                self.drow(frame, name, faces_in_frame, 'green')
        return frame, name
    def getName(self, faces_in_frame, encoded_faces):
        name =''
        for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
            faceDist = face_recognition.face_distance(self.encoded_face_train, encode_face)
            matchIndex = np.argmin(faceDist)

            min_faceDist = min(faceDist)
            if min_faceDist < self.tolerance:
                name = self.classNames[matchIndex]
            else:
                name = 'Unknown'
            if self.develop:
                print(f'{name} : {min_faceDist}')
        return name
    def drow(self, frame, name, face_loc, color):
            if color == 'red' or color == 'Red' or color == "RED":
                color = (0,0,255)
            elif color == 'green' or color == 'Green' or color == 'GREEN':
                color = (0,255,0)

            y1,x2,y2,x1 = face_loc[0]
            y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4  # 출력 프레임에 오버레이 하기 위해 4를 곱함.

            if name !='':
                cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)
                cv2.rectangle(frame, (x1,y2-35),(x2,y2), color, cv2.FILLED)
                cv2.putText(frame, name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

    def imgCaptture(self, q, send, receive):
        while True:
            if receive.is_set():
                data = q.get()
                cv2.imwrite('Unknown.jpg', data['Unknown'])
                print('img capture')
                send.setAll()
                print("send set all")
                receive.clearAll()
                print('clear all')

if __name__ == '__main__':
    camera = Camera('../registered')
    while True:
        start = time.time()
        frame, name = camera.getData()
        print(f'name : {name}')
        cv2.imshow('cam',frame)
        end = time.time()
        print(f"{end - start:.3f} sec")

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

