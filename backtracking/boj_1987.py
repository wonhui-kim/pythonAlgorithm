import sys

R, C = map(int, sys.stdin.readline().split())
board = []
for i in range(R):
    board.append(list(sys.stdin.readline().rstrip()))

result = -1
visit = set()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global result

    visit.add(board[x][y])
    result = max(result, len(visit))
    # print(visit)

    if x == R - 1 and y == C - 1:  # 마지막 노드이면 종료
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue

        if not board[nx][ny] in visit:
            dfs(nx, ny)
            visit.remove(board[nx][ny])


dfs(0, 0)
print(result)