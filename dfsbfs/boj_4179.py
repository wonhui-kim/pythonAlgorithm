import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

graph = []
for i in range(R):
    graph.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

deq_f = deque()  # 초기 불난 곳 위치
deq_j = deque()  # 지훈이 초기 위치

visit_f = [[-1 for i in range(C)] for j in range(R)]
for i in range(R):
    for j in range(C):
        if graph[i][j] == "F":
            deq_f.append([i, j, 0])
            visit_f[i][j] = 0
        elif graph[i][j] == "J":
            deq_j.append([i, j, 0])
        elif graph[i][j] == "#":
            visit_f[i][j] = 0


def bfs_f():
    while deq_f:
        cur_x, cur_y, cur_depth = deq_f.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue

            if visit_f[nx][ny] == -1:
                visit_f[nx][ny] = cur_depth + 1
                deq_f.append([nx, ny, cur_depth + 1])


bfs_f()

def bfs_j():
    answer = 0
    while deq_j:
        cur_x, cur_y, cur_depth = deq_j.popleft()

        if cur_x == 0 or cur_y == 0 or cur_x == R - 1 or cur_y == C - 1:
            answer = cur_depth + 1
            break

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue

            if visit_f[nx][ny] > cur_depth + 1 or visit_f[nx][ny] == -1:
                visit_f[nx][ny] = 0  # 방문 처리
                deq_j.append([nx, ny, cur_depth + 1])

    return answer


result = bfs_j()

if result == 0:
    print("IMPOSSIBLE")
else:
    print(result)
