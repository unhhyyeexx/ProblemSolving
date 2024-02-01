import sys
input = sys.stdin.readline
from collections import deque

def maketree(sg, tree, root):
    if (root < 1) or (2**k <= root) or (tree[root] != 0):
        return
    maketree(sg, tree, 2*root) # 왼쪽 자식 노드 탐색
    tree[root] = sg.popleft()
    maketree(sg, tree, 2*root+1) # 오른쪽 자식 노드 탐색

    return

k = int(input())
sg = list(map(int, input().split()))
sg = deque(sg)
tree = [0 for _ in range(2**k)]

maketree(sg, tree, 1)
i = 1
while i < 2**k:
    for j in range(i, i*2):
        print(tree[j], end=' ')
    print()
    i *= 2
