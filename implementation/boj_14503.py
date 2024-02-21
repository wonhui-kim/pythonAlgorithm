import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 후진할 것이기에 북->남, 서, 북, 동 방향으로 이동
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


# 현재 칸 청소 여부
def clean_cur(x, y):
    if graph[x][y] == 0:
        graph[x][y] = 2  # 청소 완료 처리
        return 1

    return 0  # 청소 이미 되어있으면


# 사방에 청소할 곳이 있는지 체크
def possible(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if graph[nx][ny] == 0:  # 청소 안한 곳 있으면
            return True

    return False


# 전진
def move_front(x, y, d):
    if d == 0:  # 북쪽이면
        return x - 1, y
    elif d == 1:
        return x, y + 1
    elif d == 2:
        return x + 1, y
    else:
        return x, y - 1


# 후진
def move_rear(x, y, d):
    nx = x + dx[d]
    ny = y + dy[d]

    return nx, ny


# 총 청소한 칸 수 반환 함수
def total_clean(x, y, d):
    cnt = 0

    while True:

        cnt += clean_cur(x, y)  # 우선 현재칸 청소 여부

        if not possible(x, y):  # 사방에 청소할 곳 없으면
            nx, ny = move_rear(x, y, d)  # 후진한 좌표

            if graph[nx][ny] == 1:  # 후진했는데 벽이면
                return cnt  # 현재까지 청소한 곳을 반환하고 종료

            # 현 좌표를 후진한 좌표로 이동
            x = nx
            y = ny
            continue  # 다시 처음부터 반복

        else:  # possible(x, y) == True -> 사방에 청소할 곳 있으면
            for i in range(4):
                d -= 1  # 반시계 방향 회전

                if d < 0:
                    d = 3

                nx, ny = move_front(x, y, d)

                if graph[nx][ny] == 0:  # 다음 칸으로 전진 가능한 곳이면
                    # 좌표 이동 후 탈출
                    x = nx
                    y = ny
                    break

    return cnt


print(total_clean(r, c, d))