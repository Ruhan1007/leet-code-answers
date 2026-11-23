class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        @lru_cache(None)
        def solve(expr):
            result = []

            for i, ch in enumerate(expr):
                if ch in '+-*':
                    left = solve(expr[:i])
                    right = solve(expr[i + 1:])

                    for a in left:
                        for b in right:
                            if ch == '+':
                                result.append(a + b)
                            elif ch == '-':
                                result.append(a - b)
                            else:
                                result.append(a * b)

            if not result:
                return [int(expr)]

            return result

        return solve(expression)