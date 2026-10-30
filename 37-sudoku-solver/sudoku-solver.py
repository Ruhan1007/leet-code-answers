
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        # Initialize sets with existing numbers
        for r in range(9):
            for c in range(9):

                num = board[r][c]
                box = (r // 3) * 3 + (c // 3)

                if num == '.':
                    empty.append((r, c))
                else:
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        digits = "123456789"

        def solve(k):

            if k == len(empty):
                return True

            # Find the empty cell with the fewest candidates
            best = k
            min_options = 10

            for i in range(k, len(empty)):

                r, c = empty[i]
                box = (r // 3) * 3 + (c // 3)

                used = rows[r] | cols[c] | boxes[box]

                options = [
                    num for num in digits
                    if num not in used
                ]

                if len(options) < min_options:
                    min_options = len(options)
                    best = i

                if min_options == 0:
                    return False

                if min_options == 1:
                    break

            # Swap the best cell into the current position
            empty[k], empty[best] = empty[best], empty[k]

            r, c = empty[k]
            box = (r // 3) * 3 + (c // 3)

            used = rows[r] | cols[c] | boxes[box]

            for num in digits:

                if num not in used:

                    # Place number
                    board[r][c] = num

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

                    if solve(k + 1):
                        return True

                    # Backtrack
                    board[r][c] = '.'

                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box].remove(num)

            # Restore empty-cell ordering
            empty[k], empty[best] = empty[best], empty[k]

            return False

        solve(0)
