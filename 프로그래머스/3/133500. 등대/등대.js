function solution(n, lighthouse) {
    const graph = Array.from({ length: n + 1 }, () => []);
    const visited = Array(n + 1).fill(false);
    const lightUp = Array(n + 1).fill(false);

    // 그래프 구성
    for (const [a, b] of lighthouse) {
        graph[a].push(b);
        graph[b].push(a);
    }

    // DFS - 반복문 기반 (post-order 방식)
    const stack = [[1, null, 0]]; // [현재 노드, 부모 노드, 방문 단계 (0: 방문 전, 1: 자식 처리 후)]
    const postOrder = [];

    while (stack.length > 0) {
        const [cur, parent, step] = stack.pop();

        if (step === 0) {
            stack.push([cur, parent, 1]); // 후위 순회를 위해 다시 push
            for (const next of graph[cur]) {
                if (next !== parent) {
                    stack.push([next, cur, 0]);
                }
            }
        } else {
            postOrder.push([cur, parent]);
        }
    }

    // 후위 순회 결과를 바탕으로 필요한 노드에 불 켜기
    for (const [cur, parent] of postOrder) {
        let needLight = false;

        for (const next of graph[cur]) {
            if (next !== parent && !lightUp[next]) {
                needLight = true;
                break;
            }
        }

        if (needLight) {
            lightUp[cur] = true;
        }
    }

    // true인 개수 세기
    return lightUp.filter(Boolean).length;
}