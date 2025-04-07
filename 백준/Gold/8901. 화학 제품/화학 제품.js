const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

function solution(a, b, c, ab, bc, ca) {
  let maxPrice = 0;
  for (let abn = 0; abn <= Math.min(a, b); abn++) {
    // ab -> bc -> ca
    let bcn = Math.min(b - abn, c);
    let can = Math.min(c - bcn, a - abn);

    let price1 = abn * ab + bcn * bc + can * ca;
    maxPrice = Math.max(maxPrice, price1);

    // ab -> ca -> bc
    can = Math.min(c, a - abn);
    bcn = Math.min(b - abn, c - can);

    let price2 = abn * ab + bcn * bc + can * ca;
    maxPrice = Math.max(maxPrice, price2);
  }

  return maxPrice;
}

let i = 0;
const T = +input[i++];
for (let t = 0; t < T; t++) {
  const [a, b, c] = input[i++].trim().split(" ").map(Number);
  const [ab, bc, ca] = input[i++].trim().split(" ").map(Number);

  console.log(solution(a, b, c, ab, bc, ca));
}