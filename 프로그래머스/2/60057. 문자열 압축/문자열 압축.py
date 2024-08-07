def solution(s):
    answer = len(s)
    n = len(s)
    
    if len(s)==1:
        return 1
    
    for l in range(1, n//2 + 1):
        tmp = ''
        idx = 0
        cnt = 1
        while idx < n:
            if s[idx:idx+l] == s[idx+l:idx+l+l]:
                cnt += 1
                idx += l
            else:
                if cnt >= 2:
                    tmp += str(cnt)+s[idx:idx+l]
                else:
                    tmp += s[idx:idx+l]
                idx += l
                cnt = 1
        answer = min(answer, len(tmp))
    return answer