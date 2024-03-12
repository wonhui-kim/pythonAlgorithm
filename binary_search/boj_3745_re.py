import sys


def lower_bound(arr, left, right, value):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return left


while True:
    try:
        N = int(sys.stdin.readline())
        stock = map(int, sys.stdin.readline().split())

        dp = []
        for s in stock:
            if (len(dp) == 0) or (dp[-1] < s):
                dp.append(s)
            else:
                dp[lower_bound(dp, 0, len(dp) - 1, s)] = s

        print(len(dp))
    except:
        break