class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sorted_pairs = sorted((val, i) for i, val in enumerate(nums))
        
        result = [0] * n
        group_start = 0
        
        for k in range(n + 1):
            if k == n or sorted_pairs[k][0] - sorted_pairs[k - 1][0] > limit:
                group = sorted_pairs[group_start:k]
                indices = sorted(idx for _, idx in group)
                values = [val for val, _ in group]
                for idx, val in zip(indices, values):
                    result[idx] = val
                group_start = k
        
        return result