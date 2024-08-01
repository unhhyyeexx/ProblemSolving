from itertools import product

def solution(user_id, banned_id):
    bn = len(banned_id)
    candidate = [[] for _ in range(bn)]
    for i in range(bn):
        bid = banned_id[i]
        for uid in user_id:
            if len(uid) == len(bid):
                flag = 0
                for j in range(len(bid)):
                    if bid[j] != '*' and bid[j] != uid[j]:
                        break
                    else:
                        flag += 1
                if flag == len(bid):
                    candidate[i].append(uid)
    
    pd = list(product(*candidate))
    setcombi = set()
    for i in pd:
        tmp = set(i)
        if len(tmp) == bn:
            setcombi.add("".join(sorted(tmp)))
    
    return len(setcombi)