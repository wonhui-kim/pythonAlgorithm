import sys

n = int(sys.stdin.readline())

INF = int(10e9)
graph = [[INF for i in range(n)] for j in range(n)]

while True:
    a, b = map(int, sys.stdin.readline().split())

    if a == -1 and b == -1:
        break

    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1


def floyd_warshall(arr):
    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j:
                    arr[i][j] = 0
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


floyd_warshall(graph)

# 1이면 친구, 2이면 친구-친구, 3이면 친구-친구-친구
score = []
for g in graph:
    score.append(max(g))

candidate = []
min_score = min(score)
for i in range(len(score)):
    if score[i] == min_score:
        candidate.append(i + 1)

print(min_score, len(candidate))
for c in candidate:
    print(c, end=' ')