answer = []
max_v = -1
def solution(n, info):
    
    def calc(a, l):
        ap, ly = 0,0
        for i in range(11):
            if a[i] == l[i] == 0: continue
            elif l[i] <= a[i] : ap += 10-i
            else: ly += 10-i

        return [ap, ly]
    def dfs(lyan, d):
        global answer, max_v
        if d == 11:
            ap, ly = 0,0
            if sum(lyan) == n:
                ap, ly = calc(info, lyan)
            elif sum(lyan) < n:
                lyan[-1] += (n-sum(lyan))
                ap, ly = calc(info, lyan)
            else:
                return
            if ap < ly:
                if max_v < (ly - ap):
                    max_v = (ly-ap)
                    answer = [lyan[:]]
                elif max_v == (ly - ap):
                    answer.append(lyan[:])
            return
        
        lyan.append(info[d]+1)
        dfs(lyan, d+1)
        lyan.pop()
        
        lyan.append(0)
        dfs(lyan, d+1)
        lyan.pop()
            
    dfs([], 0)
    if not answer: return [-1]
    answer.sort(key = lambda x: x[::-1], reverse=True)
    
    return answer[0]