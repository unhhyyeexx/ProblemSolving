def solution(prices):
    answer = [0] * len(prices)
    n = len(prices)
    stack = []
    
    for i in range(n):
        while stack != [] and stack[-1][1] > prices[i]:
            pre, _ = stack.pop()
            answer[pre] = i - pre
        stack.append((i, prices[i]))
    
    for i, s in stack:
        answer[i] = n - 1 - i  
    
    return answer