const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const x = +input[0];
let str = input[1].trim().split("");

let n = str.length;

let cnt = 0;
let strCopy = [...str];
let strList = [];
while (true) {
  let tmp = [];
  for (let i = 1; i < n - 1; i += 2) {
    tmp.push(strCopy[i]);
    strCopy[i] = "";
  }
  strCopy = (strCopy.join("") + tmp.reverse().join("")).split("");
  cnt += 1;
  strList.push(strCopy.join(""));

  if (strCopy.join("") === str.join("")) {
    break;
  }
}

// for (let k = 0; k < x%cnt; k++) {
//   // let tmp = [];
//   // for (let i = 1; i < n - 1; i += 2) {
//   //   tmp.push(str[i]);
//   //   str[i] = "";
//   // }

//   // str = (str.join("") + tmp.reverse().join("")).split("");

// }

// console.log(str.join(""));
console.log(strList[(x - 1) % cnt]);
