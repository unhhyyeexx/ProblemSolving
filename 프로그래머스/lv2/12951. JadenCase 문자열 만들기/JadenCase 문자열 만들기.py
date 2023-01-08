def solution(s):
    answer = ''
    first = True
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
            continue
        else:
            if first:
                answer += s[i].upper()
                first = False
            else:
                if s[i-1] == ' ':
                    answer += s[i].upper()
                else:
                    answer += s[i].lower()
        
    return answer