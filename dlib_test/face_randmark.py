import dlib

img = dlib.load_rgb_image('./Lena.png')
win = dlib.image_window(img, 'Image')

detector = dlib.get_frontal_face_detector()
faces = detector(img)
win.add_overlay(faces)

predictor = dlib.shape_predictor('./68_face.dat')

for face in faces:
    landmarks = predictor(img, face)
    win.add_overlay(landmarks)

win.wait_until_closed()

