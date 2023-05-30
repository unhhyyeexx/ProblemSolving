from collections import deque

def solution(participant, completion):
    participant = deque(sorted(participant))
    completion = deque(sorted(completion))
    
    while participant:
        now = participant.popleft()
        if completion and now  == completion.popleft():
            continue
        else:
            return now