
class Solution:
    def createGrid(self, m: int, n: int):
        
        # Fill the grid with obstacles
        grid = [['#'] * n for _ in range(m)]

        # Open the first row
        for j in range(n):
            grid[0][j] = '.'

        # Open the last column
        for i in range(m):
            grid[i][n - 1] = '.'

        # Convert each row into a string
        return [''.join(row) for row in grid]
