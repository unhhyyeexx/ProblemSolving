def solution(arr):
    arr.sort()
    cnt = 1
    while True:
        check = True
        now = arr[-1] * cnt
        for i in arr[:-1]:
            if now % i != 0:
                check = False
                break
        if check:
            break
        cnt += 1
    return now