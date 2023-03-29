from collections import defaultdict

def convert(time):
    return int(time[:2])*60 + int(time[3:5])

def solution(book_time):
    dic = defaultdict(int)
    for b in book_time:
        s = convert(b[0])
        e = convert(b[1])
        for t in range(s, e+10):
            dic[t] += 1
    return max(dic.values())