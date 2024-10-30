function solution(participant, completion) {
    var answer = '';
    participant.sort();
    completion.sort();
    console.log(participant)
    console.log(completion)
    for (let i=0; i<participant.length; i++) {
        if (completion.length < i+1){
            return participant[i]
        } else if (participant[i] !== completion[i]){
            return participant[i]
        }
    }
    return answer;
}