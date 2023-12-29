class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_rows = set()
        zero_cols = set()
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        
        for r in zero_rows:
            matrix[r] = [0 for _ in range(n)]

        for c in zero_cols:
            for r in range(m):
                matrix[r][c] = 0
        return matrix
