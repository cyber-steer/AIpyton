import cv2
import time

cam = cv2.VideoCapture(0)
while True:
    start = time.time()
    ret, frame = cam.read()
    cv2.imshow('web', frame)

    end = time.time()
    print(f"{end - start:.3f} sec")

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
