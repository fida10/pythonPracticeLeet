# 1351. Count Negative Numbers in a Sorted Matrix
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Solution#1
        count = 0
        for each in grid:
            for j in each:
                if j < 0:
                    count += 1
        return count
        """
       #Solution#2 
        row= len(grid)
        columns = len(grid[0])
        count = 0
        for i in range(0, row):
            for j in range(0, columns):

                if grid[i][j] < 0:
                    count += 1 
        return(count)"""


