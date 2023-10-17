import sys


def find_root(node, p):
    if p[node] == node:
        return node

    p[node] = find_root(p[node], p)
    return p[node]


def union(node_a, node_b, p):
    root_a = find_root(node_a, p)
    root_b = find_root(node_b, p)

    p[root_b] = root_a


tc = int(sys.stdin.readline())
for i in range(tc):
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())

    parent = list(range(n + 1))
    for j in range(k):
        a, b = map(int, sys.stdin.readline().split())
        union(a, b, parent)

    print("Scenario " + str(i + 1) + ": ")
    m = int(sys.stdin.readline())
    for j in range(m):
        u, v = map(int, sys.stdin.readline().split())

        root_u = find_root(u, parent)
        root_v = find_root(v, parent)

        if root_u == root_v:
            print(1)
        else:
            print(0)

    print()