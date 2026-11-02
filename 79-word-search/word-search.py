class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(row, col, index):
            # All characters of the word are matched
            if index == len(word):
                return True

            # Check boundaries and character match
            if (row < 0 or row >= m or
                col < 0 or col >= n or
                board[row][col] != word[index]):
                return False

            # Temporarily mark the cell as visited
            temp = board[row][col]
            board[row][col] = "#"

            # Explore all four directions
            found = (
                dfs(row + 1, col, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row, col - 1, index + 1)
            )

            # Restore the original character
            board[row][col] = temp

            return found

        # Try starting from every cell
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
