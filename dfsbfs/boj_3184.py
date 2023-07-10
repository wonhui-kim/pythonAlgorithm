import sys

R, C = map(int, sys.stdin.readline().split())

graph = []
for i in range(R):
    graph.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, count_o, count_v):
    stack = []
    if graph[x][y] == 'o':
        count_o += 1
    elif graph[x][y] == 'v':
        count_v += 1

    graph[x][y] = '#'
    stack.append([x, y])

    while stack:
        cur = stack.pop()
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue

            if not graph[nx][ny] == '#':
                if graph[nx][ny] == 'o':
                    count_o += 1
                elif graph[nx][ny] == 'v':
                    count_v += 1

                graph[nx][ny] = '#'
                stack.append([nx, ny])

    return count_o, count_v


sheep = 0
wolves = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'o' or graph[i][j] == 'v':
            s, w = dfs(i, j, 0, 0)
            if s > w:
                sheep += s
            else:
                wolves += w
print(sheep, wolves)