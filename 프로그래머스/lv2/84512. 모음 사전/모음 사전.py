from itertools import product

def solution(word):
    total = []
    for i in range(1, 6):
        for j in product(['A','E','I','O','U'], repeat=i):
            total.append(''.join(list(j)))
    
    total.sort()
    return total.index(word) + 1