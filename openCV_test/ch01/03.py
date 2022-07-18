import cv2

img = cv2.imread('../data/Lena.png')

cv2.imwrite('../data/Lena_compressed.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

saved_img = cv2.imread(params.out_png)
