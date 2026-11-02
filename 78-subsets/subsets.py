
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        current = []

        def backtrack(start):
            # Add the current subset to the result
            result.append(current[:])

            # Explore remaining elements
            for i in range(start, len(nums)):
                current.append(nums[i])

                backtrack(i + 1)

                # Backtrack
                current.pop()

        backtrack(0)

        return result
