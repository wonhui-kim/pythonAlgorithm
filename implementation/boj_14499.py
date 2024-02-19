import sys
import copy

N, M, x, y, K = map(int, sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 이동 명령
order = list(map(int, sys.stdin.readline().split()))

# top, bottom, left_side, right_side, up_side, down_side
dice = [0, 0, 0, 0, 0, 0]


# 다음 지도 칸으로 이동
def move_next(x, y, direction):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    nx = x + dx[direction - 1]
    ny = y + dy[direction - 1]

    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        return -1, -1

    return nx, ny


def dice_top(nx, ny, dice, direction):
    # 주사위도 굴리기
    turned_dice = turn(dice, direction)

    if graph[nx][ny] == 0:  # 지도가 0이면 주사위바닥->지도
        graph[nx][ny] = turned_dice[1]
    else:  # 0이 아니면 지도->주사위바닥, 칸은 0
        turned_dice[1] = copy.deepcopy(graph[nx][ny])
        graph[nx][ny] = 0

    return turned_dice


# 주사위 굴리기
def turn(dice, direction):
    top, bottom, left_side, right_side, up_side, down_side = dice

    # 동쪽
    if direction == 1:
        return [left_side, right_side, bottom, top, up_side, down_side]

    # 서쪽
    elif direction == 2:
        return [right_side, left_side, top, bottom, up_side, down_side]

    # 북쪽
    elif direction == 3:
        return [down_side, up_side, left_side, right_side, top, bottom]

    # 남쪽
    else:
        return [up_side, down_side, left_side, right_side, bottom, top]


for i in range(K):
    # 지도 벗어나면 무시
    if move_next(x, y, order[i]) == (-1, -1):
        continue
    else:
        x, y = move_next(x, y, order[i])

    dice = dice_top(x, y, dice, order[i])
    print(dice[0])