def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    if (len(diffs) == 1):
        return times[0]
    
    while (left < right) :
        mid = (left+right)//2
        time = 0
        for i in range(len(diffs)):
            if (mid < diffs[i]) :
                time += (diffs[i]-mid)*(times[i] + times[i-1]) + times[i]
            else :
                time += times[i]
        if time > limit:
            left = mid + 1
        else :
            right = mid
    
    return left