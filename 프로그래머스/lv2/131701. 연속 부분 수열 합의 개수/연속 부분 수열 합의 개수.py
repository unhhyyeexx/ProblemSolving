def solution(elements):
    answer = 0
    n = len(elements)
    elements = elements + elements[:n-1]
    sums = set()
    for i in range(1, n+1):
        for j in range(len(elements)-i+1):
            sums.add(sum(elements[j:j+i])) 
    answer = len(sums)
    return answer