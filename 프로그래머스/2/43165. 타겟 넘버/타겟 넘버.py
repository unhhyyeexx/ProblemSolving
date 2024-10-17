answer = 0 

def dfs(n, numbers, target, depth, now):
    global answer
    
    if depth == n-1:
        if now + numbers[depth] == target:
            answer += 1
        elif now - numbers[depth] == target:
            answer += 1
        return 
    dfs(n, numbers, target, depth + 1, now+numbers[depth])
    dfs(n, numbers, target, depth + 1, now-numbers[depth])
    
    return

def solution(numbers, target):
    global answer
    dfs(len(numbers), numbers, target, 0, 0)
    
    return answer