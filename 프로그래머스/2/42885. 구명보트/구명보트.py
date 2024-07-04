from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    q = deque(people)
    sumv = 0
    while q:
        if len(q) <= 1:
            q.pop()
        else:
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
            else:
                q.popleft()
        answer+= 1
        
    return answer


# people.sort(reverse=True)
#     people = deque(people)
#     while people:
#         if len(people) <= 1:
#             people.pop()
#         else:
#             if people[0] + people[-1] <= limit:
#                 people.pop()
#                 people.popleft()
#             else:
#                 people.popleft()

#         answer += 1