class Solution:
    def countRangeSum(self, nums, lower, upper):
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        def merge_sort(arr):
            if len(arr) <= 1:
                return 0

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            count = merge_sort(left) + merge_sort(right)

            j = k = 0

            for x in left:
                while j < len(right) and right[j] - x < lower:
                    j += 1
                while k < len(right) and right[k] - x <= upper:
                    k += 1
                count += k - j

            arr[:] = sorted(left + right)
            return count

        return merge_sort(prefix)