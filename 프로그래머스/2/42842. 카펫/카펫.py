def solution(brown, yellow):
    answer = [0, 0]
    brown = (brown+4)//2
    for i in range(1, brown//2+1):
        j = brown - i
        if (i-2)*(j-2) == yellow:
            answer = [j, i]
            break
    return answer
            