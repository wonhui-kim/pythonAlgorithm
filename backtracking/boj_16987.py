import sys


# 깨진 계란 세기
def cnt_cracked(arr):
    cnt = 0
    for a in arr:
        if a[0] <= 0:
            cnt += 1

    return cnt


def backtracking(n):  # n은 현재 들고 있는 계란
    global result

    if n == N:
        result = max(result, cnt_cracked(eggs))
        return

    # 현재 들고 있는 계란이 깨지면 다음 계란으로 이동
    if eggs[n][0] <= 0:
        backtracking(n + 1)
    else:
        for i in range(N):
            if i == n or eggs[i][0] <= 0:  # 현재 계란이 칠 계란이거나 칠 계란이 깨졌다면
                continue
            # 계란 깨기
            eggs[n][0] -= eggs[i][1]
            eggs[i][0] -= eggs[n][1]
            backtracking(n + 1)  # 다음 계란으로 넘어감
            # 원상 복구
            eggs[n][0] += eggs[i][1]
            eggs[i][0] += eggs[n][1]


N = int(sys.stdin.readline())
eggs = []
for i in range(N):
    eggs.append(list(map(int, sys.stdin.readline().split())))

result = 0
backtracking(0)
print(result)