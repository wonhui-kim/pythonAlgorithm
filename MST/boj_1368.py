import sys
import heapq

N = int(sys.stdin.readline())
parent = list(range(N + 1))

pq = []
for i in range(N):
    w = int(sys.stdin.readline())
    heapq.heappush(pq, [w, 0, i + 1])

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))

    for j in range(len(temp)):
        if i != j:
            heapq.heappush(pq, [temp[j], i + 1, j + 1])


def find_root(node, parent):
    if node == parent[node]:
        return node

    parent[node] = find_root(parent[node], parent)
    return parent[node]


def union(node_a, node_b, parent):
    root_a = find_root(node_a, parent)
    root_b = find_root(node_b, parent)

    if root_a == root_b:
        return False

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

    return True


def kruskal(pq):
    result = 0

    while pq:
        w, a, b = heapq.heappop(pq)

        if union(a, b, parent):
            result += w

    return result


print(kruskal(pq))