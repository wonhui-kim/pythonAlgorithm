import sys
import heapq

INF = int(1e9)  # 10억으로 설정

# 정점 개수, 간선 개수
V, E = map(int, sys.stdin.readline().split())
# 시작 정점 번호
K = int(sys.stdin.readline())

graph = [[] for i in range(V + 1)]  # 0은 비워두고 1부터 시작
for i in range(E):
    # 출발, 도착, 가중치
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([w, v])  # 가중치, 연결노드 삽입

dist = [INF] * (V + 1)  # 시작점으로부터 각 노드까지의 최단 거리


def dijkstra(start):
    # 우선순위큐 생성
    pq = []
    dist[start] = 0  # 시작노드-시작노드 최단거리 0

    # 시작 노드와 연결된 노드의 가중치, 노드번호를 pq에 넣음
    for v in graph[start]:
        heapq.heappush(pq, [v[0], v[1]])  # [2,2], [3,3]

    # 큐가 빌 때까지 반복
    while pq:
        d, cur = heapq.heappop(pq)

        if dist[cur] != INF:  # 갱신된 적이 있으면 넘어감
            continue

        dist[cur] = d  # INF이면 거리를 갱신해줌

        for v in graph[cur]:  # 현재 노드에 연결된 노드 검사
            if dist[v[1]] == INF:  # 갱신된 적 없는 노드이면
                heapq.heappush(pq, [d + v[0], v[1]])  # 시작 노드 - 현재노드 거리 + 현재 노드 - 연결 노드 거리


dijkstra(K)
for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])