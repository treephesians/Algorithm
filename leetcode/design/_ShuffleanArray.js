/**
 * @param {number[]} nums
 */
var Solution = function(nums) {
  this.original = [...nums]; // 원본 배열 저장
  this.array = [...nums];    // 현재 상태 배열
};

/**
 * @return {number[]}
 */
Solution.prototype.reset = function() {
  this.array = [...this.original]; // 원본으로 복원
  return this.array;
};

/**
 * @return {number[]}
 */
Solution.prototype.shuffle = function() {
  // Fisher–Yates 알고리즘
  for (let i = this.array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1)); // 0 ~ i 중 랜덤 인덱스
    [this.array[i], this.array[j]] = [this.array[j], this.array[i]];
  }
  return this.array;
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */