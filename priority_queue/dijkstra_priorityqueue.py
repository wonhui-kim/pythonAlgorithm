import sys
import heapq

INF = int(1e9) #10억
vertex_number = int(sys.stdin.readline()) #정점 개수
edge_number = int(sys.stdin.readline()) #간선 개수

graph = [[] for i in range(vertex_number)] #각 노드에 연결된 노드와 weight 저장
for i in range(edge_number):
    f, t, w = map(int, sys.stdin.readline().split()) #시작 노드, 도착 노드, weight
    graph[f-1].append((t-1, w)) #f노드에 (연결된 노드, weight) 저장

print(graph)

#시작 노드
s = int(sys.stdin.readline())

#최단 거리를 담을 배열 - INF로 초기화
dist = [INF] * len(graph)
def dijkstra(start):
    pq = [] #우선순위 큐 생성
    # heapq.heappush(pq, (0, start)) #시작노드의 거리를 0으로 설정 후 큐에 넣음
    dist[start-1] = 0

    #시작 노드와 연결된 간선들의 가중치와 노드번호를 큐에 넣음
    for v in graph[start-1]:
        heapq.heappush(pq, (v[1], v[0])) #(1, 3-4), (5, 2-3), (2, 1-2)

    #큐가 빌 때까지 반복
    while pq:
        d, cur = heapq.heappop(pq) #거리와 현재 노드를 큐에서 꺼냄 ex. (1, 3-4)

        if dist[cur] != INF: #갱신된 적이 있으면 넘어감 ex. dist[3] != INF
            continue

        dist[cur] = d #거리를 최단거리 배열에 갱신해줌

        #연결된 노드 검사 v[0] = 노드 번호, v[1] = 가중치
        for v in graph[cur]:
            if dist[v[0]] == INF: #갱신된 적이 없는 노드이면
                # dist[v[0]-1] = d + v[1] #시작노드 -> cur 노드 + cur노드 -> 연결된 노드
                heapq.heappush(pq, (d + v[1], v[0])) #힙 (거리, 노드번호)

dijkstra(s)
print(dist)