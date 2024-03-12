import sys

L, C = map(int, sys.stdin.readline().split())
alphabet = list(sys.stdin.readline().rstrip().split())
alphabet.sort()

answer = [" "] * L
answer_set = set()


def check_answer(answer):
    consonant = 0
    vowel = 0

    for a in answer:
        if a in ["a", "e", "i", "o", "u"]:
            vowel += 1
        else:
            consonant += 1

    if vowel >= 1 and consonant >= 2:
        return True

    return False


def backtracking(n, depth):
    if depth == L:
        if check_answer(answer):
            answer_str = ''.join(answer)
            if answer_str not in answer_set:
                print(answer_str)
            answer_set.add(answer_str)
        return

    for i in range(n, C):
        answer[depth] = alphabet[i]
        backtracking(i + 1, depth + 1)


for i in range(0, C - L + 1):
    backtracking(i, 0)