import sys

# 조카 수 M, 과자 수 N
M, N = map(int, sys.stdin.readline().split())

snack = list(map(int, sys.stdin.readline().split()))
snack.sort()  # 이분탐색 위해 오름차순 정렬

def parametric_search(left, right, target):
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        for s in snack:  # 현재 mid값으로 몇개의 조각이 나오는지 체크
            cnt += (s // mid)

        if cnt >= target:  # 많거나 같으면 나눠줄 수 있으나, 최대 길이를 구하므로 계속 진행
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

print(parametric_search(1, snack[-1], M))


