import sys
input = sys.stdin.readline

def dfs(v): # v는 트리에서 지울 녀석
    tree[v] = -2 #지우면 -2로 바꿈
    for i in range(n):
        # 지우고자 하는 애 == tree[i]이면 tree[i]는 v의 자식
        if v == tree[i]:
            # 자식인 친구의 자식도 싹 지운다.
            dfs(i)
    return

n = int(input())
tree = list(map(int, input().split()))
target = int(input())

dfs(target)

answer = 0
for i in range(n):
    # 지워진 노드가 아니고, tree안에 해당 i의 자식이 없으면
    if tree[i] != -2 and i not in tree:
        answer += 1

print(answer)