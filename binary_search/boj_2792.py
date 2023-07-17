import sys

# 학생 수 N, 색상 수 M
N, M = map(int, sys.stdin.readline().split())

jewels = []
for i in range(M):
    jewels.append(int(sys.stdin.readline()))


# left는 0, right는 sum(jewels), mid는 질투심
def binary_search(left, right):
    answer = -1
    while left <= right:
        mid = (left + right) // 2

        # mid로 질투심을 설정하면 나눠줄 수 있는 학생의 수
        divided = 0
        for j in jewels:
            divided += (j // mid)
            if not j % mid == 0:
                divided += 1

        # 나눠줄 수 있는 학생 수가 주어진 학생 수(N)보다 많다면 mid가 더 커져야 함
        if divided > N:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    return answer


print(binary_search(1, sum(jewels)))