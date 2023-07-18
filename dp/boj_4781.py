import sys

while True:
    # 사탕 종류 n, 돈의 양 m
    n, m = map(float, sys.stdin.readline().split())

    n = int(n)
    m = int(m * 100 + 0.5)

    # 종료조건
    if n == 0 and m == 0:
        break

    c = []  # 칼로리
    p = []  # 가격
    for i in range(n):
        calorie, price = map(float, sys.stdin.readline().split())
        c.append(int(calorie))
        p.append(int(price * 100 + 0.5))

    # 돈 m은 계산하기 용이하도록 x100 (0.01~ -> 1~)
    dp = [0 for i in range(m + 1)]

    for k in range(n):  # 사탕 종류만큼 반복
        for w in range(p[k], m + 1):
            if w >= p[k]:
                dp[w] = max(dp[w], dp[w - p[k]] + c[k])

    print(dp[m])