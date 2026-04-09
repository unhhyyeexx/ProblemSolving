import sys
input = sys.stdin.readline

n = int(input())

answer = 0
row = [0] * n #[i,j]에 퀸이 있다면 row[i] = j

def is_promising(x):
    for i in range(x): # 앞쪽부터 퀸을 놓으니까 현재 시점의 위만 보면 된다.
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    
    return True

def rcs(x):
    global answer
    
    if x == n:
        answer += 1
        return
    
    else:
        for i in range(n):
            # [x, i]에 퀸 놓겠음
            row[x] = i
            if is_promising(x):
                rcs(x+1)

rcs(0)
print(answer)