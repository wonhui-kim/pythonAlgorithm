import sys


def lower_bound(arr, left, right, value):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return left


def lis(arr):
    dp = []

    for a in arr:
        if (len(dp) == 0) or (dp[-1] < a):
            dp.append(a)
        else:
            dp[lower_bound(dp, 0, len(dp) - 1, a)] = a

    return len(dp)


T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())

    port = []
    for i in range(N):
        port.append(int(sys.stdin.readline()))

    print(lis(port))