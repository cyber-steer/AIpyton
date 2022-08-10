import cv2
from datetime import datetime
from jetson_nano.camera import Camera
from jetson_nano.doorlock import doorlock
from db.firebase_database import firebase_database
from db.firebase_storage import firebase_storage
from messenger.Telegram import Sendtelegram

if __name__ == '__main__':
    camera = Camera()
    realtime_db = firebase_database(30)
    storage = firebase_storage()
    telegram = Sendtelegram()
    doorlock = doorlock()

    while True:
        frame, name = camera.get_frame()
        cv2.imshow("webcam", frame)

        # 사람을 인식했을 경우
        if name != '':
            # 등록된 인원이 아닐경우
            if name == 'Unknown':

                # 이미지 캡쳐
                capImg = cv2.imwrite('Unknown.jpg', frame)

                # 텔레그램 메세지
                telegram.sendImg('Unknown.jpg')
                telegram.sendMessege()

                # firebase 이미지 저장
                storage.img_insert(str(datetime.now()))
            # 등록된 인원일 경우
            else:
                # firebase에 기록
                realtime_db.set(name)
                
                # 도어락 계폐
                doorlock.open()

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    print("end")