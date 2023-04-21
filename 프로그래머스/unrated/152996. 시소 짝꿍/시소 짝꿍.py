from collections import defaultdict

def solution(weights):
    answer = 0
    dic = defaultdict(int)
    for w in weights:
        answer += dic[w] + dic[w*2] + dic[w/2] + dic[(w*2)/3] + dic[(w*3)/2] + dic[(w*4)/3] + dic[(w*3)/4]
        dic[w] += 1
    return answer