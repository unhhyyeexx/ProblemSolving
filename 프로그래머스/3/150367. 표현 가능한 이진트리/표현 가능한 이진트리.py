def fillzero(strBin):
    L = len(strBin)
    size = 1
    while size < L + 1:
        size *= 2
    return strBin.zfill(size-1)

def dfs(tree):
    if len(tree) == 1: 
        return True
    
    mid = len(tree) // 2
    root = tree[mid]
    
    left = tree[:mid]
    right = tree[mid+1:]
    
    if root == '0':
        if '1' in left or '1' in right:
            return False
    
    return dfs(left) and dfs(right)

def solution(numbers):
    answer = []
    
    for n in numbers:
        strBin = bin(n)[2:]
        zeroBin = fillzero(strBin)
        answer.append(1 if dfs(zeroBin) else 0)
    return answer