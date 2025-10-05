/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    dp = Array(nums.length);
    for (let i = 0; i < nums.length; i++) {
        if (i == 0 || i == 1) {
            dp[i] = nums[i];
            continue;
        };
        if (i == 2) {
            dp[i] = dp[i - 2] + nums[i];
            continue;
        }
        dp[i] = nums[i] + Math.max(dp[i - 2], dp[i - 3]);
    }
    return Math.max(...dp);
};

const nums = [2,7,9,3,1,4,5,6];
// dp = [2, 7, 11, 10, 12, 15, 17, 21];
console.log(rob(nums));
