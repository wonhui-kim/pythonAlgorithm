import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0]
a_sum = 0
for a in arr:
    a_sum += a
    prefix_sum.append(a_sum)

result = -100 * N
for i in range(K, N+1):
    temp = prefix_sum[i] - prefix_sum[i-K]
    result = max(result, temp)

print(result)