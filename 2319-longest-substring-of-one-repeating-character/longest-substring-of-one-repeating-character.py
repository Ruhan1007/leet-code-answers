class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        size = 1
        while size < n:
            size *= 2

        tree = [None] * (2 * size)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            lc, rc, pref, suff, best, length = a
            lc2, rc2, pref2, suff2, best2, length2 = b

            new_pref = pref
            new_suff = suff2
            new_best = max(best, best2)

            if rc == lc2:
                new_best = max(new_best, suff + pref2)

                if pref == length:
                    new_pref = length + pref2

                if suff2 == length2:
                    new_suff = length2 + suff

            return (lc, rc2, new_pref, new_suff, new_best, length + length2)

        for i, c in enumerate(s):
            tree[size + i] = (c, c, 1, 1, 1, 1)

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        ans = []

        for c, idx in zip(queryCharacters, queryIndices):
            pos = size + idx
            tree[pos] = (c, c, 1, 1, 1, 1)

            pos //= 2

            while pos:
                tree[pos] = merge(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

            ans.append(tree[1][4])

        return ans