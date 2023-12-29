class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []


        def dfs(path, remaining):
            if not remaining:
                res.append(path.copy())
                return

            for i in range(len(remaining)):
                path.append(remaining[i])

                dfs(path, remaining[:i] + remaining[i + 1:])

                path.pop()


        dfs([], nums)
        return res
