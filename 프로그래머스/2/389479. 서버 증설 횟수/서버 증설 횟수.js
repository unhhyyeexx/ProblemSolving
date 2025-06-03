function solution(players, m, k) {
    var answer = 0;
    const n = players.length
    let server = new Array(n).fill(0)
    
    for (let i=0; i<n; i++) {
        if (i>0) {
            server[i] += server[i-1]
        }
        let need = Math.floor(players[i]/m) - server[i]
        if (need > 0) {
            answer += need
            server[i] += need
            if (i+k < n) {
                server[i+k] -= need
            }
        }
    }
    
    return answer;
}
