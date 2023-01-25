def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    path = set([costs[0][0]])
    
    while len(path) != n:
        for cost in costs:
            if cost[0] in path and cost[1] in path:
                continue
            if cost[0] in path or cost[1] in path:
                path.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer