import numpy as np

list_data = [1,2,3]
array = np.array(list_data)

print(array)
print(array.size)
print(array.dtype)
print(array[1])

print()

print("0부터 n-1까지의 1차원")
array1 = np.arange(4)
print(array1)
print()

print("2차원 초기화 실수")
array2 = np.zeros((5,5), dtype=float)
print(array2)
print()

print("2차원 초기화 문자")
array3 = np.ones((3,3), dtype=str)
print(array3)
print()

print("2차원 n부터 m-1까지 랜덤")
array5 = np.random.randint(1, 10, (3,3))
print(array5)

print("평균 0, 표준편차 1, 표준 정규")
array6 = np.random.normal(0,1,(5,5))
print(array6)
print()

print("배열 합치기")
array7 = np.concatenate([array, array1])
print(array7)
print()

print("차원 변경")
array8 = np.array([1,2,3,4])
array8 = array8.reshape((2,2))
print(array8)
print()

print("차원 합치기 (axis)")
arr1 = np.arange(4).reshape(1,4)
arr2 = np.arange(8).reshape(2,4)
array9 = np.concatenate([arr1, arr2],axis=0)
print(array9)
print()

print("분리")
left, right = np.split(arr2, [2], axis=1)
print(left)
print(right)
print()