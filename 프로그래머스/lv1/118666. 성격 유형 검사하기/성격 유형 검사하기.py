def solution(survey, choices):
    answer = 'RCJA'
    type = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i, choice in enumerate(choices):
        if choice < 4:
            type[survey[i][0]] += (4-choice)
        elif choice > 4:
            type[survey[i][1]] += (choice-4)
        else:
            continue
    if type['R'] < type['T']:
        answer = 'T' + answer[1:]
    if type['C'] < type['F']:
        answer = answer[0] + 'F' + answer[2:]
    if type['J'] < type['M']:
        answer = answer[0:2] + 'M' + answer[-1]
    if type['A'] < type['N']:
        answer =  answer[:-1] + 'N'

    return answer