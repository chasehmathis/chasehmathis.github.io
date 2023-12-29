class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)


        for r in range(len(board)):
            for c in range(len(board)):
                num = board[r][c]
                if num  == '.':
                    continue


                if num in rows[r]: return False
                if num in cols[c]: return False

                if num in boxes[(r//3, c//3)]: return False


                rows[r].add(num)
                cols[c].add(num)
                boxes[(r//3, c//3)].add(num)

        return True
