import sys

N, M = map(int, sys.stdin.readline().split())
parent = list(range(N + 1))


def find_root(node):
    if node == parent[node]:
        return node

    # 목적이 루트 찾기이므로 트리 구조 바껴도 됨
    parent[node] = find_root(parent[node])
    return parent[node]


def union(node_a, node_b):
    root_a = find_root(node_a)
    root_b = find_root(node_b)

    # 작은 걸 루트로 설정함
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


for m in range(M):
    i, j = map(int, sys.stdin.readline().split())

    union(i, j)

schedule = list(map(int, sys.stdin.readline().split()))

# 첫 수업 건물
cur_building = find_root(schedule[0])
move = 0
for s in range(1, len(schedule)):
    next_building = find_root(schedule[s])
    if cur_building != next_building:
        move += 1
        cur_building = next_building

print(move)