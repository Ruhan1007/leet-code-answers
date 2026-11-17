class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter

        freq = Counter(s)

        first = []
        mid = ""

        for ch in sorted(freq):
            first.append(ch * (freq[ch] // 2))

            if freq[ch] % 2:
                mid = ch

        left = "".join(first)

        return left + mid + left[::-1]