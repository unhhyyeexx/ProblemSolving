def solution(storey):
    answer = 0
    
    while storey:
        rmd = storey % 10
        if rmd > 5:
            answer += (10-rmd)
            storey += 10
        elif rmd < 5:
            answer += rmd
        else:
            if (storey//10)%10 > 4:
                storey += 10
            answer += 5
        storey //= 10
    return answer

