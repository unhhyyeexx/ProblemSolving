const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const infix = input[0].trim().split("");
let answer = "";

const stack = [];
while (infix.length > 0) {
  const now = infix.shift();

  if (now === "(") {
    stack.push("(");
  } else if (now === ")") {
    while (stack.length > 0 && stack[stack.length - 1] !== "(") {
      answer += stack.pop();
    }
    stack.pop(); // ( 빼주기
  } else if (now === "+" || now === "-") {
    while (stack.length > 0 && stack[stack.length - 1] !== "(") {
      answer += stack.pop();
    }
    stack.push(now);
  } else if (now === "*" || now === "/") {
    while (
      stack.length > 0 &&
      (stack[stack.length - 1] === "*" || stack[stack.length - 1] === "/")
    ) {
      answer += stack.pop();
    }
    stack.push(now);
  } else {
    answer += now;
  }
}

while (stack.length > 0) {
  answer += stack.pop();
}
console.log(answer);
