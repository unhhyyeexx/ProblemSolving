function solution(n, m) {
    // 공약수
    var gcd = 1;
    for (let i=2; i<=Math.min(n,m); i++){
        if(n%i===0 && m%i===0){
            gcd = i;
        }
    }
    // 공배수
    var lcm = 1;
    while (true) {
        if(lcm%n===0 && lcm%m===0){
            break;
        }
        lcm++;
    }
    return [gcd, lcm];
}