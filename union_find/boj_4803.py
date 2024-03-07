import sys


def find_root(node, parent):
    if node == parent[node]:
        return node

    parent[node] = find_root(parent[node], parent)
    return parent[node]


def union(node_a, node_b, parent):
    root_a = find_root(node_a, parent)
    root_b = find_root(node_b, parent)

    # 서로 루트가 같으면 사이클 발생
    if root_a == root_b:
        return True, root_a

    # 이미 사이클이 있는 루트에 연결되면 사이클 발생
    if ruined[root_a]:
        return True, root_b

    if ruined[root_b]:
        return True, root_a

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

    return False, 0  # 정상 종료


case = 1
while True:
    # 정점 개수 n, 간선 개수 m
    n, m = map(int, sys.stdin.readline().split())

    parent = list(range(n + 1))
    ruined = [False] * (n + 1)  # 연결되면 안되는 트리 - 사이클이 생겨버린 트리

    # 종료 조건
    if n == 0 and m == 0:
        break

    cycle = set()
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())

        is_cycle, value = union(a, b, parent)

        if is_cycle:
            cycle.add(value)
            ruined[value] = True

    # 루트 개수 세기
    roots = set()
    for i in range(1, n + 1):
        roots.add(find_root(i, parent))

    num_trees = len(roots - cycle)

    if num_trees == 0:
        print("Case " + str(case) + ": No trees.")
    elif num_trees == 1:
        print("Case " + str(case) + ": There is one tree.")
    else:
        print("Case " + str(case) + ": A forest of " + str(num_trees) + " trees.")

    case += 1