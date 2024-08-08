
def solution(picks, minerals):
    answer = 0
    
    if sum(picks)*5 < len(minerals):
        minerals = minerals[:sum(picks)*5 + 1]
        
    tmp = [[0,0,0] for _ in range(len(minerals)//5 + 1)]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            tmp[i//5][0] += 1
        elif minerals[i] == 'iron':
            tmp[i//5][1] += 1
        else:
            tmp[i//5][2] += 1
    
    tmp.sort(key=lambda x:(-x[0], -x[1], -x[2] ))
    
    i = 0
    while i < len(tmp) and picks != [0,0,0]:
        if picks[0]:
            answer += sum(tmp[i])
            picks[0] -= 1
        elif picks[1]:
            answer += (tmp[i][0] * 5 + tmp[i][1] + tmp[i][2])
            picks[1] -= 1
        else:
            answer += (tmp[i][0] * 25 + tmp[i][1]*5 + tmp[i][2])
            picks[2] -= 1
        i += 1
    
    return answer