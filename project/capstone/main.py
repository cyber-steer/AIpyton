import threading
import time
from queue import Queue

import cv2

from jetson_nano.camera import Camera
from jetson_nano.doorlock import Doorlock
from db.firebase_database import firebase_database
from db.firebase_storage import firebase_storage
from messenger.Telegram import Telegram
from messenger.thread_queue import Thread_Queue
from messenger.thread_event import Thread_Event

if __name__ == '__main__':
    # instance create ==============================================================
    # main --------------------------------------------------------------
    camera = Camera(tolerance=0.6,develop=True)
    # known --------------------------------------------------------------
    realtime_db = firebase_database(30)
    doorlock = Doorlock()
    # unknown --------------------------------------------------------------
    storage = firebase_storage()
    telegram = Telegram()
    # event --------------------------------------------------------------
    send_evnet = Thread_Event()
    receive_evnet = Thread_Event()
    update_event = threading.Event()
    patch_event = threading.Event()
    # queue --------------------------------------------------------------
    q = Thread_Queue()
    names_q = Queue()
    number_q = Queue()

    # thread create ==============================================================
    # knwon --------------------------------------------------------------
    realtime_thread = threading.Thread(
        target=realtime_db.insert, args=(q.get_realtime(),), daemon=True)
    doorlock_thread = threading.Thread(
        target=doorlock.action, args=(q.get_doorlock(),), daemon=True)
    # unknwon--------------------------------------------------------------
    capture_thread = threading.Thread(
        target=camera.imgCaptture, args=(q.get_capture(), send_evnet, receive_evnet), daemon=True)
    storage_thread = threading.Thread(
        target=storage.insert, args=(q.get_storage(), receive_evnet.get_a(), send_evnet.get_a()), daemon=True)
    telegram_thread = threading.Thread(
        target=telegram.send, args=(q.get_telegram(), receive_evnet.get_b(), send_evnet.get_b()), daemon=True)
    # update--------------------------------------------------------------
    observer_thread = threading.Thread(
        target=realtime_db.observer, args=(q.get_update(), update_event), daemon=True)
    update_thread = threading.Thread(
        target=storage.update, args=(q.get_update(), patch_event), daemon=True)
    patch_thread = threading.Thread(
        target=camera.data_update, args=(patch_event, update_event, realtime_db), daemon=True)

    # thread start ==============================================================
    # knwon--------------------------------------------------------------
    realtime_thread.start()
    doorlock_thread.start()
    # unknwon--------------------------------------------------------------
    capture_thread.start()
    storage_thread.start()
    telegram_thread.start()
    # update--------------------------------------------------------------
    observer_thread.start()
    update_thread.start()
    patch_thread.start()

    # main preparation ==============================================================
    # unkown receive ready
    receive_evnet.setAll()

    # number to eng name
    numbers = camera.get_numbers()
    camera.set_names(realtime_db.changeName(numbers))

    # main start ==============================================================
    while True:
        update = False
        if update_event.is_set():
            update = True
        frame, name = camera.getData(update)

        # cv2.namedWindow("webcam", cv2.WND_PROP_FULLSCREEN)
        # cv2.setWindowProperty("webcam", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("webcam", frame)
        # 등록된 인원이 아닐경우
        if name == 'Unknown':
            q.put_img('Unknown',frame)
        elif name != '':
            q.put(name)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    print("end")