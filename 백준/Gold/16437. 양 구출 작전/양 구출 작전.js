const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const graph = [];
for (let i = 1; i < n; i++) {
  graph.push(input[i].trim().split(" "));
}

function dfs(now) {
  let sCnt = 0;
  for (let next of tree[now]) {
    sCnt += dfs(next);
  }
  if (info[now][0] === "W") {
    sCnt -= info[now][1];
    if (sCnt < 0) sCnt = 0;
  } else {
    sCnt += info[now][1];
  }

  return sCnt;
}

let info = [[], [0, 0]];
let tree = Array.from({ length: n + 1 }, () => []);

graph.forEach((el, i) => {
  const [t, a, p] = el;
  info.push([t, +a]);
  tree[+p].push(i + 2);
});

console.log(dfs(1));
