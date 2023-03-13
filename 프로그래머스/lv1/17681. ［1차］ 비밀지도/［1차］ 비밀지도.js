function solution(n, arr1, arr2) {
    var answer = [];
    for (let i=0; i<n; i++) {
        const bin = (arr1[i] | arr2[i]).toString(2);
        let tmp = [];
        console.log(bin)
        for(let b=bin.length-n; b<bin.length; b++){
            if (bin[b] === '1'){
                tmp.push('#');
            } else{
                tmp.push(' ');
            }
        }
        answer.push(tmp.join(''));
    }
    
    return answer;
}