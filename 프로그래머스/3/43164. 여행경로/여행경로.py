from collections import defaultdict
def solution(tickets):
    answer = []
    dic = defaultdict(list)
    for i, (s, e) in enumerate(tickets):
        dic[s].append([e, i])
    
    n = len(tickets)
    visit = [0] * n

    def dfs(now, path):
        if n + 1 == len(path):
            answer.append(path)
            return
        for end, idx in dic[now]:
            if not visit[idx]:
                visit[idx] = 1
                dfs(end, path+[end])
                visit[idx] = 0

    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]