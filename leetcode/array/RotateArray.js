/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    const len = nums.length;
    k %= len;

    function reverse(start, end) {
        while (start < end) {
            [nums[start], nums[end]] = [nums[end], nums[start]];
            start++;
            end--;
        }
    }

    reverse(0, len - 1);
    reverse(0, k - 1);
    reverse(k, len - 1);
    console.log(nums);
};

rotate([1,2,3,4,5,6,7], 3);