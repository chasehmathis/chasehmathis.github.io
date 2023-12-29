# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            curr, lower, upper = stack.pop()
            
            if not curr:
                continue
            val = curr.val
            if val <= lower or val >= upper:
                return False


            stack.append((curr.left, lower, val))
            stack.append((curr.right, val, upper))

        return True

