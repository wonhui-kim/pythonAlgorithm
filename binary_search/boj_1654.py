import sys

K, N = map(int, sys.stdin.readline().split())

cables = []
for i in range(K):
    cables.append(int(sys.stdin.readline()))


def binary_search(left, right, cables):
    answer = -1
    while left <= right:
        mid = (left + right) // 2

        count = 0
        for c in cables:
            count += (c // mid)

        # 필요한 랜선 개수와 같거나 많으면
        # answer에 mid를 저장하고
        # 최대 길이를 구하고자 하기 때문에 left를 mid+1로 옮김
        if count >= N:
            answer = mid
            left = mid + 1
        # 필요한 랜선 개수보다 적으면
        # mid가 더 작아져야 하기 때문에 right를 mid-1로 옮김
        else:
            right = mid - 1

    return answer


# 랜선 길이는 자연수이기에 left는 1, right는 가장 긴 랜선 크기
print(binary_search(1, max(cables), cables))