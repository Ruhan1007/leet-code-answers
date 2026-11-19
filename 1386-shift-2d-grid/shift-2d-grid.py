class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        arr = [num for row in grid for num in row]

        k %= m * n
        arr = arr[-k:] + arr[:-k]

        return [arr[i:i + n] for i in range(0, m * n, n)]