def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

def solution(n, k):
    result = []
    num_list = [i for i in range(1, n + 1)]
    while(n != 0):
        num_case = factorial(n - 1)
        idx = k // num_case
        k = k % num_case
        if k == 0:
            result.append(num_list.pop(idx - 1))
        else:
            result.append(num_list.pop(idx))
        n -= 1
    return result