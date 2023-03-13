function check(num) {
    var divisors = [];
    for (let i=1; i <=Math.sqrt(num); i++) {
        if (num % i === 0) {
            divisors.push(i);
            if (num / i != i) {
                divisors.push(num/i);
            }
        }
    }
    return divisors.length
}

function solution(left, right) {
    var answer = 0;
    for (let n=left; n<=right; n++ ){
        if (check(n) % 2 === 0) {
            answer += n
        } else {
            answer -= n
        }
    }
    return answer;
}