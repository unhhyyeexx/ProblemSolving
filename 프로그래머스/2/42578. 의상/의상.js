function solution(clothes) {
    var answer = 1;
    var dict = {}
    for (let i=0; i<clothes.length; i++){
        if (clothes[i][1] in dict){
            dict[clothes[i][1]] += 1
        } else {
            dict[clothes[i][1]] = 1
        }
    }
    var value = Object.values(dict)
    for (let i=0; i<value.length; i++) {
        answer *= value[i]+1
    }
    
    return answer -1;
}