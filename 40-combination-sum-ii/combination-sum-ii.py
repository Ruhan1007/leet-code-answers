
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        result = []
        current = []

        candidates.sort()

        def backtrack(start, total):

            # Target reached
            if total == target:
                result.append(current.copy())
                return

            for i in range(start, len(candidates)):

                # Skip duplicate elements at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # No need to continue if sum exceeds target
                if total + candidates[i] > target:
                    break

                # Choose current number
                current.append(candidates[i])

                # Move to next index (each number used once)
                backtrack(i + 1, total + candidates[i])

                # Backtrack
                current.pop()

        backtrack(0, 0)

        return result
