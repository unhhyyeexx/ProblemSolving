function solution(price, money, count) {
    var answer = 0;
    var multi = 0;
    for (let i=1; i<=count; i++){
        multi += i
    }
    answer = (price*multi) - money
    if (answer>0) return answer

    return 0;
}