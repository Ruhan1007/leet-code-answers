
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # Check all 9 rows and columns
        for i in range(9):

            row = set()
            col = set()

            for j in range(9):

                # Check row
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])

                # Check column
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])

        # Check all 3 x 3 sub-boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                box = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):

                        if board[i][j] != '.':
                            if board[i][j] in box:
                                return False

                            box.add(board[i][j])

        return True
