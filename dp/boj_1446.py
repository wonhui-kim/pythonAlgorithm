import sys

# 지름길 개수, 고속도로 길이 D
N, D = map(int, sys.stdin.readline().split())

road = list(range(0, D + 1))

shortcut = []
for i in range(N):
    s, e, w = map(int, sys.stdin.readline().split())

    # 끝나는 지점이 고속도로 길이보다 크면 skip
    if e > D:
        continue

    # 그냥 가는 길이보다 크면 skip
    if s + w > e:
        continue

    shortcut.append([s, e, w])
shortcut.sort()  # 시작점이 빠른 순으로 정렬

for s in shortcut:
    s, e, w = s

    # 이전에 갱신된 길이보다 크면 skip
    if road[s] + w > road[e]:
        continue

    # 지름길 갱신
    road[e] = road[s] + w

    # 지름길 이후 값들 갱신
    # N이 최대 12이기에 2초 넘지 않음
    for j in range(e, D):
        # 기존에 지름길이 더 작은 경우 갱신하지 않음
        if road[j + 1] > road[j] + 1:
            road[j + 1] = road[j] + 1

print(road[D])