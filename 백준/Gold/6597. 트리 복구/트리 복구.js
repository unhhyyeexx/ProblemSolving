const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

function solution() {
    
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
        var [preorder, inorder] = input[i].split(' ');
        var idx = 0;
        var res = '';
        postorder(inorder);
        console.log(res);
    }
}

solution();