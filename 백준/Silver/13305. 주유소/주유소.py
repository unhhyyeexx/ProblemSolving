import sys
input = sys.stdin.readline

def solution(n, dist, price):
    answer = 0
    i = 0
    min_price = 1e9
    while True:
        if i >= n-1:
            break
        now_price = price[i]
        if now_price >= min_price:
            answer += min_price * dist[i]
        if now_price < min_price:
            min_price = now_price
            answer += min_price * dist[i]
        i += 1
        
    return answer

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

print(solution(n, dist, price))