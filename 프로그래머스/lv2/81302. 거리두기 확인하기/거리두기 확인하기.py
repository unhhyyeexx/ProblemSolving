def solution(places):
    answer = []
    dirs = [[-1,0], [0,1], [1,0], [0,-1]]
    def check(i, j, place):
        for di, d in enumerate(dirs):
            ni, nj = i+d[0], j+d[1]
            if 0<=ni<5 and 0<=nj<5:
                if place[ni][nj] == 'X': 
                    continue
                elif place[ni][nj] == 'P':
                    return False
                elif place[ni][nj] == 'O':
                    for ddi, dd in enumerate(dirs):
                        if (ddi+2)%4 == di: continue
                        else: 
                            nni, nnj = ni+dd[0], nj+dd[1]
                            if 0<=nni<5 and 0<=nnj<5 and place[nni][nnj] == 'P':
                                return False
                
        return True
    
    for place in places:
        for i in range(5):
            tmp = True
            for j in range(5):
                if place[i][j] == 'P':
                    if not check(i, j, place):
                        tmp = False
                        break
            if tmp == False:
                answer.append(0)
                break
        if tmp == True:
            answer.append(1)
                
    return answer