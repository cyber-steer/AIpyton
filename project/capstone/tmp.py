# import time
# import threading
# from queue import Queue
#
# def sender(q):
#     data = [2020, 8, 12, 1, 55]
#     while data:
#         d = data.pop(0)
#         q.put(d)
#         print(f'sender :{d}')
#         time.sleep(1)
#     q.put(None)
#     print('sender done')
# def receiver(q):
#     while True:
#         data = q.get()
#         # print(f'data : {data}')
#         if data is None:
#             break
#         print(f'receiver : {data}')
#     print('receiver done')
#
# if __name__ == '__main__':
#     # pass
#     q = Queue()
#     q.put(100)
#     t1 = threading.Thread(target=sender, args=(q,))
#     t2 = threading.Thread(target=receiver, args=(q,))
#     t1.start()
#     t2.start()
# # data = [2020, 8, 12, 1, 55]
# # for i in range(5):
# #     print(data)
# #     d = data.pop(0)
# #     q.put(d)


# from threading import Thread
# from queue import Queue
#
# queue = Queue()
#
#
# def consumer():
#     print('Consumer waiting')  # 뒤에 나오는 put() 이후에 실행함
#     queue.get()
#     print('Consumer done')
#
#
# thread = Thread(target=consumer)
# thread.start()
#
# # 스레드가 처음으로 실행할 때도 Queue 인스턴스에 아이템이 들어가서 get 메서드에서 반환할 아이템이 생기기 전에는 마치지 못함
# print('Producer putting')
# queue.put(object())  # 앞에 나온 get() 이전에 실행
# thread.join()
# print('Producer done')
#
# # 결과
# # Consumer waiting
# # Producer putting
# # Consumer done
# # Producer done



# from queue import Queue
# import threading
# import time
#
# class Camera:
#     def detech(self,queue):
#         i = 1
#         while True:
#             i= i+1
#             queue.put(i)
#             time.sleep(1)
#
# class Web:
#     def printQueue(self, queue):
#         while True:
#             test = queue.get()
#             print(test)
#             time.sleep(1)
#
# camera = Camera()
# web = Web()
# queue= Queue()
# th1 = threading.Thread(target=camera.detech, args=(queue,))
# th2 = threading.Thread(target=web.printQueue, args=(queue,))
# th1.start()
# th2.start()
#
import random
import threading
import time
from queue import Queue


# class Test:
#     def randNum(self, q):
#         while True:
#             n = random.randint(0,9)
#             print(f"put {n}")
#             q.put(n)
#             time.sleep(1)
#             # if n == 0:
#             #     q.put(n)
#             #     time.sleep(1)
# class Tmp:
#     def printNum(self, q):
#         while True:
#             n = q.get()
#             # print(n)
#             if n%2 == 0:
#                 print(f'{n} : 짝수')
#             else:
#                 print(f'{n} : 홀수')
#
# test = Test()
# tmp = Tmp()
# q = Queue()
#
# t1 = threading.Thread(target=test.randNum, args=(q,))
# t2 = threading.Thread(target=tmp.printNum, args=(q,))
#
# t1.start()
# t2.start()

# class Test:
#     def tmp(self, q):
#         while True:
#             n = q.get()
#             # if n == 0:
#             print(n)
# q = Queue()
# test = Test()
# t = threading.Thread(target=test.tmp, args=(q,))
# t.start()
# q.put('')
# while True:
#     n = random.randint(0,9)
#     q.put(n)

from time import sleep
from threading import Thread, Event

event = Event()


def infinite_loop():
    while True:
        sleep(1)
        if event.is_set():
            print('Infinite Loop Stop!')
            print(event.is_set())
            return
        print('Infinite Loop Thread!')


if __name__ == '__main__':
    t = Thread(target=infinite_loop, daemon=True)
    t.start()

    print('Script Start!')
    for i in range(1, 6):
        sleep(0.5)
        print('for loop #{}'.format(i))
        if i == 5:
            event.set()
    # time.sleep(2)
    print('Script End!')
