def solution(name):
    answer = 0
    
    # 기본 이동 횟수는 길이 -1
    move = len(name) -1
    
    for i, n in enumerate(name):
        answer += min(ord(n)-ord('A'), ord('Z')-ord(n)+1)
        
        # 연속된 A 찾기
        next = i+1
        while next<len(name) and name[next]=='A':
            next += 1
        
        # 기존, 연속된 A의 왼쪽 시작, 연속된 A의 오른쪽 시작
        move = min(move, 2*i + len(name) - next, i + 2*(len(name)-next))
    
    answer += move
    
    return answer