import sys

# 탑의 개수
N = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
answer = [0] * N

stack = []
for i in range(N):
    while stack:
        if stack[-1][1] > tower[i]:  # 수신 탑이 있을 때
            answer[i] = stack[-1][0] + 1  # 수신 탑 인덱스 번호 저장
            break
        else:  # 수신 탑 없을 때
            stack.pop()  # 계속 pop해봄

    if not stack:  # 그러다 수신 탑이 없으면
        answer[i] = 0

    stack.append([i, tower[i]])

for a in answer:
    print(a)
