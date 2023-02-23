def solution(files):
    answer = []
    arr = []
    for idx, file in enumerate(files):
        # head, num, idx
        tmp = ['', '', idx]
        for f in file:
            if not f.isdigit():
                if tmp[1] != '':
                    break
                tmp[0] += f.lower()
            else:
                tmp[1] += f
        tmp[1] = int(tmp[1])
        arr.append(tmp)
    arr.sort()

    for a in arr:
        answer.append(files[a[2]])
    return answer