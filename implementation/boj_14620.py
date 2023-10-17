import sys
import itertools
import copy

N = int(sys.stdin.readline())
garden = []

for i in range(N):
    garden.append(list(map(int, sys.stdin.readline().split())))


# 꽃 씨 좌표에 따른 비용
def total_fee(arr, seeds):
    total = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for seed in seeds:
        s_x, s_y = seed
        total += arr[s_x][s_y]
        arr[s_x][s_y] = -1  # 방문 처리

        for i in range(4):
            nx = s_x + dx[i]
            ny = s_y + dy[i]

            if arr[nx][ny] < 0:  # 이미 방문한 곳이면
                return -1

            total += arr[nx][ny]
            arr[nx][ny] = -1  # 방문 처리

    return total


result = int(10e9)

# 씨가 위치할 수 있는 곳은 1~(N-2)
# 위치할 수 있는 곳 중 3개를 고른다
for x in itertools.combinations([(i, j) for i in range(1, N - 1) for j in range(1, N - 1)], 3):
    copied_garden = copy.deepcopy(garden)
    fee = total_fee(copied_garden, x)
    if fee < 0:
        continue
    result = min(result, fee)

print(result)