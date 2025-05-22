def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    st = h1*3600 + m1*60 + s1
    et = h2*3600 + m2*60 + s2
    
    if st == 0 * 3600 or st == 12 * 3600:
        answer += 1
    
    while st < et:
        hangle = (st / 120) % 360
        mangle = (st / 10) % 360
        sangle = (st * 6) % 360
        
        hnangle = 360 if (st+1) / 120 % 360 == 0 else (st + 1) / 120 % 360 
        mnangle = 360 if (st + 1) / 10 % 360 == 0 else (st + 1) / 10 % 360
        snangle = 360 if (st + 1) * 6 % 360 == 0 else (st + 1) * 6 % 360
        
        if sangle < hangle and snangle >= hnangle:
            answer += 1
        if sangle < mangle and snangle >= mnangle:
            answer += 1
        if snangle == hnangle and hnangle == mnangle:
            answer -= 1
        
        st += 1
    
    return answer