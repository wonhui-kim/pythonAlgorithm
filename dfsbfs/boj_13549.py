import sys
import heapq

# 시작 N, 도착 K
N, K = map(int, sys.stdin.readline().split())
S = set()


def shortest_time(start, end, s):
    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        depth, cur = heapq.heappop(pq)
        print(depth, cur)

        if cur == end:
            return depth

        if (0 <= cur * 2 <= 100000) and (cur * 2 not in s):
            heapq.heappush(pq, [depth, cur * 2])
            s.add(cur * 2)

        if (0 <= cur - 1 <= 100000) and (cur - 1 not in s):
            heapq.heappush(pq, [depth + 1, cur - 1])
            s.add(cur - 1)

        if (0 <= cur + 1 <= 100000) and (cur + 1 not in s):
            heapq.heappush(pq, [depth + 1, cur + 1])
            s.add(cur + 1)


print(shortest_time(N, K, S))