import sys
import itertools

N, M = map(int, sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 치킨집 좌표 저장
chicken = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append([i, j])

# 치킨집 M개 구하기
selected_chicken = []
if len(chicken) > M:
    for i in itertools.combinations(chicken, M):
        selected_chicken.append(i)  # [([0, 1], [3, 0]), ([0, 1], [4, 0]), ([0, 1], [4, 1])
else:
    selected_chicken.append(chicken)  # [[1, 2], [2, 2], [4, 4]]


# 한 집으로부터의 치킨 거리 구하기
def shortest_dist(x, y, chick):
    dist = int(10e9)
    for c in chick:
        dist = min(dist, abs(c[0] - x) + abs(c[1] - y))

    return dist


min_dist = int(10e9)
for s in selected_chicken:  # 뽑은 M개 치킨집의 최소거리 구하기
    distance = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                distance += shortest_dist(i, j, s)
    min_dist = min(min_dist, distance)

print(min_dist)