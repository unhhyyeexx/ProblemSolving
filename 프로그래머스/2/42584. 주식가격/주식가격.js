function solution(prices) {
    var answer = [];
    for(let i=0; i<prices.length-1; i++){
        let time = 0;
        let a = prices[i];
        for (let j=i+1; j<prices.length; j++){
            time++
            if (a <= prices[j]) {
                if (j===prices.length-1) {
                    answer.push(time)
                    break
                }
            }else{
                answer.push(time)
                break
            }
        }
    }
    answer.push(0)
    return answer;
}