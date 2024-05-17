# from itertools import product

# def solution(word):
#     total = []
#     for i in range(1, 6):
#         for j in product(['A','E','I','O','U'], repeat=i):
#             total.append(''.join(list(j)))
    
#     total.sort()
#     return total.index(word) + 1

# def solution(word):
#     answer = 0
#     dic = ['A','E','I','O','U']
#     li = [5**i for i in range(len(dic))]
#     for i in range(len(word)-1, -1, -1):
#         idx = dic.index(word[i])
#         for j in range(5-i):
#             answer += li[j]*idx
#         answer += 1
#     return answer

def solution(word):
    dic = {'A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5}
    n = len(word)
    answer = n
    for i in range(n):
        tmp = 0
        for j in range(4-i, -1, -1):
            tmp += 5 ** j
        answer += tmp * (dic[word[i]] -1)
    return answer