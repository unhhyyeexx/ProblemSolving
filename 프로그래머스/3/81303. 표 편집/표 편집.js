function solution(n, k, cmds) {
    let linkedList = {}
    for (let i=0; i<n; i++) {
        linkedList[i] = [i-1, i+1]
    }
    const table = Array(n).fill('O')
    const del = []
    
    for (let cmd of cmds) {
        cmd = cmd.split(' ')
        
        if (cmd[0] === 'D') {
            for (let i=0; i<Number(cmd[1]); i++) {
                k = linkedList[k][1]
            }
        } else if (cmd[0] === 'U') {
            for (let i=0; i<Number(cmd[1]); i++) {
                k = linkedList[k][0]
            }
        } else if (cmd[0] === 'C') {
            const [prev, nxt] = linkedList[k]
            table[k] = 'X'
            del.push([prev, k, nxt])
            
            if (nxt === n) {
                k = linkedList[k][0]
            } else {
                k = linkedList[k][1]
            }
            
            if (prev === -1) {
                linkedList[nxt][0] = prev
            } else if (nxt === n) {
                linkedList[prev][1] = nxt
            } else {
                linkedList[prev][1] = nxt
                linkedList[nxt][0] = prev
            }
        } else {
            const [prev, now, nxt] = del.pop()
            table[now] = 'O'
            
            if (prev === -1) {
                linkedList[nxt][0] = now
            } else if (nxt === n) {
                linkedList[prev][1] = now
            } else {
                linkedList[prev][1] = now
                linkedList[nxt][0] = now
            }
        }
    }
    
    return table.join("")
}