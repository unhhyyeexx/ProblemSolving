def solution():
    for num in nums:
        cipher = 1
        for n in num[::-1]:
            idx = alphabet.find(n)
            imp[idx] += cipher
            cipher *= 10
    imp.sort(reverse=True)

    answer =  0
    numbers = [9,8,7,6,5,4,3,2,1]
    for i in range(9):
        answer += (imp[i] * numbers[i])
    return answer

N = int(input())
nums = [list(input()) for _ in range(N)]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
imp = [0]*26

print(solution())