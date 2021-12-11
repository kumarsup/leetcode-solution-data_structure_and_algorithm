'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes
first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

Follow up: Could you solve it without reversing the input lists?
'''


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1: return l2
        if not l2: return l1

        stack1, stack2 = [], []

        curr = l1
        while curr:
            stack1.append(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            stack2.append(curr.val)
            curr = curr.next
        carry, res = 0, []

        while len(stack1) > 0 and len(stack2) > 0:
            val = stack1.pop() + stack2.pop() + carry
            carry = val // 10
            val = val % 10
            res.append(val)

        while len(stack1) > 0:
            val = stack1.pop() + carry
            carry = val // 10
            val = val % 10
            res.append(val)

        while len(stack2) > 0:
            val = stack2.pop() + carry
            carry = val // 10
            val = val % 10
            res.append(val)

        if carry > 0:
            val = carry
            res.append(val)

        head, node = None, None
        while len(res) > 0:
            val = res.pop()
            if not head:
                head = ListNode(val)
                node = head
            else:
                node.next = ListNode(val)
                node = node.next

        return head
