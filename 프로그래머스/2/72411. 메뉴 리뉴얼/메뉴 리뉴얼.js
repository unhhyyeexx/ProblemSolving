
function getcombi(arr, r) {
    const result = []
    if (r === 1) return arr.map(value => [value])
    
    arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1)
        const combinations = getcombi(rest, r-1)
        const attached = combinations.map(combination => [fixed, ...combination])
        result.push(...attached)
    })
    
    return result
}

function solution(orders, course) {
    var answer = [];
    const maxNum = Array(11).fill(0)
    const orderMap = new Map()
    for (const order of orders) {
        for (const n of course) {
            const newCombi = getcombi([...order], n).sort((a, b) => a-b)
            for (const nc of newCombi) {
                const sortednc = nc.sort()
                const joinnc = sortednc.join("")
                orderMap.set(joinnc, (orderMap.get(joinnc) || 0) + 1 )
                if (orderMap.get(joinnc) > 1) {
                    maxNum[joinnc.length] = Math.max(maxNum[joinnc.length], orderMap.get(joinnc))
                }
            }
        }
    }
    
    for (const [k, v] of orderMap){
        if (v > 1 && v === maxNum[k.length]) {
            answer.push(k)
        }
    }
    answer.sort()
    return answer;
}