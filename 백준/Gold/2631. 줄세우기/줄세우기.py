n = int(input())
student = list(int(input()) for _ in range(n))

dp = [student[0]]

for i in range(1,n):
    if student[i] > dp[-1]:
        dp.append(student[i])
    else:
        for d in range(len(dp)):
            if dp[d] > student[i]:
                dp[d] = student[i]
                break
print(n-len(dp))