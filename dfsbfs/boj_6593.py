import sys
from collections import deque

while True:
    L, R, C = map(int, sys.stdin.readline().split())

    if L == 0 and R == 0 and C == 0:
        break

    building = []
    start = [0, 0, 0]
    for i in range(L):
        stair = []
        for j in range(R):
            temp = list(sys.stdin.readline().strip())
            if temp == []:
                continue
            # print(temp)

            for k in range(len(temp)):  # 시작점 찾기
                if temp[k] == "S":
                    start = [i, j, k]
                    break

            stair.append(temp)
        t = sys.stdin.readline()  # 공백 한줄 제거
        building.append(stair)  # 3차원 배열 만들기


    def bfs(start):
        dz = [1, -1, 0, 0, 0, 0]
        dx = [0, 0, 0, 0, -1, 1]
        dy = [0, 0, 1, -1, 0, 0]

        deq = deque()

        z, x, y = start
        deq.append([z, x, y, 0])  # 위치 + 소요시간(처음은 0)
        building[z][x][y] = str(0)  # 방문처리를 소요시간으로 설정

        while deq:
            cur_z, cur_x, cur_y, cur_time = deq.popleft()

            for i in range(6):  # 6방향
                nz = cur_z + dz[i]
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]

                if nz < 0 or nx < 0 or ny < 0 or nz >= L or nx >= R or ny >= C:
                    continue

                if building[nz][nx][ny] == "E":  # 출구이면
                    return cur_time + 1

                if building[nz][nx][ny] == ".":  # 이동할 수 있는 곳이면
                    deq.append([nz, nx, ny, int(cur_time) + 1])
                    building[nz][nx][ny] = str(int(cur_time) + 1)

        return -1


    result = bfs(start)

    if result == -1:
        print("Trapped!")
    else:
        print("Escaped in " + str(result) + " minute(s).")