
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        primes = [2, 3, 5, 7]
        target = [0, 0, 0, 0]

        for i, p in enumerate(primes):
            while t % p == 0:
                target[i] += 1
                t //= p

        if t > 1:
            return "-1"

        factors = [
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (2, 0, 0, 0),
            (0, 0, 1, 0),
            (1, 1, 0, 0),
            (0, 0, 0, 1),
            (3, 0, 0, 0),
            (0, 2, 0, 0)
        ]

        A, B = target[0], target[1]
        dp = [[0] * (B + 1) for _ in range(A + 1)]

        for a in range(A + 1):
            for b in range(B + 1):
                if a == 0 and b == 0:
                    continue

                best = float('inf')

                for x, y in [
                    (1, 0), (0, 1), (2, 0),
                    (1, 1), (3, 0), (0, 2)
                ]:
                    na = max(0, a - x)
                    nb = max(0, b - y)

                    if na == a and nb == b:
                        continue

                    best = min(best, 1 + dp[na][nb])

                dp[a][b] = best

        def need(a, b, c, d):
            return dp[a][b] + c + d

        def get_factors(d):
            if d == 1:
                return (0, 0, 0, 0)
            return factors[d - 2]

        def build(a, b, c, d, length):
            result = ['1'] * (length - need(a, b, c, d))

            while a or b or c or d:
                current = need(a, b, c, d)

                for digit in range(2, 10):
                    x, y, z, w = get_factors(digit)

                    na = max(0, a - x)
                    nb = max(0, b - y)
                    nc = max(0, c - z)
                    nd = max(0, d - w)

                    if need(na, nb, nc, nd) == current - 1:
                        result.append(str(digit))
                        a, b, c, d = na, nb, nc, nd
                        break

            return ''.join(result)

        total = [0, 0, 0, 0]
        zeros = 0

        for ch in num:
            digit = int(ch)

            if digit == 0:
                zeros += 1
            else:
                for j, p in enumerate(primes):
                    while digit % p == 0:
                        total[j] += 1
                        digit //= p

        if zeros == 0 and all(
            total[i] >= target[i] for i in range(4)
        ):
            return num

        n = len(num)

        for i in range(n - 1, -1, -1):
            digit = int(num[i])

            if digit == 0:
                zeros -= 1
            else:
                for j, p in enumerate(primes):
                    while digit % p == 0:
                        total[j] -= 1
                        digit //= p

            if zeros:
                continue

            for d in range(max(1, int(num[i]) + 1), 10):
                x, y, z, w = get_factors(d)

                remaining = [
                    max(0, target[0] - total[0] - x),
                    max(0, target[1] - total[1] - y),
                    max(0, target[2] - total[2] - z),
                    max(0, target[3] - total[3] - w)
                ]

                length = n - i - 1

                if need(*remaining) <= length:
                    return (
                        num[:i] + str(d) +
                        build(*remaining, length)
                    )

        length = max(n + 1, need(*target))

        return build(*target, length)
