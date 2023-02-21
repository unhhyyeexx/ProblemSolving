from collections import defaultdict

def solution(str1, str2):
    answer = 0
    
    a, b = defaultdict(int), defaultdict(int)
    for i in range(0, len(str1)-1):
        if str1[i:i+2].isalpha():
            a[str1[i:i+2].lower()] += 1
    for i in range(0, len(str2)-1):
        if str2[i:i+2].isalpha():
            b[str2[i:i+2].lower()] += 1
    
    if not a and not b:
        return 65536
    
    if not a or not b:
        return 0
    
    total, same = 0, 0
    for key, value in a.items():
        if key in b:
            same += (min(value, b[key]))
            total += (max(value, b[key]))
        else:
            total += value
    for key, value in b.items():
        if not key in a:
            total += value
    
    answer = int((same/total)*65536)
    return answer