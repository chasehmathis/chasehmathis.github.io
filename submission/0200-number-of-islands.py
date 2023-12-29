class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        
        def bfs(r, c):


            q = collections.deque([(r,c)])
            grid[r][c] = '0' # set to zero instead of visit
            
            # can move in four directions
            # Left, down, right, up
            directions = [[-1, 0], [0,-1], [0,1], [1,0]]


            while q:
                r,c = q.popleft()
                
                for dr, dc in directions:
                    # run bfs on the moving in these directions
                    nr, nc = dr + r, dc + c
    
                    outOfBounds = (nr < 0 or nr >= rows) or (nc < 0 or nc >= cols)
                    if not outOfBounds and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                # if there is land else do nothing
                if grid[r][c] == '1':
                    bfs(r,c)
                    islands += 1

        return islands
