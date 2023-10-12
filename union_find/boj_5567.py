import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

friends = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    friends[a].append(b)
    friends[b].append(a)

invited = set()

for a in friends[1]:
    # 상근 친구 먼저 넣기
    invited.add(a)

    # 친구의 친구 넣기
    for b in friends[a]:
        if b != 1:
            invited.add(b)

print(len(invited))