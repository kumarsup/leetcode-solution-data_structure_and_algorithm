'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right,
then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
'''

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        lookup = {}
        queue = deque([(0, root)])
        while queue:
            level, node = queue.popleft()
            if level not in lookup: lookup[level] = []
            if not level % 2: lookup[level].append(node.val)
            if level % 2: lookup[level].insert(0, node.val)
            if node.left: queue.append((level + 1, node.left))
            if node.right: queue.append((level + 1, node.right))
        return lookup.values()