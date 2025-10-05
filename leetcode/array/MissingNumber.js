/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    return nums.length * (nums.length + 1) / 2 - nums.reduce((acc, val) => acc + val, 0);
};

console.log(missingNumber([9,6,4,2,3,5,7,0,1]));
// Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

// Input: nums = [9,6,4,2,3,5,7,0,1]
// Output: 8