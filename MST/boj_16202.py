import sys
import heapq
import copy

N, M, K = map(int, sys.stdin.readline().split())
weight = 1
pq = []
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())

    heapq.heappush(pq, [weight, a, b])
    weight += 1


def find_root(node, parent):
    if node == parent[node]:
        return node

    parent[node] = find_root(parent[node], parent)
    return parent[node]


def union(a, b, parent):
    root_a = find_root(a, parent)
    root_b = find_root(b, parent)

    if root_a == root_b:
        return False

    parent[root_a] = root_b
    return True


def is_mst(pq, n):
    cost = 0
    copied_pq = copy.deepcopy(pq)

    parent = list(range(n + 1))

    while copied_pq:
        w, a, b = heapq.heappop(copied_pq)

        if union(a, b, parent):
            cost += w

    # mst인지 검사
    mst = True
    for i in range(1, n):
        if find_root(i, parent) != find_root(i + 1, parent):
            mst = False

    return mst, cost


mst = True
cost = 0
for i in range(K):
    if mst:
        mst, cost = is_mst(pq, N)
        heapq.heappop(pq)

    if not mst:
        cost = 0

    print(cost, end=' ')