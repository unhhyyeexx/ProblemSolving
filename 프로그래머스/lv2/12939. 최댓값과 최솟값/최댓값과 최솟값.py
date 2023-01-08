def solution(s):
    
    nums = list(map(int, s.split()))
    minv, maxv = min(nums), max(nums)
    answer = str(minv) + " " + str(maxv)
    
    return answer