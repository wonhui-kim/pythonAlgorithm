import sys

N, K = map(int, sys.stdin.readline().split())

drink = []
for i in range(N):
    drink.append(int(sys.stdin.readline()))

drink.sort()  # 이분 탐색을 위한 정렬


def parametric_search(arr, target):
    if target == 0:
        return 0

    left = 1
    right = arr[-1]  # 가장 큰 용량

    answer = 0

    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        for a in arr:
            cnt += (a // mid)

        if cnt >= target:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


print(parametric_search(drink, K))