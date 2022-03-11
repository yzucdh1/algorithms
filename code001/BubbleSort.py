# 0-N-1 选最大
# 0-N-2 选最大 0-N-3  0-N-4  ......0-1选最大
import random

'''生成随机数组'''
def generateRandomArr(maxSize, maxValue):
    arrLen = random.randint(1, maxSize)
    arr = [random.randint(-maxValue, maxValue) for _ in range(arrLen)]
    return arr


'''冒泡排序'''
def bubbleSort(arr):
    N = arr.__len__()
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


success = True
for _ in range(5000):
    arr = generateRandomArr(100, 10)
    arr1 = arr.copy()
    arr1.sort()
    bubbleSort(arr)
    if arr != arr1:
        print("冒泡排序:", arr)
        print("系统排序:", arr1)
        success = False
        break
print("nice" if success else "error")
arr = generateRandomArr(100, 10)
bubbleSort(arr)
print(arr)
