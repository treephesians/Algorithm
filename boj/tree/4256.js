const fs = require("fs");
const input = fs.readFileSync("boj/input.txt").toString().trim().split("\n");

let index = 0;
const T = parseInt(input[index++]);

function makePostorder(preStart, inStart, inEnd, preorder, inorderIndex, postorder){
    if (inStart > inEnd) return;
    const root = preorder[preStart];
    const rootIndex = inorderIndex.get(root);
    const leftSize = rootIndex - inStart;
    
    makePostorder(preStart + 1, inStart, rootIndex - 1, preorder, inorderIndex, postorder);
    makePostorder(preStart + leftSize + 1, rootIndex + 1, inEnd, preorder, inorderIndex, postorder);
    postorder.push(root);
}

for (let i = 0; i < T; i ++){
    const n = parseInt(input[index++]);
    const preorder = input[index++].split(" ").map(Number);
    const inorder = input[index++].split(" ").map(Number);
    const inorderIndex = new Map();
    inorder.forEach((value, index) => inorderIndex.set(value, index));

    const postorder = [];
    makePostorder(0, 0, n - 1, preorder, inorderIndex, postorder)
    
    console.log(postorder.join(" "));
}