def checkleftn(char, lenarray, dic, n):
    seq = 0
    L = len(char)
    for i in range(L):
        seq += lenarray[L-i-1]*dic[char[i]]
    return seq <= n

def makechar(n, lenarray):
    result = ''
    arr = 'abcdefghijklmnopqrstuvwxyz'
    
    while n > 0:
        n -= 1
        result = arr[n%26] + result
        n //= 26

    return result
    
def solution(n, bans):
    answer = ''
    bans.sort(key=lambda x: (len(x), x))
    lenarray = [26**i for i in range(12)]
    dic = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, 't':20, 'u':21, "v":22, "w":23, "x":24, "y":25, "z":26}

    for ban in bans:
        if checkleftn(ban, lenarray, dic, n):
            n += 1
    
    answer = makechar(n, lenarray)
    return answer