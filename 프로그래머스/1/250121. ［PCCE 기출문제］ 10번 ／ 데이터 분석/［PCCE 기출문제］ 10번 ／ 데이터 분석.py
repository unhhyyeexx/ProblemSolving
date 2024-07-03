def solution(data, ext, val_ext, sort_by):
    answer = []
    dic = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    ext_code = dic[ext]
    data.sort(key=lambda x: x[ext_code])
    tmp = []
    for d in data:
        if d[ext_code] > val_ext:
            break
        answer.append(d)
    answer.sort(key=lambda x: x[dic[sort_by]])
    return answer