# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def wrapper(node):
            if not node:
                return True, -1

            left_balance, left_height = wrapper(node.left)
            if not left_balance:
                return False, 0

            right_balance, right_height = wrapper(node.right)
            if not right_balance:
                return False, 0

            balanced = abs(left_height - right_height) <=1
            height = max(left_height, right_height) + 1

            return balanced, height
        return wrapper(root)[0]
       
