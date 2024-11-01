function solution(brown, yellow) {
    
    let brownSum = (brown+4)/2; // 갈색 가로 세로 하나씩 더한 크기
    for (let i=1; i<= Math.floor(brownSum/2); i++) {
        const j = brownSum - i;
        if ((i-2) * (j-2) === yellow){
            return [j, i]
        }
    }

}