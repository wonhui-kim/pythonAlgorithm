import sys
import itertools
import copy

N, M = map(int, sys.stdin.readline().split())

graph = []
for i in range(N):  # Row
    graph.append(list(map(int, sys.stdin.readline().split())))


def check_sum(arr):
    total_sum = 0
    for i in arr:
        total_sum += graph[i[0]][i[1]]

    return total_sum


def coordinate(arr):
    temp = []
    for i in arr:
        r = i // M
        c = i % M
        temp.append([r, c])
    return temp


def dfs(x, y, copied):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    stack = []
    copied[x][y] = 2  # 바이러스 방문처리
    stack.append([x, y])

    while stack:
        cur = stack.pop()

        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if copied[nx][ny] == 0:  # 방문 가능한 빈 곳
                copied[nx][ny] = 2  # 방문 처리
                stack.append([nx, ny])


# 벽 세우고 바이러스 전파 완료된 후 그래프 반환
def completed(walls):
    cop = copy.deepcopy(graph)  # 그래프 복사본

    # 전달 받은 벽 세울 위치 3개
    for w in walls:
        cop[w[0]][w[1]] = 1  # 벽 세움

    # 그래프 돌면서 바이러스 전파 위치 2로 변경
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:  # 바이러스면
                # dfs로 전파
                dfs(i, j, cop)

    return cop


# 오염되지 않은 0 구역 count
def clean(arr):
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                count += 1
    return count


safe_area = -1
for i in itertools.combinations(range(N * M), 3):
    # 0인 위치에만 벽을 세울 수 있으므로 뽑은 세 개 합이 0인지 확인
    changed = coordinate(i)
    if not check_sum(changed) == 0:
        continue

    after_virus = completed(changed)
    if safe_area < clean(after_virus):
        safe_area = clean(after_virus)
print(safe_area)