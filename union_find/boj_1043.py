import sys

# 사람 수 N, 파티 수 M
N, M = map(int, sys.stdin.readline().split())

parent = list(range(N + 1))

# 진실 아는 사람 수와 번호
truth = list(map(int, sys.stdin.readline().split()))
if truth[0] > 0:  # 진실을 아는 사람들의 부모를 0으로 설정
    for t in truth[1:]:
        parent[t] = 0


def find_root(node, p):
    if node == p[node]:
        return node

    p[node] = find_root(p[node], p)
    return p[node]


def union_root(node_a, node_b, p):
    root_a = find_root(node_a, p)
    root_b = find_root(node_b, p)

    # 더 작은 루트쪽으로 붙기
    if root_a < root_b:
        p[root_b] = root_a
    else:
        p[root_a] = root_b


# 각 파티별 사람들
parties = []
for i in range(M):
    temp = list(map(int, sys.stdin.readline().split()))

    if temp[0] > 1:
        for i in range(1, temp[0]):
            union_root(temp[i], temp[i + 1], parent)

    parties.append(temp[1:])

count = 0
for p in parties:
    flag = True
    for i in range(len(p)):
        if find_root(p[i], parent) == 0:
            flag = False
            break

    if flag:
        count += 1

print(count)