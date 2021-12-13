'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''


class Node:
    def __init__(self, level, node):
        self.level = level
        self.node = node
        self.val = self.node.val
        self.left = self.node.left
        self.right = self.node.right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        lookup = {}
        result = []
        queue = deque()
        queue.append(Node(0, root))
        while queue:
            node = queue.popleft()
            if node.level not in lookup: lookup[node.level] = []
            lookup[node.level].append(node.val)
            if node.left: queue.append(Node(node.level + 1, node.left))
            if node.right: queue.append(Node(node.level + 1, node.right))
        return lookup.values()