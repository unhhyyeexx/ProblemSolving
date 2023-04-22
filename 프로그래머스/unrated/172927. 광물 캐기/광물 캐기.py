
def solution(picks, minerals):
    answer = 0
    
    m = [[0,0,0] for _ in range(11)]
    
    if sum(picks)*5 < len(minerals):
        minerals = minerals[:sum(picks)*5+1]
        
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            m[i//5][0] += 1
        elif minerals[i] == 'iron':
            m[i//5][1] += 1
        elif minerals[i] == 'stone':
            m[i//5][2] += 1
    
    
    m.sort(key=lambda x:(-x[0], -x[1], -x[2]))

    i = 0
    while m[i] != [0,0,0] and picks != [0,0,0]:
        if picks[0]:
            answer += sum(m[i])
            picks[0] -= 1
        elif picks[1]:
            answer += (m[i][0]*5 + m[i][1] + m[i][2])
            picks[1] -= 1
        elif picks[2]:
            answer += (m[i][0]*25 + m[i][1]*5 + m[i][2])
            picks[2] -= 1
        i += 1
    return answer