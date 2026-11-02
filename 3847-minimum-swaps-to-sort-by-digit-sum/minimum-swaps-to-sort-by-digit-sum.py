class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        n = len(nums)

        # Sort based on digit sum, then number
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Store the original index of each number
        index = {num: i for i, num in enumerate(nums)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or index[sorted_nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = index[sorted_nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps