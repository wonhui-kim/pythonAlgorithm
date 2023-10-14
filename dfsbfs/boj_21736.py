import sys

N, M = map(int, sys.stdin.readline().split())

campus = []
for i in range(N):
    campus.append(list(sys.stdin.readline().rstrip()))


# 도연의 좌표 찾기
def find_start(arr):
    for i in range(N):
        for j in range(M):
            if campus[i][j] == "I":
                return [i, j]

    return [0, 0]


def dfs(x, y, arr, n, m):
    # 만나는 사람 수(P)
    answer = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    stack = []
    stack.append([x, y])
    arr[x][y] = "V"  # 방문 처리

    while stack:
        cur_x, cur_y = stack.pop()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if arr[nx][ny] == "O" or arr[nx][ny] == "P":
                if arr[nx][ny] == "P":
                    answer += 1
                stack.append([nx, ny])
                arr[nx][ny] = "V"  # 방문 처리

    return answer


# 시작 좌표 찾기
start_x, start_y = find_start(campus)
total_p = dfs(start_x, start_y, campus, N, M)

if total_p > 0:
    print(total_p)
else:
    print("TT")