class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                a, b = num[:i], num[i:j]

                if len(a) > 1 and a[0] == '0':
                    break

                if len(b) > 1 and b[0] == '0':
                    continue

                x, y = int(a), int(b)
                k = j

                while k < n:
                    s = str(x + y)

                    if not num.startswith(s, k):
                        break

                    k += len(s)
                    x, y = y, x + y

                if k == n:
                    return True

        return False