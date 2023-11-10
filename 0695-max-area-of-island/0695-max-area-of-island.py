class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        islands = 0

        if not grid:
            return 0

        self.max_area = 0

        self.rows = len(grid)
        self.cols = len(grid[0])

        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    islands += 1
                    self.count = 0
                    self.changeToWater(grid, i, j, self.count)

        return self.max_area
    
    def changeToWater(self, grid, i, j, count):

        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or grid[i][j] == 0:
            return
        
        grid[i][j] = 0

        self.count += 1

        self.changeToWater(grid, i + 1, j, self.count)
        self.changeToWater(grid, i - 1, j, self.count)
        self.changeToWater(grid, i, j + 1, self.count)
        self.changeToWater(grid, i, j - 1, self.count)

        self.max_area = max(self.max_area, self.count)
        