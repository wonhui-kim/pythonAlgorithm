import sys

# 주가 개수
N = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))
dp = [data[0]]


def lower_bound(arr, left, right, value):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return left


for d in data:
    index = lower_bound(dp, 0, len(dp) - 1, d)
    if index < len(dp):
        dp[index] = d
    else:
        dp.append(d)

print(len(dp))