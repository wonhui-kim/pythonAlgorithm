import sys

money = int(sys.stdin.readline())  # 주어진 돈
graph = list(map(int, sys.stdin.readline().split()))  # 주가 그래프

# [현금, 주식수]
JH = [money, 0]
SM = [money, 0]

# 연속 증가일수, 감소일수 체크
increase = 0
decrease = 0
for i in range(len(graph)):
    cur_price = graph[i]

    # JH
    if JH[0] >= cur_price:
        # 구매 가능한 주식수
        stock_cnt = JH[0] // cur_price
        JH[0] -= stock_cnt * cur_price
        JH[1] += stock_cnt

    if i > 0:
        prev_price = graph[i - 1]
        if cur_price > prev_price:  # 전일 주가보다 상승
            increase += 1
            decrease = 0
        elif cur_price < prev_price:  # 전일 주가보다 감소
            decrease += 1
            increase = 0
        else:  # 전일 주가와 동일
            increase = 0
            decrease = 0

    # SM
    # 전량 매수 (3일 이상 연속 감소 & 현재 주가보다 현금 많을 때)
    if decrease >= 3 and SM[0] >= cur_price:
        stock_cnt = SM[0] // cur_price
        SM[0] -= stock_cnt * cur_price
        SM[1] += stock_cnt

    # 전량 매도 (3일 이상 연속 증가 & 현재 주식수 1 이상일 때)
    if increase >= 3 and SM[1] > 0:
        SM[0] += SM[1] * cur_price
        SM[1] = 0

last_price = graph[-1]
BNP = JH[0] + (JH[1] * last_price)
TIMING = SM[0] + (SM[1] * last_price)

if BNP > TIMING:
    print("BNP")
elif BNP < TIMING:
    print("TIMING")
else:
    print("SAMESAME")