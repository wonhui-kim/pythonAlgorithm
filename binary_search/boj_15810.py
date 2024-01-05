import sys


def parametric_search(arr, start, end, target):
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        balloons = 0

        for a in arr:
            balloons += (mid // a)

        if balloons >= target:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


N, M = map(int, sys.stdin.readline().split())
time = list(map(int, sys.stdin.readline().split()))

# 가장 오래걸릴 수 있는 시간은 가장 긴 시간 * 풍선 개수
max_time = max(time) * M
print(parametric_search(time, 1, max_time, M))