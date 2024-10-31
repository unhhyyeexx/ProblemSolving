function solution(array, commands) {
    var answer = [];
    for (let i=0; i<commands.length; i++) {
        let a = commands[i][0], b = commands[i][1], c = commands[i][2];
        const newArr = (array.slice(a-1, b));
        newArr.sort((x, y) => x-y)
        answer.push(newArr[c-1])
    }
    return answer;
}