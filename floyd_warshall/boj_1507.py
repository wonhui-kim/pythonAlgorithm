import sys

N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


def floyd_warshall(arr):
    linked = [[[] for i in range(len(arr[0]))] for j in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            linked[i][j].append([i, j])

    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if k == i or k == j or i == j:
                    continue
                if arr[i][j] > (arr[i][k] + arr[k][j]):
                    return -1, linked  # 이상한 경우
                if arr[i][j] == (arr[i][k] + arr[k][j]):
                    linked[i][j] = linked[i][k] + linked[k][j]

    return 1, linked


def time(arr, linked):
    total = 0
    include = set()

    for i in range(len(linked)):
        for j in range(i, len(linked)):
            for (x, y) in linked[i][j]:
                if (x != y) and ((x, y) not in include):
                    total += arr[x][y]
                    include.add((x, y))
                    include.add((y, x))
    return total


result, link = floyd_warshall(graph)

if result == -1:
    print(-1)
else:
    print(time(graph, link))