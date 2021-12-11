'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a
multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 3:
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 4:
Input: head = [1], k = 1
Output: [1]

Constraints:
The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz

Follow-up: Can you solve the problem in O(1) extra memory space?
'''


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None: return head
        node, curr, prev, length = head, head, None, 0
        while node:
            length += 1
            node = node.next

        while True:
            i = 0
            last_node_of_prev_sub_list = prev
            last_node_of_curr_sub_list = curr
            next = None
            while curr and i < k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                i += 1

            length -= k
            if last_node_of_prev_sub_list is not None:
                last_node_of_prev_sub_list.next = prev
            else:
                head = prev

            last_node_of_curr_sub_list.next = curr
            if curr is None:
                break
            prev = last_node_of_curr_sub_list

            if length < k:
                break

        return head