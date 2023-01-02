from collections import deque

dir = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
def solution():
    # spring
    for r in range(N):
        for c in range(N):
            tree[r][c].sort()
            for t in range(len(tree[r][c])):
                if tree[r][c][t] <= 0:
                    continue
                if nutrient[r][c] < tree[r][c][t]:
                    # summer
                    for i in range(t,len(tree[r][c])):
                        nutrient[r][c] += tree[r][c].pop()//2
                    break
                nutrient[r][c] -= tree[r][c][t]
                tree[r][c][t] += 1
    # autumn
    for r in range(N):
        for c in range(N):
            for t in tree[r][c]:
                if t % 5 :
                    continue
                for d in dir:
                    nr, nc = r+d[0], c+d[1]
                    if nr<0 or nc<0 or nr>=N or nc>=N:
                        continue
                    tree[nr][nc].insert(1, 1)
            # winter
            nutrient[r][c] += sd[r][c]



N, M, K = map(int, input().split())
tree = [[[] for _ in range(N)] for _ in range(N)]
nutrient = [[5]*N for _ in range(N)]
sd = [list(map(int, input().split())) for _ in range(N)]
result = 0
for m in range(M):
     x, y, z= map(int, input().split())
     tree[x-1][y-1].append(z)
for k in range(K):
    solution()
for r in range(N):
    for c in range(N):
        result += len(tree[r][c])
print(result)