class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from collections import Counter
        from math import factorial

        freq = Counter(s)

        half = [freq[chr(i)] // 2 for i in range(97, 123)]

        mid = ""
        for i in range(26):
            if freq[chr(i + 97)] % 2:
                mid = chr(i + 97)
                break

        n = sum(half)

        ways = factorial(n)
        for c in half:
            ways //= factorial(c)

        if ways < k:
            return ""

        result = []

        for _ in range(n):
            for i in range(26):
                if half[i] == 0:
                    continue

                count = ways * half[i] // n

                if k > count:
                    k -= count
                else:
                    result.append(chr(i + 97))
                    ways = count
                    half[i] -= 1
                    n -= 1
                    break

        first = "".join(result)

        return first + mid + first[::-1]