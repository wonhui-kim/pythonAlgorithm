import sys

N = int(sys.stdin.readline())
ink = list(map(int, sys.stdin.readline().split()))
viscosity = list(map(int, sys.stdin.readline().split()))


def upper_bound(arr, left, right, value):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= value:
            left = mid + 1
        else:
            right = mid - 1

    return left


result = []
for i in range(len(ink)):
    color = upper_bound(viscosity, 0, len(ink) - 1, ink[i]) - i - 1

    if color < 0:
        result.append(0)
    else:
        result.append(color)

for r in result:
    print(r, end=' ')