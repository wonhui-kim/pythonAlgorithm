import sys


def binary_search(arr, start, end, target):
    start += 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0


T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()

    answer = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            interval = abs(arr[j] - arr[i])
            find = arr[j] + interval
            answer += binary_search(arr, j, len(arr) - 1, find)

    print(answer)