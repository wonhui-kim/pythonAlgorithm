import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = int(10e9)
graph = [[INF for j in range(n)] for i in range(n)]

# 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())

    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)


# floyd-warshall
def floyd_warshall(arr):
    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j:
                    graph[i][j] = 0
                else:
                    arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
    return arr


def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            # 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
            if arr[i][j] == INF:
                print(0, end=' ')
            else:
                print(arr[i][j], end=' ')
        print()


graph = floyd_warshall(graph)
print_arr(graph)