const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);

function getParent(arr, n) {
  if (arr[n] === n) return n;

  return (arr[n] = getParent(arr, arr[n]));
}

function unionParent(arr, a, b) {
  a = getParent(arr, a);
  b = getParent(arr, b);

  if (a < b) arr[b] = a;
  else arr[a] = b;
}

function findParent(arr, a, b) {
  a = getParent(arr, a);
  b = getParent(arr, b);
  if (a === b) return true;
  else return false;
}

function solution() {
  const arr = new Array(n + 1);
  for (let i = 1; i <= n; i++) {
    arr[i] = i;
  }

  for (let k = 1; k < m + 1; k++) {
    const [i, j] = input[k].trim().split(" ").map(Number);
    unionParent(arr, i, j);
  }
  const timeTable = input[m + 1].trim().split(" ").map(Number);

  let answer = 0;
  for (let i = 1; i < timeTable.length; i++) {
    if (!findParent(arr, timeTable[i], timeTable[i - 1])) {
      answer += 1;
    }
  }

  console.log(answer);
}

solution();