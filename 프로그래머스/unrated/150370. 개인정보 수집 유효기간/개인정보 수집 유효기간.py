def solution(today, terms, privacies):
    answer = []
    termss = {t.split()[0]:int(t.split()[1])*28 for t in terms}
    
    ntoday = 12*28*int(today.split('.')[0]) + 28*int(today.split(".")[1]) +int(today.split(".")[2])
    
    for i, p in enumerate(privacies):
        term = termss[p[-1]]
        opendate = p[:-2]
        date = 12*28*int(opendate.split(".")[0]) + 28*int(opendate.split(".")[1]) + int(opendate.split(".")[2])
        if ntoday - date >= term:
            answer.append(i+1)
    
    return answer