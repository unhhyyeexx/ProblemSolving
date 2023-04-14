def solution(m, musicinfos):
    answer = []
    tmpm = []
    for i in range(len(m)):
        if m[i] == '#': continue
        else:
            if i<len(m)-1 and m[i+1] == '#':tmpm.append(m[i:i+2])
            else: tmpm.append(m[i]+'0')
    m = ''.join(tmpm)
    infos = []
    for idx, musicinfo in enumerate(musicinfos):
        s, e, title, tmp = musicinfo.split(',')
        origin = []
        for i in range(len(tmp)):
            if tmp[i] == '#': continue
            else:
                if i<len(tmp)-1 and tmp[i+1] == '#': origin.append(tmp[i:i+2])
                else: origin.append(tmp[i]+'0')
        n = len(origin)
        l = (int(e[:2])*60 + int(e[3:5])) - (int(s[:2])*60 + int(s[3:5]))
        music = (l//n)*origin + origin[:(l%n)]
        music = ''.join(music)
        if m in music:
            print(l,int(s[:2])*60 + int(s[3:5]), title)
            answer.append([l, int(s[:2])*60 + int(s[3:5]), title])
        answer.sort(key = lambda x :(-x[0], x[1]))
    if answer:
        return answer[0][2]
    else:
        return "(None)"
