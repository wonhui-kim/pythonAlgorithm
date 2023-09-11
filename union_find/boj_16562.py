import sys

# 친구 수, 관계 수, 돈
N, M, k = map(int, sys.stdin.readline().split())

# 친구비
pay = list(map(int, sys.stdin.readline().split()))

# 초기 부모는 본인으로 세팅
parent = list(range(N))


def find_root(node, p):
    # 본인이 부모이면 루트이므로 리턴
    if node == p[node]:
        return node

    p[node] = find_root(p[node], p)
    return p[node]


def union(node_a, node_b, p):
    # 각 노드의 부모 찾기
    root_a = find_root(node_a, p)
    root_b = find_root(node_b, p)

    # 친구비 작은 노드를 루트로 설정
    if pay[root_a] < pay[root_b]:
        p[root_b] = root_a
    else:
        p[root_a] = root_b


for i in range(M):
    v, w = map(int, sys.stdin.readline().split())

    # 친구 연결
    union(v - 1, w - 1, parent)

total_root = set()
for i in range(N):
    total_root.add(find_root(i, parent))

total = 0
for t in total_root:
    total += pay[t]

if total <= k:
    print(total)
else:
    print("Oh no")