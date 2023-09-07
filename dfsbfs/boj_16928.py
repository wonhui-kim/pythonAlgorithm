import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

jump = {}
for i in range(N + M):
    start, end = map(int, sys.stdin.readline().split())
    jump[start] = end

visited = [False for i in range(101)]


def bfs(dic, visit, location, depth):  # 점프, 방문, 위치, 주사위 횟수
    deq = deque()
    deq.append([location, depth])
    visit[location] = True

    while deq:
        cur_loc, cur_depth = deq.popleft()

        for i in range(1, 7):
            next_loc = cur_loc + i

            if next_loc == 100:  # 최종 도착지이면 반환
                return cur_depth + 1

            # 도착지보다 커지거나 이미 방문했으면
            if next_loc > 100 or visit[next_loc]:
                continue

            if next_loc in dic:
                deq.append([dic[next_loc], cur_depth + 1])
                visit[dic[next_loc]] = True
            else:
                deq.append([next_loc, cur_depth + 1])
                visited[next_loc] = True


print(bfs(jump, visited, 1, 0))