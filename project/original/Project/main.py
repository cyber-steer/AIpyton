import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
from db.firebase_database import firebase_database
from db.firebase_storage import firebase_storage
from messenger.Telegram import Sendtelegram
# from doorlock import *

# DB Connection
db = firebase_database(30)
storage = firebase_storage()

# Tekegram Connection
tele = Sendtelegram()

# 훈련 데이터 폴더 정의.
path = "student"

# Serial communication
# dl = doorlock()

# 훈련 데이터 이미지를 배열에 저장하고 classNames에 파일 이름을 추가.
images = []
classNames = []
mylist = os.listdir(path)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

# 훈련 데이터를 인코딩하고 함수에 저장.
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList
encoded_face_train = findEncodings(images) # 인코딩된 훈련 데이터 저장.

# csv 파일로 내보내기.
# def markAttendance(name):
#     with open('Attendance.csv','r+') as f:
#         myDataList = f.readlines()
#         nameList = []
#         for line in myDataList:
#             entry = line.split(',')
#             nameList.append(entry[0])
#         if name not in nameList:
#             now = datetime.now()
#             time = now.strftime('%I:%M:%S:%p')
#             date = now.strftime('%d-%B-%Y')
#             f.writelines(f'\n{name}, {time}, {date}')


# Webcam에서 영상을 받아온 후 저장. (카메라 열기)
cap  = cv2.VideoCapture(1)
while True:
    found = False
    success, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 0.25,0.25)  # 인식 부분에만 크기를 1/4로 조정. (초당 프레임 향상 효과)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
    for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face)
        print(f'matches : {matches}')
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
        print(f'faceDist : {faceDist}')
        matchIndex = np.argmin(faceDist)
        print(f'matchIndex : {matchIndex}')
        if matches[matchIndex]:
            name = classNames[matchIndex].upper().lower()
            y1,x2,y2,x1 = faceloc

            y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4  # 출력 프레임에 오버레이 하기 위해 4를 곱함.
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(img,name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            # markAttendance(name)
            print(name)
            db.set(name)

            # Door Open
            # dl.doorlock()

        # If face authentication fail    
        elif not matches[matchIndex]:
            name = 'Unknown'
            y1,x2,y2,x1 = faceloc

            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4  # 출력 프레임에 오버레이 하기 위해 4를 곱함.
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,255), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0,0,255), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            capImg = cv2.imwrite('unknown.jpg', img)
            test = 'unknown.jpg'
            db.set(name)
            # storage.img_insert(str(datetime.datetime.now()))
            print(name)

            # Send message to Telegram if face authentication fails
            tele.sendImg(test)
            tele.sendMessege()
    cv2.imshow('webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
