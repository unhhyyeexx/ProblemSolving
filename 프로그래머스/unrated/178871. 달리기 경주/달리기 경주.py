def solution(players, callings):
    idx = {i: player for i, player in enumerate(players)}
    p = {player: i for i, player in enumerate(players)}
    
    for c in callings:
        now = p[c] # 현재 등수
        lead = now-1 # 앞 등수
        leadPlayer = idx[lead]
        
        idx[now] = leadPlayer
        idx[lead] = c
        
        p[c] = lead
        p[leadPlayer] = now
        
    return list(idx.values())