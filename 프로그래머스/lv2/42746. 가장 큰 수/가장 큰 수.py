def solution(numbers):
    answer = ''
    arr = []
    for n in numbers:
        arr.append(str(n))
    arr.sort(key=lambda x:x*3, reverse=True)
    for a in arr:
        answer += a
    return str(int(answer))