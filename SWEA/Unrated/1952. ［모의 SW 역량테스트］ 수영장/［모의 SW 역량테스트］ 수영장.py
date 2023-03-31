def solution(prices, plans):
    d, m, t, y = prices
    costs = [0]*13
    
    for i in range(1, 13):
        costs[i] = min(plans[i-1]*d, m) + costs[i-1]
        if i > 2:
            costs[i] = min(costs[i], t+costs[i-3])
    
    answer = min(costs[12], y)
    return answer

for tc in range(1, int(input())+1):
    prices = map(int, input().split())
    plans = list(map(int, input().split()))

    print(f'#{tc} {solution(prices, plans)}')