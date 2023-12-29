# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = [root]
        ret = []
        while queue:
            curr_level = []
            level_size = len(queue) # i.e. how many are at that height

            for _ in range(level_size):
                curr_node = queue.pop(0) # get the last one on 

                curr_level.append(curr_node.val) # append it to curr_level

                # get the left and right children on the queue
                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)

            ret.append(curr_level)

        result = []

        return ret



