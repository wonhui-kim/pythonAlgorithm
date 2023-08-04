import sys
import copy

N, L, R = map(int, sys.stdin.readline().split())

area = []
for i in range(N):
    area.append(list(map(int, sys.stdin.readline().split())))

visited = [[False for j in range(N)] for i in range(N)]


def dfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    stack = []
    visited_list = []  # 방문 좌표들 모아서 인구수 변경해줘야 함

    opened = 1  # 국경 열린 국가 개수
    population = area[x][y]  # 인구
    stack.append([x, y])
    visited_list.append([x, y])
    visited[x][y] = True  # 방문처리

    while stack:
        cur_x, cur_y = stack.pop()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            # 거리가 L 이상 R이하여야 함
            dist = abs(area[cur_x][cur_y] - area[nx][ny])

            if (not visited[nx][ny]) and dist >= L and dist <= R:
                opened += 1  # 국경 수 누적
                population += area[nx][ny]  # 인구 수 누적
                stack.append([nx, ny])
                visited_list.append([nx, ny])
                visited[nx][ny] = True  # 방문 처리

    average_population = population // opened
    for l in visited_list:
        area[l[0]][l[1]] = average_population

    return average_population


pop = -1  # 변경된 인구수
day_cnt = 0  # 인구 이동이 발생하는 일수
while True:
    before = copy.deepcopy(area)  # deepcopy

    visited = [[False for j in range(N)] for i in range(N)]  # 방문처리 - 매번 초기화

    for i in range(N):
        for j in range(N):
            if (not visited[i][j]) and (area[i][j] != pop):  # 바뀐 인구는 탐색 필요 없음
                pop = dfs(i, j)  # 변경된 인구 수 바꿔옴

    after = copy.deepcopy(area)  # dfs 이후 area 배열

    if before == after:  # 인구이동이 발생하지 않았다면 종료
        break

    day_cnt += 1

print(day_cnt)