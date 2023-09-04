import sys

N = int(sys.stdin.readline())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

INF = int(10e9)


def fine_graph(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                arr[i][j] = INF
    return arr


# floyd-warshall
def floyd_warshall(arr):
    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

    return arr


def print_graph(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] >= INF:
                arr[i][j] = 0
            else:
                arr[i][j] = 1
            print(arr[i][j], end=' ')
        print()


graph = fine_graph(graph)
graph = floyd_warshall(graph)
print_graph(graph)