def solution(a):
    n = len(a)
    if n == 1:
        return 1
    
    answer = 2
    minLeft = [a[0]]
    minRight = [a[-1]]
    
    for i in range(1, n):
        if a[i] < minLeft[-1]:
            minLeft.append(a[i])
        else:
            minLeft.append(minLeft[-1])
        
        if a[n-1-i] < minRight[-1]:
            minRight.append(a[n-i-1])
        else:
            minRight.append(minRight[-1])
    minRight.reverse()
    
    for i in range(1, n-1):
        if minLeft[i-1] > a[i] or minRight[i+1]>a[i]:
            answer += 1
    
    return answer