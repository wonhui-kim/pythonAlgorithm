import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

def bfs(x):
    # 출발지와 도착지 같은 경우 0
    if x == K:
        return 0

    s1 = set()
    deq = deque()
    deq.append([x, 0])  # 현재 값, depth (몇 초인지)
    s1.add(x)  # 중복된 숫자가 들어갈 필요가 없기에 set으로 중복 체크

    while deq:
        cur = deq.popleft()  # [현재값, depth] 형식

        # -1, +1, *2 연산
        # 넣을 때 도착 위치인지 바로 체크
        # 같은 숫자 넣을 필요 없음
        depth = cur[1] + 1
        temp = [cur[0] - 1, cur[0] + 1, cur[0] * 2]

        for i in temp:
            # 출발지와 도착지 넘어가는 범위는 skip!!
            if i < 0 or i > 100000:
                continue
            if i == K:
                return depth
            if i not in s1:
                s1.add(i)
                deq.append([i, depth])

    return -1

print(bfs(N))