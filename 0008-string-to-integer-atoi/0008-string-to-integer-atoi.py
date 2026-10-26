class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # Step 1: Ignore leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Determine sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Step 3: Convert digits manually
        result = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            # Step 4: Check overflow before updating result
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result