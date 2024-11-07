function solution(k, tangerine) {
    var answer = 0;
    const dic = {};
    tangerine.forEach((el) => dic[el]  = (dic[el] || 0) + 1)
    const arr = Object.values(dic).sort((a, b)=> b-a);
    for (const a of arr) {
        answer++;
        if (k > a) k -= a;
        else break;
    }
    return answer;
}