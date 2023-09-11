import sys

N = int(sys.stdin.readline())

graph = [[] for i in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

# 부모 저장용 - 초기는 본인으로 설정
parent = list(range(N + 1))
visited = [False] * (N + 1)


def dfs(start):
    stack = []
    visited[start] = True

    for v in graph[start]:
        stack.append(v)
        parent[v] = start
        visited[v] = True

    # dfs로 탐색해나가면서 부모를 본인으로 설정
    while stack:
        cur = stack.pop()

        for v in graph[cur]:
            if not visited[v]:
                stack.append(v)
                parent[v] = cur
                visited[v] = True


dfs(1)
for i in range(2, len(parent)):  # 1 제외 출력
    print(parent[i])