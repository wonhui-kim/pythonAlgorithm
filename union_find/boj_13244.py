import sys


def find_root(node, parent):
    if node == parent[node]:
        return node

    parent[node] = find_root(parent[node], parent)
    return parent[node]


def union(node_a, node_b, parent):
    root_a = find_root(node_a, parent)
    root_b = find_root(node_b, parent)

    if root_a == root_b:
        return True

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

    return False


def all_linked(nodes, parent):
    for i in range(1, nodes):
        if find_root(i, parent) != find_root(i + 1, parent):
            return "graph"

    return "tree"


T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())

    parent = list(range(N + 1))

    isTree = True

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())

        isCycle = union(a, b, parent)

        if isTree and isCycle:
            isTree = False

    if not isTree:
        print("graph")
        continue

    print(all_linked(N, parent))