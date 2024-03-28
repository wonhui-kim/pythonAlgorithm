import sys


def lower_bound(arr, left, right, value):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return left


T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    trophy = list(map(int, sys.stdin.readline().split()))

    dp = []
    info = []

    for i in range(len(trophy)):
        if (len(dp) == 0) or (dp[-1] < trophy[i]):
            dp.append(trophy[i])
            info.append([len(dp) - 1, i + 1, trophy[i]])  # lis 위치, 점프대 위치, 값 저장
        else:
            lis_idx = lower_bound(dp, 0, len(dp) - 1, trophy[i])
            dp[lis_idx] = trophy[i]
            info.append([lis_idx, i + 1, trophy[i]])

    result = []
    idx = len(dp) - 1
    for i in range(len(trophy) - 1, -1, -1):
        if info[i][0] == idx:
            result.append(info[i][1])
            idx -= 1

        if idx == -1:
            break

    result.sort()
    print(len(dp))
    for r in result:
        print(r, end=' ')
    print()