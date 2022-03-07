# 0-N-1选出最小的放在0  1-N-1选出最小的放在1  2-N-1......N-2-N-1
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
N = arr.__len__()
for i in range(N - 1):
    minIndex = i
    for j in range(i + 1, N):
        if arr[minIndex] > arr[j]:
            minIndex = j
    arr[i], arr[minIndex] = arr[minIndex], arr[i]

print(arr)
