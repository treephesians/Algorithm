/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    let j = 0;
    for (let i = 0; i < haystack.length; i++) {
        for (let j = 0; j < needle.length; j++) {
            if (haystack[i + j] !== needle[j]) break;
            if (haystack[i + j] === needle[j] && j === needle.length - 1) return i;
        }
    }
    return -1;
};

// sasadbutsad, sad

// Time complextion = O(n + m)
function strStr2(haystack, needle) {
  if (needle === "") return 0;

  // 1️⃣ LPS(Longest Prefix Suffix) 배열 생성
  const lps = new Array(needle.length).fill(0);
  let len = 0; // 일치한 prefix 길이
  for (let i = 1; i < needle.length; ) {
    if (needle[i] === needle[len]) {
      lps[i++] = ++len;
    } else if (len > 0) {
      len = lps[len - 1];
    } else {
      lps[i++] = 0;
    }
  }

  // 2️⃣ haystack을 순회하면서 needle과 비교
  let i = 0; // haystack index
  let j = 0; // needle index

  while (i < haystack.length) {
    if (haystack[i] === needle[j]) {
      i++;
      j++;
      if (j === needle.length) {
        return i - j; // 패턴 전체 일치 → 시작 인덱스 반환
      }
    } else if (j > 0) {
      j = lps[j - 1]; // 이전 LPS 위치로 점프
    } else {
      i++; // j가 0이면 다음 문자로 이동
    }
  }

  return -1; // 못 찾음
}