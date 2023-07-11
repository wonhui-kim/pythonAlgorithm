import sys
import itertools

graph = []
for i in range(5):
    graph.append(list(sys.stdin.readline().rstrip()))


# S의 개수 세기
def check_number(arr):
    count = 0
    for i in arr:
        if graph[i[0]][i[1]] == 'S':
            count += 1
    return count


# 0~24를 좌표로 변경
def coordinate(arr):
    temp = []
    for i in arr:
        r = i // 5
        c = i % 5
        temp.append([r, c])
    return temp


# 2차원 배열의 합 구하기
def arr_sum(arr):
    total_sum = 0
    for row in arr:
        for element in row:
            total_sum += element
    return total_sum


# dfs로 탐색하여 이어져있는지 확인하기
# 5x5배열을 모두 0으로 설정하고
# 주어진 좌표를 1로 설정하여
# 방문 완료 시 0으로 변경
# 탐색 후 2차원 배열의 합이 0인지 확인
def dfs(arr):
    # 5x5배열을 모두 0으로 설정하고
    initial = [[0 for i in range(5)] for j in range(5)]

    # 주어진 좌표를 1로 설정하여
    for i in arr:
        initial[i[0]][i[1]] = 1

    stack = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 첫번째 원소부터 탐색 시작
    stack.append([arr[0][0], arr[0][1]])
    # 방문 완료 시 0으로 초기화
    initial[arr[0][0]][arr[0][1]] = 0

    while stack:  # 스택이 빌 때까지 반복
        cur = stack.pop()

        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue

            # 1이면 이동 가능한 곳
            if initial[nx][ny] == 1:
                stack.append([nx, ny])
                initial[nx][ny] = 0  # 방문 처리

    # dfs로 탐색 완료 후 배열의 모든 합이 0인지 확인
    # 0이면 이어져있음
    if arr_sum(initial) == 0:
        return True
    else:
        return False


outnumber = []
# 1차원 배열처럼 생각하여 25개 중 7개 뽑기
for i in itertools.combinations(range(25), 7):  # 25개 중 7개 선택
    changed = coordinate(i)
    if check_number(changed) >= 4 and dfs(changed):
        outnumber.append(changed)  # S가 4개 이상 포함된 배열(좌표)
print(len(outnumber))
