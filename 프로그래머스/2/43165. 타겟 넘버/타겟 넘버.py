answer = 0 

def dfs(numbers, target, idx, sumv):
    global answer
    if idx == len(numbers):
        if sumv == target:
            answer += 1
        return

    dfs(numbers, target, idx+1, sumv+numbers[idx])
    dfs(numbers, target, idx+1, sumv-numbers[idx])

def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    
    return answer