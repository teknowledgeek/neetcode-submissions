# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        cur = root
        stack = deque()
        stack.append(cur)

        while cur or stack:
            while cur:

                stack.append(cur)
                cur = cur.left                
            
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val

            cur = cur.right 