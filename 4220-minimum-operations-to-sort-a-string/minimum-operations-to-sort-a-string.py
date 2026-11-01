
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        # Cannot sort an unsorted string of length 2
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # Minimum already at start or maximum at end
        if s[0] == mn or s[-1] == mx:
            return 1

        # Check whether minimum or maximum exists in the middle
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        # Minimum is only at the end and maximum only at the start
        return 3
