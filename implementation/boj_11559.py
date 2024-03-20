import sys
import copy

graph = []
for i in range(12):
    graph.append(list(sys.stdin.readline().rstrip()))


# 터진 뿌요 자리 .으로 변경
def after_explore(explore, arr):
    for e in explore:
        arr[e[0]][e[1]] = "."

    return arr


# 뿌요 터짐
def bomb(x, y, arr, visited):
    # 4개 이상인지 카운트
    puyo_cnt = 1

    stack = []
    stack.append([x, y])

    explore = []
    explore.append([x, y])

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while stack:
        cur_x, cur_y = stack.pop()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= 12 or ny >= 6:
                continue

            # 같은 색의 뿌요이고, 방문한 적 없을 경우
            if (arr[nx][ny] == arr[cur_x][cur_y]) and (not visited[nx][ny]):
                stack.append([nx, ny])
                visited[nx][ny] = True
                explore.append([nx, ny])
                puyo_cnt += 1

    if puyo_cnt >= 4:
        return after_explore(explore, arr), visited

    return arr, visited


# 터지고나서 뿌요 내려옴
def down(arr):
    # 열 별로 검사
    for i in range(len(arr[0])):  # 0~5
        empty = []

        for j in range(len(arr) - 1, -1, -1):  # 11~0
            if arr[j][i] == ".":  # 빈 곳이면 저장해둠 #[11, 1], [10, 1], ... [0, 1]
                empty.append([j, i])
            else:  # 뿌요이면
                if empty:
                    arr[empty[0][0]][empty[0][1]] = arr[j][i]  # 빈 곳에 뿌요 갖다넣음
                    arr[j][i] = "."  # 뿌요 자리를 빈 자리로 만듦
                    empty[0] = [j, i]  # 기존 뿌요 있던 자리 저장
                    empty.sort(reverse=True)  # 내림차순 정렬

    return arr


result = 0
while True:
    copied = copy.deepcopy(graph)

    visited = [[False for i in range(6)] for j in range(12)]
    for i in range(12):
        for j in range(6):
            if (copied[i][j] != ".") and (not visited[i][j]):  # 뿌요이면
                visited[i][j] = True
                copied, visited = bomb(i, j, copied, visited)

    # 하나도 터지지 않으면 종료
    if graph == copied:
        print(result)
        break

    copied = down(copied)
    graph = copied
    result += 1