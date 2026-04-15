import math
from functools import reduce

def lcm(a,b):
    return a*b // math.gcd(a, b)

def lcm_list(nums):
    return reduce(lcm, nums)

def solution(signals):
    answer = 0
    sumval = [sum(signal) for signal in signals]

    limit = lcm_list(sumval)
    
    for t in range(1, limit + 1):
        ok = True
        
        for G, Y, R in signals:
            cycle = G+Y+R
            pos = (t-1) % cycle
            
            if not (G <= pos < G+Y):
                ok = False
                break
        if ok:
            return t

    return -1
    
    
    

    return answer