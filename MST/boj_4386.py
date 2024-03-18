import sys
import math
import heapq


# print(math.sqrt(1.0**2 + 1.0**2))
# print(math.sqrt(2.0**2))
# print(math.sqrt(1.0**2 + 3.0**2))

def find_root(node, parent):
    if node == parent[node]:
        return node

    parent[node] = find_root(parent[node], parent)
    return parent[node]


def union(node_a, node_b, parent):
    root_a = find_root(node_a, parent)
    root_b = find_root(node_b, parent)

    # 이미 루트 노드가 같으면 union 안하고 그냥 반환
    if root_a == root_b:
        return False

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
    return True


n = int(sys.stdin.readline())
parent = list(range(n))

coordinate = []
pq = []
for i in range(n):
    a, b = map(float, sys.stdin.readline().split())

    coordinate.append([a, b])

    # 앞의 좌표들과의 거리 저장
    if i > 0:
        for j in range(i - 1, -1, -1):
            d = math.sqrt((a - coordinate[j][0]) ** 2 + (b - coordinate[j][1]) ** 2)
            heapq.heappush(pq, [d, j, i])  # 인덱스 저장


def kruskal(pq, parent):
    cost = 0

    while pq:
        dist, a, b = heapq.heappop(pq)

        if union(a, b, parent):  # union 성공 시
            cost += dist

    return '{:.2f}'.format(cost)


print(kruskal(pq, parent))