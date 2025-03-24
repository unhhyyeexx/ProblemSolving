const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 총 블럭 수 - ( 지지대-펭귄 최단거리 2개 블럭개수 + 펭귄서있는 블럭 1개개)
const [n, s, p] = input[0].trim().split(" ").map(Number);
const tree = Array.from({ length: n + 1 }, () => []);

for (let i = 1; i < n; i++) {
  const [a, b] = input[i].trim().split(" ").map(Number);
  tree[a].push(b);
  tree[b].push(a);
}

const visit = Array(n + 1).fill(false);
let distances = [];

function dfs(node, cur) {
  visit[node] = true;
  if (node === p) {
    visit[p] = false;
    if (distances.length <= 1) {
      distances.push(cur);
      distances.sort((a, b) => a - b);
    } else {
      const maxIdx = distances.indexOf(Math.max(...distances));
      if (cur < distances[maxIdx]) {
        distances[maxIdx] = cur;
      }
    }
    return;
  }
  for (const next of tree[node]) {
    if (!visit[next]) {
      dfs(next, cur + 1);
    }
  }
}

for (let i = 1; i < s + 1; i++) {
  if (!visit[i] && i !== p) {
    dfs(i, 0);
  }
}

const distSum = distances.reduce((a, b) => a + b, 0);
console.log(n - distSum - 1);