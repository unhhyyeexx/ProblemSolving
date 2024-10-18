def solution(arr):
    answer = 0
    
    n = 0
    sumv = 0
    minv, maxv = 0, 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == '+':
            continue
        elif arr[i] == '-':
            tmp_min, tmp_max = minv, maxv
            minv = min(-(sumv+tmp_max), -sumv+tmp_min)
            maxv = max(-(sumv+tmp_min), -n+(sumv-n)+tmp_max)
            sumv = 0
        else:
            n = int(arr[i])
            sumv += int(arr[i])
    maxv += sumv
    return maxv