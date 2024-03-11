import sys

n = int(sys.stdin.readline())

# 최대 나올 수 있는 전제 수 * 2
INF = int(10e9)
graph = [[INF for i in range(26 * 2)] for j in range(26 * 2)]
dic = dict()
idx = 0
for i in range(n):
    a, b = sys.stdin.readline().rstrip().split(" is ")

    if a not in dic:
        dic[a] = idx
        idx += 1

    if b not in dic:
        dic[b] = idx
        idx += 1

    graph[dic[a]][dic[b]] = 1


def floyd_warshall(graph, keys):
    for k in keys:
        for i in keys:
            for j in keys:
                if i == j:
                    graph[dic[i]][dic[j]] = 0
                graph[dic[i]][dic[j]] = min(graph[dic[i]][dic[j]], graph[dic[i]][dic[k]] + graph[dic[k]][dic[j]])


floyd_warshall(graph, dic.keys())

m = int(sys.stdin.readline())
for i in range(m):
    a, b = sys.stdin.readline().rstrip().split(" is ")

    if (a not in dic) or (b not in dic):
        print("F")
        continue

    if graph[dic[a]][dic[b]] >= INF:
        print("F")
    else:
        print("T")