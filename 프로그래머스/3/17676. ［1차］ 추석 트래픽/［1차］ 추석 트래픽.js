function solution(lines) {
    var answer = 0;
    const log = []
    
    for (const line of lines) {
        let [date, s, t] = line.split(" ")
        s = s.split(":")
        t = t.split("s")[0]
        
        end = (Number(s[0])* 3600 + Number(s[1]) * 60 + Number(s[2])) * 1000 // msec
        start = end - (Number(t) * 1000) + 1 // 끝 시간 포함이므로 + 1
        log.push([start, end])
    }
    
    // 초당 처리량
    function throughput(log, start, end) {
        // start : 초당 처리량을 계산할 시점, end : start + 1000 (1초)
        let cnt = 0
        for (const [s, e] of log) {
            if (s < end && e >= start) { 
                // 어떤 요청의 시작시간(s)이 end 보다 작고, 끝 시간(e)이 start 보다 크면 해당 시점에 요청 진행중
                cnt += 1
            }
        }
        return cnt
    }
    
    for (const [s, e] of log) {
        answer = Math.max(answer, throughput(log, s, s+1000), throughput(log, e, e+1000))
    }
    
    return answer;
}