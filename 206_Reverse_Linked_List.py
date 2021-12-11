'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head

        def recursive(node):
            if not node.next: return node
            last = recursive(node.next)
            node.next.next = node
            node.next = None
            return last

        return recursive(head)

    #         if not head: return head

    #         def recursive(node):
    #             if not node.next: return node
    #             last = recursive(node.next)
    #             node.next.next = node
    #             node.next = None
    #             return last
    #         return recursive(head)

    #         if not head: return None
    #         prev = None
    #         curr = head
    #         nxt = curr.next

    #         while nxt:
    #             curr.next = prev
    #             prev = curr
    #             curr = nxt
    #             nxt = curr.next
    #         curr.next = prev
    #         return curr