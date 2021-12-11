'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the
list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
'''


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head: return head
        if not head.next: return head
        count, last, start, curr = 1, head, head, head

        while curr and count != left:
            last = curr
            curr = curr.next
            count += 1
        start = curr

        prev = last
        next = None
        while curr and prev and count != right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if start:
            start.next = prev

        last.next = prev

        return head