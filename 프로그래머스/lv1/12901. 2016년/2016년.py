def solution(a, b):
    answer = ''
    yoil = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(1, 13):
        days[i] = days[i-1] + days[i]
    answer = yoil[(days[a-1] + b) % 7]
    return answer