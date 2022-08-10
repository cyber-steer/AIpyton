import cv2
import face_recognition

img = face_recognition.load_image_file('ImageBasic/elon.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


faceLoc = face_recognition.face_locations(img)[0]
encodeElon = face_recognition.face_encodings(img)[0]
print(faceLoc)
cv2.circle(img, (132,98),3,(0,0,255),-1)
cv2.circle(img, (287,257),3,(0,255,0),-1)

cv2.imshow('img',img)
cv2.waitKey(0)