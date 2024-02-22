import sys
import copy
from collections import deque

R, C = map(int, sys.stdin.readline().split())
graph = []
for i in range(R):
    graph.append(list(sys.stdin.readline().rstrip()))


def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    longest = 0

    copied_graph = copy.deepcopy(graph)

    deq = deque()
    deq.append([x, y, 0])

    copied_graph[x][y] = "V"

    while deq:
        cur_x, cur_y, cur_time = deq.popleft()

        longest = max(longest, cur_time)  # 최대 시간 갱신

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue

            if copied_graph[nx][ny] == "L":
                copied_graph[nx][ny] = "V"  # 방문 처리
                deq.append([nx, ny, cur_time + 1])

    return longest


result = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == "L":
            result = max(result, bfs(i, j))

print(result)