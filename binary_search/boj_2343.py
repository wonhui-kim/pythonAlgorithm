import sys

N, M = map(int, sys.stdin.readline().split())
lectures = list(map(int, sys.stdin.readline().split()))


# left는 0, right는 강의들의 총 길이 합
def binary_search(left, right):
    answer = -1
    while left <= right:
        mid = (left + right) // 2

        l_count = 0
        l_sum = 0
        for i in range(len(lectures)):
            l_sum += lectures[i]

            if l_sum > mid:
                l_count += 1
                l_sum = lectures[i]

        if l_sum > 0:
            l_count += 1

        # left, right 조정
        # bluray 개수가 원하는 개수보다 적다면
        # left를 mid+1로 변경
        if l_count <= M:
            answer = mid
            right = mid - 1
        else:  # len(blurays) < M
            left = mid + 1

    return answer


print(binary_search(max(lectures), sum(lectures)))