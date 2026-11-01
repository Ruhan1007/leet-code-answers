
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        board = [['.' for _ in range(n)] for _ in range(n)]

        cols = set()
        diagonals = set()
        anti_diagonals = set()

        def backtrack(row):
            # All queens have been placed
            if row == n:
                result.append([''.join(r) for r in board])
                return

            for col in range(n):

                # Check if this position is under attack
                if col in cols:
                    continue

                if (row - col) in diagonals:
                    continue

                if (row + col) in anti_diagonals:
                    continue

                # Place the queen
                board[row][col] = 'Q'

                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)

                # Move to the next row
                backtrack(row + 1)

                # Backtrack: remove the queen
                board[row][col] = '.'

                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

        backtrack(0)

        return result
