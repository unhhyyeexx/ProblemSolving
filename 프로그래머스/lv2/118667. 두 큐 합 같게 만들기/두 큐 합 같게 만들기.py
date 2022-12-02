from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    count = (len(queue1) + len(queue2)) * 2 
    
    while True:
        if count <0:
        # if check1 == queue1 and check2 == queue2:
            return -1
        if sum1 == sum2:
            return answer
        elif sum1 > sum2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum2 += tmp
            sum1 -= tmp
            answer += 1
        else:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
            answer += 1
        count -= 1
