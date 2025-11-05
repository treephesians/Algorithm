/**
 * @param {number[]} citations
 * @return {number}
 */
function hIndex(citations) {
  citations.sort((a, b) => a - b);
  const n = citations.length;

  for (let i = 0; i < n; i++) {
    const h = n - i; // 남은 논문 수
    if (citations[i] >= h) {
      return h;
    }
  }
  return 0;
}