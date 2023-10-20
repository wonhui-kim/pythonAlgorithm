import sys
import copy
from collections import deque

# 역의 개수 <= 3000
N = int(sys.stdin.readline())

graph = [[] for i in range(N + 1)]  # 그래프 연결 상태
graph_cnt = [0 for i in range(N + 1)]  # 연결 노드 개수
parent = [0 for i in range(N + 1)]  # 0으로 초기화
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)
    graph_cnt[a] += 1
    graph_cnt[b] += 1

# 연결 노드 개수가 1개인 노드 찾기
copied_graph = copy.deepcopy(graph)
while (1 in graph_cnt):
    idx = graph_cnt.index(1)

    # 연결된 부모 노드
    parent_node = copied_graph[idx][0]
    parent[idx] = parent_node
    # 연결 끊기
    copied_graph[parent_node].remove(idx)
    graph_cnt[parent_node] -= 1
    graph_cnt[idx] = 0


# bfs를 이용하여 거리 파악
def bfs():
    answer = [-1 for i in range(N + 1)]
    deq = deque()

    for i in range(1, N + 1):
        if parent[i] == 0:  # 순환선이면(사이클 내)
            answer[i] = 0
            deq.append(i)

    while deq:
        cur = deq.popleft()

        for v in graph[cur]:
            if answer[v] == -1:
                answer[v] = answer[cur] + 1
                deq.append(v)

    return answer


def print_answer(arr):
    for i in range(1, len(arr)):
        print(arr[i], end=' ')


result = bfs()
print_answer(result)

