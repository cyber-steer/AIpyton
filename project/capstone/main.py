import threading
import time

import cv2

from jetson_nano.camera import Camera
from jetson_nano.doorlock import Doorlock
from db.firebase_database import firebase_database
from db.firebase_storage import firebase_storage
from messenger.Telegram import Telegram
from messenger.thread_queue import Thread_Queue
from messenger.thread_event import Thread_Event

if __name__ == '__main__':
    camera = Camera()
    realtime_db = firebase_database(30)
    storage = firebase_storage()
    telegram = Telegram()
    doorlock = Doorlock()
    q = Thread_Queue()
    send_evnet = Thread_Event()
    receive_evnet = Thread_Event()

    realtime_thread = threading.Thread(
        target=realtime_db.insert, args=(q.get_realtime(),), daemon=True)
    storage_thread = threading.Thread(
        target=storage.insert, args=(q.get_storage(), receive_evnet.get_storage(), send_evnet.get_storage()), daemon=True)
    telegram_thread = threading.Thread(
        target=telegram.send, args=(q.get_telegram(), receive_evnet.get_telegram(), send_evnet.get_telegram()), daemon=True)
    doorlock_thread = threading.Thread(
        target=doorlock.action, args=(q.get_doorlock(),), daemon=True)
    capture_thread = threading.Thread(
        target=camera.imgCaptture, args=(q.get_capture(), send_evnet, receive_evnet), daemon=True)

    realtime_thread.start()
    storage_thread.start()
    telegram_thread.start()
    doorlock_thread.start()
    capture_thread.start()

    receive_evnet.setAll()
    while True:
        frame, name = camera.getData()
        # cv2.namedWindow("webcam", cv2.WND_PROP_FULLSCREEN)
        # cv2.setWindowProperty("webcam", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("webcam", frame)
        # 등록된 인원이 아닐경우
        if name == 'Unknown':
            q.put_img('Unknown',frame)
        elif name != '':
            q.put(name)

        print()
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    print("end")