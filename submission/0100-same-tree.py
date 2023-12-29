# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def wrapper(x, y):
            if x is None and y is None:
                return True
            if x is None or y is None:
                return False

            if x.val != y.val:
                return False
            

            left = wrapper(x.left, y.left)
            right = wrapper(x.right, y.right)

            return left and right

        return wrapper(p, q)

        
