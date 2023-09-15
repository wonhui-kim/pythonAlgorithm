import sys

# 뉴런(정점) 개수 N, 시냅스(간선) 개수 M
N, M = map(int, sys.stdin.readline().split())

parent = list(range(N + 1))


def find_root(node, p):
    # 본인이 즉 부모이면 루트
    if node == p[node]:
        return node

    p[node] = find_root(p[node], p)
    return p[node]


def union(node_a, node_b, p):
    root_a = find_root(node_a, p)
    root_b = find_root(node_b, p)

    # union 하려고 하는데, 루트가 같으면 사이클이므로 연산 횟수 추가
    if root_a == root_b:
        return 1

    # 둘 중 작은 수를 루트로 설정
    if root_a < root_b:
        p[root_b] = root_a
    else:
        p[root_a] = root_b

    return 0


# 연산 횟수
count = 0
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    count += union(u, v, parent)  # 사이클이 형성되므로 끊는 연산

# 루트가 하나가 아니면 연결 연산 추가
s = set()
for i in range(1, N + 1):
    s.add(find_root(i, parent))

count += (len(s) - 1)
print(count)