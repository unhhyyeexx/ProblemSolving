function solution(absolutes, signs) {
    var answer = 0;
    for (i in absolutes){
        if (signs[i] === true) {
            answer += absolutes[i]
        } else {
            answer -= absolutes[i]
        }
    }
    return answer;
}