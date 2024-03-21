import sys
import heapq

N, M, t = map(int, sys.stdin.readline().split())

parent = list(range(N + 1))

pq = []
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())

    heapq.heappush(pq, [c, a, b])
    heapq.heappush(pq, [c, b, a])


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


def cost(pq, parent, t):
    cur_t = t
    min_cost = 0
    cnt = 0

    while pq:
        c, a, b = heapq.heappop(pq)

        result = union(a, b, parent)

        if result:  # union 성공하면
            if cnt >= 1:
                min_cost += cur_t
                cur_t += t
            cnt += 1
            min_cost += c

    return min_cost


print(cost(pq, parent, t))