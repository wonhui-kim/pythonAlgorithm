# 음식물 피하기 (boj_1743)
import sys

# N, M, K 세로길이, 가로길이, 음식물개수
N, M, K = map(int, sys.stdin.readline().split())

# 2차원 그래프 생성 0으로 초기화
graph = [[0 for i in range(M + 1)] for j in range(N + 1)]

# 음식물 좌표는 1로 표시
for i in range(K):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1

# 전체 그래프를 탐색하면서 음식물 크기 count - dfs 활용
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs_stack(x, y, cnt):  # 스택 버전
    stack = []
    graph[x][y] = 0  # 방문 처리
    stack.append([x, y])

    while stack:
        cur = stack.pop()
        cnt += 1

        for i in range(4):  # 사방 확인
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]

            # 벗어나는 범위 처리
            if nx < 1 or ny < 1 or nx > N or ny > M:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                stack.append([nx, ny])

    return cnt


max = -1
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if graph[i][j] == 1:
            count = dfs_stack(i, j, 0)
            if max < count:
                max = count
print(max)