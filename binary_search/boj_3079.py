import sys

# 심사대 수 N, 사람 수 M
N, M = map(int, sys.stdin.readline().split())

# 각 심사대별 소요시간 저장
time = []
for i in range(N):
    time.append(int(sys.stdin.readline()))


def binary_search(left, right, exam, target):
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        # mid시간이 주어졌을 때 각 심사대에서 검사 가능한 사람 수 합
        person = 0
        for e in exam:
            person += (mid // e)

        if person < target:
            left = mid + 1
        else:  # 검사 가능한 수 >= target 이면 가능
            answer = mid
            right = mid - 1

    return answer


print(binary_search(0, min(time) * M, time, M))