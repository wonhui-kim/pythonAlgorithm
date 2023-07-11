import sys
from collections import deque
import copy

N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

def bfs(x, y, size):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    deq = deque()
    deq.append([0, x, y])  # 거리, 좌표
    copied = copy.deepcopy(graph)  # 현재 그래프 deepcopy
    copied[x][y] = size + 1  # 방문처리

    preys = []
    while deq:
        cur = deq.popleft()  # 큐 pop [거리, x좌표, y좌표]
        # preys.append(cur)

        for i in range(4):
            nx = cur[1] + dx[i]
            ny = cur[2] + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if copied[nx][ny] <= size:  # 현재 상어 크기보다 작으면
                if not copied[nx][ny] == 0 and not copied[nx][ny] == size:
                    preys.append([cur[0] + 1, nx, ny])  # 빈곳 0 이 아니면 먹이 후보에 넣기

                deq.append([cur[0] + 1, nx, ny])  # 큐에 넣기
                copied[nx][ny] = size + 1  # 방문처리

    if preys:
        preys.sort()
        return preys[0]
    else:
        return preys  # 결과값이 없으면 preys는 빈 배열


shark_pos = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_pos = [i, j]  # 상어 초기 위치 획득

shark_size = 2  # 상어 초기 크기는 2
eaten = 0
time_count = 0
while True:  # 중지 조건은 bfs의 결과가 빈 배열일 때까지임..
    if not bfs(shark_pos[0], shark_pos[1], shark_size):  # 빈 배열이면
        break

    # 최적의 먹이 위치
    time, x, y = bfs(shark_pos[0], shark_pos[1], shark_size)

    # 먹이 먹으러 이동하는 시간 누적
    time_count += time

    # 상어 위치 옮기기
    graph[shark_pos[0]][shark_pos[1]] = 0  # 원래 위치 0으로 빈 곳 만들어주기
    graph[x][y] = 9  # 상어 위치 먹이 먹은 위치로 옮기기
    shark_pos = [x, y]

    eaten += 1  # 먹은 개수 추가
    if eaten >= shark_size:
        shark_size += 1  # 상어 크기 증가
        eaten = 0  # 먹은 개수 초기화

print(time_count)