import sys

# 수열A의 크기
N = int(sys.stdin.readline())

# 수열A
A = list(map(int, sys.stdin.readline().split()))


def lower_bound(table, left, right, value):
    while left <= right:
        mid = (left + right) // 2

        if table[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return left


dp = []
for i in A:
    index = lower_bound(dp, 0, len(dp) - 1, i)
    if len(dp) > index:
        dp[index] = i
    else:
        dp.append(i)

print(len(dp))