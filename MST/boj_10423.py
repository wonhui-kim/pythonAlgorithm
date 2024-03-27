import sys
import heapq

N, M, K = map(int, sys.stdin.readline().split())
station = set(list(map(int, sys.stdin.readline().split())))

parent = list(range(N + 1))
pq = []
for i in range(M):
    u, v, w = map(int, sys.stdin.readline().split())

    heapq.heappush(pq, [w, u, v])


def find_root(node, parent):
    if node == parent[node]:
        return node

    parent[node] = find_root(parent[node], parent)
    return parent[node]


def union(node_a, node_b, parent):
    root_a = find_root(node_a, parent)
    root_b = find_root(node_b, parent)

    # 각각 모두 발전소에 연결되어 있다면 서로 연결 안함
    if (root_a in station) and (root_b in station):
        return False

    # 이미 서로 연결된 노드라면 연결 안함
    if root_a == root_b:
        return False

    # 발전소가 루트가 되도록
    if root_a in station:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

    return True


def calculate_cost(pq):
    cost = 0

    while pq:
        c, a, b = heapq.heappop(pq)

        if union(a, b, parent):
            cost += c

    return cost


print(calculate_cost(pq))