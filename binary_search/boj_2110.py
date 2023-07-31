import sys

# 집 개수 N, 공유기 개수 C
N, C = map(int, sys.stdin.readline().split())

house = []
for i in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()  # 오름차순 정렬


def binary_search(left, right, target):
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        cnt = 1
        start = house[0]  # 첫번째 집 시작
        for i in range(1, len(house)):
            if house[i] >= start + mid: #시작 집으로부터 mid값 더한 값 이내이면 공유기 설치 가능
                cnt += 1
                start = house[i]

        if cnt >= target:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


print(binary_search(1, house[-1] - house[0], C))