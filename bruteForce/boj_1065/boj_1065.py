import sys

N = int(sys.stdin.readline())

def split_number(num):
    result = []
    while True:
        if len(result) == len(str(num)):
            break
        result.append(int(num%10))
        num /= 10
    return result

def interval(arr):
    sub = arr[0]-arr[1]
    print(arr, sub)

    for i in range(1, len(arr)-1):
        print(i)
        if (arr[i]-arr[i+1]) != sub:
            return False

    return True

if N < 100:
    print(N)
else:
    count = 99
    print(split_number(N))
    # for i in range(100, N+1):
    #     print(i)
    #     print(interval(split_number(i)))
    #
    #
    #     # if interval(split_number(i)) == True:
    #     #     count += 1
    # print(count)