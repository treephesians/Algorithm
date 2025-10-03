/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const outputs = [];
    nums.sort((a, b) => a - b);
    const len = nums.length;

    for (let i = 0; i < len - 2; i++) {
        const num = nums[i];
        if (i > 0 && num === nums[i - 1]) continue; // i 중복 제거

        let start = i + 1, end = len - 1;

        while (start < end) {
            const sum = num + nums[start] + nums[end];

            if (sum < 0) {
                start++;
            } else if (sum > 0) {
                end--;
            } else {
                outputs.push([num, nums[start], nums[end]]);

                // start 중복 제거
                while (start < end && nums[start] === nums[start + 1]) start++;
                // end 중복 제거
                while (start < end && nums[end] === nums[end - 1]) end--;

                start++;
                end--;
            }
        }
    }

    return outputs;
};