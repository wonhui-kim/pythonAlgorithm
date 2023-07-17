import sys

# 전봇대 개수 N
N = int(sys.stdin.readline())
poles = list(map(int, sys.stdin.readline().split()))


def lower_bound(arr, left, right, value):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return left


dp = [poles[0]]
for p in poles:
    index = lower_bound(dp, 0, len(dp) - 1, p)
    if index < len(dp):
        dp[index] = p
    else:
        dp.append(p)

print(len(poles) - len(dp))