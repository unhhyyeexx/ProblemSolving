import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))

def dfs(array):
    if len(array) == m:
        print(*array)
        return
    
    for i in range(1, n+1):
        if i not in array:
            array.append(i)
            dfs(array)
            array.pop()
    
dfs([])