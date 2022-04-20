# 二分查找算法
import random


# 查找最靠右的索引
def binarySearch(lst, num):
    if lst is None or len(lst) == 0:
        return -1
    begin = 0
    end = len(lst) - 1
    maxIndex = -1
    while begin <= end:
        midden = (begin + end) // 2
        if lst[midden] == num:
            maxIndex = midden
            begin = midden + 1
        elif lst[midden] > num:
            end = midden - 1
        elif lst[midden] < num:
            begin = midden + 1
    return maxIndex


def loopSearch(lst, num):
    if lst is None or len(lst) == 0:
        return -1
    maxIndex = -1
    for index, value in enumerate(lst):
        if value == num:
            maxIndex = index
    return maxIndex


if __name__ == '__main__':
    flag = True
    for _ in range(1, 10):
        lst = [random.randint(1, 10) for _ in range(10)]
        num = random.randint(1, 10)
        lst.sort()
        loopRes = loopSearch(lst, num)
        binaryRes = binarySearch(lst, num)
        print(f'列表为:{lst}')
        print(f'查找数字为:{num}')
        print(f'循环查找的结果为:{loopRes}')
        print(f'二分查找的结果为:{binaryRes}')
        print('-' * 50)
        if loopRes != binaryRes:
            print('fuck error!')
            print(f'列表为:{lst}')
            print(f'查找数字为:{num}')
            print(f'循环查找的结果为:{loopRes}')
            print(f'二分查找的结果为:{binaryRes}')
            flag = False
            break
    if flag:
        print('nice success!')
