 function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
 }
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    if (!preorder.length) return;
    const num = preorder.shift();
    const root = new TreeNode(num);
    if (inorder.length == 1) return root;
    const numId = inorder.indexOf(num);
    root.left = buildTree(preorder, inorder.slice(0,numId));
    root.right = buildTree(preorder, inorder.slice(numId + 1, inorder.length));
    return root;
};