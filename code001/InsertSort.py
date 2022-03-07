# 0-1插入1  0-2插入2  0-3插入3  ..... 0-N-1插入N-1
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
N = arr.__len__()
for i in range(1, N):
    j = i - 1
    while j >= 0 and arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        j -= 1

print(arr)
