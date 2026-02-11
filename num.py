import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # print(arr)
# # print(arr[0])
# # arr[1:, 1:]
# # print(arr[1:, 1:])
# # print(arr([[5, 6], [8, 9]]))
# print(arr[1:, ::2])
print(np.eye(3, 3).astype(int).dtype)
print(np.dtype('int32'))


print(np.eye(3,3).astype("int"))
array = np.array([[1,0,0], [0, 1, 0], [0, 0, 1]])