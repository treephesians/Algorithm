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
 * @return {boolean}
 */
var isValidBST = function(root) {

    if (!root) return false;

    let answer = true;

    function dfs(root) {
        if (root.left) {
            if (root.left.val >= root.val) {
                answer = false;
                return ;
            }
            dfs(root.left);
        };
        if (root.right){
            if (root.val >= root.right.val) {
                answer = false;
                return ;
            }
            dfs(root.right);
        }
    }

    dfs(root);

    return answer;

};