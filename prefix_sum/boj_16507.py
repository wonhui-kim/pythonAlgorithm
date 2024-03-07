import sys

R, C, Q = map(int, sys.stdin.readline().split())

graph = []
for r in range(R):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 구간합 그래프 만들기
prefix_sum = []
for i in range(R):
    temp = 0
    temp_line = [0]
    for j in range(C):
        temp += graph[i][j]
        temp_line.append(temp)
    prefix_sum.append(temp_line)

for i in range(Q):  # <= 10,000
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

    temp_sum = 0
    for j in range(c2 - c1):
        temp_sum += (prefix_sum[r1 - 1 - j][c2] - prefix_sum[r1 - 1 + j][c1 - 1])

    # 범위 안의 개수 (분모)
    denominator = (r2 - r1 + 1) * (c2 - c1 + 1)

    print(temp_sum // denominator)