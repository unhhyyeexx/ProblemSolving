function solution(numbers) {
    var answer = 0;
    var check = [0,1,2,3,4,5,6,7,8,9]
    for (n of numbers) {
        if (check.includes(n)) {   
            check.splice(check.indexOf(n), 1);
        }
    }
    answer = check.reduce((a,b) => a+b, 0)
    return answer;
}