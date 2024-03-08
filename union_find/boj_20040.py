import sys

n, m = map(int, sys.stdin.readline().split())
parent = list(range(n))  # 0~n-1까지 노드


def find_root(node, parent):
    if node == parent[node]:
        return node

    parent[node] = find_root(parent[node], parent)
    return parent[node]


def union(node_a, node_b, parent):
    root_a = find_root(node_a, parent)
    root_b = find_root(node_b, parent)

    # 이미 루트가 같으면 사이클 발생
    if root_a == root_b:
        return True  # 사이클 발생 시 True 반환

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
    return False  # 정상 union 종료 시 False 반환


pause = 0
for i in range(m):
    # 현재 차례는 i+1
    a, b = map(int, sys.stdin.readline().split())

    isCycle = union(a, b, parent)

    if isCycle and (pause == 0):
        pause = i + 1

print(pause)