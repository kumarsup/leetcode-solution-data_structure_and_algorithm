'''
Given the head of a linked list, rotate the list to the right by k places.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        if not head.next: return head
        tail, n = head, 1
        while tail.next:
            tail = tail.next
            n += 1
        tail.next = head
        new_tail = head
        for i in range(n - k % n - 1): new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
