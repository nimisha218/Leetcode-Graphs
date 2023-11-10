class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def changeToWater(grid, i, j):

            # 1) i < 0 or i >= rows
            # 2) j < 0 or j >= cols
            # 3) grid[i][j] == 0 
            
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            changeToWater(grid, i + 1, j)
            changeToWater(grid, i - 1, j)
            changeToWater(grid, i, j + 1)
            changeToWater(grid, i, j - 1)

        islands = 0

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    changeToWater(grid, i, j)
        
        return islands

        
        