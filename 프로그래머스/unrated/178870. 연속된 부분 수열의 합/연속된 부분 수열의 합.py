def solution(sequence, k):
    answer = []
    if k in sequence:
        tmp = sequence.index(k)
        return [tmp, tmp]
    n = len(sequence)
    dp = [0]*n
    dp[0] = sequence[0]
    dp[1] = sequence[1]+dp[0]
    for i in range(2, n):
        dp[i] = dp[i-1] + sequence[i]
    
    dp = [0] + dp
    front = n
    rear = n
       
    while front >= 0:
        if dp[rear] - dp[front] < k:
            front -= 1
        elif dp[rear] - dp[front] > k:
            rear -= 1
        elif dp[rear] - dp[front] == k:
            answer = [front, rear-1]
            if sequence[front] == sequence[rear-1] and sequence.count(sequence[front]) >2:
                first = sequence.index(sequence[front])
                answer = [first, first+(rear-front-1)]
                return answer
            return answer
    return answer