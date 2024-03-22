from collections import defaultdict

def solution(friends, gifts):
    answer = 0
    
    give, get = defaultdict(list), defaultdict(list)
    
    for gift in gifts:
        a, b = gift.split()
        give[a].append(b)
        get[b].append(a)
    
    result = defaultdict(int)
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            a, b = friends[i], friends[j]
            x, y = give[a].count(b), get[a].count(b)
            if x-y > 0:
                result[a] += 1
            elif x-y < 0:
                result[b] += 1
            
            elif x-y == 0:
                av, bv = len(give[a])-len(get[a]), len(give[b])-len(get[b])
                if av-bv > 0:
                    result[a] += 1
                elif av-bv < 0:
                    result[b] += 1
            
    if not result:
        return 0
    
    return max(result.values())