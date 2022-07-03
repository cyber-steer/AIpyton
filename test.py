# import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
import numpy as np


# img = mpimg.imread('./myData.png')
# plt.imshow(img)
# plt.show()

my_array = np.array([[1,2,3],[4,5,6,7]])
print("데이터 :",my_array)
print("객체의 형태 :",my_array.shape)
print("차원 :",my_array.ndim)
print("요소의 자료형 :",my_array.dtype)
print("요소의크기 :",my_array.itemsize)
print("요소의 수 :",my_array.size)
