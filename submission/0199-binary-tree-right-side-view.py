# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        ret = []

        queue = [root]

        while queue:
            curr_level = []

            for _ in range(len(queue)):
                curr_node = queue.pop(0)

                curr_level.append(curr_node.val)


                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            ret.append(curr_level[-1])

        return ret

