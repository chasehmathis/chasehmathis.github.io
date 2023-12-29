# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return root

        curr_val = root.val

        if p.val < curr_val and q.val < curr_val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if q.val > curr_val and p.val > curr_val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root
