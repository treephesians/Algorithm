/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    const len = nums.length;
    let start = 0;
    let end = 1;

    while (end < len) {
        if (nums[start] !== 0) {
            start++;
            end++;
            continue;
        } 
        if (nums[end] === 0) {
            end++;
            continue;
        }
        [nums[start], nums[end]] = [nums[end], nums[start]];
    }
    return nums;
};

const nums = [1,2,0,4,2,0,1,1,0,0,0,1,2,3];
console.log(moveZeroes(nums));