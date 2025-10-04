/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    const l1 = nums1.length;
    const l2 = nums2.length;
    const map = new Map();
    const answer = []

    for (let i = 0; i < l1; i++) {
        if (map.has(nums1[i])) map.set(nums1[i], map.get(nums1[i]) + 1);
        else map.set(nums1[i], 1);
    }

    for (let i = 0; i < l2; i++) {
        if (map.has(nums2[i]) && map.get(nums2[i]) > 0) {
            answer.push(nums2[i]);
            map.set(nums2[i], map.get(nums2[i]) - 1);
        }
    }

    return answer;
};

console.log(intersect([4,9,5], [9,4,9,8,4]));