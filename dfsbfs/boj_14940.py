import sys
from collections import deque

# 세로 n, 가로 m
n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [[False for j in range(m)] for i in range(n)]


# 목표점 2 좌표 찾기
def find_start(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 2:
                return i, j

    return -1, -1


def bfs(x, y, depth):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    deq = deque()
    deq.append([x, y, depth])  # 시작점으로부터의 depth를 함께 저장
    graph[x][y] = 0  # 시작점 거리 0
    visited[x][y] = True  # 방문처리

    while deq:
        cur_x, cur_y, cur_depth = deq.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if (graph[nx][ny] == 1) and (not visited[nx][ny]):
                deq.append([nx, ny, cur_depth + 1])
                graph[nx][ny] = cur_depth + 1
                visited[nx][ny] = True


def print_graph(arr, visit):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if (arr[i][j] > 0) and (not visit[i][j]):
                print(-1, end=' ')
            else:
                print(arr[i][j], end=' ')
        print()


# 시작점(목표점) 좌표
x, y = find_start(graph)
bfs(x, y, 0)
print_graph(graph, visited)