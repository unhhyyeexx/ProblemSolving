def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0,0,0]
    
    for i, ans in enumerate(answers):
        if ans == one[i%5]:
            score[0] += 1
        if ans == two[i%8]:
            score[1] += 1
        if ans == three[i%10]:
            score[2] += 1
    
    max_v = max(score)
    for i, sc in enumerate(score):
        if sc == max_v:
            answer.append(i + 1)
    
    return answer