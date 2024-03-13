import sys
import heapq

N = int(sys.stdin.readline())
parent = list(range(N))


def find_root(node, parent):
    if node == parent[node]:
        return node

    parent[node] = find_root(parent[node], parent)
    return parent[node]


def union(node_a, node_b, parent):
    root_a = find_root(node_a, parent)
    root_b = find_root(node_b, parent)

    if root_a == root_b:  # 이미 연결된 노드이면 union 안하고 False 반환
        return False

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

    return True


def donate_length(pq, lan):
    donate = lan

    while pq:
        length, a, b = heapq.heappop(pq)

        # 최소 스패닝 트리에 필요한 노드라면
        if union(a, b, parent):
            donate -= length

    return donate


# 모두 연결되었는지 검사
def all_linked(N):
    for i in range(N - 1):
        if find_root(i, parent) != find_root(i + 1, parent):
            return False

    return True


lan = 0
pq = []
for i in range(N):
    temp = list(sys.stdin.readline().rstrip())

    for j in range(len(temp)):
        to_int = -1
        if temp[j] in "abcdefghijklmnopqrstuvwxyz":
            to_int = (ord(temp[j]) - 96)
        elif temp[j] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            to_int = (ord(temp[j]) - 38)
        else:
            continue

        lan += to_int  # 전체 랜선 저장

        heapq.heappush(pq, [to_int, i, j])

result = donate_length(pq, lan)
if all_linked(N):
    print(result)
else:
    print(-1)