# 0-1插入1  0-2插入2  0-3插入3  ..... 0-N-1插入N-1
import random

#生成随机数组
def generateRandomArr(maxSize, maxValue):
    len = random.randint(1, maxSize)
    arr = [random.randint(-maxValue,maxValue) for _ in range(len)]
    return arr

#插入排序
def insertSort(arr):
    N = arr.__len__()
    for i in range(1, N):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1

success = True
for _ in range(50000):
    arr = generateRandomArr(10, 100)
    arr1 = arr.copy()
    arr1.sort()
    insertSort(arr)
    if arr != arr1:
        print("插入排序:", arr)
        print("系统排序:", arr1)
        success = False
        break
print("nice" if success else "error")
arr2 = generateRandomArr(10, 100)
insertSort(arr2)
print(arr2)
