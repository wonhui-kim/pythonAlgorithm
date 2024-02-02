import sys

T = int(sys.stdin.readline())

for t in range(T):
    # 방 개수 N, 통로 개수 M
    N, M = map(int, sys.stdin.readline().split())

    INF = int(10e9)
    graph = [[INF for i in range(N + 1)] for j in range(N + 1)]

    # 통로 정보 - 통로는 하나뿐
    for i in range(M):
        a, b, c = map(int, sys.stdin.readline().split())

        graph[a][b] = c
        graph[b][a] = c

    # 친구 수 K
    K = int(sys.stdin.readline())

    # 친구 있는 방 번호
    friends = list(map(int, sys.stdin.readline().split()))


    def floyd_warshall(arr):
        for k in range(1, len(arr)):
            for i in range(1, len(arr)):
                for j in range(1, len(arr)):
                    if i == j:
                        arr[i][j] = 0

                    arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


    def find_place(arr, friends):
        dist = INF
        result = 1

        for i in range(1, len(arr)):
            temp_dist = 0
            for f in friends:
                temp_dist += arr[f][i]

            if dist > temp_dist:
                result = i
                dist = temp_dist

        return result


    floyd_warshall(graph)
    print(find_place(graph, friends))