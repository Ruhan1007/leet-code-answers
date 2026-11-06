class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        
        best = [INF] * n
        prefix = 0
        left = 0
        min_len = INF
        
        for right in range(n):
            prefix += arr[right]
            while prefix > target:
                prefix -= arr[left]
                left += 1
            if prefix == target:
                length = right - left + 1
                min_len = min(min_len, length)
            best[right] = min_len
        
        result = INF
        prefix = 0
        left = 0
        
        for right in range(n):
            prefix += arr[right]
            while prefix > target:
                prefix -= arr[left]
                left += 1
            if prefix == target:
                length = right - left + 1
                if left > 0 and best[left - 1] != INF:
                    result = min(result, length + best[left - 1])
        
        return result if result != INF else -1