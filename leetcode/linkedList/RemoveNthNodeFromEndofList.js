/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    // 가상의 노드(dummy) 사용: edge case 제거
    let dummy = new ListNode(0);
    dummy.next = head;
    
    let fast = dummy;
    let slow = dummy;
    
    // fast 포인터를 n+1 칸 이동
    for (let i = 0; i <= n; i++) {
        fast = fast.next;
    }
    
    // fast가 끝에 도달할 때까지 slow도 같이 이동
    while (fast !== null) {
        fast = fast.next;
        slow = slow.next;
    }
    
    // slow.next 제거
    slow.next = slow.next.next;
    
    return dummy.next;
};