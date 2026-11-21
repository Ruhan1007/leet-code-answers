class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        combined = s + "#" + rev

        lps = [0] * len(combined)

        for i in range(1, len(combined)):
            j = lps[i - 1]

            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]

            if combined[i] == combined[j]:
                j += 1

            lps[i] = j

        return rev[:len(s) - lps[-1]] + s