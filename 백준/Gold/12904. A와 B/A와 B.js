const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const s = input[0].trim().split("");
let t = input[1].trim().split("");

function solution() {
  while (s.length !== t.length) {
    if (t[t.length - 1] === "A") {
      t.pop();
    } else if (t[t.length - 1] === "B") {
      t.pop();
      t = t.reverse();
    }
  }

  if (JSON.stringify(s) === JSON.stringify(t)) {
    console.log(1);
  } else {
    console.log(0);
  }
}

solution();