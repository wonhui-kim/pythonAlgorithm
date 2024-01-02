import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

cur = arr[0]
prefix_sum = [0, cur]
for i in range(1, len(arr)):
    cur += arr[i]
    prefix_sum.append(cur)

M = int(sys.stdin.readline())
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(prefix_sum[end]-prefix_sum[start-1])