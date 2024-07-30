def solution(files):
    answer = []
    sep = []
    for file in files:
        head, number, tail = '','',''
        for f in file:
            if not head or (not f.isnumeric() and not number):
                head += f
            elif f.isnumeric() and head and not tail:
                number += f
            elif tail or (number and not f.isnumeric()):
                tail += f
        sep.append([head, number, tail])
    
    sep.sort(key=lambda x:(x[0].lower(), int(x[1])))
    for s in sep:
        answer.append(''.join(s))
    return answer