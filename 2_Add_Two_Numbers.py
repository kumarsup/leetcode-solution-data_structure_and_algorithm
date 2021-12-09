class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return l1

        res = ListNode(-1)
        curr = res

        i, j, val, carry = 0, 0, 0, 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            node = ListNode(val)
            curr.next = node
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res.next