import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='../data/Lena.png', help='Image path.')
params = parser.parse_args()
img = cv2.imread(params.path)

assert img is not None
print('read {}'.format(params.path))
print('shape:',img.shape)
print('dtype:',img.dtype)

img = cv2.imread(params.path, cv2.IMREAD_GRAYSCALE)
assert img is not None

print('read {} as graysclae'.format(params.path))
print('shape:',img.shape)
print('dtype:',img.dtype)

img = cv2.imread('../data/Lena.png')
print('original image shape:',img.shape)

width, height = 128, 256
resized_img = cv2.resize(img, (width, height))
print('resized to 128x256 image shpae:', resized_img.shape)

w_mult, h_mult = 0.25, 0.5
resized_img = cv2.resize(img, (0,0), resized_img, w_mult, h_mult)
print('image shape:', resized_img.shape)

w_mult, h_mult = 2, 4
resized_img = cv2.resize(img, (0, 0), resized_img, w_mult, h_mult, cv2.INTER_NEAREST)
print('half sized image shape:', resized_img.shape)

img_flip_along_x = cv2.flip(img, 0)

img_flip_along_y = cv2.flip(img, 1)
img_flip_along_xy = cv2.flip(img, -1)-9630

img = cv2.imread('../data/Lena.png')

cv2.imwrite('../data/Lena_compressed.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

saved_img = cv2.imread('Lena_compressed.png')
assert saved_img.all() == img.all()

cv2.imwrite('../data/Lena_compressed.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 0])
