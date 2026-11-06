from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda log: log[1])
        ordered_queries = sorted((q, i) for i, q in enumerate(queries))
        
        freq = defaultdict(int)
        active = 0
        left = right = 0
        ans = [0] * len(queries)
        
        for q, idx in ordered_queries:
            low = q - x
            
            # Expand window: add logs with time <= q
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                if freq[server] == 0:
                    active += 1
                freq[server] += 1
                right += 1
            
            # Shrink window: remove logs with time < q - x
            while left < len(logs) and logs[left][1] < low:
                server = logs[left][0]
                freq[server] -= 1
                if freq[server] == 0:
                    active -= 1
                left += 1
            
            ans[idx] = n - active
        
        return ans