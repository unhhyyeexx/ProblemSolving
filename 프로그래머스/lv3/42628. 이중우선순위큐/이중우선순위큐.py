import heapq

def solution(operations):
    q = []
    for oper in operations:
        op, n = oper.split()
        if op == "I":
            heapq.heappush(q, int(n))
        else:
            if len(q) == 0:
                pass
            elif n == "-1":
                heapq.heappop(q)
            elif n == "1":
                q = heapq.nlargest(len(q), q)[1:]
                heapq.heapify(q)
    if len(q) > 0:
        return [max(q), min(q)]
    return [0,0]