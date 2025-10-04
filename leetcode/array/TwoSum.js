/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const len = nums.length;

    for (let i = 0; i < len; i++) {
        nums[i] = [nums[i], i];
    }

    nums.sort((a, b) => a[0] - b[0]);

    let start = 0;
    let end = len - 1;

    while (start < end) {
        if (nums[start][0] + nums[end][0] === target) return [nums[start][1], nums[end][1]];
        if (nums[start][0] + nums[end][0] < target) {
            start++;
        } else {
            end--;
        }
    }

    return null;
    
};

const nums = [2, 7, 11, 15];
const target = 9;

console.log(twoSum(nums, target));