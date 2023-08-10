import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0]
a_sum = 0
for a in arr:
    a_sum += a
    prefix_sum.append(a_sum)

#투포인터
start = 0
end = 1

result = 0
while (start<=end) and (end<=N):
    point = prefix_sum[end] - prefix_sum[start]
    if point < M: #목표 합보다 작다면
        end += 1
    elif point > M: #목표 합보다 크다면
        start += 1
    else: #목표 합과 같다면
        result += 1
        end += 1

print(result)