function solution(number) {
    var answer = 0;
    
    const combi = (current, start) => {
        if (current.length === 3) {
            answer += current.reduce((acc, cur) => acc + cur, 0) === 0 ? 1 : 0;
            return;
        }
        for (let i=start; i<number.length; i++) {
            combi([...current, number[i]], i+1);
        }
    }
    combi([], 0)
    return answer;
}