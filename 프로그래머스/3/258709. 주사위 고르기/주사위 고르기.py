from itertools import combinations, product
from bisect import bisect_left

def solution(dices):
    answer = []
    
    dic = {}
    L = len(dices)
    for A_index in combinations(range(L), L//2):
        B_index = [i for i in range(L) if i not in A_index]
        
        A, B = [], []
        for order_product in product(range(6), repeat=L//2):
            A.append(sum(dices[i][j] for i, j in zip(A_index, order_product)))
            B.append(sum(dices[i][j] for i, j  in zip(B_index, order_product)))
            
        B.sort()
        
        wins = sum(bisect_left(B, num) for num in A)
        dic[wins] = list(A_index)
    
    max_key = max(dic.keys())
    return [x+1 for x in dic[max_key]]