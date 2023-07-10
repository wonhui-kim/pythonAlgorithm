def solution(array, commands):
    answer = []

    for i, j, k in commands:
        new = array[i - 1:j]
        new.sort()
        answer.append(new[k - 1])

    return answer