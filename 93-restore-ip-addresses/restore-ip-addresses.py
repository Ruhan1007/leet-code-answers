class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    result.append('.'.join(parts))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break
                segment = s[start:start + length]
                if len(segment) > 1 and segment[0] == '0':
                    break
                if int(segment) > 255:
                    break
                parts.append(segment)
                backtrack(start + length, parts)
                parts.pop()

        backtrack(0, [])
        return result