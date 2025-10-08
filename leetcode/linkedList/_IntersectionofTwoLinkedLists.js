/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
  if (!headA || !headB) return null;

  let pA = headA;
  let pB = headB;

  // 두 포인터가 만날 때까지 순회
  while (pA !== pB) {
    // 끝에 도달하면 반대쪽 리스트로 이동
    pA = pA ? pA.next : headB;
    pB = pB ? pB.next : headA;
  }

  return pA; // 교차점 노드 or null
};