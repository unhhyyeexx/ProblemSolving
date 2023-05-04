def solution(park, routes):
    r, c = len(park), len(park[0])
    now = []
    for i in range(r):
        for j in range(c):
            if park[i][j] == 'S':
                now = [i, j]
    
    dir = {'E':[0,1], 'W':[0,-1], 'S':[1,0], 'N':[-1,0]}
    for route in routes:
        op, n = route.split()
        d = dir[op]
        org = now.copy()
        for k in range(int(n)): 
            now[0] += d[0]
            now[1] += d[1]
            if not (0<=now[0]<r and 0<=now[1]<c and park[now[0]][now[1]] != 'X'): 
                now = org
                break

    return now