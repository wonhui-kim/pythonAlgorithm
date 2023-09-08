import sys

# 도시 수 N <=200
N = int(sys.stdin.readline())

# 여행 계획 M <= 1000
M = int(sys.stdin.readline())

cities = []
for i in range(N):
    cities.append(list(map(int, sys.stdin.readline().split())))

plan = list(map(int, sys.stdin.readline().split()))


# 해당 노드의 루트 노드 찾기
def find_root(node, p):
    # 본인이 본인 부모 노드이면 루트 노드임
    if node == p[node]:
        return node

    p[node] = find_root(p[node], p)
    return p[node]


def union_root(node_a, node_b, p):
    # 각 노드의 루트 노드 찾기
    root_a = find_root(node_a, p)
    root_b = find_root(node_b, p)

    # b의 루트 노드를 a로 변경해버려서 합침
    p[root_b] = root_a


# 도시들을 탐색하면서 연결되어 있으면 루트를 통일해줌 - union
parent = list(range(N))  # 각 노드의 부모를 본인으로 초기 세팅
for i in range(N):
    for j in range(i, N):  # 양방향 연결이므로 한쪽만 탐색해도 됨
        if cities[i][j] == 1:
            union_root(i, j, parent)

# 여행 계획의 모든 루트가 같으면 가능, 다르면 불가
possible = True
root = find_root(plan[0] - 1, parent)
for p in plan:
    if find_root(p - 1, parent) != root:
        possible = False
        break

if possible:
    print("YES")
else:
    print("NO")