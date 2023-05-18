"""
104. Maximum Depth of Binary Tree
1. bfs
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        queue = deque([(root, 1)])
        max_depth = 0
        while queue:
            cur, depth = queue.popleft()

            if depth > max_depth:
                max_depth = depth

            if cur.left is not None:
                queue.append((cur.left, depth + 1))

            if cur.right is not None:
                queue.append((cur.right, depth + 1))

        return max_depth


"""
2. recursive
"""


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
