import sys

N = int(sys.stdin.readline())
power = []
for i in range(N):
    power.append(list(map(int, sys.stdin.readline().split())))

visit = [False for i in range(N)]


def difference(visited):
    team_a = 0
    team_b = 0

    for i in range(N):
        for j in range(N):
            if visited[i] and visited[j]:
                team_a += power[i][j]
            elif not visited[i] and not visited[j]:
                team_b += power[i][j]

    return abs(team_a - team_b)


def dfs(depth, after):
    global min_diff

    if depth == N // 2:
        # 점수 차 계산
        diff = difference(visit)
        if min_diff > diff:
            min_diff = diff
        return

    for i in range(after, N):
        if not visit[i]:
            visit[i] = True
            dfs(depth + 1, i)
            visit[i] = False


min_diff = int(10e9)
dfs(0, 0)
print(min_diff)