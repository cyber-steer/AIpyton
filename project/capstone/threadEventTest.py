# Python program to explain the
# use of wait() method in Event() class
import threading
import time


def helper_function(event_obj, timeout, i):
    # Thread has started, but it will wait 10 seconds for the event
    print("Thread start")

    # flag = event_obj.wait(timeout)
    flag = event_obj.wait()
    if flag:
        print("flag True")
    else:
        print("flag False")


if __name__ == '__main__':
    # Initialising an event object
    event_obj = threading.Event()

    # starting the thread who will wait for the event
    thread1 = threading.Thread(target=helper_function, args=(event_obj, 3, 27))
    thread1.start()
    # sleeping the current thread for 5 seconds
    time.sleep(1)

    # generating the event
    event_obj.set()
    print("end")
    print()