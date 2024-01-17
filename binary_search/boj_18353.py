import sys

def lower_bound(arr, start, end, target):
    while (start <= end):
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start

N = int(sys.stdin.readline())
soldiers = list(map(int, sys.stdin.readline().split()))
reversed_soldiers = soldiers[::-1]

dp = []
for i in range(len(reversed_soldiers)):
    index = lower_bound(dp, 0, len(dp) - 1, reversed_soldiers[i])

    if len(dp) <= index:
        dp.append(reversed_soldiers[i])
    else:
        dp[index] = reversed_soldiers[i]

print(N - len(dp))