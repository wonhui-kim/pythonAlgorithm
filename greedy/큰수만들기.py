def solution(number, k):
    length = len(number) - k  # 제거하고 남은 수 개수 = 뽑아야 하는 수 개수

    card = list(map(str, number))  # 최대 배열 원소 개수 1,000,000

    start_index = 0
    end_index = len(card) - length + 1
    result = []

    for i in range(length):
        num = max(card[start_index:end_index])
        result.append(num)
        loc = card[start_index:end_index].index(num) + start_index
        start_index = loc + 1
        end_index += 1

    return ''.join(result)