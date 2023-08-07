import sys

# 수열 A의 크기
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))


def lower_bound_reverse(left, right, arr, target):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            left = mid + 1
        else:
            right = mid - 1

    return left


dp = [A[0]]
for i in range(1, N):
    index = lower_bound_reverse(0, len(dp) - 1, dp, A[i])

    if index < len(dp):
        dp[index] = A[i]
    else:
        dp.append(A[i])

print(len(dp))