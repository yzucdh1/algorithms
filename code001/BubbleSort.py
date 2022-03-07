# 0-N-1 选最大
# 0-N-2 选最大 0-N-3  0-N-4  ......0-1选最大
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
N = arr.__len__()
for i in range(N - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
