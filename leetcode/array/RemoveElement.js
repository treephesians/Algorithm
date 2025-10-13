/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let k = 0; // val이 아닌 값을 저장할 위치

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== val) {
      nums[k] = nums[i]; // val이 아닌 값만 앞으로 이동
      k++;
    }
  }

  return k;
};