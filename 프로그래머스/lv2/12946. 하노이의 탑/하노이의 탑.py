def solution(n):
    answer = []
    
    def hanoi(n, start, end, middle):
        if n == 1:
            answer.append([start, end])
            return
        hanoi(n-1, start, middle, end)
        answer.append([start, end])
        hanoi(n-1, middle, end, start)
    
    hanoi(n, 1, 3, 2)
    return answer