import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = int(10e9)

graph = [[INF for j in range(n)] for i in range(n)]

# 최소 경로 저장용 배열
way = [[[] for j in range(n)] for i in range(n)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())

    if graph[a - 1][b - 1] > c:
        graph[a - 1][b - 1] = c

        way[a - 1][b - 1].append([a, b])


def print_graph(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] >= INF:
                print(0, end=' ')
            else:
                print(arr[i][j], end=' ')
        print()


# floyd_warshall
def floyd_warshall(arr):
    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j:
                    arr[i][j] = 0
                    continue

                # arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
                if arr[i][k] + arr[k][j] < arr[i][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]  # 짧은 경로로 갱신

                    # print("way[i][k]: ", way[i][k][0])
                    # print("way[k][j]: ", way[k][j][0][1:])
                    way[i][j] = list(map(list.__add__, way[i][k], [way[k][j][0][1:]]))


floyd_warshall(graph)
print_graph(graph)

for i in range(len(way)):
    for j in range(len(way[0])):
        if not way[i][j]:
            print(0)
        else:
            print(len(way[i][j][0]), end=' ')
            for k in range(len(way[i][j][0])):
                print(way[i][j][0][k], end=' ')
            print()