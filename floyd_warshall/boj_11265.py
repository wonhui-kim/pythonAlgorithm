import sys

N, M = map(int, sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


# floyd-warshall
def floyd_warshall(arr):
    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
    return arr


graph = floyd_warshall(graph)

for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())

    if graph[A - 1][B - 1] > C:
        print("Stay here")
    else:
        print("Enjoy other party")