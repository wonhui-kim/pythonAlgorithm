import sys
import copy

R, C, T = map(int, sys.stdin.readline().split())

graph = []
purifier = []  # 공청기 위치

for i in range(R):
    temp = list(map(int, sys.stdin.readline().split()))

    for j in range(len(temp)):
        if temp[j] == -1:
            purifier.append([i, j])  # 공청기 위치 고정 (위, 아래)

    graph.append(temp)


# 미세먼지 현위치 찾기
def find_dust(arr):
    dust = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] > 0:
                dust.append([i, j])

    return dust


# 미세먼지 확산
def spread(graph, dust):
    # 미세먼지는 원래 있던 양을 기준으로 함
    original = copy.deepcopy(graph)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for d in dust:
        x, y = d

        # 확산량
        amount = original[x][y] // 5
        cnt = 0  # 확산 장소 개수
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue

            if original[nx][ny] != -1:  # 공청기 위치가 아니면
                graph[nx][ny] += amount  # 확산된 양 추가
                cnt += 1  # 확산 장소 개수 추가

        graph[x][y] -= (amount * cnt)  # 현재 위치 미세먼지 감소


# 공청기 방향
def turn_purifier(purifier):
    top = []  # 위쪽 공청기
    bottom = []  # 아래쪽 공청기
    # 작동 반대방향으로(공기를 빨아들이는 순서대로)
    # 위쪽 공청기 북쪽으로 이동
    if purifier[0][0] > 0:  # 이미 맨 위일 경우 이동 안함
        for i in range(1, purifier[0][0] + 1):
            top.append([purifier[0][0] - i, 0])

    # 아래쪽 공청기 남쪽으로 이동
    if purifier[1][0] < R - 1:  # 이미 맨 아래일 경우 이동 안함
        for i in range(1, R - purifier[1][0]):
            bottom.append([purifier[1][0] + i, 0])

    # 동쪽으로 같이 이동
    for i in range(1, C):
        top.append([0, i])
        bottom.append([R - 1, i])

    # 위쪽 공청기 남쪽으로 이동
    for i in range(1, purifier[0][0] + 1):
        top.append([i, C - 1])

    # 아래쪽 공청기 북쪽으로 이동
    for i in range(1, R - purifier[1][0]):
        bottom.append([R - 1 - i, C - 1])

    # 서쪽으로 같이 이동
    for i in range(1, C - 1):
        top.append([purifier[0][0], C - 1 - i])
        bottom.append([purifier[1][0], C - 1 - i])

    return top, bottom


# 공청기 작동
def after_purify(top, bottom):
    # 공청기 바람 이동 순서대로 빨아들이기 ->top, bottom 개수 다를 수 있음
    for i in range(len(top) - 1):
        graph[top[i][0]][top[i][1]] = graph[top[i + 1][0]][top[i + 1][1]]

    for i in range(len(bottom) - 1):
        graph[bottom[i][0]][bottom[i][1]] = graph[bottom[i + 1][0]][bottom[i + 1][1]]

    # 마지막 노드 0으로 작업
    graph[top[-1][0]][top[-1][1]] = 0
    graph[bottom[-1][0]][bottom[-1][1]] = 0


# 최종 미세먼지 남은 수 계산
def left_dust(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] > 0:
                total += arr[i][j]

    return total


# 공청기 작동 방향 - 정해짐
top, bottom = turn_purifier(purifier)

for t in range(T):  # 몇 초간
    dust = find_dust(graph)
    spread(graph, dust)
    after_purify(top, bottom)

print(left_dust(graph))
