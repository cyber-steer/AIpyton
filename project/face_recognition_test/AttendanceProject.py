import cv2
import numpy as np
import face_recognition
import os

path = 'ImageBasic'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList  = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)
print('Encoding Complate')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 1, 1)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        # print(faceDis)
        matchIndex = np.armin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)




# faceLoc = face_recognition.face_locations(imgElon)[0]
# encodeElon = face_recognition.face_encodings(imgElon)[0]
# cv2.rectangle(imgElon,(faceLoc[3], faceLoc[0]), (faceLoc[1],faceLoc[2]), (0,0,255),2) #BGR
#
# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeElonTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest,(faceLocTest[3], faceLocTest[0]), (faceLocTest[1],faceLocTest[2]), (0,0,255),2) #BGR
#
# results = face_recognition.compare_faces([encodeElon], encodeElonTest)
# faceDis = face_recognition.face_distance([encodeElon], encodeElonTest)

# imgElon = face_recognition.load_image_file('./ImageBasic/elon.jpg')
# imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
# imgTest = face_recognition.load_image_file('ImageBasic/biden.jpg')
# imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)