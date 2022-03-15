# 0-N-1选出最小的放在0  1-N-1选出最小的放在1  2-N-1......N-2-N-1
import random

def generateRandomArr(maxSize, maxValue):
    len = random.randint(1, maxSize)
    arr = [random.randint(-maxValue, maxValue) for _ in range(len)]
    return arr

def selectSort(arr):
    N = arr.__len__()
    for i in range(N - 1):
        minIndex = i
        for j in range(i + 1, N):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

success = True
for _ in range(50000):
    arr = generateRandomArr(10, 100)
    arr1 = arr.copy()
    arr1.sort()
    selectSort(arr)
    if arr != arr1:
        print("选择排序:", arr)
        print("系统排序:", arr1)
        success = False
        break
print("nice" if success else "error")
arr2 = generateRandomArr(10, 100)
selectSort(arr2)
print(arr2)
