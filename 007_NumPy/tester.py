import numpy as np
#
# """ Compare NumPy data types to standard python """
#
# """ Create and indexing of array """
# a = np.array([1, 2, 3, 4, 5, 6, 7])
# print(a[2])
#
# a[0] = 10
# #array([10, 2, 3, 4, 5 ,6 ,7])
#
# a[1:4] = [10, 12, 10]
# #array([10, 10, 12, 10, 5, 6, 7])
#
# a[1:4] + 1
# #array([10, 11 ,12, 13, 10, 5, 6, 7])
#
# """ Data Types """
# arr = np.array([True, False, True, True])
# print(arr)
# print(arr.dtype)
# # Boolean
#
# arr1 = np.array(([1, 2.5]))
# print(arr1)
# print(arr1.dtype)
# # Float, because int can convert into float (1 -> 1.0)
#
# arr2 = np.array(([1, True]))
# print(arr2)
# print(arr2.dtype)
# # Int, because Boolean converts into int (True = 1)
#
# arr3 = np.array(([2.5, True]))
# print(arr3)
# print(arr3.dtype)
# # Float, because Boolean converts into Int and Int to Float (True -> 1 -> 1.0
#
# arr4 = np.fromstring("1-2-3-4-5", sep="-")
# print(arr4)
# # array([1., 2., 3., 4., 5.])
#
# #arr5 = np.fromstring(input("Write number devided by comma: "), dtype="float32", sep=", ")
# # input: 2.8, 7.6, 9.0, 2.4
# # array([2.8, 7.6, 9. , 2.4], dtype=float32)
#
#
# """ Multy-dimensional arrays """
# # Create arrays
# arr2d = np.array([[2, 4], [7, 12], [0, -6]])
#
# arr3d = np.array([[2, 5, 6], [0, 1, 0], [-1, 0, 10]],
#                  [[3, 4, 5], [7, 9, 1], [-5, -6, 2]])

#### Indexing and slicing
#arr2d[0, 0]
#2

# Methods to create filled arrays
a = np.zeros(10)
print(a)
#[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
a1 = np.ones((5, 5))
print(a1)
# #[[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

a2 = np.full((3, 2, 3, 2), np.pi)
print(a2)
# [[[[3.14159265 3.14159265]
#    [3.14159265 3.14159265]
#    [3.14159265 3.14159265]]
#
#   [[3.14159265 3.14159265]
#    [3.14159265 3.14159265]
#    [3.14159265 3.14159265]]]
#
#
#  [[[3.14159265 3.14159265]
#    [3.14159265 3.14159265]
#    [3.14159265 3.14159265]]
#
#   [[3.14159265 3.14159265]
#    [3.14159265 3.14159265]
#    [3.14159265 3.14159265]]]
#
#
#  [[[3.14159265 3.14159265]
#    [3.14159265 3.14159265]
#    [3.14159265 3.14159265]]
#
#   [[3.14159265 3.14159265]
#    [3.14159265 3.14159265]
#    [3.14159265 3.14159265]]]]


a4 = np.eye(4, 4)
print(a4)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]


# Range, linspace


































