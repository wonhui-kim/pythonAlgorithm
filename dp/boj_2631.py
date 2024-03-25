import sys

N = int(sys.stdin.readline())
student = []
for i in range(N):
    student.append(int(sys.stdin.readline()))


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

    for i in range(len(arr)):
        if (len(dp) == 0) or (dp[-1] < arr[i]):
            dp.append(arr[i])
        else:
            dp[lower_bound(dp, 0, len(dp) - 1, arr[i])] = arr[i]

    return len(dp)


print(N - lis(student))