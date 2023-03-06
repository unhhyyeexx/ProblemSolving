from collections import defaultdict

def solution(genres, plays):
    answer = []
    genrelist = defaultdict(int)
    idxs = defaultdict(list)
    for idx, g in enumerate(genres):
        genrelist[g] += plays[idx]
        idxs[g].append([plays[idx], idx])
    tmp = sorted(genrelist.items(), key=lambda x:x[1], reverse=(True))
    for t,_ in tmp:
        idxs[t].sort(key=lambda x:(-x[0], x[1]))
        print(idxs[t])
        if len(idxs[t]) >= 2:
            for i in range(2):
                answer.append(idxs[t][i][1])
        else:   
            answer.append(idxs[t][0][1])
    return answer