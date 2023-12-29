class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:


        def dfs(i, path, target, ret):
            if target < 0 or i >= len(candidates):
                return

            if target == 0:
                ret.append(path.copy())
                return

            path.append(candidates[i])
            dfs(i, path, target - candidates[i], ret)
            path.pop()
            dfs(i + 1, path, target, ret)

        ret = []

        dfs(0, [], target, ret)
        return ret
