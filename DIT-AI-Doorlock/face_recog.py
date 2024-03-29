# face_recog.py

import face_recognition
import cv2
import camera
import os
import numpy as np
import time
import firebase
import datetime
import twilio_part
import PIL
import jetson_nano
import serial

a = 0
isN = 1
b = 0

class FaceRecog():
    pass

    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.camera = camera.VideoCamera()

        self.known_face_encodings = []
        self.known_face_names = []

        # Load sample pictures and learn how to recognize it.
        dirname = 'ImageBasic'
        files = os.listdir(dirname)
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ext == '.jpg':
                self.known_face_names.append(name)
                pathname = os.path.join(dirname, filename)
                img = face_recognition.load_image_file(pathname)
                face_encoding = face_recognition.face_encodings(img)[0]
                self.known_face_encodings.append(face_encoding)

        # Initialize some variables
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

    def __del__(self):
        del self.camera

    def get_frame(self):
        name=""
        # Grab a single frame of video
        frame = self.camera.get_frame()
        print("start frame :",id(frame))

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if self.process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

            self.face_names = []

            count = 0

            for face_encoding in self.face_encodings:
                # See if the face is a match for the known face(s)
                distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                min_value = min(distances)

                # tolerance: How much distance between faces to consider it a match. Lower is more strict.
                # 0.6 is typical best performance.

                if min_value < 0.45:
                    index = np.argmin(distances)
                    name = self.known_face_names[index]

                    global a
                    global isN
                    global b
                    a += 1
                    b += 1

                    if a > 6 and isN == 1:
                        print("잠금 해제!")
                        a = 0
                        time.sleep(5)
                        # jetson_nano.arduino()

                        ser = serial.Serial('COM3', 9600)

                        val = isN

                        if val == '1':
                            val = val.encode('utf-8')
                            ser.write(val)

                        if b > 6:
                            img = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
                            # cv2.imwrite(img, frame)
                            # firebase.fileUpload(img)
                            # twilio_part.sendMessage(img)

                            b = 0
                            time.sleep(5)

                else:
                    name = "Unknown"

                    b += 1

                    if b > 20:
                        img = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
                        # cv2.imwrite(img, frame)
                        # firebase.fileUpload(img)
                        # twilio_part.sendMessage(img)
                        b = 0
                        time.sleep(5)

                self.face_names.append(name)

        self.process_this_frame = not self.process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        print("return frame :",id(frame))
        return frame, name

    def get_jpg_bytes(self):
        frame = self.get_frame()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()


if __name__ == '__main__':
    face_recog = FaceRecog()
    print(face_recog.known_face_names)
    arr = []
    while True:
        start = time.time()
        frame, name = face_recog.get_frame()

        # show the frame
        cv2.imshow("Frame", frame)
        print("main frame :",id(frame))
        print("name :",name)
        if name == "":
            time.sleep(0.1)
        else:
            time.sleep(10)
        time.sleep(0.3)
        end = time.time()

        arr.append(end - start)
        print(f"{end - start:.5f} sec")
        key = cv2.waitKey(1) & 0xFF
        print("key :", key)

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
    sum = 0
    for sec in arr:
        sum += sec
    print("avg :",sum/len(arr))
    # do a bit of cleanup
    cv2.destroyAllWindows()
    print('finish')