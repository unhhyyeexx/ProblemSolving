from itertools import combinations as comb

def check_prime_num(n):
    if n == 1:
        return True
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    combArr = comb(nums, 3)
    for num in combArr:
        if check_prime_num(sum(num)):
            answer += 1
    
    return answer