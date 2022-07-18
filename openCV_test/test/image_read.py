import cv2

image = cv2.imread('./Lena.png')
print(type(image))

cv2.imshow('test image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()