function solution(N, number) {
    if (N===number) return 1;
    
    var answer = 0;
    var dp = Array.from(new Array(9), ()=> new Set());
    
    dp.forEach((el, idx) => {
        if (idx !== 0) {
            el.add(Number(String(N).repeat(idx)));
        }
    })
    
    for (let i=1; i<=8; i++) {
        for (let j=1; j<i; j++) {
            for (a of dp[j]) {
                for (b of dp[i-j]) {
                    dp[i].add(a+b);
                    dp[i].add(a-b);
                    dp[i].add(a*b);
                    dp[i].add(a/b);
                }
            }
        }
        if (dp[i].has(number)) return i;
    }
    return -1;
    
    return answer;
}