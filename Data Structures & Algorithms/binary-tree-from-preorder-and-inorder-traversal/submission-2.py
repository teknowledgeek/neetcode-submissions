   # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Map values to their indices in the inorder array
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Track our current position in the preorder array
        pre_idx = 0
        
        def helper(left_in, right_in):
            nonlocal pre_idx
            
            # Base case: if there are no elements to construct the subtree
            if left_in > right_in:
                return None
            
            # Select the current root value from preorder
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
            
            # Split the inorder array into left and right subtrees
            mid = inorder_map[root_val]
            
            # Crucial order: must build left child first
            root.left = helper(left_in, mid - 1)
            root.right = helper(mid + 1, right_in)
            
            return root
            
        return helper(0, len(inorder) - 1)
        