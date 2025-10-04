/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    let depth = 0;

    if (root == null) return depth;

    function dfs(root, d) {
        depth = Math.max(depth, d);
        if (root.left) dfs(root.left, d + 1);
        if (root.right) dfs(root.right, d + 1);
        return ;
    }

    dfs(root, 1);
    return depth;

};