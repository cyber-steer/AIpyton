# import dlib
#
# img = dlib.load_rgb_image('./Lena.png')
# win = dlib.image_window(img, 'My image')
#
# win.wait_until_closed()

import dlib
import time

img1 = dlib.load_rgb_image('./Lena.png')
img2 = dlib.load_rgb_image('./Lena1.png')

win1 = dlib.image_window()
win2 = dlib.image_window()
win1.set_title('My title1')
win2.set_title('My title2')


# while win.is_closed() != True:
#     win.set_image(img1)
#     time.sleep(0.5)
#     win.set_image(img2)
#     time.sleep(0.5)

win1.set_image(img1)
win2.set_image(img2)
win1.wait_for_keypress('q')
print('clicked q')

win1.wait_for_keypress(dlib.non_printable_keyboard_keys.KEY_BACKSPACE)
print('clicked BACKSPACE')