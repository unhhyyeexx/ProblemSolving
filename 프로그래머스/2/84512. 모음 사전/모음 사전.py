
def solution(word):
    answer = 0
    dic = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    n = len(word)
    answer = n
    for i in range(n):
        tmp = 0
        for j in range(4-i, -1, -1):
            tmp += 5**j
        answer += tmp * dic[word[i]]
    return answer