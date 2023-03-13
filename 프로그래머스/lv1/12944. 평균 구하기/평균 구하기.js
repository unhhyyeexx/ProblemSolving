function solution(arr) {
    var answer = 0;
    var total = 0;
    for (n of arr) {
        total += n
    }
    answer = total / arr.length
    return answer;
}