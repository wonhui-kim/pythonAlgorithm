import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())


def bfs(start, end):
    deq = deque()
    s = set()

    deq.append([start, 1])  # 숫자와 depth
    s.add(start)  # 중복 체크

    while deq:
        cur_num, cur_depth = deq.popleft()

        first = cur_num * 2  # 2 곱하기
        second = int(str(cur_num) + '1')  # 1 오른쪽 추가

        if first == end or second == end:  # B이면 바로 리턴
            return cur_depth + 1

        # B보다 작고, set에 중복되지 않았을 경우
        if (first not in s) and first < end:
            deq.append([first, cur_depth + 1])
            s.add(first)

        if (second not in s) and second < end:
            deq.append([second, cur_depth + 1])
            s.add(second)

    return -1  # deque를 다 돌았는데 답이 안나온 경우


print(bfs(A, B))