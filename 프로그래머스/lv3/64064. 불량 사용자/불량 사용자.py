def solution(user_id, banned_id):
    banned = [[] for _ in range(len(banned_id))]
    for idx, bi in enumerate(banned_id):
        bl = len(bi)
        for uidx, ui in enumerate(user_id):
            if len(ui) == bl:
                tmp = 0
                for i in range(bl):
                    if bi[i] == '*': 
                        continue
                    elif bi[i] != ui[i]:
                        break
                    elif bi[i] == ui[i]:
                        tmp += 1
                if tmp == (bl-bi.count('*')):
                    banned[idx].append(uidx)
    
    cases = set()
    def dfs(case, cnt):
        if cnt == len(banned_id):
            cases.add(tuple(sorted(case)))
            return
        for b in banned[cnt]:
            if b not in case:
                dfs(case + [b], cnt+1)
                
        return
    dfs([], 0)
    return len(cases)