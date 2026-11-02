class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        # Scan the grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4

                    # Check down cell
                    if i+1 < rows and grid[i+1][j] == 1:
                        perimeter -=2
                    
                    # Check right cell
                    if j+1 < cols and grid[i][j+1] == 1:
                        perimeter -= 2

        return perimeter 


# Every land cell contributes 4 to the perimeter and for every adjacent land cell,
# i.e, right cell or down cell, 2 is subtracted from the perimeter