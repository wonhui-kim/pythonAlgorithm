import sys
import copy
from collections import deque

R, C = map(int, sys.stdin.readline().split())
graph = []
for i in range(R):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 1년 후 빙하 상태
def melt(arr):
    after_melt = copy.deepcopy(arr)

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            cnt_zero = 0
            if arr[i][j] > 0:  # 빙하 있는 곳이면
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx < 0 or ny < 0 or nx >= len(arr) or ny >= len(arr[0]):
                        continue

                    if arr[nx][ny] == 0:
                        cnt_zero += 1

            after_melt[i][j] -= cnt_zero
            if after_melt[i][j] < 0:
                after_melt[i][j] = 0  # 음수 보강작업

    return after_melt


def dfs(x, y, arr):
    deq = deque()
    deq.append([x, y])
    arr[x][y] = 0

    while deq:
        cur_x, cur_y = deq.pop()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= len(arr) or ny >= len(arr[0]):
                continue

            if arr[nx][ny] > 0:
                deq.append([nx, ny])
                arr[nx][ny] = 0  # 방문 처리


# 빙하 덩어리 개수 세기
def chunk(arr):
    copied = copy.deepcopy(arr)

    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if copied[i][j] > 0:
                dfs(i, j, copied)
                cnt += 1

    return cnt


year = 0
while True:
    if chunk(graph) == 0:
        print(0)
        break

    if chunk(graph) >= 2:
        print(year)
        break

    graph = melt(graph)
    year += 1