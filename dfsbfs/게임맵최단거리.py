from queue import Queue

def bfs(x, y, dist, copy):
    queue = Queue()
    queue.put([x, y, dist]) #좌표와 거리 저장
    copy[x][y] = 0 #방문 처리

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    n = len(copy)
    m = len(copy[0])

    result = [[0 for j in range(m)] for i in range(n)]  # 결과 배열
    #큐가 빌 때까지 반복
    while not queue.empty():
        cur = queue.get() #[0, 0, 0] 형태로 반환
        result[cur[0]][cur[1]] = cur[2] #결과 배열에 거리 저장

        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if copy[nx][ny] == 1:
                queue.put([nx, ny, cur[2]+1]) #다음 좌표와 거리를 하나 더해서 저장
                copy[nx][ny] = 0 #방문 처리, 중복 줄이기 위해 큐에 넣을 때

    if result[n-1][m-1] == 0:
        return -1

    return result[n-1][m-1] + 1

def solution(maps):
    copy = maps
    answer = bfs(0, 0, 0, copy)
    return answer

print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))