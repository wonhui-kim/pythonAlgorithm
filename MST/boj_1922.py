import sys
import heapq
import copy

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

parent = list(range(N + 1))
pq = []
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())

    heapq.heappush(pq, [c, a, b])  # min heap


def find_root(node, parent):
    if node == parent[node]:
        return node

    parent[node] = find_root(parent[node], parent)
    return parent[node]


def union(node_a, node_b, parent):
    root_a = find_root(node_a, parent)
    root_b = find_root(node_b, parent)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


def kruskal(arr):
    result = 0
    pq = copy.deepcopy(arr)

    while pq:
        d, link_a, link_b = heapq.heappop(pq)

        # 연결되지 않았을 경우
        if find_root(link_a, parent) != find_root(link_b, parent):
            union(link_a, link_b, parent)
            result += d

    return result


print(kruskal(pq))