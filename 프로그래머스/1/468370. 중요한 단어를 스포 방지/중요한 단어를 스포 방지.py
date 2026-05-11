from collections import deque

def solution(message, spoiler_ranges):
    answer = set()
    n = len(message)
    unimportant = set()
    important = []
    important_idxs = [0 for _ in range(n+1)]
    
    # 중요한 단어 인덱스 미리 표시
    for s, e in spoiler_ranges:
        for i in range(s, e+1):
            important_idxs[i] = 1
    
    now_word = ''
    is_important = False

    for i in range(n):
        nowStr = message[i]
        if nowStr == ' ':
            if is_important:
                important.append(now_word)
            else:
                unimportant.add(now_word)
            now_word = ''
            is_important = False
        
        else:
            if not is_important and important_idxs[i] == 1:
                is_important = True
            now_word += nowStr
    
    # 마지막 단어가 중요단어였을 경우
    if is_important == True:
        important.append(now_word)
    
    for word in important:
        if word not in unimportant:
            answer.add(word)

            
    return len(answer)