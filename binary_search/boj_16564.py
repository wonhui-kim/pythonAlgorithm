import sys

def parametric_search(arr, start, end, target):
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        gap = 0
        for a in arr:
            if mid > a:
                gap += (mid - a)

        if gap <= target:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer


N, K = map(int, sys.stdin.readline().split())
levels = []

for i in range(N):
    levels.append(int(sys.stdin.readline()))

print(parametric_search(levels, min(levels), min(levels) + K, K))