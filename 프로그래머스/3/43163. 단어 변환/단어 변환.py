from collections import deque

def check(now, word, cnt):
    ch = 0
    for w in range(cnt):
        if word[w] == now[w]:
            ch += 1
    if ch == (cnt-1):
        return True
    return False
    

def solution(begin, target, words):
    answer = 0
    
    cnt = len(begin)
    n = len(words)
    visit = [0]*n
    
    q = deque([(begin, 0)])
    
    while q:
        now = q.popleft()
        if now[0] == target:
            answer = now[1]
            break
        for i in range(n):
            if visit[i] == 0 and check(now[0], words[i], cnt):
                visit[i] = 1
                q.append((words[i], now[1]+1))
    return answer