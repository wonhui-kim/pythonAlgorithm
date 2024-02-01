import sys

# 도시 수
n = int(sys.stdin.readline())

# 버스 수
m = int(sys.stdin.readline())

INF = int(10e9)
graph = [[INF for i in range(n + 1)] for j in range(n + 1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())

    # 연결 노선이 하나가 아닐 수 있기에 적은 비용 저장
    graph[a][b] = min(graph[a][b], c)


def floyd_warshall(arr):
    for k in range(1, len(arr)):
        for i in range(1, len(arr)):
            for j in range(1, len(arr)):
                if i == j:
                    arr[i][j] = 0

                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


def print_result(arr):
    for i in range(1, len(arr)):
        for j in range(1, len(arr)):
            if arr[i][j] >= INF:
                arr[i][j] = 0

            print(arr[i][j], end=' ')
        print()


floyd_warshall(graph)
print_result(graph)