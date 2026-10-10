# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        p_queue = deque([p]) if p else None
        q_queue = deque([q]) if q else None

        while p_queue and q_queue:

            p_node = p_queue.popleft()
            q_node = q_queue.popleft()
            # print(p_node.val , q_node.val)
            if p_node and q_node and p_node.val == q_node.val :

                if p_node.left or q_node.left:
                    p_queue.append(p_node.left) 
                    q_queue.append(q_node.left)
    
                if p_node.right or q_node.right:
                    p_queue.append(p_node.right)
                    q_queue.append(q_node.right)

            else :
                return False
        if p_queue or q_queue:
            return False

        else:
            return True

        