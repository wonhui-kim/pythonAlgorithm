import sys

N, K = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


def floyd_warshall(arr):
    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

    return arr


shortest_path = floyd_warshall(graph)

visited = [False for i in range(N)]


def backtracking(cur, cnt, dist):
    global result
    if cnt == N:
        result = min(result, dist)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            backtracking(i, cnt + 1, dist + shortest_path[cur][i])
            visited[i] = False


result = int(10e9)
visited[K] = True
backtracking(K, 1, 0)
print(result)