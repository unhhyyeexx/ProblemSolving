def solution(brown, yellow):
    total = brown + yellow
    # i * j = total
    # j >= i
    for i in range (1, total+1):
        if (total / i) % 1 == 0:
            j = total / i
            if j >= i: # 가로가 더 길 때
                if 2*i + 2*j - 4 == brown:
                    return [j, i]