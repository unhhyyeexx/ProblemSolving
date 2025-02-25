const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

function solution() {
  let answer;
  let preorder;
  let inorder;
  let idx;
    
  function postorder(order) {
      if (order === '') return;
      const temp = preorder[idx];
      const [left, right] = order.split(preorder[idx]);
      idx += 1;
      postorder(left);
      postorder(right);
      res += temp;
  }
  
  for (let i=0; i<input.length-1; i++) {
      [preorder, inorder] = input[i].split(' ');
      idx = 0;
      res = '';
      postorder(inorder);
      console.log(res);
  }
}

solution();