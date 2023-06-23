import sys
from bisect import bisect_left, bisect_right

def cut(trees, mid):
    remain = 0
    for tree in trees:
        if mid < tree:
            remain += (tree-mid)

    return remain

def binary_search(s, e, target):

    ans = 0
    if s == e:
        return e-target

    while (s<=e):
        m = (s + e) // 2

        #m을 기준으로 나무를 자르면 가져갈 수 있는 나무
        total = cut(trees, m)

        if total >= target: #원하는 나무 길이보다 길면 m이 더 커져야 함
            s = m+1
            ans = m
        else: #원하는 나무 길이보다 짧으면 m이 더 작아져야 함
            e = m-1

    return ans

N, M = map(int,sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))
trees.sort() #이분탐색 위해 정렬
print(binary_search(0, trees[-1], M))