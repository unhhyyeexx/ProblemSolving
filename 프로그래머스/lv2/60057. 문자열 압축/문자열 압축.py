def solution(s):
    answer = len(s)
    
    if len(s) == 1:
        answer = 1
    else:
        #몇 자씩 자를건지
        for l in range(1, len(s)//2 + 1):
            tmp =''
            idx = 0
            cutcnt = 1 #같은 문자열 개수
            while idx < len(s):
                
                if s[idx:idx+l] == s[idx+l:idx+l+l]:
                    cutcnt += 1
                    idx += l
                else:
                    if cutcnt >= 2:
                        tmp += str(cutcnt) + s[idx:idx+l]
                    else:
                        tmp += s[idx:idx+l]
                    idx += l
                    cutcnt = 1 #같은 문자열 개수

            answer = min(answer, len(tmp))
    return answer