import sys

# n = int(sys.stdin.readline())

INF = int(1e9) #10억
#그래프 연결 초기 상태
graph = [[0,2,5,1,INF,INF],
       [2,0,3,2,INF,INF],
       [5,3,0,3,1,5],
       [1,2,3,0,1,INF],
       [INF,INF,1,1,0,2],
       [INF,INF,5,INF,2,0]]

#시작 노드
s = int(sys.stdin.readline())
visited = [False] * len(graph)

#방문하지 않은 노드 중에서 가장 작은 값을 가지는 인덱스 반환
def get_smallest_index(arr):
    min_value = INF
    min_index = 0

    for i in range(len(arr)):
        if arr[i] < min_value and not visited[i]:
            min_value = arr[i]
            min_index = i

    return min_index

dist = []
def dijkstra(start):
    dist = graph[start-1]
    dist[start-1] = 0 #시작노드 초기화
    visited[start] = True #시작 노드 방문처리

    for i in range(len(dist)-1):
        cur = get_smallest_index(dist)
        visited[cur] = True

        for j in range(len(dist)):
            if dist[cur]+graph[cur][j] < dist[j]:
                dist[j] = dist[cur]+graph[cur][j]

    print(dist)

dijkstra(s)
# print(dist)