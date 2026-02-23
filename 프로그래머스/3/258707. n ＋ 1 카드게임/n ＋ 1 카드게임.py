from collections import deque 

def makeval(d1, d2, val):
    newd2 = set(d2)
    for card in d1:
        if val - card in newd2:
            d1.remove(card)
            d2.remove(val-card)
            return True
    return False

def solution(coin, cards):
    answer = 0
    n = len(cards)
    val = n+1
    q = deque(cards[n//3:])
    pending = []
    my = cards[:n//3]
        
    while coin >= 0 and q:
        pending.append(q.popleft())
        pending.append(q.popleft())
        
        if makeval(my, my, val):
            pass
        elif coin >= 1 and makeval(my, pending, val):
            coin -= 1
        elif coin >= 2 and makeval(pending, pending, val):
            coin -= 2
        else:
            break
        answer += 1
                
    return answer + 1