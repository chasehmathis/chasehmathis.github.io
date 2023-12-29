class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        candidates.sort()
        res = []
        def dfs(i, path, target):
            
            if target < 0:
                return
            if target == 0:
                res.append(path.copy())
                return

            for j in range(i, len(candidates)):
                if j> i and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])
                dfs(j + 1, path, target - candidates[j])
                path.pop()
        dfs(0, [], target)
        return res
