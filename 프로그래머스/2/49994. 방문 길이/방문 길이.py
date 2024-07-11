

def solution(dirs):
    dir = [[1,0], [-1,0], [0,1], [0,-1]]
    dic = {'U':0, 'D':1, 'R':2, 'L':3}
    i, j = 0, 0
    path = set()
    for d in dirs:
        ni, nj = i+dir[dic[d]][0], j+dir[dic[d]][1]
        if -5<=ni<=5 and -5<=nj<=5:
            path.add((i, j, ni, nj))
            path.add((ni, nj, i, j))
            i, j = ni, nj

    return len(path)//2