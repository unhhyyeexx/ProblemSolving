function solution(name) {
    let answer = 0;
    const n = name.length
    let move = n -1
    for (let i=0; i<n; i++) {
        const s = name[i]
        answer += Math.min(s.charCodeAt() - 'A'.charCodeAt(), 'Z'.charCodeAt() - s.charCodeAt() + 1)
        
        let next = i+1
        while (next < n && name[next] == 'A') {
            next += 1
        }
        
        move = Math.min(move, 2*i + n - next, i + 2*(n-next))
    }
    
    answer += move
    return answer;
}