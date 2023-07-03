def solution(arr):
    minV, maxV = 0, 0
    sumV = 0
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == '+':
            continue
        elif arr[i] == '-':
            tmpmin, tmpmax = minV, maxV
            minV = min(-(sumV+tmpmax), -sumV+tmpmin)
            minusV = int(arr[i+1])
            maxV = max(-(sumV+tmpmin), -minusV+(sumV-minusV)+tmpmax)
            sumV = 0
        elif int(arr[i]) >= 0:
            sumV += int(arr[i])
    maxV += sumV
    return maxV