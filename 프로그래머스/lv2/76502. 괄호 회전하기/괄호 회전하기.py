from collections import deque

def check(s):
    dic = {']':'[', '}':'{', ')':'(' }
    stack = []
    for i in s:
        if i in ['[', '{', '(']:
            stack.append(i)
        else:
            if stack and stack[-1] == dic[i]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False

def solution(s):
    answer = 0
    q = deque(s)
    for _ in range(len(s)):
        tmp = q.popleft()
        q.append(tmp)
        if check(q):
            answer += 1
    return answer