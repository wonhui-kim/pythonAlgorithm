import sys

N = int(sys.stdin.readline())

areas = []
for i in range(N):
    areas.append(list(map(int, sys.stdin.readline().split())))

# set에 영역 높이 모두 저장
height = set()
for i in range(N):
    for j in range(N):
        height.add(areas[i][j])


def dfs(x, y, graph):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    stack = []
    stack.append([x, y])

    while stack:
        cur_x, cur_y = stack.pop()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] == 0:
                stack.append([nx, ny])
                graph[nx][ny] = 1


max_cnt = -1
for h in height:  # 높이를 다 돌면서 최대 영역 개수 체크
    temp = [[0 for j in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N):
            if areas[i][j] <= h:  # 높이보다 작거나 같으면 침수
                temp[i][j] = 1  # 1은 방문 불가

    cnt = 0  # 물에 잠기는 지역 세기
    for i in range(N):
        for j in range(N):
            if temp[i][j] == 0:
                dfs(i, j, temp)
                cnt += 1

    max_cnt = max(max_cnt, cnt)

if len(height) == 1:  # 높이가 하나밖에 없는 경우 1임
    print(1)
else:
    print(max_cnt)


