/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    nums.reverse();
    k %= nums.length;
    reverseRange(nums, 0, k - 1);
    reverseRange(nums, k, nums.length - 1);

};

function reverseRange(arr, start, end) {
    while (start < end) {
        [arr[start], arr[end]] = [arr[end], arr[start]];
        start++;
        end--;
    }
}