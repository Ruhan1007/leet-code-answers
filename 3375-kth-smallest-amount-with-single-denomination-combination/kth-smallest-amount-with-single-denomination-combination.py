class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        def lcm(a, b):
            return a // gcd(a, b) * b
        
        def count(x):
            total = 0
            for mask in range(1, 1 << n):
                l = 1
                bits = 0
                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        l = lcm(l, coins[i])
                        if l > x:
                            break
                if l <= x:
                    if bits % 2 == 1:
                        total += x // l
                    else:
                        total -= x // l
            return total
        
        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo