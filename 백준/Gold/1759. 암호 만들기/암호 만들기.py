from itertools import combinations

L, C = map(int, input().split())
chars = input().split()
chars.sort()
vowel = ['a', 'e', 'i', 'o', 'u']

comb = combinations(chars, L)

for c in comb:
    cntvowel = 0
    for i in c:
        if i in vowel:
            cntvowel += 1
    if 0 < cntvowel <= L-2:
        print(''.join(c))