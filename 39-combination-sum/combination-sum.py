
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        result = []
        current = []

        def backtrack(start, total):

            # Target reached
            if total == target:
                result.append(current.copy())
                return

            # Target exceeded
            if total > target:
                return

            for i in range(start, len(candidates)):

                current.append(candidates[i])

                # i instead of i + 1 because reuse is allowed
                backtrack(i, total + candidates[i])

                # Backtrack
                current.pop()

        backtrack(0, 0)

        return result
