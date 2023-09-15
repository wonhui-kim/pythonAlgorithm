import sys

#물건 개수 N, 측정 수 M
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[0 for j in range(N+1)] for i in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1 #a가 큼
    graph[b][a] = -1

def floyd_warshall(arr, cnt):
    for k in range(1, cnt+1):
        for i in range(1, cnt+1):
            for j in range(1, cnt+1):
                if arr[i][j] == 0: #갱신된 적 없으면
                    if arr[i][k] == arr[k][j]: #부호 같으면 갱신
                        arr[i][j] = arr[i][k]

floyd_warshall(graph, N)

for i in range(1, N+1):
    print(graph[i].count(0)-2) #본인, 0 (2개) 제외
