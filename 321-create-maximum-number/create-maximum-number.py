class Solution:
    def maxNumber(self, nums1, nums2, k):
        def get_max(nums, t):
            drop = len(nums) - t
            stack = []

            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)

            return stack[:t]

        def merge(a, b):
            result = []

            while a or b:
                if a > b:
                    result.append(a.pop(0))
                else:
                    result.append(b.pop(0))

            return result

        ans = []

        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            a = get_max(nums1, i)
            b = get_max(nums2, k - i)
            candidate = merge(a[:], b[:])
            ans = max(ans, candidate)

        return ans