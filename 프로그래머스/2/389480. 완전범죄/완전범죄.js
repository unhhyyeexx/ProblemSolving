function solution(info, n, m) {
    let min = Infinity;
    const memo = new Set();

    const dfs = (idx, a, b) => {
        if(idx === info.length) {
            min = Math.min(min, a);
            return;
        }

        const key = `${idx}-${a}-${b}`
        if(memo.has(key)) {
            return;
        }
        memo.add(key);

        const newA = a + info[idx][0];
        const newB = b + info[idx][1];

        if(newA < n && newA < min) {
            dfs(idx + 1, newA, b);
        }

        if(newB < m) {
            dfs(idx + 1, a, newB);
        }
    }

    dfs(0, 0, 0);

    return min === Infinity ? -1 : min;
}