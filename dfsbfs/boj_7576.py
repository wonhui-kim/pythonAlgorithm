# boj_7576 토마토 bfs

import sys
from collections import deque

# 가로, 세로
M, N = map(int, sys.stdin.readline().split())
graph = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

# bfs
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

deq = deque()

for i in range(N):  # 세로
    for j in range(M):  # 가로
        if graph[i][j] == 1:
            deq.append([i, j])  # 1인 좌표들을 모두 queue에 삽입


def bfs():
    while deq:  # 큐가 빌 때까지 반복
        cur = deq.popleft()

        for i in range(4):  # 사방 체크
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]

            # 범위 넘어가는지 체크
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 다음 좌표가 0이면 큐에 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[cur[0]][cur[1]] + 1
                deq.append([nx, ny])


bfs()

max = 0
for i in range(N):
    if max == -1:
        break
    for j in range(M):
        if graph[i][j] == 0:
            max = -1
            break
        if graph[i][j] > max:
            max = graph[i][j]

if max == -1:
    print(max)
else:
    print(max - 1)
