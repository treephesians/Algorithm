function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let temp = null;
    let curr = head;
    //null -> 1 -> 2 -> 3
    while (curr) {
        let nextNode = curr.next;
        curr.next = temp;
        temp = curr;
        curr = nextNode;
    }
    
    return temp;
};