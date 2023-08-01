import sys
from collections import deque

# 총 층 F, 현재 위치 S, 목적지 G, 위버튼 U, 아래버튼 D
F, S, G, U, D = map(int, sys.stdin.readline().split())


def bfs(start):
    answer = -1

    if start == G:  # 출발지와 목적지가 같으면 바로 리턴
        return 0

    s = set()  # 중복 제거 위함
    deq = deque()
    deq.append([start, 0])  # 현 위치와 depth(버튼 몇번 눌렀는지) 저장

    while deq:
        cur_pos, cur_depth = deq.popleft()

        up = cur_pos + U
        down = cur_pos - D

        if up == G or down == G:  # 위 혹은 아래 이동 시 목적지 도착이라면
            return cur_depth + 1

        # 중복 체크, 총 층수보다 작거나 같아야 함
        if (up not in s) and (up <= F):
            s.add(up)
            deq.append([up, cur_depth + 1])

        if (down not in s) and (down >= 1):
            s.add(down)
            deq.append([down, cur_depth + 1])

    return answer


button = bfs(S)

if button == -1:
    print("use the stairs")
else:
    print(button)