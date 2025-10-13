/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let idx1 = m - 1;
    let idx2 = n - 1;
    let pos = m + n - 1;

    while (idx1 >= 0 && idx2 >= 0) {
        if (nums1[idx1] >= nums2[idx2]) {
            nums1[pos--] = nums1[idx1--];
        } else {
            nums1[pos--] = nums2[idx2--];
        }
    }

    while (idx2 >= 0) {
        nums1[pos--] = nums2[idx2--];
    }

};