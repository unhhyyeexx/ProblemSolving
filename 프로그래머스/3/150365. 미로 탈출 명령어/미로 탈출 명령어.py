def solution(n, m, x, y, r, c, k):
    answer = []
    # d l r u
    dist = abs(x-r) + abs(y-c)
    if dist > k or (k-dist)%2 == 1:
        return 'impossible'
    
    cx, cy = x, y
    remain = k
    
    dirs = [
        ('d', 1, 0),
        ('l', 0, -1),
        ('r', 0, 1),
        ('u', -1, 0)
    ]
    
    while remain > 0:
        moved = False
        
        for ch, dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            
            # 범위 체크
            if not (1<=nx<=n and 1<=ny<=m):
                continue
            # 거기서 목적지까지 최소 거리
            d = abs(nx-r) + abs(ny-c)
            # 앞으로 갈 수 있는지
            if d > remain - 1:
                continue
            # 남는 이동 수 짝수 조건
            if ((remain - 1 - d)%2) != 0:
                continue
            # 가능하면 바로 선택
            answer.append(ch)
            cx, cy = nx, ny
            remain -= 1
            moved = True
            break
        
        if not moved:
            return "impossible"
    return "".join(answer)