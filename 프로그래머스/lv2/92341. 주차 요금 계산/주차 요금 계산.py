import math

def changetime(t):
    h, m = map(int, t.split(':'))
    return h*60 + m

def solution(fees, records):
    answer = []
    dt, df, ut, uf = fees
    
    dic = dict()
    
    for r in records:
        t, n, io = r.split()
        if n in dic:
            dic[n].append([changetime(t), io])
        else:
            dic[n] = [[changetime(t), io]]
    
    histories = list(dic.items())
    histories.sort(key = lambda x: x[0])
    
    for history in histories:
        time = 0
        for h in history[1]:
            if h[1] == 'IN':
                time -= h[0]
            else:
                time += h[0]
        
        if history[1][-1][1] == 'IN':
            time += changetime('23:59')
        
        if time < dt:
            answer.append(df)
        else:
            answer.append(df + math.ceil((time-dt)/ut)*uf)
    
    return answer