import threading
import time
import logging
from queue import Queue


def consumer1(cv, e):
    print('firebase start')
    while True:
        with cv:
            cv.wait()
            print('파이어베이스 저장')
            e.clear()
def consumer2(cv, e):
    print('telegram start')
    while True:
        with cv:
            cv.wait()
            print('텔레그램 전송')
            e.clear()

def producer(cv,e1, e2, q):
    print('img start')
    while True:
        with cv:
            if e1.is_set() and e2.is_set():
                name = q.get()
                print('사진 저장', name)
                cv.notify_all()

if __name__ == '__main__':
    condition = threading.Condition()
    e1 = threading.Event()
    e2 = threading.Event()
    q = Queue()

    # e1.set()
    # e2.set()
    # cs1 = threading.Thread(name='consumer1', target=consumer1, args=(condition, e1), daemon=True)
    # cs2 = threading.Thread(name='consumer2', target=consumer2, args=(condition, e2), daemon=True)
    # pd = threading.Thread(name='producer', target=producer, args=(condition, e1, e2, q), daemon=True)
    #
    # cs1.start()
    # cs2.start()
    # pd.start()
    # q.put('hel')
    # q.put('lo')
    # time.sleep(5)

    print("start :",condition.release())
    # condition.wait(0.5)
    print("wait :",condition)
