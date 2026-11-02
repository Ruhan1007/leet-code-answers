
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        current = []

        def backtrack(start):
            # If combination contains k numbers
            if len(current) == k:
                result.append(current[:])
                return

            # Try numbers from start to n
            for i in range(start, n + 1):
                current.append(i)

                backtrack(i + 1)

                # Backtrack: remove the last number
                current.pop()

        backtrack(1)

        return result
