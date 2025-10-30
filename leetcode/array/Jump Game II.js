function jump(nums) {
  let jumps = 0;
  let end = 0;
  let farthest = 0;

  // 마지막 칸은 도착지이므로 n-2까지만 탐색
  for (let i = 0; i < nums.length - 1; i++) {
    farthest = Math.max(farthest, i + nums[i]);
    if (i === end) {   // 현재 점프 구간의 끝에 도달
      jumps++;
      end = farthest;
    }
  }

  return jumps;
}