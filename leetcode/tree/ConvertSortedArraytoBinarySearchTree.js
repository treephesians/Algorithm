function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    const makeBST = (nums) => {
        if (!nums.length) return null;
        const node = new TreeNode();
        const mid = Math.floor(nums.length / 2);
        node.val = nums[mid];
        node.left = makeBST(nums.slice(0, mid));
        node.right = makeBST(nums.slice(mid + 1, nums.length));
        return node;
    }

    return makeBST(nums);
};

// Input: nums = [-10,-3,0,5,9]
// Output: [0,-3,9,-10,null,5]
// Explanation: [0,-10,5,null,-3,null,9] is also accepted: