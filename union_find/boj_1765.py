import sys


def find_root(node, parent):
    if node == parent[node]:
        return node

    parent[node] = find_root(parent[node], parent)
    return parent[node]


def union(node_a, node_b, parent):
    root_a = find_root(node_a, parent)
    root_b = find_root(node_b, parent)

    # b의 부모로 통합
    parent[root_a] = root_b


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = list(range(n + 1))
enemy = [[] for i in range(n + 1)]
for i in range(m):
    r, a, b = sys.stdin.readline().strip().split()

    if r == "F":  # 친구인 경우
        union(int(a), int(b), parent)
    else:  # 적인 경우
        enemy[int(a)].append(int(b))
        enemy[int(b)].append(int(a))

for e in enemy:
    if len(e) >= 2:
        for i in range(len(e) - 1):
            union(e[i], e[i + 1], parent)

team = set()
for i in range(1, n + 1):
    team.add(find_root(i, parent))
print(len(team))