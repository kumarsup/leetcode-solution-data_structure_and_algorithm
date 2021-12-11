'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''


class Solution:
    def mergeTwoLists(self, node1: ListNode, node2: ListNode) -> ListNode:
        res = None
        new_head = None
        if not node1: return node2
        if not node2: return node1

        while node1 is not None and node2 is not None:
            node = None
            if node1.val < node2.val:
                node = node1
                node1 = node1.next
            else:
                node = node2
                node2 = node2.next
            node.next = None
            if res is None:
                res = node
                new_head = res
            else:
                res.next = node
                res = res.next

        while node1:
            if res is None:
                res = node1
                new_head = res
            else:
                res.next = node1
            node1 = node1.next
            res = res.next

        while node2:
            if res is None:
                res = node2
                new_head = res
            else:
                res.next = node2
            res = res.next
            node2 = node2.next

        return new_head