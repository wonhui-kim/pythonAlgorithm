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
books = list(map(int, sys.stdin.readline().split()))

dp = []
for i in range(len(books)):
    index = lower_bound(dp, 0, len(dp) - 1, books[i])

    if len(dp) <= index:
        dp.append(books[i])
    else:
        dp[index] = books[i]

print(N - len(dp))