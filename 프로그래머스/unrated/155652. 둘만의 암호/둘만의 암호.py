def solution(s, skip, index):
    answer = ''
    apb = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in skip:
        if i in apb:
            apb = apb.replace(i, "")
    
    for i in s:
        new = apb[(apb.index(i) + index) % len(apb)]
        answer += new
        
    return answer