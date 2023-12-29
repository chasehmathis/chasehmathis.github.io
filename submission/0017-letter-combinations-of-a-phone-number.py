class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        from collections import defaultdict
        letters = "abcdefghijklmnopqrstuvwxyz"
        d = defaultdict(list)

        d['2'] = list('abc') 
        d['3'] = list('def')
        d['4'] = list('ghi') 
        d['5'] = list('jkl')
        d['6'] = list('mno')
        d['7'] = list('pqrs')
        d['8'] = list('tuv')
        d['9'] = list('wxyz')

        lst = [d[digit] for digit in digits]
        res = []
        def dfs(lst, j, comb):
            if j == len(digits):
                return comb

            for i in range(len(lst[j])):
                take = dfs(lst, j + 1, comb + lst[j][i])
                if take is not None:
                    res.append(take)



        dfs(lst, 0, "")

        return res

            

