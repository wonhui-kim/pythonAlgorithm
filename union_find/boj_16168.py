import sys

# 오일러 경로 가능한지 구하는 문제
# 조건: 모든 정점이 연결되어 있는지, 각 차수가 홀수인 것이 2개이거나 없어야 함
# 지점 개수 V, 연결 구간 개수 E
V, E = map(int, sys.stdin.readline().split())


def find_root(node, p):
    if node == p[node]:
        return node

    p[node] = find_root(p[node], p)
    return p[node]


def union(node_a, node_b, p):
    root_a = find_root(node_a, p)
    root_b = find_root(node_b, p)

    p[root_b] = root_a


parent = list(range(V + 1))
degree = [0 for i in range(V + 1)]
for i in range(E):
    a, b = map(int, sys.stdin.readline().split())

    # 노드 연결
    union(a, b, parent)

    # 차수
    degree[a] += 1
    degree[b] += 1


# 모든 노드가 연결되어 있는지 확인
def find_linked(n, parent):
    for i in range(1, n):
        if find_root(i, parent) != find_root(i + 1, parent):
            return False

    return True


# 차수 조건 충족 확인 (홀수가 2개이거나 없어야 함)
def check_degree(arr):
    cnt_odd = 0

    for a in arr:
        if a % 2 == 1:
            cnt_odd += 1

    if cnt_odd == 2 or cnt_odd == 0:
        return True
    else:
        return False


v = [False for i in range(V)]
first_condition = find_linked(V, parent)
second_condition = check_degree(degree)

if first_condition and second_condition:
    print("YES")
else:
    print("NO")