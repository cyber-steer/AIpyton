# face_recog.py

import face_recognition
import cv2
import os
import numpy as np
import time

class VideoCamera():
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def get_frame(self):
        ret, frame = self.video.read()
        return frame

class FaceRecog():
    def __init__(self):
        # 카메라 불러오기
        self.camera = VideoCamera()

        # 사진 인코딩 목록
        self.known_face_encodings = []
        # 사진파일 이름 목록
        self.known_face_names = []

        dirname = 'ImageBasic'
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
        self.face_names = []
        self.process_this_frame = True

    def get_frame(self):
        name = ""
        frame = self.camera.get_frame()

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        if self.process_this_frame:
            # 얼굴 위치 찾기
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            # 얼굴 인코딩
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)
            self.face_names = []


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

                self.face_names.append(name)

        self.process_this_frame = not self.process_this_frame

        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        return frame, name

    def get_jpg_bytes(self):
        frame = self.get_frame()
        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()


if __name__ == '__main__':
    # 객체 생성
    face_recog = FaceRecog()
    arr = []
    while True:
         # 객체 내 메소드 실행
        start = time.time()
        frame, name = face_recog.get_frame()

        # 화면 출력
        cv2.imshow("Frame", frame)
        print("name :",name)
        if name == "":
            time.sleep(0.1)
        else:
            time.sleep(5)
        time.sleep(0.3)
        end = time.time()
        arr.append(end - start)
        print(f"{end - start:.5f} sec")
         # 종료 키
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
    sum = 0
    for sec in arr:
        sum += sec
    print("avg :",sum/len(arr))
    # do a bit of cleanup
    cv2.destroyAllWindows()
    print('finish')