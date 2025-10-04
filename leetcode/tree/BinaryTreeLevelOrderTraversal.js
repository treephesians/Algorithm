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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    if (!root) return [];
    const answer = []
    const dfs = (node, level) => {
        if (!node) return;
        if (answer.length == level) answer.push([]);
        answer[level].push(node.val);
        dfs(node.left, level + 1);
        dfs(node.right, level + 1);
    }
    dfs(root);
    return answer;
};