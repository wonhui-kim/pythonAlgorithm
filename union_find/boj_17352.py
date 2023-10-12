import sys

def find_root(node, p):
    if node == p[node]:
        return node

    p[node] = find_root(p[node], p)
    return p[node]

def union(node_a, node_b, p):
    root_a = find_root(node_a, p)
    root_b = find_root(node_b, p)

    if root_a <= root_b:
        p[root_b] = root_a
    else:
        p[root_a] = root_b

N = int(sys.stdin.readline())
parent = list(range(N + 1))

for i in range(N - 2):
    a, b = map(int, sys.stdin.readline().split())

    # 연결하기
    union(a, b, parent)

root_set = set()
answer = []

for i in range(1, len(parent)):
    if not find_root(i, parent) in root_set:
        root_set.add(i)

root_list = list(root_set)
for i in range(len(root_list) - 1):
    answer.append([root_list[i], root_list[i + 1]])

def print_answer(arr):
    for a in arr:
        print(a[0], a[1])

print_answer(answer)