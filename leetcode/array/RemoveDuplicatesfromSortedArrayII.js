/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let k = 0; // 유효한 원소가 저장될 위치

  for (let num of nums) {
    // 앞에서 두 개 이전 값과 같다면 skip
    if (k >= 2 && nums[k - 2] === num) continue;
    nums[k] = num;
    k++;
  }

  return k;
};