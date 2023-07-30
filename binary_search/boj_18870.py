import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

s = set(arr)
sorted_arr = sorted(s)


def lower_bound(left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


for a in arr:
    index = lower_bound(0, len(sorted_arr) - 1, a)
    print(index, end=' ')