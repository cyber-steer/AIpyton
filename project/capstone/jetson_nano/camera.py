import sys
import time

import cv2
import os
import face_recognition
import numpy as np
class Camera():
    def __init__(self):
        # 카메라 불러오기
        self.camera = cv2.VideoCapture(0)
        # 사진 인코딩 목록
        self.known_face_encodings = []
        # 사진파일 이름 목록
        self.known_face_names = []
        dirname = 'registered'
        files = os.listdir(dirname)
        print("file :",files)
        for filename in files:
            # name:파일명, ext:확장자
            name, ext = os.path.splitext(filename)
            if ext == '.jpg':
                self.known_face_names.append(name)
                pathname = os.path.join(dirname, filename)
                img = face_recognition.load_image_file(pathname)
                face_encoding = face_recognition.face_encodings(img)[0]
                self.known_face_encodings.append(face_encoding)

        self.face_locations = []
        self.face_encodings = []
        self.process_this_frame = True

    def get_frame(self):
        name = ""
        ret, frame = self.camera.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if self.process_this_frame:
            name = self.get_name(rgb_small_frame)

        self.process_this_frame = not self.process_this_frame
        if name != "":
            print("name :",name)
            if name == 'Unknown':
                self.draw(frame, 'red')
            else:
                self.draw(frame, 'green')

        return frame, name

    def get_name(self, rgb_small_frame):
        # 얼굴 위치 찾기
        self.face_locations = face_recognition.face_locations(rgb_small_frame)
        # 얼굴 인코딩
        self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)
        self.face_names = []
        name = ''

        for face_encoding in self.face_encodings:
            # 사진들과 오차율
            distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            # 가장작은 오차율
            min_value = min(distances)
            print("dist :",min_value)


            # 등록된 인원일시
            # if min_value < 0.45:
            if min_value < 0.47:
                index = np.argmin(distances)
                name = self.known_face_names[index]
            # 등록된 인원이 아닐시
            else:
                name = "Unknown"

            print("name :",name)
            self.face_names.append(name)
        return name
    def draw(self, frame, color):
        if color == 'red' or color == 'Red' or color == "RED":
            color = (0,0,255)
        elif color == 'green' or color == 'Green' or color == 'GREEN':
            color = (0,255,0)
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # 확인 용 그림
        h,w,c = frame.shape
        print("h :",h,", w :",w,", c :",c)
        right = w
        bottom = int(h/10)
        cv2.rectangle(frame, (0, 0), (right, bottom), color, -1)

    def draw_check(self):
        pass


if __name__ == '__main__':
    camera = Camera()
    while True:
        frame = camera.get_frame()
        cv2.imshow("webcam", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    print("end")