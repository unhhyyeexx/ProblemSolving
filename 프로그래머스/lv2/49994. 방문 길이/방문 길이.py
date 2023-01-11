def solution(dirs):
    dir = [[-1,0], [1,0], [0,1], [0,-1]]
    dd = ['U', 'D', 'R', 'L']
    i, j = 0, 0
    sets = set()
    for d in dirs:
        k = dd.index(d)
        ni, nj = i+dir[k][0], j+dir[k][1]
        if -5<=ni<=5 and -5<=nj<=5:
            sets.add((i, j, ni, nj))
            sets.add((ni, nj, i, j))
            i, j = ni, nj
            
    return len(sets) // 2