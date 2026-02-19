function solution(schedules, timelogs, startday) {
    let answer = 0;
    const n = schedules.length
    const newTimelogs = [];
    const sat = startday!==7 ? 7-startday-1 : 6;
    const sun = 7-startday;
    for (let j=0; j<n; j++) {
        const timelog = timelogs[j]
        const originalTime = schedules[j] + 10
        const limitTime = originalTime%100 >= 60 ? originalTime+40 : originalTime
        let flag = true
        for (let i=0; i<7; i++) {
            if (i === sat || i ===sun) continue

            if (timelog[i] > limitTime){
                flag = false;
                break;
            }
        }
        if (flag) answer++
    }
    return answer;
}