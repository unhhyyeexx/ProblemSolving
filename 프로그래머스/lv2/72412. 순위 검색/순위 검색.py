from itertools import combinations
from collections import defaultdict

# 이분탐색
def lower_bound(begin, end, target_list, target):
    if begin >= end:
        return begin
    mid = (begin+end) // 2
    if target_list[mid] >= target:
        return lower_bound(begin, mid, target_list, target)
    else:
        return lower_bound(mid+1, end, target_list, target)

def solution(infos, queries):
    answer = []
    dic = defaultdict(list)
    for info in infos:
        info = info.split()
        condition = info[:-1]
        # [java, backend, junior, pizza]
        score = int(info[-1])
        # 150
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                    # [java, -, junior, pizza]
                key = ''.join(tmp)
                #java-juniorpizza
                dic[key].append(score)
                #dic{'java-juniorpizza':[150]}
    
    # score저장된 value값을 오름차순으로 정렬
    for value in dic.values():
        value.sort()
        
    for query in queries:
        query = query.replace("and", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = lower_bound(0, len(target_list), target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)
    return answer