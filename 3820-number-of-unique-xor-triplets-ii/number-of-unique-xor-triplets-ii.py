class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        m = 2048
        masks = []

        for b in range(11):
            block = 1 << b
            mask = 0
            for i in range(0, m, block * 2):
                mask |= ((1 << block) - 1) << i
            masks.append(mask)

        def transform(bits, x):
            b = 0
            while x:
                if x & 1:
                    block = 1 << b
                    low = bits & masks[b]
                    high = bits & (masks[b] << block)
                    bits = (low << block) | (high >> block)
                x >>= 1
                b += 1
            return bits

        dp1 = 0
        dp2 = 0
        dp3 = 0

        for x in nums:
            dp3 |= transform(dp2, x)
            dp2 |= transform(dp1, x)
            dp1 |= 1 << x

        return (dp1 | dp3).bit_count()