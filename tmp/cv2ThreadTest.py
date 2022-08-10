import cv2
import threading

class Test(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.camera = cv2.VideoCapture(0)
    def run(self) -> None:
        while True:
            frame = self.get()
            cv2.imshow("f",frame)
    def get(self):
        ret, frame = self.camera.read()
        return frame


# if __name__ == '__main__':
#     t = Test()
#     while True:
#         frame = t.get()
#         cv2.imshow("webcam", frame)
#
#         key = cv2.waitKey(1) & 0xFF
#
#         if key == ord("q"):
#             break
#
#     cv2.destroyAllWindows()
#     print("end")
if __name__ == '__main__':
    t = Test()
    t.start()