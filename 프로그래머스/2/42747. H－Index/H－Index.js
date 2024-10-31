function solution(citations) {
    var answer = citations.length;
    citations.sort((a, b) => b-a);
    for (let i=0; i<citations.length; i++) {
        if (citations[i] <= i) {
            answer = i
            break
        }
    }
    return answer;
}