# from collections import deque
# def solution(queue1, queue2):
#     answer = 0
#     queue1 = deque(queue1)
#     queue2 = deque(queue2)
#     sum1 = sum(queue1)
#     sum2 = sum(queue2)
#     count = len(queue1) * 4
    
#     while True:
#         if count <0:
#         # if check1 == queue1 and check2 == queue2:
#             return -1
#         if sum1 == sum2:
#             return answer
#         elif sum1 > sum2:
#             tmp = queue1.popleft()
#             queue2.append(tmp)
#             sum2 += tmp
#             sum1 -= tmp
#             answer += 1
#         else:
#             tmp = queue2.popleft()
#             queue1.append(tmp)
#             sum1 += tmp
#             sum2 -= tmp
#             answer += 1
#         count -= 1


from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(queue1), sum(queue2)
    cnt = len(queue1) * 3
    
    while s1 != s2:
        if cnt<0 or len(q1) == 0 or len(q2) == 0 or (q1 == queue1 and q2 == queue2):
            return -1
        if s1 < s2:
            factor = q2.popleft()
            q1.append(factor)
            s1 += factor
            s2 -= factor
            answer += 1
        else:
            factor = q1.popleft()
            q2.append(factor)
            s1 -= factor
            s2 += factor
            answer += 1
        cnt -= 1
    
    return answer
