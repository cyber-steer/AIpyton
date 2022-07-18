import dlib

img = dlib.load_rgb_image('./Lena.png')
win = dlib.image_window(img)

detector = dlib.get_frontal_face_detector()
face = detector(img)

win.add_overlay(face)

win.wait_until_closed()