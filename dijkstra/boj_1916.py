import sys
import heapq

# 도시의 개수 - 정점
N = int(sys.stdin.readline())

# 버스의 개수 - 간선
M = int(sys.stdin.readline())

graph = [[] for i in range(N + 1)]
for i in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append([w, e])  # 비용, 도착지

# 구하고자 하는 시작 지점, 도착 지점
S, A = map(int, sys.stdin.readline().split())

INF = int(10e9)  # 10억
dist = [INF] * (N + 1)


def dijkstra(start):
    pq = []
    dist[start] = 0  # 시작노드-시작노드 비용 0

    for v in graph[start]:
        heapq.heappush(pq, [v[0], v[1]])  # 비용, 도착지 (비용 오름차순)

    while pq:
        cost, cur = heapq.heappop(pq)

        if dist[cur] != INF:  # 갱신된 적 있으면 넘어감
            continue

        dist[cur] = cost  # 아니면 최소 비용으로 갱신

        for v in graph[cur]:  # 현재 노드에 연결된 노드들 검사
            if dist[v[1]] == INF:  # 갱신된 적 없으면 pq 삽입
                heapq.heappush(pq, [cost + v[0], v[1]])  # 시작 노드 - 현재 노드까지 비용 + 현재 노드 - 연결된 노드 비용


dijkstra(S)
print(dist[A])
