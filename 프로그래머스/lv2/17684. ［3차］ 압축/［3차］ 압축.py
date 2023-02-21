def solution(msg):
    answer = []
    dic = dict()
    alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    for idx, a in enumerate(alphabet):
        dic[a] = idx+1
    maxIdx = 26
    
    length = 0
    idx = 0
    while True:
        length += 1
        if not msg[idx:idx+length] in dic:
            answer.append(dic[msg[idx:idx+length-1]])
            maxIdx += 1
            dic[msg[idx:idx+length]] = maxIdx
            idx += length - 1
            length = 0
        else:
            if idx+length-1 == len(msg):
                answer.append(dic[msg[idx:idx+length-1]])
                break
    return answer