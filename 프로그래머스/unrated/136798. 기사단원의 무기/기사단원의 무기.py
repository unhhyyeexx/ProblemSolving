def solution(number, limit, power):
    div = [1]
    for i in range(2, number + 1):
        cnt = 0
        for j in range(1, int(i**0.5 + 1)):
            if i % j == 0:
                cnt += 1
                if j**2 != i:
                    cnt += 1
    
        if cnt > limit :
            div.append(power)
        else:
            div.append(cnt)
    return sum(div)