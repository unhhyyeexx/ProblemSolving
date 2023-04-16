from collections import defaultdict


def solution(record):
    answer = []
    stack = []
    dic = defaultdict(str)
    for r in record:
        if r[0:5] == 'Enter':
            action, uid, name = r.split()
            dic[uid] = name
            stack.append([uid, action])
        elif r[0:5] == 'Leave':
            action, uid = r.split()
            stack.append([uid, action])
        elif r[0:5] == 'Chang':
            action, uid, name = r.split()
            dic[uid] = name
    for s in stack:
        answer.append(f"{dic[s[0]]}님이 들어왔습니다." if s[1] == 'Enter' else f"{dic[s[0]]}님이 나갔습니다.")

    return answer