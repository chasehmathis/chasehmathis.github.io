class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        num_rows = len(board)
        num_cols = len(board[0])
        word_len = len(word)
        def dfs(row, col, start):
            if start == word_len:
                return True

            if row < 0 or row >= num_rows or col < 0 or col >= num_cols or board[row][col] != word[start]:
                return False

            tmp, board[row][col] = board[row][col], '/'
            cond1 = dfs(row + 1, col, start+1)
            cond2 = dfs(row -1, col, start + 1)
            cond3 = dfs(row, col +1, start + 1)
            cond4 = dfs(row, col-1, start + 1)

            found = cond1 or cond2 or cond3 or cond4

            board[row][col] = tmp

            return found

        for i in range(num_rows):
            for j in range(num_cols):
                if dfs(i, j,0):
                    return True

        return False

