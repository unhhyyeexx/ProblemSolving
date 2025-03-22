const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const t = +input[0];
let idx = 1;
while (idx < input.length) {
  const [n, m] = input[idx].trim().split(" ").map(Number);
  const queue = [];
  for (let i = idx + 1; i < idx + n; i++) {
    const [node2, cost] = input[i].trim().split(" ").map(Number);
    queue.push([cost, i - idx, node2]);
  }
  idx += n;

  let answers = [];
  for (let i = idx; i < idx + m; i++) {
    const [n1, n2, cost] = input[i].trim().split(" ").map(Number);
    queue.push([cost, n1, n2]);
    queue.sort((a, b) => a[0] - b[0]);
    let parents = Array(n)
      .fill(0)
      .map((_, idx) => idx);
    answers.push(kruskal(n, queue, parents));
  }
  idx += m;

  // xor 하기기
  let realAnswer = answers[0];
  for (let a = 1; a < answers.length; a++) {
    realAnswer ^= answers[a];
  }

  console.log(realAnswer.toString());
}

function kruskal(n, queue, parents) {
  let total = 0n;
  let edgeCnt = 0;

  for (const [cost, n1, n2] of queue) {
    if (union(n1, n2, parents)) {
      total += BigInt(cost);
      edgeCnt += 1;
      if (edgeCnt === n - 1) {
        return total;
      }
    }
  }
  return -1;
}

function union(n1, n2, parents) {
  let a = find(n1, parents);
  let b = find(n2, parents);

  if (a === b) {
    return false;
  } else if (a < b) {
    parents[b] = a;
  } else {
    parents[a] = b;
  }
  return true;
}

function find(node, parents) {
  if (parents[node] === node) {
    return node;
  } else {
    return (parents[node] = find(parents[node], parents));
  }
}
